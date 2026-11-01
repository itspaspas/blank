---
title: "Fujii 2015 — Optimal Position Management for a Market Maker with Stochastic Price Impacts"
type: source
created: 2026-10-25
updated: 2026-10-26
status: review
author: llm
bibkey: fujii-2015-optimal-position-management
depth: standard
tags: [market-making, inventory-management, bsde, backward-stochastic-riccati, multi-asset, price-impact, dark-pool, lq-control, exogenous-flow]
relations:
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "Multi-asset value coefficient V2 solves a matrix BSDE identified as «the backward stochastic Riccati differential equation (BSRDE) associated with a special type of stochastic linear quadratic control (SLQC) problem» (p. 25), eq. (6.10)/(6.20); deterministic case is the matrix Riccati ODE (7.1) (p. 27)."
  - target: begv-2021-model
    type: mentions
    confidence: inferred
    because: "Not cited (paper predates BEGV). Both obtain a d-asset matrix Riccati for an inventory-quadratic value, but here quotes are fixed and flow is uncontrolled (pp. 2, 5), so the Riccati carries impact and dark-pool terms, not a Hamiltonian expansion."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Neither convention applies: customer flow is an exogenous marked point process whose compensator is F^W-adapted (Assumption A (a3), p. 4) and the maker «does not adjust it [the spread] in order to control the customer flows» (p. 5)."
---

# Optimal Position Management for a Market Maker with Stochastic Price Impacts

## Bibliographic Details

Fujii, Masaaki. 2015. *Optimal Position Management for a Market Maker with Stochastic Price
Impacts*. arXiv:1503.07007v2 [q-fin.PR], 5 September 2015; also SSRN 2584430
(doi 10.2139/ssrn.2584430). 41 pp. Author affiliation: Graduate School of Economics, University of
Tokyo.

