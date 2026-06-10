"""Test-taking effort on PISA: the effort thermometer (EFFORT1/EFFORT2), 2018 vs 2022.

Question: did self-reported effort on the (low-stakes) PISA test decline, and how much
of the score decline could effort shifts plausibly account for?
- EFFORT1: effort invested in the PISA test (1-10)
- EFFORT2: effort the student would have invested had it counted for marks (1-10)
- "effort gap" = EFFORT2 - EFFORT1 (slack relative to a counted test)
"""
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf

OECD = {"AUS","AUT","BEL","CAN","CHL","COL","CRI","CZE","DNK","EST","FIN","FRA","DEU",
        "GRC","HUN","ISL","IRL","ISR","ITA","JPN","KOR","LVA","LTU","LUX","MEX","NLD",
        "NZL","NOR","POL","PRT","SVK","SVN","ESP","SWE","CHE","TUR","GBR","USA"}
PVS = [f"PV{i}MATH" for i in range(1, 11)]

def wmean(s, w):
    s = pd.Series(np.asarray(s, dtype=float), index=w.index)
    m = s.notna() & w.notna()
    return np.average(s[m], weights=w[m]) if m.any() else np.nan

def load(year, path):
    cols = ["CNT", "CNTSCHID", "W_FSTUWT", "ESCS", "EFFORT1", "EFFORT2"] + PVS
    df, _ = pyreadstat.read_sav(path, usecols=cols)
    df["year"] = year
    df = df[df.EFFORT1.between(1, 10) | df.EFFORT1.isna()]
    df.loc[~df.EFFORT1.between(1, 10), "EFFORT1"] = np.nan
    df.loc[~df.EFFORT2.between(1, 10), "EFFORT2"] = np.nan
    df["gap"] = df.EFFORT2 - df.EFFORT1
    df["oecd"] = df.CNT.isin(OECD)
    return df

out = {}
frames = []
for year, path in [(2022, "data/external/pisa/CY08MSP_STU_QQQ.SAV"),
                   (2018, "data/external/pisa/STU/CY07_MSU_STU_QQQ.sav")]:
    try:
        frames.append(load(year, path))
        print(f"loaded {year}: {len(frames[-1]):,} rows")
    except Exception as e:
        print(f"{year} not available: {e}")

df = pd.concat(frames)

print("\n## Effort thermometer: weighted means")
rows = []
for (year, scope), g in [((y, s), df[(df.year == y) & (df.CNT == "USA" if s == "USA" else (df.year == y) & df.oecd)])
                         for y in sorted(df.year.unique()) for s in ("USA", "OECD")]:
    rows.append({"year": int(year), "scope": scope,
                 "EFFORT1 (invested)": round(wmean(g.EFFORT1, g.W_FSTUWT), 2),
                 "EFFORT2 (if counted)": round(wmean(g.EFFORT2, g.W_FSTUWT), 2),
                 "gap": round(wmean(g.gap, g.W_FSTUWT), 2),
                 "pct EFFORT1<=5": round(100 * wmean((g.EFFORT1 <= 5).where(g.EFFORT1.notna()), g.W_FSTUWT), 1)})
t = pd.DataFrame(rows)
print(t.to_markdown(index=False))
out["thermometer"] = rows

print("\n## Effort-score association (2022, ESCS-adjusted, PV1 quick pass then Rubin for headline)")
d22 = df[(df.year == 2022) & df.oecd].dropna(subset=["EFFORT1", "ESCS", "W_FSTUWT"])
bs, vs = [], []
for pv in PVS:
    m = smf.wls(f"{pv} ~ EFFORT1 + ESCS + I(ESCS**2) + C(CNT)", data=d22,
                weights=d22.W_FSTUWT).fit(cov_type="cluster", cov_kwds={"groups": d22.CNTSCHID})
    bs.append(m.params["EFFORT1"]); vs.append(m.bse["EFFORT1"] ** 2)
b = np.mean(bs); se = np.sqrt(np.mean(vs) + (1 + 0.1) * np.var(bs, ddof=1))
print(f"  OECD 2022: {b:+.2f} points per effort point (se {se:.2f})")
out["effort_score_oecd2022"] = {"b": round(b, 2), "se": round(se, 2)}

print("\n## Effort by within-country math quartile (2022 vs 2018, OECD)")
qrows = []
for year in sorted(df.year.unique()):
    d = df[(df.year == year) & df.oecd].dropna(subset=["W_FSTUWT"]).copy()
    d["q"] = d.groupby("CNT")["PV1MATH"].transform(
        lambda x: pd.qcut(x, 4, labels=["Q1", "Q2", "Q3", "Q4"]))
    for q, g in d.groupby("q", observed=True):
        qrows.append({"year": int(year), "quartile": str(q),
                      "EFFORT1": round(wmean(g.EFFORT1, g.W_FSTUWT), 2),
                      "gap": round(wmean(g.gap, g.W_FSTUWT), 2)})
print(pd.DataFrame(qrows).pivot_table(index="quartile", columns="year",
                                      values=["EFFORT1", "gap"]).round(2).to_markdown())
out["effort_by_quartile"] = qrows

# bound: implied score change from effort change = d(effort) * b
if len(frames) == 2:
    for scope in ("USA", "OECD"):
        g22 = df[(df.year == 2022) & ((df.CNT == "USA") if scope == "USA" else df.oecd)]
        g18 = df[(df.year == 2018) & ((df.CNT == "USA") if scope == "USA" else df.oecd)]
        de = wmean(g22.EFFORT1, g22.W_FSTUWT) - wmean(g18.EFFORT1, g18.W_FSTUWT)
        implied = de * b
        print(f"\n{scope}: EFFORT1 change 2018->2022 = {de:+.2f} -> implied score change "
              f"{implied:+.1f} pts (using cross-sectional gradient {b:+.2f}, an upper bound on causality)")
        out[f"implied_{scope}"] = {"d_effort": round(de, 2), "implied_pts": round(implied, 1)}

with open("data/effort_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nsaved data/effort_results.json")
