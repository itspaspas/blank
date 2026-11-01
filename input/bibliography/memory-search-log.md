---
title: "Novelty search log: decision-relevant memory under power-law Hawkes flow"
type: search-log
created: 2026-11-01
updated: 2026-11-01
plan: "[[lai2023-gaps-and-memory-plan]]"
design: "[[lai2023-gaps-and-memory-design]]"
author: llm
---

# Novelty search log: memory regret under power-law Hawkes flow (plan Task 2)

## Header

| Item | Value |
|---|---|
| Protocol | Fixed search protocol, design `input/ideas/lai2023-gaps-and-memory-design.md` §Cross-examination log; plan Task 2 |
| Publication cut-off | 2026-10-29 |
| Search run date | 2026-11-01 (all queries below were run on this date) |
| Databases named in the protocol | OpenAlex, arXiv (q-fin.TR/CP, math.OC, stat.AP), SSRN, Crossref, Semantic Scholar, Google Scholar |
| Blocks | (A) power-law / slowly decaying / rough / fractional kernel × market making / execution / control × exponential approximation / Markovian lift / multi-factor / regret / misspecification / number of factors. (B) Cox / time-varying / non-stationary baseline × Hawkes × trading. (C) option × order flow × Hawkes × cross / strike / maturity / chain / underlying. (D) forward and backward citations of Lai–Gao–Li 2023, Jusselin 2021, Barzykin 2026b, Acero–Plank–Zhang 2026 |
| Inclusion criterion | The work reports a control / policy / P&L / value quantity under kernel approximation or misspecification (blocks A, B, D), or a multi-contract option Hawkes estimate (block C) |
| Already owned (not counted as new) | The 107 entries of `library/references.bib`, including the 43 source pages in `knowledge/sources/` (checked by title against the bib for every hit) |

### Protocol deviation: database substitution (recorded plainly)

**None of the six named databases was queried directly.** In this container the network policy
blocks the scholarly APIs. Checked on 2026-11-01:
`curl` to `api.openalex.org`, `export.arxiv.org`, `api.crossref.org` and `api.semanticscholar.org`
returned HTTP 000 / `connect_rejected` at the egress proxy. `WebFetch` also failed with a DNS error
(`ENOTFOUND`) for `arxiv.org` and `www.techrxiv.org`. **No abstract or full-text page was opened;
every statement below rests on WebSearch result titles, URLs and snippets only.**

Each database was emulated with the WebSearch tool:

| Protocol database | Emulation used | How well it worked |
|---|---|---|
| arXiv | WebSearch, `allowed_domains: ["arxiv.org"]` | The filter held: almost every result was on arxiv.org. No category filter (q-fin.TR/CP, math.OC, stat.AP), so categories are not enforced |
| SSRN | WebSearch, `allowed_domains: ["papers.ssrn.com","ssrn.com"]` | **The filter leaked.** Only 1 of 9 results per query was on ssrn.com; the rest were arXiv |
| Semantic Scholar | WebSearch, `allowed_domains: ["semanticscholar.org"]` | Leaked: 2–4 of 9–10 results were on semanticscholar.org |
| OpenAlex | WebSearch, `allowed_domains: ["openalex.org"]` | **Did not work:** 0 openalex.org results came back |
| Crossref | WebSearch, `allowed_domains: ["crossref.org","search.crossref.org"]` | **Did not work:** 0 crossref.org results came back |
| Google Scholar | WebSearch, `allowed_domains: ["scholar.google.com"]` | Did not work in practice: at most 1 scholar.google.com page (a lookup or profile page) per query, and no "cited by" lists |
| (supplement) | WebSearch with no domain restriction ("web") | Used for every block |

**Meaning of the counts:** "Hits returned" is the number of result links WebSearch returned. It is
capped at about 10 per query, so it is **not** a database hit count. "Relevant" is the number of
returned works that meet the inclusion criterion, owned or new. "New" counts relevant works that are
not in `library/references.bib`. WebSearch has no date filter, so the cut-off was checked by hand for
each relevant hit, using the date in its arXiv ID or listing.

---

## Block A: power-law / rough kernel × control × approximation / misspecification