**Read: arXiv 1503.07007v2 (preprint); page/equation numbers follow it.** (Non-core work; preprint
accepted under the project's preprint policy.)

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $X^{\pi,\delta}_s$ ($\boldsymbol X$ for $n$ assets) | position (inventory) | $q_t$ |
| $n$ | number of securities | $d$ |
| $\pi_s$ | absolutely continuous trading speed on the exchange (control) | no project symbol |
| $\delta_s$ | block-order size sent to the "dark pool" (control) | ⚠ **not** a quote $\delta^b,\delta^a$ |
| $\mathcal N(dt,dz)$, $\Lambda(t,z)$ | customer-order marked point process and its compensator (mark $z$ = signed size) | ⚠ $\Lambda$ is not the GLFT amplitude; customer intensity is exogenous |
| $\Phi_t,\Psi_t,\Phi_{2,t}$ | moments $\int z\Lambda$, $\int|z|\Lambda$, $\int z^2\Lambda$ (eq. 3.3) | ⚠ $\Phi$ not a Hawkes kernel |
| $H$, $\lambda$ | dark-pool execution counting process and its intensity | ⚠ $\lambda$ is **not** a Hawkes intensity $\lambda_t$ |
| $M_s$ | temporary linear impact (matrix for $n$ assets) | no project symbol |
| $\beta_s$ | price reaction to the maker's inventory (eq. 3.4; matrix for $n$ assets) | ⚠ not a decay $\beta$ |
| $\widetilde\xi,\widetilde\gamma$; $\xi,\gamma,\eta$ (eq. 3.10) | terminal / running quadratic inventory penalties; adjusted coefficients | $\gamma$ here is a **penalty**, ≈ $\tfrac12\gamma\sigma^2$ in project terms |
| $b_s$, $l_s$ | proportional bid/offer spread (fixed, not controlled), repo rate | — |
| $V(t,x)=x^\top V_2x+2x^\top V_1+V_0$ (eq. 6.4) | cost (minimised) value function | $\theta=-q^\top Aq-q^\top B-C$ ⇒ $V_2\leftrightarrow A$, $2V_1\leftrightarrow B$, $V_0\leftrightarrow C$ (sign convention: cost) |
| $W$ | $d$-dimensional Brownian motion driving all coefficients | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1, F2 | 1 Introduction (post-crisis market makers; fixed-spread "good" market maker; relation to execution literature) | 1–3 |
| — | 2 Preliminaries (spaces $\mathbb S^p$, $\mathbb H^p$) | 3–4 |
| ✓ F1 | 3 Single security: Assumption A; 3.1 market description (eqs. 3.1–3.6); 3.2 problem (eqs. 3.7–3.11, Prop. 3.1); remark on $\beta X$ | 4–10 |
| ✓ F1 | 4.1 Candidate solution: stochastic HJB (4.4), quadratic ansatz (4.5), controls (4.8)–(4.9), BSDEs (4.11)–(4.13) | 10–13 |
| ✓ F1 | 4.2 Verification (Props. 4.2–4.4, Thm. 4.1) | 13–18 |
| ✓ F1 | 5 Portfolio extension: Assumption A′, B′; market (5.1)–(5.4); problem (5.6), Prop. 5.1 | 18–22 |
| ✓ F1, F2 | 6.1 Multi-security candidate (6.6)–(6.13); 6.2 verification via Bismut's BSRDE (Thm. 6.1, eqs. 6.15–6.24), Thm. 6.2; remark on spreads (6.26) | 22–27 |
| ✓ F1, F2 | 7 Implementation, deterministic coefficients: matrix Riccati ODE (7.1), $V_1$ by propagator (7.3)–(7.7) | 27–28 |
| ✓ F1, F2 | 8 Perturbative small-diffusion expansion of the BSRDE (8.1)–(8.20); 8.2 convergence (Thm. 8.1) | 28–34 |
| ✓ F1, F2 | 9 Concluding remarks | 34 |
| ✓ | Appendix A: terminal position vs penalty size (Lemmas A.1–A.2, Thm. A.1) | 34–38 |
| — | References | 39–41 |

## Kernthesen

### 1. ⭐⭐ The "good" market maker accepts every customer order at a predefined spread; customer flow is not controlled by quotes (pp. 2, 5)

«We are interested in a good market maker who accepts every customer order with a predefined
bid/offer spread. The spread can be stochastic but we do not allow the market maker to control its
size dynamically based on its proprietary reasons in order to give a bias to the customer flows»
(p. 2). Repeated in §3.1: the firm «does not adjust it in order to control the customer flows»
(p. 5). The controls are **not quotes**: they are the exchange trading speed $\pi$ and dark-pool block
size $\delta$ (eq. 3.1, pp. 5–6). This makes the problem an inventory/execution problem with
exogenous order flow, not a quote-setting problem in the Avellaneda–Stoikov/GLFT sense.

### 2. ⭐⭐ Customer flow is a marked point process with an exogenous, Brownian-driven compensator — no self- or cross-excitation (pp. 4–6, 19)

Position: $X_s=x+\int_t^s\!\int_K z\,\mathcal N(du,dz)+\int_t^s\pi_udu+\int_t^s\delta_udH_u$ (eq. 3.1).
Assumption A: «All the stochastic processes which do not jump by $\mathcal N$ and $H$ are assumed to
be $\mathbb F^W$-adapted and hence continuous» (p. 4), and (a3) the compensator $\Lambda(\cdot,z)$ is «a
uniformly bounded $\mathbb F^W$-adapted process» (p. 4). The intensity is therefore a Cox-type
(doubly stochastic, Brownian-factor) intensity that does **not** depend on past customer orders, so
Hawkes self-excitation is excluded by assumption. Order sizes have bounded support $K$, interpreted
as «the maximum acceptable order size» (fn. 2, p. 6). No simultaneous jumps of $\mathcal N$ and $H$
(a8).

### 3. ⭐ Across securities, customer orders and dark-pool fills are independent; clustering is only suggested via Markov copulas (pp. 19–21)

In the $n$-asset model each security $i$ has its own $\mathcal N^i$ and $H^i$, with «no simultaneous
jump among $(\mathcal N^i,H^i)$» (a9′, p. 19). «In the above modeling, the customer orders and the
executions in the dark pool are assumed to occur independently for each security. However, it is
not difficult to introduce simultaneous customer orders or the dark pool executions for an arbitrary
subset of the securities by following the idea of dynamic Markov copula model … If there exist
strong clusterings among the customer orders or the executions, an extension to this direction may
become worthwhile» (pp. 20–21). Cross-asset coupling of the *flow* is thus at most common-shock
(copula) in the author's outlook, never excitation.

### 4. ⭐ Cross-asset coupling enters through non-diagonal impact and penalty matrices (p. 20)

Price: $\widetilde S_s=S_s+M_s\pi_s-\beta_sX_s$ (eq. 5.4). «Here, $M$ and $\beta$ are not necessarily
diagonal and hence they can induce direct as well as contagious stochastic linear price impacts …
due to the proxy hedging by correlated assets, a high trading speed or a big outstanding position of
a certain security induces similar price actions among the closely related assets» (p. 20).
Penalties $\xi,\gamma$ can be made «proportional to the (stochastic) covariance matrix among the
securities» to capture diversification (p. 20). "Contagion" here is a *price-impact* contagion, not
order-flow contagion.

### 5. The inventory term $-\beta X$ models other participants front-running the maker's known position (pp. 6, 10)

$\beta X$ captures that exchange participants «(partially) infer the inventory size of the market
maker» and position for its future unwinding (p. 5). Because customer flow also moves $X$, this is
«different from the standard model of the permanent price impact» and closer to large-trader models
(Jarrow 1992, Cvitanić–Ma 1996, Bank–Baum 2004) (p. 6). Well-posedness then relies on risk aversion:
with a risk-neutral investor and $\beta>0$ the system «would be ill-defined» (p. 10).

### 6. Objective: minimise expected quadratic inventory penalties plus trading costs, with stochastic coefficients (pp. 7–8)

Eq. (3.8): $\widetilde V(t,x)=\operatorname{ess\,inf}\mathbb E[\widetilde\xi|X_T|^2+\int_t^T\widetilde\gamma_s|X_s|^2ds+\int_t^T(\widetilde S_s\pi_s-l_sX_s)ds+\int\!\!\int\widetilde S_{s-}(1-\mathrm{sgn}(z)b_s)z\,\mathcal N(ds,dz)+\int_t^T([S_s-\beta_sX_{s-}]\delta_s+\widetilde\eta_s|\delta_s|^2)dH_s\mid\mathcal F_t]$.
$\widetilde\xi,\widetilde\gamma$ are «proportional to the variance of the price process» (p. 8).
This is a risk-adjusted (quadratic-penalty) objective, not CARA. After an Itô rearrangement the
counting-measure integrals are replaced by their compensators and the problem reduces to an
$\mathbb F^W$-conditional cost $J^{t,x}$ (eq. 3.11) which is strictly convex in $(\pi,\delta)$; existence
and uniqueness follow (Prop. 3.1, pp. 8–10).

### 7. ⭐⭐ The value function is exactly quadratic in inventory; the stochastic HJB splits into one nonlinear and two linear BSDEs (pp. 11–13)

Ansatz $V(t,x)=V_2(t)x^2+2V_1(t)x+V_0(t)$ (4.5), with $\mathbb F^W$-adapted random coefficients.
Optimal controls are linear feedback in $X$ (4.8)–(4.9):
$\pi^*_u=-\frac1{M_u}(V_2X_{u-}+V_1+\tfrac12(S_u+M_u\Theta_u))$,
$\delta^*_u=-\frac{V_2X_{u-}+V_1+\frac12S_u}{V_2+\eta_u}$. $V_2$ solves the nonlinear BSDE
$V_2(t)=\xi+\int_t^T\{-(\frac1{M_u}+\frac{\lambda_u}{V_2+\eta_u})V_2^2+\gamma_u\}du-\int_t^TZ_2dW_u$ (4.11);
$V_1,V_0$ solve linear BSDEs (4.12)–(4.13). Verified as the unique optimum (Thm. 4.1, p. 17), with
bounds on $V_2$ adapted from Ankirchner–Jeanblanc–Kruse 2014 (Prop. 4.2, pp. 13–15).

### 8. ⭐⭐ Customer flow enters only the linear BSDEs ($V_1$, $V_0$), never the Riccati coefficient $V_2$ (pp. 12, 24)

The flow moments $\Phi,\Psi,\Phi_2$ appear in (4.12)–(4.13) through $\Theta_s:=\Phi_s-b_s\Psi_s$ (eq.
3.11) and in (6.11)–(6.12) for $n$ assets; the $V_2$ equations (4.11), (6.10) contain only $M$, the
dark-pool intensity $\lambda$, $\eta$ and $\gamma$ (pp. 12, 24). Reason (visible in (4.7), p. 12): for a
quadratic $V$ an uncontrolled jump $z$ gives $V(x+z)-V(x)=V_2(2xz+z^2)+2V_1z$, affine in $x$, so
exogenous flow only shifts the linear and constant terms. In Section 7 the author states that «the
bid/offer spread, the customer order flows and the size of repo rate impact the optimal strategy
though $V_1$» (p. 28).

### 9. ⭐⭐ For $n$ assets the quadratic coefficient is a matrix backward stochastic Riccati equation, existence via Bismut's SLQC theory (pp. 24–27)

(6.10): $V_2(t)=\xi+\int_t^T\{-V_2[M_u^{-1}+\mathrm{diag}(\frac{\lambda_u}{V_2+\eta_u})]V_2+\gamma_u\}du-\int_t^TZ_2dW_u$,
with $\mathrm{diag}$ entries $\lambda^i/([V_2]_{ii}+\eta^i)$ (p. 24). No comparison theorem exists for
matrix BSDEs, but «we shall see $V_2$ is the backward stochastic Riccati differential equation
(BSRDE) associated with a special type of stochastic linear quadratic control (SLQC) problem in a
diffusion setup studied by Bismut (1976)» (p. 25). The auxiliary SLQC (6.15)–(6.19) uses a fictitious
Brownian motion $w\perp W$ whose diffusion coefficient $D^i$ reproduces the dark-pool jump
nonlinearity; its BSRDE (6.20) coincides with (6.10) (p. 26). Thm. 6.1: unique, symmetric PSD,
uniformly bounded $V_2$ (p. 25). The single-asset comparison-theorem argument is thereby replaced.

### 10. With deterministic coefficients $V_2$ is the Kratz–Schöneborn matrix Riccati ODE and $V_1$ has a propagator formula (pp. 27–28)

$\frac{dV_2}{ds}=V_2[M_s^{-1}+\mathrm{diag}(\frac{\lambda_s}{V_2+\eta_s})]V_2-\gamma_s$, $V_2(T)=\xi$ (7.1),
«which is the same ODE studied by Kratz & Schöneborn» (p. 28). Note the diagonal term depends on
$V_2$'s own diagonal: the ODE is Riccati-like but **not** a standard constant-coefficient algebraic
Riccati, so no tanh closed form is given; it is solved numerically. $V_1$ follows from the
fundamental matrix $Y_{t,s}$ of $F(s)=V_2[M^{-1}+\mathrm{diag}(\cdot)]$ (7.3)–(7.6), needing only
conditional expectations of $S$, $\Theta$, $b\Psi$, $l$ (7.7).

### 11. ⭐ General Markovian coefficients: a small-diffusion perturbation reduces the BSRDE to linear ODEs at each order, with an error bound (pp. 28–34)

Factor SDE (8.1) with parameter $\epsilon$ (8.5); zeroth order is the deterministic Riccati ODE
(8.10); higher orders are linear FBSDEs solved by polynomial ansätze in $X^{[k]}$ with linear ODE
coefficients (8.14)–(8.20). Thm. 8.1: error $\le\epsilon^{p(N+1)}C$ in $\mathbb S^p$ (pp. 32–33). Shown
for one security; «The extension to a multiple security case is straightforward» (p. 29); no numerical
test («Detailed numerical tests … will be left for an important future work», p. 34).

### 12. Spreads are chosen outside the control problem, by simulation (p. 27)

Remark: with $b^i_s=\hat a|\sigma^i_s|$ (6.26), «Even if the intensity (and/or distribution) of the
customer orders is a non-linear function of $(b^i)$, the market maker can obtain the cost function or
the distribution of its revenue by running the simulation based on the optimal strategy … for each
choice of $\hat a$» (p. 27). Spread choice is a static outer optimisation; the flow-to-spread link is
never embedded in the HJB.

### 13. ⭐ Open: coefficients jumping with the counting processes give a BSRDE with jumps whose well-posedness is unproved (p. 34)

«Assuming general $\mathbb F$-adaptedness (instead of $\mathbb F^W$-adaptedness) of the relevant
parameters looks an interesting extension … This situation will arise when one introduces
simultaneous jumps in the parameters, such as $M$, and the executions in the dark pool. In this case,
the driver of the resultant BSRDE depends on the martingale coefficient of the counting process. As
long as we know, the existence and uniqueness of the solution for the corresponding BSRDE have not
yet been proved» (p. 34). A filtering/hidden-Markov intensity for customer orders, to model «possible
herding behavior», is named as further future work (p. 34).

### 14. Large terminal penalty drives terminal inventory to zero; the strategy doubles as liquidation under customer flow (pp. 18, 34–38)

Thm. A.1: with $\xi=L$, $\mathbb E|X_T|^2\le C(\frac{L^{-1}}{T+L^{-1}})^{2c}$ (A.18), so the terminal position
can be made arbitrarily small (p. 37). The multi-asset analogue is only argued under a common
diagonalisation in $[T-\epsilon,T]$ with flow switched off (p. 38).

### 15. ⭐⭐ The expansion is around the small-diffusion limit of the factor SDE, not a perturbation of the driver; order 1 is linear in the factor deviation and vanishes at the start (pp. 28–32)

The author contrasts his scheme with Fujii–Takahashi 2012a, which perturbs the driver: «The new
method directly expands the BSDE around the small-diffusion limit of the associated forward SDE,
which only yields a system of linear ODEs to be solved at each order of expansion» (p. 28). The
factor $X$ (8.1) is replaced by $dX^\epsilon=\mu\,ds+\epsilon\sigma\,dW$ (8.5), $\epsilon\in(0,1]$;
all coefficients of the driver $f(x,v)=-(\frac1{M(x)}+\frac{\lambda(x)}{v+\eta(x)})v^2+\gamma(x)$ (8.2)
are functions of the factor, **including the dark-pool fill intensity $\lambda(x)$** (p. 29). Order 0
is the deterministic Riccati ODE (8.10) along the noiseless factor path $X^{[0]}$ (8.9). Order 1 is
the linear FBSDE (8.11)–(8.12) with coefficients $\partial_vf^0,\partial_xf^0$ evaluated on
$(X^{[0]},V^{[0]})$, solved by $V^{[1]}_s=y(s)^\top X^{[1]}_s$ with $y$ a linear ODE (8.14)–(8.15).
Order 2 is quadratic in $X^{[1]}$ plus linear in $X^{[2]}$, with a linear ODE system for
$(y_2,y_1,y_0)$ (8.16)–(8.20); each higher order is a polynomial in $X^{[1]},\dots,X^{[n]}$ (p. 32).
Since $X^{[1]}_t=X^{[2]}_t=0$, the correction at the starting point is $V_t=V^{[0]}_t+\epsilon^2y_0(t)+O(\epsilon^3)$
[D from (8.14), (8.18)]. Error: $\le\epsilon^{p(N+1)}C$ in $\mathbb S^p$ (Thm. 8.1, p. 32), proved
for one security; the driver is not Lipschitz, which is handled through the a-priori bounds on $V$
(p. 32).

## What this source does not address

- **Self- or cross-exciting order flow.** Customer intensities are $\mathbb F^W$-adapted (Assumption A,
  p. 4); no Hawkes, no dependence of intensity on past orders, no cross-asset excitation. Herding is
  future work via hidden Markov filtering (p. 34).
- **Quote control / fill probabilities.** Spreads are fixed; no $f(\delta)$, no Hamiltonian $H(p)$,
  no shadow price in the quote sense (pp. 2, 5, 27).
- **CARA utility.** Only quadratic penalties.
- **Numerical results.** No numbers, no benchmarks, no regret; the perturbation scheme is untested
  (p. 34).
- **Point-process-driven coefficients.** Jumps in $M$ or intensities with the counting processes
  lead to an open BSRDE-with-jumps problem (p. 34).
- **RL or neural methods.** None.

## Model card

| Field | Value |
|---|---|
| Assets | 1 (§§3–4) and $n$ (§§5–6) |
| Kernel | n/a — customer orders are a marked point process with exogenous $\mathbb F^W$-adapted (Brownian-factor, Cox-type) compensator $\Lambda(t,z)$ (Assumption A (a3), p. 4); no excitation kernel |
| Excitation | none — no self, cross-side or cross-asset excitation; cross-asset orders independent (p. 20); copula clustering only suggested (p. 21) |
| Who excites the flow | n/a — flow is exogenous and not controlled; the maker «does not adjust» spreads to steer flow (p. 5) |
| Objective | minimise expected cost with quadratic inventory penalties $\xi|X_T|^2+\int\gamma|X|^2$, impact costs and spread income (eq. 3.8 / 5.6); risk-adjusted, not CARA |
| Solution method | exact: value quadratic in inventory; matrix backward stochastic Riccati BSDE for $V_2$ + two linear BSDEs (6.10)–(6.12), existence via Bismut 1976 (Thm. 6.1); deterministic case = matrix Riccati ODE (7.1); general Markovian case = small-diffusion perturbation into linear ODEs (Thm. 8.1) |
| Benchmark | none |
| Reported regret / gap numbers | none — no numerical section |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 2, 3, 4, 7, 8, 9, 10, 13.**

### What this focus needs beyond the Kernthesen

1. **Verdict on the gap claim: qualifies, does not refute.** This is a multi-asset "market maker"
   with an exact matrix (backward stochastic) Riccati closure. But all three ingredients of the
   project's gap are missing. (a) The flow is not a self- or cross-exciting point process: its
   compensator is Brownian-driven and does not react to past orders (p. 4). (b) Fills are not
   controlled by quotes: every order is accepted at a predefined spread (pp. 2, 5). (c) There is no
   cross-asset excitation: orders are independent across securities (p. 20). Cross-asset coupling
   enters only through impact and penalty matrices $M,\beta,\xi,\gamma$ (p. 20). The paper therefore
   shows that a *d*-asset Riccati closure exists for *inventory management under exogenous flow*. It
   says nothing about quote-controlled Hawkes market making. Cite it as the multi-asset
   stochastic-Riccati precedent with exogenous, uncontrolled flow.
2. **Why the closure holds (mechanism) [I from eqs. 4.7, 6.6].** Three structural facts:
   uncontrolled flow jumps give terms affine in $x$; the controls $\pi,\delta$ enter linearly and
   quadratically (LQ); the dark-pool intensity $\lambda$ multiplies an expression quadratic in
   $(x,\delta)$ that is minimised in closed form. So $V$ stays exactly quadratic in $x$ with random
   coefficients. The flow-driven Hawkes market-making problem violates the second fact: the control
   acts through a nonlinear fill probability $f(\delta)$ multiplying $\lambda_j$, which is why BEGV
   need the Hamiltonian expansion ([[hamiltonian-quadratic-approximation]]).
3. **What would happen with Hawkes customer flow in Fujii's setup [I, not the author's].** If
   $\Lambda$ were a Markov-lifted exponential Hawkes intensity $\lambda^c$ (state, jumping by $K$ at
   each order), the jump term $\lambda^c_j[V(x+z,\lambda^c+Ke_j)-V(x,\lambda^c)]$ with a joint
   ansatz quadratic in $(x,\lambda^c)$ stays quadratic: intensity times affine. The controls do not
   touch $\lambda^c$. So the Fujii-type LQ structure plausibly survives exactly, with a Riccati in
   the augmented state $(x,\lambda^c)$. This is the same mechanism as Zarezade's
   ([[zarezade-2018-steering-social-activity]]). That is: **exact quadratic closure under Hawkes
   is available when the intensity-weighted terms are affine in the state and the control does not
   multiply the intensity nonlinearly.** Market making with quote-controlled fills breaks the last
   condition. This supports the proposal's diagnosis that the Hamiltonian, not memory, is the
   obstruction (cf. [[barzykin-2026-hawkes-driven-otc]] Kernthese 11). The author's own remark
   (Kernthese 13) points the same way: once coefficients jump with the counting processes, even his
   BSRDE leaves known theory (p. 34).
