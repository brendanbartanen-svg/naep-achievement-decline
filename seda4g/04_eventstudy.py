#!/usr/bin/env python3
"""
04_eventstudy.py — Headline analysis: 4G/LTE rollout (NTIA SBDD) x SEDA 5.0 county test scores.

Estimators (see docs/seda4g_design.md):
  1. Manual Callaway-Sant'Anna-style ATT(g,t), aggregated to event time theta(e),
     county-block bootstrap CIs; "full" vs "restricted" (not-yet-treated controls exist) versions.
  2. TWFE continuous dose (share_mobile_t7) with county FE + state x year x grade x subject FE,
     cluster by state; distributed-lag variant (years-since-50% dummies 0/1/2/3+).
  3. Adolescent-exposure gradient: years_exposed with county x year FE + grade x subject x year FE.
  4. Permutation inference (500 draws, within-state) for dose & gradient coefficients.
  5. Robustness grid for the pooled TWFE coefficient.

Outputs: seda4g/eventstudy_results.json, figures/fig_4g_eventstudy.pdf
Units: SEDA CS scale = SD units of the national reference-cohort student-level distribution.
"""

import json
import os
import sys
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats as sps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEDA4G = os.path.join(ROOT, "seda4g")
FIGDIR = os.path.join(ROOT, "figures")
os.makedirs(FIGDIR, exist_ok=True)

RNG_BOOT = np.random.default_rng(20260610)
RNG_PERM = np.random.default_rng(46101962)
N_BOOT = 200
N_PERM = 500
NEVER = 9999
YEARS = list(range(2009, 2020))
YIDX = {y: i for i, y in enumerate(YEARS)}
ARTIFACT_STATES = ["CO", "MO", "UT", "NH", "HI"]


def make_figure(pooled_cs):
    """Event-study figure from the pooled CS results dict {full/restricted: {theta_e: ...}}."""
    fig, ax = plt.subplots(figsize=(9, 5.5))
    colors = {"full": "#1f77b4", "restricted": "#d62728"}
    offs = {"full": -0.08, "restricted": 0.08}
    labels = {"full": "Full (controls incl. never-treated only for t≥2015)",
              "restricted": "Restricted (not-yet-treated controls exist, max(t,g)≤2014)"}
    for ver in ["full", "restricted"]:
        th = pooled_cs[ver]["theta_e"]
        es = sorted(int(e) for e in th if -4 <= int(e) <= 6)
        x = [e + offs[ver] for e in es]
        y = [th[str(e)]["theta"] for e in es]
        lo = [th[str(e)]["ci95_lo"] for e in es]
        hi = [th[str(e)]["ci95_hi"] for e in es]
        yerr = [[yi - (li if li is not None else yi) for yi, li in zip(y, lo)],
                [(hi_ if hi_ is not None else yi) - yi for yi, hi_ in zip(y, hi)]]
        ax.errorbar(x, y, yerr=yerr, fmt="o", ms=4.5, capsize=2.5, lw=1.2,
                    color=colors[ver], label=labels[ver])
    ax.plot([-1], [0], marker="o", ms=5.5, mfc="white", mec="0.3", ls="none",
            label="θ(−1) = 0 (reference period, by construction)")
    ax.axhline(0, color="0.4", lw=0.8)
    ax.axvline(-0.5, color="0.6", lw=0.8, ls="--")
    ax.text(-0.45, ax.get_ylim()[1] * 0.92, "treatment (e=0)", fontsize=8, color="0.4")
    ax.set_xlabel("Event time e = test year − first treated test year (t7 ≥ 50% coverage)")
    ax.set_ylabel("θ(e), SEDA CS scale (SD of national reference cohort)")
    ax.set_title("4G/LTE rollout and county test scores: CS-style event study\n"
                 "(math+RLA pooled, grades 3–8; cohort weights = treated population; "
                 "95% CI from 200-draw county block bootstrap)", fontsize=10)
    ax.legend(fontsize=8, loc="lower left")
    ax.set_xticks(range(-4, 7))
    fig.tight_layout()
    fig.savefig(os.path.join(FIGDIR, "fig_4g_eventstudy.pdf"))
    print("  wrote figures/fig_4g_eventstudy.pdf")


if "--figure-only" in sys.argv:
    with open(os.path.join(SEDA4G, "eventstudy_results.json")) as _f:
        _res = json.load(_f)
    make_figure(_res["cs_att"]["pooled"])
    sys.exit(0)

