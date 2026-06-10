"""Clean-room replication: PISA 2022 math gap by digital-device distraction (ST273Q06JA).

Spec decisions (stated for transparency):
- "Distracted" = ST273Q06JA in {1 'Every lesson', 2 'Most lessons'} (coding read from file
  metadata; 1 = most frequent). Codes 95/97/98/99 treated as missing.
- Drop rows missing ST273Q06JA always; adjusted models additionally require ESCS non-missing.
  Unadjusted models are run on the same ESCS-non-missing sample? NO -> unadjusted run on the
  distraction-non-missing sample (max sample); adjusted on the ESCS-complete subset.
- Weights: final student weights W_FSTUWT for USA. For pooled OECD: SENATE weights
  (W_FSTUWT rescaled so each country contributes equally, sum = 5000 per country),
  with country fixed effects.
- PVs: all 10 PV*MATH combined by Rubin's rules: point = mean of 10 estimates;
  total var = mean(within var) + (1 + 1/10) * var(between, ddof=1).
- SEs: cluster-robust by CNTSCHID within each PV regression (statsmodels WLS, cov_type
  'cluster'). Note: this is not BRR replicate weights (PISA's official method), so SEs
  will differ somewhat from official OECD-method SEs.
- Adjusted model: PV ~ distracted + ESCS + ESCS^2 (+ C(CNT) for pooled).
"""
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.api as sm

SAV = "data/external/pisa/CY08MSP_STU_QQQ.SAV"
OUT = "verification/cleanroom/pisa/results.json"

PVS = [f"PV{i}MATH" for i in range(1, 11)]
COLS = ["CNT", "CNTSCHID", "OECD", "ST273Q06JA", "ESCS", "W_FSTUWT"] + PVS

print("Loading SAV (usecols)...", flush=True)
df, meta = pyreadstat.read_sav(SAV, usecols=COLS)
print("rows:", len(df), flush=True)

# --- clean distraction item ---
d = df["ST273Q06JA"]
d = d.where(~d.isin([95.0, 97.0, 98.0, 99.0]))
df["distracted"] = np.where(d.isna(), np.nan, (d <= 2.0).astype(float))

# ESCS missing codes (continuous; SPSS user-missing usually 95/97/98/99 too)
df.loc[df["ESCS"].isin([95.0, 97.0, 98.0, 99.0]), "ESCS"] = np.nan

usa = df[(df["CNT"] == "USA") & df["distracted"].notna()].copy()
oecd = df[(df["OECD"] == 1.0) & df["distracted"].notna()].copy()

# senate weights for pooled OECD: each country sums to 5000
oecd["senwt"] = oecd.groupby("CNT")["W_FSTUWT"].transform(lambda w: w / w.sum() * 5000.0)

def wshare(sub, w="W_FSTUWT"):
    return float(np.average(sub["distracted"], weights=sub[w]))

def rubin(estimates, variances):
    estimates = np.asarray(estimates); variances = np.asarray(variances)
    q = estimates.mean()
    within = variances.mean()
    between = estimates.var(ddof=1)
    tot = within + (1 + 1 / len(estimates)) * between
    return q, float(np.sqrt(tot))

def run(sub, weightcol, adjusted, country_fe):
    ests, vars_ = [], []
    X_parts = [sub["distracted"]]
    if adjusted:
        X_parts += [sub["ESCS"], sub["ESCS"] ** 2]
    X = pd.concat(X_parts, axis=1)
    X.columns = ["distracted"] + (["ESCS", "ESCS2"] if adjusted else [])
    if country_fe:
        dums = pd.get_dummies(sub["CNT"], drop_first=True, dtype=float)
        X = pd.concat([X, dums], axis=1)
    X = sm.add_constant(X)
    for pv in PVS:
        m = sm.WLS(sub[pv], X, weights=sub[weightcol]).fit(
            cov_type="cluster", cov_kwds={"groups": sub["CNTSCHID"]})
        ests.append(m.params["distracted"])
        vars_.append(m.bse["distracted"] ** 2)
    est, se = rubin(ests, vars_)
    return {"estimate": round(float(est), 3), "se": round(se, 3), "n": int(len(sub))}

results = {
    "item": "ST273Q06JA",
    "item_label": meta.column_names_to_labels["ST273Q06JA"],
    "value_labels": {str(k): v for k, v in meta.variable_value_labels["ST273Q06JA"].items()},
    "distracted_definition": "ST273Q06JA in {1 Every lesson, 2 Most lessons}; 95/97/98/99 missing",
    "pooled_oecd_weighting": "senate weights (W_FSTUWT rescaled to sum 5000 per country) + country FE",
    "se_method": "cluster-robust by CNTSCHID within each PV; Rubin's rules across 10 PVs (not BRR)",
}

results["share_distracted"] = {
    "usa_weighted": round(wshare(usa), 4),
    "oecd_senate_weighted": round(wshare(oecd, "senwt"), 4),
    "oecd_raw_weighted": round(wshare(oecd), 4),
}

usa_adj = usa[usa["ESCS"].notna()]
oecd_adj = oecd[oecd["ESCS"].notna()]

print("USA unadjusted...", flush=True)
results["usa_unadjusted"] = run(usa, "W_FSTUWT", adjusted=False, country_fe=False)
print("USA adjusted...", flush=True)
results["usa_adjusted_escs_quadratic"] = run(usa_adj, "W_FSTUWT", adjusted=True, country_fe=False)
print("OECD unadjusted...", flush=True)
results["oecd_unadjusted"] = run(oecd, "senwt", adjusted=False, country_fe=True)
print("OECD adjusted...", flush=True)
results["oecd_adjusted_escs_quadratic"] = run(oecd_adj, "senwt", adjusted=True, country_fe=True)

results["n_oecd_countries"] = int(oecd["CNT"].nunique())

with open(OUT, "w") as fh:
    json.dump(results, fh, indent=2)
print(json.dumps(results, indent=2))
