#!/usr/bin/env python3
"""Clean-room pull of NAEP state P10 scores from the NCES Data Service API.

Pulls grade 8 math (priority), grade 8 reading, grade 4 math/reading,
10th percentile (stattype=PC:P1), all 50 states + DC, 2003-2019 odd years.
Chunked requests (<=4 years x <=13 jurisdictions), 40s timeout, retries.
"""
import json
import sys
import time
from pathlib import Path

import requests

OUT = Path(__file__).parent
URL = "https://www.nationsreportcard.gov/DataService/GetAdhocData.aspx"

STATES = [
    "AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN",
    "IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH",
    "NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT",
    "VT","VA","WA","WV","WI","WY",
]
YEARS = [2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019]

SUBJECTS = [
    ("mathematics", 8, "MRPCM"),
    ("reading", 8, "RRPCM"),
    ("mathematics", 4, "MRPCM"),
    ("reading", 4, "RRPCM"),
]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def fetch(params, tries=4):
    for attempt in range(tries):
        try:
            r = requests.get(URL, params=params, timeout=40)
            r.raise_for_status()
            txt = r.text.strip()
            j = json.loads(txt)
            if j.get("status") == 200:
                return j["result"]
            # status != 200 (e.g. no data) -> return empty but log
            print(f"  API status {j.get('status')}: {str(j)[:200]}", file=sys.stderr)
            return []
        except Exception as e:  # noqa: BLE001
            print(f"  attempt {attempt+1} failed: {e}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"giving up on {params}")


def pull_subject(subject, grade, subscale):
    rows = []
    for ychunk in chunks(YEARS, 4):
        for jchunk in chunks(STATES, 13):
            params = {
                "type": "data",
                "subject": subject,
                "grade": grade,
                "subscale": subscale,
                "variable": "TOTAL",
                "jurisdiction": ",".join(jchunk),
                "stattype": "PC:P1",
                "Year": ",".join(str(y) for y in ychunk),
            }
            res = fetch(params)
            print(
                f"{subject} g{grade} years={ychunk[0]}-{ychunk[-1]} "
                f"juris {jchunk[0]}..{jchunk[-1]}: {len(res)} rows"
            )
            rows.extend(res)
            time.sleep(1)
    return rows


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for subject, grade, subscale in SUBJECTS:
        tag = f"{subject[:4]}_g{grade}"
        if only and only != tag:
            continue
        out = OUT / f"raw_{tag}_p10.json"
        if out.exists():
            print(f"skip {tag}, already pulled")
            continue
        rows = pull_subject(subject, grade, subscale)
        out.write_text(json.dumps(rows, indent=1))
        print(f"wrote {out} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
