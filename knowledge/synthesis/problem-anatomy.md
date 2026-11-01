---
title: "Problem anatomy: where closed-form market making breaks under (cross-asset) Hawkes order flow"
type: synthesis
created: 2026-10-25
updated: 2026-10-25
status: draft
author: mixed
tags: [market-making, hawkes, closed-form, riccati, multi-asset, phase-1]
---

# Problem anatomy: where closed-form market making breaks under (cross-asset) Hawkes order flow

**Question (design Q1–Q3):** why does the closed-form theory close under Poisson flow, what does a
Hawkes intensity add to the state, and at which step, under which modelling convention, does the
closure break or become approximate?

**Status: first pass (plan Task 5).** It rests on the 8 core sources only; Q4–Q6 come later
(comparison matrix, empirical evidence, gap search). Statements are tagged:
- **[S]** stated in a source, with page;
- **[D]** derived in this synthesis from the sources' equations; checked only in outline. Per the
  proposal's verification rule (p. 21) every [D] needs an independent re-derivation before it is
  used in a paper;
- **[I]** an inference or conjecture.

Notation: project notation (CLAUDE.md § Notation). One reduced value function
$\theta(t,q,\lambda)$ after cash and marked-to-market inventory are factored out.

---

## 1. Why the Poisson case closes (Q1)

Three different closed forms exist, and they close for **different** reasons.

### 1a. GLFT 2013: exact linearisation, one asset
- **[S]** With exponential fills $\Lambda e^{-k\delta}$, CARA utility and a Brownian price, the
  substitution $u=-\exp(-\gamma(x+qs))\,v_q(t)^{-\gamma/k}$ turns the HJB into a *linear* system
  $\dot v=Mv$, solved by $v=e^{-M(T-t)}\mathbf 1$ (Prop. 1 p. 481, Thm. 1 p. 482;
  [[gueant-2013-dealing-inventory-risk]]).
- **[S]** It needs: the same $k$ on both sides; every state jump is a fill (pp. 481, 496–497).
- **What makes it work [D]:** after the substitution, the optimised fill term
  $\sup_\delta e^{-k\delta}\,[\dots]$ becomes $c\,v_{q\pm1}/v_q$ times a common factor, and every
  other term is linear in $v$. Linearity is a property of the *exponential × CARA* pairing, not of
  any expansion; nothing is approximated.

### 1b. BEGV 2021: quadratic Hamiltonian → matrix Riccati, d assets
- **[S]** The reduction $\theta=\theta(t,q)$ works because prices are arithmetic BM with constant
  $\Sigma$ and intensities depend only on each asset's own quote (p. 104, p. 107;
  [[bergault-2021-closed-form-approximations]]).
- **[S]** Replacing each Hamiltonian by $\breve H(p)=\alpha_0+\alpha_1p+\tfrac12\alpha_2p^2$ (Taylor
  at $p=0$ is only «A natural choice», Remark 1, p. 109) makes
  $\theta=-q^\top Aq-q^\top B-C$ an exact solution of the approximated equation, with
  $A'=2AD_+A-\tfrac12\gamma\Sigma$, solved by tanh (eq. 13), ergodic limit Prop. 3
  (pp. 111–116).
- **What makes it work [S+D]:** the Hamiltonian is evaluated at a finite difference of $\theta$ in
  $q$, which is **affine in $q$** for a quadratic $\theta$; the quadratic $\breve H$ of an affine
  argument is quadratic in $q$; all other terms are at most quadratic; matching coefficients closes
  the system (reconstructed step by step on the BEGV source page, focus item 4).
- **[S]** Explicit formulas additionally need a **constant** $D_+$: the tanh solution and the formula
  for $B$ use that all $A(s)D_+$ commute (p. 113).
- **[S]** Assets interact only through $\Sigma$ (and drift): $D_+$ is diagonal; cross-asset quote skew
  comes from off-diagonal entries of $A$ (p. 117).