4. **Bearing on D2 (λ-dependent Riccati coefficients).** Here the Riccati coefficient $V_2$ is
   random only through Brownian factors. The flow intensity never enters $V_2$ (Kernthese 8). This
   is the opposite of the flow-driven Hawkes market-making case, where intensities enter the
   quadratic coefficient $A$ through $\sum_jm_jh_2$ (BEGV/Barzykin eq. 29). Fujii therefore offers
   no template for $A(t,\lambda)$. His stochastic-coefficient BSRDE is, however, the right
   *formal* object for "Riccati with random coefficients", and his small-diffusion perturbation
   (Kernthese 11) is a candidate technique if Hawkes intensities were replaced by a diffusive
   (e.g. CIR-type) factor proxy [I].
5. **Bearing on D1 (fill-driven CARA linearisation).** None: no CARA, no fills in the quote sense.

### Direct quotes (for the draft)

> "We are interested in a good market maker who accepts every customer order with a predefined bid/offer spread. The spread can be stochastic but we do not allow the market maker to control its size dynamically based on its proprietary reasons in order to give a bias to the customer flows." (p. 2)

> "In the above modeling, the customer orders and the executions in the dark pool are assumed to occur independently for each security." (p. 20)

> "Interestingly however, we shall see V2 is the backward stochastic Riccati differential equation (BSRDE) associated with a special type of stochastic linear quadratic control (SLQC) problem in a diffusion setup studied by Bismut (1976)." (p. 25)

