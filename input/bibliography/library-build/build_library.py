"""Copy canonical PDFs to <library>/pdf/<bibkey>.pdf and write <library>/references.bib.

Sources of truth: title pages (inventory), arXiv API, Crossref. Originals are never moved.
"""
import json
import shutil
import sys
from pathlib import Path

lib = Path(sys.argv[1])
ax = json.load(open(sys.argv[2], encoding="utf-8"))["records"]

# file stem -> (bibkey, arxiv id or None, published: (journal, year, doi, extra) or None)
M = [
 ("arXiv_1105.3115", "gueant-2013-dealing-inventory-risk", "1105.3115", ("Mathematics and Financial Economics", 2013, "10.1007/s11579-012-0087-0", "volume = {7}, number = {4}, pages = {477--507}")),
 ("Closed-form approximations in multi-asset market making__", "bergault-2021-closed-form-approximations", "1810.04383", ("Applied Mathematical Finance", 2021, "10.1080/1350486X.2021.1949359", "volume = {28}, number = {2}, pages = {101--142}")),
 ("Cartea, Jaimungal & Ricci- the 2014 paper.", "cartea-2014-buy-low-sell", None, ("SIAM Journal on Financial Mathematics", 2014, "10.1137/130911196", "volume = {5}, number = {1}, pages = {415--444}")),
 ("arXiv_2608.02002", "barzykin-2026-hawkes-driven-otc", "2608.02002", None),
 ("arXiv_2405.03496", "bergault-2024-price-aware-automated", "2405.03496", None),
 ("Optimal Market-Making with Hawkes Process A Markovian Approximation Approach via Mercer's Expansion", "martin-2026-market-making-hawkes", None, None),
 ("arXiv_2003.05958", "jusselin-2021-persistent-order-flow", "2003.05958", ("SIAM Journal on Financial Mathematics", 2021, "10.1137/20M1376054", "volume = {12}, pages = {1150--1200}")),
 ("arXiv_2610.16524", "acero-2026-hawkes-structured-networks", "2610.16524", None),
 ("Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks", "choi-2021-synchronised-order-arrivals", None, ("Journal of Economic Dynamics and Control", 2021, "10.1016/j.jedc.2021.104098", "volume = {125}, pages = {104098}")),
 ("arXiv_2510.26438", "jain-2025-impulse-control-hawkes", "2510.26438", None),
 ("arXiv_2507.11294", "khabou-2025-markov-approximation-hawkes", "2507.11294", None),
 ("arXiv_2608.19151", "bielecki-2026-continuous-time-reinforcement", "2608.19151", None),
 ("arXiv_2608.29473", "sakhanda-2026-hawkes-jump-diffusion", "2608.29473", None),
 ("arXiv_2603.07752", "barzykin-2026-dynamic-slippage-control", "2603.07752", None),
 ("arXiv_2603.10569", "barzykin-2026-win-score-promotion", "2603.10569", None),
 ("arXiv_2607.11328", "barzykin-2026-strategic-otc-reputation", "2607.11328", None),
 ("Deep reinforcement learning for market making in corporate bonds- beating the curse of dimensionality", "gueant-2019-deep-reinforcement-learning", "1910.13205", ("Applied Mathematical Finance", 2019, "10.1080/1350486X.2020.1714455", "volume = {26}, number = {5}")),
 ("arXiv_2207.09951", "gasperov-2022-deep-reinforcement-learning", "2207.09951", ("IEEE Control Systems Letters", 2022, "10.1109/LCSYS.2022.3166446", "volume = {6}, pages = {2485--2490}")),
 ("arXiv_2109.15110", "kumar-2024-deep-hawkes-process", "2109.15110", ("Journal of Banking and Financial Technology", 2024, "10.1007/s42786-024-00049-8", "volume = {8}, number = {1}")),
 ("arXiv_2609.22785", "yang-2026-robust-market-making", "2609.22785", None),
 ("arXiv_2508.16589", "wang-2024-arl-multi-action", "2508.16589", ("Proceedings of the 5th ACM International Conference on AI in Finance (ICAIF '24)", 2024, "10.1145/3677052.3698695", "")),
 ("arXiv_2510.27334", "jafree-2025-ai-trading-agents", "2510.27334", None),
 ("arXiv_2606.05882", "ochedzan-2026-market-informedness", "2606.05882", None),
 ("arXiv_2609.11614", "moret-2026-deep-learning-robust", "2609.11614", None),
 ("arXiv_1605.01862", "gueant-2017-optimal-market-making", "1605.01862", ("Applied Mathematical Finance", 2017, "10.1080/1350486X.2017.1342552", "volume = {24}, number = {2}, pages = {112--154}")),
 ("arXiv_1907.01225", "bergault-2020-size-matters-otc", "1907.01225", ("Mathematical Finance", 2020, "10.1111/mafi.12286", "")),
 ("arXiv_2106.06974", "barzykin-2022-algorithmic-market-making", "2106.06974", ("Mathematical Finance", 2022, "10.1111/mafi.12367", "")),
 ("arXiv_2112.02269", "barzykin-2021-market-making-fx", "2112.02269", None),
 ("arXiv_2207.04100", "barzykin-2022-multi-currency-inventory", "2207.04100", None),
 ("arXiv_2309.04216", "bergault-2023-liquidity-dynamics-rfq", "2309.04216", None),
 ("arXiv_2604.20406", "barzykin-2026-bond-market-making", "2604.20406", None),
 ("arXiv_2212.10164", "rosenbaum-2022-multi-asset-market", "2212.10164", None),
 ("arXiv_2202.07478", "drissi-2022-solvability-differential-riccati", "2202.07478", ("Applied Mathematical Finance", 2022, "10.1080/1350486X.2023.2241130", "volume = {29}, number = {6}, pages = {457--493}")),
 ("arXiv_2407.17393", "boyce-2025-market-making-exogenous", "2407.17393", ("SIAM Journal on Financial Mathematics", 2025, "10.1137/24M1679811", "")),
 ("arXiv_1106.5040", "guilbaud-2011-optimal-high-frequency", "1106.5040", None),
 ("arXiv_1303.7177", "fodra-2013-high-frequency-market", "1303.7177", None),
 ("arXiv_1310.1756", "fodra-2015-high-frequency-trading", "1310.1756", ("SIAM Journal on Financial Mathematics", 2015, "10.1137/140976005", "")),
 ("arXiv_1902.01157", "campi-2020-optimal-market-making", "1902.01157", ("Applied Mathematical Finance", 2020, "10.1080/1350486X.2020.1758587", "")),
 ("arXiv_2508.20225", "barzykin-2025-optimal-quoting-adverse", "2508.20225", None),
 ("arXiv_2601.13421", "barzykin-2026-market-making-transient", "2601.13421", None),
 ("arXiv_2512.04603", "barzykin-2025-fx-market-making", "2512.04603", None),
 ("arXiv_2605.30643", "niang-2026-quality-adjusted-hit", "2605.30643", None),
 ("arXiv_2501.03658", "barucci-2025-market-making-fads", "2501.03658", None),
 ("arXiv_2608.07690", "cotton-2026-simple-relationship-order", "2608.07690", None),
 ("arXiv_2307.14129", "guo-2023-macroscopic-market-making", "2307.14129", None),
 ("arXiv_2504.06717", "guo-2025-optimal-execution-macroscopic", "2504.06717", None),
 ("arXiv_2203.13053", "baldacci-2023-mean-field-game", "2203.13053", ("SIAM Journal on Financial Mathematics", 2023, "10.1137/22M1486492", "")),
 ("arXiv_2405.11444", "chavezcasillas-2024-adaptive-optimal-market", "2405.11444", ("SIAM Journal on Financial Mathematics", 2024, "10.1137/23M1571058", "")),
 ("arXiv_2101.03086", "capponi-2021-market-making-stochastic", "2101.03086", None),
 ("arXiv_2307.15599", "pulido-2026-understanding-worst-kept", "2307.15599", ("Finance and Stochastics", 2026, "10.1007/s00780-026-00585-9", "")),
 ("arXiv_1610.00261", "lehalle-2017-limit-order-strategic", "1610.00261", ("Market Microstructure and Liquidity", 2017, "10.1142/S2382626617500095", "")),
 ("arXiv_1806.05849", "gao-2020-optimal-market-making", "1806.05849", ("Quantitative Finance", 2020, "10.1080/14697688.2020.1741670", "")),
 ("arXiv_1903.07222", "law-2019-market-making-weakly", "1903.07222", ("High Frequency", 2019, "10.1002/hf2.10050", "")),
 ("arXiv_2409.02025", "cao-2026-logarithmic-regret-ergodic", "2409.02025", ("SIAM Journal on Financial Mathematics", 2026, "10.1137/24M1690497", "")),
 ("arXiv_2601.23172", "muhlekarbe-2026-unified-theory-order", "2601.23172", None),
 ("arXiv_2609.36631", "lee-2026-spread-gated-hawkes", "2609.36631", None),
 ("arXiv_2507.05749", "anantha-2025-event-time-anchor", "2507.05749", None),
 ("arXiv_2502.18625", "albers-2025-market-makers-dilemma", "2502.18625", None),
 ("arXiv_1511.07773", "fermanian-2016-behavior-dealers-clients", "1511.07773", ("Market Microstructure and Liquidity", 2016, "10.1142/S2382626617500046", "")),
 ("arXiv_1810.05884", "gueant-2018-mid-price-estimation", "1810.05884", ("Market Microstructure and Liquidity", 2018, "10.1142/S2382626619500059", "")),
 ("arXiv_2506.18147", "marinmartinez-2026-causal-interventions-bond", "2506.18147", ("PLOS One", 2026, "10.1371/journal.pone.0341369", "")),
 ("arXiv_2607.17991", "feil-2026-optimal-market-making", "2607.17991", None),
 ("arXiv_2610.18158", "wu-2026-order-flow-interventions", "2610.18158", None),
 ("arXiv_2504.00846", "ma-2025-effect-latency-optimal", "2504.00846", None),
 ("arXiv_2505.12465", "jiang-2025-resolving-latency-inventory", "2505.12465", None),
 ("arXiv_2605.21707", "asadulaev-2026-zero-shot-adaptation", "2605.21707", None),
 ("arXiv_2508.04344", "kleitsikas-2025-performative-market-making", "2508.04344", None),
]

