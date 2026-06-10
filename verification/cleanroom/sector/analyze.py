import json, math

means_sd = json.load(open("api_means_sd.json"))
sig = json.load(open("api_sigtests.json"))

# ---- organize means and SDs ----
data = {}  # (subj, grade, year, sector) -> {"mean":, "sd":}
SECTOR = {"1":"public", "3":"catholic"}
for r in means_sd:
    if r["varValue"] not in SECTOR or not r["isStatDisplayable"]:
        continue
    key = (r["subject"], r["grade"], r["year"], SECTOR[r["varValue"]])
    d = data.setdefault(key, {})
    if r["stattype"] == "MN:MN": d["mean"] = r["value"]
    elif r["stattype"] == "SD:SD": d["sd"] = r["value"]

# ---- sample size assumptions (documented) ----
# Assessed-student counts from official technical appendices (participation tables):
#   2019 reading G8: public 138,100; private 2,600   (2019 reading tech appendix, Table A-5)
#   2019 math    G8: public 142,200; private 2,700   (2019 math tech appendix, Table A-5)
#   2024 reading G8: public 108,000; private 1,500   (2024 reading tech appendix, Participation G8)
#   2024 math    G8: public 107,700; private 1,500   (2024 math tech appendix, Participation G8)
#   2013: same design as 2019 (state public samples + national private sample); private n assumed ~2,600
# Catholic assumed ~55% of assessed private-school students (range 40-70%);
# design effect (clustered school samples) assumed deff = 3 (range 2-4).
N = {
 ("RED",8,2013): {"public":171800, "private":2600},
 ("MAT",8,2013): {"public":170100, "private":2700},
 ("RED",8,2019): {"public":138100, "private":2600},
 ("MAT",8,2019): {"public":142200, "private":2700},
 ("RED",8,2024): {"public":108000, "private":1500},
 ("MAT",8,2024): {"public":107700, "private":1500},
}
CATH_SHARE, DEFF = 0.55, 3.0

def se_mean(subj, grade, year, sector):
    d = data.get((subj, grade, year, sector))
    if not d or "sd" not in d: return None
    nrow = N.get((subj, grade, year))
    if not nrow: return None
    n = nrow["public"] if sector=="public" else nrow["private"]*CATH_SHARE
    return d["sd"] * math.sqrt(DEFF / n)

def change(subj, grade, y1, y2, sector):
    m1 = data.get((subj,grade,y1,sector),{}).get("mean")
    m2 = data.get((subj,grade,y2,sector),{}).get("mean")
    s1, s2 = se_mean(subj,grade,y1,sector), se_mean(subj,grade,y2,sector)
    if None in (m1,m2,s1,s2): return None
    delta = m2-m1; se = math.sqrt(s1**2+s2**2)
    return {"y1":y1,"y2":y2,"mean_y1":round(m1,2),"mean_y2":round(m2,2),
            "change":round(delta,2),"se_approx":round(se,2),"z_approx":round(delta/se,2)}

def official_change_verdict(subj, grade, y1, y2, sector_code):
    for r in sig["sigacrossyear"]:
        if (r["subject"]==subj and r["grade"]==grade and r["valValue"]==sector_code
            and r["focalYear"]==y1 and r["targetYear"]==y2 and r["isSigDisplayable"]):
            # gap = focal - target = y1 - y2; verdict 'HIGHER' means y1 > y2 (decline)
            return {"gap_y1_minus_y2": round(r["gap"],2), "verdict_focal_vs_target": r["sig"]}
    return None

def official_did(subj, grade, y1, y2):
    # rows where val pair is public(1) vs catholic(3), focal year y1 target y2
    for r in sig["gaponvaracrossyear"]:
        vals = {r["valValue1"], r["valValue2"]}
        if (r["subject"]==subj and r["grade"]==grade and vals=={"1","3"}
            and r["focalYear"]==y1 and r["targetYear"]==y2 and r["isGapDisplayable"]):
            return {"innerDiff_focal": round(r["innerDiff1"],2), "innerDiff_target": round(r["innerDiff2"],2),
                    "gap_DiD": round(r["gap"],2), "verdict": r["sig"],
                    "val1": r["valLabel1"], "val2": r["valLabel2"]}
    return None

