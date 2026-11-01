---
title: "Zarezade et al. 2018 — Steering Social Activity: A Stochastic Optimal Control Point of View"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: zarezade-2018-steering-social-activity
depth: standard
tags: [hawkes, multivariate-hawkes, controlled-intensity, matrix-riccati, lq-control, jump-sde, social-networks, outside-market-making]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Actions are «multidimensional Hawkes processes» (p. 2) with exponential kernel; Prop. 1 (p. 5): «the tuple (N(t), λ(t)) is a doubly stochastic Markov process» with dλ = [λ0' + ωλ0 − ωλ]dt + C dN (eq. 3)."
  - target: markov-lift
    type: builds-on
    confidence: extracted
    because: "Exponential kernels chosen because «the dynamics of the corresponding intensity can be expressed by a linear SDE with jumps» (fn. 1, p. 5); the state of the global problem is the intensity vector λ(t) itself (Def. 8, p. 13)."
  - target: matrix-riccati-equation
    type: supports
    confidence: extracted
    because: "Lemma 10 (p. 14): J = f + gᵀλ + ½λᵀHλ with Ḣ = (ωI−B)ᵀH + H(ωI−B) + HBS⁻¹BᵀH + Q, «a matrix Riccati differential equation» — exact quadratic closure in the multivariate Hawkes intensity."
  - target: branching-matrix
    type: mentions
    confidence: extracted
    because: "Influence matrix B = (β_uv) «sparse nonnegative» (p. 5) enters the Riccati drift as (ωI − B) (p. 14); no stability condition on ρ(B)/ω is stated."
---

# Steering Social Activity: A Stochastic Optimal Control Point of View

## Bibliographic Details

Zarezade, Ali; De, Abir; Upadhyay, Utkarsh; Rabiee, Hamid R.; Gomez-Rodriguez, Manuel. 2018.
*Steering Social Activity: A Stochastic Optimal Control Point of View*. arXiv:1802.07244v1
[cs.SI], 19 February 2018. 28 pp. Extended version of the RedQueen WSDM 2017 paper («Preliminary
version of this work appeared in [42]», fn. ∗, p. 1); a later journal version, if any, was not
checked. Affiliations: Sharif University of Technology; MPI for Software Systems.

**Read: arXiv 1802.07244v1 (preprint); page/equation numbers follow it.** (Non-core work, outside
market making; preprint accepted under the project's preprint policy.)

### Notation map (source → project)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $N(t)$, $\lambda(t)\in\mathbb R^n$ | organic actions of $n$ users, Hawkes intensity (eq. 2) | $\lambda_t$ |
| $\lambda_0$ | exogenous (baseline) intensity | $\mu$ |
| $B=(\beta_{uv})$, $C$ | influence (excitation) matrix; jump size of $\lambda$ | $DK$ (jump matrix), cf. $K$ |
| $\omega$, $\kappa_\omega(t)=e^{-\omega t}$ | common decay, exponential kernel | $\beta$ (scalar, all components) |
| $P(t)$, $u(t)$ | incentivised actions and their intensity = **the control** | no project symbol |
| $\gamma(t)$, $M(t)$, $D=\mathrm{diag}(\alpha_j)$ | feed intensity / counts from other broadcasters (local problem) | ⚠ $\gamma$ is not risk aversion; ⚠ $D$ not $\mathrm{diag}(\beta)$ |
| $r(t)$ | rank (visibility) of the user's last post in a follower's feed (eq. 5) | no project symbol |
| $J$; $H(t),g(t),f(t)$ | cost-to-go; quadratic, linear, constant coefficients (Lemma 10) | $-\theta$; $H\leftrightarrow A$ (on $\lambda$, not on $q$!) |
| $Q,S,F$ | running reward on $\lambda$, control cost, terminal reward | — |
| $q$, $s(t)$ | posting cost, follower-online significance (local problem) | ⚠ $q$ not inventory |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (two technical novelties: intensities as controls; doubly stochastic intensities) | 1–2 |
| ✓ | 1.1 Related work (when-to-post, activity shaping, stochastic control of point processes) | 2–3 |
| ✓ F1 | 2.1 Temporal point processes; 2.2 actions and feeds; 2.3 Hawkes model of endogenous/exogenous actions (eqs. 1–4), Prop. 1 (Markov jump-SDE representation) | 3–5 |
| ✓ F1 | 3 Local problem "when-to-post": visibility SDE (eq. 6), problem (7)–(8), cost-to-go (10), Bellman (11), HJB (13)–(15), Lemma 5, Thm. 6 (RedQueen), multiple followers (16), oracle (Alg. 2) | 5–11 |
| ✓ F1 | 4 Global problem "activity maximisation": controlled excitation (17)–(18), problem (19), HJB (22), control (23), PDE (24), Lemma 10 (matrix Riccati), Thm. 11, Alg. 3 (Cheshire) | 11–15 |
| ✓ | 5.1 When-to-post experiments (synthetic Hawkes feeds; 2,000 Twitter users) | 15–18 |
| ✓ | 5.2 Activity maximisation experiments (Kronecker networks; five Twitter datasets) | 18–22 |
| ✓ | 6 Conclusions and future work | 22 |
| ✓ F1 | Appendices A–G (proofs of Prop. 1, Bellman, Lemmas 4, 5, 9, 10; monotonicity of $J$ in $\lambda$) | 23–26 |
| — | References | 26–28 |

## Kernthesen

### 1. ⭐⭐ The controls are point-process intensities, not real-valued signals, and the controlled dynamics are doubly stochastic (p. 2)

«I. The control signals are conditional (posting) intensities, which are used to sample stochastic
events … our approach requires another layer of stochasticity. II. The (posting) intensities are
stochastic Markov processes and thus the dynamics are doubly stochastic. This requires us to redefine
the cost-to-go to incorporate the instantaneous value of these intensities as additional arguments»
(p. 2). The resulting policies are closed-loop feedback in the current intensity state, with
coefficients computed once offline (p. 3).

### 2. ⭐⭐ An exponential-kernel multivariate Hawkes process is a Markov jump-SDE in its intensity (Prop. 1, p. 5)

For $\lambda(t)=\lambda_0(t)+C\int_0^t\kappa_\omega(t-s)dN(s)$, $\kappa_\omega=e^{-\omega t}$:
$d\lambda(t)=[\lambda_0'(t)+\omega\lambda_0(t)-\omega\lambda(t)]dt+C\,dN(t)$ (eq. 3), so $(N,\lambda)$ is a
«doubly stochastic Markov process» (p. 5). A **single** decay $\omega$ for all dimensions. Exponential
kernels are chosen for this reason, while acknowledging that «power-law may have higher predictive
performance in some scenarios» (fn. 1, p. 5).

### 3. Local problem: visibility in a reverse-chronological feed obeys a jump SDE reset by the user's own posts (pp. 6–7)

Rank of user $i$'s last post in follower $j$'s feed: $dr_{ij}=-r_{ij}\,dN_i+dM_{j\backslash i}$ (eq. 6),
with feed arrivals $M$ a Hawkes process with intensity $\gamma$ (eq. 1, local view, diagonal
$D=\mathrm{diag}(\alpha_j)$). The user's posting intensity $u(t)=\lambda_i(t)$ is the control (eq. 7).
In this local problem the control does **not** excite $\gamma$: the user's posts only reset $r$.

### 4. ⭐ Quadratic loss in rank and intensity gives a value linear in $r$ and an optimal intensity linear in $r$ (pp. 9–10)

HJB (13); with $\phi=\tfrac12r^2(t_f)$, $\ell=\tfrac12s(t)r^2+\tfrac12qu^2$: $u^*=q^{-1}[J(r,\gamma,t)-J(0,\gamma,t)]$
(14). Lemma 5: «In the space of m-degree polynomials» the unique solution is
$J=f(t)+\sqrt{s(t)q}\,r(t)+\sum_jg_j(t)\gamma^j(t)$ (p. 9), hence Thm. 6:
$u^*(t)=\sqrt{s(t)/q}\,r(t)$ (p. 10), and $u^*=\sum_i\sqrt{s_i/q}\,r_i$ for several followers (16).
Remarkably, the optimal rule does not depend on the Hawkes parameters of the feed at all (only the
$g_j$ do).

### 5. RedQueen samples the optimal policy by superposing Poisson processes (p. 10, Alg. 1)

Because $u^*$ is linear in $r$, which increments by one at each competing post, the policy is a
superposition of $r(t)$ Poisson processes with rate $\sqrt{s/q}$ started at the rank jumps; the
algorithm needs $O(1)$ space per follower (p. 10). An oracle with known future feed (Alg. 2, a
discrete DP of complexity $O(m^2)$) serves as the benchmark (pp. 10–11).

### 6. ⭐⭐ Global problem: incentivised actions are a controlled point process that excites the network through the same matrix $B$ (pp. 11–12)

$\lambda(t)=\lambda_0+B\int\kappa_\omega(t-s)dN(s)+B\int\kappa_\omega(t-s)dP(s)$ (eq. 17), with
$\mathbb E[dP]=u\,dt$; equivalently $d\lambda=[\omega\lambda_0-\omega\lambda]dt+B\,dN+B\,dP$ (eq. 18, Prop. 7).
**The control feeds the intensity:** each incentivised action of user $i$ (rate $u_i$) jumps $\lambda$ by
the column $b_i$. $P$ itself is excluded from $\lambda$'s own count, so the objective rewards only
the triggered follow-ups (p. 12). Fn. 8 (p. 12): a different matrix $C\ne B$ for incentivised actions is
a straightforward change.

### 7. ⭐⭐ The state of the global problem is the $n$-vector of Hawkes intensities only (Def. 8, p. 13)

$J(\lambda(t),t)=\min_u\mathbb E[\phi(\lambda(t_f))+\int_t^{t_f}\ell(\lambda,u)ds]$ (eq. 20). No counts,
no inventory, no history beyond $\lambda$ (exponential kernel). HJB (eq. 22):
$0=J_t+[\omega\lambda_0-\omega\lambda]^\top\nabla_\lambda J+\lambda^\top\Delta_BJ+\min_u\{\ell(u,\lambda)+u^\top\Delta_BJ\}$,
$(\Delta_BJ)_i=J(\lambda+b_i,t)-J(\lambda,t)$ (p. 13). Both organic events (rate $\lambda$) and controlled
events (rate $u$) produce the **same** jump $b_i$.

### 8. ⭐⭐ With quadratic reward on $\lambda$ and quadratic control cost, the value is exactly quadratic in $\lambda$ and $H$ solves a matrix Riccati ODE (pp. 13–14)

$\ell=-\tfrac12\lambda^\top Q\lambda+\tfrac12u^\top Su$, $\phi=-\tfrac12\lambda^\top F\lambda$; unconstrained minimiser
$u^*=-S^{-1}\Delta_BJ$ (23). Lemma 10: $J=f+g^\top\lambda+\tfrac12\lambda^\top H\lambda$ with
$\dot H=(\omega I-B)^\top H+H(\omega I-B)+HBS^{-1}B^\top H+Q$,
$\dot g=[\omega I-B^\top+HBS^{-1}B^\top]g-\omega H\lambda_0+\tfrac12[HBS^{-1}-I]\mathrm{diag}(B^\top HB)$,
$H(t_f)=-F$, $g(t_f)=0$ (p. 14). «the first differential equation is a matrix Riccati differential
equation … and the second one is a first order differential equation which has closed form
solution» (p. 14). Mechanism: for constant jumps $b_i$, $\Delta_BJ$ is **affine** in $\lambda$, so
$\lambda^\top\Delta_BJ$ and $(\Delta_BJ)^\top S^{-1}\Delta_BJ$ are quadratic. The drift is linear, so the
ansatz closes.

### 9. ⭐ The optimal incentive intensity is affine in the current intensities (Thm. 11, p. 14)

$u^*(t)=-S^{-1}[B^\top g(t)+B^\top H(t)\lambda(t)+\tfrac12\mathrm{diag}(B^\top H(t)B)]$ (p. 14). Feasibility
$u\ge0$ is argued from $(\Delta_BJ)_i\le0$, i.e. $J(\lambda+b_i)\le J(\lambda)$ (Appendix F, p. 26), with $S$
non-negative (in practice diagonal, fn. 9, p. 13). Cheshire (Alg. 3) again samples by superposition and
needs $O(n)$ operations per event after precomputing $H$, $g$ (pp. 14–15).

### 10. Uniqueness of the polynomial solution is shown by degree-matching, not by a verification theorem (Appendices D, G, pp. 24–26)

For a cubic proposal, matching fourth-degree terms gives $\sum_k(\sum_\ell B_{\ell k}^2)H_{ijk}^2=0$, so
cubic coefficients vanish; «any proposal with arbitrary degree m ≥ 2, would result in a quadratic
optimal cost» (p. 26). Uniqueness is claimed *within polynomials*; no general verification theorem,
no admissibility/integrability argument, and no condition preventing finite-time blow-up of the
Riccati (they cite a thesis on Riccati «with solution singularities», ref. [14], p. 14).

### 11. ⭐ Empirically: small incentive budgets trigger large activity increases; Cheshire beats deterministic-control baselines (pp. 18–22)

64-node Kronecker networks: «a relatively small number of incentivized actions (… ∼3,600 actions)
result in a dramatic increase in the overall number of (non directly incentivized) actions … (∼96,000
vs ∼4,800 actions)» (p. 18). On 512-node networks Cheshire triggers «up to 50%–100% more posts than
the second best performer» (p. 19). On five Twitter datasets: «up to 100%–400% more posts» (p. 21) and
reaches a 30,000-tweet milestone «20%–50% faster … for low budgets» (p. 21). Baselines OPL
(offline-optimal deterministic, Farajtabar et al. 2014) and MSC (multistage) are open-loop or
stage-wise (pp. 18–19). Evaluation is simulation from fitted Hawkes models, not live intervention
(p. 22).

### 12. ⭐ RedQueen beats the state of the art on real Twitter timelines (pp. 15–18)

Synthetic Hawkes feeds ($\gamma_0=10,\alpha=1,\omega=10$, Fig. 2, p. 15): RedQueen is within 3× of the
oracle's position-over-time when the budget is < 30% of competing posts and achieves > 40% of the
oracle's time at the top (p. 16). On 2,000 Twitter users: «0.28× lower average position and 3.5× higher
time at the top, in average, than the broadcasters' true posts» (p. 18).

### 13. Stated limitations: quadratic losses, constant parameters, single controller (p. 22)

«our algorithms optimize quadratic losses and assume the model parameters do not change over time»
(p. 22); multi-broadcaster (competitive, cooperative, adversarial) settings and algorithmic feed
ranking are future work (p. 22); the local user is assumed to have only a «local view» (p. 5).

## What this source does not address

- **Market making, inventory, prices.** No inventory, price, fills, spreads or risk aversion; the
  "reward" is the level of the Hawkes intensity itself.
- **Control through a nonlinear fill probability.** The control *is* an intensity with a quadratic
  cost; it is never a price/quote that thins an exogenous intensity.
- **Non-exponential or heterogeneous-decay kernels.** One common $\omega$; power laws acknowledged
  only in fn. 1 (p. 5).
- **Stability / well-posedness of the Riccati.** No condition on $\rho(B)$ vs $\omega$, no blow-up
  analysis, no verification theorem (Kernthese 10).
- **Approximation or regret against an exact benchmark.** The global solution is claimed exact; the
  comparison is only against heuristics and open-loop methods.

## Model card

| Field | Value |
|---|---|
| Assets | n/a — no assets; $n$ users (nodes) of a social network (512 in synthetic, Twitter sets in Table 1, p. 21) |
| Kernel | exponential, single decay $\omega$ (eqs. 1–3, fn. 1, p. 5) |
| Excitation | self and cross-node (full influence matrix $B$, sparse on the graph, p. 5); local problem uses diagonal $D$ on feeds (eq. 1) |
| Who excites the flow | all events: organic actions $N$ **and** the controlled actions $P$ (rate $u$ = control) jump $\lambda$ by the same $b_i$ (eq. 18, p. 12). Closest market-making analogue: an excitation that the controller can purchase directly |
| Objective | quadratic: maximise $\tfrac12\lambda^\top Q\lambda$ (running) and $\tfrac12\lambda^\top F\lambda$ (terminal) net of $\tfrac12u^\top Su$ (p. 13); local: minimise $\tfrac12s r^2+\tfrac12qu^2$ (p. 9) |
| Solution method | exact closed-loop: HJB on the Markov intensity state, quadratic value, matrix Riccati ODE for $H$ + linear ODE for $g$ (Lemma 10, p. 14); local problem: value linear in rank, $u^*=\sqrt{s/q}\,r$ (Thm. 6) |
| Benchmark | oracle DP (local); OPL, MSC, PageRank/degree heuristics, uncontrolled (global) |
| Reported regret / gap numbers | no regret vs an exact optimum; relative activity gains: +50–100% (synthetic, p. 19), +100–400% (Twitter, p. 21), milestone 20–50% faster (p. 21); RedQueen 0.28× position, 3.5× time-at-top vs real posts (p. 18) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

*Read as a non-market-making control source: what its machinery says about Riccati closures under
mutually exciting jumps, and whether the control feeds the intensity.*

**Carries Kernthesen 1, 2, 6, 7, 8, 9, 10.**

### What this focus needs beyond the Kernthesen

1. **What exactly is the state, and does the control feed the intensity?** In the global problem the
   state is the $n$-vector $\lambda(t)$ alone, made Markov by a single exponential decay (Prop. 1,
   Def. 8). The control $u$ is the intensity of an extra point process $P$, and **yes, it feeds the
   Hawkes intensity**: every controlled event jumps $\lambda$ by $b_i$, the same column as an organic
   event (eq. 18). In the local problem the state is $(r,\gamma)$. The control resets $r$ but does
   not excite $\gamma$.
2. **Why the matrix Riccati closes exactly [D from eqs. 22–24].** Four conditions hold at once:
   (i) a drift linear in $\lambda$; (ii) constant jump vectors $b_i$, so $\Delta_BJ$ is affine in
   $\lambda$ for quadratic $J$; (iii) intensity-weighted terms $\lambda^\top\Delta_BJ$ are then
   quadratic; (iv) the control enters linearly in the generator ($u^\top\Delta_BJ$) with quadratic
   cost, so the minimised Hamiltonian is $-\tfrac12\Delta_BJ^\top S^{-1}\Delta_BJ$, again quadratic.
   This is the cleanest available instance of **"controlled multivariate Hawkes + LQ ⇒ matrix
   Riccati in $\lambda$"**.
3. **Why it does not transfer to market making [I].** The market maker's value is quadratic in
   *inventory* $q$, with coefficients that depend on $\lambda$. Write $\theta=-q^\top A(\lambda)q-\dots$.
   The term $\lambda_j\,H(p^j)$ with $p^j$ affine in $q$ gives $\lambda_j\,h_2(p^j)^2$. If $A$ is
   affine in $\lambda$ (the polynomial analogue of Zarezade's ansatz), $p^j$ contains
   $A(\lambda^{+j})q$, and $\lambda_j(p^j)^2$ is **cubic in $\lambda$** times $q^2$. A joint polynomial
   ansatz in $(q,\lambda)$ therefore does not close. Zarezade's degree-matching argument (Kernthese
   10) closes only because reward and control cost are quadratic in $\lambda$ and $u$ directly, and
   no state variable multiplies a squared jump. This supports the project's D2 position: under
   flow-driven Hawkes market making, $A,B,C$ must be genuine functions of $\lambda$ (transport-jump
   system, [[problem-anatomy]] §3a), or $\lambda$ must be frozen at its forecast
   ([[volterra-riccati]]). An exact finite Riccati of Zarezade's type would need the market-making
   Hamiltonian to be linear in the control intensity. GLFT's exponential fill with CARA does not
   give that.
4. **What does carry over to several assets with cross-asset excitation.** (a) The Markov
   representation $d\lambda=(\dots)dt+B\,dN$ with a full off-diagonal $B$ is exactly the project's
   cross-asset jump structure $\lambda^{+j}=\lambda+DKe_j$ (with one common decay; the project's
   $D=\mathrm{diag}(\beta)$ generalises it). (b) The term $(\omega I-B)$ in the Riccati is the
   mean-reversion matrix of the intensity; in market making the same matrix governs the forecast
   $m_t(u)$ ([[intensity-forecast]]). (c) The **"controller excites the flow"** structure (eq. 18)
   is the social-network counterpart of the fill-driven convention ([[who-excites-the-flow]]),
   where the market maker's own fills raise future intensity. Here it costs nothing structurally,
   because the control enters linearly. In market making the fills come through
   $\lambda_jf(\delta)$ and the simultaneity problem of Bergault et al. reappears
   ([[bergault-2024-price-aware-automated]]).
5. **Bearing on the gap claim.** Neither refutes nor qualifies it directly: no market making, no
   inventory. It is useful precedent for the narrower statement that *LQ control of a multivariate
   exponential Hawkes intensity has an exact matrix-Riccati solution*. It should be cited as such,
   so that the project's novelty claim is not phrased as "first Riccati for controlled
   multivariate Hawkes".
6. **Bearing on D1 (fill-driven CARA linearisation).** Indirect. Zarezade's local problem shows
   that a controlled reset process gives a value *linear* in the reset state. This is not the GLFT
   exponential-transform linearity. No CARA.

### Direct quotes (for the draft)

> "I. The control signals are conditional (posting) intensities, which are used to sample stochastic events (i.e., stories to post). In contrast, previous work considered the control signal to be a time-varying real vector." (p. 2)

> "Then, the tuple (N(t), λ(t)) is a doubly stochastic Markov process, whose dynamics can be defined by the following jump SDEs: dλ(t) = [λ0′(t) + ωλ0(t) − ωλ(t)] dt + C dN(t)" (p. 5)

> "In the above lemma, note that the first differential equation is a matrix Riccati differential equation, which can be solved using many well-known efficient numerical solvers [14], and the second one is a first order differential equation which has closed form solution." (p. 14)

> "Here, we opt for exponential kernels since, in such case, the dynamics of the corresponding intensity can be expressed by a linear SDE with jumps and this will be helpful in the derivation of our stochastic optimal control algorithms." (fn. 1, p. 5)

### Examples & illustrations (for later drafting)

- Lemma 10 (p. 14) is a two-line worked example for the claim "intensity × affine jump closes; the
  market-making Hamiltonian does not". Set its $\dot H$ beside BEGV's matrix Riccati and the
  flow-driven transport-jump system of [[problem-anatomy]] §3a.
- Fig. 6 (p. 19): ∼3,600 purchased events raise organic activity from ∼4,800 to ∼96,000 on a
  64-node network. This is a vivid picture of the leverage of controlled excitation near
  criticality. It also hints at the blow-up risk of rewarding $\lambda^\top Q\lambda$ (no stability
  condition is stated).

### Boundary of this focus

The transfer to market making (items 3–5) is the project's derivation and inference. The paper never
mentions finance. Its "exact" claim rests on polynomial degree-matching without a verification
theorem. Its numbers are activity gains against heuristics, not regret against an optimum, so it
cannot inform the three-way comparison.

## Mentioned entities

- Concepts: [[hawkes-process]], [[markov-lift]], [[matrix-riccati-equation]], [[branching-matrix]], [[who-excites-the-flow]], [[intensity-forecast]], [[volterra-riccati]].
- Other works (not in library): Farajtabar et al. 2014 (OPL, "Shaping social activity by incentivizing users"); Farajtabar et al. 2016 (MSC, multistage campaigning); Karimi et al. 2016 (smart broadcasting); Wang et al. 2016/2017 (SDE framework / variational policy for guiding point processes); Hanson 2007 (control of jump-diffusions); Hawkes 1971.

## Connections

- Supports: [[matrix-riccati-equation]]: exact matrix Riccati for LQ control of a multivariate exponential Hawkes intensity (Lemma 10).
- Builds on: [[hawkes-process]], [[markov-lift]] (exponential-kernel Markov representation, Prop. 1).
- Contrast with: [[begv-2021-model]] / [[barzykin-2026-hawkes-driven-otc]]: Riccati in inventory with intensity-dependent coefficients, which closes only by expansion or by forecast freezing.
- Same exact-quadratic mechanism in finance, with exogenous Brownian-driven flow: [[fujii-2015-optimal-position-management]].
- Fill-driven analogue (controller's events excite): [[who-excites-the-flow]], [[bergault-2024-price-aware-automated]].
