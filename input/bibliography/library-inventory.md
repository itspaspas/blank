---
title: "Library inventory — ./library"
type: inventory
created: 2026-10-25
updated: 2026-10-25
plan: "[[hawkes-multi-asset-mm-plan]]"
---

# Library inventory (Plan Task 1)

**Method:** every PDF in `./library/` identified from its title page, then verified against the
arXiv API and Crossref (title match ≥ 0.9). Reproducible from `input/bibliography/library-build/`
(`arxiv_meta.py` → `crossref_meta.py` → `build_library.py`; raw results in `*_meta.json`).

**Status (Task 2, 2026-10-25): verified.** The canonical copies are at `library/pdf/<bibkey>.pdf`
(67 files; the originals are untouched), and the master bibliography is `library/references.bib`
(67 entries, each noting the preprint version on disk). The full-text index is built
(`scripts/bib-search.py`, 2,022 pages).

**Bibkey rule applied:** the year is the journal year where Crossref found a published version,
otherwise the arXiv first-version year. **The final keys are those in `library/references.bib`.**
The tables below show provisional keys; these differ from the final ones:

| Provisional | Final | Reason |
|---|---|---|
| jusselin-2020-persistent-order-flow | jusselin-2021-persistent-order-flow | SIFIN 12 (2021) |
| kumar-2021-deep-hawkes-process | kumar-2024-deep-hawkes-process | J. Banking & Financial Technology 8(1) (2024) |
| bergault-2019-size-matters-otc | bergault-2020-size-matters-otc | Mathematical Finance (2020) |
| barzykin-2021-algorithmic-market-making | barzykin-2022-algorithmic-market-making | Mathematical Finance (2022) |
| boyce-2024-market-making-exogenous | boyce-2025-market-making-exogenous | SIFIN (2025) |
| fodra-2013-high-frequency-trading | fodra-2015-high-frequency-trading | SIFIN (2015) |
| campi-2019-optimal-market-making | campi-2020-optimal-market-making | Applied Mathematical Finance (2020); title-page author order kept (arXiv lists Zabaljauregui first) |
| baldacci-2022-mean-field-game | baldacci-2023-mean-field-game | SIFIN (2023) |
| pulido-2023-understanding-worst-kept | pulido-2026-understanding-worst-kept | Finance and Stochastics (2026) |
| lehalle-2016-limit-order-strategic | lehalle-2017-limit-order-strategic | Market Microstructure and Liquidity (2017) |
| gao-2018-optimal-market-making | gao-2020-optimal-market-making | Quantitative Finance (2020) |
| cao-2024-logarithmic-regret-ergodic | cao-2026-logarithmic-regret-ergodic | SIFIN (2026) |
| fermanian-2015-behavior-dealers-clients | fermanian-2016-behavior-dealers-clients | Market Microstructure and Liquidity (2016) |
| marin-2025-causal-interventions-bond | marinmartinez-2026-causal-interventions-bond | PLOS One (2026); surname "Marín Martínez" |
| ananthan-2025-event-time-anchor | anantha-2025-event-time-anchor | arXiv surname "Anantha". **Open:** the title page reads "Aditya Nittur Anantha", so it is unclear whether "Nittur" belongs to the surname |

GLFT is kept at **2013**: the print volume 7(4) is 2013, Crossref "issued" says 2012 (online first).
Possible later version, not yet confirmed: Guo, Jin & Nam's "Macroscopic Market Making" may be
published as "Macroscopic Market Making Games" (*Mathematical Finance* 2025, DOI 10.1111/mafi.70010).
The titles differ, so check before treating it as the same work.

**Counts:** 71 files → 4 exact duplicate pairs → **67 unique works**.

## Duplicates (resolve: keep the arXiv-ID file, which carries the version stamp)