results = {"metadata": {
    "means_sds_source": "NAEP Data Service API GetAdhocData (type=data, stattype MN:MN and SD:SD), variable SCHTYPE, jurisdiction NT",
    "official_sig_source": "NAEP Data Service API GetAdhocData (type=sigacrossyear and type=gaponvaracrossyear) - NAEP's own significance tests using its internal standard errors",
    "se_method": ("APPROXIMATED from SD (stattype SD:SD): SE = SD*sqrt(deff/n). True SEs live in the NAEP Data Explorer, "
                  "whose backend (POST /ndecore/api/dataTable) could not be invoked programmatically (HTTP 400; "
                  "undocumented contract) and whose UI requires an interactive session that repeatedly froze. "
                  "n from official technical-appendix participation tables (assessed-student counts); "
                  "Catholic n assumed 55% of private-school n (range 40-70%); design effect assumed 3 (range 2-4)."),
    "n_assumptions": {str(k): v for k,v in N.items()},
    "catholic_share_of_private_n": CATH_SHARE, "design_effect": DEFF,
}, "grade8": {}, "grade4_descriptive": {}}

for subj, sname in [("RED","reading"), ("MAT","math")]:
    block = {}
    for sector, scode in [("public","1"), ("catholic","3")]:
        for (y1,y2) in [(2013,2019),(2019,2024),(2013,2024),(2019,2022),(2022,2024)]:
            c = change(subj,8,y1,y2,sector)
            if c:
                c["official_naep_test"] = official_change_verdict(subj,8,y1,y2,scode)
                block[f"{sector}_change_{y1}_{y2}"] = c
    # DiD public minus catholic: (pub_y2-pub_y1) - (cath_y2-cath_y1)
    for (y1,y2) in [(2013,2019),(2019,2024)]:
        cp = change(subj,8,y1,y2,"public"); cc = change(subj,8,y1,y2,"catholic")
        if cp and cc:
            did = cp["change"] - cc["change"]
            se = math.sqrt(cp["se_approx"]**2 + cc["se_approx"]**2)
            block[f"DiD_publicMinusCatholic_{y1}_{y2}"] = {
                "public_change": cp["change"], "catholic_change": cc["change"],
                "did": round(did,2), "se_approx": round(se,2), "z_approx": round(did/se,2),
                "official_naep_gap_test": official_did(subj,8,y1,y2)}
    results["grade8"][sname] = block

# grade 4 descriptive changes (means only)
for subj, sname in [("RED","reading"), ("MAT","math")]:
    block = {}
    for sector in ["public","catholic"]:
        for (y1,y2) in [(2013,2019),(2019,2024)]:
            m1 = data.get((subj,4,y1,sector),{}).get("mean")
            m2 = data.get((subj,4,y2,sector),{}).get("mean")
            if m1 and m2:
                scode = "1" if sector=="public" else "3"
                block[f"{sector}_{y1}_{y2}"] = {"mean_y1":round(m1,2),"mean_y2":round(m2,2),
                    "change":round(m2-m1,2),
                    "official_naep_test": official_change_verdict(subj,4,y1,y2,scode)}
    results["grade4_descriptive"][sname] = block

# trend table for context
trend = {}
for (subj, grade, year, sector), d in sorted(data.items()):
    if grade!=8: continue
    trend.setdefault(f"{subj}_G8_{sector}", {})[year] = round(d.get("mean",float('nan')),2)
results["grade8_mean_trends"] = trend

json.dump(results, open("results.json","w"), indent=1)
print(json.dumps(results["grade8"], indent=1))
