#!/usr/bin/env python3
"""Clean-room DiD of ESEA/NCLB waiver receipt on NAEP P10 scores.

Spec decisions (recorded in results.json):
- Outcome: grade 8 math 10th percentile (PC:P1), public-school state NAEP.
- Treatment timing: first NAEP wave testing a school year >= the state's first
  waiver school year (waivers.csv `first_sy_end`). NAEP wave y tests SY (y-1,y),
  so first treated wave = first_sy_end if odd, else first_sy_end + 1.
  -> early approvals (SY 2012-13): treated from 2013 wave.
  -> late approvals (SY 2013-14) and IL (SY 2014-15): treated from 2015 wave.
- WA (waiver revoked Apr 2014): kept as treated from 2013 (intent-to-treat,
  absorbing treatment). Sensitivity not run; noted as judgment call.
- Never-waiver controls: CA, IA, MT, NE, ND, VT, WY (7 states).
- TWFE OLS, state + year FE, unweighted. Cluster-robust (state) SEs.
- SD units: coefficient / cross-state SD of P10 in 2011.
- Randomization inference: 2000 draws permuting the first-treated-wave vector
  (incl. never = inf) across the 51 jurisdictions, re-estimating the pooled
  TWFE coefficient. p = share of |perm coef| >= |actual|. MDE80 = 2.8 * sd(perm).
- Event study: indicators for event time (NAEP waves relative to first treated
  wave, in wave steps: ..., -2, -1, 0, +1, ...), omitted category = -1 (last
  pre-wave); never-treated states contribute as pure controls (all indicators 0).
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
PROJ = HERE.parent.parent.parent
RNG = np.random.default_rng(20260610)
N_PERM = 2000

NAEP_YEARS = [2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019]


def load_outcome(tag):
    rows = json.loads((HERE / f"raw_{tag}_p10.json").read_text())
    df = pd.DataFrame(
        [
            {"state": r["jurisdiction"], "year": int(r["year"]), "p10": r["value"]}
            for r in rows
            if r.get("isStatDisplayable", 1)
        ]
    )
    assert df.duplicated(["state", "year"]).sum() == 0
    return df


def load_treatment():
    w = pd.read_csv(PROJ / "data" / "waivers.csv")
    def first_wave(row):
        if row["approval"] == "never" or pd.isna(row["first_sy_end"]):
            return np.inf
        sy = int(row["first_sy_end"])
        return sy if sy % 2 == 1 else sy + 1
    w["first_treat_wave"] = w.apply(first_wave, axis=1)
    return w[["state", "first_treat_wave", "group"]]


def twfe_coef(y, post, state_codes, year_codes, return_se=False):
    """Pooled TWFE coefficient via two-way demeaning (balanced-ish panel OK
    via iterated demeaning), with optional cluster-robust (state) SE."""
    df = pd.DataFrame({"y": y, "d": post, "s": state_codes, "t": year_codes})
    # iterate demeaning to converge for unbalanced panels
    yd, dd = df["y"].astype(float).copy(), df["d"].astype(float).copy()
    for _ in range(50):
        y0, d0 = yd.copy(), dd.copy()
        for g in ("s", "t"):
            grp = df[g]
            yd = yd - yd.groupby(grp).transform("mean")
            dd = dd - dd.groupby(grp).transform("mean")
        if max((yd - y0).abs().max(), (dd - d0).abs().max()) < 1e-12:
            break
    denom = (dd**2).sum()
    if denom < 1e-10:
        return (np.nan, np.nan) if return_se else np.nan
    beta = (dd * yd).sum() / denom
    if not return_se:
        return beta
    resid = yd - beta * dd
    # cluster-robust by state, 1 regressor after FE projection
    meat = sum(
        (dd[df["s"] == s] * resid[df["s"] == s]).sum() ** 2
        for s in df["s"].unique()
    )
    G = df["s"].nunique()
    n = len(df)
    k = 1 + df["s"].nunique() + df["t"].nunique() - 1  # approx dof
    adj = (G / (G - 1)) * ((n - 1) / max(n - k, 1))
    se = np.sqrt(adj * meat) / denom
    return beta, se


def event_study(df, omit=-1):
    """TWFE with event-time dummies (in wave steps), omit `omit`."""
    d = df.copy()
    d["etime"] = np.where(
        np.isinf(d["first_treat_wave"]),
        np.nan,
        (d["year"] - d["first_treat_wave"]) / 2,
    )
    ets = sorted(e for e in d["etime"].dropna().unique() if e != omit)
    X = pd.DataFrame(index=d.index)
    for e in ets:
        X[f"e{e:+.0f}"] = (d["etime"] == e).astype(float)
    # add FE dummies
    S = pd.get_dummies(d["state"], drop_first=True, dtype=float)
    T = pd.get_dummies(d["year"], drop_first=True, dtype=float, prefix="y")
    Xf = pd.concat([X, S, T], axis=1)
    Xf.insert(0, "const", 1.0)
    yv = d["p10"].to_numpy(float)
    Xm = Xf.to_numpy(float)
    beta, *_ = np.linalg.lstsq(Xm, yv, rcond=None)
    return {f"e{e:+.0f}": round(float(b), 3) for e, b in zip(ets, beta[1 : 1 + len(ets)])}


def run_window(df, lo, hi, label, do_ri=True):
    d = df[(df["year"] >= lo) & (df["year"] <= hi)].copy()
    d["post"] = (d["year"] >= d["first_treat_wave"]).astype(float)
    beta, se = twfe_coef(d["p10"], d["post"], d["state"], d["year"], return_se=True)
    # cluster t-test p (normal approx with G-1 dof t)
    from scipy import stats
    G = d["state"].nunique()
    p_cluster = 2 * (1 - stats.t.cdf(abs(beta / se), df=G - 1))
    out = {
        "window": f"{lo}-{hi}",
        "coef_points": round(float(beta), 4),
        "cluster_se": round(float(se), 4),
        "cluster_p": round(float(p_cluster), 4),
    }
    if do_ri:
        treat_vec = (
            d[["state", "first_treat_wave"]].drop_duplicates().set_index("state")[
                "first_treat_wave"
            ]
        )
        states = treat_vec.index.to_numpy()
        vals = treat_vec.to_numpy()
        perm = np.empty(N_PERM)
        for i in range(N_PERM):
            shuf = RNG.permutation(vals)
            fmap = dict(zip(states, shuf))
            dpost = (d["year"] >= d["state"].map(fmap)).astype(float)
            perm[i] = twfe_coef(d["p10"], dpost, d["state"], d["year"])
        perm = perm[~np.isnan(perm)]
        out["ri_p"] = round(float(np.mean(np.abs(perm) >= abs(beta))), 4)
        out["ri_sd"] = round(float(perm.std(ddof=1)), 4)
        out["mde80_points"] = round(float(2.8 * perm.std(ddof=1)), 4)
        out["ri_n_perms"] = int(len(perm))
    return out, d


def main():
    treat = load_treatment()
    results = {"spec_decisions": __doc__.strip(), "outcomes": {}}

    for tag, prio in [("math_g8", True), ("read_g8", False),
                      ("math_g4", False), ("read_g4", False)]:
        f = HERE / f"raw_{tag}_p10.json"
        if not f.exists():
            continue
        df = load_outcome(tag).merge(treat, on="state", how="inner")
        sd2011 = float(df.loc[df["year"] == 2011, "p10"].std(ddof=1))
        n_treated = int((~np.isinf(treat["first_treat_wave"])).sum())
        n_never = int(np.isinf(treat["first_treat_wave"]).sum())

        main_res, dmain = run_window(df, 2009, 2019, "main", do_ri=prio)
        full_res, _ = run_window(df, 2003, 2019, "full", do_ri=False)
        main_res["coef_sd_units"] = round(main_res["coef_points"] / sd2011, 4)
        full_res["coef_sd_units"] = round(full_res["coef_points"] / sd2011, 4)

        res = {
            "n_states_treated": n_treated,
            "n_states_never": n_never,
            "sd_p10_2011_cross_state": round(sd2011, 4),
            "twfe_2009_2019": main_res,
            "twfe_2003_2019": full_res,
        }
        if prio:
            res["event_study_2003_2019"] = event_study(
                df[(df["year"] >= 2003) & (df["year"] <= 2019)]
            )
            res["event_study_2009_2019"] = event_study(
                df[(df["year"] >= 2009) & (df["year"] <= 2019)]
            )
        results["outcomes"][tag] = res
        print(tag, json.dumps(res, indent=1)[:600])

    (HERE / "results.json").write_text(json.dumps(results, indent=1))
    print("wrote results.json")


if __name__ == "__main__":
    main()