# ----------------------------------------------------------------------------- load
print("Loading inputs ...")
td = pd.read_csv(os.path.join(SEDA4G, "treatment_dates.csv"), dtype={"county_fips": str})
panel = pd.read_csv(os.path.join(SEDA4G, "exposure_county_panel_national.csv"),
                    dtype={"county_fips": str})
seda = pd.read_csv(
    os.path.join(ROOT, "data/external/seda4g/seda_county_long_cs_5.0.csv"),
    usecols=["sedacounty", "stateabb", "subject", "grade", "year",
             "cs_mn_all", "cs_mn_se_all", "tot_asmt_all"],
)
seda["county_fips"] = seda["sedacounty"].astype(str).str.zfill(5)

def cohort_from_date(s):
    """g = wave_year + 1 for both June and December waves (first spring test after coverage)."""
    if pd.isna(s):
        return NEVER
    return int(str(s)[:4]) + 1

CODINGS = ["first_t6_25", "first_t6_50", "first_t6_75",
           "first_t7_25", "first_t7_50", "first_t7_75"]
for c in CODINGS:
    td["g_" + c] = td[c].map(cohort_from_date)

# Verizon-only t6 crossing, recomputed from the panel
vz = panel.pivot(index="county_fips", columns="wave", values="share_mobile_t6_vzw")
vz = vz[sorted(vz.columns)]
first_vzw = {}
for cf, row in vz.iterrows():
    hit = [w for w, v in row.items() if pd.notna(v) and v >= 0.5]
    first_vzw[cf] = cohort_from_date(hit[0]) if hit else NEVER
td["g_first_t6_50_vzw"] = td["county_fips"].map(first_vzw).fillna(NEVER).astype(int)

# merge diagnostics
seda_counties = set(seda["county_fips"].unique())
tx_counties = set(td["county_fips"])
matched = seda_counties & tx_counties
merge_diag = {
    "seda_counties": len(seda_counties),
    "treatment_counties": len(tx_counties),
    "matched_counties": len(matched),
    "merge_rate_seda_counties": len(matched) / len(seda_counties),
    "merge_rate_seda_rows": float(seda["county_fips"].isin(tx_counties).mean()),
    "unmatched_seda_counties": sorted(seda_counties - tx_counties),
}
print(f"Merge: {len(matched)}/{len(seda_counties)} SEDA counties "
      f"({merge_diag['merge_rate_seda_counties']:.4f}); "
      f"row match {merge_diag['merge_rate_seda_rows']:.4f}")

df = seda[seda["county_fips"].isin(matched)].copy()
df = df[df["cs_mn_all"].notna() & (df["tot_asmt_all"] > 0)]
tdm = td.set_index("county_fips")
df["g_primary"] = df["county_fips"].map(tdm["g_first_t7_50"]).astype(int)
df["county_pop"] = df["county_fips"].map(tdm["county_pop"])

cohort_sizes = {}
tdm_m = tdm.loc[sorted(matched)]
for g, grp in tdm_m.groupby("g_first_t7_50"):
    key = "never" if g == NEVER else str(g)
    cohort_sizes[key] = {"n_counties": int(len(grp)), "pop": int(grp["county_pop"].sum()),
                         "pop_share": float(grp["county_pop"].sum() / tdm_m["county_pop"].sum())}
print("Cohorts (g = first_t7_50):", {k: v["n_counties"] for k, v in cohort_sizes.items()})

# =============================================================================
# 1. Callaway-Sant'Anna-style ATT(g,t)
# =============================================================================
print("\n[1] CS-style ATT(g,t) ...")

def county_year_matrices(d):
    """Return (Y, W, fips_list): county x year tot_asmt-weighted mean of cs_mn_all and weight sums."""
    d = d.copy()
    d["wy"] = d["cs_mn_all"] * d["tot_asmt_all"]
    agg = d.groupby(["county_fips", "year"]).agg(wy=("wy", "sum"), w=("tot_asmt_all", "sum"))
    agg["ybar"] = agg["wy"] / agg["w"]
    Yp = agg["ybar"].unstack("year").reindex(columns=YEARS)
    Wp = agg["w"].unstack("year").reindex(columns=YEARS)
    fips = Yp.index.to_numpy()
    return Yp.to_numpy(), Wp.fillna(0.0).to_numpy(), fips

