"""Pull main-NAEP national + state data from the NCES Data Service API."""
import json, time, urllib.request, urllib.parse, csv, sys

BASE = "https://www.nationsreportcard.gov/DataService/GetAdhocData.aspx"

YEARS = {
    ("mathematics", 4): "1990R2,1992R2,1996R2,2000R3,2003,2005,2007,2009,2011,2013,2015,2017,2019,2022,2024",
    ("mathematics", 8): "1990R2,1992R2,1996R2,2000R3,2003,2005,2007,2009,2011,2013,2015,2017,2019,2022,2024",
    ("reading", 4): "1992R2,1994R2,1998R3,2000R3,2002,2003,2005,2007,2009,2011,2013,2015,2017,2019,2022,2024",
    ("reading", 8): "1992R2,1994R2,1998R3,2002,2003,2005,2007,2009,2011,2013,2015,2017,2019,2022,2024",
}
SCALE = {"mathematics": "MRPCM", "reading": "RRPCM"}
STATS = "MN:MN,PC:P1,PC:P2,PC:P5,PC:P7,PC:P9"

STATES = ("AL,AK,AZ,AR,CA,CO,CT,DE,DC,FL,GA,HI,ID,IL,IN,IA,KS,KY,LA,ME,MD,MA,MI,MN,MS,MO,MT,"
          "NE,NV,NH,NJ,NM,NY,NC,ND,OH,OK,OR,PA,RI,SC,SD,TN,TX,UT,VT,VA,WA,WV,WI,WY")

def fetch(params, tries=3):
    url = BASE + "?" + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                d = json.loads(r.read().decode())
            if d.get("status") == 200:
                return d["result"]
            print("  API error:", str(d)[:200], file=sys.stderr, flush=True)
            return []
        except Exception as e:
            print(f"  retry {i+1}: {e}", file=sys.stderr, flush=True)
            time.sleep(3 * (i + 1))
    return []

rows = []

def chunks(csvlist, n):
    items = csvlist.split(",")
    return [",".join(items[i:i + n]) for i in range(0, len(items), n)]

def save():
    if not rows:
        return
    with open("data/naep_main.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"  saved {len(rows)} rows", flush=True)

def add(result, tag):
    for x in result:
        rows.append({
            "dataset": tag, "subject": x["subject"], "grade": x["grade"],
            "year": x["year"], "jurisdiction": x["jurisdiction"],
            "jurisLabel": x["jurisLabel"], "stat": x["stattype"],
            "variable": x["variable"], "group": x["varValueLabel"],
            "value": x["value"], "errorFlag": x.get("errorFlag"),
            "displayable": x.get("isStatDisplayable"),
        })

# 1. National means + percentiles (chunk years by 4)
for (subj, grade), yrs in YEARS.items():
    for yc in chunks(yrs, 4):
        print(f"national {subj} G{grade} {yc}", flush=True)
        add(fetch({"type": "data", "subject": subj, "grade": grade, "subscale": SCALE[subj],
                   "variable": "TOTAL", "jurisdiction": "NT", "stattype": STATS, "Year": yc}),
            "national")
        time.sleep(0.5)
    save()

# 2. National subgroup means (2003+ only)
for (subj, grade), yrs in YEARS.items():
    yrs03 = ",".join(y for y in yrs.split(",") if y.isdigit() and int(y) >= 2003)
    for var in ("SDRACE", "GENDER", "SLUNCH3"):
        for yc in chunks(yrs03, 4):
            print(f"subgroup {subj} G{grade} {var} {yc}", flush=True)
            add(fetch({"type": "data", "subject": subj, "grade": grade, "subscale": SCALE[subj],
                       "variable": var, "jurisdiction": "NT", "stattype": "MN:MN", "Year": yc}),
                "subgroup")
            time.sleep(0.5)
    save()

# 3. State means (key years only; chunk states by 13)
state_years = "2013,2015,2017,2019,2022,2024"
for subj in ("mathematics", "reading"):
    for grade in (4, 8):
        for sc in chunks(STATES, 13):
            for yc in chunks(state_years, 3):
                print(f"states {subj} G{grade} [{sc[:8]}...] {yc}", flush=True)
                add(fetch({"type": "data", "subject": subj, "grade": grade,
                           "subscale": SCALE[subj], "variable": "TOTAL",
                           "jurisdiction": sc, "stattype": "MN:MN", "Year": yc}),
                    "state")
                time.sleep(0.5)
        save()

save()
print(f"DONE: wrote {len(rows)} rows to data/naep_main.csv", flush=True)
