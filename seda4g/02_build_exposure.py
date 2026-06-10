#!/usr/bin/env python3
"""
02_build_exposure.py — build the county x wave high-speed-mobile exposure panel
from the NTIA SBDD / National Broadband Map archive.

Two construction paths:
  A. NBM "Analyze Table" county summaries (7 waves: Jun-2011 ... Jun-2014).
     Pre-built by NTIA from the full wireless polygon overlays, so they do NOT
     suffer the <2-sq-mi CSV block restriction (which applies to wireline CSVs
     only). Key columns:
       terrmobilewless        — % pop with any terrestrial mobile wireless
       wireless_advdl_gr10000k — % pop with >=10 Mbps adv. down via ANY wireless
                                 (mobile + fixed wireless: upper bound on 4G)
       wireless_advdl_gr6000k  — same at >=6 Mbps (tier >=6 robustness)
  B. Block-level build from per-state Wireless CSVs for 8 pilot states
     (DE CO MS OH WA TX MA MT), waves Jun-2010, Dec-2010 (no analyze tables
     exist for these) and Jun-2014 (cross-validation + fixed-wireless-leakage
     quantification). Measure: county pop share in blocks with >=1 provider
     transtech==80 & maxaddown>=7 (>=10 Mbps advertised down). Also computes
     Verizon-only (near-pure LTE) and any-mobile variants.
     Pop weights: Census 2000 PL94-171 block pops for the 2010 waves (SBDD used
     2000-vintage blocks through mid-2011), Census 2010 PL94-171 for Jun-2014.

Outputs (in seda4g/):
  exposure_county_panel.csv   — tidy panel, one row per county x wave x source
  build/ intermediates in data/external/seda4g/build/
"""
import glob
import io
import os
import re
import sys
import zipfile

import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "external", "seda4g")
BUILD = os.path.join(DATA, "build")
OUT = os.path.join(ROOT, "seda4g")
os.makedirs(BUILD, exist_ok=True)

PILOT = ["DE", "CO", "MS", "OH", "WA", "TX", "MA", "MT"]
ST_FIPS = {"DE": "10", "CO": "08", "MS": "28", "OH": "39",
           "WA": "53", "TX": "48", "MA": "25", "MT": "30"}

# ----------------------------------------------------------------------------
# 1. Census block populations
# ----------------------------------------------------------------------------

def blockpop_2010(st):
    """2010 PL94-171 geo file: SUMLEV 750 rows carry POP100. Fixed-width."""
    cache = os.path.join(BUILD, f"blockpop2010_{st.lower()}.csv.gz")
    if os.path.exists(cache):
        d = pd.read_csv(cache, dtype={"block": str})
        return dict(zip(d["block"], d["pop"]))
    zf = zipfile.ZipFile(os.path.join(DATA, "census", f"{st.lower()}2010.pl.zip"))
    geoname = [n for n in zf.namelist() if "geo2010" in n][0]
    out = {}
    with zf.open(geoname) as f:
        for raw in io.TextIOWrapper(f, encoding="latin-1"):
            if raw[8:11] != "750":
                continue
            block = raw[27:32] + raw[54:60] + raw[61:65]  # state+county+tract+block
            out[block] = int(raw[318:327])
    pd.DataFrame({"block": list(out), "pop": list(out.values())}).to_csv(
        cache, index=False)
    return out


def blockpop_2000(st):
    """2000 PL94-171: geo file (fixed width) gives LOGRECNO->block GEOID at
    SUMLEV 750; part-1 file (comma) gives P0010001 (5th and 6th fields)."""
    cache = os.path.join(BUILD, f"blockpop2000_{st.lower()}.csv.gz")
    if os.path.exists(cache):
        d = pd.read_csv(cache, dtype={"block": str})
        return dict(zip(d["block"], d["pop"]))
    geo_zf = zipfile.ZipFile(os.path.join(DATA, "census", f"{st.lower()}geo.upl.zip"))
    p1_zf = zipfile.ZipFile(os.path.join(DATA, "census", f"{st.lower()}00001.upl.zip"))
    logrec2block = {}
    with geo_zf.open(geo_zf.namelist()[0]) as f:
        for raw in io.TextIOWrapper(f, encoding="latin-1"):
            if raw[8:11] != "750":
                continue
            logrec = raw[18:25]
            block = raw[29:34] + raw[55:61] + raw[62:66]
            logrec2block[logrec] = block
    out = {}
    with p1_zf.open(p1_zf.namelist()[0]) as f:
        for raw in io.TextIOWrapper(f, encoding="latin-1"):
            parts = raw.split(",")
            logrec = parts[4].zfill(7)
            if logrec in logrec2block:
                out[logrec2block[logrec]] = int(parts[5])
    pd.DataFrame({"block": list(out), "pop": list(out.values())}).to_csv(
        cache, index=False)
    return out

