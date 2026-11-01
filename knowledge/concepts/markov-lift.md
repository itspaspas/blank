---
title: "Markov lift of a Hawkes intensity"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [hawkes, stochastic-control, dimensionality]
---

# Markov lift of a Hawkes intensity

## Definition
A Hawkes intensity $\lambda_t=\mu+\int_0^t g(t-s)\,dN_s$ is path-dependent: the control problem's
state is the whole order-flow history. A **Markov lift** replaces that history by finitely many
"memory" state variables whose joint dynamics are Markov, so that dynamic programming (an HJB
equation in inventory × memory) applies. With an exponential kernel $g(u)=\alpha\beta e^{-\beta u}$
the lift is exact with one variable per kernel; general kernels are approximated by a finite
expansion.

## Where it comes from
Lifts for general kernels in the four core works ingested so far:

| Route | Kernel class | Variables added | Source |
|---|---|---|---|
| Exponential kernel | exponential | 1 per (side × type) | [[barzykin-2026-hawkes-driven-otc]] (exact 2-D lift, eq. 46, p. 13) |
| Sum of exponentials / quadrature over decay rates | completely monotone (Bernstein) | $p$ per channel | [[acero-2026-hawkes-structured-networks]] (eq. 3, Prop. 1, p. 3) |
| Mercer expansion $K(t,s)\approx\phi(t)^\top\phi(s)$ | general, not necessarily completely monotone | $n$ per kernel ($4n$ for one asset with buy/sell flow and fill elasticity) | [[martin-2026-market-making-hawkes]] (pp. 6–9, eq. 2.10, Thm 2.4) |
| Exact function-valued state $\theta_t(u)=\int K(u-s)\,dN_s$ on a locally compact domain; then sum of exponentials | completely monotone ($L^1$) | $2n+2$ (price, inventory, $c^a,c^b\in\mathbb R^n$) | [[jusselin-2021-persistent-order-flow]] (Lemma 2.1 p. 3; Thm 3.1 p. 9; density Lemma 3.1 p. 10; preprint pages) |
| None needed | one exponential per channel | intensities and depths are already state | [[cartea-2014-buy-low-sell]] (HJB 5.3, pp. 426–427) |

Jusselin proves existence and uniqueness of a viscosity solution of the path-dependent HJB and
convergence of the lifted value functions and controls, without a rate (Thm 2.1 p. 7; Props 3.1–3.2,
pp. 7–8). He also notes the practical limit: with dimension $2n+2$, «when n is larger than 2 it is
very unlikely that simple finite differences methods can be used» (p. 11, checked against the PDF).

Convergence: Martin & Tse prove $V_n\to V$ without a rate (Thm 2.4, p. 7). Acero et al. bound
the kernel $L^2$ error at rate $p^{-1/2}$ in the regret (Thm 1, p. 3). Bergault et al. note that
power-law kernels "do not lead to Markovian setups" ([[bergault-2024-price-aware-automated]],
fn. 8, p. 11). Barzykin counts $2Kd$ memory variables for a $d$-factor, two-sided, $K$-size model,
and an infinite-dimensional state for a power law (p. 8).

## How it is applied
The lifted state enters the HJB through two terms: a **transport** term (memory decays
between events, $-\sum_j\beta_j(\lambda_j-\mu_j)\partial_{\lambda_j}\theta$) and a **jump** term
(each event moves memory to $\lambda+DKe_j$). Solved on grids for 1–2 memory variables
(Barzykin's exact benchmark), by PINN (Martin & Tse), or implicitly learned (Acero et al.'s HSN
features recover $\lambda$ with probe MSE $<10^{-6}$, Table 2, p. 6).

## Criticism
- The lift does **not** rescue the closed form. Barzykin: lift + quadratic expansion yields «a
  system of transport-jump equations in the memory variables, not a small Riccati system» (p. 8).
- Dimension grows with assets × sides × exponentials; for $d$ assets with cross-asset kernels this
  is the curse of dimensionality the closed-form route was meant to avoid (project inference, not
  stated by any source yet).

## Not to be confused with
[[intensity-forecast]]: the forecast is a deterministic function of today's memory, not an
extra state. Markov-modulated Poisson flow (finite regimes, [[bergault-2024-price-aware-automated]])
is an alternative to a lift, not a lift.

## Relevance to this project
Q2 of the design: the lift defines the exact problem against which every closed form is measured,
and its dimension is what makes an exact multi-asset benchmark hard.

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[jain-2025-impulse-control-hawkes]]: 12-type model with pair-specific decays needs a 144-dimensional lift (p. 9); general kernels have no SDE form (p. 7)
- [[tarditi-2026-hawkes-process-models]]: exact 3-D grid (q, λ+, λ−) via IMEX (p. 46)
- [[yuan-2026-dynamic-pricing-self]]: excitement level x_t as 1-D sufficient statistic (Lemma 1, p. 11)
- [[zarezade-2018-steering-social-activity]]: Prop. 1 (p. 5)
- [[khabou-2025-markov-approximation-hawkes]]: signed non-monotone L¹ kernels; rate |V₀ⁿ−V₀| ≤ ‖ϕₙ−ϕ‖₁C₁e^{C₂T} for Lipschitz rewards only (Thm 4.1, p. 11)
- [[bielecki-2026-continuous-time-reinforcement]]: convergence uniform over controls even for action-dependent kernels, no rate (Thm 3.10, p. 19)

## Sources
[[barzykin-2026-hawkes-driven-otc]] · [[martin-2026-market-making-hawkes]] ·
[[acero-2026-hawkes-structured-networks]] · [[bergault-2024-price-aware-automated]]
