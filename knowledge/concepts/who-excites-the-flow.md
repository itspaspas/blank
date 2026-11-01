---
title: "Who excites the flow: fill-driven vs flow-driven excitation"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [hawkes, closure, modelling-convention]
---

# Who excites the flow: fill-driven vs flow-driven excitation

## Definition
A modelling convention every Hawkes market-making paper must choose, usually without naming it:
- **Flow-driven** (exogenous): every order or request excites the intensities, whether or not it
  fills the market maker. The order stream does not depend on the quotes.
- **Fill-driven** (endogenous): only the market maker's own fills excite. The quotes change future
  intensity.

## In the core sources
| Source | Convention |
|---|---|
| [[barzykin-2026-hawkes-driven-otc]] | flow-driven: every RFQ excites; fills are thinnings of the request flow (p. 9) |
| [[cartea-2014-buy-low-sell]] | flow-driven: influential market orders, independent of the maker's quotes (p. 421) |
| [[martin-2026-market-making-hawkes]] | flow-driven: market orders and fill elasticity excited by the market |
| [[acero-2026-hawkes-structured-networks]] | flow-driven |
| [[bergault-2024-price-aware-automated]] | fill-driven in the Hawkes-liquidity model: the AMM's trades excite (Sec. 4.2, p. 16) |
| [[jusselin-2021-persistent-order-flow]] | fill-driven: «one market maker», every market order is his fill (pp. 1–2) |

## Why it matters for the closure: the two closed forms pull in opposite directions
- **Quadratic/Riccati closure (BEGV):** fill-driven excitation breaks it. Inventory and intensity
  jump together, so the finite difference in the Hamiltonian picks up a term in
  $(A(\lambda+\Delta)-A(\lambda))q^2$ and the curvature term produces $q^3,q^4$
  ([[bergault-2024-price-aware-automated]], p. 17). Flow-driven excitation keeps an
  approximate closure: freeze the forecast and run the Riccati system along it
  ([[barzykin-2026-hawkes-driven-otc]], pp. 9–12), at the price of the forecast-freezing error.
- **Exact linear closure (GLFT):** the opposite. With fill-driven excitation the GLFT change of
  variables still linearises the HJB (a fill moves $q$ and $\lambda$ in one jump term, raised to the
  same power), giving a linear transport-jump equation in $(q,\lambda)$. With flow-driven
  excitation, unfilled orders add a term $\lambda(1-e^{-k\delta})\,[w(q,\lambda+\Delta)-w(q,\lambda)]$ that
  depends on $\delta$ and is nonlinear after the substitution $w=v^{-\gamma/k}$.
  *Status: inference by the GLFT source reader ([[gueant-2013-dealing-inventory-risk]], focus
  points 2–3), re-derived in outline in the main session; not stated by any source. To be verified
  in full in the problem-anatomy synthesis.*

## Relevance to this project
Worked out with the generator terms in [[problem-anatomy]] §3. The proposal fixes the flow-driven convention (proposal p. 21: «all orders excite the flow») and
leaves the fill-driven case to exact and learning methods. This page shows the choice is not
neutral: it decides **which** closed form can be extended and which error source dominates (Q3).

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[jain-2025-impulse-control-hawkes]]: flow-driven (impulse operator never updates λ, App. B pp. 26–27, inferred)
- [[gasperov-2022-deep-reinforcement-learning]]: claims the maker's orders affect arrival intensities («the market maker's controls … affect the order arrival intensities», PDF p. 3) without a specified mechanism
- [[tarditi-2026-hawkes-process-models]]: explicit flow-driven price-taker convention (Remark 4.4, p. 12); eq. (60) compares Θ at post-order intensity, extra −Θ(q,λ) term (p. 33)
- [[yuan-2026-dynamic-pricing-self]]: fill-driven pricing analogue; Lemma 3 (p. 21): if non-buyers excite as much as buyers, the optimal intensity is constant (checked)
- [[chen-2026-optimal-trade-execution]]: execution example where the trader's own selling raises the sell baseline (p. 5)
- [[fujii-2015-optimal-position-management]]: third case, exogenous uncontrolled flow (p. 5)
- [[aitsahalia-2016-portfolio-choice-markets]]: exogenous contrast case; CARA L=−exp(−κx)g(λ), κ=rγ, ratio g(λ+d_l)/g(λ) (7.12), implicit nonlinear (7.13–7.14, p. 28), no verification

## Sources
[[barzykin-2026-hawkes-driven-otc]] · [[bergault-2024-price-aware-automated]] ·
[[jusselin-2021-persistent-order-flow]] · [[gueant-2013-dealing-inventory-risk]] ·
[[cartea-2014-buy-low-sell]] · [[martin-2026-market-making-hawkes]] ·
[[acero-2026-hawkes-structured-networks]]
