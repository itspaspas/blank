---
title: "Does a first-order expansion around the deterministic intensity forecast give a closed-form feedback policy, with an error order, for multi-asset market making under cross-asset Hawkes flow?"
type: design
created: 2026-10-26
updated: 2026-10-26
tags: [market-making, hawkes-processes, stochastic-control, multi-asset, perturbation, matrix-riccati]
status: approved
author: mixed
methodology: quantitative   # Stage-2 sub-study; full pre-registration in the plan
revision: 2   # after adversarial + Prover review and the 5-source prior-art ingest (2026-10-26)
---

# Stage 2a — Perturbative closed form for multi-asset market making under cross-asset Hawkes flow

Builds on Phase 1 ([[problem-anatomy]], design `hawkes-multi-asset-mm-design.md`). Under the
flow-driven convention the quadratic BEGV ansatz closes in inventory $q$, but the reduced
object is a $d\times d$ matrix Riccati system indexed by the $2d$-dimensional intensity state and
nonlocal in it (problem-anatomy §5, [D]).

**Why it does not close exactly** (Prover review, 2026-10-26, [D]): for an ansatz affine in
$\lambda$, the transport term and the unfilled-jump term together are exactly affine and close.
The nonlinearity comes only from the prefactor $\lambda_j$ multiplying $\breve H(p^j)$, where $p^j$
is affine in $\lambda$ through $A(\lambda+DKe_j)$; the product is quadratic in $\lambda$ through
$h_1$ and cubic through $h_2$. An exponential-affine ansatz does not close either (Shen 2022
analogue; agent derivation, [[shen-2022-mean-variance-portfolio]] focus 2). A truncation is
therefore needed.

## Model specification (fixed)

- $d$ assets, exponential Hawkes, one exponential per asset-side; $\lambda\in\mathbb R^{2d}$,
  $d\lambda=D(\mu-\lambda)dt+DK\,dN$, branching matrix $K$, $D=\operatorname{diag}(\beta)$, $\rho(K)<1$.
- **Flow-driven convention:** all market orders excite the intensities; the maker's quotes do not.
  Target market: **exchange-traded futures** (public aggressor flow). RFQ/OTC is out of scope
  (Bergault–Guéant 2023 reject Hawkes for RFQ flow, p. 4).
- **Risk-adjusted objective** (expected PnL minus quadratic inventory penalty), as in BEGV 2021.
- Fill probability $f(\delta)=\Lambda e^{-k\delta}$ per unit intensity; Hamiltonian expanded to
  second order as in BEGV.

## Research Question

**Under flow-driven, multivariate exponential Hawkes order flow with cross-asset excitation
and a risk-adjusted objective, does a first-order expansion of the reduced value function
around the deterministic intensity forecast — under an explicit large-baseline scaling — close
into a finite system of matrix ODEs with a stated error order? And does the resulting feedback
policy lower regret against the frozen-forecast policy, measured against exact grid solutions
at $d=2$?**

### Expansion point and small parameter (fixed by review)

- Expansion point: the **deterministic** forecast $m(t)$ from the initial state,
  $\dot m=D\mu-D(I-K)m$, not the conditional forecast (around which the surprise is identically 0).
- Scaling (candidate, S1 confirms): baseline $\mu\to\mu/\varepsilon^2$ with $K$ fixed, so $\rho(K)$
  is unchanged, the jump-to-mean ratio is $O(\varepsilon^2)$ and relative intensity fluctuations
  are $O(\varepsilon)$. Expand $A=A^0(t)+\varepsilon\sum_k\tilde\Delta_kA^1_k(t)+O(\varepsilon^2)$ in the
  rescaled surprise $\tilde\Delta$, likewise $B$, $C$. Under this scaling the jump coupling
  $J_j=\sum_k(DK)_{kj}A^1_k$ is higher order, so the order-1 system is **linear (Lyapunov/Sylvester)
  given $A^0$**.
- Without a scaling, dropping second-order terms is a moment closure, not an asymptotic
  expansion (Prover); the scaling is what makes "where it breaks down" a testable statement.

### Sub-questions