> "In this case, the driver of the resultant BSRDE depends on the martingale coefficient of the counting process. As long as we know, the existence and uniqueness of the solution for the corresponding BSRDE have not yet been proved." (p. 34)

### Examples & illustrations (for later drafting)

- Eq. (4.7) (p. 12): the completed-square form of the HJB shows on one page why exogenous order
  jumps only feed the linear coefficient $V_1$. It is a compact contrast to BEGV's Hamiltonian term.
- Eq. (6.10) vs (7.1) (pp. 24, 27): the same matrix Riccati structure, first as a BSDE with random
  coefficients and then as a deterministic ODE. Use it to illustrate "Riccati with stochastic
  coefficients" if the project ever needs that formal object.
- The proxy-hedging sentence (p. 20) is a ready example of *price-impact* contagion across assets,
  to be distinguished from *order-flow* contagion (cross-asset Hawkes).

### Boundary of this focus

Everything said about Hawkes flow (focus items 2–4) is the project's inference from Fujii's equations.
The source has no self-exciting process. The paper offers no numbers, so it cannot inform the
three-way comparison (closed form / exact / RL).

## Focus: Perturbative/asymptotic closed forms for multi-asset market making with a stochastic intensity factor (Hawkes or Markov-modulated): which expansion, around which point, with which small parameter and error order; whether it closes into finite matrix ODEs; how accuracy is tested; how much of Stage 2a it already covers. — 2026-10-26

