"""Analyze main-NAEP pulls: trends, percentiles, subgroups, states.

Outputs summary tables (markdown to stdout + data/summary.json) and figures/*.pdf
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

df = pd.read_csv("data/naep_main.csv")
df = df[df["displayable"] == 1]

LBL = {("MAT", 4): "Math, Grade 4", ("MAT", 8): "Math, Grade 8",
       ("RED", 4): "Reading, Grade 4", ("RED", 8): "Reading, Grade 8"}
PCT = {"PC:P1": 10, "PC:P2": 25, "PC:P5": 50, "PC:P7": 75, "PC:P9": 90}

subj_codes = sorted(df["subject"].unique())
print("subjects in file:", subj_codes)
# normalize subject code for reading (could be 'RED' or 'RRP'); detect:
rsubj = [s for s in subj_codes if s != "MAT"][0]
LBL = {("MAT", 4): "Math, Grade 4", ("MAT", 8): "Math, Grade 8",
       (rsubj, 4): "Reading, Grade 4", (rsubj, 8): "Reading, Grade 8"}

nat = df[(df.dataset == "national")]
means = nat[nat.stat == "MN:MN"].pivot_table(index="year", columns=["subject", "grade"], values="value")

summary = {}

# ---------- 1. National mean trends ----------
print("\n## National mean trends")
rows = []
for key, label in LBL.items():
    s = means[key].dropna()
    # estimate student SD from 2013 percentile spread (P90-P10)/2.5631
    p = nat[(nat.subject == key[0]) & (nat.grade == key[1]) & (nat.year == 2013)]
    spread = (p[p.stat == "PC:P9"].value.iloc[0] - p[p.stat == "PC:P1"].value.iloc[0])
    sd = spread / 2.5631
    peak_year = int(s.idxmax()); peak = s.max()
    def ch(a, b):
        return s.get(b, np.nan) - s.get(a, np.nan)
    rows.append({
        "series": label, "sd_est": round(sd, 1),
        "peak_year": peak_year, "peak": round(peak, 1),
        "score_2013": round(s.get(2013, np.nan), 1),
        "score_2019": round(s.get(2019, np.nan), 1),
        "score_2022": round(s.get(2022, np.nan), 1),
        "score_2024": round(s.get(2024, np.nan), 1),
        "chg_2013_2019": round(ch(2013, 2019), 1),
        "chg_2019_2022": round(ch(2019, 2022), 1),
        "chg_2022_2024": round(ch(2022, 2024), 1),
        "chg_2013_2024": round(ch(2013, 2024), 1),
        "chg_2013_2024_sd": round(ch(2013, 2024) / sd, 2),
        "first_year_at_or_below_2024": int(s[s <= s.get(2024, np.nan)].index.min()),
    })
t1 = pd.DataFrame(rows)
print(t1.to_markdown(index=False))
summary["national_means"] = rows
summary["mean_series"] = {f"{k[0]}_G{k[1]}": {int(y): round(v, 1) for y, v in means[k].dropna().items()} for k in LBL}

# ---------- 2. Percentile divergence ----------
print("\n## Percentile changes (2013 -> 2024 and sub-periods)")
prow = []
for key, label in LBL.items():
    sub = nat[(nat.subject == key[0]) & (nat.grade == key[1]) & nat.stat.str.startswith("PC")]
    pv = sub.pivot_table(index="year", columns="stat", values="value")
    for stat, pct in PCT.items():
        s = pv[stat].dropna()
        prow.append({"series": label, "pctile": pct,
                     "chg_2013_2019": round(s.get(2019, np.nan) - s.get(2013, np.nan), 1),
                     "chg_2019_2022": round(s.get(2022, np.nan) - s.get(2019, np.nan), 1),
                     "chg_2022_2024": round(s.get(2024, np.nan) - s.get(2022, np.nan), 1),
                     "chg_2013_2024": round(s.get(2024, np.nan) - s.get(2013, np.nan), 1)})
t2 = pd.DataFrame(prow)
print(t2.to_markdown(index=False))
summary["percentile_changes"] = prow

# 90-10 gap over time
gaps = {}
for key, label in LBL.items():
    sub = nat[(nat.subject == key[0]) & (nat.grade == key[1])]
    pv = sub.pivot_table(index="year", columns="stat", values="value")
    gaps[label] = (pv["PC:P9"] - pv["PC:P1"]).dropna()
summary["gap_90_10"] = {k: {int(y): round(v, 1) for y, v in s.items()} for k, s in gaps.items()}

# ---------- 3. Subgroups ----------
print("\n## Subgroup mean changes")
sg = df[df.dataset == "subgroup"]
srow = []
for key, label in LBL.items():
    sub = sg[(sg.subject == key[0]) & (sg.grade == key[1])]
    for (var, grp), g in sub.groupby(["variable", "group"]):
        s = g.set_index("year")["value"]
        if 2013 not in s.index:
            continue
        srow.append({"series": label, "var": var, "group": grp,
                     "score_2013": round(s.get(2013, np.nan), 1),
                     "chg_2013_2019": round(s.get(2019, np.nan) - s.get(2013, np.nan), 1),
                     "chg_2019_2022": round(s.get(2022, np.nan) - s.get(2019, np.nan), 1),
                     "chg_2013_2022": round(s.get(2022, np.nan) - s.get(2013, np.nan), 1),
                     "chg_2013_2024": round(s.get(2024, np.nan) - s.get(2013, np.nan), 1)})
t3 = pd.DataFrame(srow)
print(t3.to_markdown(index=False))
summary["subgroup_changes"] = srow

# counterfactual: hold 2013 race composition fixed? (no weights via API; skip, note in text)

# ---------- 4. States ----------
print("\n## State-level analysis")
st = df[df.dataset == "state"]
strow = []
state_detail = {}
for key, label in LBL.items():
    sub = st[(st.subject == key[0]) & (st.grade == key[1])]
    pv = sub.pivot_table(index="jurisdiction", columns="year", values="value")
    d_pre = pv[2019] - pv[2013]
    d_covid = pv[2022] - pv[2019]
    d_rec = pv[2024] - pv[2022]
    below13 = (pv[2024] < pv[2013]).mean()
    declined_pre = (d_pre < 0).mean()
    corr = d_covid.corr(d_rec)
    strow.append({"series": label,
                  "share_states_declined_2013_2019": round(declined_pre, 2),
                  "median_chg_2013_2019": round(d_pre.median(), 1),
                  "median_chg_2019_2022": round(d_covid.median(), 1),
                  "median_chg_2022_2024": round(d_rec.median(), 1),
                  "share_states_below_2013_in_2024": round(below13, 2),
                  "corr_drop_vs_recovery": round(corr, 2)})
    state_detail[label] = {
        "d_pre": d_pre.dropna().to_dict(), "d_covid": d_covid.dropna().to_dict(),
        "d_rec": d_rec.dropna().to_dict()}
t4 = pd.DataFrame(strow)
print(t4.to_markdown(index=False))
summary["states"] = strow

with open("data/summary.json", "w") as f:
    json.dump(summary, f, indent=1)

# ================= FIGURES =================
C = {"MAT4": "#1f5fa8", "MAT8": "#7fb0d8", "RED4": "#b03a2e", "RED8": "#e09b94"}

# Fig 1: national means, 4 panels
fig, axes = plt.subplots(2, 2, figsize=(7, 5), sharex=True)
for ax, (key, label) in zip(axes.flat, LBL.items()):
    s = means[key].dropna()
    ax.plot(s.index, s.values, "-o", ms=3, color="#1f5fa8")
    pk = s.idxmax()
    ax.axvline(2013, color="gray", lw=0.7, ls=":")
    ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
    ax.set_title(label)
    ax.annotate(f"peak {int(pk)}: {s.max():.0f}", (pk, s.max()),
                textcoords="offset points", xytext=(0, 6), ha="center", fontsize=7)
fig.supylabel("NAEP scale score")
fig.tight_layout()
fig.savefig("figures/fig_national_trends.pdf"); plt.close(fig)

# Fig 2: percentile changes since 2013, G8 math & reading
fig, axes = plt.subplots(1, 2, figsize=(7, 3), sharey=True)
for ax, key in zip(axes, [("MAT", 8), (rsubj, 8)]):
    sub = nat[(nat.subject == key[0]) & (nat.grade == key[1])]
    pv = sub.pivot_table(index="year", columns="stat", values="value")
    pv = pv[pv.index >= 2003]
    cmap = plt.cm.coolwarm_r
    for i, (stat, pct) in enumerate(PCT.items()):
        s = pv[stat] - pv[stat].loc[2013]
        ax.plot(s.index, s.values, "-o", ms=2.5, color=cmap(i / 4),
                label=f"{pct}th")
    ax.axhline(0, color="k", lw=0.6)
    ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
    ax.set_title(LBL[key])
axes[0].set_ylabel("Score change since 2013")
axes[1].legend(frameon=False, fontsize=7, title="Percentile", title_fontsize=7)
fig.tight_layout()
fig.savefig("figures/fig_percentiles_g8.pdf"); plt.close(fig)

# Fig 2b: same for grade 4
fig, axes = plt.subplots(1, 2, figsize=(7, 3), sharey=True)
for ax, key in zip(axes, [("MAT", 4), (rsubj, 4)]):
    sub = nat[(nat.subject == key[0]) & (nat.grade == key[1])]
    pv = sub.pivot_table(index="year", columns="stat", values="value")
    pv = pv[pv.index >= 2003]
    cmap = plt.cm.coolwarm_r
    for i, (stat, pct) in enumerate(PCT.items()):
        s = pv[stat] - pv[stat].loc[2013]
        ax.plot(s.index, s.values, "-o", ms=2.5, color=cmap(i / 4), label=f"{pct}th")
    ax.axhline(0, color="k", lw=0.6)
    ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
    ax.set_title(LBL[key])
axes[0].set_ylabel("Score change since 2013")
axes[1].legend(frameon=False, fontsize=7, title="Percentile", title_fontsize=7)
fig.tight_layout()
fig.savefig("figures/fig_percentiles_g4.pdf"); plt.close(fig)

# Fig 3: 90-10 gap
fig, ax = plt.subplots(figsize=(5.5, 3.2))
colors = ["#1f5fa8", "#7fb0d8", "#b03a2e", "#e09b94"]
for (label, s), c in zip(gaps.items(), colors):
    s = s[s.index >= 2003]
    ax.plot(s.index, s.values, "-o", ms=3, color=c, label=label)
ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
ax.set_ylabel("90th $-$ 10th percentile gap (scale points)")
ax.legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("figures/fig_gap9010.pdf"); plt.close(fig)

# Fig 4: lunch-eligibility subgroup trends, G8 math + G4 reading
fig, axes = plt.subplots(1, 2, figsize=(7, 3))
for ax, key in zip(axes, [("MAT", 8), (rsubj, 4)]):
    sub = sg[(sg.subject == key[0]) & (sg.grade == key[1]) & (sg.variable == "SLUNCH3")]
    for grp, c in [("Eligible", "#b03a2e"), ("Not eligible", "#1f5fa8")]:
        s = sub[sub.group == grp].set_index("year")["value"].sort_index()
        s = s[s.index >= 2003]
        ax.plot(s.index, s.values, "-o", ms=3, color=c, label=f"NSLP {grp.lower()}")
    ax.axvspan(2020, 2021.5, color="gray", alpha=0.15, lw=0)
    ax.set_title(LBL[key])
axes[0].set_ylabel("NAEP scale score")
axes[0].legend(frameon=False, fontsize=8)
fig.tight_layout()
fig.savefig("figures/fig_lunch.pdf"); plt.close(fig)

# Fig 5: state scatter — covid drop vs recovery, G4 math
fig, axes = plt.subplots(1, 2, figsize=(7, 3.4))
for ax, key in zip(axes, [("MAT", 4), ("MAT", 8)]):
    label = LBL[key]
    d = state_detail[label]
    x = pd.Series(d["d_covid"]); y = pd.Series(d["d_rec"])
    common = x.index.intersection(y.index)
    ax.scatter(x[common], y[common], s=8, color="#1f5fa8", alpha=0.7)
    for st_ in common:
        ax.annotate(st_, (x[st_], y[st_]), fontsize=4.5, alpha=0.6,
                    textcoords="offset points", xytext=(2, 2))
    b, a = np.polyfit(x[common], y[common], 1)
    xs = np.linspace(x[common].min(), x[common].max(), 10)
    ax.plot(xs, a + b * xs, color="#b03a2e", lw=1)
    ax.axhline(0, color="k", lw=0.5); ax.axvline(0, color="k", lw=0.5)
    ax.set_xlabel("Change 2019–2022")
    ax.set_title(f"{label} (slope={b:.2f}, r={x[common].corr(y[common]):.2f})")
axes[0].set_ylabel("Change 2022–2024")
fig.tight_layout()
fig.savefig("figures/fig_states.pdf"); plt.close(fig)

print("\nfigures written")
