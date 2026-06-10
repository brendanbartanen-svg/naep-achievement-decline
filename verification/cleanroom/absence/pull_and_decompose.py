#!/usr/bin/env python3
"""Clean-room replication: NAEP declines attributable to shift in student-reported
absences (B018101). Pulls fresh from NAEP Data Service API, computes absence-share
time series and Kitagawa/Oaxaca decompositions. Writes results.json + raw CSV."""

import json
import time
import urllib.request
import urllib.parse

import pandas as pd

BASE = "https://www.nationsreportcard.gov/DataService/GetAdhocData.aspx"
OUT = "/Users/yvp3tf/Documents/CC Sandbox/naep-achievement-decline/verification/cleanroom/absence"

SUBJECTS = [("mathematics", "MRPCM"), ("reading", "RRPCM")]
GRADES = [4, 8]
STATTYPES = ["MN:MN", "RP:RP"]
YEAR_CHUNKS = [["2013", "2015"], ["2017", "2019"], ["2022", "2024"]]


def fetch(params, tries=4):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                payload = json.loads(r.read().decode("utf-8"))
            if payload.get("status") == 200:
                return payload["result"]
            raise RuntimeError(f"API status {payload.get('status')}: {str(payload)[:300]}")
        except Exception as e:
            if i == tries - 1:
                raise
            print(f"  retry {i+1} after error: {e}")
            time.sleep(3 * (i + 1))


rows = []
for subject, scale in SUBJECTS:
    for grade in GRADES:
        for stattype in STATTYPES:
            for chunk in YEAR_CHUNKS:
                params = {
                    "type": "data",
                    "subject": subject,
                    "grade": grade,
                    "subscale": scale,
                    "variable": "B018101",
                    "jurisdiction": "NT",
                    "stattype": stattype,
                    "Year": ",".join(chunk),
                }
                print(f"pull {subject} g{grade} {stattype} {chunk}")
                res = fetch(params)
                rows.extend(res)
                time.sleep(1)

df = pd.DataFrame(rows)
df.to_csv(f"{OUT}/raw_b018101.csv", index=False)
print(f"\n{len(df)} rows pulled")

# Reload defensively the way the task warns about (label "None" must survive)
df = pd.read_csv(f"{OUT}/raw_b018101.csv", keep_default_na=False)
df["value"] = pd.to_numeric(df["value"], errors="coerce")
df["stat"] = df["stattype"].map({"MN:MN": "mean", "RP:RP": "pct"})

# sanity: displayable
bad = df[(df["isStatDisplayable"] != 1) | (df["errorFlag"] != 0)]
if len(bad):
    print(f"WARNING: {len(bad)} rows flagged not-displayable/error")
    print(bad[["subject", "grade", "year", "stat", "varValueLabel", "value"]])

piv = df.pivot_table(
    index=["subject", "grade", "year", "varValueLabel", "varValue"],
    columns="stat", values="value", aggfunc="first",
).reset_index()

CAT_ORDER = ["None", "1-2 days", "3-4 days", "5-10 days", "More than 10 days"]
ABSENT3 = ["3-4 days", "5-10 days", "More than 10 days"]

# --- 2. share of G8 students absent 3+ days ---
shares_3plus = {}
for subj in ["MAT", "RED"]:
    sub = piv[(piv.subject == subj) & (piv.grade == 8)]
    for yr in sorted(sub.year.unique()):
        s = sub[sub.year == yr]
        tot = s.pct.sum()
        share = s[s.varValueLabel.isin(ABSENT3)].pct.sum()
        shares_3plus.setdefault(subj, {})[int(yr)] = {
            "pct_3plus": round(float(share), 2),
            "pct_sum_check": round(float(tot), 2),
        }

