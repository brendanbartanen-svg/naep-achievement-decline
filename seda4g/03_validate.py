#!/usr/bin/env python3
"""
03_validate.py — four-way validation of the SBDD-derived county 4G exposure
measure, plus diagnostics. Reads intermediates from 02_build_exposure.py.

FCC Form 477 Dec-2015 mobile centroid-method CSVs were fetched from the FCC
Box account (fcc.gov blocks scripted access; links recovered from the archived
page https://www.fcc.gov/mobile-deployment-form-477-data):
  folder https://us-fcc.box.com/s/ysnymj6besnrjtaewo6v8hs3v3615sng ("By State")
  files downloaded via
  https://us-fcc.app.box.com/index.php?rm=box_download_shared_file&shared_name=
  ysnymj6besnrjtaewo6v8hs3v3615sng&file_id=f_<id>
  MT=f_210708596892 MS=f_210708595100 MA=f_210708597404 TX=f_210708593564
Form 477 mobile TechCode 83 = LTE.

Writes seda4g/validation_results.json and prints a summary.
"""
import json
import os
import zipfile

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "external", "seda4g")
BUILD = os.path.join(DATA, "build")
OUT = os.path.join(ROOT, "seda4g")

R = {}  # results accumulator

panel = pd.read_csv(os.path.join(OUT, "exposure_county_panel.csv"),
                    dtype={"county_fips": str})
blockpanel = pd.read_csv(os.path.join(BUILD, "block_panel_pilot.csv"),
                         dtype={"county": str})
diag = pd.read_csv(os.path.join(BUILD, "block_diagnostics.csv"))
allgeo = pd.read_csv(os.path.join(BUILD, "analyze_allgeo.csv.gz"),
                     dtype={"geography_id": str}, low_memory=False)

PILOT = ["DE", "CO", "MS", "OH", "WA", "TX", "MA", "MT"]
ST_FIPS = {"DE": "10", "CO": "08", "MS": "28", "OH": "39",
           "WA": "53", "TX": "48", "MA": "25", "MT": "30"}

# ---------------------------------------------------------------- 0. census reconciliation
PUBLISHED_2010 = {  # 2010 Census official county populations
    "30111": 147972,   # Yellowstone, MT
    "28049": 245285,   # Hinds, MS
    "10003": 538479,   # New Castle, DE
    "48201": 4092459,  # Harris, TX
    "53033": 1931249,  # King, WA
}
bp = blockpanel[blockpanel["wave"] == "2014-06"][["county", "county_pop"]]
rec = []
for fips, pub in PUBLISHED_2010.items():
    got = int(bp.loc[bp["county"] == fips, "county_pop"].iloc[0])
    rec.append(dict(fips=fips, published=pub, built=got,
                    match=bool(got == pub)))
R["census_reconciliation"] = rec

# ---------------------------------------------------------------- a. trajectory vs FCC
nat = allgeo[allgeo["geography_type"] == "NATIONAL"].copy()
nat = nat.groupby("wave").first()
traj = nat[["terrmobilewless", "wireless_advdl_gr3000k",
            "wireless_advdl_gr6000k", "wireless_advdl_gr10000k"]].round(4)

# pilot-aggregate for the two 2010 waves (no analyze tables): pop-weighted
b10 = blockpanel[blockpanel["wave"].isin(["2010-06", "2010-12"])]
agg10 = (b10.assign(w=lambda d: d["county_pop"])
         .groupby("wave")
         .apply(lambda d: pd.Series({
             "mobile_t7_wt": np.average(d["mobile_t7_wt"], weights=d["w"]),
             "mobile_t6_wt": np.average(d["mobile_t6_wt"], weights=d["w"]),
             "mobile_any_wt": np.average(d["mobile_any_wt"], weights=d["w"]),
             "mobile_t7_vzw_wt": np.average(d["mobile_t7_vzw_wt"], weights=d["w"]),
         }), include_groups=False).round(4))

# pilot aggregate Jun-2014 (block) for continuity with the 2010 points
b14 = blockpanel[blockpanel["wave"] == "2014-06"]
agg14 = {k: float(np.average(b14[k], weights=b14["county_pop"]))
         for k in ["mobile_t7_wt", "mobile_t6_wt", "mobile_any_wt",
                   "mobile_t7_vzw_wt", "anywless_t7_wt"]}

