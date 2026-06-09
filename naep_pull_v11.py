"""v1.1 pulls: school-type (public/private/Catholic) national trends + state-level percentiles."""
import json, time, urllib.request, urllib.parse, csv, sys

BASE = "https://www.nationsreportcard.gov/DataService/GetAdhocData.aspx"
SCALE = {"mathematics": "MRPCM", "reading": "RRPCM"}
YEARS = "2003,2005,2007,2009,2011,2013,2015,2017,2019,2022,2024"
STATS_ALL = "MN:MN,PC:P1,PC:P2,PC:P5,PC:P7,PC:P9"
STATES = ("AL,AK,AZ,AR,CA,CO,CT,DE,DC,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,"
          "NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY")

def chunks(csvlist, n):
    items = csvlist.split(",")
    return [",".join(items[i:i + n]) for i in range(0, len(items), n)]

def fetch(params, tries=3):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                d = json.loads(r.read().decode())
            if d.get("status") == 200:
                return d["result"]
            print("  API error:", str(d)[:150], file=sys.stderr, flush=True)
            return []
        except Exception as e:
            print(f"  retry {i+1}: {e}", file=sys.stderr, flush=True)
            time.sleep(3 * (i + 1))
    return []

rows = []

def save():
    if not rows:
        return
    with open("data/naep_v11.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  saved {len(rows)} rows", flush=True)

def add(result, tag):
    for x in result:
        rows.append({
            "dataset": tag, "subject": x["subject"], "grade": x["grade"],
            "year": x["year"], "jurisdiction": x["jurisdiction"],
            "stat": x["stattype"], "variable": x["variable"],
            "group": x["varValueLabel"], "value": x["value"],
            "errorFlag": x.get("errorFlag"), "displayable": x.get("isStatDisplayable"),
        })

# 1. School type, national: means + percentiles
for subj in ("mathematics", "reading"):
    for grade in (4, 8):
        for var in ("SCHTYP2", "SCHTYPE"):
            for yc in chunks(YEARS, 4):
                print(f"schtype {subj} G{grade} {var} {yc}", flush=True)
                add(fetch({"type": "data", "subject": subj, "grade": grade,
                           "subscale": SCALE[subj], "variable": var, "jurisdiction": "NT",
                           "stattype": STATS_ALL if var == "SCHTYP2" else "MN:MN",
                           "Year": yc}), "schtype")
                time.sleep(0.4)
        save()

# 2. State percentiles (P10, P25, P50, P90)
for subj in ("mathematics", "reading"):
    for grade in (4, 8):
        for sc in chunks(STATES, 13):
            for yc in chunks(YEARS, 3):
                print(f"statepct {subj} G{grade} [{sc[:8]}...] {yc}", flush=True)
                add(fetch({"type": "data", "subject": subj, "grade": grade,
                           "subscale": SCALE[subj], "variable": "TOTAL", "jurisdiction": sc,
                           "stattype": "PC:P1,PC:P2,PC:P5,PC:P9", "Year": yc}), "statepct")
                time.sleep(0.4)
        save()

save()
print(f"DONE: {len(rows)} rows", flush=True)
