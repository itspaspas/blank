---
title: "Zhang–Dong–Meng 2020 — Backward Stochastic Riccati Equation with Jumps (SLQ with jumps and random coefficients)"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: zhang-2020-backward-stochastic-riccati
depth: standard
based_on: preprint
tags: [lq-control, backward-stochastic-riccati, bsrej, random-coefficients, poisson-jumps, existence-uniqueness, dynamic-programming, non-market-making]
relations:
  - target: matrix-riccati-equation
    type: supports
    confidence: extracted
    because: "Gives existence and uniqueness for the matrix Riccati equation when LQ coefficients are random (adapted): «the existence and uniqueness of the solution for the BSREJ is established» (abstract, p. 1); with deterministic coefficients «L = R = 0, and the BSREJ (1.3) degenerates to a deterministic Riccati integral-differential equation» (p. 3)."
---

# Backward Stochastic Riccati Equation with Jumps Associated with Stochastic LQ Optimal Control with Jumps and Random Coefficients

## Bibliographic Details

Zhang, Fu; Dong, Yuchao; Meng, Qingxin. 2020. "Backward Stochastic Riccati Equation with Jumps
Associated with Stochastic Linear Quadratic Optimal Control with Jumps and Random Coefficients."
*SIAM Journal on Control and Optimization* 58 (1): 393–424. doi:10.1137/18M1209684.

**Read: arXiv 1808.08336v1 (preprint, stamped 25 Aug 2018, 28 pp.); page and equation numbers on
this page follow that version.** The arXiv stamp on p. 1 says *v1*; the library bib note says
"latest version", which the PDF on disk does not bear out (see Notes in the ingest report). The
published SICON version (2020, 32 pp.) may differ in numbering and possibly content.

Field: stochastic control theory (BSDE / LQ). Not a market-making or finance paper; no numerics.

### Notation map (source → project)

| Source symbol | Meaning in source | Project remark |
|---|---|---|
| $X(t)\in\mathbb R^n$, $u(t)\in\mathbb R^m$ | controlled state, control (eq. 2.3) | in a BEGV-type reading: $X\leftrightarrow q$ (inventory), $u\leftrightarrow$ trading speed |
| $A,B,C^i,D^i,E,F$ | drift, control, diffusion, jump coefficients (random) | ⚠ source $A,B,C$ ≠ project quadratic coefficients $A,B,C$ |
| $Q,N,M$ | running state cost, control cost ($N\ge\delta I$), terminal cost | $Q\leftrightarrow\tfrac12\gamma\Sigma$; $N^{-1}\leftrightarrow$ intensity × $h_2$ (inference) |
| $K(t)$ | first component of BSREJ solution; value $V(t,x)=\langle K(t)x,x\rangle$ | ⚠ clashes with project $K$ (branching matrix); plays the role of project $A(t)$ |
| $(L,R)$ | martingale integrands w.r.t. $W$ and $\tilde\mu$ | no project symbol; $R(t,e)$ = jump of $K$ |
| $\mu(de,dt)$, $\nu$ | Poisson random measure of a stationary Poisson point process, finite Lévy measure | **not** a Hawkes measure |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1.1 Framework (Brownian motion + stationary Poisson random measure, filtration) | 1–2 |
| ✓ F1 | 1.2 BSREJ (1.2)–(1.4), Assumption 1.1, Definition 1.1 | 2–3 |
| ✓ F1 | 1.3 History of BSREs (Bismut, Peng, Tang), contribution, inverse-flow difficulty (1.6)–(1.7) | 4–5 |
| — | 2.1 Notation (function spaces), Lemma 2.1 (essential infimum) | 5–6 |
| ✓ F1 | 2.2 $\mathcal T$-systems, aggregation (Defs. 2.1–2.4, Prop. 2.2) | 6–7 |
| ✓ F1 | 2.3 Linear SDE with jumps (Lemma 2.3); 2.4 SLQ problem (2.3)–(2.5), Problem 2.4 | 8–9 |
| ✓ F1 | 3.1 Initial-data-parameterised SLQ, Prop. 3.2 (value quadratic, unique optimum) | 9–11 |
| ✓ F1 | 3.2 DPP (Thm. 3.3), RCE (Lemma 3.4), semimartingale representation of $K$ (Thm. 3.5), Remark 3.1 | 11–15 |
| ✓ F1 | 4 Existence (Thm. 4.1, BMO estimates, nonnegativity of the jump term) | 16–23 |
| ✓ F1 | 5 Verification (Thm. 5.1, feedback (5.3), value (5.4)); uniqueness (Thm. 5.2) | 24–26 |
| — | References | 26–28 |

## Kernthesen

