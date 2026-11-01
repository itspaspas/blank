---
title: "Wiki Index"
type: synthesis
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
---

# Wiki index

As of: 2026-10-25 · Phase 1: core done; Task 8 (wider library) in progress, wave 1 merged.

## Entities (models)

- [[glft-2013-model]]: one asset, Poisson, CARA; exact linear ODE system (5 sources)
- [[begv-2021-model]]: several assets, quadratic Hamiltonian, matrix Riccati (5 sources)
- [[avellaneda-stoikov-model]]: base model (2 sources)
- [[cartea-jaimungal-ricci-model]]: first Hawkes market-making model; first-order expansion, linear ODEs (4 sources)

## Concepts

- [[hawkes-process]]: self- and mutually exciting order flow (4 sources)
- [[branching-matrix]]: $K$, $\rho(K)$, cross-asset blocks (4 sources)
- [[markov-lift]]: memory state variables that make the HJB Markov (4 sources)
- [[intensity-forecast]]: $m_t(u)$, the conditional expected intensity (3 sources)
- [[hamiltonian-quadratic-approximation]]: the BEGV closure step and where it breaks (4 sources)
- [[matrix-riccati-equation]]: the resulting closed form (2 sources)
- [[volterra-riccati]]: Barzykin's forecast-driven Riccati policy (1 source)
- [[shadow-price]]: value per unit inventory at post-event intensities (1 source)
- [[regret]]: benchmark regret vs approximation regret (6 sources)
- [[who-excites-the-flow]]: fill-driven vs flow-driven excitation; decides which closed form survives (7 sources)

## Sources

- [[barzykin-2026-hawkes-driven-otc]]: Hawkes-driven OTC market making, Volterra–Riccati (deep)
- [[bergault-2024-price-aware-automated]]: price-aware AMMs; why Hawkes liquidity breaks the closure (deep)
- [[martin-2026-market-making-hawkes]]: Mercer lift + PINN, one asset (deep)
- [[acero-2026-hawkes-structured-networks]]: RL with Hawkes-structured networks, 1 and 2 assets (deep)
- [[gueant-2013-dealing-inventory-risk]]: GLFT, the exact linear-ODE solution (deep, published original)
- [[bergault-2021-closed-form-approximations]]: BEGV, quadratic Hamiltonian + matrix Riccati (deep, published original)
- [[cartea-2014-buy-low-sell]]: CJR, mutually exciting orders, first-order expansion (deep, published original)
- [[jusselin-2021-persistent-order-flow]]: path-dependent HJB, viscosity solution, sum-of-exp lift (deep, **based on preprint**)

### Wider library (plan Task 8)