| # | Query (exact string) | Database / emulation | Date | Hits returned | Relevant (new) | Notes |
|---|---|---|---|---|---|---|
| A1 | `market making power-law Hawkes kernel sum of exponentials approximation number of factors regret` | arXiv: web via WebSearch, restricted to arxiv.org | 2026-11-01 | 10 | 2 (0) | Barzykin 2608.02002 and Jain 2510.26438 (both owned). Also returned Bacry 2015 (owned), plus Hardiman 1302.1405, Lallouache 1406.3967 and Filimonov 1308.6756 (all on the acquisition list; estimation papers, outside the inclusion criterion) |
| A2 | `optimal execution power-law Hawkes kernel multi-factor Markovian approximation optimal control error` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 3 (1) | **New:** TechRxiv 10.36227/techrxiv.176412729.90497182/v1 (26 Nov 2025, execution under self-exciting flow). Owned: Bielecki 2608.19151, Barzykin. Also Alfonsi–Blanc 1506.08740 (owned; outside the criterion) |
| A3 | `rough Hawkes OR fractional Hawkes market making optimal quotes Markovian lift exponential factors` | arXiv: restricted to arxiv.org | 2026-11-01 | 9 | 3 (0) | Barzykin, Acero 2610.16524 and Jusselin 2003.05958 (all owned). Not included: 2609.08541 (rough Hawkes–Heston hedging), 2608.07709, 2409.12776, 2610.37324, 1710.03506 |
| A4 | `misspecified Hawkes kernel market maker regret exponential vs power law intensity forecast error` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 3 (0) | Barzykin, Acero, Jain (owned). Not included: 2503.14814 (power-law vs exponential fit; estimation only), 1405.6047 |
| A5 | `Hawkes power-law kernel approximation sum of exponentials optimal trading value function convergence number of exponentials` | SSRN: restricted to papers.ssrn.com and ssrn.com (filter leaked; 1 of 9 on SSRN) | 2026-11-01 | 9 | 1 (1) | **New:** Abi Jaber et al., arXiv 2503.04323 (Fredholm, nonlinear propagator): optimal P&L vs number of exponential time scales on a power-law and a shifted power-law impact kernel. The one SSRN hit, Bilokon SSRN 6649358 (sum-of-exponentials for rough-volatility *simulation*), is outside the criterion |
| A6 | `market making Hawkes kernel misspecification regret power-law memory exponential approximation` | Semantic Scholar: restricted to semanticscholar.org (filter leaked; 2 of 9 on S2) | 2026-11-01 | 9 | 1 (0) | Jain (owned). Not included: 1610.05383 (burst detection, robust to kernel misspecification; no control), 1402.1288, 1403.5227 |
| A7 | `optimal execution transient impact power-law propagator multi-factor exponential approximation value function convergence Volterra` | arXiv: restricted to arxiv.org | 2026-11-01 | 10 | 3 (1) | **New:** 2601.03799 (Uniswap execution; power-law kernel replaced by a convex combination of exponentials, "a single term was already accurate enough" per snippet). Owned: Abi Jaber–Neuman 2211.00447, Barzykin. Not resolvable: 2610.24558v1, "Optimal Trading Filters and the Value of Predictive Signals" (a title-only lookup found nothing; see Not reachable). Not included: 2511.09701, 2601.22113, 1901.02327, 1609.00599, 2403.10273 |
| A8 | `"regret" "Hawkes" "power-law" kernel "exponential" approximation reinforcement learning market making number of exponentials reward` | arXiv: restricted to arxiv.org | 2026-11-01 | 10 | 4 (0) | Acero, Jain, Barzykin, Bielecki (all owned). Others owned or outside the criterion (2508.16589 Wang, 2207.09951 Gašperov) |
| A9 | `Fredholm nonlinear propagator models optimal execution Abi Jaber 2025 sum of exponentials power law PnL` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 1 (0, duplicate of A5) | Authors of 2503.04323 per the search summary: Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann. Not included: 2601.03215 (power-law propagator with resistance; no approximation sweep), 2609.02447, 2506.07993 |
| A10 | `Hawkes order flow slowly decaying kernel optimal market making approximation error control policy value loss` | OpenAlex: restricted to openalex.org (**0 of 9 on openalex.org**; every result was arXiv) | 2026-11-01 | 9 | 1 (0) | Jain (owned). Owned, outside the criterion: Gennaro 2606.19772, Yang 2609.22785, Bacry 1412.7096, Muhle-Karbe 2601.23172 |
| A11 | `market making Hawkes power law kernel exponential approximation regret` | Google Scholar: restricted to scholar.google.com (1 of 9 on GS, a DOI lookup page) | 2026-11-01 | 9 | 2 (0) | Jain, Khabou 2507.11294 (owned). Block-C lead: Baldacci 2012.10875 (see C1). Not included: 2303.02038 |
| A12 | `stochastic Volterra control multi-factor approximation convergence value function optimal control fractional kernel number of factors` | arXiv: restricted to arxiv.org | 2026-11-01 | 9 | 1 (0) | Abi Jaber–Miller–Pham 1911.01900 (owned: value-function approximation by multi-factor LQ problems, bounded by the kernel L² error). Abi Jaber–El Euch 1801.10359 is on the acquisition list. Not included: 2603.02946, 2503.01716, 1901.01193 |
| A13 | `"fractional Hawkes" OR "rough Hawkes" optimal control trading strategy Markovian approximation` | web via WebSearch, unrestricted | 2026-11-01 | 10 | 4 (0) | Martin–Tse (SSRN 6451058), Barzykin, Jusselin, Jain (all owned). TechRxiv preprint again (duplicate of A2). Not included: 2409.12776, MDPI Risks 10(8):160 |
| A14 | `Hawkes kernel misspecification optimal execution robust model uncertainty value loss exponential kernel true power law` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 1 (0, duplicate) | Per its snippet, the TechRxiv preprint (A2) has a section that "tests robustness to kernel misspecification … when the true kernel differs from the assumed one". Also returned: Chatziandreou–Karbach 2504.10282 (block B) and Alfonsi–Blanc (owned) |
| A15 | `"sum of exponentials" power-law kernel trading strategy P&L "number of exponentials" Hawkes or propagator approximation performance` | web via WebSearch, unrestricted | 2026-11-01 | 10 | 1 (0, duplicate) | 2503.04323 snippet: the "two exponential time scales" rule of thumb looks reasonable; "five exponential time scales are preferred to properly mimic the same numerical performances as the power-law"; for the shifted power law, three suffice. Not included: 2508.20311 (numerical sum-of-exponentials) |
| A16 | `cost of misspecifying impact decay kernel optimal trading second-order loss formula quadratic in forecast error` | arXiv: restricted to arxiv.org | 2026-11-01 | 9 | 2 (2) | **New:** Hey et al. 2306.00599, "The Cost of Misspecifying Price Impact" (asymmetric cost of a wrong impact concavity or decay). **New:** 2204.08581, "On Parametric Optimal Execution and Machine Learning Surrogates" (Tao Chen et al.; a misspecified decay kernel costs 9–12%). The snippets do not show whether either cost is second order |
| A17 | `market making long-memory order flow nearly unstable Hawkes rough order flow optimal market maker strategy power law` | arXiv: restricted to arxiv.org | 2026-11-01 | 10 | 2 (0) | Barzykin, Jusselin (owned). Not included: 2412.16850 (LOB model with rough volatility) |
| A18 | `Hawkes power-law kernel exponential approximation market making optimal control` | Crossref: restricted to crossref.org and search.crossref.org (**0 of 9 on Crossref**) | 2026-11-01 | 9 | 3 (0) | Jusselin, Khabou, Jain (owned). Baldacci 2012.10875 again (C) |
| A19 | `controlled Hawkes process general kernel finite-dimensional approximation value function error bound number of exponentials optimal control math.OC` | arXiv (math.OC intent): restricted to arxiv.org | 2026-11-01 | 9 | 3 (0) | Acero, Khabou, Bielecki (owned). Not included: 1801.08273, 2411.00621 (estimation) |
| A20 | `value of memory order flow market maker how many exponential factors needed power-law Hawkes forecast policy loss second-order` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 1 (0) | Barzykin (owned). Nothing else in scope |
| A21 | `"Reinforcement Learning in Non-Markov Market-Making" Hawkes kernel` | web via WebSearch, unrestricted (check on an A3/B4 lead) | 2026-11-01 | 10 | 1 (0) | Lalor–Swishchuk 2410.14504: semi-Markov/Hawkes SAC market making, **no kernel approximation**, so excluded. Bielecki (owned): in the power-law case the filtered method comes close to the *mixture* HJB benchmark, not an exact oracle (already recorded on its source page) |

