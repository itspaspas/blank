---
title: "Wiki Log"
type: synthesis
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
---

# Wiki log

Append-only. See CLAUDE.md § Meta files.

## [2026-10-25] meta | project start
- Design approved: `input/ideas/hawkes-multi-asset-mm-design.md`
- Plan ready: `input/ideas/hawkes-multi-asset-mm-plan.md` (Phase 1, hermeneutic sub-study of a `mixed` project)
- `.research-library` → `./library`

## [2026-10-25] inventory | plan Task 1 (partial)
- 71 PDFs identified from title pages → 4 exact duplicate pairs → 67 unique works: `input/bibliography/library-inventory.md`
- Correction to the plan: suspected duplicate `arXiv_2106.06974` ↔ BEGV was wrong. BEGV is arXiv 1810.04383v5; 2106.06974 is Barzykin–Bergault–Guéant (hedging).
- All works on disk are preprints. Published versions are recorded per work for later verification.
- Not done: network verification of metadata (arXiv / Crossref). Shell and web calls failed on a transient tool-permission check this session.

- 2026-10-25 · deviation · plan=hawkes-multi-asset-mm · ingest batches extended from B2–B7 to B2–B8. B8 holds 6 peripheral `map` works so that no batch exceeds 10. No change to scope.

## [2026-10-25] meta | plan Task 0 done (scaffold)
- Template copied without overwriting anything. CLAUDE.md patched: methodology `mixed`, discipline, `[en]`, plugin 0.41.1, ingest-depth list, notation and Model card conventions. Example pages removed. Project registered.
- PyYAML installed (needed by lint-wiki.py and wiki-global-graph.py).

## [2026-10-25] library | plan Tasks 1–2 done (inventory verified, library built)
- 67 unique works verified against the arXiv API and Crossref. 14 provisional bibkeys changed year to the journal year; see `input/bibliography/library-inventory.md`.
- `library/pdf/<bibkey>.pdf` × 67 (copies; originals untouched). `library/references.bib`: 67 entries, each noting the preprint version read.
- Full-text index: 67 documents, 2,022 pages. Cross-project bibkey audit: 0 collisions, 0 splits.
- Proposal references: 24 of 35 on disk, 11 missing → plan Task 3.
- Correction: the inventory's first draft attributed BEGV to SIFIN "per proposal". That was wrong; the proposal correctly cites *Applied Mathematical Finance* 28(2), 2021.
- Open: the surname split for Nittur Anantha (`anantha-2025-event-time-anchor`); whether Guo–Jin–Nam 2023 = *Mathematical Finance* 2025 "Macroscopic Market Making Games".

## [2026-10-25] acquire | plan Task 3: proposal references missing from library
- Worklist: 11 (proposal §8 refs not on disk; no `literaturguide.md` yet, so graded from the proposal: 9 A, 2 B)
- Downloaded 1 (Schulman 2017, an arXiv-native original); manual 7; 3 published works staged as arXiv preprints in `library/preprint-candidates/` pending the preprint policy (Bacry 2015, Bacry 2016, Cheridito 2025)
- Manual worklist: `input/bibliography/acquisition-todo.md` (7 items + 3 awaiting decision)
- Audit: input/bibliography/acquisition-log-2026-10-25.json
- `library/references.bib`: +11 entries (78 total)
- optimize-pdf scan not run: Ghostscript not installed. New files are 0.9–2.9 MB, so there is no bloat concern.
- bib-search re-indexed (+1 document)

## [2026-10-25] meta | preprint policy decided (user)
- Core works (B1): published original required. Other works: the preprint on disk is accepted, and the source page records the version read. Written to CLAUDE.md § Preprint policy.
- The preprints of the 4 published core works (GLFT 2013, BEGV 2021, CJR 2014, Jusselin 2021) were moved to `library/preprints/`; their originals are on the manual worklist (priority section).
- The 3 staged preprints (Bacry 2015, Bacry 2016, Cheridito 2025) were promoted to `library/pdf/`. `library/pdf/` now holds 67 PDFs (plus 4 core preprints in `library/preprints/`); 11 manual downloads are open.
- Consequence for plan Task 4: the B1 ingest runs now for the 4 preprint-only core works (Barzykin 2026b, Bergault et al. 2024, Martin–Tse 2026, Acero et al. 2026). The other 4 are blocked until their originals are on disk.

