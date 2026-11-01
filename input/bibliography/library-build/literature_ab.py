"""Verify metadata of the A+B candidates from the Task-6 literature search and emit BibTeX.

Run: python -I literature_ab.py <out.json> <out.bib>
Crossref by DOI (3 s apart); arXiv for arXiv-only items. Bibkey = surname-year-shorttitle (library rule).
"""
import json
import re
import sys
import time
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET

# (grade, doi or None, arxiv or None, short title for the key)
C = [
 ("A", "10.2139/ssrn.2584430", "1503.07007", "optimal-position-management"),
 ("A", "10.1137/20M1320560", "2110.09417", "mean-variance-portfolio"),
 ("A", "10.1287/opre.2024.1172", None, "dynamic-pricing-self"),
 ("A", "10.1093/jjfinec/nbv024", "1210.1598", "portfolio-choice-markets"),
 ("A", None, "1802.07244", "steering-social-activity"),
 ("A", "10.2139/ssrn.7625720", None, "dynamic-market-making"),
 ("A", "10.1137/18M1176968", None, "algorithmic-trading-stochastic"),
 ("B", "10.1007/s00780-015-0282-y", "1404.0648", "dynamic-optimal-execution"),
 ("B", "10.1142/S2382626616500052", "1506.08740", "extension-calibration-hawkes"),
 ("B", "10.1287/opre.2023.0151", None, "optimal-trade-execution"),
 ("B", "10.1111/mafi.12359", "2011.05589", "portfolio-liquidation-games"),
 ("B", "10.1137/090771272", None, "affine-point-processes"),
 ("B", "10.1111/1468-0262.00164", None, "transform-analysis-asset"),
 ("B", "10.1080/14697688.2025.2488450", "2404.11482", "optimal-reinsurance-dynamic"),
 ("B", "10.1111/mafi.12177", None, "credit-portfolio-selection"),
 ("B", "10.1111/mafi.12074", None, "optimal-investment-credit"),
 ("B", "10.1214/20-AAP1645", "1911.01900", "linear-quadratic-control"),
 ("B", "10.1137/19M1298287", "1911.01903", "integral-operator-riccati"),
 ("B", "10.1111/mafi.12465", "2211.00447", "optimal-liquidation-signals"),
 ("B", "10.1287/mnsc.2018.3070", None, "dynamic-credit-collections"),
 ("B", "10.3934/mcrf.2024038", None, "stochastic-control-diffusions"),
 ("B", "10.1137/18M1209684", "1808.08336", "backward-stochastic-riccati"),
 ("B", "10.1016/j.jedc.2013.10.005", None, "partial-information-contagion"),
 ("B", "10.4310/CIS.2002.v2.n3.a4", None, "indefinite-stochastic-lq"),
 ("B", "10.2139/ssrn.6777719", None, "structural-hawkes-ambiguity"),
 ("B", "10.2139/ssrn.6847019", None, "liquidation-aware-market"),
 ("B", None, "2606.19772", "signature-methods-optimal"),
 ("B", None, "2509.12456", "reinforcement-learning-based"),
 ("B", "10.2139/ssrn.4729290", None, "optimal-option-market"),
]

H = {"User-Agent": "research-wiki-literature-check/0.1"}


def ascii_surname(s):
    s = s.replace("ß", "ss").replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z]", "", s.lower())


def crossref(doi):
    with urllib.request.urlopen(urllib.request.Request(
            "https://api.crossref.org/works/" + urllib.request.quote(doi), headers=H), timeout=60) as r:
        m = json.load(r)["message"]
    return {"title": " ".join((m.get("title") or [""])[0].split()),
            "authors": [(a.get("family", ""), a.get("given", "")) for a in m.get("author", [])],
            "year": m["issued"]["date-parts"][0][0], "venue": (m.get("container-title") or [""])[0],
            "type": m.get("type"), "volume": m.get("volume"), "issue": m.get("issue"), "pages": m.get("page"),
            "publisher": m.get("publisher")}


def arxiv(aid):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    r = urllib.request.urlopen("https://export.arxiv.org/api/query?id_list=" + aid, timeout=60).read()
    e = ET.fromstring(r).find("a:entry", ns)
    names = [a.find("a:name", ns).text for a in e.findall("a:author", ns)]
    return {"title": " ".join(e.find("a:title", ns).text.split()),
            "authors": [(n.split()[-1], " ".join(n.split()[:-1])) for n in names],
            "year": int(e.find("a:published", ns).text[:4]), "venue": "arXiv preprint", "type": "preprint"}


out, entries = [], []
for grade, doi, aid, short in C:
    rec = {"grade": grade, "doi": doi, "arxiv": aid}
    try:
        rec.update(crossref(doi) if doi else arxiv(aid))
    except Exception as e:  # noqa: BLE001 — record and continue
        rec["error"] = str(e)
        out.append(rec); time.sleep(3); continue
    key = f"{ascii_surname(rec['authors'][0][0])}-{rec['year']}-{short}"
    rec["bibkey"] = key
    out.append(rec)
    au = " and ".join(f"{f}, {g}".strip(", ") for f, g in rec["authors"])
    kind = ("article" if rec["type"] == "journal-article" else
            "inproceedings" if rec["type"] == "proceedings-article" else "misc")
    f = [f"  title = {{{rec['title']}}}", f"  author = {{{au}}}", f"  year = {{{rec['year']}}}"]
    if kind == "article":
        f.append(f"  journal = {{{rec['venue']}}}")
        for k in ("volume", "number", "pages"):
            v = rec.get("issue" if k == "number" else k)
            if v:
                f.append(f"  {k} = {{{v.replace('-', '--') if k == 'pages' else v}}}")
    elif rec.get("venue"):
        f.append(f"  howpublished = {{{rec['venue']}}}")
    if doi:
        f.append(f"  doi = {{{doi}}}")
    if aid:
        f += [f"  eprint = {{{aid}}}", "  archiveprefix = {arXiv}"]
    f.append(f"  note = {{Literature search 2026-10-25 (plan Task 6), grade {grade}; not yet acquired.}}")
    entries.append(f"@{kind}{{{key},\n" + ",\n".join(f) + "\n}\n")
    time.sleep(3)

json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
open(sys.argv[2], "w", encoding="utf-8").write("\n".join(entries))
sys.stdout.reconfigure(encoding="utf-8")
for r in out:
    print(r["grade"], r.get("bibkey", "ERROR " + r.get("error", "")), "|", r.get("year"), "|",
          (r.get("venue") or "")[:40], "|", (r.get("title") or "")[:70])