**Block A total:** 21 queries (13 restricted, 8 unrestricted). Relevant (with duplicates): 43.
**Distinct new works:** 5 (2503.04323, 2306.00599, 2204.08581, 2601.03799, TechRxiv 176412729).

## Block B: Cox / time-varying / non-stationary baseline × Hawkes × trading

| # | Query (exact string) | Database / emulation | Date | Hits returned | Relevant (new) | Notes |
|---|---|---|---|---|---|---|
| B1 | `market making Hawkes time-varying baseline intensity non-stationary Cox process optimal quotes` | arXiv: restricted to arxiv.org | 2026-11-01 | 9 | 1 (0) | Barzykin (owned; seasonality-adjusted RFQ flow, Poisson benchmark on the deterministic baseline). **Adjacent, new:** Chatziandreou–Karbach 2504.10282 (B-spline time-varying baseline, Hawkes, execution; cost vs TWAP/VWAP, but no misspecification arm visible). Not included: 2610.37324 |
| B2 | `non-stationary baseline Hawkes trading optimal execution intraday seasonality exogenous intensity spurious criticality control` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 1 (0, duplicate of A2) | TechRxiv preprint (A2): spline baselines, plus a stability condition that "prevent[s] spurious round-trip strategies". Not included (estimation only): Filimonov 1308.6756 (acquisition list), 2506.02631 and 2501.17245 (locally stationary Hawkes), 2401.09361, 2502.04027 |
| B3 | `market making doubly stochastic Cox intensity time-varying arrival rate Hawkes intraday seasonality optimal spreads` | SSRN: restricted to papers.ssrn.com and ssrn.com (leaked; 1 of 9 on SSRN: Barzykin SSRN 7224080) | 2026-11-01 | 9 | 3 (0) | Barzykin, Jusselin, Jain (owned). Not included: 1811.03766 (periodic baseline; estimation), 1301.1135, 2405.11444 (owned: chavezcasillas-2024) |
| B4 | `Markov-modulated OR regime-switching Hawkes baseline market making optimal control misspecified baseline` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 2 (0) | Acero (owned; regime-switching kernel environment), Yang 2609.22785 (owned; adversarial robustness). Not included: 2502.04027, 2410.14504, 2502.17417 |

