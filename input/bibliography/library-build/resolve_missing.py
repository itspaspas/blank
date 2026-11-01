"""Resolve metadata + open-access PDF URLs for the proposal references missing from the library."""
import json
import sys
import time
import urllib.parse
import urllib.request

out = sys.argv[1]
H = {"User-Agent": "research-wiki-acquire/0.1"}
# (bibkey, grade, title for search, first-author surname)
W = [
 ("avellaneda-2008-high-frequency-trading", "A", "High-frequency trading in a limit order book", "Avellaneda"),
 ("bacry-2016-estimation-slowly-decreasing", "A", "Estimation of slowly decreasing Hawkes kernels: application to high-frequency order book dynamics", "Bacry"),
 ("bacry-2015-hawkes-processes-finance", "A", "Hawkes processes in finance", "Bacry"),
 ("cartea-2015-algorithmic-high-frequency", "A", "Algorithmic and High-Frequency Trading", "Cartea"),
 ("cheridito-2025-deep-learning-continuous", "A", "Deep learning for continuous-time stochastic control with jumps", "Cheridito"),
 ("hawkes-1971-spectra-self-exciting", "A", "Spectra of some self-exciting and mutually exciting point processes", "Hawkes"),
 ("ho-1981-optimal-dealer-pricing", "A", "Optimal dealer pricing under transactions and return uncertainty", "Ho"),
 ("lai-2023-data-driven-deep", "A", "A data-driven deep learning approach for options market making", "Lai"),
 ("ogata-1981-lewis-simulation-method", "B", "On Lewis' simulation method for point processes", "Ogata"),
 ("schulman-2017-proximal-policy-optimization", "B", "Proximal Policy Optimization Algorithms", "Schulman"),
 ("tarditi-2026-hawkes-process-models", "A", "Hawkes process models of limit order books for optimal market making", "Tarditi"),
]


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=60) as r:
        return json.load(r)


res = []
for key, grade, title, author in W:
    rec = {"bibkey": key, "grade": grade, "query": title}
    try:
        q = urllib.parse.urlencode({"search": title, "per-page": 5})
        hits = get("https://api.openalex.org/works?" + q)["results"]
        hit = next((h for h in hits
                    if any(author.lower() in (a["author"]["display_name"] or "").lower()
                           for a in h.get("authorships", []))), None)
        if hit:
            locs = [l for l in hit.get("locations", []) if l.get("pdf_url")]
            rec.update({
                "title": hit["title"], "year": hit["publication_year"],
                "doi": (hit.get("doi") or "").replace("https://doi.org/", "") or None,
                "venue": ((hit.get("primary_location") or {}).get("source") or {}).get("display_name"),
                "authors": [a["author"]["display_name"] for a in hit["authorships"]],
                "is_oa": hit.get("open_access", {}).get("is_oa"),
                "best_oa_pdf": (hit.get("best_oa_location") or {}).get("pdf_url"),
                "pdf_urls": [(l["pdf_url"], (l.get("source") or {}).get("display_name"), l.get("version"))
                             for l in locs],
            })
    except Exception as e:
        rec["error"] = str(e)
    res.append(rec)
    time.sleep(1)

json.dump(res, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
sys.stdout.reconfigure(encoding="utf-8")
for r in res:
    print(r["bibkey"], "|", r.get("year"), "|", (r.get("venue") or "-")[:35], "|", r.get("doi"),
          "| oa:", r.get("is_oa"), "|", "; ".join(f"{u} [{s}, {v}]" for u, s, v in r.get("pdf_urls", [])[:3]) or "-",
          r.get("error", ""))
