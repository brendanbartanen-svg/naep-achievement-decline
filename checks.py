#!/usr/bin/env python3
"""Assertion tests for the NAEP-decline report's load-bearing numbers.

Usage:  python3 checks.py        (exit 0 = all pass, nonzero = failure)

Tier 1 recomputes headline descriptives directly from the raw CSVs
(data/naep_main.csv, data/naep_v11.csv, data/ltt.csv).
Tier 2 freezes the key entries of the computed-results JSONs at their
2026-06-10 values, so any future re-run that silently changes a number
the report cites will fail loudly here.

Cross-reference: evidence/claims_audit.md maps each check to the report claim.
Dependencies: pandas + stdlib only.
"""
import json
import os
import re
import sys

import pandas as pd

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

RESULTS = []


def check(name, actual, expected, tol=None):
    """Record a check. tol=None means exact equality (use for ints/strings)."""
    if tol is None:
        ok = actual == expected
    else:
        try:
            ok = abs(actual - expected) <= tol
        except TypeError:
            ok = False
    RESULTS.append(ok)
    status = "PASS" if ok else "FAIL"
    tolstr = "" if tol is None else f" (tol ±{tol})"
    print(f"[{status}] {name}: actual={actual} expected={expected}{tolstr}")
    return ok


def jload(fname):
    with open(os.path.join(DATA, fname)) as f:
        return json.load(f)


# ----------------------------------------------------------------------
# Tier 1 — recompute from raw CSVs
# ----------------------------------------------------------------------
print("=" * 72)
print("TIER 1: recomputed from raw CSVs")
print("=" * 72)

main = pd.read_csv(os.path.join(DATA, "naep_main.csv"))
main = main[main.displayable == 1]
nat = main[main.dataset == "national"]
RSUBJ = [s for s in nat.subject.unique() if s != "MAT"][0]  # 'RED' or 'RRP'
LBL = {"MAT4": ("MAT", 4), "MAT8": ("MAT", 8), "RED4": (RSUBJ, 4), "RED8": (RSUBJ, 8)}

means = nat[nat.stat == "MN:MN"].pivot_table(
    index="year", columns=["subject", "grade"], values="value")

# T1.1 national G8 reading mean 2024 ~ 258
check("T1.1 G8 reading national mean, 2024",
      round(means[LBL["RED8"]][2024], 1), 258.0, tol=0.5)
# ... and it is the lowest ever recorded
red8 = means[LBL["RED8"]].dropna()
check("T1.1b G8 reading 2024 is the series minimum (lowest ever)",
      int(red8.idxmin()), 2024)

# T1.2/T1.3 peak years: all 2013 except G4 reading 2015
for key, want in [("MAT4", 2013), ("MAT8", 2013), ("RED4", 2015), ("RED8", 2013)]:
    s = means[LBL[key]].dropna()
    check(f"T1.2 peak year, {key}", int(s.idxmax()), want)

# T1.4 90-10 gap, G8 math: 2024 wider than 2013 and the widest on record
p8m = nat[(nat.subject == "MAT") & (nat.grade == 8)].pivot_table(
    index="year", columns="stat", values="value")
gap = (p8m["PC:P9"] - p8m["PC:P1"]).dropna()
check("T1.4 G8 math 90-10 gap 2024 > 2013",
      bool(gap[2024] > gap[2013]), True)
check("T1.4b G8 math 90-10 gap widest on record in 2024",
      int(gap.idxmax()), 2024)

# T1.5 G8 math mean change 2013->2024 ~ -10.8 (Table 1)
check("T1.5 G8 math mean change 2013->2024",
      round(means[LBL["MAT8"]][2024] - means[LBL["MAT8"]][2013], 1), -10.8, tol=0.2)

# T1.6 pre-pandemic percentile divergence, G8 math 2013->2019
check("T1.6 G8 math P10 change 2013->2019",
      round(p8m["PC:P1"][2019] - p8m["PC:P1"][2013], 1), -6.6, tol=0.2)
check("T1.6b G8 math P90 change 2013->2019",
      round(p8m["PC:P9"][2019] - p8m["PC:P9"][2013], 1), 2.7, tol=0.2)

# T1.7 every state below its 2013 level in G8 math by 2024
st = main[(main.dataset == "state") & (main.subject == "MAT") & (main.grade == 8)]
pv = st.pivot_table(index="jurisdiction", columns="year", values="value")
share_below = float((pv[2024] < pv[2013]).mean())
check("T1.7 share of states below 2013 in 2024, G8 math", share_below, 1.0)

