---
title: "Shadow price of inventory"
type: concept
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
tags: [stochastic-control]
---

# Shadow price of inventory

## Definition
The value lost per unit of inventory taken on by a fill,
$p^j=[\theta(t,q,\lambda^{+j})-\theta(t,q\pm z_ie_i,\lambda^{+j})]/z_i$; the optimal quote solves
$\sup_\delta f(\delta)(\delta-p)$. Under Hawkes flow it is evaluated at the **post-event**
intensities (proposal p. 19).

## In the core sources
BEGV: quotes are $\tilde\delta(p)$ evaluated at the finite difference $(\theta(q)-\theta(q\pm ze^i))/z$
(eqs. 7–8, p. 108; p. 117); the paper never uses the term «shadow price».
([[bergault-2021-closed-form-approximations]])
Jusselin: $\delta^*=(\sigma/k-D_KU)_+$, where the jump changes inventory and memory together
(eqs. 4–5, pp. 5, 7, preprint). ([[jusselin-2021-persistent-order-flow]])
Barzykin: post-request shadow price (eq. 17); eq. (43) splits it into an inventory term and an
«information value» term, the channel through which a burst skews quotes (p. 12).
([[barzykin-2026-hawkes-driven-otc]])

## Sources
[[barzykin-2026-hawkes-driven-otc]]