- [[aitsahalia-2016-portfolio-choice-markets]]: Aït-Sahalia & Hurd 2016 — Portfolio Choice in Markets with Contagion (standard · preprint)
- [[bathini-2026-dynamic-market-making]]: Bathini et al. 2026 — Dynamic Market Making under Stochastic Liquidity and Inventory Risk (standard)
- [[bielecki-2026-continuous-time-reinforcement]]: Bielecki, Mastrolia & Yan 2026 — Continuous-time reinforcement learning for controlled Hawkes jump-diffusions (standard)
- [[cartea-2018-algorithmic-trading-stochastic]]: Cartea, Jaimungal & Ricci 2018 — Algorithmic Trading, Stochastic Control, and Mutually Exciting Processes (SIAM Review SIGEST) (standard)
- [[chen-2026-optimal-trade-execution]]: Chen, Horst & Tran 2026 — Optimal Trade Execution Under Endogenous Order Flow (standard · preprint)
- [[choi-2021-synchronised-order-arrivals]]: Choi, Jang, Lee & Zheng 2021 — Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks (standard · preprint)
- [[fujii-2015-optimal-position-management]]: Fujii 2015 — Optimal Position Management for a Market Maker with Stochastic Price Impacts (standard)
- [[gasperov-2022-deep-reinforcement-learning]]: Gašperov–Kostanjčar 2022 — Deep Reinforcement Learning for Market Making Under a Hawkes Process-Based Limit Order Book Model (standard · preprint)
- [[jain-2025-impulse-control-hawkes]]: Jain–Firoozye–Kochems–Treleaven 2025 — An Impulse Control Approach to Market Making in a Hawkes LOB Market (standard)
- [[khabou-2025-markov-approximation-hawkes]]: Khabou & Talbi 2025 — Markov approximation for controlled Hawkes jump-diffusions with general kernels (standard)
- [[kumar-2024-deep-hawkes-process]]: Kumar 2024 — Deep Hawkes Process for High-Frequency Market Making (standard · preprint)
- [[lai-2023-data-driven-deep]]: Lai, Gao & Li 2023 — A Data-Driven Deep Learning Approach for Options Market Making (standard)
- [[shen-2022-mean-variance-portfolio]]: Shen & Zou 2022 — Mean-Variance Portfolio Selection in Contagious Markets (standard · preprint)
- [[tarditi-2026-hawkes-process-models]]: Tarditi 2026 — Hawkes Process Models of Limit Order Books for Optimal Market Making (MSc thesis) (standard)
- [[yuan-2026-dynamic-pricing-self]]: Yuan, Du & Hu 2026 — Dynamic Pricing Under Self-Exciting Arrival Processes (standard · preprint)
- [[zarezade-2018-steering-social-activity]]: Zarezade et al. 2018 — Steering Social Activity: A Stochastic Optimal Control Point of View (standard)
- [[bergault-2023-liquidity-dynamics-rfq]]: Bergault & Guéant 2023 — Liquidity Dynamics in RFQ Markets (MMPP regime-switching; standard · preprint)
- [[rosenbaum-2022-multi-asset-market]]: Rosenbaum & Zhang 2022 — Multi-asset market making under quadratic rough Heston (standard · preprint)
- [[barzykin-2022-multi-currency-inventory]]: Barzykin, Bergault & Guéant 2022 — Multi-currency inventory / FX dealer (standard · preprint)
- [[barzykin-2026-strategic-otc-reputation]]: Barzykin 2026 — Strategic OTC Market Making with Reputation Feedback (standard)
- [[barzykin-2026-bond-market-making]]: Barzykin & Ciceri 2026 — Bond Market Making with a Hit-Ratio Target (standard)
- [[sakhanda-2026-hawkes-jump-diffusion]]: Sakhanda & Ricalde-Guerrero 2026 — Stochastic Optimal Control of Hawkes Jump-Diffusion Systems (standard)
- [[ceci-2025-optimal-reinsurance-dynamic]]: Ceci & Cretarola 2025 — Optimal reinsurance in a dynamic contagion model: comparing self-exciting and externally-exciting risks (standard · preprint)
- [[yang-2026-robust-market-making]]: Yang–Xu 2026 — Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning (standard)
- [[wang-2024-arl-multi-action]]: Wang–Ventre–Polukarov 2024 — ARL-Based Multi-Action Market Making with Hawkes Processes and Variable Volatility (standard · preprint)
- [[alfonsi-2016-dynamic-optimal-execution]]: Alfonsi & Blanc 2016 — Dynamic optimal execution in a mixed-market-impact Hawkes price model (standard · preprint)
- [[alfonsi-2016-extension-calibration-hawkes]]: Alfonsi & Blanc 2016 — Extension and calibration of a Hawkes-based optimal execution model (standard · preprint)
- [[abijaber-2021-integral-operator-riccati]]: Abi Jaber, Miller & Pham 2021 — Integral operator Riccati equations arising in stochastic Volterra control problems (standard · preprint)
- [[drissi-2022-solvability-differential-riccati]]: Drissi 2022 — Solvability of Differential Riccati Equations and Applications to Algorithmic Trading with Signals (standard · preprint)
- [[fu-2022-portfolio-liquidation-games]]: Fu, Horst & Xia 2022 — Portfolio Liquidation Games with Self-Exciting Order Flow (standard · preprint)
- [[abijaber-2025-optimal-liquidation-signals]]: Abi Jaber & Neuman 2025 — Optimal Liquidation with Signals: the General Propagator Case (standard · preprint)
- [[abijaber-2021-linear-quadratic-control]]: Abi Jaber, Miller & Pham 2021 — Linear–quadratic control for a class of stochastic Volterra equations: solvability and approximation (standard · preprint)
- [[zhang-2020-backward-stochastic-riccati]]: Zhang–Dong–Meng 2020 — Backward Stochastic Riccati Equation with Jumps (SLQ with jumps and random coefficients) (standard · preprint)
- [[barzykin-2026-dynamic-slippage-control]]: Barzykin 2026 — Dynamic Slippage Control and Rejection Feedback in Spot FX Market Making (standard)
- [[barzykin-2026-win-score-promotion]]: Barzykin 2026 — Win-Score Promotion Gates in Aggregator-Routed RFQ Markets: A Two-Tier Stochastic Control Model (standard)

## Synthesis

- [[problem-anatomy]]: Q1–Q3. Why the closed forms close, what Hawkes adds, and where the closure breaks depending on who excites the flow (draft, first pass)
- [[memory-regret-gap-verification]]: plan `lai2023-gaps-and-memory` Task 2. Is the memory-regret gap open? Verdict: (1) and (3) open; (2) narrowed (execution, Abi Jaber et al. 2025; Jusselin Fig. 4), open for Hawkes market making; stop rule not triggered (draft)
