"""LTT figures: long-run trends, percentile changes pre/post pandemic, reading for fun."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "serif", "font.size": 9, "axes.titlesize": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.dpi": 150, "savefig.bbox": "tight",
})

ltt = pd.read_csv("data/ltt.csv")

# Fig: LTT long-run, 2 panels (math, reading), age 9 & 13
fig, axes = plt.subplots(1, 2, figsize=(7, 3.2))
panels = [("math", ["age9_math", "age13_math"]), ("reading", ["age9_reading", "age13_reading"])]
cols = {"age9": "#b03a2e", "age13": "#1f5fa8"}
for ax, (subj, series) in zip(axes, panels):
    for s in series:
        d = ltt[ltt.series == s]
        age = s.split("_")[0]
        ax.plot(d.year, d.value, "-o", ms=2.5, color=cols[age], label=f"Age {age[3:]}")
        pk = d.loc[d.value.idxmax()]
    ax.axvline(2012, color="gray", lw=0.7, ls=":")
    ax.axvspan(2020.2, 2021.5, color="gray", alpha=0.15, lw=0)
    ax.set_title(f"LTT {subj}")
axes[0].set_ylabel("LTT scale score (0–500)")
axes[0].legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig("figures/fig_ltt.pdf"); plt.close(fig)

# Fig: LTT percentile changes, pre-pandemic (2012->2020), pandemic (2020->2022/23),
# post-pandemic (2022/23->2025; sources: evidence/ltt_2025.md API pull)
pcts = [10, 25, 50, 75, 90]
pre = {  # 2012 -> 2020
    "Age 13 math": [-12.6, -7.4, -4.4, -1.5, 0.1],
    "Age 13 reading": [-5.6, -3.3, -2.3, -1.3, -0.6],
    "Age 9 math": [-6.0, -4.2, -2.2, -0.9, -0.5],
    "Age 9 reading": [-6.6, -2.7, -0.7, 0.7, 2.0],
}
post = {  # 2020 -> 2022/2023
    "Age 13 math": [-14.0, -11.5, -8.1, -5.8, -6.5],
    "Age 13 reading": [-6.7, -5.6, -4.2, -3.7, -3.1],
    "Age 9 math": [-12.3, -10.6, -7.5, -5.2, -2.5],
    "Age 9 reading": [-9.5, -7.6, -4.3, -2.8, -2.4],
}
post2 = {  # 2022/2023 -> 2025
    "Age 13 math": [-2.8, -1.1, -0.8, -0.4, 2.3],
    "Age 13 reading": [1.2, 0.3, 0.1, 0.1, 0.6],
    "Age 9 math": [7.5, 5.9, 3.5, 1.6, 0.7],
    "Age 9 reading": [9.3, 6.3, 2.5, 1.2, 0.9],
}
fig, axes = plt.subplots(1, 3, figsize=(9.3, 3.1), sharey=True)
colors = {"Age 13 math": "#1f5fa8", "Age 13 reading": "#7fb0d8",
          "Age 9 math": "#b03a2e", "Age 9 reading": "#e09b94"}
for ax, (title, data) in zip(axes, [("Pre-pandemic: 2012 $\\rightarrow$ 2020", pre),
                                    ("Pandemic era: 2020 $\\rightarrow$ 2022/23", post),
                                    ("Post-pandemic: 2022/23 $\\rightarrow$ 2025", post2)]):
    for k, v in data.items():
        ax.plot(pcts, v, "-o", ms=3.5, color=colors[k], label=k)
    ax.axhline(0, color="k", lw=0.6)
    ax.set_title(title)
    ax.set_xticks(pcts)
    ax.set_xlabel("Percentile of score distribution")
axes[0].set_ylabel("Score change (LTT points)")
for ax in axes[1:]:
    ax.tick_params(axis="y", labelleft=True)
axes[0].legend(frameon=False, fontsize=7.5)
fig.tight_layout()
fig.savefig("figures/fig_ltt_percentiles.pdf"); plt.close(fig)

# Fig: reading for fun + screen context
years9 = [2008, 2012, 2020, 2022, 2025]; vals9 = [47.6, 52.5, 42.0, 39.3, 37.0]
years13 = [2008, 2012, 2020, 2023, 2025]; vals13 = [25.6, 27.1, 17.1, 14.3, 14.2]
never13_y = [2008, 2012, 2020, 2023, 2025]; never13 = [24.0, 21.9, 29.1, 31.2, 28.9]
fig, ax = plt.subplots(figsize=(5.2, 3.2))
ax.plot(years9, vals9, "-o", ms=4, color="#b03a2e", label="Age 9: reads for fun almost daily")
ax.plot(years13, vals13, "-o", ms=4, color="#1f5fa8", label="Age 13: reads for fun almost daily")
ax.plot(never13_y, never13, "--s", ms=4, color="#1f5fa8", alpha=0.6,
        label="Age 13: never/hardly ever reads for fun")
ax.set_ylabel("Percent of students")
ax.set_ylim(0, 60)
ax.set_xticks([2008, 2012, 2016, 2020, 2025])
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("figures/fig_readingfun.pdf"); plt.close(fig)

print("LTT figures done")
