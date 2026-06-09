"""v1.1 analyses #1 and #2.

1. Public vs Catholic school trends (accountability never applied to privates).
2. NCLB-waiver event study / DiD on state 10th-percentile scores.
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

v11 = pd.read_csv("data/naep_v11.csv")
spct = pd.read_csv("data/naep_schtype_pct.csv")
rsubj = [s for s in v11.subject.unique() if s != "MAT"][0]
LBL = {("MAT", 4): "Math, Grade 4", ("MAT", 8): "Math, Grade 8",
       (rsubj, 4): "Reading, Grade 4", (rsubj, 8): "Reading, Grade 8"}
out = {}

# ============ 1. Public vs Catholic ============
st = v11[(v11.dataset == "schtype") & (v11.displayable == 1) & (v11.stat == "MN:MN") &
         (v11.variable == "SCHTYPE")]
print("## Public vs Catholic means (changes)")
rows = []
for key, label in LBL.items():
    sub = st[(st.subject == key[0]) & (st.grade == key[1])]
    for grp in ["Public", "Catholic"]:
        s = sub[sub.group == grp].set_index("year")["value"].sort_index()
        if 2013 not in s.index:
            continue
        rows.append({"series": label, "group": grp,
                     "2013": round(s[2013], 1),
                     "chg_2013_2019": round(s.get(2019, np.nan) - s[2013], 1),
                     "chg_2019_2024": round(s.get(2024, np.nan) - s.get(2019, np.nan), 1),
                     "chg_2013_2024": round(s.get(2024, np.nan) - s[2013], 1)})
t = pd.DataFrame(rows)
print(t.to_markdown(index=False))
out["public_catholic_means"] = rows

# percentile changes for Catholic vs public(SCHTYP2)
print("\n## P10/P90 changes by school type")
pub_pct = spct[(spct.group == "Public") & (spct.displayable == 1)]
cath_pct = spct[(spct.group == "Catholic") & (spct.displayable == 1)]
prow = []
for key, label in LBL.items():
    for grp, src in [("Public", pub_pct), ("Catholic", cath_pct)]:
        sub = src[(src.subject == key[0]) & (src.grade == key[1])]
        for stat, pct in [("PC:P1", 10), ("PC:P9", 90)]:
            s = sub[sub.stat == stat].set_index("year")["value"].sort_index()
            if 2013 not in s.index:
                continue
            prow.append({"series": label, "group": grp, "pctile": pct,
                         "chg_2013_2019": round(s.get(2019, np.nan) - s[2013], 1),
                         "chg_2019_2024": round(s.get(2024, np.nan) - s.get(2019, np.nan), 1)})
tp = pd.DataFrame(prow)
print(tp.to_markdown(index=False))
out["public_catholic_pctiles"] = prow

# figure: G8 math + G8 reading, public vs Catholic, indexed to 2013
fig, axes = plt.subplots(1, 2, figsize=(7, 3.1), sharey=True)
for ax, key in zip(axes, [("MAT", 8), (rsubj, 8)]):
    sub = st[(st.subject == key[0]) & (st.grade == key[1])]
    for grp, c in [("Public", "#1f5fa8"), ("Catholic", "#b03a2e")]:
        s = sub[sub.group == grp].set_index("year")["value"].sort_index()
        ax.plot(s.index, s - s[2013], "-o", ms=3.5, color=c, label=grp)
    ax.axhline(0, color="k", lw=0.6)
    ax.axvline(2013, color="gray", lw=0.7, ls=":")
    ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
    ax.set_title(LBL[key])
axes[0].set_ylabel("Score change since 2013")
axes[0].legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("figures/fig_pubcath.pdf"); plt.close(fig)

# ============ 2. Waiver event study ============
w = pd.read_csv("data/waivers.csv")
stp = v11[(v11.dataset == "statepct") & (v11.displayable == 1)].copy()
stp = stp.merge(w[["state", "first_sy_end", "group"]],
                left_on="jurisdiction", right_on="state", how="left")
stp["wgroup"] = stp["group_y"]

# pre-COVID panel
panel = stp[stp.year <= 2019].copy()

print("\n## Group-mean P10 trends relative to 2011 (pre-COVID)")
trend_fig_data = {}
grows = []
for key, label in LBL.items():
    sub = panel[(panel.subject == key[0]) & (panel.grade == key[1]) & (panel.stat == "PC:P1")]
    gm = sub.groupby(["wgroup", "year"])["value"].mean().unstack(0)
    rel = gm - gm.loc[2011]
    trend_fig_data[label] = rel
    grows.append({"series": label,
                  "early_2011_2019": round(rel.loc[2019, "early"], 1),
                  "late_2011_2019": round(rel.loc[2019, "late"], 1) if "late" in rel else np.nan,
                  "never_2011_2019": round(rel.loc[2019, "never"], 1)})
tg = pd.DataFrame(grows)
print(tg.to_markdown(index=False))
out["waiver_group_trends_p10"] = grows

# TWFE DiD: post = year >= first_sy_end (never states post=0); cluster by state
print("\n## TWFE DiD estimates, P10 and P90 (2003-2019 panel, cluster-robust by state)")
did_rows = []
for stat, pct in [("PC:P1", "P10"), ("PC:P2", "P25"), ("PC:P9", "P90")]:
    for key, label in LBL.items():
        sub = panel[(panel.subject == key[0]) & (panel.grade == key[1]) &
                    (panel.stat == stat)].copy()
        sub["post"] = ((sub.first_sy_end.notna()) & (sub.year >= sub.first_sy_end)).astype(int)
        # drop WA after revocation (treated 2013, untreated 2015+)
        sub = sub[~((sub.jurisdiction == "WA") & (sub.year >= 2015))]
        m = smf.ols("value ~ post + C(jurisdiction) + C(year)", data=sub).fit(
            cov_type="cluster", cov_kwds={"groups": sub["jurisdiction"]})
        did_rows.append({"stat": pct, "series": label,
                         "beta_post": round(m.params["post"], 2),
                         "se": round(m.bse["post"], 2),
                         "p": round(m.pvalues["post"], 3)})
td = pd.DataFrame(did_rows)
print(td.to_markdown(index=False))
out["waiver_did"] = did_rows

# pooled across series in z-units
zsub = panel[panel.stat.isin(["PC:P1"])].copy()
zsub["cell"] = zsub.subject + "_" + zsub.grade.astype(str)
zsub["z"] = zsub.groupby("cell")["value"].transform(lambda x: (x - x.mean()) / x.std())
zsub["post"] = ((zsub.first_sy_end.notna()) & (zsub.year >= zsub.first_sy_end)).astype(int)
zsub = zsub[~((zsub.jurisdiction == "WA") & (zsub.year >= 2015))]
m = smf.ols("z ~ post + C(jurisdiction) + C(year) + C(cell)", data=zsub).fit(
    cov_type="cluster", cov_kwds={"groups": zsub["jurisdiction"]})
print(f"\nPooled P10 (z-units): beta_post = {m.params['post']:.3f} (se {m.bse['post']:.3f}, p {m.pvalues['post']:.3f})")
out["waiver_did_pooled_p10_z"] = {"beta": round(m.params["post"], 3),
                                  "se": round(m.bse["post"], 3),
                                  "p": round(m.pvalues["post"], 3)}

# event-study figure: group means + DiD coefficients by year (interaction model)
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2))
ax = axes[0]
colors = {"early": "#1f5fa8", "late": "#b03a2e", "never": "#2e7d32", "revoked": "#999999"}
rel = trend_fig_data["Math, Grade 8"]
for g in ["early", "late", "never"]:
    if g in rel:
        ax.plot(rel.index, rel[g], "-o", ms=3.5, color=colors[g],
                label=f"{g} waiver" if g != "never" else "no waiver")
ax.axvline(2012.5, color="gray", lw=0.7, ls=":")
ax.axhline(0, color="k", lw=0.6)
ax.set_title("Math G8, 10th percentile by waiver group")
ax.set_ylabel("Change since 2011 (scale points)")
ax.legend(frameon=False, fontsize=8)

# yearly DiD coefficients (ever-early-treated vs never), pooled z, P10
ax = axes[1]
ev = panel[panel.stat == "PC:P1"].copy()
ev = ev[ev.wgroup.isin(["early", "never"])]
ev["cell"] = ev.subject + "_" + ev.grade.astype(str)
ev["z"] = ev.groupby("cell")["value"].transform(lambda x: (x - x.mean()) / x.std())
ev["treat"] = (ev.wgroup == "early").astype(int)
yrs = sorted(ev.year.unique())
terms = []
for y in yrs:
    if y == 2011:
        continue  # base year: interaction omitted to break collinearity with state FE
    ev[f"tX{y}"] = ev.treat * (ev.year == y).astype(int)
    terms.append(f"tX{y}")
m2 = smf.ols("z ~ " + " + ".join(terms) + " + C(jurisdiction) + C(year) + C(cell)",
             data=ev).fit(cov_type="cluster", cov_kwds={"groups": ev["jurisdiction"]})
coefs = np.array([m2.params.get(f"tX{y}", 0.0) for y in yrs])
ses = np.array([m2.bse.get(f"tX{y}", 0.0) for y in yrs])
ax.errorbar(yrs, coefs, yerr=1.96 * ses, fmt="o", ms=4, color="#1f5fa8", capsize=2)
ax.axvline(2012.5, color="gray", lw=0.7, ls=":")
ax.axhline(0, color="k", lw=0.6)
ax.set_title("Event study: early-waiver vs no-waiver, P10 (pooled, $z$)")
ax.set_ylabel("Coefficient (SD units), rel. 2011")
fig.tight_layout()
fig.savefig("figures/fig_waiver.pdf"); plt.close(fig)

with open("data/v11_results.json", "w") as f:
    json.dump(out, f, indent=1)
print("\nv1.1 figures + results written")