R["trajectory"] = {
    "national_analyze_table": traj.reset_index().to_dict("records"),
    "pilot8_block_2010_waves": agg10.reset_index().to_dict("records"),
    "pilot8_block_2014_06": {k: round(v, 4) for k, v in agg14.items()},
    "fcc_benchmarks": {"2010-06_any_lte": 0.0,
                       "2012-10_any_lte_mosaik": 0.856,
                       "2014-01_any_lte": 0.985},
}

# ---------------------------------------------------------------- b. Verizon Dec-2010 launch check
d10 = blockpanel[blockpanel["wave"] == "2010-12"].set_index("county")
LAUNCH = {  # central counties of Verizon 5 Dec 2010 launch metros in pilot states
    "08031": "Denver CO", "08005": "Arapahoe CO (Denver metro)",
    "53033": "King WA (Seattle)", "53053": "Pierce WA (Tacoma)",
    "48113": "Dallas TX", "48439": "Tarrant TX (Ft Worth)",
    "48201": "Harris TX (Houston)", "48029": "Bexar TX (San Antonio)",
    "25025": "Suffolk MA (Boston)", "25017": "Middlesex MA (Boston)",
    "39049": "Franklin OH (Columbus)", "39035": "Cuyahoga OH (Cleveland)",
    "39061": "Hamilton OH (Cincinnati)", "39153": "Summit OH (Akron)",
}
launch_rows = []
for fips, name in LAUNCH.items():
    if fips in d10.index:
        r = d10.loc[fips]
        launch_rows.append(dict(fips=fips, name=name,
                                vzw_t7=round(float(r["mobile_t7_vzw_wt"]), 4),
                                any_t7=round(float(r["mobile_t7_wt"]), 4)))
# non-launch rural: all RUCC 8-9 counties in MT and MS
rucc = pd.read_excel(os.path.join(DATA, "ruralurbancodes2013.xls"))
rucc["fips"] = rucc["FIPS"].astype(str).str.zfill(5)
rucc = rucc.dropna(subset=["RUCC_2013"])
rural_fips = rucc[(rucc["RUCC_2013"] >= 8) &
                  (rucc["fips"].str[:2].isin(["30", "28"]))]["fips"]
rural = d10.loc[d10.index.intersection(rural_fips)]

# GRANTEE CODING CAVEAT (investigated separately, see final report): in the
# Dec-2010 wave the speed-tier coding of Verizon LTE differs by state grantee:
# MA/DE coded launch areas tier 7; TX/WA coded them tier 6 (Verizon had no
# HSPA+, and EVDO tops out at tier 5, so Verizon tier>=6 is still LTE there);
# OH coded Verizon's entire footprint tier 6 (uninformative); CO left
# everything at tier 5 (LTE invisible until the Dec-2011 wave).
# Therefore the launch check uses tier>=6 for TX/WA and tier>=7 for MA/DE.
import zipfile as _zf, io as _io, re as _re

def vzw_dec2010(st, min_tier):
    outer = _zf.ZipFile(os.path.join(
        DATA, f"states/{st}-NBM-CSV-December-2010.zip"))
    nm = [n for n in outer.namelist()
          if _re.search("Wireless-CSV-December-2010", n) and n.endswith(".zip")][0]
    inner = _zf.ZipFile(_io.BytesIO(outer.read(nm)))
    dn = [n for n in inner.namelist() if n.lower().endswith((".csv", ".txt"))][0]
    df = pd.read_csv(_io.BytesIO(inner.read(dn)), sep="|", dtype=str,
                     encoding="latin-1")
    df.columns = [c.lower() for c in df.columns]
    vz = df[df[["provname", "dbaname", "hoconame"]].apply(
        lambda c: c.str.contains("verizon|cellco", case=False, na=False)).any(axis=1)]
    vz = vz[(vz["transtech"] == "80") &
            (pd.to_numeric(vz["maxaddown"], errors="coerce") >= min_tier)].copy()
    vz["pct"] = pd.to_numeric(vz["pct_blk_in_shape"], errors="coerce").fillna(0)
    if len(vz) and vz["pct"].max() > 1.5:
        vz["pct"] /= 100
    bm = vz.groupby(vz["censusblock_fips"].str.strip())["pct"].max()
    pops = pd.read_csv(os.path.join(BUILD, f"blockpop2000_{st.lower()}.csv.gz"),
                       dtype={"block": str})
    pops["county"] = pops["block"].str[:5]
    m = pops.merge(bm.rename("pct"), left_on="block", right_index=True, how="left")
    m["pct"] = m["pct"].fillna(0)
    g = m.assign(cov=m["pop"] * m["pct"]).groupby("county")[["pop", "cov"]].sum()
    g["share"] = g["cov"] / g["pop"]
    return g