# ----------------------------------------------------------------------------
# 2. SBDD wireless CSV -> county coverage  (one state x wave)
# ----------------------------------------------------------------------------

WAVE_FILES = {
    # wave: (outer zip pattern, inner wireless zip regex, vintage)
    "2010-06": ("states/SBDD_{st}_Fall2010.zip", r"Wireless.*fall2010", 2000),
    "2010-12": ("states/{st}-NBM-CSV-December-2010.zip",
                r"Wireless-CSV-December-2010", 2000),
    # Dec-2012 downloaded for MT MS CO MA only — quantifies fixed-wireless
    # leakage in the analyze-table >=10Mbps any-wireless column at mid-rollout
    "2012-12": ("states/{st}-NBM-CSV-Dec-2012.zip",
                r"WIRELESS-CSV-Dec-2012", 2010),
    "2014-06": ("states/{st}-NBM-CSV-June-2014.zip",
                r"Wireless-CSV-JUN-2014", 2010),
}


def _extract_member(zf, info, dest):
    """Extract a zip member to path `dest`, with a manual Deflate64
    (compress_type 9) fallback — several SBDD zips (e.g. TX Jun-2014) use
    Deflate64, unsupported by the stdlib (and by macOS unzip/bsdtar)."""
    if info.compress_type != 9:
        with zf.open(info) as src, open(dest, "wb") as out:
            while True:
                chunk = src.read(1 << 24)
                if not chunk:
                    break
                out.write(chunk)
        return
    import inflate64
    fp = zf.fp
    fp.seek(info.header_offset)
    hdr = fp.read(30)
    n_name = int.from_bytes(hdr[26:28], "little")
    n_extra = int.from_bytes(hdr[28:30], "little")
    fp.seek(info.header_offset + 30 + n_name + n_extra)
    inflater = inflate64.Inflater()
    remaining = info.compress_size
    with open(dest, "wb") as out:
        while remaining > 0:
            chunk = fp.read(min(1 << 24, remaining))
            remaining -= len(chunk)
            out.write(inflater.inflate(chunk))


def read_wireless(st, wave):
    """Stream one state x wave Wireless CSV; return
    (dict measure -> Series(block -> max pct_blk_in_shape), n_rows,
     set of all block ids seen)."""
    outer_pat, inner_re, _ = WAVE_FILES[wave]
    outer = zipfile.ZipFile(os.path.join(DATA, outer_pat.format(st=st)))
    inner_names = [n for n in outer.namelist()
                   if re.search(inner_re, n, re.I) and n.lower().endswith(".zip")]
    if not inner_names:
        raise FileNotFoundError(f"no wireless zip for {st} {wave}")
    tmp_inner = os.path.join(BUILD, "_tmp_inner.zip")
    tmp_csv = os.path.join(BUILD, "_tmp_wireless.csv")
    _extract_member(outer, outer.getinfo(inner_names[0]), tmp_inner)
    inner = zipfile.ZipFile(tmp_inner)
    dataname = [n for n in inner.namelist()
                if n.lower().endswith((".csv", ".txt"))][0]
    _extract_member(inner, inner.getinfo(dataname), tmp_csv)
    inner.close()

    with open(tmp_csv, encoding="latin-1") as f:
        head = f.readline()
    sep = "|" if head.count("|") > head.count(",") else ","
    hdr = [c.strip().lower().strip('"') for c in head.strip().split(sep)]
    blockcol = "fullfipsid" if "fullfipsid" in hdr else "censusblock_fips"
    namecols = [c for c in ("provname", "dbaname", "hoconame") if c in hdr]
    use = [blockcol, "pct_blk_in_shape", "transtech", "maxaddown"] + namecols

    partials = {m: [] for m in MEASURES}
    allblocks = set()
    n_rows = 0
    for ch in pd.read_csv(tmp_csv, sep=sep, dtype=str, encoding="latin-1",
                          on_bad_lines="skip", header=0, names=hdr,
                          usecols=use, chunksize=2_000_000):
        n_rows += len(ch)
        ch = ch.rename(columns={blockcol: "block"})
        ch["block"] = ch["block"].str.replace('"', "").str.strip()
        ch = ch[ch["block"].str.len() == 15]
        ch["transtech"] = pd.to_numeric(ch["transtech"], errors="coerce")
        ch["maxaddown"] = pd.to_numeric(ch["maxaddown"], errors="coerce")
        ch["pct"] = pd.to_numeric(ch["pct_blk_in_shape"],
                                  errors="coerce").fillna(0.0)
        prov = ch[namecols[0]].fillna("") if namecols else ""
        for c in namecols[1:]:
            prov = prov + "|" + ch[c].fillna("")
        ch["provider"] = prov
        allblocks.update(ch["block"].unique())
        for m, mask in MEASURES.items():
            sub = ch[mask(ch)]
            if len(sub):
                partials[m].append(sub.groupby("block")["pct"].max())
    os.remove(tmp_inner)
    os.remove(tmp_csv)
    out = {}
    # Jun-2014 files store percent (0-100); 2010 files store fraction (0-1).
    # Decide once per file from the largest pct seen in ANY measure.
    gmax = max((p.max() for parts in partials.values() for p in parts
                if len(p)), default=0.0)
    for m, parts in partials.items():
        if parts:
            s = pd.concat(parts).groupby(level=0).max()
        else:
            s = pd.Series(dtype=float)
        if gmax > 1.5 and len(s):
            s = s / 100.0
        out[m] = s.clip(0, 1)
    return out, n_rows, allblocks


