---
title: "Volterra–Riccati approximation"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [closed-form, hawkes, market-making]
---

# Volterra–Riccati approximation

## Definition
Coined by Barzykin ([[barzykin-2026-hawkes-driven-otc]]): replace the random future Hawkes
intensity by its conditional forecast $m_t(u)$, which solves a Volterra equation (eq. 20, p. 9), and
solve the Riccati system of [[begv-2021-model]] along that deterministic path. Three levels:

1. **Mean VR** — frozen forecast (eq. 23, p. 9).
2. **Noise-aware VR** — adds a covariance correction for intensity uncertainty (eq. 38, p. 11).
3. **State-feedback VR** — re-evaluates at the post-request forecast $m_t+\rho_i$, so each arriving
   request updates the quotes (eqs. 42–43, p. 12).

Each level is a certainty-equivalent and is not time-consistent (pp. 9, 11, 22).

## How it is applied
Single asset, OTC RFQ flow, all requests excite (fills do not). Against the exact lifted HJB with
one exponential memory (Table 3, p. 16):

| Regime | State-feedback VR regret | Poisson policy regret |
|---|---|---|
| benign | 0.080 % | 6.138 % |
| near-critical | 0.083 % | 12.742 % |
| directional | 0.170 % | 27.312 % |

(Values checked against the PDF.) The Poisson comparator uses the **baseline** intensity $\mu$,
far below the stationary mean (p. 15), so part of its regret is a level error, not the cost of
ignoring memory. In the power-law experiment (Sec. 6) the Poisson policy is calibrated to
$\bar\lambda$ instead (p. 19).

## Criticism
- Proposal p. 6: an independent reproduction matched the exact values and the Poisson regrets but
  found ≈ 0.6 % for the state-feedback policy in the directional regime, against 0.17 % reported.
  Most of the gap came from the Hamiltonian expansion. **Contested, unresolved.**
- The reader of the source notes an inconsistency: the mean VR policy is said to be recomputed as
  information arrives (p. 9) but appears to be solved once from $X_0$ in the benchmark (p. 16).
- No regret against an optimum for power-law kernels; no convergence theory.

## Not to be confused with
Rough-volatility Volterra structures (Rosenbaum–Zhang 2022, `rosenbaum-2022-multi-asset-market`),
where the Volterra kernel sits in prices, not in order flow.

## Relevance to this project
The only closed-form route to Hawkes market making with a benchmark. It is single-asset; whether
the forecast layer carries over to cross-asset kernels and the Riccati layer to BEGV's
$d\times d$ system is the core of Stage 2 (Q1–Q3). Barzykin does not address it.

## Sources
[[barzykin-2026-hawkes-driven-otc]]