**Block B total:** 4 queries. Relevant (with duplicates): 7. **Distinct new works meeting the criterion: 0.**
One new adjacent work: 2504.10282.

## Block C: option × order flow × Hawkes × cross / strike / maturity / chain / underlying

| # | Query (exact string) | Database / emulation | Date | Hits returned | Relevant (new) | Notes |
|---|---|---|---|---|---|---|
| C1 | `multivariate Hawkes option order flow across strikes maturities option chain cross-excitation estimation` | arXiv: restricted to arxiv.org | 2026-11-01 | 10 | 0 strict (2 adjacent, new) | **Adjacent:** Baldacci 2012.10875, "High-frequency dynamics of the implied volatility surface" (Hawkes cross-excitation between options of different strikes drives skew and convexity; the snippet calls the example illustrative, not a fitted chain). **Adjacent analogue:** Jhabli et al. 2610.23619 (cross-contract Hawkes estimate for quarter-hourly vs hourly *electricity* contracts, not options). Not included: 1811.08076, 2408.03594, 1809.08060 |
| C2 | `Hawkes process option trades underlying stock cross-excitation options market high-frequency empirical` | web via WebSearch, unrestricted | 2026-11-01 | 10 | 1 (1) | **New, meets the C criterion:** Hsieh–Guo–Zhao, EFMA 2017 symposium paper, "Contagion Behavior of High-frequency Trading in Future and Option Markets": a bivariate Hawkes model estimated on US index futures and options; "little mutual-excitation evidence of the futures on the options", strong self-excitation within options. It is cross-market, not cross-strike. Lai (owned): insignificant buy–sell cross-excitation |
| C3 | `options market making Hawkes order arrivals multiple strikes portfolio of options inventory vega` | SSRN: restricted to papers.ssrn.com and ssrn.com (leaked; 1 of 9 on SSRN: Lai SSRN 4080704) | 2026-11-01 | 9 | 0 strict (2 adjacent, new) | **Adjacent:** Aubert–Chevalier–Ly Vath 2511.02518, option MM with hedging-induced impact. Option flow is Cox with intensities that depend on the underlying (abstract), but one PDF snippet says marked Hawkes with exponential kernels; snippets disagree. **Adjacent:** 2609.26606, "Liquidity Provision and Rebate Design in Option Markets" (multi-option delta and vega bounds; Hawkes not confirmed). Lai (owned) |
| C4 | `Hawkes model option order flow cross-excitation between strikes and maturities and underlying futures estimated CBOE OPRA data` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 0 (0) | Nothing option-specific. Jhabli 2610.23619 again |

**Block C total:** 4 queries. **1 new work meets the C criterion** (Hsieh–Guo–Zhao 2017, futures × options).
**No multi-strike or multi-maturity option-chain Hawkes estimate was found.**

## Block D: forward and backward citations of the four seeds

Seed metadata as confirmed in results: Lai, Gao & Li, "A data-driven deep learning approach for
options market making", *Quant. Finance* 23(5) 777–797 (2023), DOI 10.1080/14697688.2023.2186257,
SSRN 4080704 (**title confirmed**). Jusselin, "Optimal market making with persistent order flow",
SIFIN 12 (2021), arXiv 2003.05958. Barzykin, "Hawkes-Driven OTC Market Making: Volterra–Riccati
Approximation", arXiv 2608.02002 (3 Aug 2026) and SSRN 7224080. Acero, Plank & Zhang,
"Reinforcement Learning with Hawkes-Structured Networks for Market Making", arXiv 2610.16524,
accepted at ACM ICAIF 2026.

