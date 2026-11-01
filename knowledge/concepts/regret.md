---
title: "Regret of a quoting policy"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [evaluation]
---

# Regret of a quoting policy

## Definition (two senses; do not mix)
1. **Benchmark regret** (this project, proposal p. 8): loss of a policy relative to the exact
   optimum, in % of the optimal value, estimated on common simulated flow. Barzykin uses paired
   regret with common random numbers (p. 15; Table 3, p. 16). ([[barzykin-2026-hawkes-driven-otc]])
2. **Approximation regret** (Acero et al.): $\mathrm{Reg}(\hat\pi)=\sup J^g-J^g(\hat\pi)$ for the
   exact optimiser of a truncated-kernel model; bounded by $C\,(\text{kernel }L^2\text{ error})^{1/2}$,
   rate $p^{-1/2}$, constant not explicit, and only «up to RL training error» (Thm 1, p. 3).
   ([[acero-2026-hawkes-structured-networks]])

Martin & Tse compare a naive (no-excitation) strategy with the Hawkes-aware one (mean P&L −0.700 vs
0.727, Fig. 8, p. 16): a comparison, not regret against an optimum.
([[martin-2026-market-making-hawkes]])

The older closed-form papers report no regret either. BEGV compare mean P&L of the closed form
with the numerical optimum in one two-asset example (88,600 € vs 89,000 €, 4,000 runs, p. 135), a gap
within Monte Carlo noise by the source reader's estimate ([[bergault-2021-closed-form-approximations]]).
CJR compare misspecified agents by P&L only (Table 1, p. 432; [[cartea-2014-buy-low-sell]]).
Jusselin reports Hawkes-aware vs Poisson value gains of «10 %» that his own Fig. 1 does not support
(≈ +3 % then +4 %, reader's reading of the plot, p. 12, preprint;
[[jusselin-2021-persistent-order-flow]]).

## Relevance to this project
The common currency of the planned three-way comparison; only Barzykin reports regret against an
exact solution, single-asset.

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[jain-2025-impulse-control-hawkes]]: DGM Sharpe 4.54 Poisson vs 0.78 Hawkes ('pump and dump'), full 12-D DGM did not converge; PPO+SIL 31.54 / 28.81 (Table 1 p. 10; pp. 17–20); no regret against an optimum
- [[bielecki-2026-continuous-time-reinforcement]]: CT-DDPG vs DGM/HJB oracle costs +1–5 % (Table 3, p. 43; reader's arithmetic)
- [[choi-2021-synchronised-order-arrivals]]: DNN vs CJR closed form at κ=0 within 0.07 %, «statistically non-distinguishable» (Table C.11 p. 46; p. 31)

## Sources
[[barzykin-2026-hawkes-driven-otc]] · [[acero-2026-hawkes-structured-networks]] ·
[[martin-2026-market-making-hawkes]]