def wmean(x, w, m):
    sw = w[m].sum()
    return np.nan if sw <= 0 else float((x[m] * w[m]).sum() / sw)

def att_gt(Y, W, cohort, g, t, restricted):
    """ATT(g,t) with base period g-1; controls = never + cohorts > max(t,g).
    restricted: only keep comparisons where not-yet-treated controls exist (max(t,g) <= 2014)."""
    base = g - 1
    if t == base or t not in YIDX or base not in YIDX:
        return None
    if restricted and max(t, g) > 2014:
        return None
    it, ib = YIDX[t], YIDX[base]
    dY = Y[:, it] - Y[:, ib]
    ok = ~np.isnan(dY) & (W[:, ib] > 0)
    w = W[:, ib]                      # base-period tot_asmt as county weight
    treated = ok & (cohort == g)
    ctrl = ok & ((cohort == NEVER) | (cohort > max(t, g)))
    if treated.sum() == 0 or ctrl.sum() == 0:
        return None
    return wmean(dY, w, treated) - wmean(dY, w, ctrl), treated, ctrl

def theta_e(Y, W, cohort, pop, restricted, collect_gt=False):
    """Aggregate ATT(g,t) to event time, cohorts weighted by treated population."""
    acc = {}   # e -> [(att, popw, g, t)]
    gts = []
    for g in range(2011, 2016):
        for t in YEARS:
            r = att_gt(Y, W, cohort, g, t, restricted)
            if r is None:
                continue
            att, tmask, cmask = r
            pw = float(pop[tmask].sum())
            e = t - g
            acc.setdefault(e, []).append((att, pw))
            if collect_gt:
                gts.append({"g": g, "t": t, "att": att, "n_treated": int(tmask.sum()),
                            "n_control": int(cmask.sum()),
                            "n_never_in_control": int((cohort[cmask] == NEVER).sum()),
                            "treated_pop": pw})
    out = {}
    for e, items in acc.items():
        atts = np.array([a for a, _ in items])
        ws = np.array([p for _, p in items])
        out[e] = float((atts * ws).sum() / ws.sum())
    return (out, gts) if collect_gt else out

results_cs = {}
cs_inputs = {}
for subj_key, dsub in [("pooled", df), ("mth", df[df["subject"] == "mth"]),
                       ("rla", df[df["subject"] == "rla"])]:
    Y, W, fips = county_year_matrices(dsub)
    cohort = tdm.loc[fips, "g_first_t7_50"].to_numpy().astype(int)
    pop = tdm.loc[fips, "county_pop"].to_numpy().astype(float)
    cs_inputs[subj_key] = (Y, W, cohort, pop)
    res = {}
    for ver, restr in [("full", False), ("restricted", True)]:
        th, gts = theta_e(Y, W, cohort, pop, restr, collect_gt=True)
        # county-block bootstrap
        n = len(fips)
        boot = {e: [] for e in th}
        for b in range(N_BOOT):
            idx = RNG_BOOT.integers(0, n, n)
            thb = theta_e(Y[idx], W[idx], cohort[idx], pop[idx], restr)
            for e in th:
                boot[e].append(thb.get(e, np.nan))
        out = {}
        for e in sorted(th):
            bb = np.array(boot[e], float)
            bb = bb[~np.isnan(bb)]
            out[str(e)] = {
                "theta": th[e],
                "se_boot": float(bb.std(ddof=1)) if len(bb) > 10 else None,
                "ci95_lo": float(np.percentile(bb, 2.5)) if len(bb) > 10 else None,
                "ci95_hi": float(np.percentile(bb, 97.5)) if len(bb) > 10 else None,
                "n_boot_valid": int(len(bb)),
            }
        res[ver] = {"theta_e": out, "att_gt": gts}
        npost = [th[e] for e in th if e >= 0]
        print(f"  {subj_key:6s} {ver:10s}: theta(0)={th.get(0, np.nan):+.4f}  "
              f"mean theta(e>=0)={np.mean(npost):+.4f}  "
              f"mean theta(e<0,e!=-1)={np.mean([th[e] for e in th if e < -1]):+.4f}")
    results_cs[subj_key] = res

# =============================================================================
# FE machinery: weighted alternating projections (absorb two grouped FE sets)
# =============================================================================
def make_gid(*cols):
    key = cols[0].astype(str)
    for c in cols[1:]:
        key = key + "_" + c.astype(str)
    return pd.factorize(key)[0]

