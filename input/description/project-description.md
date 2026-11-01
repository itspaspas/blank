# Project description — market-making

**Full proposal:** `proposal/proposal.pdf` (October 2026), "Market Making under
Cross-Asset Hawkes Order Flow: Closed-Form Approximations, Exact Solutions and
Reinforcement Learning in One Study".

## Central question

Can the closed-form approach of the 2013 (Guéant–Lehalle–Fernandez-Tapia, one asset) and
2021 (Bergault–Evangelista–Guéant–Vieira, several assets) market-making models be
extended to Hawkes order flow with excitation across assets, and how do such closed
forms compare with the exact optimum and with reinforcement learning?

## Current phase (Phase 1, from 2026-10-25)

Understand the problem and verify the gap: where and why the multi-asset closed form
breaks under multivariate Hawkes flow, and whether anyone has already solved it.
Design: `input/ideas/hawkes-multi-asset-mm-design.md`.

## Methodology

`mixed`: literature phases are hermeneutic; quantitative sub-studies (hypotheses H1–H4
of the proposal, regret experiments) get individually pre-registered plans.

## Guidance for ingest / synthesis

Prioritise in every source: number of assets; kernel type; self / cross-side /
cross-asset excitation; who excites the flow (all orders vs. the maker's fills);
objective (exponential utility vs. risk-adjusted); solution method (closed form,
grid / lifted HJB, neural PDE, RL); what it is benchmarked against; reported regret
numbers. Record equations with their numbers in the source.
