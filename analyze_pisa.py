"""PISA 2022 microdata: device distraction, leisure screen use, and math scores.

Goes beyond OECD's published bivariate tables: ESCS-adjusted within-country estimates
with Rubin-combined plausible values and school-clustered SEs, US vs OECD; plus the
distributional tie-in — is distraction concentrated among low performers?
"""
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf

F = "data/external/pisa/CY08MSP_STU_QQQ.SAV"
PVS = [f"PV{i}MATH" for i in range(1, 11)]
COLS = (["CNT", "CNTSCHID", "W_FSTUWT", "ESCS",
         "ST273Q06JA", "ST273Q07JA",
         "ST326Q04JA", "ST326Q05JA", "ST326Q06JA",
         "ST322Q01JA", "ST322Q07JA", "IC171Q02JA"] + PVS)

print("reading PISA 2022 student file (selected columns)...")
df, meta = pyreadstat.read_sav(F, usecols=COLS)
print("rows:", len(df))

OECD = {"AUS","AUT","BEL","CAN","CHL","COL","CRI","CZE","DNK","EST","FIN","FRA","DEU",
        "GRC","HUN","ISL","IRL","ISR","ITA","JPN","KOR","LVA","LTU","LUX","MEX","NLD",
        "NZL","NOR","POL","PRT","SVK","SVN","ESP","SWE","CHE","TUR","GBR","USA"}
df["oecd"] = df.CNT.isin(OECD)

# ST273Q06JA codebook: 1=Every lesson, 2=Most lessons, 3=Some lessons, 4=Never/almost never
df["distr_high"] = np.where(df.ST273Q06JA.isin([1, 2]), 1.0,
                            np.where(df.ST273Q06JA.isin([3, 4]), 0.0, np.nan))
df["distr_any"] = np.where(df.ST273Q06JA.isin([1, 2, 3]), 1.0,
                           np.where(df.ST273Q06JA == 4, 0.0, np.nan))
# ST326 leisure hours/day categories: 1=None ... 8=More than 7 hours (per codebook ordering)
df["leis_school"] = df.ST326Q04JA   # leisure at school
df["leis_after"] = df.ST326Q05JA    # leisure before/after school

def rubin_ols(d, formula_tmpl, coef, w="W_FSTUWT", cluster="CNTSCHID"):
    """Run OLS once per plausible value; combine via Rubin's rules."""
    bs, vs = [], []
    for pv in PVS:
        m = smf.wls(formula_tmpl.format(pv=pv), data=d, weights=d[w]).fit(
            cov_type="cluster", cov_kwds={"groups": d[cluster]})
        bs.append(m.params[coef]); vs.append(m.bse[coef] ** 2)
    bs, vs = np.array(bs), np.array(vs)
    b = bs.mean()
    var = vs.mean() + (1 + 1 / len(bs)) * bs.var(ddof=1)
    return b, np.sqrt(var)

out = {}
print("\n## 1. Distraction (most/every lesson vs never/some) -> math, ESCS-adjusted")
res = {}
for name, d in [("USA", df[(df.CNT == "USA")]), ("OECD pool", df[df.oecd])]:
    d = d.dropna(subset=["distr_high", "ESCS", "W_FSTUWT"])
    extra = " + C(CNT)" if name != "USA" else ""
    b, se = rubin_ols(d, "{pv} ~ distr_high + ESCS + I(ESCS**2)" + extra, "distr_high")
    res[name] = (b, se, len(d))
    print(f"  {name}: b = {b:+.1f} (se {se:.1f}), n = {len(d):,}")
out["distraction_adj"] = {k: {"b": round(v[0], 1), "se": round(v[1], 1), "n": v[2]}
                          for k, v in res.items()}

print("\n## 2. Leisure screen hours at school (5+ hrs/day vs <=1) -> math, ESCS-adjusted")
# categories: 1 none, 2 up to 1hr, 3 1-2, 4 2-3, 5 3-4, 6 4-5, 7 5-6, 8 6-7, 9 >7 (verify range)
print("  leisure-at-school category counts (USA):")
print(df[df.CNT == "USA"].leis_school.value_counts().sort_index().to_string())
df["leis_high"] = np.where(df.leis_school.between(7, 9), 1.0,
                           np.where(df.leis_school.between(1, 2), 0.0, np.nan))
# ST326/ST322 were not administered in the USA (0 nonmissing) -> OECD-subset analyses only
df["phone_daily"] = np.where(df.IC171Q02JA == 5, 1.0,
                             np.where(df.IC171Q02JA.isin([1, 2, 3, 4, 6]), 0.0, np.nan))
