"""v1.4 analyses.

1. TUDA district dose-response: 26 urban districts' NAEP changes vs CSDH virtual share
   (the within-NAEP version of the district closure literature).
2. Common Core tests: never-adopters (AK,NE,TX,VA) and 2014 repealers (IN,OK,SC) vs
   adopters, 2013->2019 changes in means and P10, math vs reading; Minnesota math-only
   subject contrast.
3. Opioid try-and-cut: state P10 change 2013-2019 vs change in overdose death rate.
"""
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import statsmodels.formula.api as smf

mpl.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.titlesize": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})
out = {}

# ============ 1. TUDA dose-response ============
tuda = pd.read_csv("data/naep_tuda.csv")
tuda = tuda[(tuda.displayable == 1) & (tuda.value < 900)]
match = pd.read_csv("data/tuda_csdh_match.csv").set_index("jur")
rsubj = [s for s in tuda.subject.unique() if s != "MAT"][0]
LBL = {("MAT", 4): "Math G4", ("MAT", 8): "Math G8",
       (rsubj, 4): "Reading G4", (rsubj, 8): "Reading G8"}

stack = []
print("## TUDA dose-response (26 districts, OLS HC1)")
rows = []
for key, label in LBL.items():
    pv = tuda[(tuda.subject == key[0]) & (tuda.grade == key[1])].pivot_table(
        index="jur", columns="year", values="value")
    m = pd.DataFrame({"d_1922": pv[2022] - pv[2019],
                      "d_2224": pv.get(2024) - pv.get(2022),
                      "d_1924": pv.get(2024) - pv.get(2019)}).join(match, how="inner").dropna(subset=["d_1922"])
    r1 = smf.ols("d_1922 ~ share_virtual", data=m).fit(cov_type="HC1")
    sp = m[["d_1922", "share_virtual"]].corr(method="spearman").iloc[0, 1]
    r3 = smf.ols("d_1924 ~ share_virtual", data=m.dropna(subset=["d_1924"])).fit(cov_type="HC1")
    rows.append({"series": label, "n": int(r1.nobs),
                 "drop b/10pp": round(r1.params["share_virtual"] / 10, 2),
                 "p": round(r1.pvalues["share_virtual"], 3),
                 "spearman": round(sp, 2),
                 "net1924 b/10pp": round(r3.params["share_virtual"] / 10, 2),
                 "p_net": round(r3.pvalues["share_virtual"], 3)})
    mm = m.reset_index(); mm["series"] = label
    stack.append(mm)
print(pd.DataFrame(rows).to_markdown(index=False))
out["tuda"] = rows

pool = pd.concat(stack)
mp = smf.ols("d_1922 ~ share_virtual + C(series)", data=pool).fit(
    cov_type="cluster", cov_kwds={"groups": pool["jur"]})
print(f"Pooled TUDA drop ~ virtual: {mp.params['share_virtual']/10:+.2f} pts/10pp "
      f"(p={mp.pvalues['share_virtual']:.4f}, n={int(mp.nobs)})")
mp2 = smf.ols("d_1924 ~ share_virtual + C(series)", data=pool.dropna(subset=["d_1924"])).fit(
    cov_type="cluster", cov_kwds={"groups": pool["jur"]})
print(f"Pooled TUDA net 2019-24 ~ virtual: {mp2.params['share_virtual']/10:+.2f} pts/10pp "
      f"(p={mp2.pvalues['share_virtual']:.4f})")
out["tuda_pooled"] = {"drop_b10": round(mp.params["share_virtual"] / 10, 2),
                      "p": round(mp.pvalues["share_virtual"], 4),
                      "net_b10": round(mp2.params["share_virtual"] / 10, 2),
                      "p_net": round(mp2.pvalues["share_virtual"], 4)}

# figure: TUDA scatter, math G4 & G8
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.3))
for ax, key in zip(axes, [("MAT", 4), ("MAT", 8)]):
    pv = tuda[(tuda.subject == key[0]) & (tuda.grade == key[1])].pivot_table(
        index="jur", columns="year", values="value")
    m = pd.DataFrame({"d": pv[2022] - pv[2019]}).join(match, how="inner").dropna(subset=["d"])
    x = m.share_virtual * 100
    ax.scatter(x, m.d, s=14, color="#1f5fa8", alpha=0.8)
    for j in m.index:
        ax.annotate(m.loc[j, "label"].split(" (")[0], (x[j], m.loc[j, "d"]),
                    fontsize=4.5, alpha=0.7, textcoords="offset points", xytext=(2, 2))
    b, a = np.polyfit(x, m.d, 1)
    xs = np.linspace(0, 100, 10)
    ax.plot(xs, a + b * xs, color="#b03a2e", lw=1)
    ax.set_xlabel("Percent of 2020--21 fully virtual")
    ax.set_title(f"{LBL[key]}: slope {10*b:.2f} pts/10pp")
axes[0].set_ylabel("Change in NAEP mean, 2019--2022")
fig.tight_layout()
fig.savefig("figures/fig_tuda.pdf"); plt.close(fig)

# ============ 2. Common Core ============
cc = pd.read_csv("data/commoncore.csv")
main = pd.read_csv("data/naep_main.csv")
st = main[(main.dataset == "state") & (main.displayable == 1)]
v11 = pd.read_csv("data/naep_v11.csv")
stp = v11[(v11.dataset == "statepct") & (v11.displayable == 1) & (v11.stat == "PC:P1")]

