---
title: "Stage 2a — Perturbative closed form for multi-asset market making under cross-asset Hawkes flow — Research Plan"
type: plan
created: 2026-10-26
updated: 2026-10-26
status: pre-registered   # user confirmed H-A/H-B/H-C + F on 2026-10-26
author: mixed
design: "[[hawkes-perturbative-closed-form-design]]"
methodology: quantitative
---

# Stage 2a — Research Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `research-superpowers:executing-research-plan` to run this plan task by task. Tasks use checkbox (`- [ ]`) syntax for TodoWrite integration.

**Research Question:** Under flow-driven, multivariate exponential Hawkes order flow with
cross-asset excitation and a risk-adjusted objective, does a first-order expansion of the reduced
value function around the deterministic intensity forecast, under the large-baseline scaling
$\mu\to\mu/\varepsilon^2$, close into a finite system of matrix ODEs with a stated error order, and does
the resulting feedback policy lower regret against the frozen-forecast policy at $d=2$?

**Hypotheses (pre-registered, immutable):**
*Revised 2026-10-26 after Prover pre-registration review (order counting under the scaling).*

**Definitions.** $\bar\delta$ = the $O(1)$ quote part common to all policies; $\delta^n$ = quote of the
order-$n$ policy ($n=0$ is the frozen policy, i.e. $A^0$ along $m(t)$ from $x_0$); $\delta^{\text{quad}}$ =
quote from the $V^{\text{quad}}$ grid solution. **State set** $S$ = $\{t=0\}\times q\in\{-Q..Q\}^2\times
\lambda=m(0)+c\,\mathrm{sd}_{\text{stat}}e_k$, $c\in\{\pm1,\pm2\}$, all components $k$ (excludes $\lambda=m$,
where the order-1 term vanishes). Relative quote error
$e_n(\varepsilon)=\max_S|\delta^n-\delta^{\text{quad}}|/\max_S|\delta^{\text{quad}}-\bar\delta|$.

- **H-A (closure, primary):** Under the scaling, the order-1 coefficients solve a linear ODE system
  given order 0, with the jump coupling $J$ retained wherever it appears at $O(\varepsilon)$ (it does in
  the $B$/$C$ equations), and $e_1=O(\varepsilon^2)$ while $e_0=O(\varepsilon)$. H-A is decided by the
  numerical criterion F-A; the proof (Task 5) is reported, not used to revise H-A.
- **H-B (accuracy, primary):** Evaluated at the 3 core $\rho(K)\in\{0.4,0.6,0.8\}$ with off-diagonal
  share 0.5, correlation 0.6, $\varepsilon=1$. $R_\pi$ = mean over the 4 initial states of
  $V^{\text{quad}}(x_0)-V^\pi(x_0)$. A point **succeeds** iff
  $1-R_1/\min(R_{\text{frozen}},R_{\text{refrozen}})\ge 0.25$ **and**
  $\min(R_{\text{frozen}},R_{\text{refrozen}})-R_1>2\,(\text{grid bound}+95\%\text{ half-width of the CRN paired difference})$.
  A point with $\min(R_{\text{frozen}},R_{\text{refrozen}})\le 2\times$error is **undecidable** and counts
  as non-success. H-B is confirmed at $\ge2$ of 3 successes; inconclusive if $\ge2$ points are undecidable.
- **H-C (cross-asset, secondary):** $s_{ij}(\pi)=\tfrac12[\delta^{j,b}(q=e_i)-\delta^{j,b}(q=-e_i)]$ at $t=0$,
  $\lambda=m(0)\pm\mathrm{sd}_{\text{stat}}e_k$ (all $k$, both signs), at the 6 core points with
  correlation 0.6. Confirmed iff in $\ge75\%$ of these (point, $\lambda$) cases
  $\operatorname{sign}(s^1)=\operatorname{sign}(s^{\text{quad}})$ and
  $|s^1-s^{\text{quad}}|<|s^0-s^{\text{quad}}|-2\times$grid error.
- **Lemma S4a (to prove, not a hypothesis):** with diagonal $\Sigma$, separable penalty **and**
  off-diagonal share of $K$ equal to 0, the exact HJB separates and $A$ stays diagonal.

**Falsification Criteria:**
- **F-A:** the order-1 system is not linear given order 0 (Task 3), **or** $\mathrm{slope}(e_1)<1.5$,
  **or** $\mathrm{slope}(e_1)-\mathrm{slope}(e_0)<0.5$, slopes fitted by least squares on log–log over
  $\varepsilon\in\{\tfrac12,\tfrac14,\tfrac18,\tfrac1{16}\}$ ($\varepsilon=1$ reported, not fitted). An $\varepsilon$
  is kept only if the Richardson bound on quotes is $\le e_1(\varepsilon)/5$ (grid $\Delta t\propto\varepsilon^2$);
  if fewer than 3 survive, H-A is **inconclusive**. On rejection → small-$\lVert K\rVert$ expansion
  (Task 3b), reported as such.