### 1. ⭐ The object: a matrix-valued backward stochastic Riccati equation with jumps (BSREJ) for LQ control with random coefficients (pp. 2–3)

The unknown is a triple $(K,L,R)$ with $K$ in $\mathbb S^n$, solving
$dK(t)=-G(t,K(t-),L(t),R(t,\cdot))\,dt+\sum_iL_i(t)\,dW^i_t+\int_{\mathcal E}R(t,e)\,\tilde\mu(de,dt)$,
$K(T)=M$ (eq. 1.3), with generator
$G=A^\top K+KA+\sum_i(L_iC^i+C^{i\top}L_i+C^{i\top}KC^i)+\int(RE+E^\top R+E^\top(K+R)E)\nu(de)+Q-\mathcal M^\top\mathcal N^{-1}\mathcal M$
(eq. 1.2), where $\mathcal N(t,K,R)=N+\sum_iD^{i\top}KD^i+\int F^\top(K+R)F\,\nu(de)$ and
$\mathcal M=KB+\sum_iL_iD^i+\sum_iC^{i\top}KD^i+\int(E^\top KF+(I+E)^\top RF)\nu(de)$. The jump
integrand $R$ enters the inverse $\mathcal N^{-1}$, which is the new difficulty (p. 4).

### 2. Standing assumptions: bounded random coefficients, definite cost (p. 2)

Assumption 1.1: $A,B,C,D,N,Q$ uniformly bounded predictable; $E,F$ uniformly bounded
$\tilde{\mathcal P}$-measurable; $M$ bounded $\mathcal F_T$-measurable; $Q\ge0$, $M\ge0$, and
$N\ge\delta I$ uniformly positive. This is the **definite** case; indefinite BSREs are only cited
(p. 4: Chen–Li–Zhou 1998, Qian–Zhou 2013, Du 2015, etc.).

### 3. ⭐ With deterministic coefficients the BSREJ collapses to an ordinary Riccati (integro-)ODE (p. 3)

«When the coefficients A, B, C, D, E, F, Q, N are all deterministic, then $L^1=\dots=L^d=R=0$,
and the BSREJ (1.3) degenerates to a deterministic Riccati integral-differential equation» (p. 3).
Randomness of the coefficients is what creates the martingale parts $(L,R)$.

### 4. When the control does not enter the noise ($D=0$, $F=0$), $(L,R)$ enter only linearly (p. 3)

«If D = 0 and F = 0, i.e. the corresponding controlled differential system does not contain control
in martingale integration terms, … (L, R) only have a linear structure in the generator G. And in
this case the solvability of BSREJ could be covered by the result of Meng [19]» (p. 3). The
"highly nonlinear" case is the one with control in the diffusion/jump coefficients (p. 3).

### 5. Historical line: Bismut's problem, open until Tang (2003, 2015) (p. 4)

The Brownian BSRE (1.5) was proposed by Bismut, listed as open by Peng, solved by Tang 2003 via
stochastic Hamiltonian systems and stochastic flows, and again by Tang 2015 via DPP and Doob–Meyer
(p. 4). For jumps: Hu–Øksendal 2008 (one-dimensional, well-posedness not discussed), Meng 2014
(generator linear in $L,R$), Li–Wu–Yu 2018 (indefinite special cases) (p. 4).

### 6. ⭐ The key obstruction with jumps: positivity of $\mathcal N(t,K(t-),R)$ (p. 4)

«not only the first unknown element K and but also the third unknown element R are included in the
nonlinear term $\mathcal N(t,K(t-),R(t,\cdot))^{-1}$ … one only expects to prove the square
integrability of the third unknown element R, but this regularity is difficult to derive the
non-negativity of matrix $\mathcal N$» (p. 4).

### 7. ⭐ Method: build $K$ from the value function and DPP, not from a fixed-point argument (pp. 4, 9–15)

Following Tang 2015, the conditional value $V(\tau,\xi)=\mathrm{ess\,inf}_uJ(u;\tau,\xi)$ (eq. 3.4) is
shown to be a quadratic form, $V(\tau,\xi)=\langle\mathcal K(\tau)\xi,\xi\rangle$ (Prop. 3.2(iii),
eq. 3.6), with $0\le V\le\lambda|\xi|^2$ (3.5) and a unique optimal control (Prop. 3.2(ii)). DPP
(Thm. 3.3) makes $V$ along trajectories a submartingale; Doob–Meyer gives
$K(t)=K(0)-\int dk+\int L\,dW+\int R\,d\tilde\mu$ (Thm. 3.5, eq. 3.13). Positivity of
$\mathcal N$ then comes out of the control problem rather than being assumed (p. 4).

### 8. ⭐ The jump integrand is the jump of $K$, which gives positivity of the jump term (pp. 4–5, 23)

