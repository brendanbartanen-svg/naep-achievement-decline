import json, time, urllib.request

BASE = "https://www.nationsreportcard.gov/DataService/GetAdhocData.aspx"
YEAR_CHUNKS = [["2003","2005","2007","2009"], ["2011","2013","2015","2017"], ["2019","2022","2024"]]
SUBJECTS = [("mathematics","MRPCM"), ("reading","RRPCM")]
GRADES = ["8","4"]
STATS = ["MN:MN","SD:SD"]

rows = []
for subj, scale in SUBJECTS:
    for grade in GRADES:
        for stat in STATS:
            for chunk in YEAR_CHUNKS:
                url = (f"{BASE}?type=data&subject={subj}&grade={grade}&subscale={scale}"
                       f"&variable=SCHTYPE&jurisdiction=NT&stattype={stat}&Year={','.join(chunk)}")
                for attempt in range(3):
                    try:
                        with urllib.request.urlopen(url, timeout=40) as r:
                            d = json.load(r)
                        if d.get("status") == 200:
                            rows.extend(d["result"])
                        else:
                            print("NON-200", subj, grade, stat, chunk, d.get("status"))
                        break
                    except Exception as e:
                        print("retry", attempt, subj, grade, stat, chunk, repr(e))
                        time.sleep(5)
                time.sleep(1)

with open("verification/cleanroom/sector/api_means_sd.json","w") as f:
    json.dump(rows, f, indent=1)
print("total rows:", len(rows))