### 1c. CJR 2014: perturbation → linear ODEs, one asset, already with Hawkes flow
- **[S]** With one exponential per channel the HJB is Markov in $(t,q,\alpha,\lambda^\pm,\kappa^\pm)$, so
  no lift is needed; an expansion «correct to $o(\varsigma)$ where $\varsigma=\max(\phi,\alpha,\mathbb E[\varepsilon])$»
  (p. 427) gives first-order terms solving **linear** ODEs via Feynman–Kac, with matrix-exponential
  closed forms (pp. 438–441; [[cartea-2014-buy-low-sell]]).
- **[S]** The expansion ansatz is assumed, not proved; no comparison with an exact solution.
- Role here: the only pre-2024 closed form *with* mutually exciting flow, and it closes by being
  **first order in the inventory penalty**, i.e. by giving up the inventory nonlinearity that
  BEGV keeps.

---

## 2. What a Hawkes intensity adds to the state (Q2)

- **[S]** With exponential kernels the intensities are Markov state: one variable per (asset × side)
  for a single exponential, $n$ per channel for sums of exponentials
  ([[markov-lift]]; [[barzykin-2026-hawkes-driven-otc]] p. 8, eq. 46;
  [[jusselin-2021-persistent-order-flow]] Thm 3.1, p. 9). General kernels need a lift with
  convergence but no rate (Jusselin Props 3.1–3.2; [[martin-2026-market-making-hawkes]] Thm 2.4) or
  a truncation bound at rate $p^{-1/2}$ in regret ([[acero-2026-hawkes-structured-networks]] Thm 1).
- **[S]** The HJB gains two operators in $\lambda$ (proposal eq. 7):
  a **transport** term $-\sum_j\beta_j(\lambda_j-\mu_j)\partial_{\lambda_j}\theta$ (decay between
  events), and a **jump** term at post-event intensities $\lambda^{+j}=\lambda+DKe_j$.
- **Dimension [S+I]:** state $(q,\lambda)\in\mathbb Z^d\times\mathbb R^{2dn}$. Jusselin: lift dimension
  $2n+2$ for one asset, and «when n is larger than 2 it is very unlikely that simple finite
  differences methods can be used» (p. 11). Barzykin: $2Kd$ memory variables for $d$ factors and $K$
  sizes, infinite for power laws (p. 8). For the project's two-asset, one-exponential case:
  $\lambda\in\mathbb R^4$ plus two inventories, the proposal's own estimate (p. 20).

---

## 3. Where the closure breaks: it depends on who excites the flow (Q3)

The decisive modelling choice is [[who-excites-the-flow]]:
- **flow-driven**: every order excites, filled or not; this is the proposal's convention (p. 21),
  Barzykin's, CJR's, Martin–Tse's and Acero et al.'s;
- **fill-driven**: only the maker's own fills excite; this is Jusselin's (one market maker, every
  order is his fill) and Bergault et al.'s Hawkes-liquidity AMM model.

Write the generator of one order type $j=(i,s)$ arriving at rate $\lambda_j$, filling with probability
$f(\delta)$. The two conventions differ in **where the intensity jump sits**.

**Flow-driven [D]:**
$$\lambda_j\Big\{\underbrace{\theta(q,\lambda^{+j})-\theta(q,\lambda)}_{\text{jump, linear in }\theta}+\;z_i\,H\big(p^j\big)\Big\},\qquad p^j=\frac{\theta(q,\lambda^{+j})-\theta(q\pm z_ie_i,\lambda^{+j})}{z_i}.$$
Filled and unfilled orders both move $\lambda$ to $\lambda^{+j}$, so the shadow price is a finite
difference **in $q$ at fixed $\lambda^{+j}$**, which matches proposal p. 19, where $p^j$ is taken at
post-order intensities.

