#!/usr/bin/env python3
"""Clean-room cohort-matched decomposition of grade 8 NAEP changes.

Pulls national mean scale scores fresh from the NAEP Data Service API and
decomposes G8 changes into an "entry" component (what the cohort had at G4)
and a "growth" component (change in pseudo-growth G8(t) - G4(t-4)).
"""

import json
import time
import urllib.request
import urllib.parse

BASE = "https://www.nationsreportcard.gov/DataService/GetAdhocData.aspx"
YEARS = [2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2022, 2024]
SUBJECTS = {"mathematics": "MRPCM", "reading": "RRPCM"}
GRADES = [4, 8]
TIMEOUT = 40
CHUNK = 4


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def fetch(subject, subscale, grade, years, jurisdiction):
    params = {
        "type": "data",
        "subject": subject,
        "grade": grade,
        "subscale": subscale,
        "variable": "TOTAL",
        "jurisdiction": jurisdiction,
        "stattype": "MN:MN",
        "Year": ",".join(str(y) for y in years),
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "cleanroom-replication/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        payload = json.loads(r.read().decode("utf-8"))
    if payload.get("status") != 200:
        return None, payload
    return payload.get("result", []), payload


def pull_series(jurisdiction):
    """Return data[subject][grade][year] = mean, or None if jurisdiction fails."""
    data = {s: {g: {} for g in GRADES} for s in SUBJECTS}
    for subject, subscale in SUBJECTS.items():
        for grade in GRADES:
            for ychunk in chunks(YEARS, CHUNK):
                rows = None
                for attempt in range(3):
                    try:
                        rows, payload = fetch(subject, subscale, grade, ychunk, jurisdiction)
                        break
                    except Exception as e:
                        print(f"  retry {attempt+1} after error: {e}")
                        time.sleep(3)
                if rows is None:
                    # status != 200: some years in chunk may not exist; try singly
                    rows = []
                    for y in ychunk:
                        try:
                            r1, _ = fetch(subject, subscale, grade, [y], jurisdiction)
                            if r1:
                                rows.extend(r1)
                        except Exception:
                            pass
                for row in rows or []:
                    if row.get("isStatDisplayable") == 1 and row.get("errorFlag") == 0:
                        data[subject][grade][int(row["year"])] = float(row["value"])
                print(f"{jurisdiction} {subject} G{grade} years {ychunk}: "
                      f"{len(rows or [])} rows")
                time.sleep(1)
    return data


def decompose(data, subject, g8_y0, g8_y1, g4_y0, g4_y1):
    """ΔG8 = entry + growth, where
    entry  = G4(g4_y1) - G4(g4_y0)                        (cohort entry change)
    growth = [G8(y1)-G4(g4_y1)] - [G8(y0)-G4(g4_y0)]      (Δ pseudo-growth)
    """
    g4 = data[subject][4]
    g8 = data[subject][8]
    need = [(8, g8_y0), (8, g8_y1), (4, g4_y0), (4, g4_y1)]
    for g, y in need:
        if y not in data[subject][g]:
            return None
    d_g8 = g8[g8_y1] - g8[g8_y0]
    entry = g4[g4_y1] - g4[g4_y0]
    pg0 = g8[g8_y0] - g4[g4_y0]
    pg1 = g8[g8_y1] - g4[g4_y1]
    growth = pg1 - pg0
    return {
        "g8_change_years": [g8_y0, g8_y1],
        "g4_cohort_years": [g4_y0, g4_y1],
        "G8_start": round(g8[g8_y0], 2),
        "G8_end": round(g8[g8_y1], 2),
        "delta_G8_total": round(d_g8, 2),
        "entry_component_G4_change": round(entry, 2),
        "growth_component_delta_pseudo_growth": round(growth, 2),
        "pseudo_growth_start_cohort": round(pg0, 2),
        "pseudo_growth_end_cohort": round(pg1, 2),
        "identity_check_entry_plus_growth": round(entry + growth, 2),
    }


def main():
    jurisdiction_used = "NT"
    data = pull_series("NT")
    n = sum(len(data[s][g]) for s in SUBJECTS for g in GRADES)
    if n == 0:
        print("NT returned nothing; falling back to NP")
        jurisdiction_used = "NP"
        data = pull_series("NP")

    results = {
        "meta": {
            "source": BASE,
            "stattype": "MN:MN",
            "variable": "TOTAL",
            "jurisdiction_used": jurisdiction_used,
            "jurisdiction_note": (
                "Tried NT first per spec; NT returned data (label 'National'). "
                "NP (national public) not needed as fallback."
            ),
            "subscales": SUBJECTS,
            "years_requested": YEARS,
            "pulled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "levels_panel_2009_2024": {},
        "decompositions": {},
        "alignment_decisions": {},
    }

    # Sanity panel 2009-2024
    for subject in SUBJECTS:
        results["levels_panel_2009_2024"][subject] = {
            "G4": {str(y): round(v, 2) for y, v in sorted(data[subject][4].items()) if y >= 2009},
            "G8": {str(y): round(v, 2) for y, v in sorted(data[subject][8].items()) if y >= 2009},
        }

    # Decomposition 1: G8 2013 -> 2019; cohorts were G4 in 2009 and 2015 (exact t-4)
    for subject in SUBJECTS:
        results["decompositions"].setdefault(subject, {})
        results["decompositions"][subject]["2013_to_2019"] = decompose(
            data, subject, 2013, 2019, 2009, 2015)

    results["alignment_decisions"]["2013_to_2019"] = (
        "Exact alignment: G8 2013 cohort = G4 2009; G8 2019 cohort = G4 2015. "
        "Both are NAEP years; no approximation needed."
    )

    # Decomposition 2: G8 2019 -> 2024. G8 2024 cohort was G4 in 2020 (not a
    # NAEP year). Nearest available G4 year is 2019 (1 year early; 2022 is 2
    # years late and post-pandemic). Use G4 2019 as the entry proxy.
    for subject in SUBJECTS:
        results["decompositions"][subject]["2019_to_2024"] = decompose(
            data, subject, 2019, 2024, 2015, 2019)

    results["alignment_decisions"]["2019_to_2024"] = (
        "Imperfect alignment: G8 2024 cohort was G4 in 2020, not a NAEP year. "
        "Nearest available assessment is G4 2019 (1 year before the true entry "
        "year; G4 2022 is 2 years after and contaminated by pandemic G4 losses). "
        "Used G4 2019, so the end-cohort pseudo-growth spans 5 calendar years "
        "(2019 G4 -> 2024 G8) vs 4 for the base cohort (2015 G4 -> 2019 G8); "
        "the growth component therefore mixes true G4-8 growth change with the "
        "1-year alignment slippage and any 2019-2020 pre-pandemic G4 drift."
    )

    out = (""
           "verification/cleanroom/cohort/results.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