«$\int R(t,e)\mu(de,\{t\})$ is nothing but the jump measure of K(t)», so $K(s-)+R(s,p_s)=K(s)\ge0$
at jump times and $\int F^\top(K(t-)+R)F\,\nu(de)\ge0$ (pp. 4–5, eq. 1.6; proof p. 23).

### 9. Inverse flow without the usual invertibility condition, by working between jumps (pp. 5, 15)

The condition $I+E(t,e)\ge\delta I$ (eq. 1.7/3.17), standard for inverse flows of jump SDEs, «is not
necessary for the LQ control problem» (p. 5). The authors represent $K$ piecewise by the inverse flow
on each interval between consecutive Poisson jump times and glue by the semimartingale property
(Remark 3.1, p. 15). This uses that jump times are those of a *stationary Poisson point process*
(finite $\nu$), so there are finitely many on $[0,T]$.

### 10. ⭐ Existence (Thm. 4.1) with BMO bounds (pp. 16–23)

Under Assumption 1.1, $(K,L,R)$ from Thm. 3.5 solves (1.3), with
$\mathbb E\int_0^T\sum_i|L_i|^2dt+\mathbb E\int_0^T\int|R|^2\nu(de)dt\le C$ (4.1); the martingale
parts are BMO; the jump term $\int F^\top(K(t-)+R)F\,\nu(de)$ is nonnegative (p. 16). The HJB-type
identity $dk(t)x\cdot x=\min_v\{\mathcal F(t,x,v,K,L,R)+f(t,x,v)\}dt$ (4.7) identifies the drift.

### 11. ⭐ Verification: linear feedback and quadratic value (Thm. 5.1, pp. 24–26)

If the BSREJ has a solution, the optimal control is the linear feedback
$u^*(s)=-\mathcal N^{-1}(s,K(s-),R)\,\mathcal M(s,K(s-),L,R)\,X^*(s-)$ (5.3) and
$V(t,x)=\langle K(t)x,x\rangle$ (5.4). Uniqueness of $(K,L,R)$ follows (Thm. 5.2, p. 26).

### 12. Structural remark: $K$ does not depend on the state (p. 15)

«in the form of optimal feedback (see (5.3)), K is independent of the state of the controlled
equation, which hint us to represent K by different state process in different time interval» (p. 15).
The random coefficients carry all the "extra state"; the state enters only through $x^\top Kx$.

## What this source does not address

- **Controlled or state-dependent jump intensities.** The jump measure is that of a stationary
  Poisson point process with a fixed finite Lévy measure $\nu$ (p. 2); the control acts on jump
  *sizes* ($F u$), never on jump *rates*. No Hawkes, Cox or self-exciting measure.
- **Unbounded coefficients.** All coefficients are uniformly bounded (Assumption 1.1); a Hawkes
  intensity entering a coefficient would be unbounded.
- **Indefinite weights** (only cited, p. 4), exponential/CARA criteria, non-LQ Hamiltonians.
- **Any application, numerical method or example.** Purely existence/uniqueness/verification.
- Finance, market making, inventory problems: not mentioned.

## Model card

n/a — not a market-making model. For the record: assets n/a (state dimension $n$, control
dimension $m$) · kernel: none; noise = Brownian motion + stationary compound-Poisson random measure ·
excitation: none · who excites the flow: n/a, jump rate is exogenous and constant (Lévy measure
$\nu$) · objective: quadratic cost (definite LQ, eq. 2.4) · solution method: existence via DPP +
Doob–Meyer + piecewise inverse flow; verification theorem; no numerics · benchmark: none ·
reported numbers: none.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

*Read as LQ theory:* what its machinery says about a quadratic-in-inventory closure whose Riccati
coefficients are random (λ-driven), as in derivation D2.

**Carries Kernthesen 1, 2, 3, 4, 6, 7, 8, 10, 11, 12.**

### What this focus needs beyond the Kernthesen

