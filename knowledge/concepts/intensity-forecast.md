---
title: "Intensity forecast (conditional expected Hawkes intensity)"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [hawkes, forecast]
---

# Intensity forecast (conditional expected Hawkes intensity)

## Definition
$m_t(u)=\mathbb E[\lambda_{t+u}\mid\mathcal F_t]$. For exponential kernels it is explicit,
$m_t(u)=\bar\lambda+e^{-D(I-K)u}(\lambda_t-\bar\lambda)$ (proposal eq. 8); for general kernels it solves a
Volterra equation (Barzykin eq. 20, p. 9). After a new event it jumps by the resolvent response
(eq. 22). The forecast does not depend on quotes when requests, not fills, drive the flow (p. 9).
([[barzykin-2026-hawkes-driven-otc]])

CJR already use the same object for exponential kernels:
$m_t(u)=e^{-\mathcal A(u-t)}[\lambda_t-\mathcal A^{-1}\zeta]+\mathcal A^{-1}\zeta$ (eq. B.2, p. 436), evaluated
**after** the triggering market order through the operator $S_\lambda$, which parallels Barzykin's
post-request forecast (comparison by the source reader; neither paper draws it).
([[cartea-2014-buy-low-sell]])

## How it is applied
Input of the [[volterra-riccati]] policies. Not used as such elsewhere so far:
[[bergault-2024-price-aware-automated]] filters or estimates the current intensity (p. 12;
fn. 16, p. 18); [[acero-2026-hawkes-structured-networks]] learns features that recover the current
$\lambda$ (probe MSE $<10^{-6}$, Table 2, p. 6) but never forecasts $m_t(u)$.

## Not to be confused with
The lifted memory state ([[markov-lift]]): the forecast is a deterministic function of it.

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[bathini-2026-dynamic-market-making]]: intensity frozen as a constant in a 30-min receding-horizon Bellman solve, «does not value the option to simply wait for that intensity to decay» (p. 12)
- [[chen-2026-optimal-trade-execution]]: only expected intensities enter via resolvent e^{-ωt}, ω=β−α (eq. 2.2, p. 5); closed form by risk neutrality + deterministic control (p. 1)
- [[lai-2023-data-driven-deep]]: ExpN feature = one-step Volterra forecast (eqs. 15–16, p. 785)
- [[choi-2021-synchronised-order-arrivals]]: (A.2) p. 37, matrix D=B−J

## Sources
[[barzykin-2026-hawkes-driven-otc]] · [[bergault-2024-price-aware-automated]] ·
[[acero-2026-hawkes-structured-networks]]
