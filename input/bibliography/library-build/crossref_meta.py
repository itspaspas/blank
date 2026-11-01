"""Look up published versions on Crossref by title; keep only near-exact title matches."""
import difflib
import json
import re
import sys
import time
import urllib.parse
import urllib.request

src = json.load(open(sys.argv[1], encoding="utf-8"))["records"]
out = sys.argv[2]
titles = {k: (r["title"], r["authors"][0].split()[-1]) for k, r in src.items()}
titles.update({  # library files without an arXiv stamp
    "cjr": ("Buy Low Sell High: a High Frequency Trading Perspective", "Cartea"),
    "choi": ("Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks", "Choi"),
    "martin": ("Optimal Market-Making with Hawkes Process: A Markovian Approximation Approach via Mercer's Expansion", "Martin"),
})


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower())


res = {}
for k, (title, author) in titles.items():
    q = urllib.parse.urlencode({"query.bibliographic": title, "query.author": author, "rows": 5,
                                "select": "DOI,title,container-title,issued,author,type"})
    req = urllib.request.Request("https://api.crossref.org/works?" + q,
                                 headers={"User-Agent": "research-wiki-metadata-check/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            items = json.load(r)["message"]["items"]
    except Exception as e:  # keep going; record the failure
        res[k] = {"error": str(e)}
        continue
    best = None
    for it in items:
        t = (it.get("title") or [""])[0]
        score = difflib.SequenceMatcher(None, norm(t), norm(title)).ratio()
        if score >= 0.9 and (best is None or score > best["score"]):
            best = {"score": round(score, 3), "doi": it["DOI"], "type": it.get("type"),
                    "container": (it.get("container-title") or [""])[0],
                    "year": it["issued"]["date-parts"][0][0],
                    "authors": [a.get("family", "") for a in it.get("author", [])]}
    res[k] = best
    time.sleep(1)

json.dump(res, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.stdout.reconfigure(encoding="utf-8")
for k, v in sorted(res.items()):
    if v:
        print(k, "|", v.get("year"), "|", v.get("container", "")[:50], "|", v.get("doi"), "|",
              ", ".join(v.get("authors", [])[:3]), "|", v.get("type"), v.get("error", ""))
