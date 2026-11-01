---
title: "GLFT 2013 model (Guéant–Lehalle–Fernandez-Tapia)"
type: entity
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [model, closed-form, single-asset]
---

# GLFT 2013 model (Guéant–Lehalle–Fernandez-Tapia)

## What it is
Single-asset market making: Brownian reference price, Poisson market orders filling a quote at
distance $\delta$ with intensity $\Lambda e^{-k\delta}$ (the paper writes $A$ for $\Lambda$), CARA
utility, inventory bounds $|q|\le Q$. The change of variables
$u=-\exp(-\gamma(x+qs))\,v_q(t)^{-\gamma/k}$ turns the HJB into a **linear** ODE system
$\dot v=Mv$, solved by $v=e^{-M(T-t)}\mathbf 1$; optimal quotes in closed form from $v$ (Prop. 1,
p. 481; Thm. 1, p. 482). Verification theorem pp. 499–501; spectral (ground-state) asymptotics
and closed-form approximations of the quotes (p. 485). Drift and market-impact extensions keep
the method (Props. 4–5, pp. 486–488). Source: [[gueant-2013-dealing-inventory-risk]] (published
version, *Math. Financ. Econ.* 7:477–507).

## What the linear closure needs (pp. 481, 496–497)
1. exponential intensity $\Lambda e^{-k\delta}$, with the **same $k$** on both sides;
2. CARA utility with an additive Brownian price;
3. every jump of the state is a fill (inventory moves at every event).

## Contested / inference
- [inference, reader of the source; derivation re-checked in [[who-excites-the-flow]]] A deterministic
  $\Lambda(t)$ keeps the system exactly linear ($\dot v=M(t)v$), losing only the matrix exponential
  and the asymptotics. A Hawkes intensity whose jumps happen **at the maker's own fills** keeps it
  linear (a linear transport-jump equation in $(q,\lambda)$). Jumps caused by orders that do **not**
  fill the maker make it nonlinear.
- Q used for the figures is not stated; a reproduction with $Q=30$ gives a spread of 6.626 ticks at
  $q=0$, matching Fig. 3, but the closed form is off near $\pm Q$ (reader's calculation).

## Relevance to this project
Stage 1 of the proposal. Benchmark parameters confirmed against Figs. 1–3 (pp. 483–484):
$\sigma=0.3$ tick s$^{-1/2}$, $\Lambda=0.9$ s$^{-1}$, $k=0.3$ tick$^{-1}$, $\gamma=0.01$ tick$^{-1}$,
$T=600$ s; **$Q$ must be fixed by the project**.

## Further evidence (plan Task 8, wider library)
*Added from the source-ingester reports, wave by wave; each line points to the source page, where the evidence and page anchors are.*

- [[gasperov-2022-deep-reinforcement-learning]]: GLFT-form quotes only as a member of the LIN benchmark class (p. 5)
- [[bathini-2026-dynamic-market-making]]: on BTCUSDT data AS beats GLFT and both beat the frozen-Hawkes policy (Table 5, p. 13)

## Sources
[[gueant-2013-dealing-inventory-risk]] · lineage citations in [[barzykin-2026-hawkes-driven-otc]],
[[martin-2026-market-making-hawkes]], [[acero-2026-hawkes-structured-networks]],
[[jusselin-2021-persistent-order-flow]]
