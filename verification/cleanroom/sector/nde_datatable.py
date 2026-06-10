import json, copy, urllib.request, time, sys

API = "https://www.nationsreportcard.gov/ndecore/api/"
HDRS = {"Content-Type":"application/json;charset=UTF-8",
        "Accept":"application/json, text/plain, */*",
        "X-Requested-With":"XMLHttpRequest",
        "Referer":"https://www.nationsreportcard.gov/ndecore/xplore/NDE"}

def post(path, payload, timeout=90):
    req = urllib.request.Request(API+path, data=json.dumps(payload).encode(), headers=HDRS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:400].decode(errors="replace")

def get_settings(subject_code, scale, years):
    n = {
      "survey": {"code":"NDE","label":"NAEP"},
      "subject": {"dimensionType":1,"code":subject_code,"label":"","language":0},
      "cohort": {"cohort":"8","dimensionType":15,"code":"8","label":"","language":1033},
      "framework": "",
      "years": years,
      "scales": [scale],
      "jurisdictions": [{"level":0,"sortOrder":10,"restOf":False,"dimensionType":7,"code":"NT","label":"National","language":1033}],
      "combinedJurisdictions": [],
      "variables": [{"code":"SCHTYPE","label":"","isCombined":False,"newVariables":[],"mapping":[]}],
      "crossTab": [],
      "statistics": [{"statType":"MN","label":"","statElements":[]}],
      "varexpanded": False, "sgysexpanded": [], "statexpanded": False, "jurisexpanded": False,
      "querySelectionActive": "", "categoryGroup": "", "subCategoryLevel": "",
      "showMissing": "", "include": "SE", "shareType": "NONE", "acrossYearSigTest": False,
      "selectedSigBtns": [],
    }
    code, out = post("refdata/nde/applyqueryparams", n)
    assert code == 200, (code, out)
    return out

def build_orch(s):
    iv = s["independentVariable"]
    var = {"code": iv["code"], "label": iv["label"],
           "combValueLabels": iv["combValueLabels"],
           "mapping": iv["combValueLabels"]}
    stats = [{"statType": st["code"], "label": st["label"],
              "statElements": [{"element": el["code"], "label": el["label"]} for el in st["elementsList"]]}
             for st in s["statTypes"]]
    juris = [{"code": j["code"], "label": j["label"], "level": j["level"], "restOf": j["restOf"], "isCombined": False}
             for j in s["jurisdictions"]]
    dep = s["dependentVariable"]
    orch = {
      "survey": {"code":"NDE","label":"NAEP (National Assessment of Educational Progress)"},
      "requestType": "TABULAR",
      "subject": {"code": s["subject"]["code"], "label": s["subject"]["label"]},
      "cohort": {"code": s["cohort"]["code"], "cohort": s["cohort"]["cohort"], "label": s["cohort"]["label"]},
      "years": [y["code"] for y in s["yearSamples"]],
      "selectedYears": [{"code": y["code"], "label": y["label"]} for y in s["yearSamples"]],
      "allYearSampleData": s["yearSamples"],
      "framework": s["framework"]["code"],
      "frameworkLabel": s["framework"]["label"],
      "scales": [dep],
      "dependent": dep["code"],
      "scale": "",
      "jurisdictions": juris,
      "combinedJurisdictions": [],
      "selectedJurisdictions": juris,
      "variables": [var],
      "combinedVariables": [],
      "crosstabVariables": [],
      "selectedVariables": [var],
      "statistics": stats,
      "selectedStatistics": stats,
      "reportTitle": {"label":"", "isUserAssignedName": False},
      "reportIndex": 0,
      "isReportEditMode": False,
      "isNoFiltersMode": False,
      "isCreateReportClicked": True,
      "newReports": False,
      "tableOptions": {},
      "selectedChartValue": "",
      "selectedGroupedBy": "",
      "selections": [],
      "chartType": "",
      "MapSelectorKey": "",
      "compGridIsInitialTableLoad": True,
      "focalJurisdictionCode": "NT",
      "compGridSortColumn": 1,
      "compGridSortOrder": "asc",
      "variableLabels": "SHORT",
      "showVariableNameInTitle": True,
      "showMissing": False,
      "numDecimalPlaces": "TWO",
      "yearOrder": "ASC",
      "include": "SE",
      "useParensBrackets": True,
      "surveyForGlobalOptions": "NDE",
      "forExport": False,
      "defaultOverrides": {},
      "runReportImmediately": True,
      "wantUnicode": True,
      "rowLayouts": [{"layoutType":"SAMPLE","position":1,"code":"SAMPLE"},
                     {"layoutType":"JURISDICTION","position":2,"code":"JURISDICTION"}],
      "tableLayouts": [{"position":1,"layoutType":"VARIABLE","code":"SCHTYPE"},
                       {"position":2,"layoutType":"JURISDICTION","code":""}],
      "dataTableName": "",
      "acrossYearSigTest": False,
      "shareType": "NONE",
      "selectedSigOptType": {},
      "selectedSigBtns": [],
    }
    return orch

if __name__ == "__main__":
    s = get_settings("RED", "RRPCM", ["2013R3","2019R3"])
    orch = build_orch(s)
    code, out = post("dataTable", orch)
    print(code)
    print(json.dumps(out, indent=1)[:4000] if isinstance(out,(dict,list)) else out)