def demean_two(X, w, g1, g2, tol=1e-10, max_iter=200):
    """Weighted demeaning by two FE groupings, alternating projections. X: (n,) or (n,k)."""
    X = np.array(X, dtype=float, copy=True)
    one_d = X.ndim == 1
    if one_d:
        X = X[:, None]
    sw1 = np.bincount(g1, weights=w)
    sw2 = np.bincount(g2, weights=w)
    for _ in range(max_iter):
        delta = 0.0
        for g, sw in ((g1, sw1), (g2, sw2)):
            for k in range(X.shape[1]):
                m = np.bincount(g, weights=w * X[:, k]) / sw
                X[:, k] -= m[g]
                delta = max(delta, np.abs(m).max())
        if delta < tol:
            break
    return X[:, 0] if one_d else X

def cluster_ols(Xd, yd, w, clu, k_absorbed=0):
    """Weighted OLS on demeaned data with cluster-robust (CR1) SEs. Xd: (n,k)."""
    if Xd.ndim == 1:
        Xd = Xd[:, None]
    XtWX = Xd.T @ (Xd * w[:, None])
    XtWy = Xd.T @ (yd * w)
    beta = np.linalg.solve(XtWX, XtWy)
    resid = yd - Xd @ beta
    G = len(np.unique(clu))
    scores = Xd * (w * resid)[:, None]
    meat = np.zeros((Xd.shape[1], Xd.shape[1]))
    for c in np.unique(clu):
        s = scores[clu == c].sum(axis=0)
        meat += np.outer(s, s)
    Ainv = np.linalg.inv(XtWX)
    V = Ainv @ meat @ Ainv * (G / (G - 1))
    se = np.sqrt(np.diag(V))
    tstat = beta / se
    p = 2 * sps.t.sf(np.abs(tstat), df=G - 1)
    return beta, se, tstat, p, G

# =============================================================================
# 2. TWFE continuous dose
# =============================================================================
print("\n[2] TWFE continuous dose ...")
WAVES = sorted(panel["wave"].unique())  # '2010-06' ... '2014-06'

def wave_for_test_year(t):
    """Latest wave on/before December of the school year (Dec of t-1); carry Jun-2014 fwd for t>=2016."""
    cutoff = f"{t-1}-12"
    elig = [w for w in WAVES if w <= cutoff]
    return elig[-1] if elig else None

dose_map = {t: wave_for_test_year(t) for t in YEARS}
pw = panel.pivot(index="county_fips", columns="wave", values="share_mobile_t7")
dose_by_cy = pd.DataFrame(index=pw.index)
for t in YEARS:
    wv = dose_map[t]
    dose_by_cy[t] = 0.0 if wv is None else pw[wv].fillna(0.0)

reg = df.copy().reset_index(drop=True)
reg["dose_t7"] = dose_by_cy.stack().reindex(
    pd.MultiIndex.from_arrays([reg["county_fips"], reg["year"]])).to_numpy()
reg["dose_t7"] = reg["dose_t7"].fillna(0.0)

g_county = pd.factorize(reg["county_fips"])[0]
g_sygs = make_gid(reg["stateabb"].to_numpy(), reg["year"].to_numpy(),
                  reg["grade"].to_numpy(), reg["subject"].to_numpy())
clu_state = pd.factorize(reg["stateabb"])[0]
w_main = reg["tot_asmt_all"].to_numpy().astype(float)
y_raw = reg["cs_mn_all"].to_numpy().astype(float)

yd_main = demean_two(y_raw, w_main, g_county, g_sygs)

def run_twfe(xraw, w=w_main, yd=yd_main, gc=g_county, gs=g_sygs, clu=clu_state):
    xd = demean_two(xraw, w, gc, gs)
    b, se, ts, p, G = cluster_ols(xd, yd, w, clu)
    return b, se, ts, p, G, xd

b, se, ts, p, G, xd_dose = run_twfe(reg["dose_t7"].to_numpy())
twfe_dose = {"coef": float(b[0]), "se": float(se[0]), "t": float(ts[0]), "p": float(p[0]),
             "n_obs": int(len(reg)), "n_counties": int(len(np.unique(g_county))),
             "n_clusters_state": int(G),
             "fe": "county + state x year x grade x subject",
             "dose_mapping": {str(t): (dose_map[t] or "none->0") for t in YEARS}}
print(f"  dose (share_mobile_t7): {b[0]:+.4f} (se {se[0]:.4f}, p {p[0]:.3f})")