- **S1 Closure and error order.** Derive the order-0 and order-1 systems; prove (or bound) the
  error order in $\varepsilon$. Expected size: $(2d+1)\frac{(d+1)(d+2)}{2}$ scalar ODEs for $A,B,C$
  (30 at $d=2$). Check global existence (BEGV's comparison argument does not cover the coupled
  system) and positive-definiteness of $A^0+\varepsilon\sum\tilde\Delta_kA^1_k$; specify clipping/PSD
  projection if needed.
- **S2 Limit checks.** $K\to0$ → Poisson BEGV. $d=1$ → compare with Barzykin 2026b eqs. (40)–(43)
  (post-request forecast plus linearised sensitivity), which likely already *are* the $d=1$ order-1
  correction; and with CJR 2014 to $O(\phi,\alpha)$ after removing their midprice effects.
- **S3 Accuracy.** Regret at $d=2$ as $\rho(K)$, the off-diagonal share of $K$, the price
  correlation in $\Sigma$, and $\varepsilon$ vary. Includes transient flow-imbalance episodes
  (Barzykin 2022: the quadratic approximation degrades at ≈5× buy/sell asymmetry, p. 6).
- **S4 Cross-asset content.**
  - **S4a (lemma):** with diagonal $\Sigma$ and separable penalty, the exact HJB separates and $A$
    stays diagonal (problem-anatomy §5 correction). Prove it.
  - **S4b:** with correlated $\Sigma$, does the order-1 term change cross-asset inventory skew
    relative to the frozen forecast, and is the change in the direction of the exact solution?

### Disconfirmation (to be frozen as stop criteria in the plan)

1. The order-1 system does not close linearly under the scaling, or no error order can be
   shown → fall back to the small-$\lVert K\rVert$ expansion and record why.
2. The regret gain over the best simple comparator (frozen or re-frozen forecast) is within the
   combined numerical error (grid convergence + MC confidence interval) at every tested point.
3. A prior publication of the $d>1$ result is found under a **fixed search protocol** (queries,
   databases, forward citations of Fujii 2015, BEGV 2021, Barzykin 2026b) with a cut-off date set
   in the plan.

## Relevance / State of the field (brief)

The closed-form branch (Avellaneda–Stoikov 2008 → GLFT 2013 → BEGV 2021) assumes constant
intensities; its multi-asset extensions keep them constant or finite-state (Barzykin et al.
2022; Rosenbaum–Zhang 2022, factor frozen, "asymptotic" = $T\to\infty$; Bergault–Guéant 2023,
MMPP, single asset in the control problem). Hawkes closed forms are single-asset (CJR 2014,
Barzykin 2026b). **Method precedent:** Fujii 2015 expands a multi-security BSRDE around the
deterministic path of a *diffusive* factor, order 1 linear given order 0, error $\varepsilon^{N+1}$ —
but no jumps/excitation, no quote control, matrix order-1 system not written, no numerics.

**Claimed novelty (narrowed):** (i) a Hawkes jump factor with cross-asset excitation and its own
error order; (ii) intensities entering the Riccati system through the Hamiltonian curvature
$h_2$; (iii) the explicit matrix order-1 system for $d>1$; (iv) an accuracy map against exact
solutions. The $d=1$ correction is probably not new (Barzykin 2026b).

Empirical branching ratios span ≈0.4–0.9 by market: FX RFQ 0.86–0.90 (Barzykin 2026b Table 1,
p. 4, author warns of upward bias), IBM ≈0.67 (CJR 2014 p. 436), INTC ≈0.75 (Cartea 2018 p. 694),
equities 0.41 (Choi 2021 pp. 15, 44), crypto 0.56–0.59 (Bathini 2026 p. 10). No futures estimate
in the wiki yet.

## Method

1. **Derivation** (S1, S2, S4a). From the flow-driven lifted HJB (problem-anatomy §2/§3a) and
   BEGV's quadratic Hamiltonian, under the scaling above. Symbolic check (SymPy) at $d=1,2$.