1. **The quadratic closure survives random coefficients — as a BSDE, not an ODE.** Prop. 3.2(iii)
   and Thm. 5.1 show that with adapted random coefficients the value stays exactly quadratic in
   the state, $V=\langle K(t)x,x\rangle$, but $K$ becomes a semimartingale $(K,L,R)$ solving a
   backward stochastic Riccati equation. Read against [[problem-anatomy]] §3a *(inference, not the
   authors')*: the flow-driven exact-in-$q$ object $A(t,\lambda_t)$ is a Markovian instance of such
   a random Riccati coefficient; its jump at an order arrival, $A(t,\lambda^{+j})-A(t,\lambda)$, is
   the analogue of $R(t,e)$ (Kernthese 8), and the "nonlocal transport-jump Riccati system in
   $\lambda$" is the PDE form of a BSREJ.
2. **Where the analogy holds and where it breaks (inference).** It holds for the *fluid / LQ*
   version of the BEGV approximation: inventory driven by a speed control with quadratic cost
   $u^\top N(t)u$, where $N(t)^{-1}$ would carry the λ-dependent liquidity ($\lambda\,h_2$). That is
   the case $D=F=0$ of Kernthese 4, where $(L,R)$ enter only linearly and existence is already
   in Meng 2014. It breaks in three places for actual Hawkes market making: (a) the jump measure
   must be stationary Poisson with finite $\nu$, while a Hawkes intensity is itself the
   jump rate; it can be built by thinning a Poisson measure on $[0,T]\times\mathbb R_+$, but then
   $\nu$ is infinite unless λ is truncated; (b) the coefficients must be bounded, and λ is not;
   (c) in market making the control (quote) changes the jump *rate* of inventory, not a jump
   *size* $F u$, so the problem is not LQ in the source's sense.
3. **Who excites the flow.** n/a in the source. Its coefficients are exogenous (adapted to the
   driving noise, never to the control), which matches the flow-driven convention: there the
   intensity, and hence any λ-driven coefficient, does not depend on the quotes. A fill-driven
   intensity would make the coefficients control-dependent, which this framework excludes
   *(inference)*.
4. **Several assets.** The Riccati is matrix-valued from the start ($K\in\mathbb S^n$, $n$
   arbitrary), so a $d$-asset inventory with a $2d$-dimensional random intensity vector feeding
   the coefficients is no harder *in form*. Cross-asset excitation would enter only through the law
   of the coefficient process *(inference)*.
5. **No closed form.** The paper offers no formula or computational scheme for $K$; with random
   coefficients nothing like BEGV's tanh survives. Kernthese 3 is the bridge back: freezing the
   coefficients at their forecast (deterministic) kills $(L,R)$ and returns an ODE, which is the
   [[volterra-riccati]] / frozen-forecast step seen from the BSDE side.

### Direct quotes (for the draft)

> "When the coefficients A, B, C, D, E, F, Q, N are all deterministic, then $L^1 = \dots = L^d = R = 0$, and the BSREJ (1.3) degenerates to a deterministic Riccati integral-differential equation" (p. 3)

> "But for the BSREJ (1.3), one only expects to prove the square integrability of the third unknown element R, but this regularity is difficult to derive the non-negativity of matrix $\mathcal N(t, K(t-), R(t,\cdot))$. How to show $\mathcal N(t, K(t-), R(t,\cdot))$ keeping to be positive is key to give the solvability of BSREJ (1.3)." (p. 4)

> "We observe that in the form of optimal feedback (see (5.3)), K is independent of the state of the controlled equation" (p. 15)

### Examples & illustrations

None in the source (no numerics, no example). The construction itself is the illustration:
$K_{ij}(\tau)=\tfrac14\big(V(\tau,e_i+e_j)-V(\tau,e_i-e_j)\big)$ (eq. 3.8, p. 11) recovers the
Riccati matrix entry by entry from the value function.

### Boundary of this focus

Everything said here about market making, Hawkes intensities and $A(t,\lambda)$ is the project's
inference. The paper proves solvability for a definite LQ problem with bounded random coefficients
and an exogenous stationary Poisson jump measure. It does not cover control of jump rates,
unbounded or self-exciting coefficients, or exponential (CARA) criteria.

## Mentioned entities

- Concepts: [[matrix-riccati-equation]], [[volterra-riccati]] (contrast only), [[hawkes-process]] (absent from the source; used only in the focus inference)
- Synthesis: [[problem-anatomy]]
- Other task source: [[drissi-2022-solvability-differential-riccati]] (deterministic, indefinite DRE; contrast)
- Works cited by the source, not in the library: Bismut 1976; Peng 1992, 1999, 2010; Tang 2003, 2015; Kohlmann–Tang 2001–2003; Hu–Øksendal 2008; Meng 2014; Li–Wu–Yu 2018; Chen–Li–Zhou 1998; Qian–Zhou 2013; Du 2015; Wonham 1968; Zhou–Li 2000.

## Connections

- Supports (theory side): [[matrix-riccati-equation]], adding a random-coefficient variant to the
  BEGV deterministic one.
- Compare: [[drissi-2022-solvability-differential-riccati]], deterministic time-varying
  coefficients but indefinite and CARA-derived; this paper has random coefficients but is definite
  and plain LQ.
- Compare (not cited by the source): [[fujii-2015-optimal-position-management]], which uses a
  backward stochastic Riccati with random coefficients in a position-management problem.
