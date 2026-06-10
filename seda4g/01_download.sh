#!/bin/bash
# 01_download.sh — download NTIA SBDD / NBM data + Census block populations
# for the seda4g build. All raw data goes to data/external/seda4g/ (gitignored).
#
# NATIONAL mode (default): 50 states + DC, all 9 SBDD waves (Jun-2010 ... Jun-2014)
# plus 2010 + 2000 PL94-171 block populations for every state. ~12-15 GB of zips;
# 02_build_exposure.py deletes non-pilot state-wave zips after caching county
# aggregates, so steady-state disk stays well under 20 GB.
#
# Usage:
#   ./01_download.sh              # everything (census + all 9 waves + extras)
#   ./01_download.sh census       # census PL files only
#   ./01_download.sh 2012-06      # one SBDD wave only (all 51 states)
#   ./01_download.sh extras       # analyze tables, FCC477 pilot files, SEDA, RUCC
#
# Idempotent: skips zips that already exist AND state-waves already processed
# (build cache cov2_<ST>_<wave>.csv present). Failures are appended to
# $DATA/download_failures.log (one line per file) and do not stop the run.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data/external/seda4g"
BUILD="$DATA/build"
FAILLOG="$DATA/download_failures.log"
mkdir -p "$DATA/states" "$DATA/census" "$DATA/fcc477" "$BUILD"

NTIA="https://www2.ntia.gov/files/broadband-data"
PILOT="DE CO MS OH WA TX MA MT"
STATES="AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY"
WAVES="2010-06 2010-12 2011-06 2011-12 2012-06 2012-12 2013-06 2013-12 2014-06"
NJOBS=6

stname () {  # postal -> census directory name
  case "$1" in
    AL) echo Alabama;; AK) echo Alaska;; AZ) echo Arizona;; AR) echo Arkansas;;
    CA) echo California;; CO) echo Colorado;; CT) echo Connecticut;;
    DE) echo Delaware;; DC) echo District_of_Columbia;; FL) echo Florida;;
    GA) echo Georgia;; HI) echo Hawaii;; ID) echo Idaho;; IL) echo Illinois;;
    IN) echo Indiana;; IA) echo Iowa;; KS) echo Kansas;; KY) echo Kentucky;;
    LA) echo Louisiana;; ME) echo Maine;; MD) echo Maryland;;
    MA) echo Massachusetts;; MI) echo Michigan;; MN) echo Minnesota;;
    MS) echo Mississippi;; MO) echo Missouri;; MT) echo Montana;;
    NE) echo Nebraska;; NV) echo Nevada;; NH) echo New_Hampshire;;
    NJ) echo New_Jersey;; NM) echo New_Mexico;; NY) echo New_York;;
    NC) echo North_Carolina;; ND) echo North_Dakota;; OH) echo Ohio;;
    OK) echo Oklahoma;; OR) echo Oregon;; PA) echo Pennsylvania;;
    RI) echo Rhode_Island;; SC) echo South_Carolina;; SD) echo South_Dakota;;
    TN) echo Tennessee;; TX) echo Texas;; UT) echo Utah;; VT) echo Vermont;;
    VA) echo Virginia;; WA) echo Washington;; WV) echo West_Virginia;;
    WI) echo Wisconsin;; WY) echo Wyoming;;
  esac
}

# SBDD zip name per wave (verified against the live NTIA archive 2026-06-10),
# plus an alternate naming scheme to try on 404.
zipname () { # zipname <wave> <ST>
  case "$1" in
    2010-06) echo "SBDD_${2}_Fall2010.zip";;
    2010-12) echo "${2}-NBM-CSV-December-2010.zip";;
    2011-06) echo "${2}-NBM-CSV-June-2011.zip";;
    2011-12) echo "${2}-NBM-CSV-December-2011.zip";;
    2012-06) echo "${2}-NBM-CSV-June-2012.zip";;
    2012-12) echo "${2}-NBM-CSV-Dec-2012.zip";;
    2013-06) echo "${2}-NBM-CSV-June-2013.zip";;
    2013-12) echo "${2}-NBM-CSV-Dec-2013.zip";;
    2014-06) echo "${2}-NBM-CSV-June-2014.zip";;
  esac
}
zipname_alt () { # alternate scheme (Dec<->December, June<->Jun)
  case "$1" in
    2010-06) echo "${2}-NBM-CSV-June-2010.zip";;
    2010-12) echo "${2}-NBM-CSV-Dec-2010.zip";;
    2011-06) echo "${2}-NBM-CSV-Jun-2011.zip";;
    2011-12) echo "${2}-NBM-CSV-Dec-2011.zip";;
    2012-06) echo "${2}-NBM-CSV-Jun-2012.zip";;
    2012-12) echo "${2}-NBM-CSV-December-2012.zip";;
    2013-06) echo "${2}-NBM-CSV-Jun-2013.zip";;
    2013-12) echo "${2}-NBM-CSV-December-2013.zip";;
    2014-06) echo "${2}-NBM-CSV-Jun-2014.zip";;
  esac
}

