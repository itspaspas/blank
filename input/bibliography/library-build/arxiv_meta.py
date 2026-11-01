"""Fetch arXiv metadata for every arXiv_<id>.pdf in the library (plus extra ids)."""
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

lib = Path(sys.argv[1])
out = Path(sys.argv[2])
extra = ["1810.04383", "1910.13205"]  # BEGV and Guéant–Manziuk files carry these stamps

ids = sorted({re.match(r"arXiv_(.+)\.pdf$", p.name).group(1)
              for p in lib.glob("arXiv_*.pdf")} | set(extra))
ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
records = {}
for i in range(0, len(ids), 20):
    chunk = ids[i:i + 20]
    url = ("https://export.arxiv.org/api/query?max_results=50&id_list="
           + ",".join(chunk))
    with urllib.request.urlopen(url, timeout=60) as r:
        root = ET.fromstring(r.read())
    for e in root.findall("a:entry", ns):
        aid = e.find("a:id", ns).text.rsplit("/", 1)[-1]
        base = re.sub(r"v\d+$", "", aid)
        records[base] = {
            "arxiv": aid,
            "title": " ".join(e.find("a:title", ns).text.split()),
            "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)],
            "published": e.find("a:published", ns).text[:10],
            "updated": e.find("a:updated", ns).text[:10],
            "journal_ref": (e.find("x:journal_ref", ns).text
                            if e.find("x:journal_ref", ns) is not None else None),
            "doi": (e.find("x:doi", ns).text
                    if e.find("x:doi", ns) is not None else None),
        }
    time.sleep(3)

missing = [i for i in ids if i not in records]
out.write_text(json.dumps({"records": records, "missing": missing},
                          indent=1, ensure_ascii=False), encoding="utf-8")
print(len(records), "records; missing:", missing)