# T1.8/T1.9 sector facts from naep_v11.csv
v11 = pd.read_csv(os.path.join(DATA, "naep_v11.csv"))
v11 = v11[v11.displayable == 1]
RS2 = [s for s in v11.subject.unique() if s != "MAT"][0]
sch = v11[v11.dataset == "schtype"]


def sector_mean(subj, grade, group):
    d = sch[(sch.subject == subj) & (sch.grade == grade) &
            (sch.group == group) & (sch.stat == "MN:MN")]
    return d.groupby("year").value.mean()  # dedupe SCHTYP2/SCHTYPE overlap years


cath_r8 = sector_mean(RS2, 8, "Catholic")
check("T1.8 Catholic G8 reading change 2013->2019",
      round(cath_r8[2019] - cath_r8[2013], 1), -7.8, tol=0.2)

pub_m8 = sector_mean("MAT", 8, "Public")
cath_m8 = sector_mean("MAT", 8, "Catholic")
dd = (pub_m8[2024] - pub_m8[2019]) - (cath_m8[2024] - cath_m8[2019])
check("T1.9 G8 math 2019->2024 divergence, public minus Catholic",
      round(dd, 1), -7.9, tol=0.3)

# T1.10 LTT means (data/ltt.csv): age-13 math 2012 peak, pre-pandemic fall
ltt = pd.read_csv(os.path.join(DATA, "ltt.csv"))
a13m = ltt[ltt.series == "age13_math"].set_index("year").value
check("T1.10 LTT age-13 math 2012 level", round(a13m[2012], 1), 285.0, tol=0.5)
check("T1.10b LTT age-13 math change 2012->2020 (pre-pandemic)",
      round(a13m[2020] - a13m[2012], 1), -5.3, tol=0.5)
a13r = ltt[ltt.series == "age13_reading"].set_index("year").value
check("T1.10c LTT age-13 reading 2023 within 1.5 pts of 1971 baseline",
      round(abs(a13r[2023] - a13r[1971]), 1), 0.0, tol=1.5)

# T1.11 the headline LTT P10 -12.6 is NOT in ltt.csv (means only); it is
# hard-coded in analyze_ltt.py and sourced in evidence/ltt_evidence.md.
# Pin the script literal to the evidence file so they cannot drift apart.
with open(os.path.join(ROOT, "analyze_ltt.py")) as f:
    src = f.read()
m = re.search(r'"Age 13 math":\s*\[(-?[\d.]+)', src)
check("T1.11 analyze_ltt.py hard-coded age-13 math P10 change (2012->2020)",
      float(m.group(1)) if m else None, -12.6, tol=0.01)
with open(os.path.join(ROOT, "evidence", "ltt_evidence.md")) as f:
    ev = f.read()
check("T1.11b evidence/ltt_evidence.md documents the -12.6 P10 change",
      ("−12.6" in ev) or ("-12.6" in ev), True)

# T1.12 LTT 2025 wave (released 2026-06-10; API pull in evidence/ltt_2025.md)
check("T1.12 LTT age-13 math 2025 level", round(a13m[2025], 1), 270.3, tol=0.2)
check("T1.12b LTT age-13 math 2023->2025 flat",
      round(a13m[2025] - a13m[2023], 1), -0.4, tol=0.3)
a9m = ltt[ltt.series == "age9_math"].set_index("year").value
a9r = ltt[ltt.series == "age9_reading"].set_index("year").value
check("T1.12c LTT age-9 math 2022->2025 recovery",
      round(a9m[2025] - a9m[2022], 1), 3.8, tol=0.3)
check("T1.12d LTT age-9 reading 2022->2025 recovery",
      round(a9r[2025] - a9r[2022], 1), 3.8, tol=0.3)
check("T1.12e LTT age-13 reading 2025 level", round(a13r[2025], 1), 256.1, tol=0.2)
# pin the post-pandemic percentile dict (third panel) to the evidence file:
# age-13 math P10 fell 2.8 more 2023->2025 while P90 rose 2.3 (fan-out continues)
m2 = re.search(r'post2 = \{[^}]*"Age 13 math":\s*\[(-?[\d.]+),[^\]]*?(-?[\d.]+)\]', src)
check("T1.12f analyze_ltt.py post2 age-13 math P10 change (2023->2025)",
      float(m2.group(1)) if m2 else None, -2.8, tol=0.01)