**Carries Kernthesen 9, 10, 11, 13, 15.**

### What this focus needs beyond the Kernthesen

1. **Which expansion, around which point.** A regular small-noise expansion of the Brownian factor
   $X$ (8.5) around its noiseless ODE path $X^{[0]}$ (8.9), applied to the Riccati BSDE for the
   inventory-quadratic coefficient $V_2$ (Kernthese 15). In project terms, $X^{[0]}$ plays the role
   of a deterministic forecast and $X^{[1]}\approx(X-X^{[0]})/\epsilon$ that of the deviation
   $\lambda-m_t$ [I].
2. **Small parameter and error order.** $\epsilon$ multiplies the factor's diffusion coefficient;
   the truncation error after order $N$ is $O(\epsilon^{N+1})$ in $\mathbb S^p$ (Thm. 8.1, p. 32).
   Stage 2a's small parameter scales *jumps* ($\epsilon DK$, with large $\mu$). Fujii's proof uses
   continuity and differentiability of a Brownian SDE in $\epsilon$ (p. 32). It does not transfer to
   a jump factor without a new argument [I].
3. **Does it close into finite ODEs?** Yes: at each order a finite system of linear ODEs (8.15),
   (8.19) given the order-0 Riccati solution. It is written out only for one security (scalar $V$,
   vector factor). For $n$ securities $V^{[1]}$ would be a matrix linear in $X^{[1]}$, with linear
   matrix ODEs of Lyapunov type [I; «straightforward», p. 29, «easily … extended», p. 33].