res2 = {}
for name, dd in [("OECD subset w/ ST326", df[df.oecd]),
                 ("USA smartphone several-times-daily (IC171)", df[df.CNT == "USA"])]:
    var = "leis_high" if "ST326" in name else "phone_daily"
    dd = dd.dropna(subset=[var, "ESCS", "W_FSTUWT"])
    if len(dd) == 0:
        print(f"  {name}: no data"); continue
    extra = " + C(CNT)" if "OECD" in name else ""
    b, se = rubin_ols(dd, "{pv} ~ " + var + " + ESCS + I(ESCS**2)" + extra, var)
    res2[name] = (b, se, len(dd))
    print(f"  {name}: b = {b:+.1f} (se {se:.1f}), n = {len(dd):,}")
out["leisure_adj"] = {k: {"b": round(v[0], 1), "se": round(v[1], 1), "n": v[2]}
                      for k, v in res2.items()}

print("\n## 3. Distributional tie-in: distraction & leisure use by within-country math quartile (weighted, OECD)")
d = df[df.oecd].dropna(subset=["W_FSTUWT"]).copy()
d["q"] = d.groupby("CNT")["PV1MATH"].transform(
    lambda x: pd.qcut(x, 4, labels=["Q1 (bottom)", "Q2", "Q3", "Q4 (top)"]))
def wmean(s, w):
    s = pd.Series(np.asarray(s, dtype=float), index=w.index)
    m = s.notna() & w.notna()
    return np.average(s[m], weights=w[m]) if m.any() else np.nan
rows = []
for q, g in d.groupby("q", observed=True):
    rows.append({"quartile": str(q),
                 "pct distracted most/every": round(100 * wmean(g.distr_high, g.W_FSTUWT), 1),
                 "pct leisure 5+hr at school": round(100 * wmean(g.leis_high.where(g.leis_high.notna()), g.W_FSTUWT), 1),
                 "pct anxious w/o device": round(100 * wmean(
                     np.where(g.ST322Q07JA.isin([4, 5]), 1.0,
                              np.where(g.ST322Q07JA.isin([1, 2, 3]), 0.0, np.nan)),
                     g.W_FSTUWT), 1),
                 "pct notif off in class": round(100 * wmean(
                     np.where(g.ST322Q01JA.isin([4, 5]), 1.0,
                              np.where(g.ST322Q01JA.isin([1, 2, 3]), 0.0, np.nan)),
                     g.W_FSTUWT), 1)})
t = pd.DataFrame(rows)
print(t.to_markdown(index=False))
out["by_quartile_oecd"] = rows

rows_us = []
du = d[d.CNT == "USA"]
for q, g in du.groupby("q", observed=True):
    rows_us.append({"quartile": str(q),
                    "pct distracted most/every": round(100 * wmean(g.distr_high, g.W_FSTUWT), 1),
                    "pct smartphone several times daily": round(100 * wmean(g.phone_daily, g.W_FSTUWT), 1)})
print("\nUSA:")
print(pd.DataFrame(rows_us).to_markdown(index=False))
out["by_quartile_usa"] = rows_us

print("\n## 3b. USA IC171 category gradient (ESCS-adjusted adjusted means rel. to 'never')")
du2 = df[(df.CNT == "USA")].dropna(subset=["IC171Q02JA", "ESCS", "W_FSTUWT"])
du2 = du2[du2.IC171Q02JA.between(1, 6)]
labs = {1:"never/almost never",2:"1-2x month",3:"1-2x week",4:"daily",5:"several times daily",6:"no access"}
du2["cat"] = du2.IC171Q02JA.map(labs)
m = smf.wls("PV1MATH ~ C(cat, Treatment(reference='never/almost never')) + ESCS + I(ESCS**2)",
            data=du2, weights=du2.W_FSTUWT).fit(cov_type="cluster", cov_kwds={"groups": du2.CNTSCHID})
for k, v in m.params.items():
    if "cat" in k:
        print(f"  {k.split('T.')[-1].rstrip(']')}: {v:+.1f}")
out["usa_ic171_gradient"] = {k.split("T.")[-1].rstrip("]"): round(v, 1)
                             for k, v in m.params.items() if "cat" in k}

print("\n## 4. ESCS-gradient of exposure (OECD): distraction prevalence by ESCS quartile")
d = d.dropna(subset=["ESCS"])
d["escs_q"] = d.groupby("CNT")["ESCS"].transform(
    lambda x: pd.qcut(x, 4, labels=["E1 (low)", "E2", "E3", "E4 (high)"]))
rows_e = []
for q, g in d.groupby("escs_q", observed=True):
    rows_e.append({"ESCS quartile": str(q),
                   "pct distracted most/every": round(100 * wmean(g.distr_high, g.W_FSTUWT), 1),
                   "pct leisure 5+hr at school": round(100 * wmean(g.leis_high, g.W_FSTUWT), 1)})
print(pd.DataFrame(rows_e).to_markdown(index=False))
out["by_escs_oecd"] = rows_e

with open("data/pisa_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nsaved data/pisa_results.json")