check("T1.12g analyze_ltt.py post2 age-13 math P90 change (2023->2025)",
      float(m2.group(2)) if m2 else None, 2.3, tol=0.01)
check("T1.12h evidence files document the 2025 percentile fan-out (114.0 gap)",
      ("114.0" in ev) or ("114.0" in open(os.path.join(ROOT, "evidence", "ltt_2025.md")).read()), True)
# reading-for-fun floor: age-13 "almost every day" 14.2 in 2025
m3 = re.search(r"vals13 = \[[^\]]*?(-?[\d.]+)\]", src)
check("T1.12i analyze_ltt.py reading-for-fun age-13 2025 share",
      float(m3.group(1)) if m3 else None, 14.2, tol=0.01)

# ----------------------------------------------------------------------
# Tier 2 — freeze the computed-results JSONs at their 2026-06-10 values
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("TIER 2: frozen values of computed-results JSONs")
print("=" * 72)

TOL = 0.05  # JSONs store rounded values; any real change exceeds this

# summary.json (analyze.py)
s = jload("summary.json")
nm = {r["series"]: r for r in s["national_means"]}
check("T2.1 summary: G8 math score 2024", nm["Math, Grade 8"]["score_2024"], 273.8, tol=TOL)
check("T2.1b summary: G8 math change 2013->2024", nm["Math, Grade 8"]["chg_2013_2024"], -10.8, tol=TOL)
check("T2.1c summary: G8 math change in SD units", nm["Math, Grade 8"]["chg_2013_2024_sd"], -0.30, tol=0.005)
check("T2.2 summary: G8 reading score 2024", nm["Reading, Grade 8"]["score_2024"], 258.0, tol=TOL)
check("T2.2b summary: G8 reading change 2013->2019 (pre-pandemic)",
      nm["Reading, Grade 8"]["chg_2013_2019"], -4.4, tol=TOL)
g = s["gap_90_10"]["Math, Grade 8"]
check("T2.3 summary: G8 math 90-10 gap 2013", g["2013"], 93.2, tol=TOL)
check("T2.3b summary: G8 math 90-10 gap 2024", g["2024"], 108.9, tol=TOL)

# absence_results.json (analyze_absence.py)
a = jload("absence_results.json")
sh = a["share_3plus"]["Math, Grade 4"]
check("T2.4 absence: G4 math 3+days share 2013", sh["2013"], 19.5, tol=TOL)
check("T2.4b absence: G4 math 3+days share 2019", sh["2019"], 24.3, tol=TOL)
check("T2.4c absence: G4 math 3+days share 2022", sh["2022"], 35.0, tol=TOL)
check("T2.4d absence: G4 math 3+days share 2024", sh["2024"], 30.4, tol=TOL)
dec = {(d["series"], d["period"]): d["pct_from_absence"] for d in a["decomposition"]}
check("T2.5 Kitagawa: G4 math 2019-2024 pct from absence",
      dec[("Math, Grade 4", "2019-2024")], 42.0, tol=0.5)
check("T2.5b Kitagawa: G8 math 2019-2024 pct from absence",
      dec[("Math, Grade 8", "2019-2024")], 25.0, tol=0.5)
check("T2.5c Kitagawa: G8 math 2013-2019 pct from absence (pre-pandemic)",
      dec[("Math, Grade 8", "2013-2019")], 19.0, tol=0.5)
check("T2.5d Kitagawa: G8 reading 2013-2019 pct from absence (pre-pandemic)",
      dec[("Reading, Grade 8", "2013-2019")], 7.0, tol=0.5)

# v11_results.json (analyze_v11.py) — waiver DiD
v11j = jload("v11_results.json")
w = v11j["waiver_did_pooled_p10_z"]
check("T2.6 waiver DiD pooled P10 beta (SD units)", w["beta"], 0.092, tol=0.005)
check("T2.6b waiver DiD pooled P10 p-value", w["p"], 0.502, tol=0.005)

# v13_results.json (analyze_v13.py) — randomization inference, MDE, sector z
v13 = jload("v13_results.json")
check("T2.7 waiver permutation p (pooled, z)", v13["permutation"]["p_perm"], 0.463, tol=0.005)
check("T2.7b waiver MDE80, G8 math P10 (points)", v13["permutation_g8math_pts"]["MDE80_pts"], 3.24, tol=0.05)
check("T2.7c waiver pre-trend joint p", v13["pretrend"]["p"], 0.076, tol=0.005)
sec = {r["series"]: r for r in v13["sector_tests"]}
check("T2.8 sector z: Catholic G8 reading 2013-19", sec["Reading, Grade 8"]["z"], -3.45, tol=0.05)
check("T2.8b sector z: G8 math 2019-24 divergence", sec["Math, Grade 8"]["z_dd"], -2.63, tol=0.05)