# Distributed-lag: years since t7-50% crossing (0,1,2,3+)
ys = reg["year"].to_numpy() - reg["g_primary"].to_numpy()
ys[reg["g_primary"].to_numpy() == NEVER] = -99
Xdl = np.column_stack([(ys == 0), (ys == 1), (ys == 2), (ys >= 3)]).astype(float)
Xdl_d = demean_two(Xdl, w_main, g_county, g_sygs)
bdl, sedl, tdl, pdl, _, = cluster_ols(Xdl_d, yd_main, w_main, clu_state)[0:5]
twfe_dose["distributed_lag_years_since_t7_50"] = {
    lab: {"coef": float(bdl[i]), "se": float(sedl[i]), "p": float(pdl[i])}
    for i, lab in enumerate(["ys0", "ys1", "ys2", "ys3plus"])}
print("  distributed lag:", {k: round(v["coef"], 4)
      for k, v in twfe_dose["distributed_lag_years_since_t7_50"].items()})

# =============================================================================
# 3. Adolescent-exposure gradient
# =============================================================================
print("\n[3] Exposure gradient (within county-year, across grades) ...")

def years_exposed(gvec, tvec, grvec):
    """# of school years from the cohort's grade-3 spring (t-gr+3) through t with t7-50 crossed."""
    start = tvec - grvec + 3
    lo = np.maximum(gvec, start)
    ye = np.maximum(0, tvec - lo + 1)
    ye[gvec == NEVER] = 0
    return ye.astype(float)

reg["yexp"] = years_exposed(reg["g_primary"].to_numpy(), reg["year"].to_numpy(),
                            reg["grade"].to_numpy())
g_cy = make_gid(reg["county_fips"].to_numpy(), reg["year"].to_numpy())
g_gsy = make_gid(reg["grade"].to_numpy(), reg["subject"].to_numpy(), reg["year"].to_numpy())
yd_grad = demean_two(y_raw, w_main, g_cy, g_gsy)
xd_grad = demean_two(reg["yexp"].to_numpy(), w_main, g_cy, g_gsy)
bg, seg, tg, pg, Gg = cluster_ols(xd_grad, yd_grad, w_main, clu_state)
gradient = {"coef": float(bg[0]), "se": float(seg[0]), "t": float(tg[0]), "p": float(pg[0]),
            "n_obs": int(len(reg)), "n_clusters_state": int(Gg),
            "fe": "county x year + grade x subject x year",
            "mean_yexp": float(reg["yexp"].mean()), "sd_yexp": float(reg["yexp"].std())}
print(f"  years_exposed: {bg[0]:+.5f} (se {seg[0]:.5f}, p {pg[0]:.3f})")

# =============================================================================
# 4. Permutation inference (within-state permutation of treatment assignment)
# =============================================================================
print("\n[4] Permutation inference (%d draws) ..." % N_PERM)
fips_u = pd.Index(pd.unique(reg["county_fips"]))
state_u = reg.groupby("county_fips")["stateabb"].first().reindex(fips_u).to_numpy()
cf_codes = pd.Categorical(reg["county_fips"], categories=fips_u).codes
yr_idx = reg["year"].map(YIDX).to_numpy()
dose_mat = dose_by_cy.reindex(fips_u).fillna(0.0).to_numpy()         # (nc, nyears)
g_vec_u = tdm.reindex(fips_u)["g_first_t7_50"].to_numpy().astype(int)
grade_v = reg["grade"].to_numpy()
year_v = reg["year"].to_numpy()

state_groups = [np.where(state_u == s)[0] for s in np.unique(state_u)]

def perm_indices():
    pidx = np.arange(len(fips_u))
    for grp in state_groups:
        pidx[grp] = grp[RNG_PERM.permutation(len(grp))]
    return pidx

perm_dose, perm_grad = [], []
for i in range(N_PERM):
    pidx = perm_indices()
    # dose: permute counties' whole exposure trajectory within state
    xp = dose_mat[pidx][cf_codes, yr_idx]
    xpd = demean_two(xp, w_main, g_county, g_sygs)
    bswx = float((w_main * xpd * yd_main).sum() / (w_main * xpd * xpd).sum())
    perm_dose.append(bswx)
    # gradient: permute the t7-50 crossing year within state
    gp = g_vec_u[pidx][cf_codes]
    xg = years_exposed(gp, year_v, grade_v)
    xgd = demean_two(xg, w_main, g_cy, g_gsy)
    perm_grad.append(float((w_main * xgd * yd_grad).sum() / (w_main * xgd * xgd).sum()))
    if (i + 1) % 100 == 0:
        print(f"    {i+1}/{N_PERM}")

