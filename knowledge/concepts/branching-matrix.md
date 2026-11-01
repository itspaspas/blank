---
title: "Branching matrix and spectral radius"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [hawkes, stability]
---

# Branching matrix and spectral radius

## Definition
$K_{jl}$ = mean number of type-$j$ events triggered by one type-$l$ event (the $L^1$ norm of kernel
$g_{jl}$). Stationary flow requires $\rho(K)<1$; mean intensity $\bar\lambda=(I-K)^{-1}\mu$. For
one symmetric asset, $\rho(K)$ is the branching ratio, the share of events triggered by earlier
ones. Cross-asset excitation = nonzero off-diagonal **asset** blocks of $K$.

## Values used in the core sources
- CJR: $K=\frac{\rho}{\beta}\begin{pmatrix}\eta&\nu\\\nu&\eta\end{pmatrix}$, stability $\beta>\rho(\eta+\nu)$
  (Lemma 2.1, p. 421); simulation $\rho(K)=0.58$ (p. 432); IBM fit $\hat\beta=180.05$,
  $\hat\eta=64.16$, $\hat\nu=55.73$, i.e. about 0.67 with cross-side excitation nearly as strong as
  self-excitation (p. 436). ([[cartea-2014-buy-low-sell]])
- Jusselin: branching ratio 0.9 in the examples ($\mu_0=1$ = stationary mean $0.1/(1-0.9)$, p. 12).
  ([[jusselin-2021-persistent-order-flow]])
- Barzykin: two-type $\mathcal B=\begin{pmatrix}0.55&0.05\\0.05&0.55\end{pmatrix}$, $r=0.60$
  (p. 19); the tail law of quote impact uses $(I-\mathcal B)^{-1}$ (eq. 53, p. 18).
  ([[barzykin-2026-hawkes-driven-otc]])
- Bergault et al.: scalar self-excitation per side, $K=\mathrm{diag}(\mathfrak m,\mathfrak m)$ (p. 16).
  ([[bergault-2024-price-aware-automated]])
- Martin & Tse: scalar per flow; condition stated as $\|g\|_1<1/a$ (p. 4) but $\|g\|_1<a$ in
  Thm 2.4, and some experiments appear to violate the bound (reader's calculation). **Inconsistent.**
  ([[martin-2026-market-making-hawkes]])
- Acero et al.: the only multi-asset case so far: 2 assets, self 0.12, same-side cross-asset
  0.28, $\rho=0.40$, no cross-side excitation (p. 5). It is unclear whether these are kernel
  weights or $L^1$ norms. ([[acero-2026-hawkes-structured-networks]])

## Relevance to this project
Hypothesis H2 varies the cross-asset share of $K$ at fixed $\rho(K)$; the relaxation rate of the
forecast is $\beta(1-\rho(K))$ (proposal p. 8).

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[tarditi-2026-hawkes-process-models]]: fitted K diag 0.538/0.432, cross 0.030/0.001, ρ≈0.54 at ms decay (Fig. 9, pp. 42–43)
- [[khabou-2025-markov-approximation-hawkes]]: stability L·E[b]·sp(‖ϕ‖₁)<1 (p. 4)
- [[aitsahalia-2016-portfolio-choice-markets]]: stationarity Γ=αδ−d positive (p. 9)
- [[cartea-2018-algorithmic-trading-stochastic]]: INTC 2018 fit β̂=3,774, η̂=2,766, ν̂=54 → ratio ≈0.75, cross-side ≈2 % of self (p. 694), vs 2014 IBM fit with cross ≈ self
- [[choi-2021-synchronised-order-arrivals]]: fitted ρ(K) ≈ 0.41 (0.29–0.61 per stock), cross/self ≈ 0.12–0.15 (pp. 15, 44)

## Sources
[[barzykin-2026-hawkes-driven-otc]] · [[bergault-2024-price-aware-automated]] ·
[[martin-2026-market-making-hawkes]] · [[acero-2026-hawkes-structured-networks]]