| Kept file | Duplicate file | Work | Evidence |
|---|---|---|---|
| `arXiv_1105.3115.pdf` | `Dealing with the Inventory Risk.pdf` | GLFT | both 1105.3115v5, 827.7 KB |
| `arXiv_2610.16524.pdf` | `Reinforcement Learning with Hawkes-Structured Networks for Market Making.pdf` | Acero et al. | both 2610.16524v1, 690.1 KB |
| `arXiv_2608.02002.pdf` | `Hawkes-Driven OTC Market Making Volterra-Riccati Approximation.pdf` | Barzykin | both 2608.02002v2, 522.5 KB |
| `arXiv_2003.05958.pdf` | `Optimal Market Making with Persistent Order Flow.pdf` | Jusselin | both 2003.05958v2, 938.8 KB |

## Related versions (not duplicates)

- `arXiv_2101.03086` (Capponi, Figueroa-López, Yu 2021) is superseded by `arXiv_2405.11444` (Chávez-Casillas, Figueroa-López, Yu, Zhang 2024). The 2024 paper states the 2021 preprint "will remain an unpublished manuscript". Ingest both; the 2021 one only at `map` depth.
- `arXiv_1810.04383v5` = the BEGV file `Closed-form approximations in multi-asset market making__.pdf`. The earlier guess that `arXiv_2106.06974` duplicates it was **wrong**: 2106.06974 is Barzykin–Bergault–Guéant on hedging.

## Version notes (preprint vs. published)

All 67 works on disk are **preprints** (arXiv, or SSRN for CJR). Where a published version
exists, the ingest records "read: preprint vX". No substitution without consent (ingest hard-stop rule).

| Work | On disk | Published version (to verify) |
|---|---|---|
| GLFT | arXiv 1105.3115v5 ("This draft: July 2012") | *Mathematics and Financial Economics* 2013 |
| BEGV | arXiv 1810.04383v5 (Sep 2022) | *Applied Mathematical Finance* 28(2), 101–142 (2021), verified |
| Cartea–Jaimungal–Ricci | SSRN 1964781, dated 15 Apr 2014, "Forthcoming in SIFIN" | *SIAM J. Financial Mathematics* 2014 |
| Gašperov–Kostanjčar | arXiv 2207.09951v1 | *IEEE Control Systems Letters* 6 (2022) 2485–2490, DOI 10.1109/LCSYS.2022.3166446 |
| Wang–Ventre–Polukarov | arXiv 2508.16589v1 | ICAIF '24 (2024), DOI 10.1145/3677052.3698695 |
| Law–Viens | arXiv 1903.07222v4 | *High Frequency* (year to verify) |
| Choi–Jang–Lee–Zheng | "Preprint submitted to Elsevier", 25 Jan 2021, no arXiv stamp | journal to verify |
| Martin–Tse | dated 24 Mar 2026, no arXiv stamp on p.1 | to verify |
| Guéant–Manziuk | arXiv 1910.13205v1 | *Applied Mathematical Finance* 2019 (to verify) |
| Jusselin | arXiv 2003.05958v2 | proposal cites 2021; journal to verify |

## Inventory

Depth: **D** = deep, **S** = standard, **M** = map (consult only).

### B1 — Core works (deep)

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 1 | arXiv_1105.3115 | gueant-2013-dealing-inventory-risk (pub?) | Guéant, Lehalle, Fernandez-Tapia | Dealing with the Inventory Risk: a solution to the market making problem | v5 | D |
| 2 | Closed-form approximations…__.pdf | bergault-2021-closed-form-approximations (pub?) | Bergault, Evangelista, Guéant, Vieira | Closed-form approximations in multi-asset market making | 1810.04383v5 | D |
| 3 | Cartea, Jaimungal & Ricci….pdf | cartea-2014-buy-low-sell (pub?) | Cartea, Jaimungal, Ricci | Buy Low Sell High: a High Frequency Trading Perspective | SSRN 2014 | D |
| 4 | arXiv_2608.02002 | barzykin-2026-hawkes-driven-otc | Barzykin | Hawkes-Driven OTC Market Making: Volterra–Riccati Approximation | v2 | D |
| 5 | arXiv_2405.03496 | bergault-2024-price-aware-automated | Bergault, Bertucci, Bouba, Guéant, Guilbert | Price-Aware Automated Market Makers: Models Beyond Brownian Prices and Static Liquidity | v3 | D |
| 6 | Optimal Market-Making with Hawkes Process…Mercer's Expansion.pdf | martin-2026-market-making-hawkes | Martin, Tse | Optimal Market-Making with Hawkes Process: A Markovian Approximation Approach via Mercer's Expansion | 2026-03-24 | D |
| 7 | arXiv_2003.05958 | jusselin-2020-persistent-order-flow (pub?) | Jusselin | Optimal market making with persistent order flow | v2 | D |
| 8 | arXiv_2610.16524 | acero-2026-hawkes-structured-networks | Acero, Plank, Zhang | Reinforcement Learning with Hawkes-Structured Networks for Market Making | v1 | D |