## [2026-10-25] ingest | B1 core batch, part 1 (4 of 8, depth deep)
- 2026-10-25 · ingest · [[barzykin-2026-hawkes-driven-otc]] · focus: «closure + multi-asset» (30 Kernthesen)
- 2026-10-25 · ingest · [[bergault-2024-price-aware-automated]] · focus: «closure + multi-asset» (25 Kernthesen)
- 2026-10-25 · ingest · [[martin-2026-market-making-hawkes]] · focus: «closure + multi-asset» (28 Kernthesen)
- 2026-10-25 · ingest · [[acero-2026-hawkes-structured-networks]] · focus: «closure + multi-asset» (29 Kernthesen)
- Full focus string: «How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation.»
- Process: 4 parallel source-ingester agents, each writing only its own page. Concept and model pages (9 + 4) filled in the main context from the agents' reports. BibTeX keywords added to `library/references.bib`; `output/bibtex/references.bib` regenerated by bib-subset (4 entries).
- Review (hermeneutic synthesis review): spot-checked the central claims against the PDFs via bib-search/pdftotext. All confirmed: Barzykin p. 8 "transport-jump … not a small Riccati system"; Table 3 regrets (0.080/0.083/0.170 % vs 6.138/12.742/27.312 %); Poisson comparator uses baseline intensity. Bergault et al. p. 17 "inadequate"; fn. 8 p. 11. Martin–Tse p. 16 cross-excitation as future work. Acero et al. p. 2 "Similar results extend to the multi-asset case"; p. 5 ρ = 0.40.
- Blocked: GLFT 2013, BEGV 2021, CJR 2014, Jusselin 2021 (originals on the manual worklist).
- Candidate pages proposed by the agents, not created (create when a second source needs them): markov-modulated-poisson-process, mercer-expansion, hawkes-structured-network, request-vs-fill-excitation.
- Lint: 0 issues.

## [2026-10-25] ingest | B1 core batch, part 2 (4 of 8, depth deep): Task 4 complete
- Acquired by user: published originals of GLFT 2013, BEGV 2021, CJR 2014 (journal headers verified on p. 1). Jusselin 2021: SIAM blocked user and bot (HTTP 403); the user approved the arXiv 2003.05958v2 preprint as substitute.
- 2026-10-25 · ingest · [[gueant-2013-dealing-inventory-risk]] · focus: «closure + multi-asset» (26 Kernthesen)
- 2026-10-25 · ingest · [[bergault-2021-closed-form-approximations]] · focus: «closure + multi-asset» (25 Kernthesen)
- 2026-10-25 · ingest · [[cartea-2014-buy-low-sell]] · focus: «closure + multi-asset» (30 Kernthesen)
- 2026-10-25 · ingest · [[jusselin-2021-persistent-order-flow]] · based_on: preprint (user-approved substitute) · focus: «closure + multi-asset» (24 Kernthesen)
- Spot checks against the PDFs, all confirmed:
  - BEGV: tanh solution (eq. 13); «A natural choice» (Remark 1); commutation used for B
  - GLFT: Figs. 1–3 parameters σ = 0.3, A = 0.9, k = 0.3, γ = 0.01, T = 600 = proposal benchmark
  - CJR: expansion «correct to o(ς) where ς = max(φ, α, E[ε])» (p. 427)
  - Jusselin: «one market maker» (pp. 1–2); dimension 2n+2, finite differences «very unlikely» for n > 2 (p. 11)
