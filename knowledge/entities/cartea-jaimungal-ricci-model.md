---
title: "Cartea–Jaimungal–Ricci 2014 model"
type: entity
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [model, hawkes, single-asset]
---

# Cartea–Jaimungal–Ricci 2014 model

## What it is
First market-making model with mutually exciting market orders. Buy and sell market orders form a
bivariate exponential Hawkes process; a latent mark («influential», probability $\rho$) decides
whether an order excites the intensities (eq. 2.2, p. 421), the LOB depth $\kappa$ (eq. 3.1) and the
short-term drift $\alpha$ (eq. 4.1). Objective: terminal wealth with a running inventory penalty
$\phi$. With one exponential per channel the HJB (5.3) is already Markov in
$(t,q,\alpha,\lambda^\pm,\kappa^\pm)$: **no lift is needed** (pp. 426–427).
Source: [[cartea-2014-buy-low-sell]] (published version, *SIFIN* 5, 415–444).

## The closure
An asymptotic expansion «correct to $o(\varsigma)$ where $\varsigma=\max(\phi,\alpha,\mathbb E[\varepsilon])$»
(p. 427): small inventory penalty, small drift and small mean drift jump together. The
first-order terms solve **linear** ODEs (C.6)/(C.7) via Feynman–Kac, with matrix-exponential closed
forms (5.12), (C.7) (pp. 438–441). Quotes are linear in $\lambda^+-\lambda^-$ only in the symmetric
case (5.13, p. 430). **No Riccati equation** appears.

## Contested
- The expansion ansatz (5.6) is assumed, not proved; $\alpha$ is a state treated as small.
- [inference, reader] At first order the inventory skew $\phi(1\mp2q)(T-t)$ grows with time-to-go
  and never saturates as in GLFT/BEGV; the Riccati nonlinearity is $O(\phi^2)$.
- Tests are P&L simulations of six misspecified agents (5 min, 5,000 runs, pp. 430–434; benchmark
  14.09 vs about −4 for agents ignoring alpha, Table 1, p. 432); no exact solution, no regret.
- Printed inconsistencies (Appendix D swaps self/cross jumps vs eq. 2.2b, p. 443; others on the source page).
- Later papers cite the **2018 SIAM Review** version ([[barzykin-2026-hawkes-driven-otc]] p. 2;
  [[martin-2026-market-making-hawkes]] Remark 2.2). [[acero-2026-hawkes-structured-networks]]
  attributes a fill function $e^{-10\delta}$ to CJR, but CJR's simulation uses $\kappa$ with
  long-run level 50 (p. 432).

## Relevance to this project
A second closed-form route (perturbative + linear), the only one with mutually exciting flow
before 2026. [inference, reader] Its ODEs generalise formally to $2d$ types with cross-asset
blocks, giving quotes that respond linearly to cross-asset flow, but without BEGV's Riccati
inventory coupling; combining the two is an open construction.

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[cartea-2018-algorithmic-trading-stochastic]]: SIGEST reprint, maths unchanged (p. 673); new §7 (pp. 692–693) does not treat multi-asset Hawkes MM: «such problems cannot be solved in closed form» (p. 692)

## Sources
[[cartea-2014-buy-low-sell]] · [[barzykin-2026-hawkes-driven-otc]] ·
[[martin-2026-market-making-hawkes]] · [[acero-2026-hawkes-structured-networks]]