VZW = re.compile(r"verizon|cellco", re.I)


def county_coverage(block_pct, pops):
    """block_pct: dict measure -> Series(block -> max pct_blk_in_shape).
    Returns DataFrame county x measure with pop-weighted coverage shares,
    using max pct_blk_in_shape per block ('wt') and any-overlap ('any')."""
    blocks = pd.DataFrame({"block": list(pops), "pop": list(pops.values())})
    blocks["county"] = blocks["block"].str[:5]
    cty = blocks.groupby("county")["pop"].sum().rename("county_pop")
    res = pd.DataFrame(index=cty.index)
    res["county_pop"] = cty
    for name, bm in block_pct.items():
        m = blocks.merge(bm.rename("pct"), left_on="block",
                         right_index=True, how="left")
        m["pct"] = m["pct"].fillna(0.0)
        res[name + "_wt"] = (m["pop"] * m["pct"]).groupby(m["county"]).sum() / cty
        res[name + "_any"] = (m["pop"] * (m["pct"] > 0)).groupby(m["county"]).sum() / cty
    return res.reset_index()


MEASURES = {
    "mobile_any":   lambda d: d["transtech"] == 80,
    "mobile_t6":    lambda d: (d["transtech"] == 80) & (d["maxaddown"] >= 6),
    "mobile_t7":    lambda d: (d["transtech"] == 80) & (d["maxaddown"] >= 7),
    "mobile_t7_vzw": lambda d: ((d["transtech"] == 80) & (d["maxaddown"] >= 7)
                                & d["provider"].str.contains(VZW)),
    "anywless_t7":  lambda d: d["maxaddown"] >= 7,   # incl. fixed wireless
}


def build_block_panel():
    rows = []
    blockstats = []
    for wave, (_, _, vintage) in WAVE_FILES.items():
        for st in PILOT:
            ccache = os.path.join(BUILD, f"cov_{st}_{wave}.csv")
            dcache = os.path.join(BUILD, f"diag_{st}_{wave}.csv")
            if os.path.exists(ccache) and os.path.exists(dcache):
                rows.append(pd.read_csv(ccache, dtype={"county": str}))
                blockstats.append(pd.read_csv(dcache).iloc[0].to_dict())
                continue
            print(f"  block build {st} {wave}", flush=True)
            pops = blockpop_2000(st) if vintage == 2000 else blockpop_2010(st)
            try:
                block_pct, n_rows, allblocks = read_wireless(st, wave)
            except FileNotFoundError as e:
                print("   MISSING:", e)
                continue
            cov = county_coverage(block_pct, pops)
            cov.insert(0, "wave", wave)
            cov.insert(1, "state", st)
            cov.to_csv(ccache, index=False)
            rows.append(cov)
            # large-block / completeness diagnostics
            tot = sum(pops.values())
            pop_incsv = sum(p for b, p in pops.items() if b in allblocks)
            n_unmatched = len(allblocks - set(pops))
            d = dict(
                wave=wave, state=st, vintage=vintage,
                state_pop=tot, n_blocks_census=len(pops),
                n_blocks_in_csv=len(allblocks),
                pop_share_in_csv=pop_incsv / tot,
                csv_blocks_not_in_census=n_unmatched,
                csv_rows=n_rows)
            pd.DataFrame([d]).to_csv(dcache, index=False)
            blockstats.append(d)
    panel = pd.concat(rows, ignore_index=True)
    panel.to_csv(os.path.join(BUILD, "block_panel_pilot.csv"), index=False)
    pd.DataFrame(blockstats).to_csv(
        os.path.join(BUILD, "block_diagnostics.csv"), index=False)
    return panel


# ----------------------------------------------------------------------------
# 3. Analyze tables -> county / state / national panel (7 waves)
# ----------------------------------------------------------------------------