- Pages:
  - rewritten: [[glft-2013-model]], [[begv-2021-model]], [[cartea-jaimungal-ricci-model]], [[matrix-riccati-equation]] (notation fix: BEGV's D₊ vs Γ)
  - new: [[who-excites-the-flow]]
  - extended: markov-lift, hawkes-process, branching-matrix, intensity-forecast, hamiltonian-quadratic-approximation, shadow-price, regret
- Corrections to earlier pages:
  - the CJR expansion parameter is max(φ, α, E[ε]), not the inventory penalty alone
  - the CJR closure is linear ODEs, not Riccati
- New finding (inference, not stated by any source; flagged on the page): the GLFT exact closure survives fill-driven excitation and breaks under flow-driven excitation; the BEGV quadratic closure behaves the other way round. To be verified in full in the problem-anatomy synthesis (Task 5).
- Bib: keywords for 4 sources; output/bibtex/references.bib regenerated (8 entries). Lint: 0 issues.

## [2026-10-25] synthesis | plan Task 5: problem-anatomy, first pass
- Synthesis created: [[problem-anatomy]] (status: draft), answering Q1–Q3 from the 8 core sources.
- Main results, each tagged [S] stated / [D] derived here / [I] inference:
  - Three closures close for different reasons: GLFT exact linearisation; BEGV quadratic Hamiltonian plus Riccati; CJR first-order expansion plus linear ODEs.
  - [D] Flow-driven excitation (the proposal's convention): the quadratic ansatz closes in q, but A, B, C solve a nonlocal transport-jump Riccati system in λ. This is consistent with Barzykin p. 8 and proposal p. 19.
  - [D] Fill-driven excitation: the quadratic route fails (Bergault et al. p. 17), while the GLFT exact linearisation survives. The flow-driven half of this is also stated in proposal p. 18.
  - Error anatomy E0 (lift), E1 (Hamiltonian expansion), E2 (forecast freezing) mapped to hypothesis H3.
  - [I] Prediction for H2: in the frozen-forecast closed form, cross-asset excitation reaches other assets only through the diagonal D₊(t) and Σ-coupling.
- Synthesis review (hermeneutic): central citations re-checked against sources (Barzykin p. 8; proposal pp. 18, 19, 21; BEGV p. 113; Bergault et al. p. 17). [D] items still need independent re-derivation before use (proposal p. 21).
- New Q6 search items: is a fill-driven CARA linearisation known? Is any multi-asset Hawkes Riccati system published?

## [2026-10-25] literature | plan Task 6: supplementary search (Q6, D1, D2)
- Guide: `input/bibliography/literaturguide.md` (weighted table, verdicts, methods map, reading order). Audit: `input/bibliography/audit-log-2026-10-25.json`.
- Library first (bib-search): no new owned source on the gap. Then two literature scouts at high effort (OpenAlex, arXiv, Crossref, HAL; forward citations of BEGV, Jusselin, CJR, GLFT).
- Result: 46 new candidates after dedup (A 7, B 22, C 17). 29 A+B entries verified via Crossref/arXiv and added to library/references.bib (now 107) and output/bibtex/references.bib.
- Verdicts:
  - gap (1), multi-asset Hawkes closed form: **not refuted**; wording to sharpen (Fujii 2015 multi-security BSRDE without point-process fills; Shen 2022 cross-asset Hawkes LQ in portfolio selection)
  - gap (2), three-way comparison: **not refuted**
  - D1: not found; decisive lead Yuan 2026 (OR, paywalled)
  - D2: structure known outside market making (Shen 2022, quotes checked)
- Main-session checks: Shen 2022 and Zarezade 2018 quotes in full text; Fujii 2015 abstract; Acero cs = 0.7 vs 0.28 reconciled (note added to the source page).
- Gate: ≥15 A/B sources yes (29); guide with weighted table yes; bib updated yes; log yes.

## [2026-10-25] acquire | plan Task 7 (run 2): user downloads reconciled, OA set fetched
- User-added files renamed to bibkeys after title-page checks:
  - published: avellaneda-2008, ho-1981 (scan with OCR layer), hawkes-1971 (JSTOR), lai-2023, cartea-2018 (SIAM Review)
  - thesis: tarditi-2026
  - preprints: bathini-2026 (SSRN), yuan-2026 (author preprint, not the OR version; non-core, accepted)
- Rejected: the Cartea–Jaimungal–Penalva book. The PDF is damaged (invalid XRef, /Pages object; pdftotext, pypdf and rendering all fail); moved to library/damaged/ and back on the manual worklist.
- Downloaded and validated 15 OA copies (arXiv and LMU repository) for the A+B set.
- Manual worklist: 14 items (book, Jusselin original, 11 A+B without OA, Ogata). Audit: input/bibliography/acquisition-log-2026-10-25-run2.json. bib-search re-indexed (+23 documents).
- Task 7 status: done, except user-only manual downloads.

## [2026-10-25] ingest | plan Task 8 started: 86 PDFs without a source page
- Brief for all agents: scratchpad `ingest-brief-task8.md` (same focus string; standard depth unless map; agents write only their own pages).
- Cost-saving layout: 2 standard sources per agent; 4 map sources per agent; 5 waves of 8 agents; gap-relevant first.
- Wave 1 (DISPATCHED 2026-10-25, running): shen-2022+aitsahalia-2016 · fujii-2015+zarezade-2018 · yuan-2026+chen-2026 · bathini-2026+tarditi-2026 · cartea-2018+choi-2021 · lai-2023+kumar-2024 · jain-2025+gasperov-2022 · khabou-2025+bielecki-2026
- Wave 2 (DISPATCHED 2026-10-25, running): sakhanda-2026+ceci-2025 · alfonsi-2016-dynamic+alfonsi-2016-extension · fu-2022+abijaber-2025 · abijaber-2021-linear+abijaber-2021-integral · zhang-2020+drissi-2022 · yang-2026+wang-2024 · barzykin-2026-dynamic-slippage+barzykin-2026-strategic-otc · barzykin-2026-win-score+barzykin-2026-bond
- Wave 3 (planned): barzykin-2022-multi-currency+barzykin-2021-market-making-fx · barzykin-2022-algorithmic+barzykin-2025-fx · barzykin-2025-optimal-quoting+barzykin-2026-market-making-transient · bergault-2020+bergault-2023 · gueant-2017+gueant-2019 · rosenbaum-2022+boyce-2025 · avellaneda-2008+ho-1981 · bacry-2015+bacry-2016
- Wave 4 (planned): muhlekarbe-2026+lee-2026 · cheridito-2025+gennaro-2026 · zimmer-2025+moret-2026 · jafree-2025+ochedzan-2026 · guilbaud-2011+fodra-2013 · fodra-2015+campi-2020 · guo-2023+guo-2025 · baldacci-2023+pulido-2026
- Wave 5 (planned): chavezcasillas-2024+gao-2020 · lehalle-2017+law-2019 · cao-2026+albers-2025 · anantha-2025+barucci-2025 · niang-2026+cotton-2026 · MAP hawkes-1971+schulman-2017+capponi-2021+fermanian-2016 · MAP gueant-2018+marinmartinez-2026+feil-2026+wu-2026 · MAP ma-2025+jiang-2025+asadulaev-2026+kleitsikas-2025
- After each wave: merge keywords into library/references.bib, bib-subset, concept/entity/index updates, spot checks, lint.
- Wave 1 status: 7/8 reports in (cartea-2018+choi-2021 still running). Main-session checks: Yuan p. 12 «does not have close-form solutions» and Lemma 3 p. 21 (non-buyers exciting equally → constant optimal intensity) confirmed. based_on: preprint added to 6 preprint-read pages after lint PAGE-OUT-OF-RANGE; CLAUDE.md preprint policy and ingest brief updated accordingly. Report data staged in scratchpad task8-merge.tsv for the wave merge.

## [2026-10-25] ingest | plan Task 8, wave 1 merged (16 sources, standard)
- 2026-10-25 · ingest · [[shen-2022-mean-variance-portfolio]], [[aitsahalia-2016-portfolio-choice-markets]], [[fujii-2015-optimal-position-management]], [[zarezade-2018-steering-social-activity]], [[yuan-2026-dynamic-pricing-self]], [[chen-2026-optimal-trade-execution]], [[bathini-2026-dynamic-market-making]], [[tarditi-2026-hawkes-process-models]], [[cartea-2018-algorithmic-trading-stochastic]], [[choi-2021-synchronised-order-arrivals]], [[lai-2023-data-driven-deep]], [[kumar-2024-deep-hawkes-process]], [[jain-2025-impulse-control-hawkes]], [[gasperov-2022-deep-reinforcement-learning]], [[khabou-2025-markov-approximation-hawkes]], [[bielecki-2026-continuous-time-reinforcement]] · focus: «closure + multi-asset»
- Merge: keywords for 16 keys added to library/references.bib; output bib 45 entries; based_on: preprint on 7 preprint-read pages; "Further evidence" sections on 9 concept/entity pages; 16 index lines.
- Findings that matter (each verified on the source page; main-session spot checks: Yuan p. 12 + Lemma 3):
  - Gap (1): no refutation. Fujii 2015 qualifies only (no excitation, no quote control, «occur independently for each security»). Lai 2023 sets cross-excitation to zero as «insignificant». CJR 2018 §7: «such problems cannot be solved in closed form».
  - Gap (2): no three-way comparison. Nearest: Choi 2021 (DNN vs CJR closed form within 0.07 %, no exact grid, no RL), Bielecki 2026 (RL vs DGM oracle, not market making), Bathini 2026 (bounded policy families on data).
  - D1: Yuan 2026 is a risk-neutral fill-driven pricing model where w = e^V linearises the HJB (reader's [D], not in the paper). The paper's own non-buyer extension (eq. 5) breaks linearity, and Lemma 3 gives a constant price when non-buyers excite equally. This independently confirms the §3b asymmetry.
  - D2: Zarezade (Riccati closes because the control enters linearly and λ jumps are constant) and Shen (λ-dependent coefficient, nonlocal PDE) bracket the market-making case, where λ_j multiplies a nonlinear Hamiltonian.
- Lint: 0 issues.

## [2026-10-26] ingest | Stage 2a prior-art check (5 sources)
- Focus: «Perturbative/asymptotic closed forms for multi-asset market making with a stochastic intensity factor (Hawkes or Markov-modulated): which expansion, around which point, with which small parameter and error order; whether it closes into finite matrix ODEs; how accuracy is tested; how much of Stage 2a it already covers.»
- 2026-10-26 · ingest · [[bergault-2023-liquidity-dynamics-rfq]], [[rosenbaum-2022-multi-asset-market]], [[barzykin-2022-multi-currency-inventory]] (fresh, standard)
- 2026-10-26 · re-ingest · [[fujii-2015-optimal-position-management]], [[shen-2022-mean-variance-portfolio]] (now 2 focus blocks)
- Trigger: adversarial + Prover review of input/ideas/hawkes-perturbative-closed-form-design.md (draft).
- Verdict: none pre-empts Stage 2a. Fujii 2015 is the method precedent (small-noise expansion around the deterministic factor path, order 1 linear given order 0, error eps^(N+1); diffusive factor, no Hawkes, no quote control, no numerics). Shen 2022: exponential-affine ansatz does not close (agent's derivation, not the paper's claim). Rosenbaum-Zhang 2022 "asymptotic" = T to infinity, factor frozen. Barzykin 2022 and Bergault-Guéant 2023: constant / finite-state intensities, no expansion.
- Keywords unioned into library/references.bib; bib-subset -> output bib 50 entries; 3 index lines.

## [2026-10-26] plan | hawkes-perturbative-closed-form (Stage 2a)
- Design approved: input/ideas/hawkes-perturbative-closed-form-design.md (revision 2, after adversarial + Prover review and the 5-source prior-art ingest).
- Plan pre-registered: input/ideas/hawkes-perturbative-closed-form-plan.md. H-A (closure, relative quote error e1=O(eps^2) vs e0=O(eps)), H-B (>=25 % regret reduction vs best of frozen/re-frozen at >=2/3 rho values, eps=1), H-C (cross-asset skew, secondary). Frozen after a Prover review of the pre-registration wording; user confirmed.
- Pre-registration decision: design disconfirmation #2 replaced by the stricter F-B (intentional tightening, not a deviation).
- Synthesis corrected: problem-anatomy §5 separability (diagonal Sigma -> A stays diagonal), [D] to verify in plan Task 5.

## [2026-10-26] ingest | Phase 1 Task 8 wave 2 completed (plan Stage 2a Task 2)
- 2026-10-26 · ingest · [[barzykin-2026-strategic-otc-reputation]], [[barzykin-2026-bond-market-making]], [[sakhanda-2026-hawkes-jump-diffusion]], [[ceci-2025-optimal-reinsurance-dynamic]], [[yang-2026-robust-market-making]], [[wang-2024-arl-multi-action]], [[alfonsi-2016-dynamic-optimal-execution]], [[alfonsi-2016-extension-calibration-hawkes]], [[abijaber-2021-integral-operator-riccati]], [[drissi-2022-solvability-differential-riccati]], [[fu-2022-portfolio-liquidation-games]], [[abijaber-2025-optimal-liquidation-signals]] (standard) · focus: «closure + multi-asset» (Phase 1 string)
- Merged the 4 earlier half-finished wave-2 pages into the index: [[abijaber-2021-linear-quadratic-control]], [[zhang-2020-backward-stochastic-riccati]], [[barzykin-2026-dynamic-slippage-control]], [[barzykin-2026-win-score-promotion]]
- Keywords unioned into library/references.bib; bib-subset re-run.
- Bearing on Stage 2a (agent reports, not yet verified): none pre-empts it. Alfonsi-Blanc 2016 = exact Hawkes instance of "Riccati order 0, linear order 1" (no fill probability multiplies the intensity); Sakhanda 2026 = O(eta) Poisson-vs-Hawkes value bound by residual+verification (precedent for the small-||K|| fallback and an S1 proof route); Barzykin 2026 bond eq. (32) = order-0 A^0 check for S2; Drissi 2022 / Abi Jaber 2021 = existence routes for S1; Barzykin 2026 strategic = O(alpha) shadow-price correction analogue (S1: state whether order 1 enters curvature or only quotes).
- Flag for later: chen-2026 page focus item 2 may mischaracterise Fu 2022 ("controlled-intensity HJB"); see fu-2022 focus item 3.

## [2026-10-26] literature | Stage 2a Task 1, search protocol run 1 (provisional)
- Protocol: input/bibliography/stage2a-search-protocol.md (cut-off 2026-11-30). New A: 0; new B: 7; known A re-confirmed: Barzykin 2026b (d=1), Acero et al. 2026 (RL).
- F-novelty: not triggered. Open before the run counts as conclusive: Semantic Scholar keyword queries (HTTP 429) and Park & Malinova 2026 (SSRN abstract unreadable).

## [2026-11-01] meta | lai2023-gaps-and-memory: design approved, plan pre-registered (plan Task 1)
- Framing chosen by the user: the reframed favourite (decision-relevant memory + second-order regret law, synthetic, no data cost). The cross-contract option-flow gap is not taken up. Design `input/ideas/lai2023-gaps-and-memory-design.md` → `status: approved`.
- Sign-off (user, 2026-11-01): H1, H2, F1–F3 and the fixed constants (ε_eq = 0.25 % of |J(π_ref)|; p ∈ {0, 1, 2, 3, 4, 6, 8}; 24 cells b ∈ {1.15, 1.25, 1.4, 1.8} × ρ ∈ {0.5, 0.8, 0.95} × {common-mode, directional}) frozen **as written, no amendments**.
- Control problem confirmed: flow-driven, single-asset GLFT/BEGV-type problem (risk-adjusted objective, exponential fills), not Lai's discrete-time option problem.
- Plan `input/ideas/lai2023-gaps-and-memory-plan.md` → `status: pre-registered`, `pre_registered: 2026-11-01`. Tasks 3–9 are pre-registered from this date; deviations go to this log with slug `lai2023-gaps-and-memory`.
- Acquisition decision (user): paywalled sources stay on the manual worklist; Tasks 2–3 continue with what is on disk.

## [2026-11-01] acquire | lai2023-gaps-and-memory Task 2 (run 3): 9 plan keys + 2 novelty follow-ups
- Downloaded 0, already present 0, manual 11 (of 11). Cause: the cloud container's network policy refuses CONNECT to arxiv.org, export.arxiv.org, api.openalex.org, api.crossref.org, api.unpaywall.org and projecteuclid.org (curl HTTP 000, `connect_rejected`), so every OA copy is unreachable from here. The user decided (2026-11-01) to continue past unfetchable sources.
- Metadata resolved via WebSearch: `input/bibliography/memory-acquisition-metadata.json`.
  - Renamed: `lai-2021-data-driven-approach-option` → `lai-2021-data-driven-approach` (the short title had 4 words; the rule allows 1–3).
  - Corrected: Hillairet 2024 is Hillairet & Réveillac only.
  - arXiv copies exist for 7 of the 9 and are acceptable originals under the preprint policy (non-core works).
- Manual worklist: `input/bibliography/acquisition-todo.md`, section "Priority 3b" (25 items open in total). Audit: `input/bibliography/acquisition-log-2026-11-01.json`.
- optimize-pdf scan: not applicable (no new PDF). bib-search re-indexed (94 documents, unchanged).

## [2026-11-01] ingest | re-ingest of 2 B1 core sources, focus «p-sweep / error theory» (plan lai2023-gaps-and-memory Task 2)
- 2026-11-01 · re-ingest · [[barzykin-2026-hawkes-driven-otc]] · new focus block (forecast-curve eqs. 19–22, levels 1–3, lifted HJB eq. 46, all §5/§6.2 parameters from page images, Table 3), Kernthese 31, Model card added
- 2026-11-01 · re-ingest · [[acero-2026-hawkes-structured-networks]] · new focus block (eq. 3 is an equal-width rectangle rule in the decay rate, not Gauss; Prop. 1 and Thm 1 verbatim; Fig. 2 sweeps kernel and intensity error, never reward, over p ∈ {1,2,3,4,6,8}); erratum note on setting-(1) decay rates (0.3, not 0.4)
- Main-session spot checks against the PDFs, all confirmed: Barzykin p. 19 «do not solve a lifted HJB», p. 21 «not available at comparable complexity», p. 22 «convergence theory remains open»; Acero p. 6–7 p-grid {1,2,3,4,6,8}, eq. (3) and Thm 1 on the page image (p. 3).
- BibTeX keywords unioned into library/references.bib (Barzykin: exponential-mixture kernel approximation; receding-horizon certainty equivalent. Acero: kernel truncation; regret bound; Bernstein representation). bib-subset → output bib 56 entries.

## [2026-11-01] literature | lai2023-gaps-and-memory Task 2: fixed search protocol A–D + novelty verdict
- Log: `input/bibliography/memory-search-log.md`. Queries: A 21 · B 4 · C 4 · D 9; cut-off 2026-10-29.
- **Deviation (protocol, not a pre-registration deviation — Task 2 is `pre-registered: false`):** the six named databases could not be queried directly (network policy); each was emulated with domain-restricted WebSearch. OpenAlex and Crossref were in effect not searched; classifications rest on snippets. Verdict marked provisional until a re-run against the real APIs.
- Re-read of Jusselin (preprint), Martin–Tse, Khabou–Talbi, Jain et al. for value/regret vs number of factors: only Jusselin Fig. 4 (p. 14; value of the lifted model U^{K_n} vs n ≤ ≈1100 on a power-law-type kernel) comes close — model value, not policy regret.
- New hits: R1 Abi Jaber et al. 2025 (arXiv 2503.04323; optimal P&L vs number of exponentials for a power-law propagator, execution) narrows gap part (2); R5 (TechRxiv, kernel-misspecification robustness, execution) not conclusive. Both on the manual worklist; must be read in full before the novelty claim.
- Synthesis created: [[memory-regret-gap-verification]] (draft). Verdict: (1) OPEN, (2) NARROWED (execution) / OPEN for Hawkes market making, (3) OPEN. **Stop rule not triggered** → Task 3 proceeds.
- Noted for later tasks, no change to the pre-registered hypotheses: whether H1's K or "K minus the fixed-policy curvature" is the regret kernel (Task 6); Barzykin's common-mode convention (Task 4); Barzykin §6.2's mixture decays like u^{-0.35} (b < 1, outside the grid).
