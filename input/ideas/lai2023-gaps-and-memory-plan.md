---
title: "Decision-relevant memory under power-law Hawkes flow — Research Plan"
type: plan
created: 2026-10-29
updated: 2026-11-01
status: pre-registered   # user sign-off 2026-11-01: H1, H2, F1–F3 and constants frozen as written; control problem = flow-driven GLFT/BEGV, d = 1 (mixed methodology: Tasks 3–9 are pre-registered, the rest are not)
pre_registered: 2026-11-01
author: mixed
methodology: mixed
design: "[[lai2023-gaps-and-memory-design]]"
---

# Decision-relevant memory under power-law Hawkes flow — Research Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `research-superpowers:executing-research-plan` to run this plan task by task. Tasks use checkbox syntax. Tasks marked `pre-registered: true` are frozen at sign-off; deviations go to `knowledge/_meta/log.md`.

**Research Question:** Under power-law Hawkes order flow, which functional of the flow history does the optimal quote depend on, and therefore how many exponential memory factors *p* does a market maker need — i.e. how large is the regret of a policy that conditions on a *p*-factor forecast instead of the true forecast curve?

**Gap this fills (verified in the full texts, see design §Re-evaluation):** Acero–Plank–Zhang 2026 give a worst-case bound Reg ≤ C·(kernel L² error)^{1/2} (C unspecified, subcritical truncation required) and never sweep *reward* over p; Barzykin 2026b gives a forecast-curve (Volterra–Riccati) policy with an exact anchor for **one** exponential only and says a general error theory "remains open" (p. 22). Nobody has a predictive second-order regret law, a regret-vs-p table on a power-law truth with the control-approximation error separated out, or a map of when memory is irrelevant (Acero's "tie" regime).

**Hypotheses (proposed; frozen at sign-off):**
- **H1 (regret law).** In a flow-driven single-asset market-making problem with the BEGV quadratic Hamiltonian, the regret of a policy fed a mis-specified forecast curve *m̂_t(u)* instead of the true *m_t(u)* is second order: r ≈ ½ E∬ K(u,v) Δm(u) Δm(v) du dv with Δm = m̂ − m, where K is the curvature kernel of the Riccati value map (Barzykin eqs. 36–38).
- **H2 (relevance map).** On a shifted power-law kernel g(t) = ρ(b−1)t₀^{b−1}(t+t₀)^{−b} (‖g‖₁ = ρ), the smallest p whose memory regret is below the equivalence margin, p\*, is ≤ 2 for exponent b ≥ 1.4 and ρ ≤ 0.8, and ≥ 4 for b = 1.15, ρ = 0.95.

**Falsification Criteria:**
- **F1 (kills H1).** In Tier 1 (exact anchor), among cells with measured regret > 3 SE: (a) median |log₂(R̂ₚ / rₚ)| > 1 (prediction off by more than a factor 2), **or** (b) the OLS slope of log rₚ on log ‖Δm‖_{L²} lies outside [1.6, 2.4].
- **F2 (kills H2).** p\*(b = 1.15, ρ = 0.95) ≤ 2 in both flow regimes, **or** p\*(b ≥ 1.4, ρ ≤ 0.8) > 2 in any cell.
- **F3 (null, stop).** rₚ at p = 1 is below the solver error (see Stop Criterion) in every cell → memory beyond one factor is irrelevant; stop after Task 7 and write the short equivalence note; Tasks 8–10 are cancelled.

**Stop Criterion:** per cell, the paired-regret standard error ≤ 0.05% of |J| (cap 2×10⁵ paths); the exact anchor's regret changes by < 10% when the grid is refined by a factor 2 (Richardson); 5 training seeds in the cross-check.

**Fixed constants (frozen at sign-off):** equivalence margin ε_eq = 0.25% of |J(π_ref)|; p ∈ {0, 1, 2, 3, 4, 6, 8}; p_max = 8; grid cells b ∈ {1.15, 1.25, 1.4, 1.8} × ρ ∈ {0.5, 0.8, 0.95} × flow regime {common-mode, directional} = 24 cells.

**Method:** Three tiers on one policy engine. *Tier 0* (kernel only, no control): forecast error Δm and kernel tail mass per lift. *Tier 1* (exact anchor): truth = 2-exponential mixture, exact lifted HJB on a (q, x₁, x₂) grid, lift p ∈ {0, 1} → tests H1 with an exact reference. *Tier 2* (target): truth = shifted power law, policy = Barzykin's Riccati layer fed with the p-factor forecast vs the exact forecast, Monte-Carlo under common random numbers → tests H2. Memory regret (p-lift vs exact-forecast policy) is always reported **separately** from the control-approximation floor (Riccati engine vs exact HJB), because Barzykin's own VR error is 0.1–2.5% and would otherwise be confounded with p.

**Output target:** journal article (Quant. Finance / SIAM J. Financial Math.); feeds Stage 2 of `proposal/proposal.pdf`.
**Language:** en

**Notation (project § Notation + mapping):** intensity λ_t, baseline μ, branching norm ρ = ‖g‖₁, decay rates β_j (lift), forecast m_t(u), Hamiltonian curvature h₂, risk aversion γ, inventory q. Power-law kernel: exponent *b*, offset *t₀*; Lai's (α, β, δ) → (b = β, t₀ = δ, ρ = αδ^{1−β}/(β−1)); Acero's tail index α_A = b − 1. Lai's *K* (number of decision periods) is not used.

**Problem fixed for all tiers:** one asset, two sides, unit size; **flow-driven** (all requests/market orders excite, the maker's fills do not); exponential fill probability f(δ) = e^{−kδ} (sigmoid in Task 8); risk-adjusted objective (BEGV/Barzykin eq. 14: fill revenue − ½γσ²∫q² − terminal penalty); horizon T = 1 (activity-time day), baseline set so that μ̄T ≈ 400 events per side; t₀ = 0.01 T.

---

## Data Sources

No market data in the pre-registered core (synthetic flow; Lai Table 2 used only as anchor points).

- [[lai-2023-data-driven-deep]] — on disk, ingested; Table 2 anchors (AAPL (1.01,1.02] 0–5 buy: b ≈ 1.12, ρ ≈ 0.59 → cell b = 1.15, ρ = 0.5; BAC b ≈ 1.67–2.22 → cell b = 1.8)
- [[barzykin-2026-hawkes-driven-otc]] — on disk, ingested; re-ingest with focus "p-sweep, error theory, parameters of Tables 2–3" (Task 2)
- [[acero-2026-hawkes-structured-networks]] — on disk, ingested; re-ingest with the same focus
- [[jusselin-2021-persistent-order-flow]], [[martin-2026-market-making-hawkes]], [[khabou-2025-markov-approximation-hawkes]], [[jain-2025-impulse-control-hawkes]] — on disk, ingested; re-read for a regret-vs-p table (Task 2, novelty risk)
- *acquire pending (keys proposed; `acquire-sources` confirms):* `lai-2021-data-driven-approach-option` (CUHK thesis: time unit, same-timestamp aggregation), `alfonsi-2024-approximation-stochastic-volterra`, `bayer-2023-markovian-approximations-stochastic`, `abijaber-2019-multifactor-approximation-rough`, `hardiman-2013-critical-reflexivity`, `filimonov-2015-apparent-criticality`, `lallouache-2016-limits-statistical-significance`, `hillairet-2024-chaotic-expansion-counting`, `leblanc-2024-exponential-moments-hawkes`
- Optional exploratory leg (Task 10c): public trade prints (Binance/Tardis free tier named in the project design) — availability checked in the task, not assumed.

## Tasks

### Task 1: Pre-flight decisions and sign-off
**Files:** `input/ideas/lai2023-gaps-and-memory-plan.md`, `knowledge/_meta/log.md`
`pre-registered: false`

- [x] User confirms H1, H2, F1–F3, ε_eq = 0.25%, p-grid, 24 cells (or amends; amendments are logged) — confirmed as written, no amendments (2026-11-01)
- [x] User confirms the control problem (flow-driven GLFT/BEGV-type, d = 1) instead of Lai's discrete-time option problem — confirmed (2026-11-01)
- [x] Set `status: pre-registered` and write the sign-off date into the log — 2026-11-01

### Task 2: Acquire sources, close the novelty check
**Files:** `<library>/pdf/*.pdf`, `input/bibliography/acquisition-todo.md`, `input/bibliography/memory-search-log.md`, `knowledge/sources/{barzykin-2026-hawkes-driven-otc,acero-2026-hawkes-structured-networks,jusselin-2021-persistent-order-flow,martin-2026-market-making-hawkes,khabou-2025-markov-approximation-hawkes,jain-2025-impulse-control-hawkes}.md`, `knowledge/synthesis/memory-regret-gap-verification.md`
`pre-registered: false`

- [x] Run `acquire-sources` for the nine keys listed under Data Sources; reconcile manual downloads — 2026-11-01: metadata resolved for all 9 (`lai-2021-data-driven-approach-option` → `lai-2021-data-driven-approach`); 0 downloaded because the container's network policy blocks arXiv/OpenAlex/Crossref; all 9 + 2 novelty follow-ups on the manual worklist (user decision: continue). Audit: `input/bibliography/acquisition-log-2026-11-01.json`
- [x] Re-ingest Barzykin and Acero with focus "p-sweep / error theory": record Acero Thm 1 (p. 3, sqrt-L² bound, subcritical condition), Fig. 2 (kernel error, not reward, vs p), Barzykin Table 3 and §6 (8-exponential "power law", no exact anchor), p. 22 ("error theory open")
- [x] Re-read Jusselin, Martin–Tse, Khabou, Jain for any table of value or regret versus number of factors on a power-law/fractional kernel; add one line per source to the gap-verification page — only Jusselin Fig. 4 (value of the lifted model vs n, not policy regret) comes close
- [x] Execute the fixed search protocol (blocks A–D, cut-off 2026-10-29; design §Cross-examination log); log query, database, date, hit count in `input/bibliography/memory-search-log.md` — run 2026-11-01 via domain-restricted WebSearch (database APIs blocked; deviation logged); verdict provisional until re-run against the APIs
- [x] **Stop rule:** — not triggered (2026-11-01; see [[memory-regret-gap-verification]]). if any source already reports regret/reward vs p on a power-law kernel with an exact or near-exact reference **and** a second-order law, mark the gap CLOSED, log it, and return to the user before Task 3

### Task 3: Tier 0 — analytic screen (no control problem)
**Files:** `output/data-analysis/memory-regret/screen.py`, `output/data-analysis/memory-regret/results/screen.json`, `output/data-analysis/memory-regret/tests/test_screen.py`
`pre-registered: true`

- [ ] Implement the shifted power-law kernel and its exact forecast curve m_t(u) via the discretised Volterra resolvent (Barzykin eqs. 20–22)
- [ ] Implement three p-factor lifts: (i) Gauss-type quadrature in the decay rate (Alfonsi–Kebaier/Acero), (ii) NNLS L²[0,T] fit, (iii) mass-preserving (Σ wⱼ = ρ) log-spaced fit
- [ ] Compute for each cell and lift: kernel L² error, mean ‖Δm‖_{L²}, kernel mass beyond one decision interval (δ/(Δ+δ))^{b−1}
- [ ] Test: reproduce the L¹ norms and tail masses of Lai Table 2 rows (e.g. AAPL (1.01,1.02] 6–10 buy: 1.0002, 0.119)
- [ ] Write `results/screen.json`; check that p\* predicted by ‖Δm‖ ordering is consistent with H2's direction (informational, does not change the hypotheses)

### Task 4: Riccati engine and reproduction of Barzykin's exponential benchmark
**Files:** `output/data-analysis/memory-regret/vr_engine.py`, `output/data-analysis/memory-regret/lifted_hjb.py`, `output/data-analysis/memory-regret/results/repro_barzykin.json`, `output/data-analysis/memory-regret/tests/test_engine.py`
`pre-registered: true`

- [ ] Read Barzykin Tables 2–3 and §5.1 parameters (including the sigmoid constants) from the PDF page images, pp. 14–16, into `params_barzykin.json`
- [ ] Implement the backward Riccati system (his eqs. 29–31) for a given forecast curve and the quote map (eq. 32); implement mean, noise-aware and state-feedback variants
- [ ] Implement the exact lifted HJB on (t, q, x) (his eq. 46) with the stated grids; check Poisson limit against the 1-D inventory HJB (his eq. 50)
- [ ] Run the three regimes with common random numbers, 2×10⁴ paths; **acceptance:** each relative regret within ±0.1 percentage points of Barzykin's Table 3 or inside the overlap of 95% CIs; otherwise stop and diagnose before Task 5
- [ ] Time the engine (events/s) and fix the receding-horizon re-solve rule (per event vs per clock step) so Task 7 fits the compute budget

### Task 5: Tier 1 — exact anchor with a 2-factor truth
**Files:** `output/data-analysis/memory-regret/lifted_hjb.py` (2-factor extension), `output/data-analysis/memory-regret/tier1.py`, `output/data-analysis/memory-regret/results/tier1.json`
`pre-registered: true`

- [ ] Extend the exact lifted HJB to two memory states (q, x₁, x₂) with a refinement study (grid ×1, ×2) and Richardson error bound
- [ ] Define 12 Tier-1 cells: truth = 2-exponential mixture; vary timescale ratio {3, 10, 30} and weight split {0.5/0.5, 0.8/0.2} and regime {common-mode, directional}; approximations p ∈ {0, 1} with lifts (i)–(iii)
- [ ] Record per cell: control-approximation floor r(VR(m) vs exact) and memory regret rₚ (VR(m̂ᵖ) vs VR(m)) and total regret vs exact
- [ ] **Gate:** floor ≤ 0.5% in the cells used for H1; if not, replace the Riccati engine by the exact lift for p ≤ 2 in Tier 2 and log the deviation
- [ ] Write `results/tier1.json`

### Task 6: Test H1 — the regret law
**Files:** `output/data-analysis/memory-regret/regret_law.py`, `output/data-analysis/memory-regret/results/h1.json`, `output/data-analysis/memory-regret/tests/test_curvature.py`
`pre-registered: true`

- [ ] Compute the curvature kernel K(u,v) by finite differences of the Riccati value map on a lag grid (and, as a check, by the adjoint of the Riccati system)
- [ ] Test: K symmetric; directional derivative of V along Δm matches a finite-difference value change to 1%
- [ ] Simulate stationary histories, compute Δmₜ(u) for each Tier-1 lift, form R̂ₚ = ½ E∬ K Δm Δm
- [ ] Evaluate F1(a) and F1(b) on Tier-1 cells with measured regret > 3 SE; write the verdict (confirmed / refuted / limited to a regime) to `results/h1.json`
- [ ] If refuted: decompose the gap into (information the lift lacks) vs (forecast error) and record, per the design's stated failure mode

### Task 7: Tier 2 — power-law truth, regret vs p, test H2
**Files:** `output/data-analysis/memory-regret/tier2.py`, `output/data-analysis/memory-regret/results/tier2.json`, `output/data-analysis/memory-regret/results/h2.json`
`pre-registered: true`

- [ ] Simulate the power-law Hawkes flow (thinning/Ogata with the exact kernel), 24 cells, CRN across policies
- [ ] Policies per cell: Poisson/NHPP-matched, VR(m̂ᵖ) for p ∈ {1, 2, 3, 4, 6, 8} × lifts (i)–(iii), VR(m) with the exact forecast, state-feedback variants
- [ ] Compute rₚ relative to VR(m) and to Poisson; apply the stop criterion (SE ≤ 0.05% of |J|)
- [ ] Define p\* = min{p : rₚ ≤ ε_eq}; compare with R̂ₚ from Task 6 (law as predictor outside the anchor)
- [ ] Evaluate F2 and F3; write `results/h2.json`; **if F3 triggers, stop here** (Tasks 8–9 cancelled)

### Task 8: Robustness
**Files:** `output/data-analysis/memory-regret/results/robustness.json`
`pre-registered: true` (cells and variants listed here are frozen)

- [ ] t₀ ∈ {0.001, 0.1}·T and T ∈ {0.5, 1} on the four corner cells
- [ ] Sigmoid win probability (Barzykin §6.2 shape) instead of e^{−kδ}; γ doubled and halved
- [ ] Near-critical diagnostics at ρ = 0.95: stationary-count check, burn-in sensitivity, truncated-kernel subcriticality (‖ĝ‖₁ < 1) per lift
- [ ] Report whether each H2 verdict is stable across the variants; unstable cells are flagged, not removed

### Task 9: Cross-check with direct policy optimisation
**Files:** `output/data-analysis/memory-regret/crosscheck_policy.py`, `output/data-analysis/memory-regret/results/crosscheck.json`
`pre-registered: true`

- [ ] Implement the Han–E-style direct optimiser (or PPO as in Acero) on features = p exponential filters, Constant quote inside the function class, 5 seeds
- [ ] Run the four corner cells for p ∈ {0, 1, 2, 4, 8}; V\*(p) with day-block bootstrap CIs
- [ ] **Check:** Constant quote is beaten (else the optimiser is not trustworthy, as in Lai Table 8 BAC); the sign of rₚ − rₚ₊₁ agrees with Task 7 within SE for p ∈ {1, 2, 4}
- [ ] Record disagreements as limitations of the Riccati engine, not as corrections of Task 7

### Task 10: Exploratory arms (not pre-registered; labelled as such in any text)
**Files:** `output/data-analysis/memory-regret/explore_*.py`, `output/data-analysis/memory-regret/results/explore_*.json`
`pre-registered: false`

- [ ] (a) Decision-optimal lift: choose lift weights to minimise the Riccati-weighted forecast error ½∬K Δm Δm instead of the L² kernel error; count factors saved against lifts (i)–(iii)
- [ ] (b) Fill-driven arm at p = 1: exact lifted HJB where the maker's executions excite the memory; regret of the flow-driven policy when the truth is fill-driven
- [ ] (c) Optional real-data identifiability leg (only if a free trade-print source is confirmed): fit exponential, 2-/3-exponential, power-law, each with a flexible/Cox baseline; AIC/BIC and out-of-sample log-likelihood; compare with Lai's and Barzykin's branching estimates

### Task 11: Synthesis
**Files:** `knowledge/synthesis/memory-regret-results.md`, `knowledge/_meta/index.md`, `knowledge/_meta/log.md`
`pre-registered: false`

- [ ] Pull Tier 1/2 results into one page with **Evidence base** (which sources and results carry each claim) and **What stays open**
- [ ] State separately: control-approximation floor, memory regret, regime map, law verdict; label exploratory arms
- [ ] Cross-link [[problem-anatomy]], [[markov-lift]], [[intensity-forecast]]; set `status: stable` after user review
- [ ] Run `python scripts/lint-wiki.py` (green before drafting)

### Task 12: Draft the article (staged, per project CLAUDE.md § Draft)
**Files:** `output/article/outline/memory-regret.md`, `output/article/memory-regret.qmd`
`pre-registered: false`

- [ ] Write the outline (thesis, claim chain, claim + evidence + word budget per section) and get the user's approval **before any prose**
- [ ] Draft per section after an approved argument sketch; floors: Introduction + related work 1,200 words; Model and lifts 1,200; Regret law and proof sketch 1,500; Experiments (Tier 1, 2, robustness) 2,000; Discussion, limits, what stays open 900
- [ ] Citations `@bibkey` from `output/bibtex/references.bib` only; every figure states its source
- [ ] Peer review round via `requesting-peer-review` (constructive + adversarial)

## Verification

The project is complete when:
- [ ] `results/h1.json` and `results/h2.json` each contain a verdict (confirmed / refuted / limited / inconclusive) with the numbers behind F1–F3
- [ ] Task 4 reproduces Barzykin Table 3 within the stated tolerance (or the deviation is logged)
- [ ] Every reported regret carries a paired SE ≤ 0.05% of |J| or is marked "below resolution"
- [ ] The control-approximation floor is reported next to every memory-regret table
- [ ] `knowledge/synthesis/memory-regret-gap-verification.md` contains the executed search protocol with hit counts and the date
- [ ] `python scripts/lint-wiki.py` exits 0
- [ ] Outline approved; draft renders without errors; peer review completed
- [ ] Hypotheses H1 and H2 are each marked confirmed, refuted, or "inconclusive — exploratory" in the manuscript, with exploratory arms labelled

## Deviations Log

Append to `knowledge/_meta/log.md` whenever scope, method, constants (ε_eq, p-grid, cells) or data sources change after pre-registration. Reference the slug `lai2023-gaps-and-memory`.

## Risks carried from the design

- The law may fail because the lift's policy errs through the *information it lacks*, not only through Δm (Task 6 decomposes this).
- Acero's subcriticality condition fails at ρ = 0.95 for some lifts; those cells are reported as such, not repaired.
- Barzykin's engine is validated only for one exponential; Task 5's floor gate protects against attributing engine error to memory.
- Time units of Lai's Table 2 are unstated; anchors are used only as cell labels until the thesis is read (Task 2).
- If the gap is closed by a source found in Task 2, the plan stops there and returns to the user.