launch_t6 = {}
for st, fips_pref, tier in [("TX", "48", 6), ("WA", "53", 6),
                            ("MA", "25", 7), ("DE", "10", 7)]:
    g = vzw_dec2010(st, tier)
    in_launch = [f for f in LAUNCH if f.startswith(fips_pref)]
    rest = g.drop(index=[f for f in in_launch if f in g.index])
    launch_t6[st] = {
        "tier_used": tier,
        "launch_counties": {f: round(float(g.loc[f, "share"]), 3)
                            for f in in_launch if f in g.index},
        "nonlaunch_popwt_mean": round(float(
            np.average(rest["share"], weights=rest["pop"])), 4),
        "nonlaunch_share_counties_gt10pct": round(float(
            (rest["share"] > .10).mean()), 4),
    }

R["verizon_dec2010"] = {
    "launch_metro_counties_t7": launch_rows,
    "rural_MT_MS_rucc8_9_t7": {
        "n_counties": int(len(rural)),
        "mean_vzw_t7": round(float(np.average(
            rural["mobile_t7_vzw_wt"], weights=rural["county_pop"])), 5),
        "n_counties_vzw_t7_gt_1pct": int((rural["mobile_t7_vzw_wt"] > .01).sum()),
        "max_vzw_t7": round(float(rural["mobile_t7_vzw_wt"].max()), 4),
    },
    # statewide tier-7 mobile of ANY provider in pilot states Dec-2010
    "statewide_t7_dec2010": {
        st: round(float(np.average(
            d10[d10.index.str[:2] == ST_FIPS[st]]["mobile_t7_wt"],
            weights=d10[d10.index.str[:2] == ST_FIPS[st]]["county_pop"])), 4)
        for st in PILOT},
    "grantee_coding_note": (
        "Dec-2010 Verizon speed-tier coding varies by state grantee: "
        "MA/DE tier7, TX/WA tier6, OH tier6-everywhere (uninformative), "
        "CO tier5 (LTE invisible until Dec-2011 wave)."),
    "launch_check_grantee_adjusted": launch_t6,
}

# grantee artifact census: states with t7 < 5% per wave (vs national 58-98%)
stt = allgeo[allgeo["geography_type"] == "STATE"].copy()
terr = ["Puerto Rico", "Guam", "American Samoa", "U.S. Virgin Islands",
        "United States Virgin Islands",
        "Commonwealth of the Northern Mariana Islands"]
stt = stt[~stt["geography_desc"].isin(terr)]
piv = stt.pivot_table(index="geography_desc", columns="wave",
                      values="wireless_advdl_gr10000k")
R["grantee_artifacts"] = {
    w: sorted(piv[piv[w] < 0.05].index.tolist())
    for w in ["2011-06", "2011-12", "2012-06", "2012-12"]}
R["grantee_artifacts"]["note"] = (
    "States with statewide t7<5%. Jun-2011 list mixes genuine no-LTE rural "
    "states (MT ND SD ME VT MS IA AK) with grantee under-coding (CO: Denver "
    "was a Dec-2010 launch metro yet t7=0 until the Dec-2011 wave; MO: "
    "St. Louis launched Apr-2011). Self-correcting by Dec-2012.")

# ---------------------------------------------------------------- c. rural lag (national, analyze tables)
a = panel[panel["source"] == "analyze_table"].copy()
waves = sorted(a["wave"].unique())
wave_num = {w: i for i, w in enumerate(waves)}  # 0 = 2011-06 ... 6 = 2014-06
a["wnum"] = a["wave"].map(wave_num)
first = (a[a["share_anywless_t7"] >= 0.5]
         .groupby("county_fips")["wnum"].min().rename("first_wave"))
cty = a[a["wave"] == waves[-1]][["county_fips", "county_pop"]].merge(
    first, on="county_fips", how="left")
cty["first_wave"] = cty["first_wave"].fillna(len(waves))  # censored
cty = cty.merge(rucc[["fips", "RUCC_2013"]],
                left_on="county_fips", right_on="fips", how="inner")
cty = cty.dropna(subset=["RUCC_2013", "first_wave", "county_pop"])
cty["metro"] = cty["RUCC_2013"] <= 3
g = cty.groupby("metro").apply(
    lambda d: pd.Series({
        "popwt_mean_first_wave": np.average(d["first_wave"], weights=d["county_pop"]),
        "share_counties_never_ge50_by_jun2014": float((d["first_wave"] == len(waves)).mean()),
        "n": len(d)}), include_groups=False)