| # | Seed | Query (exact string) | Database / emulation | Date | Hits returned | Relevant (new) | Notes |
|---|---|---|---|---|---|---|---|
| D1 | Lai 2023 (forward) | `"data-driven deep learning approach for options market making" Lai Gao Li cited` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 0 (0) | Citers seen: "Data-driven hedging of stock index options via deep learning" (*Oper. Res. Lett.* 2023; hedging, outside the criterion); "Beyond the Greeks: Proactive Neural Residual Hedging…" (listed on ouci.dntb.gov.ua; hedging); a Medium post. **No citer reports a memory or kernel-approximation quantity** |
| D2 | Lai 2023 (forward) | `Lai Gao Li 2023 options market making Hawkes power law citing paper deep learning option market making order flow` | Semantic Scholar / Google Scholar / OpenAlex: restricted to semanticscholar.org, scholar.google.com, openalex.org (4 of 10 on S2) | 2026-11-01 | 10 | 0 (0) | Kumar, Gašperov, Yang, Jain (owned; Acero, owned, cites Lai). Not included: 2502.17417 (neural-Hawkes LOB simulation), 2510.15883 |
| D3 | Jusselin 2021 (forward) | `"Optimal market making with persistent order flow" Jusselin citations power law Hawkes market making` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 0 (0) | Citers seen: Feil 2607.17991 (owned), Guo 2025 (owned), Jain (owned), Moret 2609.11614 (owned), and a Springer chapter "Computational Methods for Market Making Algorithms" (10.1007/978-3-031-11818-0_66; content not visible, not assessable) |
| D4 | Jusselin 2021 (forward) | `Jusselin "persistent order flow" market making Hawkes cited by 2025 2026 long memory order flow optimal quotes` | Semantic Scholar / Google Scholar: restricted to semanticscholar.org, scholar.google.com (2 of 9 on-domain) | 2026-11-01 | 9 | 0 (0) | A Google Scholar snapshot gives 29 citations, but the cited-by list was not reachable. Citers seen: Gennaro 2606.19772 (owned), Jain, Yang (owned). Not included: 2511.18117 |
| D5 | Barzykin 2026b (forward) | `"Volterra-Riccati" Barzykin Hawkes OTC market making citing OR follow-up power-law kernel forecast curve` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 0 (0) | **No forward citer found** (the paper is from Aug 2026). A pith.science page claims "cited by 1"; this is unverified and probably automated |
| D6 | Acero 2026 (forward) | `"Hawkes-Structured Networks" market making Acero Plank Zhang` | web via WebSearch, unrestricted | 2026-11-01 | 9 | 0 (0) | Confirms ICAIF 2026 acceptance. **No forward citer found** (Oct 2026 preprint) |
| D7 | Acero 2026 (forward) | `Acero Plank Zhang 2026 Hawkes-structured networks ICAIF cited power-law truncation regret bound follow-up` | web via WebSearch, unrestricted | 2026-11-01 | 10 | 0 (0) | All results off topic (2304.08061, 2311.02577 queueing with Hawkes arrivals, network science) |
| D8 | Barzykin / Acero (recency sweep for citers) | `Hawkes market making 2026 arXiv power-law kernel memory factors exponential mixture policy regret benchmark exact lifted HJB` | arXiv: restricted to arxiv.org | 2026-11-01 | 9 | 3 (0) | Barzykin, Acero, Jain (owned). Jhabli 2610.23619 again: "every finite R exponential mixture decays geometrically and … underestimates the power-law tail" (estimation, not control) |
| D9 | Jusselin 2021 (forward) | `Optimal market making persistent order flow Jusselin completely monotone kernel approximating exponentials feedback control converges gains 10% Poisson` | Semantic Scholar: restricted to semanticscholar.org (4 of 9 on S2) | 2026-11-01 | 9 | 0 (0) | Owned only (Moret, Gennaro); others outside the criterion |

**Backward citations (all four seeds)** were taken from the reference lists that were read in full
during earlier ingests and are recorded on the source pages, not from a database: Barzykin 2026b
pp. 23–24, Acero 2026 refs [1]–[42], Lai 2023 pp. 796–797, Jusselin 2021 refs [1]–[27]. Results:

- **Owned:** Martin–Tse 2026, Bergault et al. 2024, Abi Jaber–Neuman 2025, Jusselin 2021, Khabou–Talbi 2025, Lai 2023, Jain 2025.
- **On the acquisition list:** Alfonsi–Kebaier 2024 and Bayer–Breneis 2023 (cited by Acero), Abi Jaber 2019 (cited by Jusselin), Lai 2021 thesis (cited by Lai 2023).
- **Not in the library and outside the criterion:** Gao–Zhou–Zhu 2018 and Baldacci–Bergault–Guéant 2021 (options MM, Poisson flow), both cited by Lai.

None of these backward references reports a quantity versus the number of factors on a power-law truth.

**Block D total:** 9 queries, at least one per seed (Lai 2, Jusselin 3, Barzykin 1 + D8, Acero 2 + D8).
Relevant (with duplicates): 3, all owned. **New works meeting the criterion: 0.**

## Metadata lookups (not protocol queries; listed for completeness)

These were run on 2026-11-01 to identify hits and to resolve the nine acquisition keys. They are not
counted in the block totals.