**Fill-driven [D]:**
$$\lambda_j\,z_i\,H\big(\tilde p^j\big),\qquad \tilde p^j=\frac{\theta(q,\lambda)-\theta(q\pm z_ie_i,\lambda^{+j})}{z_i}.$$
Only a fill moves $\lambda$, so the Hamiltonian's argument mixes two intensity levels.

### 3a. Consequence for the quadratic (BEGV) closure
| | Flow-driven | Fill-driven |
|---|---|---|
| Ansatz $\theta=-q^\top A(t,\lambda)q-q^\top B(t,\lambda)-C(t,\lambda)$ | $p^j$ affine in $q$ → **closes in $q$** with $\breve H$ **[D]** | $\tilde p^j\ni\frac{A(\lambda^{+j})-A(\lambda)}{z}q^2$ → $\tfrac12\alpha_2\tilde p^2$ gives $q^3,q^4$ → **does not close** **[S]** (Bergault et al. p. 17; reconstruction on [[bergault-2024-price-aware-automated]], focus item 1) |
| What remains | $A,B,C$ solve a **nonlocal transport-jump Riccati system in $\lambda$** (the jump term enters through $A(\lambda^{+j})$ inside $\breve H$) **[D]**, matching Barzykin's «system of transport-jump equations in the memory variables, not a small Riccati system» (p. 8) **[S]** | no finite reduction; full PIDE in $(q,\lambda)$ (3-D for one AMM pair, 4–5-D with price factors, Bergault et al. p. 17) **[S]** |
| Escape routes in the literature | freeze $\lambda$ at its forecast → Volterra–Riccati ODE ([[volterra-riccati]]) | replace Hawkes by Markov-modulated Poisson regimes, giving $p^2$ coupled Riccati ODEs (eq. 43) **[S]** |

### 3b. Consequence for the exact linear (GLFT) closure: the reverse
| | Flow-driven | Fill-driven |
|---|---|---|
| GLFT substitution $w=v^{-\gamma/k}$ with $v=v(t,q,\lambda)$ | unfilled orders contribute $\lambda_j[w(q,\lambda^{+j})-w(q,\lambda)]$, and after dividing by the common factor the fill term carries $\big(v(q,\lambda)/v(q,\lambda^{+j})\big)^{1+\gamma/k}$ → **nonlinear** **[D]**. The proposal states this too: «No exponential change of variables linearizes the Hawkes equation, because the value of an order that does not fill the market maker enters nonlinearly» (p. 18) **[S]** | the fill term becomes $c\,v(q\pm1,\lambda^{+j})$, decay drift and diffusion stay linear → **exact linear transport-jump equation** in $(q,\lambda)$ **[D]**; the GLFT reader reached the same conclusion independently ([[gueant-2013-dealing-inventory-risk]], focus points 2–3) |
| Deterministic $\Lambda(t)$ | stays exactly linear, $\dot v=M(t)v$ **[S+D]** (proposal p. 18 reports a numerical confirmation) | same |

**Reading [I]:** the two closed-form families pull in opposite directions. The proposal's
convention (flow-driven) is the one under which the **quadratic** route survives in reduced form
and the **exact linear** route is lost. Jusselin's convention (fill-driven, one market maker) is the
one under which GLFT stays exact. Jusselin uses a risk-neutral objective with running penalty, so
his paper does not exhibit this linearity. Whether an exact CARA linearisation of fill-driven
Hawkes market making exists in the literature is a **Q6 search item**; it is not claimed here as
new.

---

## 4. Anatomy of the approximation error under the flow-driven convention (Q3 continued)

From the exact problem to a closed-form quote, three approximations can be stacked, each with a
literature handle:

