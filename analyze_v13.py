"""v1.3 robustness & inference upgrade.

1. Waiver DiD: permutation (randomization) inference, joint pre-trend test,
   and minimum detectable effect (MDE) vs the Dee-Jacob NCLB benchmark.
2. Public-Catholic divergence: z-tests using published NAEP standard errors
   (Digest dt19_222.32a: Catholic G8 math SE 1.6, G4 1.3; public 0.2-0.3;
   2022/2024 Catholic SE assumed 2.5 conservatively).
3. Dose-response robustness: enrollment-weighted WLS, exclude DC.
"""
import json
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

rng = np.random.default_rng(20260609)
out = {}

# ---------- 1. Waiver permutation inference ----------
v11 = pd.read_csv("data/naep_v11.csv")
w = pd.read_csv("data/waivers.csv")
stp = v11[(v11.dataset == "statepct") & (v11.displayable == 1)].copy()
stp = stp.merge(w[["state", "first_sy_end", "group"]],
                left_on="jurisdiction", right_on="state", how="left")
panel = stp[(stp.year <= 2019) & (stp.stat == "PC:P1")].copy()
panel["cell"] = panel.subject + "_" + panel.grade.astype(str)
panel["z"] = panel.groupby("cell")["value"].transform(lambda x: (x - x.mean()) / x.std())

states = sorted(panel.jurisdiction.unique())
# observed assignment tuples (first_sy_end or nan, revoked flag)
assign_obs = {r.state: (r.first_sy_end, r.group == "revoked")
              for r in w.itertuples() if r.state in states}
tuples = list(assign_obs.values())

def beta_post(df, assign):
    df = df.copy()
    df["fse"] = df.jurisdiction.map({s: a[0] for s, a in assign.items()})
    df["revoked"] = df.jurisdiction.map({s: a[1] for s, a in assign.items()})
    df["post"] = ((df.fse.notna()) & (df.year >= df.fse)).astype(int)
    df = df[~((df.revoked) & (df.year >= 2015))]
    m = smf.ols("z ~ post + C(jurisdiction) + C(year) + C(cell)", data=df).fit()
    return m.params["post"]

b_obs = beta_post(panel, assign_obs)
B = 2000
perm = np.empty(B)
for i in range(B):
    shuffled = rng.permutation(len(tuples))
    assign_p = {s: tuples[shuffled[j]] for j, s in enumerate(states)}
    perm[i] = beta_post(panel, assign_p)
p_perm = float((np.abs(perm) >= abs(b_obs)).mean())
mde = 2.8 * perm.std()  # ~80% power, 5% two-sided
print(f"Waiver DiD pooled P10 (z): beta_obs={b_obs:+.3f}, permutation p={p_perm:.3f} "
      f"(B={B}), sd(perm)={perm.std():.3f}, MDE80={mde:.3f} z")
out["permutation"] = {"beta_obs_z": round(b_obs, 3), "p_perm": p_perm,
                      "sd_perm": round(float(perm.std()), 3),
                      "MDE80_z": round(float(mde), 3)}

# points version for G8 math (for benchmark comparison)
g8 = panel[panel.cell.str.startswith("MAT_8")].copy()
def beta_pts(df, assign):
    df = df.copy()
    df["fse"] = df.jurisdiction.map({s: a[0] for s, a in assign.items()})
    df["revoked"] = df.jurisdiction.map({s: a[1] for s, a in assign.items()})
    df["post"] = ((df.fse.notna()) & (df.year >= df.fse)).astype(int)
    df = df[~((df.revoked) & (df.year >= 2015))]
    return smf.ols("value ~ post + C(jurisdiction) + C(year)", data=df).fit().params["post"]
b8 = beta_pts(g8, assign_obs)
perm8 = np.empty(B)
for i in range(B):
    shuffled = rng.permutation(len(tuples))
    assign_p = {s: tuples[shuffled[j]] for j, s in enumerate(states)}
    perm8[i] = beta_pts(g8, assign_p)
p8 = float((np.abs(perm8) >= abs(b8)).mean())
mde8 = 2.8 * perm8.std()
print(f"Waiver DiD G8 math P10 (points): beta={b8:+.2f}, perm p={p8:.3f}, "
      f"MDE80={mde8:.2f} points")
out["permutation_g8math_pts"] = {"beta_obs": round(b8, 2), "p_perm": p8,
                                 "MDE80_pts": round(float(mde8), 2)}

