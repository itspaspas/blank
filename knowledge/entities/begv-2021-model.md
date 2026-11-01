---
title: "BEGV 2021 model (Bergault–Evangelista–Guéant–Vieira)"
type: entity
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [model, closed-form, multi-asset]
---

# BEGV 2021 model (Bergault–Evangelista–Guéant–Vieira)

## What it is
$d$-asset market making with Poisson requests whose intensities depend only on each asset's own
quote, deterministic and time-homogeneous (p. 104). Two objectives: Model A (CARA, $\xi=\gamma$)
and Model B (risk-adjusted, $\xi=0$) (pp. 105–107). Each Hamiltonian is replaced by a quadratic
([[hamiltonian-quadratic-approximation]]); the value function becomes exactly quadratic in
inventory, $\theta=-q^\top A q-q^\top B-C$, with $A$ solving the [[matrix-riccati-equation]]
$A'=2AD_+A-\tfrac12\gamma\Sigma$, solved in closed form with tanh (eq. 13) and an ergodic limit
(Prop. 3, pp. 111–116). Quotes come from the **exact** optimiser at the approximate finite
difference (p. 117). For $d=1$ it recovers GLFT's asymptotics (p. 118). Extensions: drift, client
tiers, size distributions, fixed costs (Sec. 5, pp. 121–128); a Monte Carlo correction (Sec. 4,
pp. 119–121). Source: [[bergault-2021-closed-form-approximations]] (published version,
*Applied Mathematical Finance* 28:2, 101–142).

## What the closure needs (pp. 104–111, 128, 139)
- each intensity depends on its own quote only, with no other state (p. 104);
- regularity $\sup\Lambda\Lambda''/\Lambda'^2<2$ (p. 105);
- inventory limits dropped, $Q^i=+\infty$ (p. 109);
- quadratic coefficients **constant** (Remark 1, p. 109: Taylor at $p=0$ is only «A natural choice»);
- $\alpha_2^b+\alpha_2^a>0$ assumed (Prop. 2, p. 111);
- $\Sigma$ and drift constant (pp. 104, 121); terminal condition zero or quadratic (note 6, p. 139).

## Contested / inference
- [inference, reader] The polynomial step (Prop. 1) still closes with **time-varying deterministic**
  coefficients; what is lost is the tanh formula and the explicit $B$ (variation of parameters
  uses that all $A(s)D_+$ commute, p. 113). So cross-asset excitation frozen into a forecast would
  enter only through a diagonal, time-varying $D_+(t)$: the Riccati structure survives, the
  explicit formulas do not.
- $D_+$ is diagonal: in the base model assets interact only through $\Sigma$ (and drift);
  cross-asset skew comes from off-diagonal entries of $A$ (p. 117).
- Accuracy evidence is one two-asset example; the P&L gap (88,600 € vs 89,000 €, 4,000 runs,
  p. 135) is within noise by the reader's estimate; no regret metric; «higher dimensions should be
  just as good» is asserted, not tested (p. 137).

## Relevance to this project
The model Stage 2 extends. No source ingested so far extends it to Hawkes flow with cross-asset
excitation (Q6).

## Sources
[[bergault-2021-closed-form-approximations]] · [[bergault-2024-price-aware-automated]] ·
[[barzykin-2026-hawkes-driven-otc]] · citations in [[martin-2026-market-making-hawkes]],
[[acero-2026-hawkes-structured-networks]]