rho_rucc = stats.spearmanr(cty["RUCC_2013"], cty["first_wave"])
R["rural_lag"] = {
    "wave_index": {w: i for w, i in wave_num.items()},
    "by_metro_nonmetro": {("metro" if k else "nonmetro"): v.round(4).to_dict()
                          for k, v in g.iterrows()},
    "spearman_rucc_vs_first_wave": [round(rho_rucc.statistic, 4),
                                    float(rho_rucc.pvalue)],
}

# ---------------------------------------------------------------- d. Form 477 Dec-2015 splice
def f477_county_lte(st):
    z = zipfile.ZipFile(os.path.join(
        DATA, "fcc477", f"F477_2015_12_Centroid_State_{st}.zip"))
    name = [n for n in z.namelist() if n.lower().endswith(".csv")][0]
    df = pd.read_csv(z.open(name), dtype={"BlockCode": str, "TechCode": str})
    lte_blocks = set(df.loc[df["TechCode"] == "83", "BlockCode"])
    pops = pd.read_csv(os.path.join(
        BUILD, f"blockpop2010_{st.lower()}.csv.gz"), dtype={"block": str})
    pops["county"] = pops["block"].str[:5]
    pops["lte"] = pops["block"].isin(lte_blocks)
    g = pops.groupby("county").apply(
        lambda d: pd.Series({"pop": d["pop"].sum(),
                             "lte477": (d["pop"] * d["lte"]).sum() / max(d["pop"].sum(), 1)}),
        include_groups=False)
    return g.reset_index()

splice = []
b14i = blockpanel[blockpanel["wave"] == "2014-06"].set_index("county")
a14 = a[a["wave"] == "2014-06"].set_index("county_fips")
for st in ["MT", "MS", "MA", "TX"]:
    c477 = f477_county_lte(st).set_index("county")
    m = c477.join(b14i[["mobile_t7_wt", "mobile_t6_wt"]], how="inner") \
            .join(a14[["share_anywless_t7"]], how="left")
    m = m.dropna(subset=["mobile_t7_wt"])
    sp_blk = stats.spearmanr(m["lte477"], m["mobile_t7_wt"])
    pr_blk = stats.pearsonr(m["lte477"], m["mobile_t7_wt"])
    sp_anz = stats.spearmanr(m.dropna()["lte477"], m.dropna()["share_anywless_t7"])
    splice.append(dict(
        state=st, n_counties=int(len(m)),
        spearman_477_vs_sbdd_block_t7=round(float(sp_blk.statistic), 4),
        pearson_477_vs_sbdd_block_t7=round(float(pr_blk.statistic), 4),
        spearman_477_vs_analyze_t7=round(float(sp_anz.statistic), 4),
        mean_lte477=round(float(np.average(m["lte477"], weights=m["pop"])), 4),
        mean_sbdd_t7=round(float(np.average(m["mobile_t7_wt"], weights=m["pop"])), 4),
        share_counties_477_ge_sbdd=round(float(
            (m["lte477"] >= m["mobile_t7_wt"] - 0.02).mean()), 4)))
R["splice_477_dec2015"] = splice

# ---------------------------------------------------------------- e. large-block / completeness
R["large_block_problem"] = {
    "note": ("SBDD wireless coverage was submitted as shapefiles; NTIA overlaid "
             "them on ALL census blocks, so the Wireless CSV has no <2-sq-mi "
             "restriction (that restriction applies to the wireline CBLOCK/"
             "Address-Street split). Quantified below: share of state pop in "
             "blocks that appear in the wireless CSV at all."),
    "diagnostics": diag.round(4).to_dict("records"),
}
# cross-check block build vs NTIA analyze tables, Jun-2014, all pilot counties
m = (b14i[["mobile_any_wt", "mobile_t7_wt", "anywless_t7_wt", "county_pop"]]
     .join(a14[["share_mobile_any", "share_anywless_t7"]], how="inner")).dropna()