### B2 — Hawkes control: numerical/neural solutions, Markov lift, Barzykin feedback models

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 9 | Optimal Market-Making Strategies under Synchronised…pdf | choi-2021-synchronised-order-arrivals (pub?) | Choi, Jang, Lee, Zheng | Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks | preprint 2021 | S |
| 10 | arXiv_2510.26438 | jain-2025-impulse-control-hawkes | Jain, Firoozye, Kochems, Treleaven | An Impulse Control Approach to Market Making in a Hawkes LOB Market | v2 | S |
| 11 | arXiv_2507.11294 | khabou-2025-markov-approximation-hawkes | Khabou, Talbi | Markov approximation for controlled Hawkes Jump-Diffusions with general kernels | v1 | S |
| 12 | arXiv_2608.19151 | bielecki-2026-continuous-time-reinforcement | Bielecki, Mastrolia, Yan | Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions | v1 | S |
| 13 | arXiv_2608.29473 | sakhanda-2026-hawkes-jump-diffusion | Sakhanda, Ricalde-Guerrero | Stochastic Optimal Control of Hawkes Jump-Diffusion Systems | v1 | S |
| 14 | arXiv_2603.07752 | barzykin-2026-dynamic-slippage-control | Barzykin | Dynamic slippage control and rejection feedback in spot FX market making | v1 | S |
| 15 | arXiv_2603.10569 | barzykin-2026-win-score-promotion | Barzykin | Win-score promotion gates in aggregator-routed RFQ markets: A two-tier stochastic control model | v1 | S |
| 16 | arXiv_2607.11328 | barzykin-2026-strategic-otc-reputation | Barzykin | Strategic OTC market making with reputation feedback | v2 | S |

### B3 — Learned policies (RL) under Hawkes or non-stationary flow

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 17 | Deep reinforcement learning…corporate bonds….pdf | gueant-2019-deep-reinforcement-learning (pub?) | Guéant, Manziuk | Deep reinforcement learning for market making in corporate bonds: beating the curse of dimensionality | 1910.13205v1 | S |
| 18 | arXiv_2207.09951 | gasperov-2022-deep-reinforcement-learning | Gašperov, Kostanjčar | Deep Reinforcement Learning for Market Making Under a Hawkes Process-Based Limit Order Book Model | v1 | S |
| 19 | arXiv_2109.15110 | kumar-2021-deep-hawkes-process | Kumar | Deep Hawkes Process for High-Frequency Market Making | v1 | S |
| 20 | arXiv_2609.22785 | yang-2026-robust-market-making | Yang, Xu | Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning | v1 | S |
| 21 | arXiv_2508.16589 | wang-2024-arl-multi-action | Wang, Ventre, Polukarov | ARL-Based Multi-Action Market Making with Hawkes Processes and Variable Volatility | v1 | S |
| 22 | arXiv_2510.27334 | jafree-2025-ai-trading-agents | Jafree, Jain, Firoozye | When AI Trading Agents Compete: Adverse Selection of Meta-Orders by RL-Based Market Making | v1 | S |
| 23 | arXiv_2606.05882 | ochedzan-2026-market-informedness | Ochedzan, Antulov-Fantulin | The Impact of Market Informedness on Market Makers' Profitability | v2 | S |
| 24 | arXiv_2609.11614 | moret-2026-deep-learning-robust | Moret, Lillo | Deep Learning of Robust Market Making under Regime-Switching Order Flow | v1 | S |