2. **Two exact benchmarks at $d=2$**, separating the two approximation layers:
   - $V^{\text{quad}}$: grid solution of the lifted HJB with the *quadratic* Hamiltonian
     (isolates the perturbation error);
   - $V^{\text{exact}}$: grid solution with the exact Hamiltonian (adds the Hamiltonian-expansion
     error, which Phase 1 found dominant in Barzykin's setting, problem-anatomy §4).
3. **Grid protocol** (pre-registered): intensity truncation bounds from stationary quantiles at
   each $\rho(K)$; interpolation of off-grid jump targets $\lambda+DKe_j$; refinement study with
   Richardson extrapolation to bound discretisation error.
4. **Policy evaluation:** every policy evaluated by Monte Carlo under common random numbers,
   from fixed initial states, with confidence intervals; regret = shortfall against the
   grid-optimal policy evaluated the same way. Note (Fujii structure): the order-1 value correction
   vanishes at $\lambda=m$, so value gaps between order-0 and order-1 are expected at $O(\varepsilon^2)$,
   while the quote correction is $O(\varepsilon)$ — report both.
5. **Comparators:** Poisson BEGV; frozen-forecast BEGV; **re-frozen** forecast (recomputed every
   $\Delta t$, Rosenbaum–Zhang 2022 p. 16); Barzykin 2026b state feedback applied per asset;
   small-$\lVert K\rVert$ expansion; order-1 feedback; order-1 with diagonal $K$ only. Optional:
   regime-indexed matrix Riccati from a Markov-chain approximation of the intensity (Khabou 2025
   style).
6. **Sweep:** $\rho(K)\in[0.2,0.9]$, off-diagonal share of $K$, price correlation, $\varepsilon$.

## Data Sources / Material Basis

- **Synthetic only;** parameter ranges from the wiki estimates above. No real-data calibration.
- **Compute:** full model at $d=2$ = 4 intensity + 2 inventory dimensions; 20 points per intensity
  is likely too coarse at $\rho(K)=0.9$ (slow relaxation $\beta(1-\rho)$, heavy tails). The plan sets
  resolution from the refinement study. **Fallback that keeps both sides:** a low-rank $K$ (one
  buy-side and one sell-side factor shared across assets), so intensities live on a 2-dimensional
  manifold while bid/ask asymmetry is preserved.
- Theory sources (all ingested): GLFT 2013, BEGV 2021, CJR 2014, Barzykin 2026b, Bergault et al.
  2024, Fujii 2015, Shen 2022, Barzykin et al. 2022, Rosenbaum–Zhang 2022, Bergault–Guéant 2023.

## Output Target

☐ Book chapter  ☑ Journal article (methods paper: closed form + error order + accuracy map)  ☑ Grant proposal (Stage-2 section)  ☐ Talk

## Expected Results

- **Positive:** the order-1 system closes linearly with a proven error order; regret falls below
  the frozen and re-frozen forecasts beyond numerical error across realistic $\rho(K)$; S4b shows a
  cross-asset inventory-skew correction toward the exact solution.
- **Null:** no linear closure, or no gain beyond numerical error → publishable as a precise
  obstruction statement plus an accuracy map of the frozen/re-frozen forecast policies and the
  S4a separability lemma.

## Ethical / Methodological Risks

- **Derivation errors** ([D] steps by LLM reviewers, unverified) → symbolic check, limits, two grid benchmarks.
- **Novelty erosion** → fixed search protocol (stop criterion 3); claim stated narrowly above.
- **Grid feasibility** → refinement study and the low-rank fallback.
- **Framing bias:** same researcher wrote the proposal; stop criteria 2–3 guard against it.
- No ethical issues (synthetic data).

## Feasibility

Single researcher with LLM support. Derivation + error order: weeks, the riskiest part.
Code: Python + numba. No paid data, no collaborators required.

## Scope Boundaries (what is NOT investigated)

**Not investigated:** the fill-driven convention; RFQ/OTC markets; CARA utility;
sums-of-exponentials kernels; real-data calibration; an RL arm (gap (2)); adverse selection and
price impact; execution/hedging costs (Hamiltonians for hedging set to 0, as in Barzykin et al.
2022); grid validation for $d>2$ (closure only).

## Next Step

Hand off to `writing-research-plan` to produce `input/ideas/hawkes-perturbative-closed-form-plan.md`
(full pre-registration: frozen hypothesis, operationalisation, numeric thresholds, stop criteria).
