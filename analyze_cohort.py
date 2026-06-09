"""Cohort vs. period decomposition.

Test: is the decline a cohort effect (successive birth cohorts arrive weaker,
visible already at grade 4 / age 9) or a period effect (losses accrue during a
specific calendar window, hitting whatever cohort is in adolescence)?

Tool: cohort-matched pseudo-growth = G8 mean(t) - G4 mean(t-4) for the same
birth cohort; plus scores plotted against birth year by age group.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import json

mpl.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.titlesize": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})

df = pd.read_csv("data/naep_main.csv")
nat = df[(df.dataset == "national") & (df.stat == "MN:MN") & (df.displayable == 1)]
rsubj = [s for s in nat.subject.unique() if s != "MAT"][0]

series = {}
for subj, grade in [("MAT", 4), ("MAT", 8), (rsubj, 4), (rsubj, 8)]:
    s = nat[(nat.subject == subj) & (nat.grade == grade)].set_index("year")["value"].sort_index()
    series[(subj, grade)] = s

# ---- pseudo-growth: cohort-matched G4 -> G8 (4-year-apart assessment pairs) ----
pairs = [(2003, 2007), (2005, 2009), (2007, 2011), (2009, 2013),
         (2011, 2015), (2013, 2017), (2015, 2019)]
pg = {}
for subj, lbl in [("MAT", "Math"), (rsubj, "Reading")]:
    rowsx = []
    for g4y, g8y in pairs:
        s4, s8 = series[(subj, 4)], series[(subj, 8)]
        if g4y in s4.index and g8y in s8.index:
            rowsx.append({"g8year": g8y, "cohort_g4year": g4y,
                          "growth": s8[g8y] - s4[g4y]})
    pg[lbl] = pd.DataFrame(rowsx)
    print(f"\nPseudo-growth G4->G8, {lbl}:")
    print(pg[lbl].to_markdown(index=False))

# ---- decomposition of G8 change 2013->2019: entry vs during-middle-school ----
print("\nDecomposition of G8 change (2013->2019):")
out = {}
for subj, lbl in [("MAT", "Math"), (rsubj, "Reading")]:
    s4, s8 = series[(subj, 4)], series[(subj, 8)]
    d_g8 = s8[2019] - s8[2013]                     # total G8 change
    d_entry = s4[2015] - s4[2009]                  # change in same cohorts' G4 scores
    d_growth = (s8[2019] - s4[2015]) - (s8[2013] - s4[2009])  # change in pseudo-growth
    print(f"  {lbl}: G8 change {d_g8:+.1f} = entry {d_entry:+.1f} + growth {d_growth:+.1f}")
    out[lbl] = {"d_g8": round(d_g8, 1), "d_entry": round(d_entry, 1),
                "d_growth": round(d_growth, 1)}

with open("data/cohort_decomp.json", "w") as f:
    json.dump({"pseudo_growth": {k: v.to_dict("records") for k, v in pg.items()},
               "decomp_2013_2019": out}, f, indent=1)

# ---- figure ----
ltt = pd.read_csv("data/ltt.csv")
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2))

ax = axes[0]
for lbl, c in [("Math", "#1f5fa8"), ("Reading", "#b03a2e")]:
    d = pg[lbl]
    ax.plot(d.g8year, d.growth - d.growth.iloc[0], "-o", ms=4, color=c, label=lbl)
ax.axvline(2013, color="gray", lw=0.7, ls=":")
ax.axhline(0, color="k", lw=0.6)
ax.set_title("Cohort-matched growth, grade 4 $\\rightarrow$ grade 8")
ax.set_xlabel("Year cohort reached grade 8")
ax.set_ylabel("Pseudo-growth, change from\n2007 cohort (scale points)")
ax.legend(frameon=False, fontsize=8)

# scores by birth cohort, math (main NAEP G4/G8 + LTT age9/13), normalized at peak
ax = axes[1]
defs = [
    ("G4 (age $\\approx$ 9)", series[("MAT", 4)], 9, "#1f5fa8", "-o"),
    ("G8 (age $\\approx$ 13)", series[("MAT", 8)], 13, "#b03a2e", "-o"),
    ("LTT age 9", ltt[ltt.series == "age9_math"].set_index("year")["value"], 9, "#7fb0d8", "--s"),
    ("LTT age 13", ltt[ltt.series == "age13_math"].set_index("year")["value"], 13, "#e09b94", "--s"),
]
for lbl, s, age, c, style in defs:
    s = s[s.index >= 2003]
    cohort = s.index - age
    ax.plot(cohort, s.values - s.max(), style, ms=3, color=c, label=lbl)
ax.axhline(0, color="k", lw=0.6)
ax.set_title("Mathematics by birth cohort")
ax.set_xlabel("Approximate birth year")
ax.set_ylabel("Score relative to series peak")
ax.legend(frameon=False, fontsize=7.5)
fig.tight_layout()
fig.savefig("figures/fig_cohort.pdf"); plt.close(fig)
print("\ncohort figure done")