### B4 — Multi-asset closed forms / Riccati structure (Poisson or other non-Hawkes flow)

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 25 | arXiv_1605.01862 | gueant-2017-optimal-market-making (pub?) | Guéant | Optimal market making | v5 | S |
| 26 | arXiv_1907.01225 | bergault-2019-size-matters-otc | Bergault, Guéant | Size matters for OTC market makers: general results and dimensionality reduction techniques | v5 | S |
| 27 | arXiv_2106.06974 | barzykin-2021-algorithmic-market-making | Barzykin, Bergault, Guéant | Algorithmic market making in dealer markets with hedging and market impact | v6 | S |
| 28 | arXiv_2112.02269 | barzykin-2021-market-making-fx | Barzykin, Bergault, Guéant | Market making by an FX dealer: tiers, pricing ladders and hedging rates for optimal risk control | v3 | S |
| 29 | arXiv_2207.04100 | barzykin-2022-multi-currency-inventory | Barzykin, Bergault, Guéant | Dealing with multi-currency inventory risk in FX cash markets | v4 | S |
| 30 | arXiv_2309.04216 | bergault-2023-liquidity-dynamics-rfq | Bergault, Guéant | Liquidity Dynamics in RFQ Markets and Impact on Pricing | v3 | S |
| 31 | arXiv_2604.20406 | barzykin-2026-bond-market-making | Barzykin, Ciceri | Bond Market Making with a Hit-Ratio Target | v2 | S |
| 32 | arXiv_2212.10164 | rosenbaum-2022-multi-asset-market | Rosenbaum, Zhang | Multi-asset market making under the quadratic rough Heston | v1 | S |
| 33 | arXiv_2202.07478 | drissi-2022-solvability-differential-riccati | Drissi | Solvability of Differential Riccati Equations and Applications to Algorithmic Trading with Signals | v3 | S |
| 34 | arXiv_2407.17393 | boyce-2024-market-making-exogenous | Boyce, Herdegen, Sánchez-Betancourt | Market Making with Exogenous Competition | v1 | S |

### B5 — Other single-agent control models of market making

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 35 | arXiv_1106.5040 | guilbaud-2011-optimal-high-frequency | Guilbaud, Pham | Optimal high frequency trading with limit and market orders | v1 | S |
| 36 | arXiv_1303.7177 | fodra-2013-high-frequency-market | Fodra, Labadie | High-frequency market-making for multi-dimensional Markov processes | v2 | S |
| 37 | arXiv_1310.1756 | fodra-2013-high-frequency-trading | Fodra, Pham | High frequency trading and asymptotics for small risk aversion in a Markov renewal model | v2 | S |
| 38 | arXiv_1902.01157 | campi-2019-optimal-market-making | Campi, Zabaljauregui | Optimal market making under partial information with general intensities | v3 | S |
| 39 | arXiv_2508.20225 | barzykin-2025-optimal-quoting-adverse | Barzykin, Bergault, Guéant, Lemmel | Optimal Quoting under Adverse Selection and Price Reading | v6 | S |
| 40 | arXiv_2601.13421 | barzykin-2026-market-making-transient | Barzykin | Market Making and Transient Impact in Spot FX | v2 | S |
| 41 | arXiv_2512.04603 | barzykin-2025-fx-market-making | Barzykin, Boyce, Neuman | FX Market Making with Internal Liquidity | v1 | S |
| 42 | arXiv_2605.30643 | niang-2026-quality-adjusted-hit | Niang | Quality-Adjusted Hit-Ratio Targeting in Corporate Bond Market Making | v1 | S |
| 43 | arXiv_2501.03658 | barucci-2025-market-making-fads | Barucci, Mathieu, Sánchez-Betancourt | Market Making with Fads, Informed, and Uninformed Traders | v3 | S |
| 44 | arXiv_2608.07690 | cotton-2026-simple-relationship-order | Cotton | On a Simple Relationship Between Order Imbalance, Skew and Width in Over-The-Counter Trading | v1 | S |

