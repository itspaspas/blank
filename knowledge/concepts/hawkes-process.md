---
title: "Hawkes process"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [hawkes, point-process, order-flow]
---

# Hawkes process

## Definition
A point process whose intensity rises after each event and decays back to a baseline:
$\lambda^j_t=\mu_j+\sum_l\int_0^t g_{jl}(t-s)\,dN^l_s$ (Hawkes 1971, `hawkes-1971-spectra-self-exciting`,
not yet acquired). Exponential kernel: $g_{jl}(u)=K_{jl}\beta_je^{-\beta_ju}$, see [[branching-matrix]].
Stationary iff the spectral radius $\rho(K)<1$.

## How it is applied in market making (sources so far)
| Source | What excites | Kernel | Assets |
|---|---|---|---|
| [[barzykin-2026-hawkes-driven-otc]] | every RFQ (fills do not matter) | marked, exponential; power-law in Sec. 6 | 1 (side × size types) |
| [[bergault-2024-price-aware-automated]] | price jumps (Sec. 3.4) or the AMM's own trades (Sec. 4.2) | exponential, self only | 1 pair |
| [[martin-2026-market-making-hawkes]] | market orders; also the fill elasticity κ | general (Mercer-lifted) | 1, buy/sell separate |
| [[acero-2026-hawkes-structured-networks]] | market orders | completely monotone (mixture of exp., shifted power law) | 1 and 2 |
| [[cartea-2014-buy-low-sell]] | «influential» market orders (latent mark, probability $\rho$); also excite LOB depth and drift | bivariate exponential, self + cross-side | 1 |
| [[jusselin-2021-persistent-order-flow]] | the maker's own fills (single market maker); nonlinear link $\Phi$ | completely monotone, same side only | 1 |

Who excites (all orders vs the maker's fills) decides which closed form survives: see
[[who-excites-the-flow]].

Empirics: FX RFQ branching ratios 0.86–0.90 (Barzykin, Table 1, p. 4; read as predictive, not
causal, p. 2). Proposal preliminary fits on Binance: 0.44–0.93 (proposal p. 5).

## Criticism
Bergault et al. concede Hawkes fits trade data well but call it «inadequate for our stochastic
optimal control problems» when trades drive intensity (p. 17).

## Not to be confused with
Markov-modulated Poisson flow (finite regimes, no self-excitation), the tractable substitute in
[[bergault-2024-price-aware-automated]].

## Relevance to this project
The order-flow model of the whole study; cross-asset excitation means off-diagonal asset blocks of
$K$ (see [[branching-matrix]]).

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[jain-2025-impulse-control-hawkes]]: richest single-asset cross-type structure, 12 event types (pp. 4, 7)
- [[gasperov-2022-deep-reinforcement-learning]]: 8-variate exponential Hawkes, Biais 12→8 events (p. 3)
- [[lai-2023-data-driven-deep]]: KS pass rates power-law 91–97 %, exponential 36–86 %, Poisson 0.09–15.5 % (Table 1, p. 782); cross-excitation assumed zero as «insignificant» (p. 780)
- [[kumar-2024-deep-hawkes-process]]: neural (LSTM) generalisation, eq. 4.1 p. 18; multi-asset only in the simulator, one security quoted (p. 24)

## Sources
[[barzykin-2026-hawkes-driven-otc]] · [[bergault-2024-price-aware-automated]] ·
[[martin-2026-market-making-hawkes]] · [[acero-2026-hawkes-structured-networks]]