4. **Accuracy test.** None: «Detailed numerical tests … will be left for an important future work»
   (p. 34).
5. **What the factor is.** An exogenous Brownian (diffusion) factor driving impact $M$, penalties
   $\gamma,\xi,\eta$ and the dark-pool fill intensity $\lambda$. The intensity enters the
   *nonlinear* driver of $V_2$ through $\lambda(x)v^2/(v+\eta(x))$ (8.2). So Fujii's expansion is
   already an expansion of a matrix-Riccati coefficient in a stochastic *intensity* factor. But that
   factor is Cox-type and diffusive, not a jumping Hawkes intensity, and fills are not quote-controlled.

### Overlap with Stage 2a

| Element | Verdict | Evidence |
|---|---|---|
| (a) multi-asset matrix Riccati with a stochastic intensity/liquidity factor | **partly** | Matrix BSRDE (6.10) with stochastic $M_u$ and dark-pool intensities $\lambda^i_u$ in the driver, «$V_2$ is the backward stochastic Riccati differential equation (BSRDE)» (p. 25). Brownian-adapted, not Hawkes; no quote control. |
| (b) perturbative expansion in that factor | **partly** | «directly expands the BSDE around the small-diffusion limit of the associated forward SDE» (p. 28). Expands in diffusion amplitude around the factor's deterministic path. No jump factor. |
| (c) order-1 system linear given order 0 | **covered (scalar)** | «In the first order, we have the linear FBSDE system» (p. 30); $V^{[1]}=y^\top X^{[1]}$, $y$ from a linear ODE with coefficients on $(X^{[0]},V^{[0]})$ (8.15, p. 31). Matrix version not written. |
| (d) explicit small parameter + error order | **covered (diffusive ε)** | Thm. 8.1: error $\le\epsilon^{p(N+1)}C$ (p. 32). Different ε (diffusion, not jump size). |
| (e) accuracy test vs exact/numerical solution | **not** | «Detailed numerical tests … will be left for an important future work» (p. 34). |
| (f) cross-asset coupling of the factor | **partly** | One $d$-dimensional factor drives all securities' coefficients (8.1). The multi-security expansion is only asserted: «The extension to a multiple security case is straightforward» (p. 29). No cross-excitation. |