### B6 — Games, macroscopic models, discrete-time / LOB-structural models

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 45 | arXiv_2307.14129 | guo-2023-macroscopic-market-making | Guo, Jin, Nam | Macroscopic Market Making | v3 | S |
| 46 | arXiv_2504.06717 | guo-2025-optimal-execution-macroscopic | Guo, Jin | Optimal Execution and Macroscopic Market Making | v2 | S |
| 47 | arXiv_2203.13053 | baldacci-2022-mean-field-game | Baldacci, Bergault, Possamaï | A mean-field game of market-making against strategic traders | v1 | S |
| 48 | arXiv_2405.11444 | chavezcasillas-2024-adaptive-optimal-market | Chávez-Casillas, Figueroa-López, Yu, Zhang | Adaptive Optimal Market Making Strategies with Inventory Liquidation Cost | v1 | S |
| 49 | arXiv_2101.03086 | capponi-2021-market-making-stochastic | Capponi, Figueroa-López, Yu | Market Making with Stochastic Liquidity Demand: Simultaneous Order Arrival and Price Change Forecasts | v1 | M |
| 50 | arXiv_2307.15599 | pulido-2023-understanding-worst-kept | Pulido, Rosenbaum, Sfendourakis | Understanding the worst-kept secret of high-frequency trading | v2 | S |
| 51 | arXiv_1610.00261 | lehalle-2016-limit-order-strategic | Lehalle, Mounjid | Limit Order Strategic Placement with Adverse Selection Risk and the Role of Latency | v4 | S |
| 52 | arXiv_1806.05849 | gao-2018-optimal-market-making | Gao, Wang | Optimal Market Making in the Presence of Latency | v3 | S |
| 53 | arXiv_1903.07222 | law-2019-market-making-weakly (pub?) | Law, Viens | Market Making under a Weakly Consistent Limit Order Book Model | v4 | S |
| 54 | arXiv_2409.02025 | cao-2024-logarithmic-regret-ergodic | Cao, Šiška, Szpruch, Treetanthiploet | Logarithmic Regret in the Ergodic Avellaneda–Stoikov Market Making Model | v2 | S |

### B7 — Empirical order flow, Hawkes statistics, RFQ data (Q5 evidence)

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 55 | arXiv_2601.23172 | muhlekarbe-2026-unified-theory-order | Muhle-Karbe, Ouazzani Chahdi, Rosenbaum, Szymanski | A unified theory of order flow, market impact, and volatility | v2 | S |
| 56 | arXiv_2609.36631 | lee-2026-spread-gated-hawkes | Lee, Lee | A Spread-Gated Hawkes-Flocking Model for Best Bid and Ask Dynamics, with an Application to Limit Order Placement | v1 | S |
| 57 | arXiv_2507.05749 | ananthan-2025-event-time-anchor | Nittur Anantha, Jain, Goyal, Misra | Event-Time Anchor Selection for Multi-Contract Quoting | v2 | S |
| 58 | arXiv_2502.18625 | albers-2025-market-makers-dilemma | Albers, Cucuringu, Howison, Shestopaloff | The Market Maker's Dilemma: Navigating the Fill Probability vs. Post-Fill Returns Trade-Off | v2 | S |
| 59 | arXiv_1511.07773 | fermanian-2015-behavior-dealers-clients | Fermanian, Guéant, Pu | The behavior of dealers and clients on the European corporate bond market: the case of MD2C platforms | v4 | M |
| 60 | arXiv_1810.05884 | gueant-2018-mid-price-estimation | Guéant, Pu | Mid-price estimation for European corporate bonds: a particle filtering approach | v2 | M |
| 61 | arXiv_2506.18147 | marin-2025-causal-interventions-bond | Marín, Ardanza-Trevijano, Sabio | Causal interventions in bond multi-dealer-to-client platforms | v2 | M |

### B8 — Peripheral (map only)