- **F-B:** fewer than 2 successes as defined in H-B.
- **F-C:** the H-C condition holds in fewer than 75 % of cases.
- *Intentional tightening:* the design's disconfirmation #2 ("within error at every point") is
  replaced by F-B; logged as a pre-registration decision, not a deviation.
- **F-novelty:** the fixed search protocol (Task 1) finds a published $d>1$ Hawkes perturbative
  closed form before the cut-off **2026-11-30**. → contribution re-scoped to accuracy map + S4a.

**Stop Criterion:** the fixed sweep in Task 9 is complete (no added points after seeing results);
numerical tolerances met (grid: Richardson bound on quotes per F-A, on values ≤ ¼ of the smallest
regret difference tested; MC: path count raised until the 95 % half-width of each CRN paired
regret difference is ≤ ¼ of that difference or 10⁶ paths, whichever first). Any added point is logged as exploratory.

**Method:** Derive order-0/order-1 systems symbolically (SymPy), prove S4a and the error order;
solve two lifted HJBs on a grid at $d=2$ ($V^{\text{quad}}$ with the quadratic Hamiltonian,
$V^{\text{exact}}$ with the exact one); evaluate all policies by Monte Carlo under common random
numbers from fixed initial states. Regret is measured against the grid-optimal policy evaluated
the same way; H-B and H-C are judged against $V^{\text{quad}}$ (isolates the perturbation error);
$V^{\text{exact}}$ is reported alongside.

**Output target:** article (methods paper) + Stage-2 section of the proposal
**Language:** en

---

## Data Sources

- Synthetic only. Parameter ranges from wiki pages: [[barzykin-2026-hawkes-driven-otc]] (ρ 0.86–0.90),
  [[cartea-2014-buy-low-sell]] (≈0.67), [[cartea-2018-algorithmic-trading-stochastic]] (≈0.75),
  [[choi-2021-synchronised-order-arrivals]] (0.41), [[bathini-2026-dynamic-market-making]] (0.56–0.59),
  [[acero-2026-hawkes-structured-networks]] (ρ 0.40, cross 0.28) — *in wiki*.
- Theory: [[bergault-2021-closed-form-approximations]], [[gueant-2013-dealing-inventory-risk]],
  [[cartea-2014-buy-low-sell]], [[barzykin-2026-hawkes-driven-otc]], [[bergault-2024-price-aware-automated]],
  [[fujii-2015-optimal-position-management]], [[shen-2022-mean-variance-portfolio]],
  [[barzykin-2022-multi-currency-inventory]], [[rosenbaum-2022-multi-asset-market]],
  [[bergault-2023-liquidity-dynamics-rfq]], [[khabou-2025-markov-approximation-hawkes]] — *in wiki*.

## Core parameters (frozen)

- $d=2$; $\gamma$, $k$, $\Lambda$, $\sigma$, horizon $T$, inventory bound $Q=5$: central values fixed in
  Task 4 from BEGV 2021's numerical section before any solve, and not changed afterwards.
- Core sweep: $\rho(K)\in\{0.4,0.6,0.8\}$ × off-diagonal share $\in\{0,0.5\}$ × price correlation
  $\in\{0,0.6\}$ = 12 points, each with $V^{\text{quad}}$ and $V^{\text{exact}}$.
- Extended (reported, not used for H-B): $\rho\in\{0.2,0.9\}$ at central values; flow-imbalance
  scenario (initial sell/buy intensity ratio 5).
- $\varepsilon$-study (H-A): $\varepsilon\in\{1,\tfrac12,\tfrac14,\tfrac18,\tfrac1{16}\}$ at $\rho=0.6$, off-diagonal share 0.5, correlation 0.6.
- Core sweep runs at $\varepsilon=1$ (the unscaled, realistic model).
- Horizon $T\ge20\max_k(1/\beta_k)$, frozen as a number in Task 4; re-frozen refresh interval $\Delta t$ frozen as a number in Task 4.

## Tasks

### Task 1: Fixed prior-art search protocol (F-novelty)
**Files:** `input/bibliography/stage2a-search-protocol.md`, `input/bibliography/literaturguide.md`
- [ ] Write the protocol: databases (OpenAlex, arXiv q-fin/math.OC, Crossref, Semantic Scholar), 6 fixed queries, forward citations of Fujii 2015, BEGV 2021, Barzykin 2026b; cut-off 2026-11-30
- [ ] Run it via `literature-review`; grade A/B/C; every A candidate gets an explicit verdict against the design's four novelty items
- [ ] `acquire-sources` + `ingest-source` for any A candidate; log result

### Task 2: Finish Phase 1 ingest dependencies
**Files:** `knowledge/sources/*.md`
- [x] Re-run Phase 1 Task 8 wave 2 (4 half-finished pages, 9 lint issues) and confirm `lint-wiki.py` exit 0 — done 2026-10-26 (12 sources, lint 0)
- [x] Re-check Barzykin 2026b eqs. (40)–(43) on its source page; record the $d=1$ correspondence claim as [D] to verify in Task 5 — done 2026-10-26: source page lines 288–291 give $m^{i,+}=m+\rho_i$ (40–41), shadow price at the post-request forecast (42), linearised in the forecast perturbation (43). [D] claim: (42)–(43) = our $(J, A^1)$ at $d=1$; verify in Task 5.