print("\n## Common Core: 2013->2019 changes by adoption status")
ccrows = []
for key, label in LBL.items():
    pv = st[(st.subject == key[0]) & (st.grade == key[1])].pivot_table(
        index="jurisdiction", columns="year", values="value")
    d = (pv[2019] - pv[2013]).rename("d_mean")
    pvp = stp[(stp.subject == key[0]) & (stp.grade == key[1])].pivot_table(
        index="jurisdiction", columns="year", values="value")
    dp = (pvp[2019] - pvp[2013]).rename("d_p10")
    m = pd.concat([d, dp], axis=1).join(cc.set_index("state"), how="left")
    grp = {"adopters": m[m.cc_status == "adopted"],
           "never (AK,NE,TX,VA)": m[m.cc_status == "never"],
           "repealed 2014 (IN,OK,SC)": m[m.repeal_year == 2014]}
    for g, sub in grp.items():
        ccrows.append({"series": label, "group": g, "n": len(sub),
                       "mean chg": round(sub.d_mean.mean(), 1),
                       "P10 chg": round(sub.d_p10.mean(), 1)})
ccdf = pd.DataFrame(ccrows)
print(ccdf.to_markdown(index=False))
out["commoncore_groups"] = ccrows

# t-test style: never vs adopters, pooled z over series, cluster state
zstack = []
for key, label in LBL.items():
    pvp = stp[(stp.subject == key[0]) & (stp.grade == key[1])].pivot_table(
        index="jurisdiction", columns="year", values="value")
    d = (pvp[2019] - pvp[2013]).rename("d").to_frame().join(cc.set_index("state"), how="left").reset_index()
    d["series"] = label
    zstack.append(d)
zz = pd.concat(zstack).dropna(subset=["d"])
zz = zz[zz.cc_status.isin(["adopted", "never"])]
zz["never"] = (zz.cc_status == "never").astype(int)
mcc = smf.ols("d ~ never + C(series)", data=zz).fit(
    cov_type="cluster", cov_kwds={"groups": zz["jurisdiction"]})
print(f"\nNever-adopter difference in P10 change 2013-19 (pooled): "
      f"{mcc.params['never']:+.2f} pts (p={mcc.pvalues['never']:.3f})")
out["cc_never_diff"] = {"b": round(mcc.params["never"], 2), "p": round(mcc.pvalues["never"], 3)}

# Minnesota subject contrast (math never adopted; ELA adopted)
print("\n## Minnesota subject contrast (math non-CC, reading CC)")
mnrows = []
for grade in (4, 8):
    pm = st[(st.subject == "MAT") & (st.grade == grade)].pivot_table(
        index="jurisdiction", columns="year", values="value")
    pr = st[(st.subject == rsubj) & (st.grade == grade)].pivot_table(
        index="jurisdiction", columns="year", values="value")
    dm, dr = pm[2019] - pm[2013], pr[2019] - pr[2013]
    mn_rel_math = dm["MN"] - dm.drop("MN").mean()
    mn_rel_read = dr["MN"] - dr.drop("MN").mean()
    mnrows.append({"grade": grade,
                   "MN math chg vs other states": round(mn_rel_math, 1),
                   "MN reading chg vs other states": round(mn_rel_read, 1),
                   "triple-diff (math - reading)": round(mn_rel_math - mn_rel_read, 1)})
print(pd.DataFrame(mnrows).to_markdown(index=False))
out["minnesota"] = mnrows

# ============ 3. Opioid try-and-cut ============
od = pd.read_csv("data/overdose.csv").set_index("state")
od["d_od"] = od.od_2019 - od.od_2013
print("\n## Opioid: state P10 change 2013-19 vs overdose-rate change")
oprows = []
for key, label in LBL.items():
    pvp = stp[(stp.subject == key[0]) & (stp.grade == key[1])].pivot_table(
        index="jurisdiction", columns="year", values="value")
    d = (pvp[2019] - pvp[2013]).rename("d").to_frame().join(od, how="inner").dropna()
    r = smf.ols("d ~ d_od", data=d).fit(cov_type="HC1")
    oprows.append({"series": label, "b per +10/100k": round(r.params["d_od"] * 10, 2),
                   "p": round(r.pvalues["d_od"], 3),
                   "r": round(np.sqrt(r.rsquared) * np.sign(r.params["d_od"]), 2)})
print(pd.DataFrame(oprows).to_markdown(index=False))
out["opioid"] = oprows

# figure: Common Core groups, P10 change 2013-19 by series
fig, ax = plt.subplots(figsize=(6.2, 3.0))
groups = ["adopters", "never (AK,NE,TX,VA)", "repealed 2014 (IN,OK,SC)"]
colors = {"adopters": "#1f5fa8", "never (AK,NE,TX,VA)": "#b03a2e",
          "repealed 2014 (IN,OK,SC)": "#e09b94"}
series_order = list(LBL.values())
xbase = np.arange(len(series_order))
for k, g in enumerate(groups):
    vals = [next(r["P10 chg"] for r in ccrows if r["series"] == s and r["group"] == g)
            for s in series_order]
    ax.bar(xbase + (k - 1) * 0.26, vals, width=0.24, color=colors[g],
           label=g.replace(" (", "\n("))
ax.axhline(0, color="k", lw=0.6)
ax.set_xticks(xbase); ax.set_xticklabels(series_order)
ax.set_ylabel("10th-percentile change, 2013--2019")
ax.legend(frameon=False, fontsize=7.5, ncol=3, loc="lower center",
          bbox_to_anchor=(0.5, 1.0))
fig.tight_layout()
fig.savefig("figures/fig_commoncore.pdf"); plt.close(fig)

with open("data/v14_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nv1.4 analyses done")
