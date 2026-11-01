---
title: "Quadratic approximation of the Hamiltonian"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [closed-form, stochastic-control, market-making]
---

# Quadratic approximation of the Hamiltonian

## Definition
In the multi-asset model of [[begv-2021-model]], each side's Hamiltonian
$H^{i,s}(p)=\sup_\delta f^{i,s}(\delta)(\delta-p)$ is replaced by its second-order expansion
$H(p)\approx h_0+h_1p+\tfrac12 h_2p^2$ in the shadow price $p$. With that replacement the reduced
value function is exactly quadratic in inventory, $\theta\approx-q^\top Aq-q^\top B-C$, and $A$
solves a [[matrix-riccati-equation]].

## Where it comes from
[[bergault-2021-closed-form-approximations]]. Justification: the Hamiltonians enter through
$H^b(p)+H^a(-p)$, which is U-shaped, so a quadratic is natural (p. 109). Taylor expansion at $p=0$
is only «A natural choice» (Remark 1, p. 109): any constant coefficients close the system. The exact
Hamiltonian is still used in the quote map (p. 117) and in the Monte Carlo correction of Sec. 4
(pp. 119–121). Used as the reduction step in every Bergault/Guéant/Barzykin paper ingested so far.
An earlier, unrelated use: Jusselin replaces the Hamiltonian by a second-order polynomial only to
make his branching Monte Carlo work (App. H, p. 35, preprint;
[[jusselin-2021-persistent-order-flow]]).

## How it is applied
- **Hawkes order flow, forecast frozen:** Barzykin applies the expansion only to the
  continuation value along the intensity forecast; quotes are then computed from the *exact*
  optimiser at the approximate shadow price (eq. 32, p. 10).
  ([[barzykin-2026-hawkes-driven-otc]])
- **Extra price factors:** the closure survives stochastic volatility (Heston–Bates, Stein–Stein)
  and Hawkes *price* jumps, the Riccati ODE becoming a PDE in one extra variable (eqs. 8, 16, 24;
  pp. 2, 15). ([[bergault-2024-price-aware-automated]])
- **Markov-modulated Poisson liquidity:** $p^2$ scalar Riccati ODEs linearly coupled through the
  generator (eq. 43, p. 18–19). ([[bergault-2024-price-aware-automated]])

## Criticism — where it breaks
**When the market maker's own fills excite the flow.** Then a fill moves inventory and
intensity at once, the finite difference inside the Hamiltonian picks up a term
$(A(\lambda+\kappa\mathfrak m)-A(\lambda))y^2/z$, and the $\tfrac12\alpha_2p^2$ term produces
$y^3,y^4$ terms: the quadratic ansatz no longer closes (p. 17;
[[bergault-2024-price-aware-automated]], derivation reconstructed on that page). The authors call
Hawkes liquidity «inadequate for our stochastic optimal control problems» (p. 17) and switch to
MMPP. When *all* orders excite the flow (fills or not), the order stream is exogenous to the
policy, and the obstruction moves to the forecast-freezing step instead
([[barzykin-2026-hawkes-driven-otc]], pp. 6, 9).

Two papers avoid the approximation entirely: [[martin-2026-market-making-hawkes]] keeps the
exact Hamiltonian and solves numerically (p. 11); [[acero-2026-hawkes-structured-networks]] uses no
value-function closure at all.

## Not to be confused with
The GLFT 2013 exponential change of variables ([[glft-2013-model]]), which is *exact* (linear ODE
system) for one asset and does not expand the Hamiltonian.

## Relevance to this project
Q1/Q3: the expansion is the step that makes BEGV close; whether it survives cross-asset Hawkes
flow depends on who excites the flow. The error it introduces is what hypothesis H3 of the
proposal isolates.

## Sources
[[bergault-2024-price-aware-automated]] · [[barzykin-2026-hawkes-driven-otc]] ·
[[martin-2026-market-making-hawkes]] · [[acero-2026-hawkes-structured-networks]]