### What this changes for Stage 2a [I]

- **Cite as the precedent** for the method skeleton: deterministic-path order 0 (Riccati ODE), then a
  linear order-1 system, with an $\epsilon^{N+1}$ bound. Stage 2a's novelty must then rest on four
  points. (i) A *jump* (Hawkes) factor with a jump-size scaling and its own error proof. (ii) The
  intensity entering $A$ through the quote-controlled Hamiltonian ($\sum_j\lambda_jh_2$). (iii) An
  explicit matrix order-1 system. (iv) A numerical accuracy test, which Fujii lacks.
- **Order-1 vanishes at the starting point.** $X^{[1]}_t=0$ gives $V_t=V^{[0]}_t+O(\epsilon^2)$
  (Kernthese 15). The analogue in Stage 2a: the order-1 term $A^1\cdot(\lambda-m_t)$ changes quotes
  through the *realised* deviation, but its effect on the value at $\lambda=m_t$ is zero. So any
  value-gap test should expect the first nonzero correction at order 2.

### Direct quotes (for the draft)

> "We propose a perturbative expansion technique for the BSRDE with a general Markovian factor process, which only requires to solve a system of linear ODEs at each order of expansion. A justification and convergence rate of the approximation scheme are also given." (p. 3)

> "The new method directly expands the BSDE around the small-diffusion limit of the associated forward SDE, which only yields a system of linear ODEs to be solved at each order of expansion." (p. 28)

