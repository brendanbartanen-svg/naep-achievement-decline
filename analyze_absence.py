"""#5: Within-NAEP absence crosswalk (B018101: days absent last month).

(a) How much did self-reported absence rise?
(b) Kitagawa/Oaxaca decomposition: how much of the score decline is a shift of
    students into high-absence categories vs. declines within absence categories?
"""
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.titlesize": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})

d = pd.read_csv("data/naep_absence.csv", keep_default_na=False, na_values=[""])
d["value"] = pd.to_numeric(d["value"], errors="coerce")
d = d[pd.to_numeric(d.displayable, errors="coerce") == 1]
rsubj = [s for s in d.subject.unique() if s != "MAT"][0]
LBL = {("MAT", 4): "Math, Grade 4", ("MAT", 8): "Math, Grade 8",
       (rsubj, 4): "Reading, Grade 4", (rsubj, 8): "Reading, Grade 8"}
CATS = ["None", "1-2 days", "3-4 days", "5-10 days", "More than 10 days"]
out = {}

def cell(key, stat):
    sub = d[(d.subject == key[0]) & (d.grade == key[1]) & (d.stat == stat)]
    return sub.pivot_table(index="year", columns="group", values="value")[CATS]

# (a) share missing 3+ days, and gradient
print("## Share absent 3+ days in past month (%)")
share3 = {}
for key, label in LBL.items():
    rp = cell(key, "RP:RP")
    share3[label] = rp[["3-4 days", "5-10 days", "More than 10 days"]].sum(axis=1)
    print(f"  {label}: 2013 {share3[label].get(2013):.1f} | 2019 {share3[label].get(2019):.1f} | "
          f"2022 {share3[label].get(2022):.1f} | 2024 {share3[label].get(2024):.1f}")
out["share_3plus"] = {k: {int(y): round(v, 1) for y, v in s.items()} for k, s in share3.items()}

print("\n## Score gap: 'None' minus 'More than 10 days'")
gap = {}
for key, label in LBL.items():
    mn = cell(key, "MN:MN")
    gap[label] = mn["None"] - mn["More than 10 days"]
    print(f"  {label}: 2013 {gap[label].get(2013):.1f} | 2019 {gap[label].get(2019):.1f} | "
          f"2024 {gap[label].get(2024):.1f}")
out["gap_none_vs_10plus"] = {k: {int(y): round(v, 1) for y, v in s.items()} for k, s in gap.items()}

# (b) decomposition of mean change between year pairs
def decompose(key, y0, y1):
    mn, rp = cell(key, "MN:MN"), cell(key, "RP:RP") / 100.0
    m0, m1 = mn.loc[y0], mn.loc[y1]
    p0, p1 = rp.loc[y0], rp.loc[y1]
    total = (p1 * m1).sum() - (p0 * m0).sum()
    comp = ((p1 - p0) * (m0 + m1) / 2).sum()      # composition (absence shift)
    within = (((m1 - m0) * (p0 + p1) / 2)).sum()  # within-category score change
    return total, comp, within

print("\n## Decomposition of mean change: composition (absence shift) vs within-category")
rows = []
for key, label in LBL.items():
    for (y0, y1) in [(2013, 2019), (2019, 2024)]:
        t, c, wv = decompose(key, y0, y1)
        rows.append({"series": label, "period": f"{y0}-{y1}",
                     "total": round(t, 1), "absence_shift": round(c, 1),
                     "within_category": round(wv, 1),
                     "pct_from_absence": round(100 * c / t, 0) if abs(t) > .3 else np.nan})
t5 = pd.DataFrame(rows)
print(t5.to_markdown(index=False))
out["decomposition"] = rows

with open("data/absence_results.json", "w") as f:
    json.dump(out, f, indent=1)

# figure
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.1))
ax = axes[0]
colors = ["#1f5fa8", "#7fb0d8", "#b03a2e", "#e09b94"]
for (label, s), c in zip(share3.items(), colors):
    ax.plot(s.index, s.values, "-o", ms=3, color=c, label=label)
ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
ax.set_ylabel("Percent absent 3+ days in past month")
ax.legend(frameon=False, fontsize=7.5)

ax = axes[1]
key = ("MAT", 8)
mn = cell(key, "MN:MN")
for cat, c in zip(CATS, plt.cm.coolwarm(np.linspace(0, 1, 5))):
    s = (mn[cat] - mn[cat].loc[2013]).dropna()
    ax.plot(s.index, s.values, "-o", ms=2.5, color=c, label=cat)
ax.axhline(0, color="k", lw=0.6)
ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
ax.set_title("Math G8: score change since 2013,\nby days absent last month")
ax.set_ylabel("Score change since 2013")
ax.legend(frameon=False, fontsize=7, title="Days absent", title_fontsize=7)
fig.tight_layout()
fig.savefig("figures/fig_absence.pdf"); plt.close(fig)
print("\nabsence figure done")