| # | Query (exact string) | Emulation | Purpose / outcome |
|---|---|---|---|
| M1 | `"Fredholm Approach to Nonlinear Propagator Models" authors` | web | No authors in the snippets; see A9 |
| M2 | `"Optimal Trading Filters and the Value of Predictive Signals"` | web | No match for the 2610.24558v1 title |
| M3 | `techrxiv 2025 "optimal execution under self-exciting" order flow kernel misspecification` | web | No match; the TechRxiv preprint's title and authors stay unresolved |
| M4 | `"High-frequency dynamics of the implied volatility surface" Hawkes power law market making options` | web | 2012.10875, Dec 2020; "one listing credits Bastien Baldacci" |
| M5 | `"The Cost of Misspecifying Price Impact" Hey Mastromatteo Muhle-Karbe Webster` | web | Authors: Hey, Bouchaud, Mastromatteo, Muhle-Karbe, Webster; arXiv 2306.00599 (1 Jun 2023); Risk.net version |
| M6 | `Karbach Chatziandreou optimal execution intraday energy markets Hawkes transient impact B-spline baseline` | web | Chatziandreou & Karbach; *Quant. Finance* 26(2) 185–211 (2026), per the UvA repository |
| M7 | `"Contagion Behavior of High-frequency Trading in Future and Option Markets" Hawkes authors` | web | Peilin Hsieh, Yuqiang Guo, Hongbiao Zhao (Xiamen); EFMA 2017; PDF dated 23 Dec 2016 |
| M8 | `"Option market making with hedging-induced market impact" Hawkes authors 2025` | web | Aubert, Chevalier, Ly Vath; arXiv 2511.02518 (4 Nov 2025); flow model ambiguous (Cox vs marked Hawkes) |
| M9 | `"Cross-product Modelling in Continuous Intraday Electricity Markets via Hawkes Processes"` | web | Jhabli, Alskaif, Bennin, Tekinerdogan, Pennings; arXiv 2610.23619 (exact posting day not seen) |
| M10–M27 | Metadata queries for the nine keys (titles, DOIs, venues) | web; restricted to projecteuclid.org, ideas.repec.org / econpapers.repec.org / tandfonline.com, repository.lib.cuhk.edu.hk / cuhk.edu.hk, scholar / S2 / OpenAlex / proquest | Results in `memory-acquisition-metadata.json`. The Lai 2021 thesis citation was also checked against the reference list in `library/pdf/lai-2023-data-driven-deep.pdf` (local, `pdftotext`) |

---

## Relevant hits (new, not in the library)

Gap parts: **(1)** a predictive second-order regret law; **(2)** a reward/regret-vs-p table on a
power-law / slowly decaying truth, with the control-approximation error separated and an exact or
near-exact reference; **(3)** a map of when memory is irrelevant. "C" marks a block-C
(cross-contract option flow) hit, which bears on the design's second-paper gap and not on (1)–(3).