| Step | What is replaced | Source handle | Size evidence |
|---|---|---|---|
| (E0) lift truncation | general kernel → finite sum of exponentials | Jusselin, Martin–Tse, Acero et al. ([[markov-lift]]) | rate $p^{-1/2}$ in regret (Acero Thm 1); none with a constant |
| (E1) Hamiltonian expansion | $H\to\breve H$, makes $\theta$ quadratic in $q$ | BEGV Remark 1 | BEGV: one 2-asset P&L comparison within noise (p. 135); proposal preliminary: most of the 0.6 % directional regret of the state-feedback policy came from this step (proposal p. 6) |
| (E2) forecast freezing | the transport-jump system in $\lambda$ → ODE along $m_t(\cdot)$ | Barzykin eq. 23; covariance correction eq. 38; state-feedback eqs. 42–43 | Barzykin Table 3 (p. 16): state-feedback 0.080/0.083/0.170 % vs exact (checked against the PDF); proposal reproduction: 0.6 %, of which 0.25 % with the exact Hamiltonian and 0.09 % with the pre-order forecast (p. 6), **contested** |

**[D/I]** In this decomposition, hypothesis H3 of the proposal (Riccati policies lose mostly through
E1, not E2) is a statement about the relative size of E1 and E2. The flow-driven derivation in
§3a shows the two are separable: E1 alone leaves an exact-in-$q$ but $\lambda$-dependent system;
E2 alone (the exact Hamiltonian with a frozen forecast) is the proposal's "second version"
(p. 20). The comparison the proposal plans is therefore well defined.

---

## 5. What carries over to d assets with cross-asset excitation

- **[S]** No core source does it. Barzykin, Bergault et al. (2024), Jusselin, CJR and Martin–Tse are
  single-asset or single-pair; Martin–Tse leave even buy/sell cross-excitation to future work
  (p. 16, checked); Acero et al. run one 2-asset RL configuration (same-side cross-asset
  excitation 0.28, $\rho(K)=0.40$, p. 5, checked) and claim only «Similar results extend to the
  multi-asset case» for their theory (p. 2, checked).
- **[D] Flow-driven, quadratic route, d assets:** with $\lambda\in\mathbb R^{2d}$, the ansatz
  $\theta=-q^\top A(t,\lambda)q-\dots$ still closes in $q$. Cross-asset excitation enters through the
  jump targets $\lambda^{+j}=\lambda+DKe_j$, so the matrix $A(t,\lambda)$ couples assets **both**
  through $\Sigma$ (as in BEGV) **and** through its dependence on every intensity. The exact
  reduced object is a $d\times d$ matrix Riccati system indexed by a $2d$-dimensional continuous
  state, nonlocal in that state.
- **[S+D] Frozen forecast:** BEGV's Prop. 1 algebra survives with deterministic time-varying
  coefficients. Cross-asset excitation then enters only through the *diagonal* $D_+(t)$, built from
  the forecast of all intensities (proposal eqs. 8–10; BEGV page, focus item 6). A burst in asset
  $i$ raises the forecast for asset $j$ via off-diagonal $K$, which raises $D_+^{jj}(t)$ and moves
  every correlated quote through $A$. The tanh formula, the commuting propagator and the ergodic
  $\Gamma$ are lost (Riccati integrated numerically).
- **[I]** Consequently, a policy that uses only the *diagonal* blocks of $K$ (hypothesis H2's
  comparator) differs from the cross-aware one only through the forecast feeding $D_+(t)$. In the
  frozen-forecast closed form, cross-asset excitation never enters the off-diagonal of $D_+$; it
  reaches other assets only through $\Sigma$-coupling in $A$. This is a testable prediction: with
  $\Sigma$ diagonal (uncorrelated prices), the frozen-forecast closed form makes quotes of asset $j$
  react to a burst in asset $i$ **only** via asset $j$'s own forecasted liquidity, never via
  inventory hedging. **Correction (2026-10-26, [D], Prover review of the Stage 2a design; to
  verify):** the exact solution does *not* do more for this objective. With $\Sigma$ diagonal and a
  separable terminal penalty, the flow-driven HJB separates additively,
  $\theta=\sum_i\theta_i(t,q_i,\lambda)$: each Hamiltonian uses differences in $q_i$ only, and the
  jump, transport and penalty terms all split. So $A$ stays diagonal even exactly; cross-asset
  bursts move $A_{ii}(\lambda)$, never $q_j$-hedging. Cross-asset inventory coupling therefore
  needs correlated prices ($\Sigma$ off-diagonal), and any test of it must use correlated $\Sigma$.