# v14_results.json (analyze_v14.py) — Common Core, TUDA, Minnesota
v14 = jload("v14_results.json")
check("T2.9 Common Core never-adopter pooled P10 diff (pts)", v14["cc_never_diff"]["b"], -0.39, tol=0.02)
check("T2.9b Common Core never-adopter diff p-value", v14["cc_never_diff"]["p"], 0.724, tol=0.005)
mn8 = [r for r in v14["minnesota"] if r["grade"] == 8][0]
check("T2.9c Minnesota G8 triple-difference (math - reading)",
      mn8["triple-diff (math - reading)"], 2.3, tol=0.05)
check("T2.10 TUDA pooled dose-response b/10pp", v14["tuda_pooled"]["drop_b10"], -0.18, tol=0.02)
check("T2.10b TUDA pooled dose-response p", v14["tuda_pooled"]["p"], 0.2274, tol=0.005)

# doseresponse_results.json (analyze_doseresponse.py) — state-level
dr = jload("doseresponse_results.json")
check("T2.11 state dose-response pooled b/10pp virtual", dr["pooled_d_1922_virt"]["b_per10pp"], -0.04, tol=0.01)
check("T2.11b state dose-response pooled p", dr["pooled_d_1922_virt"]["p"], 0.804, tol=0.005)

# pisa_results.json (analyze_pisa.py)
pisa = jload("pisa_results.json")
check("T2.12 PISA distraction gap, USA (ESCS-adj)", pisa["distraction_adj"]["USA"]["b"], -13.2, tol=0.05)
check("T2.12b PISA distraction gap, OECD pool", pisa["distraction_adj"]["OECD pool"]["b"], -15.0, tol=0.05)
check("T2.13 PISA 5+hr leisure gap (ESCS-adj)",
      pisa["leisure_adj"]["OECD subset w/ ST326"]["b"], -40.5, tol=0.05)
q = {r["quartile"]: r for r in pisa["by_quartile_oecd"]}
check("T2.14 PISA distraction %, bottom score quartile", q["Q1 (bottom)"]["pct distracted most/every"], 31.9, tol=0.1)
check("T2.14b PISA distraction %, top score quartile", q["Q4 (top)"]["pct distracted most/every"], 23.7, tol=0.1)
e = {r["ESCS quartile"]: r for r in pisa["by_escs_oecd"]}
check("T2.14c PISA distraction % flat across SES (E1 - E4 small)",
      e["E1 (low)"]["pct distracted most/every"] - e["E4 (high)"]["pct distracted most/every"],
      2.1, tol=0.2)

# effort_results.json (analyze_effort.py)
eff = jload("effort_results.json")
check("T2.15 effort thermometer change, USA 2018->2022", eff["implied_USA"]["d_effort"], -0.13, tol=0.01)
check("T2.15b implied effort-attributable PISA change, USA (pts)", eff["implied_USA"]["implied_pts"], -0.5, tol=0.05)
check("T2.15c effort thermometer change, OECD", eff["implied_OECD"]["d_effort"], -0.16, tol=0.01)
check("T2.15d effort-score gradient (pts per effort pt)", eff["effort_score_oecd2022"]["b"], 3.88, tol=0.05)

# cohort_decomp.json (analyze_cohort.py)
co = jload("cohort_decomp.json")
check("T2.16 cohort decomp, reading: G8 change 2013-19", co["decomp_2013_2019"]["Reading"]["d_g8"], -4.4, tol=TOL)
check("T2.16b cohort decomp, reading: entry component", co["decomp_2013_2019"]["Reading"]["d_entry"], 1.6, tol=TOL)
check("T2.16c cohort decomp, reading: growth component", co["decomp_2013_2019"]["Reading"]["d_growth"], -6.0, tol=TOL)
check("T2.16d cohort decomp, math: growth component", co["decomp_2013_2019"]["Math"]["d_growth"], -3.3, tol=TOL)

# ----------------------------------------------------------------------
print()
n = len(RESULTS)
fails = n - sum(RESULTS)
print(f"{n} checks: {sum(RESULTS)} passed, {fails} failed")
sys.exit(1 if fails else 0)