| # | Citation (as far as verified in snippets) | Link seen in results | Before cut-off? | Gap part | Verdict | Why |
|---|---|---|---|---|---|---|
| R1 | Abi Jaber, E., Bondi, A., De Carvalho, N., Neuman, E., Tuschmann, S. (2025). *Fredholm Approach to Nonlinear Propagator Models.* arXiv 2503.04323 (authors per a search summary; "forthcoming in Finance & Stochastics, 2026" per the same summary, unverified) | https://arxiv.org/pdf/2503.04323 | Yes (Mar 2025) | (2), (3) | **Narrows** (adjacent problem) | Optimal **execution** with signals and a nonlinear transient-impact **propagator**, not Hawkes order-flow market making. It reports empirical optimal P&L as the number of exponential time scales grows, for a power-law and a shifted power-law propagator, against the power-law kernel's own performance computed by its Fredholm scheme. That reference is general-kernel, so possibly near-exact. Rule of thumb from the snippet: 2 exponentials reasonable, 5 to match the power law, 3 for the shifted kernel. Unknown from snippets: whether the p-exponential *policy* is evaluated on the *true* kernel (a regret) or optimal P&Ls are compared across models (a value of the model, as in Jusselin Fig. 4). **No regret law.** Must be read in full |
| R2 | Hey, N., Bouchaud, J.-P., Mastromatteo, I., Muhle-Karbe, J., Webster, K. (2023). *The Cost of Misspecifying Price Impact.* arXiv 2306.00599 | https://www.arxiv.org/pdf/2306.00599 ; https://risk.net/investing/7958754/the-cost-of-mis-specifying-price-impact | Yes (Jun 2023) | (1) | **Adjacent** | Misspecification cost of the impact concavity and decay in execution, with formulas in a technical companion paper. The cost is **asymmetric** (overestimating decay can turn profits into losses), so it is not, on the snippet's evidence, a symmetric second-order law in a forecast error. Not market making, not an intensity forecast |
| R3 | Chen, T. et al. (2022). *On Parametric Optimal Execution and Machine Learning Surrogates.* arXiv 2204.08581 (only the first author's name is visible) | https://arxiv.org/pdf/2204.08581 | Yes | (1) | **Adjacent** | Snippet: misspecifying the decay kernel is costly; a neural solver beats a linear-factor strategy by 9–12%. A control quantity under kernel misspecification, but no p-sweep and no regret law |
| R4 | (authors not seen) *Optimal execution on Uniswap v2/v3 under transient price impact.* arXiv 2601.03799 | https://arxiv.org/html/2601.03799v1 | Yes (Jan 2026) | (2), (3) | **Adjacent** | A power-law resilience kernel is replaced by a fitted convex combination of exponentials on [0,T]; "a single term was already accurate enough" in their setting. One data point for (3) in an execution problem; no table vs p, no exact reference reported in the snippet |
| R5 | (title truncated, authors not seen) TechRxiv preprint, 26 Nov 2025, "Optimal execution under self-exciting [order flow …]". DOI 10.36227/techrxiv.176412729.90497182/v1 | https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176412729.90497182/v1 | Yes (Nov 2025) | (1); block B | **Adjacent; not conclusive** | The snippets describe a section testing robustness when the true kernel differs from the assumed one, min-max control under misspecification, spline intraday baselines, and a remark that closed-form execution with Markovian embeddings of power-law decay is an open gap (suggesting 2–3 exponentials). Execution, not MM. **The full text could not be opened** (techrxiv.org blocked) |
| R6 | Chatziandreou, K., Karbach, S. (2026). *Optimal Execution in Intraday Energy Markets under Hawkes Processes with Transient Impact.* *Quant. Finance* 26(2) 185–211; arXiv 2504.10282 | https://arxiv.org/abs/2504.10282 ; https://dare.uva.nl/id/01ed0d45-7152-4386-94da-ba8bf29a1304 | Yes | block B only | **Adjacent** | Hawkes execution with a B-spline time-varying baseline. The back-test costs are a control quantity, but no kernel misspecification or approximation arm is visible. Does not touch (1)–(3) |
| R7 | Hsieh, P., Guo, Y., Zhao, H. (2017). *Contagion Behavior of High-frequency Trading in Future and Option Markets.* EFMA 2017 symposium paper | https://www.efmaefm.org/0EFMSYMPOSIUM/2017/papers/Paper_HF_Contagion.pdf | Yes | C | **Narrows the cross-contract gap slightly** | The only multi-contract Hawkes *estimate* involving options that was found: futures × options (US index), structural shifts after overnight jumps; weak futures→options excitation. Not cross-strike or cross-maturity, so it does not close the option-chain gap |
| R8 | Baldacci, B. (2020). *High-frequency dynamics of the implied volatility surface.* arXiv 2012.10875 (sole authorship not confirmed) | https://arxiv.org/pdf/2012.10875 | Yes | C | **Adjacent** | A tick-level Hawkes model of the IV surface with cross-excitation between strikes, plus no-arbitrage conditions across maturities. Per the snippet the example is illustrative, not a fitted option-chain estimate |
| R9 | Jhabli, A., Alskaif, T., Bennin, K. E., Tekinerdogan, B., Pennings, J. M. E. (2026). *Cross-product Modelling in Continuous Intraday Electricity Markets via Hawkes Processes.* arXiv 2610.23619 | https://arxiv.org/html/2610.23619 ; https://econpapers.repec.org/RePEc:arx:papers:2610.23619 | Unverified (Oct 2026; posting day not seen) | C (analogue); context for (2) | **Adjacent** | A cross-contract state-dependent Hawkes estimate (quarter-hourly vs hourly electricity), not options. Remarks that a finite R-exponential mixture underestimates a power-law tail; estimation only, no control |
| R10 | Aubert, P., Chevalier, E., Ly Vath, V. (2025). *Option market making with hedging-induced market impact.* arXiv 2511.02518 | https://arxiv.org/pdf/2511.02518 | Yes | C | **Adjacent** | Option MM; flow intensities depend on the underlying's state. The snippets disagree on Cox vs marked exponential Hawkes. No multi-contract estimate |
| R11 | (authors not seen) *Liquidity Provision and Rebate Design in Option Markets.* arXiv 2609.26606 | https://arxiv.org/pdf/2609.26606 | Yes (Sep 2026) | C | **Adjacent (weak)** | Multi-option MM with delta and vega bounds; Hawkes flow not confirmed |

**Owned works re-found** (not counted as new): Barzykin 2026b, Acero 2026, Jusselin 2021, Jain 2025,
Khabou–Talbi 2025, Martin–Tse 2026, Bielecki et al. 2026, Abi Jaber–Neuman 2025, Abi Jaber–Miller–Pham
2021 (LQ Volterra), Alfonsi–Blanc 2016, Yang 2026, Moret 2026, Gennaro 2026, Feil 2026, Guo 2025,
Kumar 2024, Gašperov 2022, Lai 2023, Wang 2024, Bacry 2015/2016, Muhle-Karbe 2026, Chávez-Casillas 2024.

---

## Verdict

| Gap part | Verdict | By whom / why |
|---|---|---|
| **(1)** A predictive second-order regret law for a market maker fed a mis-specified intensity forecast, $r \approx \tfrac12\,\mathbb E\iint K\,\Delta m\,\Delta m$ | **OPEN** | No hit states a second-order law in a forecast error for market making. The nearest are misspecification-cost results in **execution**: Hey et al. 2023 (R2; asymmetric, so not a symmetric quadratic law on the snippet's evidence) and Chen et al. 2022 (R3). The owned bounds are first-order or sqrt-type, not predictive: Acero Thm 1 (√L²) and Abi Jaber–Miller–Pham (L² kernel error) |
| **(2)** Reward/regret vs p on a power-law / slowly decaying truth, with the control-approximation error separated and an exact or near-exact reference | **NARROWED, not closed.** By Abi Jaber–Bondi–De Carvalho–Neuman–Tuschmann 2025 (R1) for **propagator / execution**; already narrowed by Jusselin 2021 Fig. 4 (owned, value of the lifted model vs n) | R1 is the closest object found: optimal P&L vs the number of exponential time scales on a power-law and a shifted power-law kernel, against a general-kernel reference. It differs from the gap: no Hawkes order flow, no market making, no forecast object m_t(u), and nothing visible that separates control-approximation error from memory error. For Hawkes-flow **market making, (2) stays OPEN.** R4 (Uniswap) is a further execution data point |
| **(3)** A map of when memory is irrelevant | **OPEN** for market making; weakly narrowed for execution | R1's rule of thumb (2 / 3 / 5 exponentials depending on shift) and R4's "one term suffices" are point statements in execution problems, not maps over (b, ρ, regime). Acero's "tie" regime (owned) is still the only MM evidence |

### Task 2 stop-rule answer

> *Does any source report regret/reward vs p on a power-law kernel with an exact or near-exact
> reference **and** a second-order law?*

**No.** No source found meets both conditions. The single source that comes near the first condition
is R1 (Abi Jaber et al. 2025), in an optimal-execution / propagator problem. It reports P&L vs the number
of exponentials on a power-law kernel against a general-kernel reference, but has no second-order law
and no Hawkes-flow market making. **The gap is not CLOSED; the stop rule does not trigger.** Before the
novelty claim is written, two things are needed: (i) a full read of R1 (does its sweep measure the
regret of the p-exponential *policy* on the *true* kernel, and how exact is the Fredholm reference?),
and (ii) a full read of R5 (TechRxiv, kernel-misspecification robustness). R1 must be cited in the
related-work section as the execution-side precedent for (2) and (3).

---

## Not reachable / not conclusive

- **No direct database access.** OpenAlex, arXiv API, Crossref and Semantic Scholar API: `connect_rejected` at the proxy. **OpenAlex and Crossref were in effect not searched:** their domain-restricted WebSearch calls returned 0 on-domain results. **Google Scholar** returned only lookup or profile pages, never a "cited by" list. **SSRN** and **Semantic Scholar** filters leaked, with 1–4 on-domain results per query. Recall for SSRN-only working papers and for non-arXiv journal articles is therefore **unknown**, and probably lower than the protocol intends.
- **No full text or abstract page opened.** WebFetch failed with DNS errors for arxiv.org and techrxiv.org. All classifications rest on search snippets. The R1 and R5 verdicts depend on content the snippets only partly show.
- **No arXiv category filter.** q-fin.TR/CP, math.OC and stat.AP were targeted through wording only (e.g. A19), not through category restriction.
- **No date filter.** The cut-off (2026-10-29) was checked by hand from arXiv IDs and listings. For R9 (arXiv 2610.23619) the exact posting day could not be seen. Its verdict (adjacent) does not depend on it.
- **Forward citations are incomplete.** Barzykin 2026b (Aug 2026) and Acero 2026 (Oct 2026) are too recent for indexed citers, and none were found. For Jusselin 2021, Google Scholar reports 29 citations, but the list could not be opened, and only the citers that surfaced in snippets were checked. For Lai 2023, only 2–3 citers surfaced.
- **Unresolved items:**
  - R5 (TechRxiv): title truncated, authors unknown.
  - arXiv 2610.24558v1, "Optimal Trading Filters and the Value of Predictive Signals": an arXiv-domain result, but a title lookup found nothing, so content was not assessed. Its title (value of predictive signals vs filter design) suggests possible relevance to (1) and (3); **check when arXiv is reachable**.
  - The Springer chapter "Computational Methods for Market Making Algorithms" (Jusselin citer): content not visible.
- **Fix:** allow `api.openalex.org`, `export.arxiv.org`, `api.crossref.org`, `api.semanticscholar.org` and `arxiv.org` in the session's network settings. Then re-run blocks A–D with the same query strings against the real APIs and diff the hit lists against this log.