R["blockcsv_vs_analyze_jun2014"] = {
    "n_counties": int(len(m)),
    "corr_mobile_any": round(float(
        stats.pearsonr(m["mobile_any_wt"], m["share_mobile_any"]).statistic), 4),
    "corr_anywless_t7": round(float(
        stats.pearsonr(m["anywless_t7_wt"], m["share_anywless_t7"]).statistic), 4),
    "mean_abs_diff_mobile_any": round(float(
        (m["mobile_any_wt"] - m["share_mobile_any"]).abs().mean()), 4),
    "mean_abs_diff_anywless_t7": round(float(
        (m["anywless_t7_wt"] - m["share_anywless_t7"]).abs().mean()), 4),
}
# fixed-wireless leakage in the >=10Mbps any-wireless proxy (Jun-2014, pilot)
leak = (b14i["anywless_t7_wt"] - b14i["mobile_t7_wt"])
R["fixed_wireless_leakage_jun2014"] = {
    "popwt_mean_anywless_t7_minus_mobile_t7": round(float(
        np.average(leak, weights=b14i["county_pop"])), 4),
    "p50": round(float(leak.median()), 4),
    "p90": round(float(leak.quantile(.9)), 4),
    "max": round(float(leak.max()), 4),
}

# same leakage at mid-rollout (Dec-2012, MT MS CO MA block build) + proof that
# the analyze-table county t7 column == any-wireless t7 (incl. fixed wireless)
b12 = blockpanel[blockpanel["wave"] == "2012-12"].set_index("county")
a12 = panel[(panel["source"] == "analyze_table") &
            (panel["wave"] == "2012-12")].set_index("county_fips")
m12 = b12.join(a12[["share_anywless_t7"]], how="inner").dropna(
    subset=["share_anywless_t7"])
lk = m12["anywless_t7_wt"] - m12["mobile_t7_wt"]
R["fixed_wireless_leakage_dec2012"] = {
    "states": "MT MS CO MA",
    "popwt_mean_anywless_t7_minus_mobile_t7": round(float(
        np.average(lk, weights=m12["county_pop"])), 4),
    "p50": round(float(lk.median()), 4),
    "p90": round(float(lk.quantile(.9)), 4),
    "corr_analyze_t7_vs_block_anywless_t7": round(float(
        m12["share_anywless_t7"].corr(m12["anywless_t7_wt"])), 4),
    "corr_analyze_t7_vs_block_mobile_t7": round(float(
        m12["share_anywless_t7"].corr(m12["mobile_t7_wt"])), 4),
    "by_state_popwt": {
        s: {"analyze_t7": round(float(np.average(
                g["share_anywless_t7"], weights=g["county_pop"])), 4),
            "mobile_t7": round(float(np.average(
                g["mobile_t7_wt"], weights=g["county_pop"])), 4)}
        for s, g in m12.groupby(m12.index.str[:2])},
    "note": ("Analyze-table t7 column is numerically identical to the "
             "block-built ANY-wireless t7 (corr 1.000) — it includes fixed "
             "wireless. Mobile-only exposure must come from the block CSVs "
             "(transtech==80), or the analyze tables need a fixed-wireless "
             "adjustment. Leakage is concentrated in WISP-heavy rural states "
             "(CO, MT); ~0 in MA/MS."),
}
# leakage at the 2010 waves (8 pilot states)
for w, key in [("2010-06", "fixed_wireless_leakage_jun2010"),
               ("2010-12", "fixed_wireless_leakage_dec2010")]:
    bw = blockpanel[blockpanel["wave"] == w]
    R[key] = {
        "popwt_mean_anywless_t7_minus_mobile_t7": round(float(np.average(
            bw["anywless_t7_wt"] - bw["mobile_t7_wt"],
            weights=bw["county_pop"])), 4)}

# ---------------------------------------------------------------- f. SEDA
seda_path = os.path.join(DATA, "seda_county_long_cs_5.0.csv")
if os.path.exists(seda_path):
    s = pd.read_csv(seda_path, usecols=["sedacounty", "year", "subject", "grade"])
    R["seda"] = {
        "status": "downloaded, no registration wall",
        "url": "https://stacks.stanford.edu/file/druid:cs829jn7849/seda_county_long_cs_5.0.csv",
        "rows": int(len(s)), "years": [int(s["year"].min()), int(s["year"].max())],
        "counties": int(s["sedacounty"].nunique()),
        "subjects": sorted(s["subject"].unique().tolist()),
        "grades": sorted(int(g) for g in s["grade"].unique()),
    }
else:
    R["seda"] = {"status": "NOT downloaded"}

with open(os.path.join(OUT, "validation_results.json"), "w") as f:
    json.dump(R, f, indent=2, default=str)
print(json.dumps(R, indent=2, default=str))