| # | File | Provisional bibkey | Authors | Title | Ver. | Depth |
|---|---|---|---|---|---|---|
| 62 | arXiv_2607.17991 | feil-2026-optimal-market-making | Feil, Nendel | Optimal Market Making in Prediction Markets | v1 | M |
| 63 | arXiv_2610.18158 | wu-2026-order-flow-interventions | Wu, Cai, Li, Wang | When and How Order-Flow Interventions Work After Dealers Adapt | v1 | M |
| 64 | arXiv_2504.00846 | ma-2025-effect-latency-optimal | Ma, Saggese, Smith | The Effect of Latency on Optimal Order Execution Policy | v2 | M |
| 65 | arXiv_2505.12465 | jiang-2025-resolving-latency-inventory | Jiang, Yang, Wang, Li, Huang, Li | Resolving Latency and Inventory Risk in Market Making with Reinforcement Learning | v1 | M |
| 66 | arXiv_2605.21707 | asadulaev-2026-zero-shot-adaptation | Asadulaev | Zero-shot adaptation to order book dynamics | v1 | M |
| 67 | arXiv_2508.04344 | kleitsikas-2025-performative-market-making | Kleitsikas, Leonardos, Ventre | Performative Market Making | v2 | M |

## Proposal references ↔ library (proposal §8, pp. 29–31, 35 references)

**On disk (24 of 35):** Acero et al. 2026 (#8); Barzykin 2026a = arXiv 2603.07752 (#14);
Barzykin 2026b = 2608.02002 (#4); Barzykin 2026c = 2607.11328 (#16); Barzykin, Bergault & Guéant
"2023" = 2207.04100 (#29, key year 2022: no published version found); Barzykin & Ciceri 2026 (#31);
Bergault et al. 2024 (#5); BEGV 2021 (#2); Bergault & Guéant 2023 (#30); Bielecki et al. 2026 (#12);
Boyce et al. 2025 (#34); CJR 2014 (#3); Choi et al. 2021 (#9); Gašperov & Kostanjčar 2022 (#18);
Guéant 2017 (#25); GLFT 2013 (#1); Guéant & Manziuk 2019 (#17); Jain et al. 2025 (#10);
Jusselin 2021 (#7); Khabou & Talbi 2025 (#11); Kumar 2024 (#19); Martin & Tse 2026 (#6);
Rosenbaum & Zhang 2022 (#32); Yang & Xu 2026 (#20).

On disk but **not cited** in the proposal: Barzykin 2026 win-score (#15) and 41 others. These go
into the Q4 comparison matrix wherever they concern Hawkes or multi-asset market making.

**Missing from library (11), the input for plan Task 3:**

| Proposal ref. | Role | Access (expected) |
|---|---|---|
| Avellaneda & Stoikov 2008, *Quantitative Finance* 8(3) | base model | paywalled; author preprint may exist |
| Bacry, Jaisson & Muzy 2016, *Quantitative Finance* 16(8) | slowly decaying Hawkes kernels in LOB data (Q5) | arXiv OA |
| Bacry, Mastromatteo & Muzy 2015, *Market Microstructure and Liquidity* 1(1) | Hawkes in finance, review | arXiv OA |
| Cartea, Jaimungal & Penalva 2015, CUP | textbook, risk-adjusted objective | book; manual |
| Cheridito, Dupret & Hainaut 2025, NeurIPS, arXiv 2505.15602 | generalised policy iteration with jumps | arXiv OA |
| Hawkes 1971, *Biometrika* 58(1) | Hawkes processes | paywalled; manual |
| Ho & Stoll 1981, *J. Financial Economics* 9(1) | inventory models, origin | paywalled; manual |
| Lai, Gao & Li 2023, *Quantitative Finance* 23(5) | multi-asset Hawkes, options market making, RL | paywalled; check arXiv |
| Ogata 1981, *IEEE Trans. Information Theory* 27(1) | thinning simulation | paywalled; manual (methods only, low priority) |
| Schulman et al. 2017, arXiv 1707.06347 | PPO | arXiv OA (methods only, low priority) |
| Tarditi 2026, MSc thesis, Politecnico di Milano, hdl 10589/253302 | bivariate Hawkes, grid solution | institutional repository; may be embargoed |

## Deviations from the plan

- The plan foresaw B2–B7 with ≤ 10 works each. To keep that limit, the inventory adds **B8** (6 peripheral `map` works). Logged in `knowledge/_meta/log.md`.