# Works without an arXiv record: metadata from their title pages.
MANUAL = {
 "cartea-2014-buy-low-sell": ("Buy Low, Sell High: A High Frequency Trading Perspective", ["Cartea, Álvaro", "Jaimungal, Sebastian", "Ricci, Jason"], "SSRN preprint 1964781, dated 15 April 2014"),
 "martin-2026-market-making-hawkes": ("Optimal Market-Making with Hawkes Process: A Markovian Approximation Approach via Mercer's Expansion", ["Martin, Nicholas", "Tse, Alex S. L."], "preprint dated 24 March 2026 (SSRN 10.2139/ssrn.6451058)"),
 "choi-2021-synchronised-order-arrivals": ("Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks", ["Choi, So Eun", "Jang, Hyun Jin", "Lee, Kyungsub", "Zheng, Harry"], "author preprint dated 25 January 2021"),
}
# Title-page author order where arXiv metadata differs.
AUTHOR_FIX = {"campi-2020-optimal-market-making": ["Campi, Luciano", "Zabaljauregui, Diego"]}


def bibname(n):
    parts = n.split()
    return f"{parts[-1]}, {' '.join(parts[:-1])}" if len(parts) > 1 else n


assert len(M) == 67 and len({k for _, k, _, _ in M}) == 67
(lib / "pdf").mkdir(exist_ok=True)
entries = []
for stem, key, aid, pub in M:
    src = lib / f"{stem}.pdf"
    assert src.exists(), src
    dst = lib / "pdf" / f"{key}.pdf"
    if not dst.exists():
        shutil.copy2(src, dst)
    if aid:
        r = ax[aid]
        title, authors = r["title"], [bibname(a) for a in r["authors"]]
        read = f"read: arXiv {r['arxiv']}"
    else:
        title, authors, read = MANUAL[key]
    authors = AUTHOR_FIX.get(key, authors)
    f = [f"  title = {{{title}}}", f"  author = {{{' and '.join(authors)}}}"]
    if pub:
        journal, year, doi, extra = pub
        kind = "inproceedings" if "Proceedings" in journal else "article"
        f.append(f"  {'booktitle' if kind == 'inproceedings' else 'journal'} = {{{journal}}}")
        f.append(f"  year = {{{year}}}")
        f.append(f"  doi = {{{doi}}}")
        if extra:
            f.append("  " + extra)
    else:
        kind = "misc"
        f.append(f"  year = {{{key.split('-')[1]}}}")
    if aid:
        f += [f"  eprint = {{{aid}}}", "  archiveprefix = {arXiv}"]
    f.append(f"  note = {{Library copy is a preprint ({read}).}}")
    entries.append(f"@{kind}{{{key},\n" + ",\n".join(f) + "\n}\n")

text = "\n".join(entries)
for a, b in [("Tapia, Joaquin Fernandez", "Fernandez-Tapia, Joaquin"),
             ("Chahdi, Youssef Ouazzani", "Ouazzani Chahdi, Youssef"),
             ("Marín, Paloma", "Marín Martínez, Paloma")]:
    assert a in text, a
    text = text.replace(a, b)
(lib / "references.bib").write_text(text, encoding="utf-8")
print(len(entries), "entries;", len(list((lib / "pdf").glob("*.pdf"))), "PDFs in library/pdf")