# joint pre-trend test (early vs never, pooled z)
ev = panel[panel.group_y.isin(["early", "never"])].copy()
ev["treat"] = (ev.group_y == "early").astype(int)
yrs = sorted(ev.year.unique())
terms = []
for y in yrs:
    if y == 2011:
        continue
    ev[f"tX{y}"] = ev.treat * (ev.year == y).astype(int)
    terms.append(f"tX{y}")
m2 = smf.ols("z ~ " + " + ".join(terms) + " + C(jurisdiction) + C(year) + C(cell)",
             data=ev).fit(cov_type="cluster", cov_kwds={"groups": ev["jurisdiction"]})
pre = [t for t in terms if int(t[2:]) < 2011]
wald = m2.wald_test([f"{t} = 0" for t in pre], scalar=True)
print(f"Pre-trend joint test ({len(pre)} coefs 2003-2009): "
      f"stat={float(wald.statistic):.2f}, p={float(wald.pvalue):.3f}")
out["pretrend"] = {"stat": round(float(wald.statistic), 2),
                   "p": round(float(wald.pvalue), 3)}

# ---------- 2. Public-Catholic z-tests (published SEs) ----------
# SEs: Digest dt19_222.32a -> Catholic G8 math 1.6, G4 1.3; public 0.3/0.2 (2019).
# Assume same magnitudes for 2013/reading; assume 2.5 for Catholic 2022/2024 (smaller samples).
res = json.load(open("data/v11_results.json"))
pc = pd.DataFrame(res["public_catholic_means"])
SE = {"Public": {"any": 0.3}, "Catholic": {"pre": 1.6, "post": 2.5}}
print("\nPublic-Catholic inference (approx, published SEs):")
sector_tests = []
for series in pc.series.unique():
    sub = pc[pc.series == series].set_index("group")
    d_cath_pre = sub.loc["Catholic", "chg_2013_2019"]
    se_cath_pre = np.sqrt(1.6**2 + 1.6**2)
    z1 = d_cath_pre / se_cath_pre
    dd_recov = sub.loc["Public", "chg_2019_2024"] - sub.loc["Catholic", "chg_2019_2024"]
    se_dd = np.sqrt(0.3**2 + 0.3**2 + 1.6**2 + 2.5**2)
    z2 = dd_recov / se_dd
    sector_tests.append({"series": series,
                         "cath_chg_2013_19": d_cath_pre, "z": round(z1, 2),
                         "dd_2019_24_pub_minus_cath": round(dd_recov, 1),
                         "z_dd": round(z2, 2)})
    print(f"  {series}: Catholic 2013-19 {d_cath_pre:+.1f} (z={z1:.2f}); "
          f"2019-24 divergence pub-cath {dd_recov:+.1f} (z={z2:.2f})")
out["sector_tests"] = sector_tests

# ---------- 3. Dose-response robustness ----------
main = pd.read_csv("data/naep_main.csv")
st = main[(main.dataset == "state") & (main.displayable == 1)]
rsubj = [s for s in st.subject.unique() if s != "MAT"][0]
csdh = pd.read_csv("data/external/CSDH_state_learning_model_shares_2020_21.csv").set_index("StateAbbrev")
rows = []
for key, label in [(("MAT", 4), "Math G4"), (("MAT", 8), "Math G8"),
                   ((rsubj, 4), "Reading G4"), ((rsubj, 8), "Reading G8")]:
    pv = st[(st.subject == key[0]) & (st.grade == key[1])].pivot_table(
        index="jurisdiction", columns="year", values="value")
    m = pd.DataFrame({"d_1922": pv[2022] - pv[2019]}).join(csdh, how="inner").dropna()
    m_noDC = m[m.index != "DC"]
    r_w = smf.wls("d_1922 ~ share_virtual", data=m, weights=m.total_enrollment).fit(cov_type="HC1")
    r_n = smf.ols("d_1922 ~ share_virtual", data=m_noDC).fit(cov_type="HC1")
    rows.append({"series": label,
                 "WLS b/10pp": round(r_w.params["share_virtual"] / 10, 2),
                 "p_wls": round(r_w.pvalues["share_virtual"], 3),
                 "noDC b/10pp": round(r_n.params["share_virtual"] / 10, 2),
                 "p_noDC": round(r_n.pvalues["share_virtual"], 3)})
print("\nDose-response robustness:")
print(pd.DataFrame(rows).to_markdown(index=False))
out["dose_robustness"] = rows

with open("data/v13_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nv1.3 results saved")
