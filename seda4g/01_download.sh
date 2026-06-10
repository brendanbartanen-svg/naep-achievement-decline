#!/bin/bash
# 01_download.sh — download NTIA SBDD / NBM data + Census block populations
# for the seda4g validation exercise. All raw data goes to data/external/seda4g/
# (gitignored). Total ~1 GB. Idempotent: skips files that already exist.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data/external/seda4g"
mkdir -p "$DATA/states" "$DATA/census" "$DATA/fcc477"

NTIA="https://www2.ntia.gov/files/broadband-data"
PILOT="DE CO MS OH WA TX MA MT"

get () { # get <url> <dest>
  if [ -s "$2" ]; then echo "skip $(basename "$2")"; else
    echo "GET $(basename "$2")"; curl -sfL "$1" -o "$2" || echo "FAILED: $1"
  fi
}

# --- 1. NBM Analyze Tables (pre-built geographic summaries; 7 of 9 waves exist;
#         NO analyze table for June-2010 or December-2010) ---
for W in June-2011 December-2011 June-2012 December-2012 June-2013 Dec-2013 June-2014; do
  get "$NTIA/All-NBM-Analyze-Table-$W.zip" "$DATA/All-NBM-Analyze-Table-$W.zip"
  (cd "$DATA" && unzip -o -q "All-NBM-Analyze-Table-$W.zip")
done

# --- 2. Per-state NBM CSV zips for pilot states ---
# June 2010 wave (2000 census blocks):   SBDD_XX_Fall2010.zip
# December 2010 wave (2000 census blocks): XX-NBM-CSV-December-2010.zip
# June 2014 wave (2010 census blocks):   XX-NBM-CSV-June-2014.zip
for ST in $PILOT; do
  get "$NTIA/SBDD_${ST}_Fall2010.zip"          "$DATA/states/SBDD_${ST}_Fall2010.zip"
  get "$NTIA/${ST}-NBM-CSV-December-2010.zip"  "$DATA/states/${ST}-NBM-CSV-December-2010.zip"
  get "$NTIA/${ST}-NBM-CSV-June-2014.zip"      "$DATA/states/${ST}-NBM-CSV-June-2014.zip"
done
# Dec-2012 wave for 4 states only (fixed-wireless leakage check at mid-rollout)
for ST in MT MS CO MA; do
  get "$NTIA/${ST}-NBM-CSV-Dec-2012.zip" "$DATA/states/${ST}-NBM-CSV-Dec-2012.zip"
done

# --- 3. Census PL94-171 block populations ---
# (bash 3.2 on macOS: no associative arrays)
stname () {
  case "$1" in
    DE) echo Delaware;;   CO) echo Colorado;;  MS) echo Mississippi;;
    OH) echo Ohio;;       WA) echo Washington;; TX) echo Texas;;
    MA) echo Massachusetts;; MT) echo Montana;;
  esac
}
for ST in $PILOT; do
  st=$(echo "$ST" | tr 'A-Z' 'a-z'); NM=$(stname "$ST")
  # 2010 PL (block POP100 in geo header, SUMLEV 750)
  get "https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/$NM/${st}2010.pl.zip" \
      "$DATA/census/${st}2010.pl.zip"
  # 2000 PL (for the two 2010-wave files on 2000 blocks): geo + part 1 (P0010001)
  get "https://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/$NM/${st}geo.upl.zip" \
      "$DATA/census/${st}geo.upl.zip"
  get "https://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/$NM/${st}00001.upl.zip" \
      "$DATA/census/${st}00001.upl.zip"
done

# --- 5. FCC Form 477 mobile deployment, Dec 2015 centroid-method block CSV ---
# fcc.gov blocks scripted access; Box shared links recovered from the
# Wayback snapshot of fcc.gov/mobile-deployment-form-477-data.
# Shared folder ("Centroid Methodology" -> "By State"):
#   https://us-fcc.box.com/s/ysnymj6besnrjtaewo6v8hs3v3615sng
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

# --- 6. SEDA 5.0 county long file (CS scale) — direct, no registration ---
get "https://stacks.stanford.edu/file/druid:cs829jn7849/seda_county_long_cs_5.0.csv" \
    "$DATA/seda_county_long_cs_5.0.csv"

# --- 7. USDA ERS Rural-Urban Continuum Codes 2013 ---
get "https://ers.usda.gov/sites/default/files/_laserfiche/DataFiles/53251/ruralurbancodes2013.xls" \
    "$DATA/ruralurbancodes2013.xls"

echo "done."