def perm_summary(actual, draws):
    d = np.array(draws)
    return {"actual": float(actual),
            "perm_p_two_sided": float((np.abs(d) >= abs(actual)).mean()),
            "sd_perm": float(d.std(ddof=1)),
            "mde80": float(2.8 * d.std(ddof=1)),
            "n_perms": int(len(d)),
            "perm_mean": float(d.mean())}

permutation = {"dose_t7": perm_summary(twfe_dose["coef"], perm_dose),
               "gradient_years_exposed": perm_summary(gradient["coef"], perm_grad),
               "scheme": "counties' entire treatment vector (dose trajectory / crossing year) "
                         "permuted across counties within state"}
print(f"  dose perm p={permutation['dose_t7']['perm_p_two_sided']:.3f}, "
      f"MDE80={permutation['dose_t7']['mde80']:.4f}; "
      f"gradient perm p={permutation['gradient_years_exposed']['perm_p_two_sided']:.3f}, "
      f"MDE80={permutation['gradient_years_exposed']['mde80']:.5f}")

# =============================================================================
# 5. Robustness grid (pooled TWFE coefficient)
# =============================================================================
print("\n[5] Robustness grid ...")
robust = []

def binary_post(gcol):
    g = reg["county_fips"].map(tdm[gcol]).to_numpy().astype(int)
    return (reg["year"].to_numpy() >= g).astype(float)

def add_spec(name, xraw, mask=None, w=None, note=""):
    mm = np.ones(len(reg), bool) if mask is None else mask
    ww = (w_main if w is None else w)[mm]
    gc = pd.factorize(reg.loc[mm, "county_fips"])[0]
    gs = make_gid(reg.loc[mm, "stateabb"].to_numpy(), reg.loc[mm, "year"].to_numpy(),
                  reg.loc[mm, "grade"].to_numpy(), reg.loc[mm, "subject"].to_numpy())
    cl = pd.factorize(reg.loc[mm, "stateabb"])[0]
    ydm = demean_two(y_raw[mm], ww, gc, gs)
    xdm = demean_two(np.asarray(xraw, float)[mm], ww, gc, gs)
    bb, ss, tt, pp, GG = cluster_ols(xdm, ydm, ww, cl)
    robust.append({"spec": name, "coef": float(bb[0]), "se": float(ss[0]),
                   "p": float(pp[0]), "n_obs": int(mm.sum()), "n_clusters": int(GG),
                   "note": note})
    print(f"  {name:42s} {bb[0]:+.4f} (se {ss[0]:.4f}, p {pp[0]:.3f})")

add_spec("dose_t7 (primary, continuous)", reg["dose_t7"].to_numpy(),
         note="primary spec repeated for reference")
add_spec("binary post: first_t7_50", binary_post("g_first_t7_50"))
add_spec("binary post: first_t6_50", binary_post("g_first_t6_50"))
add_spec("binary post: first_t7_25", binary_post("g_first_t7_25"))
add_spec("binary post: first_t7_75", binary_post("g_first_t7_75"))
add_spec("binary post: first_t6_50 Verizon-only", binary_post("g_first_t6_50_vzw"),
         note="crossing recomputed from share_mobile_t6_vzw >= 0.5")
mask_art = ~reg["stateabb"].isin(ARTIFACT_STATES).to_numpy()
add_spec("dose_t7, drop CO/MO/UT/NH/HI", reg["dose_t7"].to_numpy(), mask=mask_art,
         note="drops 2010-wave tier-coding artifact states")
add_spec("binary post t7_50, drop CO/MO/UT/NH/HI", binary_post("g_first_t7_50"), mask=mask_art)
add_spec("dose_t7, unweighted", reg["dose_t7"].to_numpy(), w=np.ones(len(reg)))
add_spec("binary post t7_50, unweighted", binary_post("g_first_t7_50"), w=np.ones(len(reg)))

# =============================================================================
# Figure
# =============================================================================
print("\nFigure ...")
make_figure(results_cs["pooled"])