### Task 3: Derivation — order 0 and order 1 (H-A)
**Files:** `knowledge/synthesis/perturbative-closure.md`, `output/data-analysis/stage2a/derive/derive.py`
- [ ] Write the rescaled lifted HJB under $\mu\to\mu/\varepsilon^2$ with the quadratic Hamiltonian
- [ ] Insert the ansatz; collect orders $\varepsilon^0,\varepsilon^1$; state the order-0 and order-1 systems
- [ ] SymPy check at $d=1$ and $d=2$: residual of the HJB at order ≤ 1 vanishes identically
- [ ] Decide F-A (linearity) and log it
- [ ] **3b (only if F-A triggers):** derive the small-$\lVert K\rVert$ expansion instead

### Task 4: Freeze numerical parameters
**Files:** `output/data-analysis/stage2a/config/params.yaml`
- [ ] Central values from BEGV 2021 numerics; sweep values as above; grid bounds rule (stationary 99.9 % quantile of each intensity); MC path count rule; fixed initial states ($\lambda_0=\bar m$, $q_0\in\{(0,0),(\pm Q/2,0),(Q/2,-Q/2)\}$). The design's optional regime-indexed Riccati comparator is **not** included (YAGNI; add only as a logged exploratory deviation)
- [ ] Commit before any solve; log the commit hash in `knowledge/_meta/log.md`

### Task 5: Proofs and limit checks
**Files:** `knowledge/synthesis/perturbative-closure.md`
- [ ] Prove Lemma S4a
- [ ] Error-order argument for $e_1=O(\varepsilon^2)$, $e_0=O(\varepsilon)$ (reported; H-A is decided by F-A, not by this proof)
- [ ] Limits: $K\to0$ → BEGV; $d=1$ vs Barzykin 2026b (40)–(43) and CJR 2014
- [ ] Global existence / positive-definiteness check; specify PSD projection if needed

### Task 6: Closed-form solvers
**Files:** `output/data-analysis/stage2a/policies/*.py`, `output/data-analysis/stage2a/tests/`
- [ ] Implement Poisson BEGV, frozen, re-frozen ($\Delta t$ fixed in params), Barzykin per-asset feedback, small-$\lVert K\rVert$, order-1, order-1 diagonal-K
- [ ] Unit tests: BEGV reproduces its published numbers; $K=0$ makes all Hawkes policies coincide with BEGV

### Task 7: Grid solvers $V^{\text{quad}}$ and $V^{\text{exact}}$
**Files:** `output/data-analysis/stage2a/grid/*.py`
- [ ] Semi-Lagrangian scheme on $\{-Q..Q\}^2\times\mathbb R^4_+$ with interpolated jump targets
- [ ] Refinement study + Richardson bound at the central point; pass tolerance or switch to the low-rank-$K$ fallback (logged as deviation)

### Task 8: $\varepsilon$-study (H-A numerical)
**Files:** `output/data-analysis/stage2a/results/eps_study.json`
- [ ] Compute $e_0(\varepsilon)$, $e_1(\varepsilon)$ on $S$ for $\varepsilon\in\{1,\tfrac12,\tfrac14,\tfrac18,\tfrac1{16}\}$; apply the grid-survival rule; fit slopes; decide F-A exactly as worded

### Task 9: Policy evaluation sweep (H-B, H-C)
**Files:** `output/data-analysis/stage2a/results/sweep.json`, `output/data-analysis/stage2a/results/figures/`
- [ ] MC under common random numbers, fixed initial states, all policies, 12 core + extended points
- [ ] Decide F-B and F-C exactly as worded above; report $V^{\text{exact}}$ regrets alongside

### Task 10: Synthesis
**Files:** `knowledge/synthesis/perturbative-closure.md`, `knowledge/synthesis/problem-anatomy.md`
- [ ] Results per hypothesis: confirmed / refuted / inconclusive; deviations listed
- [ ] Update problem-anatomy §5 with verified status of the separability correction
- [ ] `## Evidence base` and `## What stays open`; status `review`

### Task 11: Draft article outline
**Files:** `output/article/outline/stage2a.md`
- [ ] Via `drafting-manuscript` (architecture first; target 7 000–9 000 words for the full article)

## Verification

- [ ] `scripts/lint-wiki.py` exits 0
- [ ] Search protocol run and logged before 2026-11-30
- [ ] SymPy residual test passes; unit tests pass
- [ ] Grid tolerance met (or fallback logged)
- [ ] H-A, H-B, H-C each marked confirmed / refuted / inconclusive — exploratory
- [ ] `perturbative-closure` synthesis at `status: review` with evidence base

## Deviations Log

Append to `knowledge/_meta/log.md` with prefix `## [date] deviation | hawkes-perturbative-closed-form` whenever scope, method, parameters or data change after pre-registration.
