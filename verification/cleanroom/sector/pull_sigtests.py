import json, time, urllib.request

BASE = "https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx"

def get(url):
    for a in range(3):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return json.load(r)
        except Exception as e:
            print("retry", a, repr(e)); time.sleep(5)
    return None

out = {"sigacrossyear": [], "gaponvaracrossyear": []}
for subj, scale in [("reading","RRPCM"), ("mathematics","MRPCM")]:
    for grade in ["8","4"]:
        for years in ["2013,2019", "2019,2024", "2013,2024", "2019,2022", "2022,2024"]:
            u = (f"{BASE}?type=sigacrossyear&subject={subj}&grade={grade}&subscale={scale}"
                 f"&variable=SCHTYPE&jurisdiction=NT&stattype=MN:MN&Year={years}")
            d = get(u)
            if d and d.get("status")==200:
                out["sigacrossyear"].extend(d["result"])
            else:
                print("FAIL sig", subj, grade, years, d if not d else d.get("status"))
            time.sleep(0.5)
        for years in ["2013,2019", "2019,2024"]:
            u = (f"{BASE}?type=gaponvaracrossyear&subject={subj}&grade={grade}&subscale={scale}"
                 f"&variable=SCHTYPE&jurisdiction=NT&stattype=MN:MN&Year={years}&ComparisonValues=1,3")
            d = get(u)
            if d and d.get("status")==200:
                out["gaponvaracrossyear"].extend(d["result"])
            else:
                print("FAIL gap", subj, grade, years, d if not d else d.get("status"))
            time.sleep(0.5)

json.dump(out, open("api_sigtests.json","w"), indent=1)
print("sig rows:", len(out["sigacrossyear"]), "gap rows:", len(out["gaponvaracrossyear"]))