> "For clarity of demonstration, let us assume a single security case. The extension to a multiple security case is straightforward." (p. 29)

> "Detailed numerical tests and the extension to more general class of BSRDEs [43] will be left for an important future work." (p. 34)

### Boundary of this focus

Fujii's factor is diffusive and exogenous, and his customer flow never enters $V_2$ (Kernthese 8).
The bridge to a Hawkes factor in a quote-controlled Hamiltonian, and the order-2 remark, are the
project's inferences. The source has no numbers, so it offers no accuracy benchmark.

## Mentioned entities

- Models: [[begv-2021-model]] (not cited, later; structural comparison only), [[avellaneda-stoikov-model]] (not cited; contrast: quote-controlled flow).
- Concepts: [[matrix-riccati-equation]], [[hamiltonian-quadratic-approximation]], [[who-excites-the-flow]], [[hawkes-process]] (absent here).
- Other works (bibkeys / not in library): Kratz & Schöneborn 2013 (dark-pool liquidation, source of ODE 7.1); Bismut 1976 (SLQC/BSRDE); Mania & Tevzadze 2003 (stochastic HJB decomposition); Ankirchner, Jeanblanc & Kruse 2014; Almgren & Chriss 1999/2000; Bielecki et al. 2014a,b (Markov copula); Cartea & Jaimungal 2015a,b (order flow); Tang 2003/2014 and Peng 1992 (general BSRDE).

## Connections

- Builds on: [[matrix-riccati-equation]] in its backward-stochastic form (Bismut BSRDE), eqs. (6.10), (6.20).
- Contrast with: [[begv-2021-model]]: also $d$ assets and a matrix Riccati, but there quotes control fills and a Hamiltonian expansion is needed. Here flow is exogenous and the problem is exactly LQ.
- Contrast with: [[barzykin-2026-hawkes-driven-otc]] and [[problem-anatomy]] §3: Fujii's flow enters only linear coefficients, while Hawkes intensities in market making enter the quadratic one.
- Same exact-quadratic mechanism (intensity × affine jump, control not multiplying the intensity nonlinearly): [[zarezade-2018-steering-social-activity]].
