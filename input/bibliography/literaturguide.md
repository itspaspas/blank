# Literature guide: Phase 1 supplementary search (plan Task 6, design Q6)

Project: `hawkes-multi-asset-mm` · Search date: 2026-10-25 · Audit: `audit-log-2026-10-25.json`.
Scope (fixed by the design): English-language quantitative finance and adjacent applied
probability, control and operations research; all years, emphasis 2013–2026. Two scouts searched
OpenAlex, arXiv, Crossref and HAL, plus forward citations of the core papers. Semantic Scholar
(HTTP 429) and SSRN (bot-blocked) could not be used.

This guide adds to the 78-entry library. The 8 core works and the 59 un-ingested library works
are not repeated in the table; see `library-inventory.md`.

## 1. Source table (weighted)

| Grade | Author Year | Short title | OA/Access | DOI/Link |
|-------|------------|-----------|-----------|----------|
| A | Aït-Sahalia 2016 | portfolio-choice-markets | ✓ OA (arXiv 1210.1598) | [10.1093/jjfinec/nbv024](https://doi.org/10.1093/jjfinec/nbv024) |
| A | Bathini 2026 | dynamic-market-making | ◐ SSRN (manual) | [10.2139/ssrn.7625720](https://doi.org/10.2139/ssrn.7625720) |
| A | Cartea 2018 | algorithmic-trading-stochastic | ◐ UB (SIAM Review) | [10.1137/18M1176968](https://doi.org/10.1137/18M1176968) |
| A | Fujii 2015 | optimal-position-management | ✓ OA (arXiv 1503.07007) | [10.2139/ssrn.2584430](https://doi.org/10.2139/ssrn.2584430) |
| A | Shen 2022 | mean-variance-portfolio | ✓ OA (arXiv 2110.09417) | [10.1137/20M1320560](https://doi.org/10.1137/20M1320560) |
| A | Yuan 2026 | dynamic-pricing-self | ○ paywalled (Operations Research) | [10.1287/opre.2024.1172](https://doi.org/10.1287/opre.2024.1172) |
| A | Zarezade 2018 | steering-social-activity | ✓ OA (arXiv 1802.07244) | [arXiv:1802.07244](https://arxiv.org/abs/1802.07244) |
| B | Abi Jaber 2021 | integral-operator-riccati | ✓ OA (arXiv 1911.01903) | [10.1137/19M1298287](https://doi.org/10.1137/19M1298287) |
| B | Abi Jaber 2021 | linear-quadratic-control | ✓ OA (arXiv 1911.01900) | [10.1214/20-AAP1645](https://doi.org/10.1214/20-AAP1645) |
| B | Abi Jaber 2025 | optimal-liquidation-signals | ✓ OA (arXiv 2211.00447) | [10.1111/mafi.12465](https://doi.org/10.1111/mafi.12465) |
| B | Alfonsi 2016 | dynamic-optimal-execution | ✓ OA (arXiv 1404.0648) | [10.1007/s00780-015-0282-y](https://doi.org/10.1007/s00780-015-0282-y) |
| B | Alfonsi 2016 | extension-calibration-hawkes | ✓ OA (arXiv 1506.08740) | [10.1142/S2382626616500052](https://doi.org/10.1142/S2382626616500052) |
| B | Bensoussan 2024 | stochastic-control-diffusions | ✓ OA (AIMS) | [10.3934/mcrf.2024038](https://doi.org/10.3934/mcrf.2024038) |
| B | Bo 2016 | optimal-investment-credit | ◐ UB / SSRN | [10.1111/mafi.12074](https://doi.org/10.1111/mafi.12074) |
| B | Bo 2019 | credit-portfolio-selection | ◐ UB (Wiley) | [10.1111/mafi.12177](https://doi.org/10.1111/mafi.12177) |
| B | Branger 2014 | partial-information-contagion | ◐ UB (econstor served HTML) | [10.1016/j.jedc.2013.10.005](https://doi.org/10.1016/j.jedc.2013.10.005) |
| B | Ceci 2025 | optimal-reinsurance-dynamic | ✓ OA (arXiv 2404.11482) | [10.1080/14697688.2025.2488450](https://doi.org/10.1080/14697688.2025.2488450) |
| B | Chehrazi 2019 | dynamic-credit-collections | ◐ UB (INFORMS) | [10.1287/mnsc.2018.3070](https://doi.org/10.1287/mnsc.2018.3070) |
| B | Chen 2026 | optimal-trade-execution | ✓ OA (LMU repository discussion paper) | [10.1287/opre.2023.0151](https://doi.org/10.1287/opre.2023.0151) |
| B | Duffie 2000 | transform-analysis-asset | ◐ UB (JSTOR) | [10.1111/1468-0262.00164](https://doi.org/10.1111/1468-0262.00164) |
| B | Errais 2010 | affine-point-processes | ◐ UB / SSRN 908045 | [10.1137/090771272](https://doi.org/10.1137/090771272) |
| B | Fu 2022 | portfolio-liquidation-games | ✓ OA (arXiv 2011.05589) | [10.1111/mafi.12359](https://doi.org/10.1111/mafi.12359) |
| B | Gennaro 2026 | signature-methods-optimal | ✓ OA (arXiv 2606.19772) | [arXiv:2606.19772](https://arxiv.org/abs/2606.19772) |
| B | Li 2002 | indefinite-stochastic-lq | ✓ OA (International Press) | [10.4310/CIS.2002.v2.n3.a4](https://doi.org/10.4310/CIS.2002.v2.n3.a4) |
| B | Lim 2026 | liquidation-aware-market | ◐ SSRN (manual) | [10.2139/ssrn.6847019](https://doi.org/10.2139/ssrn.6847019) |
| B | Lucic 2024 | optimal-option-market | ◐ SSRN (manual) | [10.2139/ssrn.4729290](https://doi.org/10.2139/ssrn.4729290) |
| B | Sharma 2026 | structural-hawkes-ambiguity | ◐ SSRN (manual) | [10.2139/ssrn.6777719](https://doi.org/10.2139/ssrn.6777719) |
| B | Zhang 2020 | backward-stochastic-riccati | ✓ OA (arXiv 1808.08336) | [10.1137/18M1209684](https://doi.org/10.1137/18M1209684) |
| B | Zimmer 2025 | reinforcement-learning-based | ✓ OA (arXiv 2509.12456) | [arXiv:2509.12456](https://arxiv.org/abs/2509.12456) |
| C | Liu 2003 | dynamic-asset-allocation | ◐ UB / NBER w9103 | [10.1111/1540-6261.00523](https://doi.org/10.1111/1540-6261.00523) |
| C | Cayé 2016 | liquidation-self-exciting | ◐ UB / SSRN | [10.1007/s11579-015-0148-2](https://doi.org/10.1007/s11579-015-0148-2) |
| C | Lu 2018 | modelisation-carnet-ordres (thesis, French) | ✓ OA (HAL) | [tel-01893379](https://theses.hal.science/tel-01893379/document) |
| C | Lu 2019 | order-book-modeling | ✓ OA (arXiv 1806.05101) | [10.1142/S2382626619500035](https://doi.org/10.1142/S2382626619500035) |
| C | Swishchuk 2021 | merton-investment-problems | ✓ OA (MDPI) | [10.3390/risks9060108](https://doi.org/10.3390/risks9060108) |
| C | Roldan-Contreras 2022 | optimal-liquidation-acquisition | ✓ OA (MDPI) | [10.3390/risks10080160](https://doi.org/10.3390/risks10080160) |
| C | Jerome 2023 | mbt-gym | ◐ UB (ACM) | [10.1145/3604237.3626873](https://doi.org/10.1145/3604237.3626873) |
| C | Ragel 2024 | methodes-apprentissage-renforcement (thesis, French) | ✓ OA (HAL) | [tel-04913317](https://theses.hal.science/tel-04913317v1) |
| C | Lalor 2025 | reinforcement-learning-non | ✓ OA (arXiv 2410.14504) | [10.3390/risks13030040](https://doi.org/10.3390/risks13030040) |
| C | Lalor 2025 | event-based-limit | ✓ OA (arXiv 2502.17417) | [10.1080/1350486X.2025.2548448](https://doi.org/10.1080/1350486X.2025.2548448) |
| C | Lalor 2025 | algorithmic-high-frequency | ✓ OA (arXiv 2409.12776) | [10.1080/14697688.2025.2541007](https://doi.org/10.1080/14697688.2025.2541007) |
| C | Tiwari 2025 | optimal-execution-self (grey literature) | ✗ (SSRN/TechRxiv blocked) | [10.2139/ssrn.5775204](https://doi.org/10.2139/ssrn.5775204) |
| C | Aubert 2026 | optimal-dividend-capital | ✓ OA (arXiv 2511.19701) | [10.1007/s00245-026-10464-6](https://doi.org/10.1007/s00245-026-10464-6) |
| C | Aubert 2026 | option-market-making | ✓ OA (arXiv 2511.02518) | [10.1080/1350486X.2026.2671725](https://doi.org/10.1080/1350486X.2026.2671725) |
| C | Chatziandreou 2026 | optimal-execution-intraday | ✓ OA (arXiv 2504.10282) | [10.1080/14697688.2025.2597415](https://doi.org/10.1080/14697688.2025.2597415) |
| C | Dro 2026 | optimal-merton-problem | ✓ OA (arXiv 2605.00688) | [arXiv:2605.00688](https://arxiv.org/abs/2605.00688) |
| C | Eyjolfsson 2026 | stochastic-control-self | ✓ OA (arXiv 2605.12035) | [arXiv:2605.12035](https://arxiv.org/abs/2605.12035) |

Legend. **Grade:** A core / must-read for Q6, or the decisive test of a claim; B supporting
(solution machinery, partial comparisons); C context. **OA/Access:** ● library · ✓ OA
(auto-downloadable) · ◐ UB (university licence or SSRN, manual) · ○ paywalled, manual · ✗ no copy
located. A+B BibTeX (29 entries, verified against Crossref/arXiv) is in `library/references.bib` and
`output/bibtex/references.bib`. C items are listed here only.

## 2. Research question for this search

Q6 of the design: has anyone, since or outside the proposal's 75-paper search, extended the
multi-asset closed form to Hawkes (or other self-/mutually exciting) flow? Is there a three-way
comparison (closed form, exact, learned) on one Hawkes problem? The problem anatomy
(`knowledge/synthesis/problem-anatomy.md`) added two targets:
- **D1:** the exact GLFT linearisation survives when only the maker's own fills excite the flow;
- **D2:** under flow-driven excitation, the quadratic-in-inventory value function has coefficients
  that depend on the intensity and solve a nonlocal transport-jump Riccati system.

## 3. Verdicts

| Claim | Verdict | Evidence |
|---|---|---|
| (1) No closed form for multi-asset market making with cross-asset Hawkes flow | **Not refuted; wording to be sharpened** | No hit in either scout. Nearest: Fujii 2015, a multi-security dealer whose stochastic HJB reduces to a backward stochastic Riccati equation, but with generic exogenous flow processes, no quote-controlled point process (abstract checked); Shen 2022, cross-asset mutually exciting jumps with a semi-closed LQ solution, but in portfolio selection. Proposed wording: *"no closed form for multi-asset market making in which fills arrive as point processes controlled by the quotes and driven by cross-asset Hawkes intensities"* |
| (2) No three-way comparison on one Hawkes problem | **Not refuted** | Partial pairs only: Barzykin 2026 (closed form vs exact, owned), Bathini 2026 (Hawkes HJB vs GLFT vs AS, empirical, not read), Gennaro 2026 and Zimmer 2025 (learned vs closed form, not under Hawkes). Boyce 2025 (owned) does all three but under Poisson flow, so it is a template, not a refutation |
| D1: fill-driven CARA linearisation | **Not found; one decisive lead** | No CARA plus fill-driven Hawkes paper uses an exponential transform. Lead: Yuan 2026 (*Operations Research*), dynamic pricing where each sale excites future demand, exactly the fill-driven convention. The scout's own sketch shows the risk-neutral analogue linearises (Gallego–van Ryzin trick). **Read the full text before claiming novelty.** |
| D2: intensity-dependent Riccati coefficients | **Known in structure, outside market making** | Shen 2022: value quadratic in the state, coefficient a function of a multivariate Hawkes intensity solving a nonlocal PDE; «U has a non-local dependence on g … which originates from the mutual-excitation feature of the Hawkes process» (p. 17 of arXiv version, checked) and «a non-local component remains an open question» (checked). The d×d inventory-matrix version produced by a market-making Hamiltonian was not found |

## 4. Primary sources and the debate they shape

- **Market-making core (owned, ingested):** GLFT 2013, BEGV 2021, CJR 2014, Jusselin 2021, Barzykin
  2026, Bergault et al. 2024, Martin–Tse 2026, Acero et al. 2026. Forward citations of BEGV (20)
  and Jusselin (9) were screened in full; of GLFT (203) and CJR 2014 (197) by keyword. They yielded
  no multi-asset Hawkes closed form.
- **Single-asset Hawkes market making since the proposal's search:** Lim 2026 (perpetuals,
  bivariate marked Hawkes, exit cost quadratic in inventory and linear in intensity), Sharma 2026
  (robustness: a branching-matrix error amplified through $(I-\Gamma)^{-1}$ near criticality),
  Bathini 2026 (Hawkes HJB vs GLFT vs AS on Binance data). All three are SSRN-only and unread.
  Cartea–Jaimungal–Ricci 2018 (SIAM Review) is the SIGEST version of CJR 2014 with a new follow-up
  section, the version Barzykin and Martin–Tse cite.

## 5. Methods map: where the needed machinery lives

| Machinery | Where | Use for the project |
|---|---|---|
| Quadratic value with λ-dependent coefficients, nonlocal PDE, multivariate mutual excitation | Shen 2022 | the template for D2 and §5 of the problem anatomy |
| CARA separation $-e^{-\gamma x}g(\lambda)$ with the ratio $g(\lambda+d_l)/g(\lambda)$ | Aït-Sahalia 2016; Ceci 2025 | confirms the flow-driven nonlinearity of §3b (GLFT side) |
| Quadratic form jointly in state and intensities, ODE coefficients | Alfonsi 2016 (both) | when cost and intensity are affine; differs from D2, where $\lambda_j$ multiplies the Hamiltonian |
| Matrix Riccati with controlled multivariate Hawkes | Zarezade 2018 | the closest "Riccati + controlled mutual excitation" result (social networks) |
| Riccati ODEs for transforms of self/cross-exciting point processes | Errais 2010; Duffie 2000 | frozen-forecast and Feynman–Kac steps; moments of the forecast (covariance correction) |
| Lift plus operator Riccati with convergence of finite-dimensional approximations | Abi Jaber 2021 (×2), 2025 | the E0 step (lift truncation) with a rigorous error theory |
| Coupled Riccati over finite regimes | Li 2002 | the discrete analogue of D2; the MMPP escape route of Bergault et al. 2024 |
| Own actions feed the intensity (fill-driven analogues) | Chen 2026; Fu 2022; Chehrazi 2019; Yuan 2026 | evidence and machinery for D1 |
| Backward stochastic Riccati equations | Fujii 2015; Zhang 2020 | the multi-asset dealer route without point-process fills |

## 6. Open access and acquisition

- **Auto-downloadable (✓ OA):** 15 A+B items via arXiv or a repository; `acquire-sources` fetches
  them. Under the preprint policy these are non-core, so the arXiv versions are accepted.
- **Manual (◐/○):**
  - SSRN-only: Bathini, Lim, Sharma, Lucic. SSRN blocks bots; downloading in a browser usually works.
  - Paywalled: Yuan 2026 (OR), Cartea 2018 (SIAM Review), Bo 2016/2019, Branger 2014, Chehrazi 2019, Errais 2010, Duffie 2000.
- **Highest-value manual download: Yuan 2026.** It alone settles D1.

## 7. Gaps

1. The core gap claim survives a search aimed at refuting it, with sharper wording (§3).
2. **Only one closed-form-vs-exact Hawkes comparison exists** (Barzykin, single asset). No paper
   measures the Hamiltonian-expansion error and the forecast-freezing error separately.
3. **D2 in market making** (a d×d inventory matrix $A(t,\lambda)$) is unpublished as far as found;
   Shen 2022 calls the numerics of its scalar analogue an open question.
4. **D1** awaits Yuan 2026.
5. No thesis on multi-asset Hawkes market making was found. HAL theses (Lu 2018, Ragel 2024) and
   Jusselin's 2020 thesis (not reachable) are single-asset or RL.

## 8. Recommended reading order

1. Shen 2022, the closest mathematical template (D2, cross-asset excitation).
2. Yuan 2026, the D1 test (needs manual download).
3. Fujii 2015, the multi-security dealer Riccati (gap wording).
4. Aït-Sahalia 2016, CARA with mutually exciting jumps (the flow-driven ratio nonlinearity).
5. Bathini 2026, the closest comparison study.
6. Alfonsi 2016 and Zarezade 2018, worked Riccati closed forms with Hawkes intensities.
7. Abi Jaber 2021/2025 and Errais 2010, as needed for the lift and the forecast.
8. Cartea 2018, Lim 2026, Sharma 2026, for single-asset completeness.

## 9. Follow-up searches

- Retry Semantic Scholar (forward citations of Shen 2022, Aït-Sahalia 2016, Fujii 2015).
- Forward citations of Shen 2022 and Zarezade 2018, for any market-making use of their machinery.
- Jusselin's PhD thesis (HAL tel-02926102): does it contain a CARA variant of his fill-driven model (D1)?
- Revenue-management and queueing literature on self-exciting demand under exponential transforms (D1).
- Re-run the gap query after the remaining library batches (Task 8). The un-ingested library may
  hold relevant multi-asset work, e.g. Barzykin et al. multi-currency and Rosenbaum–Zhang.

## 10. BibTeX overview

29 A+B entries added on 2026-10-25 to `library/references.bib` (now 107 entries) and
`output/bibtex/references.bib` (37 entries), each with the note "Literature search 2026-10-25
(plan Task 6), grade X; not yet acquired". Keys follow the library rule; volume year replaced
Crossref's online-first year for Aït-Sahalia 2016, Alfonsi 2016, Bo 2016 and Bo 2019. Metadata
source: `library-build/literature_ab.json`.