# full share tables (all categories, all years, both grades)
share_tables = {}
for subj in ["MAT", "RED"]:
    for g in GRADES:
        sub = piv[(piv.subject == subj) & (piv.grade == g)]
        tab = sub.pivot_table(index="varValueLabel", columns="year", values="pct")
        tab = tab.reindex(CAT_ORDER)
        share_tables[f"{subj}_g{g}"] = json.loads(tab.round(2).to_json())


# --- 3. Kitagawa/Oaxaca decomposition ---
def decompose(subj, grade, y0, y1):
    sub = piv[(piv.subject == subj) & (piv.grade == grade)]
    a = sub[sub.year == y0].set_index("varValueLabel").reindex(CAT_ORDER)
    b = sub[sub.year == y1].set_index("varValueLabel").reindex(CAT_ORDER)
    s0, s1 = a.pct / 100.0, b.pct / 100.0
    m0, m1 = a["mean"], b["mean"]
    # renormalize shares to sum exactly to 1 (rounding in API percentages)
    s0, s1 = s0 / s0.sum(), s1 / s1.sum()
    mu0, mu1 = float((s0 * m0).sum()), float((s1 * m1).sum())
    total = mu1 - mu0
    ds, dm = s1 - s0, m1 - m0
    comp_base0 = float((ds * m0).sum())          # comp at base(y0) means; within at y1 shares
    within_base0 = float((s1 * dm).sum())
    comp_base1 = float((ds * m1).sum())          # comp at end(y1) means; within at y0 shares
    within_base1 = float((s0 * dm).sum())
    comp_mid = float((ds * (m0 + m1) / 2).sum())  # midpoint (exact two-part split)
    within_mid = float(((s0 + s1) / 2 * dm).sum())
    return {
        "period": f"{y0}->{y1}",
        "implied_mean_y0": round(mu0, 2),
        "implied_mean_y1": round(mu1, 2),
        "total_change": round(total, 3),
        "composition_base_period_means": round(comp_base0, 3),
        "within_component_base_period": round(within_base0, 3),
        "composition_end_period_means": round(comp_base1, 3),
        "within_component_end_period": round(within_base1, 3),
        "composition_midpoint": round(comp_mid, 3),
        "within_midpoint": round(within_mid, 3),
        "composition_pct_of_change_base": round(100 * comp_base0 / total, 1),
        "composition_pct_of_change_end": round(100 * comp_base1 / total, 1),
        "composition_pct_of_change_midpoint": round(100 * comp_mid / total, 1),
    }


decomps = {}
for subj, name in [("RED", "g8_reading"), ("MAT", "g8_math")]:
    decomps[name] = {
        "2019_to_2024": decompose(subj, 8, 2019, 2024),
        "2013_to_2019": decompose(subj, 8, 2013, 2019),
    }

results = {
    "meta": {
        "source": "NAEP Data Service API GetAdhocData.aspx, pulled fresh",
        "variable": "B018101 (Days absent from school in the last month)",
        "jurisdiction": "NT (national)",
        "pull_date": "2026-06-10",
        "categories": CAT_ORDER,
        "absent_3plus_def": ABSENT3,
        "notes": (
            "Shares are RP:RP row percentages among students with valid B018101 "
            "response; renormalized to sum to 1 for decomposition. Total change is "
            "the change in the share-weighted crosstab mean (may differ slightly "
            "from published overall mean due to item nonresponse). Headline "
            "composition share uses the midpoint convention (exact two-part split); "
            "both base-period conventions also reported."
        ),
    },
    "g8_absent_3plus_share": {
        "math_sample": {str(y): shares_3plus["MAT"][y]["pct_3plus"] for y in sorted(shares_3plus["MAT"])},
        "reading_sample": {str(y): shares_3plus["RED"][y]["pct_3plus"] for y in sorted(shares_3plus["RED"])},
    },
    "share_tables_pct": share_tables,
    "decompositions": decomps,
}

with open(f"{OUT}/results.json", "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps(results["g8_absent_3plus_share"], indent=2))
print(json.dumps(decomps, indent=2))
print("\nwrote results.json")
