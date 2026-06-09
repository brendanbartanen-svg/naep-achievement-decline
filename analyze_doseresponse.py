"""#4: State dose-response — pandemic schooling mode and absenteeism vs NAEP changes.

(a) Delta NAEP 2019->2022 vs share of 2020-21 spent virtual (CSDH, enrollment-weighted).
(b) Recovery 2022->2024 and net 2019->2024 vs virtual share and vs the rise in
    chronic absenteeism (FutureEd 2018-19 -> 2023-24).
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

US_ABBR = {
 'Alabama':'AL','Alaska':'AK','Arizona':'AZ','Arkansas':'AR','California':'CA','Colorado':'CO',
 'Connecticut':'CT','Delaware':'DE','District of Columbia':'DC','Dist. of Columbia':'DC',
 'Florida':'FL','Georgia':'GA','Hawaii':'HI','Idaho':'ID','Illinois':'IL','Indiana':'IN',
 'Iowa':'IA','Kansas':'KS','Kentucky':'KY','Louisiana':'LA','Maine':'ME','Maryland':'MD',
 'Massachusetts':'MA','Michigan':'MI','Minnesota':'MN','Mississippi':'MS','Missouri':'MO',
 'Montana':'MT','Nebraska':'NE','Nevada':'NV','New Hampshire':'NH','New Jersey':'NJ',
 'New Mexico':'NM','New York':'NY','North Carolina':'NC','North Dakota':'ND','Ohio':'OH',
 'Oklahoma':'OK','Oregon':'OR','Pennsylvania':'PA','Rhode Island':'RI','South Carolina':'SC',
 'South Dakota':'SD','Tennessee':'TN','Texas':'TX','Utah':'UT','Vermont':'VT','Virginia':'VA',
 'Washington':'WA','West Virginia':'WV','Wisconsin':'WI','Wyoming':'WY'}

# --- NAEP state changes ---
main = pd.read_csv("data/naep_main.csv")
st = main[(main.dataset == "state") & (main.displayable == 1)]
rsubj = [s for s in st.subject.unique() if s != "MAT"][0]
LBL = {("MAT", 4): "Math G4", ("MAT", 8): "Math G8",
       (rsubj, 4): "Reading G4", (rsubj, 8): "Reading G8"}
chg = {}
for key, label in LBL.items():
    pv = st[(st.subject == key[0]) & (st.grade == key[1])].pivot_table(
        index="jurisdiction", columns="year", values="value")
    chg[label] = pd.DataFrame({
        "d_1922": pv[2022] - pv[2019],
        "d_2224": pv[2024] - pv[2022],
        "d_1924": pv[2024] - pv[2019]})

# --- external data ---
csdh = pd.read_csv("data/external/CSDH_state_learning_model_shares_2020_21.csv")
csdh = csdh.set_index("StateAbbrev")[["share_virtual", "share_hybrid", "share_inperson"]]

fe = pd.read_csv("data/external/FutureEd_state_chronic_absenteeism.csv")
fe["abbr"] = fe["state"].map(US_ABBR)
fe = fe.dropna(subset=["abbr"]).set_index("abbr")
for c in ["2018-19", "2023-24"]:
    fe[c] = pd.to_numeric(fe[c].astype(str).str.replace("%", "").str.replace("*", ""),
                          errors="coerce")
fe["d_abs"] = fe["2023-24"] - fe["2018-19"]

out = {}
print("## Dose-response regressions (unweighted state OLS, HC1 SEs)")
rows = []
for label, c in chg.items():
    m = c.join(csdh, how="inner").join(fe[["d_abs"]], how="left")
    # (a) pandemic drop vs virtual share
    r1 = smf.ols("d_1922 ~ share_virtual", data=m).fit(cov_type="HC1")
    # (b) recovery vs virtual share
    r2 = smf.ols("d_2224 ~ share_virtual", data=m).fit(cov_type="HC1")
    # (c) net 2019-2024 vs virtual share
    r3 = smf.ols("d_1924 ~ share_virtual", data=m).fit(cov_type="HC1")
    # (d) net vs absenteeism rise (subset with FutureEd data)
    md = m.dropna(subset=["d_abs"])
    r4 = smf.ols("d_1924 ~ d_abs", data=md).fit(cov_type="HC1")
    # (e) both
    r5 = smf.ols("d_1924 ~ share_virtual + d_abs", data=md).fit(cov_type="HC1")
    rows.append({
        "series": label, "n": int(r1.nobs),
        "drop~virt b(per10pp)": round(r1.params["share_virtual"] / 10, 2),
        "p1": round(r1.pvalues["share_virtual"], 3),
        "recov~virt b": round(r2.params["share_virtual"] / 10, 2),
        "p2": round(r2.pvalues["share_virtual"], 3),
        "net~virt b": round(r3.params["share_virtual"] / 10, 2),
        "p3": round(r3.pvalues["share_virtual"], 3),
        "net~dAbs b(per pp)": round(r4.params["d_abs"], 2),
        "p4": round(r4.pvalues["d_abs"], 3),
        "joint: virt": round(r5.params["share_virtual"] / 10, 2),
        "joint: dAbs": round(r5.params["d_abs"], 2),
    })
    out[label] = rows[-1]
print(pd.DataFrame(rows).to_markdown(index=False))
# note: share_virtual in 0-1 units; "per10pp" = coefficient*0.1

# pooled across the four series (series FE, cluster by state)
stack = []
for label, c in chg.items():
    m = c.join(csdh, how="inner").join(fe[["d_abs"]], how="left").reset_index()
    m["series"] = label
    stack.append(m)
pool = pd.concat(stack)
pool = pool.rename(columns={"index": "state"}) if "index" in pool.columns else pool
pool["state"] = pool.get("state", pool.get("jurisdiction"))
for dv, name in [("d_1922", "drop 2019-22"), ("d_1924", "net 2019-24")]:
    mP = smf.ols(f"{dv} ~ share_virtual + C(series)", data=pool).fit(
        cov_type="cluster", cov_kwds={"groups": pool["state"]})
    print(f"\nPooled {name} ~ virtual: {mP.params['share_virtual']/10:+.2f} pts/10pp "
          f"(p={mP.pvalues['share_virtual']:.3f}, n={int(mP.nobs)})")
    out[f"pooled_{dv}_virt"] = {"b_per10pp": round(mP.params["share_virtual"] / 10, 2),
                                "p": round(mP.pvalues["share_virtual"], 3)}
pa = pool.dropna(subset=["d_abs"])
mA = smf.ols("d_1924 ~ d_abs + C(series)", data=pa).fit(
    cov_type="cluster", cov_kwds={"groups": pa["state"]})
print(f"Pooled net 2019-24 ~ rise in absenteeism: {mA.params['d_abs']:+.2f} pts/pp "
      f"(p={mA.pvalues['d_abs']:.3f}, n={int(mA.nobs)})")
out["pooled_d1924_dabs"] = {"b_per_pp": round(mA.params["d_abs"], 2),
                            "p": round(mA.pvalues["d_abs"], 3)}

with open("data/doseresponse_results.json", "w") as f:
    json.dump(out, f, indent=1)

# --- figure ---
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.3))
ax = axes[0]
m = chg["Math G4"].join(csdh, how="inner")
x = m.share_virtual * 100
ax.scatter(x, m.d_1922, s=10, color="#1f5fa8", alpha=0.75)
for stx in m.index:
    ax.annotate(stx, (x[stx], m.d_1922[stx]), fontsize=4.5, alpha=0.6,
                textcoords="offset points", xytext=(2, 2))
b, a = np.polyfit(x, m.d_1922, 1)
xs = np.linspace(0, x.max(), 10)
ax.plot(xs, a + b * xs, color="#b03a2e", lw=1)
ax.set_xlabel("Percent of 2020--21 fully virtual")
ax.set_ylabel("Change in NAEP mean, 2019--2022")
ax.set_title(f"Math G4: slope {10*b:.2f} pts/10pp virtual")

ax = axes[1]
m = chg["Math G4"].join(fe[["d_abs"]], how="inner").dropna()
ax.scatter(m.d_abs, m.d_1924, s=10, color="#1f5fa8", alpha=0.75)
for stx in m.index:
    ax.annotate(stx, (m.d_abs[stx], m.d_1924[stx]), fontsize=4.5, alpha=0.6,
                textcoords="offset points", xytext=(2, 2))
b, a = np.polyfit(m.d_abs, m.d_1924, 1)
xs = np.linspace(m.d_abs.min(), m.d_abs.max(), 10)
ax.plot(xs, a + b * xs, color="#b03a2e", lw=1)
ax.set_xlabel("Rise in chronic absenteeism, 2018-19 to 2023-24 (pp)")
ax.set_ylabel("Change in NAEP mean, 2019--2024")
ax.set_title(f"Math G4: slope {b:.2f} pts/pp absenteeism")
fig.tight_layout()
fig.savefig("figures/fig_doseresponse.pdf"); plt.close(fig)
print("\ndose-response figure done")