# =============================================================================
# JSON
# =============================================================================
spec_notes = {
    "outcome_units": "SEDA 5.0 cs_mn_all, CS scale: SD units of the national reference-cohort "
                     "student-level distribution; county-level means.",
    "cohort_def": "g = wave_year + 1 for both June and December waves (first spring test "
                  "following coverage). Primary coding first_t7_50 (share_mobile_t7 >= 0.5). "
                  "g in {2011..2015} or never (135 matched never counties, 0.5% of pop).",
    "cs_att": "Manual Callaway-Sant'Anna: ATT(g,t) = wmean_treated[Y_t - Y_{g-1}] - "
              "wmean_control[Y_t - Y_{g-1}], county-level Y = tot_asmt-weighted mean of "
              "cs_mn_all pooled over grades 3-8 and subjects (also mth/rla separately). "
              "County weights within each comparison = base-period (g-1) county tot_asmt; "
              "counties must be observed in both t and g-1 (composition can shift across t). "
              "Controls = never-treated UNION cohorts > max(t,g). theta(e) aggregates ATT(g,g+e) "
              "with weights = contributing treated county population. 'restricted' version keeps "
              "only comparisons with max(t,g) <= 2014 so not-yet-treated units exist in the "
              "control pool; 'full' uses all t (for t >= 2015 the controls are ONLY the 135 "
              "never-treated, deep-rural counties). theta(-1) = 0 by construction. CIs: "
              "percentile, 200-draw county block bootstrap (resample counties w/ replacement).",
    "twfe_dose": "cs_mn_all on share_mobile_t7 from the latest SBDD wave on/before December of "
                 "the school year (test year t -> wave <= (t-1)-12); t=2009,2010 have no eligible "
                 "wave -> dose 0 (true t7 coverage ~0 then); t=2015 uses Jun-2014; t>=2016 "
                 "carries Jun-2014 forward (saturated ~0.98 -> these years contribute almost no "
                 "dose variation). FE: county + state x year x grade x subject, absorbed by "
                 "weighted alternating projections; weights tot_asmt_all; CR1 cluster-robust SEs "
                 "by state, t-dist with G-1 df.",
    "distributed_lag": "Dummies for years-since-t7-50-crossing 0/1/2/3+ (never & pre = omitted "
                       "category), same FE/weights/clustering.",
    "gradient": "years_exposed = #{school years s in [t-grade+3, t] : s >= g}, i.e. adolescent "
                "(grade-3-onward) years under t7-50 coverage; 0 for never. FE: county x year + "
                "grade x subject x year; identifies from cross-grade exposure differences within "
                "county-year. Weights tot_asmt_all, cluster by state.",
    "permutation": "500 draws; counties' ENTIRE treatment vector permuted across counties WITHIN "
                   "state (dose: the full share_mobile_t7 trajectory; gradient: the t7-50 "
                   "crossing year). p = share of |perm coef| >= |actual|; MDE80 = 2.8 x sd(perm).",
    "robustness_grid": "Same TWFE FE structure; alternative codings entered as binary "
                       "post-crossing indicators (the codings are dates, not doses); Verizon-only "
                       "crossing recomputed from share_mobile_t6_vzw >= 0.5 in the wave panel; "
                       "artifact-state drop = CO/MO/UT/NH/HI (Jun-2011 / Dec-2011 tier-coding "
                       "artifacts).",
    "known_caveats": "Tier-coding artifacts make t7-based 2010-11 treatment dates noisy for "
                     "CO/MO/UT/NH/HI (hence robustness codings + artifact-state drop). 2 SEDA "
                     "counties unmatched. Counties with <9 observed waves (n=10) keep their "
                     "possibly-censored crossing dates.",
    "software": "python3 + pandas/numpy/scipy/statsmodels-free manual implementation; "
                "FE absorption via weighted alternating projections (tol 1e-10).",
}

out = {
    "spec_notes": spec_notes,
    "merge_diagnostics": merge_diag,
    "cohort_sizes_first_t7_50": cohort_sizes,
    "cs_att": results_cs,
    "twfe_dose": twfe_dose,
    "gradient": gradient,
    "permutation": permutation,
    "robustness_grid": robust,
}

def to_py(o):
    if isinstance(o, dict):
        return {str(k): to_py(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_py(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return None if np.isnan(o) else float(o)
    if isinstance(o, float) and np.isnan(o):
        return None
    return o

with open(os.path.join(SEDA4G, "eventstudy_results.json"), "w") as f:
    json.dump(to_py(out), f, indent=1)
print("wrote seda4g/eventstudy_results.json")
print("DONE")