# fetch worker: $1=primary-url $2=dest [$3=alternate-url]; .part + rename so a
# killed run never leaves a truncated file that would be skipped as complete.
fetch () {
  url="$1"; dest="$2"; alt="${3:-}"
  [ "$alt" = "-" ] && alt=""   # "-" = no-alternate sentinel (BSD xargs -0 drops empty tokens)
  [ -s "$dest" ] && return 0
  curl -sfL --retry 3 --retry-delay 5 --connect-timeout 30 "$url" -o "$dest.part" \
    && mv "$dest.part" "$dest" && { echo "GET  $(basename "$dest")"; return 0; }
  rm -f "$dest.part"
  if [ -n "$alt" ]; then
    curl -sfL --retry 3 --retry-delay 5 --connect-timeout 30 "$alt" -o "$dest.part" \
      && mv "$dest.part" "$dest" && { echo "GET* $(basename "$dest") (alt name)"; return 0; }
    rm -f "$dest.part"
  fi
  echo "FAILED $(basename "$dest") $url" | tee -a "$FAILLOG" >&2
  return 1
}
export -f fetch
export FAILLOG

# queue runner: reads NUL-separated url/dest/alt token triples on stdin,
# runs NJOBS parallel fetches. NUL-delimited because paths contain spaces.
run_queue () {
  xargs -0 -P "$NJOBS" -n 3 bash -c 'fetch "$0" "$1" "$2"'
}

dl_wave () { # dl_wave <wave>
  W="$1"
  echo "== SBDD wave $W =="
  for ST in $STATES; do
    Z=$(zipname "$W" "$ST"); A=$(zipname_alt "$W" "$ST")
    # skip if zip present or this state-wave already processed into the cache
    if [ -s "$DATA/states/$Z" ] || [ -s "$BUILD/cov2_${ST}_${W}.csv" ]; then
      continue
    fi
    printf '%s\0%s\0%s\0' "$NTIA/$Z" "$DATA/states/$Z" "$NTIA/$A"
  done | run_queue
}

dl_census () {
  echo "== Census PL94-171 block populations (2010 + 2000), all states =="
  for ST in $STATES; do
    st=$(echo "$ST" | tr 'A-Z' 'a-z'); NM=$(stname "$ST")
    # 2010 PL (block POP100 in geo header, SUMLEV 750)
    [ -s "$DATA/census/${st}2010.pl.zip" ] || [ -s "$BUILD/blockpop2010_${st}.csv.gz" ] || \
      printf '%s\0%s\0%s\0' \
        "https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/$NM/${st}2010.pl.zip" \
        "$DATA/census/${st}2010.pl.zip" "-"
    # 2000 PL (for the two 2010-wave files on 2000 blocks): geo + part 1
    [ -s "$DATA/census/${st}geo.upl.zip" ] || [ -s "$BUILD/blockpop2000_${st}.csv.gz" ] || \
      printf '%s\0%s\0%s\0' \
        "https://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/$NM/${st}geo.upl.zip" \
        "$DATA/census/${st}geo.upl.zip" "-"
    [ -s "$DATA/census/${st}00001.upl.zip" ] || [ -s "$BUILD/blockpop2000_${st}.csv.gz" ] || \
      printf '%s\0%s\0%s\0' \
        "https://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/$NM/${st}00001.upl.zip" \
        "$DATA/census/${st}00001.upl.zip" "-"
  done | run_queue
}

dl_extras () {
  # --- NBM Analyze Tables (validation only — they leak fixed wireless; 7 of 9
  #     waves exist; none for June-2010 / December-2010) ---
  for W in June-2011 December-2011 June-2012 December-2012 June-2013 Dec-2013 June-2014; do
    fetch "$NTIA/All-NBM-Analyze-Table-$W.zip" "$DATA/All-NBM-Analyze-Table-$W.zip"
    (cd "$DATA" && unzip -o -q "All-NBM-Analyze-Table-$W.zip" 2>/dev/null)
  done

  # --- FCC Form 477 mobile deployment, Dec 2015 centroid-method block CSV ---
  # fcc.gov blocks scripted access; Box shared links recovered from the
  # Wayback snapshot of fcc.gov/mobile-deployment-form-477-data.
  SN="ysnymj6besnrjtaewo6v8hs3v3615sng"
  BOXDL="https://us-fcc.app.box.com/index.php?rm=box_download_shared_file&shared_name=$SN"
  UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
  f477 () { # f477 <file_id> <ST>
    d="$DATA/fcc477/F477_2015_12_Centroid_State_$2.zip"
    if [ -s "$d" ]; then echo "skip $(basename "$d")"; else
      echo "GET F477 $2"; curl -sL -A "$UA" "$BOXDL&file_id=f_$1" -o "$d"
    fi
  }
  f477 210708596892 MT
  f477 210708595100 MS
  f477 210708597404 MA
  f477 210708593564 TX

  # --- SEDA 5.0 county long file (CS scale) — direct, no registration ---
  fetch "https://stacks.stanford.edu/file/druid:cs829jn7849/seda_county_long_cs_5.0.csv" \
        "$DATA/seda_county_long_cs_5.0.csv"

  # --- USDA ERS Rural-Urban Continuum Codes 2013 ---
  fetch "https://ers.usda.gov/sites/default/files/_laserfiche/DataFiles/53251/ruralurbancodes2013.xls" \
        "$DATA/ruralurbancodes2013.xls"
}

case "${1:-all}" in
  census) dl_census ;;
  extras) dl_extras ;;
  all)    dl_census; for W in $WAVES; do dl_wave "$W"; done; dl_extras ;;
  *)      dl_wave "$1" ;;
esac
echo "done."