- **Fill-driven, d assets [I]:** cross-asset fills raising another asset's intensity reproduce the
  simultaneity of §3a across assets; the quadratic ansatz fails as in Bergault et al. (2024). GLFT's
  exact linear route survives formally but on $(2Q+1)^d\times\mathbb R^{2d}$ points.

---

## Evidence base

| Claim | Sources | Strength |
|---|---|---|
| GLFT linearisation and its conditions | [[gueant-2013-dealing-inventory-risk]] | [S], published original |
| BEGV closure, tanh, commutation, assumptions | [[bergault-2021-closed-form-approximations]] | [S], published original; spot-checked |
| CJR first-order linear closure | [[cartea-2014-buy-low-sell]] | [S], published original; spot-checked |
| Lift dimension / convergence | [[jusselin-2021-persistent-order-flow]] (preprint), [[martin-2026-market-making-hawkes]], [[acero-2026-hawkes-structured-networks]], [[barzykin-2026-hawkes-driven-otc]] | [S]; Jusselin page numbers are preprint pages |
| Fill-driven breaks quadratic closure | [[bergault-2024-price-aware-automated]] p. 17 | [S] conclusion; step-by-step is the source reader's reconstruction |
| Lift + quadratic → transport-jump system | [[barzykin-2026-hawkes-driven-otc]] p. 8 | [S], checked |
| Flow-driven: quadratic closes in $q$ with $\lambda$-dependent coefficients | this page §3a | **[D] only**, consistent with Barzykin p. 8 and proposal p. 19 |
| GLFT: fill-driven linear, flow-driven nonlinear | this page §3b; GLFT page focus; proposal p. 18 (flow-driven half) | **[D]**, the fill-driven half has no source |
| Regret numbers | Barzykin Table 3; proposal p. 6 | [S]; reproduction gap contested |

**Gaps in the evidence:** only one paper (Barzykin) measures closed-form regret against an exact
Hawkes solution. No source measures E1 and E2 separately except the proposal's own preliminary work.
The multi-asset statements of §5 rest entirely on [D]/[I].

## What stays open

1. **Verify [D] items independently** (proposal p. 21 rule). Priority: §3a flow-driven closure in
   $q$ and the exact form of the $\lambda$-system; §3b fill-driven GLFT linearity.
2. **Q6:** is the fill-driven CARA linearisation (§3b) known? Is any multi-asset Hawkes Riccati
   system (§5) published? This feeds plan Task 6 (literature search) and `gap-verification`.
3. **Which convention is empirically right** for the proposal's data (exchange futures: all
   aggressors excite, so flow-driven seems natural; OTC RFQ: Barzykin's requests vs fills). This
   feeds `cross-asset-excitation-evidence` (Task 10).
4. **The H2 prediction of §5 [I]** (with uncorrelated prices, frozen-forecast quotes ignore
   cross-asset inventory effects) should be stated as a sub-hypothesis in the Stage-2
   pre-registration if it survives verification.
5. **Contested numbers:** Barzykin's 0.17 % vs the proposal's 0.6 %; the Poisson comparator at
   baseline μ; Jusselin's «10 %» vs his Fig. 1; Acero et al.'s «45–90 %» vs Table 1.
6. Not yet read: the 59 non-core sources (Task 8), several of which (Bergault–Guéant 2023 MMPP,
   Barzykin et al. multi-currency, Rosenbaum–Zhang) bear on §1b and §5.