ANALYZE = {
    "2011-06": "june2011_analyze_table.csv",
    "2011-12": "All-NBM-Analyze-Table-December-2011/Dec2011_analyze_table.xls",
    "2012-06": "All-NBM-Analyze-Table-June-2012/Jun2012_analyze_master.xls",
    "2012-12": "All-NBM-Analyze-Table-December-2012/Dec2012_analyze_master.xlsx",
    "2013-06": "All-NBM-Analyze-Table-June-2013/Analyze_Table_Jun2013.xlsx",
    "2013-12": "All-NBM-Analyze-Table-December-2013/Analyze_Table_Dec2013.xlsx",
    "2014-06": "All-NBM-Analyze-Table-June-2014/Analyze_Table_Jun2014.xlsx",
}

KEEP = ["geography_type", "geography_id", "geography_desc", "state_fips",
        "metric_type", "land_area", "population", "terrmobilewless",
        "anywless_nosat", "wireless_advdl_gr3000k", "wireless_advdl_gr6000k",
        "wireless_advdl_gr10000k", "wireless_advdl_gr25000k",
        "terrmobilewless_error"]


def read_analyze(path):
    p = os.path.join(DATA, path)
    if p.endswith(".csv"):
        df = pd.read_csv(p, dtype={"geography_id": str}, low_memory=False)
    elif p.endswith(".xls"):
        df = pd.read_excel(p, sheet_name=0, dtype={"geography_id": str})
    else:
        import openpyxl
        wb = openpyxl.load_workbook(p, read_only=True)
        sheet = [s for s in wb.sheetnames if "POP" in s.upper()][0]
        ws = wb[sheet]
        it = ws.iter_rows(values_only=True)
        hdr = [str(h) for h in next(it)]
        df = pd.DataFrame(it, columns=hdr)
        df["geography_id"] = df["geography_id"].astype(str)
    df.columns = [c.strip().lower() for c in df.columns]
    cols = [c for c in KEEP if c in df.columns]
    df = df[cols]
    if "metric_type" in df.columns:
        df = df[df["metric_type"].astype(str).str.upper().str.startswith("POP")]
    return df


def build_analyze_panel():
    cache = os.path.join(BUILD, "analyze_allgeo.csv.gz")
    if os.path.exists(cache):
        return pd.read_csv(cache, dtype={"geography_id": str}, low_memory=False)
    frames = []
    for wave, path in ANALYZE.items():
        print(f"  analyze table {wave}", flush=True)
        df = read_analyze(path)
        df.insert(0, "wave", wave)
        frames.append(df)
    allgeo = pd.concat(frames, ignore_index=True)
    for c in allgeo.columns:
        if c.startswith(("terr", "anyw", "wireless", "land", "popul")):
            allgeo[c] = pd.to_numeric(allgeo[c], errors="coerce")
    allgeo.to_csv(os.path.join(BUILD, "analyze_allgeo.csv.gz"), index=False)
    return allgeo


# ----------------------------------------------------------------------------

def main():
    print("== analyze tables ==")
    allgeo = build_analyze_panel()
    cty = allgeo[allgeo["geography_type"] == "COUNTY"].copy()
    cty["county_fips"] = cty["geography_id"].str.replace(r"\.0$", "", regex=True).str.zfill(5)

    print("== block-level pilot build ==")
    panel = build_block_panel()

    # tidy combined output
    a = cty[["wave", "county_fips", "population", "terrmobilewless",
             "wireless_advdl_gr6000k", "wireless_advdl_gr10000k",
             "wireless_advdl_gr25000k"]].copy()
    a["source"] = "analyze_table"
    a = a.rename(columns={
        "population": "county_pop",
        "terrmobilewless": "share_mobile_any",
        "wireless_advdl_gr6000k": "share_anywless_t6",
        "wireless_advdl_gr10000k": "share_anywless_t7",
        "wireless_advdl_gr25000k": "share_anywless_t8"})

    b = panel.rename(columns={
        "county": "county_fips",
        "mobile_any_wt": "share_mobile_any",
        "mobile_t6_wt": "share_mobile_t6",
        "mobile_t7_wt": "share_mobile_t7",
        "mobile_t7_vzw_wt": "share_mobile_t7_vzw",
        "anywless_t7_wt": "share_anywless_t7"})
    b["source"] = "block_csv"
    bcols = ["wave", "county_fips", "county_pop", "source", "share_mobile_any",
             "share_mobile_t6", "share_mobile_t7", "share_mobile_t7_vzw",
             "share_anywless_t7", "mobile_t7_any", "mobile_any_any"]
    out = pd.concat([a, b[[c for c in bcols if c in b.columns]]],
                    ignore_index=True, sort=False)
    out = out.sort_values(["source", "wave", "county_fips"])
    out.to_csv(os.path.join(OUT, "exposure_county_panel.csv"), index=False)
    print("wrote", os.path.join(OUT, "exposure_county_panel.csv"), len(out), "rows")


if __name__ == "__main__":
    main()
