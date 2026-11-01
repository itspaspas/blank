---
title: "Matrix Riccati equation in market making"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [closed-form, riccati]
---

# Matrix Riccati equation in market making

## Definition
In [[begv-2021-model]], with the [[hamiltonian-quadratic-approximation]], the inventory-quadratic
coefficient $A(t)$ of the reduced value function solves
$$A'(t)=2A(t)D_+A(t)-\tfrac12\gamma\Sigma,\qquad A(T)=0,\qquad D_+=\mathrm{diag}\big((\alpha_2^{i,b}+\alpha_2^{i,a})z^i\big),$$
with closed-form solution
$A(t)=\tfrac12 D_+^{-1/2}\hat A\tanh(\hat A(T-t))D_+^{-1/2}$, $\hat A=\sqrt\gamma\,(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}$
(eq. 13), and ergodic limit $A\to\tfrac12\sqrt\gamma\,\Gamma$ with
$\Gamma=D_+^{-1/2}(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}D_+^{-1/2}$ (Prop. 3, pp. 111–116).
([[bergault-2021-closed-form-approximations]])

*Notation:* $D_+$ collects intensities and Hamiltonian curvatures ($h_2$ in project notation); the
proposal's $\Gamma$ (eq. 10) plays the role of BEGV's $D_+$, while BEGV's own $\Gamma$ is the
ergodic matrix above.

## Variants in the core sources
- **Time-varying, forecast-driven** (scalar, one asset): eqs. (29)–(31), «in representative form»;
  clean only with a quadratic terminal penalty (fn. 3, p. 10). ([[barzykin-2026-hawkes-driven-otc]])
- **Regime-coupled:** under Markov-modulated Poisson liquidity, $p^2$ scalar Riccati ODEs coupled
  linearly through the generator (eq. 43, pp. 18–19). ([[bergault-2024-price-aware-automated]])
- **Absent:** [[gueant-2013-dealing-inventory-risk]] (exact linear ODEs, no expansion),
  [[cartea-2014-buy-low-sell]] (first-order expansion, linear ODEs),
  [[jusselin-2021-persistent-order-flow]], [[martin-2026-market-making-hawkes]],
  [[acero-2026-hawkes-structured-networks]].

## Criticism
The explicit tanh solution and the formula for $B$ need a **constant** $D_+$ (all $A(s)D_+$ commute,
p. 113). With time-varying $D_+(t)$, the Riccati ODE remains but must be integrated numerically
(inference from the BEGV source page).

## Relevance to this project
Stage 2 makes $D_+$ time-varying and driven by the forecast of all intensities (proposal eqs. 9–10),
so a burst in one asset skews quotes in another through the off-diagonal terms of $A$.

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[fujii-2015-optimal-position-management]]: backward stochastic (random-coefficient) Riccati, eqs. (6.10)/(6.20) pp. 24–26; deterministic case = Kratz–Schöneborn ODE (7.1) p. 27; customer flow enters only linear/constant coefficients, never the quadratic one (pp. 12, 24)
- [[zarezade-2018-steering-social-activity]]: Lemma 10 (p. 14) Ḣ=(ωI−B)ᵀH+H(ωI−B)+HBS⁻¹BᵀH+Q, value quadratic in λ, control feeds λ (eq. 18)
- [[shen-2022-mean-variance-portfolio]]: non-MM variant with λ-dependent coefficient V=e^{2r(T−t)+g(t,λ)}x², nonlocal PDE (3.24) p. 16, App. C p. 34; control does NOT feed λ («price-taker», p. 9); bivariate case not computable «in three days on a personal laptop» (p. 29)

## Sources
[[bergault-2021-closed-form-approximations]] · [[barzykin-2026-hawkes-driven-otc]] ·
[[bergault-2024-price-aware-automated]]
