---
title: "Drissi 2022 — Solvability of Differential Riccati Equations and Applications to Algorithmic Trading with Signals"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: drissi-2022-solvability-differential-riccati
depth: standard
based_on: preprint
tags: [market-making, multi-asset, otc, rfq, indefinite-riccati, differential-riccati-equation, leqg, cara, ornstein-uhlenbeck, signals, hedging, hamiltonian-quadratic-approximation, bayesian-learning, poisson-flow]
relations:
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "«We use an approximation technique similar to that introduced in Bergault et al. (2018)» (p. 2); «We use the approximation method introduced in Bergault et al. (2018) to obtain a quoting and hedging strategy that can efficiently be computed by solving the DRE (1)» (p. 9). Bergault et al. 2018 = arXiv 1810.04383, the BEGV preprint. Extends it to multi-OU prices, signals, hedging instruments, client tiers and RFQ sizes."
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "The Hamiltonian terms are replaced by quadratic functions whose coefficients are «obtained using the Taylor expansion around p = 0» (p. 14), after a small-RFQ-size approximation of the finite differences (p. 14). The approximated HJB then closes with a quadratic ansatz in (q,S), eq. (22) (p. 15)."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "The nonlinear (A,B,C) part of the ODE system (23) «is equivalent to the DRE» (24) for P=[[A,½B],[½Bᵀ,C]] (p. 16); its quadratic coefficient U is indefinite, and existence and uniqueness follow from the paper's Theorem 2 via Corollary 1 (p. 16)."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Neither convention applies. RFQ arrivals have intensity kernels Λ^{i,n,s}(δ^{i,n,s}(z))ψ^{i,n,s}(dz), built by a change of measure from unit-rate compound Poisson processes (p. 10). They depend only on the current quote, with no history and no excitation."
  - target: bergault-2021-closed-form-approximations
    type: cites
    confidence: extracted
    because: "Cites «Bergault, P., Evangelista, D., Guéant, O., Vieira, D., 2018. Closed-form approximations in multi-asset market making. arXiv preprint arXiv:1810.04383» (references, p. 36) as the source of the approximation (pp. 2, 9)."
  - target: barzykin-2022-multi-currency-inventory
    type: cites
    confidence: extracted
    because: "«matrix DREs arise in various algorithmic trading problems; see Cartea et al. (2019, 2022c); Barzykin et al. (2022)» (p. 3); reference = Barzykin, Bergault, Guéant 2022, arXiv 2207.04100 (p. 36)."
  - target: gueant-2013-dealing-inventory-risk
    type: cites
    confidence: extracted
    because: "Cited among the market-making extensions «Guéant et al. (2012, 2013)» and for the curse of dimensionality in multi-asset market making (p. 3); reference Guéant, Lehalle, Fernandez-Tapia 2013 (p. 37)."
  - target: cartea-2014-buy-low-sell
    type: cites
    confidence: extracted
    because: "Cited as a market-making extension, «Cartea et al. (2014)» (p. 3); reference Cartea, Jaimungal, Ricci 2014, Buy low, sell high (p. 36). Cited only; its Hawkes content is not used."
---

# Solvability of Differential Riccati Equations and Applications to Algorithmic Trading with Signals

## Bibliographic Details

Drissi, Fayçal. 2022. "Solvability of Differential Riccati Equations and Applications to Algorithmic
Trading with Signals." *Applied Mathematical Finance* 29 (6): 457–493.
doi:10.1080/1350486X.2023.2241130.

**Read: arXiv 2202.07478v3 (preprint, dated 28 August 2023, 37 pp.); page and equation numbers on
this page follow that version.** The published AMF version was not read. Non-core work; preprint
accepted under the project's preprint policy. Author affiliation: Oxford-Man Institute, University of
Oxford. Code for the numerics: github.com/FDR0903/Market Making Riccati (fn. 5, p. 18).

⚠ Two different "Bergault et al." are cited. **Bergault et al. (2018)** is the BEGV preprint
(closed-form approximations, the approximation method used in §3). **Bergault et al. (2021)** is
Bergault–Drissi–Guéant, multi-asset optimal execution under OU dynamics (arXiv 2103.13773), whose
DRE existence result this paper generalises (p. 3). The second is not in the library.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $r$ | number of quoted assets (plus hedging instruments) | $d$ |
| $k$, $d=r+k$ | number of signals; dimension of the joint price-signal OU state | ⚠ source $d$ ≠ project $d$ |
| $S_t\in\mathbb R^d$, $R$, $\bar S$, $V$, $\Sigma=VV^\top$ | multi-OU prices and signals (12), mean-reversion matrix, long-run mean, volatility | $S_t,\Sigma$ (extended by signals); no project symbol for $R$ |
| $q_t\in\mathbb R^r$, $X_t$ | inventory, cash | $q_t$, $X_t$ |
| $\delta^{i,n,b}_t(z),\delta^{i,n,a}_t(z)$ | quotes for asset $i$, client tier $n$, RFQ size $z$ | $\delta^b,\delta^a$ (tier- and size-dependent) |
| $\Lambda^{i,n,s}(\delta)$, $\psi^{i,n,s}(dz)$ | intensity function, RFQ size distribution | $\Lambda e^{-k\delta}$ in the exponential case (p. 17) |
| $\rho$ | CARA risk aversion | $\gamma$ |
| $\Gamma\in\mathcal S^{++}_r$ | terminal inventory penalty, $q_T^\top\Gamma q_T$ (13) | ⚠ **not** BEGV's ergodic $\Gamma$ |
| $\eta\in\mathcal S^{++}_r$, $v_t$ | quadratic externalisation cost, hedging speed | no project symbol |
| $H^{i,n,s}(z,p)$ (17) | CARA Hamiltonian per size $z$ | $H^{i,s}$ |
| $\alpha_0,\alpha_1,\alpha_2$ | Taylor coefficients of $H$ at $p=0$ (p. 14) | $h_0,h_1,h_2$ |
| $\theta(t,q,S)$, $\tilde\theta$ | reduced value; its approximation | $\theta$ |
| $\tilde\theta=q^\top Aq+q^\top BS+S^\top CS+D^\top q+E^\top S+F$ (22) | quadratic ansatz in $(q,S)$ | project $\theta=-q^\top Aq-q^\top B-C$ ⇒ project $A\leftrightarrow-A$; project $B\leftrightarrow-(BS+D)$; project $C\leftrightarrow-(S^\top CS+E^\top S+F)$ |
| $P=\begin{pmatrix}A&\frac12B\\\frac12B^\top&C\end{pmatrix}$ | DRE unknown (24) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (DREs with indefinite coefficients; market making with signals and hedging; Bayesian execution; literature) | 1–4 |
| ✓ F1 | 2 General DRE (1)–(2) with block structure | 4–5 |
| ✓ F1 | 2.1 Equivalent LEQG (exponential-utility) control problem: (3)–(6), Assumptions 1–2, Prop. 1, Thm 1 | 5–8 |
| ✓ F1 | 2.2 Existence and uniqueness: Thm 2, Corollaries 1–2 | 8 |
| ✓ F1 | 3.1–3.2 Multi-asset OTC market making: multi-OU (12), quotes, RFQ marked point processes, inventory, externalisation, cash | 8–11 |
| ✓ F1 | 3.3 CARA problem (13), HJB (14)–(15), Prop. 2 (16), Hamiltonian (17), quotes (18)–(19) | 11–13 |
| ✓ F1 | 3.4 Quadratic approximation: HJB (20)–(21), ansatz (22), ODE system (23), DRE (24)–(25), approximate quotes (26), exponential case | 13–17 |
| ✓ F1 | 3.5 Numerics: single asset vs exact HJB grid (Figs 2–4); two cointegrated assets (Fig. 5) | 17–23 |
| ✓ | 4 Execution and statistical arbitrage with Bayesian drift learning: (27)–(32) | 23–26 |
| ✓ | 5 Conclusion | 26 |
| ✓ F1 | Appendix A (Prop. 1), B (Thm 1: HJB → Riccati, verification), C (Thm 2: a-priori bounds) | 27–35 |
| — | References | 35–37 |

## Kernthesen

### 1. ⭐⭐ Matrix DREs with indefinite coefficients have no general existence theory; this paper proves it for one structured family (pp. 1, 3–4)

The DRE (1) is $\dot P=Q+Y^\top P+PY+PUP$ on $[0,T]$ with $P\in\mathcal S_{d+r}$, block coefficients
$Q=\begin{pmatrix}Q_{11}&0\\0&0\end{pmatrix}$, $Y=\begin{pmatrix}Y_{11}&0\\Y_{21}&0\end{pmatrix}$,
$U=\begin{pmatrix}\rho U_{11}&0\\0&-U_{22}\end{pmatrix}$ with $U_{11}\ge0$, $U_{22}>0$, and terminal
condition (2) $P(T)=-\begin{pmatrix}\Psi&\frac12\Upsilon\\\frac12\Upsilon^\top&\Gamma\end{pmatrix}$ (p. 4). The
quadratic coefficient $U$ is indefinite. «The existence and uniqueness of solutions in general
remains an open problem for matrix DREs with indefinite matrix coefficients» (p. 3). Such equations
come from CARA (LEQG) trading problems, where «the quadratic term matrix coefficient has both
positive and negative eigenvalues, so classical existence results are not readily available» (p. 1).

### 2. ⭐⭐ The DRE is the Riccati equation of an exponential-utility (LEQG) control problem (pp. 5–8)

A $d$-dimensional observed state $dx_t=R(t)x_tdt+V(t)dW_t$ (4), a control $u\in\mathbb R^r$ with
$dy_t=u_tdt$, and a quadratic output $z$ (p. 6). Criterion (5): $\mathbb E[-\exp(-\rho(z_T-(x_T,y_T)^\top M_T(x_T,y_T)))]$ with $M_T=\begin{pmatrix}\Psi&\frac12\Upsilon\\frac12\Upsilon^\top&\Gamma\end{pmatrix}$ (p. 6).
Theorem 1: if the DRE has a solution $P=\begin{pmatrix}M_1&\frac12M_2\\\frac12M_2^\top&M_3\end{pmatrix}$, then
$\vartheta=-\exp(-\rho(z+\Theta))$ with $\Theta$ quadratic in $(x,y)$ (8)–(9), and the optimal control is
linear feedback (11) (p. 7). Verification is in Appendix B (pp. 29–32).

### 3. Three structural assumptions make the bounds work (p. 6)

Assumption 1: (i) $C=Q_{11}+Y_{21}^\top U_{22}Y_{21}\ge0$, so the state-quadratic term «is a cost and not
a gain»; (ii) $B\Sigma B^\top>0$; (iii) $Y_{11}(s)$ and $Y_{11}(t)$ commute for all $s,t$ (p. 6). Assumption 2:
$C\equiv\Psi=0$. Without Assumption 2, the results hold only for small enough risk aversion
$\rho\in(0,\bar\rho]$ (Prop. 1, Thm 1, Thm 2). With $r=d$, constant coefficients and Assumptions 1–2 the
DRE «is similar to that in Bergault et al. (2021)» (p. 6), i.e. Bergault–Drissi–Guéant.

### 4. ⭐⭐ Existence and uniqueness follow from a-priori bounds read off the control problem (pp. 8, 32–34)

Theorem 2: under Assumptions 1–2 the DRE has a unique symmetric solution on $[0,T]$; without
Assumption 2, for $\rho\in(0,\bar\rho]$ (p. 8). Proof (App. C): Cauchy–Lipschitz gives a left-maximal
solution on $(T-\tau,T]$; on that interval Theorem 1 identifies $\Theta$ as the value function. A
**lower bound** comes from evaluating the zero control (p. 32–33). An **upper bound** comes from
dropping nonnegative terms and solving a relaxed problem whose Riccati equation is linear
(C.2)–(C.7) (pp. 33–34). Both are quadratic polynomials in $(x,y)$, so $P$ stays in a compact
order interval and cannot blow up: «This contradicts the maximality of the solution, hence $\tau=\infty$»
(p. 34).

### 5. The result extends to shifted and congruence-transformed DREs (p. 8)

Corollary 1: replacing $P(T)$ by $P(T)-K$ and adjusting $\tilde Y=Y+UK$, $\tilde Q=Q+KUK+Y^\top K+KY$
keeps a unique solution. Corollary 2: congruence by a time-dependent invertible $Z(t)$ does too
(p. 8). These are the devices used to map the market-making DRE (24) onto the family (1) (p. 16).

### 6. ⭐ Multi-asset OTC model: multi-OU prices and signals, hedging instruments, client tiers, RFQ sizes (pp. 8–11)

$r$ quoted assets and $k$ signals follow a joint $d$-dimensional OU process $dS_t=R(\bar S-S_t)dt+VdW_t$
(12) (p. 9). Hedging instruments are added «by considering zero RFQ arrival intensities for these
assets» (p. 9). Quotes depend on asset $i$, client tier $n$ and size $z$ (pp. 9–10). Inventory
$dq^i_t=v^i_tdt+\sum_n\int z\,N^{i,n,b}(dt,dz)-\sum_n\int z\,N^{i,n,a}(dt,dz)$, where $v$ is the externalisation
(hedging) speed in a dealer-to-dealer venue with quadratic cost $v^\top\eta v$ (pp. 10–11).

### 7. ⭐⭐ RFQ flow is quote-dependent Poisson: no history, no excitation (p. 10)

The marked point processes are constructed from «two independent compound Poisson processes
$M^{i,n,b}$ and $M^{i,n,a}$ with intensity one», then reweighted by a Radon–Nikodym density so that under
$\mathbb P$ they have intensity kernels $\lambda^{i,n,b}_t(dz)=\Lambda^{i,n,b}(\delta^{i,n,b}_t(z))\psi^{i,n,b}(dz)$ (p. 10). $\Lambda$ is
$C^2$, decreasing, vanishes at infinity and satisfies the usual curvature condition
$\sup\Lambda\Lambda''/(\Lambda')^2<2$ (p. 10). Arrivals across assets, tiers and sides are independent given
the quotes. Cross-asset dependence enters only through prices and signals ($R$, $\Sigma$) and through
the inventory penalty.

### 8. CARA objective with terminal inventory penalty; the HJB is written but not verified (pp. 11–13)

Objective (13): $\mathbb E[-\exp(-\rho(X_T+q_T^\top\mathcal JS_T-q_T^\top\Gamma q_T))]$ (p. 11). With
$w=-\exp(-\rho(x+q^\top\mathcal JS+\theta))$ the HJB reduces to (16) for $\theta(t,q,S)$, with size-dependent
Hamiltonians $H^{i,n,s}(z,p)=\sup_\delta\frac{\Lambda^{i,n,s}(\delta)}{\rho z}(1-\exp(-\rho z(\delta-p)))$ (17) (p. 13). Quotes
follow from $\tilde\delta(z,p)=\Lambda^{-1}(\rho zH(z,p)-\partial_pH(z,p))$ (19). The author does not verify
that $\theta$ is the value function: «It is beyond the scope of this paper to provide a formal solution to
the optimal quote problem and we focus on the approximation technique» (p. 13).

### 9. ⭐⭐ Approximation: small RFQ size, then a quadratic Taylor expansion of the Hamiltonian at p = 0 (pp. 13–15)

«For small RFQ sizes, we use the approximation» $\frac{\theta(q)-\theta(q+ze^i)}z\approx-\frac{\theta(q)-\theta(q-ze^i)}z$ (p. 14), so
bid and ask Hamiltonians are evaluated at opposite shadow prices. Each $H$ is replaced by
$\alpha_0(z)+\alpha_1(z)p+\frac12\alpha_2(z)p^2$, with coefficients «obtained using the Taylor expansion around
$p=0$» (p. 14). The approximated HJB (20) closes with the quadratic ansatz
$\tilde\theta=q^\top Aq+q^\top BS+S^\top CS+D^\top q+E^\top S+F$ (22) (p. 15). This is BEGV's approximation, with the
state augmented by the price-signal vector $S$.

### 10. ⭐⭐ The approximate value solves a joint (q,S) Riccati with indefinite quadratic term, then linear ODEs (pp. 15–16)

The ODE system (23) «can be solve[d] sequentially. First, solve the subsystem in $(A,B,C)$, then solve
the linear subsystem in $(D,E)$, and $F$ is obtained by an integration» (p. 16). $(A,B,C)$ is equivalent
to the DRE (24) $\dot P=Q+Y^\top P+PY+PUP$ with
$U=\begin{pmatrix}-2(V^b_{2,1}+V^a_{2,1})-\eta^{-1}&0\\0&2\rho\Sigma\end{pmatrix}$ and $P(T)=\begin{pmatrix}-\Gamma&0\\0&0\end{pmatrix}$ (25),
where $V^s_{2,1}$ are diagonal matrices of size-weighted Hamiltonian curvatures (p. 16). The
inventory block of $U$ is negative and the price block positive. Under
$2V^b_{2,1}+2V^a_{2,1}+\eta^{-1}\ge0$ Assumptions 1–2 hold, and Corollary 1 gives existence and uniqueness
(p. 16). Only the $q$-$q$ block $A$ feeds the inventory skew; $B(t)S$ adds a signal-driven term to the
shadow price.

### 11. With exponential intensities the approximate quotes are explicit and linear in (q, S) (p. 17)

For $\Lambda^{i,n}(\delta)=A^{i,n}e^{-k^{i,n}\delta}$: $\bar\delta^{i,n,b}(z)=-2q^\top A e^i-ze^{i\top}Ae^i-S^\top B^\top e^i-e^{i\top}D+\frac1{\rho z}\log(1+\frac{\rho z}{k^{i,n}})$,
and symmetrically for the ask (p. 17). The externalisation rate is
$\bar v^*_t=\frac12\eta^{-1}(2A(t)q_t+B(t)S_t+D(t))$ (p. 16). Quotes and hedging are thus affine in inventory and
in the signal-augmented price vector.

### 12. ⭐ Accuracy is checked only qualitatively, and only for one asset (pp. 17–21)

Logistic intensity $\Lambda(\delta)=\lambda_{\text{base}}/(1+\exp(a+b\delta))$, Gamma RFQ sizes, $T=7$ days (Tables 1–3,
pp. 17–18). Exact quotes come from an implicit Euler scheme for the HJB in dimension three (time,
inventory, price; fn. 4, p. 18). For $R=0$ the approximation «is satisfactory for different levels of
the inventory». For $R>0$ the approximate bid deviates when $S>\bar S$ with large negative inventory or
$S<\bar S$ with large positive inventory, and symmetrically for the ask (p. 20). No error numbers are
reported; Figure 4 shows the curves. The author's summary: «the approximated quotes capture all the
relevant financial effects of the optimal quoting strategy» (p. 20).

### 13. ⭐ For two cointegrated assets the exact problem is not solved; only the approximation is shown (pp. 21–23)

«To obtain the optimal quote shifts … one should employ a numerical scheme in dimension five; one
for time, two for inventory in both assets, and two for the asset prices of both assets, which
becomes rapidly intractable with fine grids. In contrast, the approximated shifts (26) are quickly
computed with Riccati ODE solvers» (p. 21). Uncorrelated noise ($V=I$) with $R=\begin{pmatrix}0.5&-0.5\\-0.5&0.5\end{pmatrix}$
makes $S^1-S^2$ stationary. The speculative component then «uses the cointegration factor $S^1-S^2$
instead of the prices of the individual assets» (p. 22). Cross-asset quoting effects come from the
drift matrix $R$, not from correlated noise or correlated flow.

### 14. Bayesian drift learning yields a time-dependent OU drift and a DRE in the same family (pp. 23–26)

Under a Gaussian prior on the drift, the filtered price dynamics are $dS_t=R(t)(\bar S-S_t)dt+Vd\hat W_t$
with a time-dependent matrix $R(t)$ built from the posterior covariance ((28)–(29), p. 24), «linear and resemble those of a
multi-OU process with a time-dependent mean reversion matrix» (p. 24). The execution problem reduces
to DRE (32), and since the $R(s)$ commute, Theorems 1–2 apply (p. 26). Performance is not studied
(p. 26).

## What this source does not address

- **Self- or cross-exciting flow.** RFQ arrivals are quote-dependent Poisson with i.i.d. sizes
  (p. 10). No Hawkes process, no intensity state, no dependence on past trades.
- **Verification of the exact market-making problem.** «beyond the scope of this paper» (p. 13);
  the reader is referred to Barzykin et al. 2023.
- **Quantitative accuracy or regret.** Only figures, one asset (p. 20); no error metric; the
  multi-asset exact solution is not computed (p. 21).
- **Error order of the approximation.** Neither the small-size step nor the Taylor step comes with
  an asymptotic parameter or bound.
- **Risk-adjusted (non-CARA) objective.** Only CARA; the BEGV risk-adjusted variant is not discussed.
- **Performance of the Bayesian strategy.** Deferred to Bismuth et al. 2019 (p. 26).

## Model card

| Field | Value |
|---|---|
| Assets | $r$ quoted assets, plus hedging instruments (zero RFQ intensity) and $k$ signals in a joint $d=r+k$ OU state (p. 9); numerics with 1 and 2 assets |
| Kernel | Poisson — intensity kernel $\Lambda^{i,n,s}(\delta)\psi^{i,n,s}(dz)$ obtained by change of measure from unit-rate compound Poisson processes (p. 10) |
| Excitation | none — no self, cross-side or cross-asset excitation; cross-asset coupling only through prices/signals ($R,\Sigma$) and the inventory penalty |
| Who excites the flow | n/a — no excitation; intensities depend only on the current quote (p. 10) |
| Objective | CARA utility of terminal wealth with inventory penalty $q_T^\top\Gamma q_T$ (13) (p. 11); externalisation cost $v^\top\eta v$ |
| Solution method | closed form up to ODEs: small-RFQ-size step + quadratic Taylor expansion of the Hamiltonian at $p=0$ (BEGV), quadratic ansatz in $(q,S)$ (22), indefinite DRE (24) for $(A,B,C)$ + linear ODEs for $(D,E)$; existence via LEQG representation and a-priori bounds (Thm 2) |
| Benchmark | exact HJB by implicit Euler on a 3-D grid (single asset only; fn. 4, p. 18) |
| Reported regret / gap numbers | none — qualitative comparison of quote curves (Fig. 4, p. 21); deviations named at large inventory with $R>0$ (p. 20) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 1, 2, 4, 6, 7, 9, 10, 12, 13.**

### What this focus needs beyond the Kernthesen

1. **Verdict: a multi-asset BEGV extension with an extra stochastic factor, but the factor is a
   price-signal OU, not an intensity.** The flow is quote-dependent Poisson (Kernthese 7). So the
   paper does not model self- or cross-exciting order flow. What it does show is how far the BEGV
   closure stretches when the state is augmented by a Gaussian factor $S$. The approximate value
   is quadratic jointly in $(q,S)$. The Riccati unknown grows from $r\times r$ to $(r+d)\times(r+d)$, and
   it becomes indefinite (Kernthese 10). Cite it as the "BEGV + exogenous Gaussian factor" precedent
   and as an existence theorem for the resulting indefinite DRE.
2. **Why the closure holds here and not under Hawkes [I from eqs. (16), (20), (22)].** The factor
   $S$ enters the reduced HJB *additively*. It appears in the drift term $(\bar S-S)^\top R(\cdots)$, in the
   diffusion term, and, through $B(t)S$, inside the shadow price $p$. It never multiplies the
   Hamiltonian. After the quadratic Taylor step every term is a polynomial of degree ≤ 2 in
   $(q,S)$, so the ansatz (22) closes exactly. A Hawkes intensity enters *multiplicatively*,
   $\lambda_jH(p^j)$. With $p^j$ depending on $\lambda$, the product is quadratic to cubic in $\lambda$ (Stage 2a design,
   "Why it does not close exactly"). The joint quadratic ansatz then fails. **Additive factors
   close; multiplicative (intensity) factors do not.** That is the sharpest contrast this source
   offers.
3. **Where the approximation breaks [I from p. 20].** The Taylor point is $p=0$ for every state.
   When $R>0$, the term $B(t)S$ pushes the shadow price away from 0 whenever $S$ is far from $\bar S$. The
   reported deviations occur exactly where inventory and price displacement point the same way
   (p. 20), i.e. where $|p|$ is largest. This matches the Barzykin 2022 finding that the quadratic
   approximation degrades under large flow imbalance
   ([[barzykin-2022-multi-currency-inventory]], noted in the Stage 2a design S3). A factor that
   moves the shadow price far from the expansion point degrades the approximation, whether it is a
   price signal or an intensity.
4. **What carries over to several assets.** The DRE machinery is fully multi-asset, with
   cross-asset coupling through $\Sigma$ and $R$ (cointegration, Kernthese 13). The flow is
   independent across assets, so there is no cross-asset excitation. The two-asset example has
   uncorrelated noise ($V=I$), so cross-asset skew there comes only from the drift. Accuracy is not
   tested in two dimensions.
5. **Bearing on D1 (fill-driven CARA linearisation).** Partial. This is a CARA market-making model
   whose $\exp$-transform turns the HJB into (16) with Hamiltonians $(1-e^{-\rho z(\delta-p)})/(\rho z)$ (17). The
   CARA Hamiltonian depends on the size $z$ and on $\rho$. A fill-driven (self-exciting on own
   fills) intensity would multiply this $H$ by a state variable, which is the same obstruction as in
   item 2.
6. **Bearing on D2 ($\lambda$-dependent Riccati coefficients).** Here the inventory coefficient $A(t)$
   is deterministic and does not depend on the factor. The factor enters only through the cross
   term $B(t)S$ (Kernthese 10). If a Hawkes intensity were added as an additive factor, it would
   only shift the shadow price. In the flow-driven model it also scales the curvature
   $\sum_j\lambda_jh_2$ inside $A$'s Riccati. That is why $A$ becomes $\lambda$-dependent there and is not here [I].

### Bearing on Stage 2a (`input/ideas/hawkes-perturbative-closed-form-design.md`) [I]

- **S1 global existence: the a-priori-bound technique is the relevant tool.** Stage 2a notes that
  BEGV's comparison argument does not cover the coupled system. Drissi's route avoids comparison
  arguments. It represents the Riccati equation as the value of an auxiliary control problem, and
  bounds that value from below (any fixed control) and above (a relaxed problem). Bounded $P$ then
  means no finite-time blow-up (Kernthese 4). For the order-0 Riccati with time-dependent forecast
  $m(t)$, Theorem 2 already allows continuous time-dependent coefficients. For the coupled
  order-0/order-1 system an analogous control representation would have to be built.
- **PSD of the inventory block.** Existence here needs the effective curvature
  $2V^b_{2,1}+2V^a_{2,1}+\eta^{-1}\ge0$ (p. 16). In Stage 2a the analogue is positivity of the intensity-weighted
  curvature $\sum_jm_j(t)h_2$ (plus the order-1 correction). That links Stage 2a's PSD/clipping
  question to a condition of the same shape.
- **Not a precedent for the expansion itself.** No small parameter, no error order, no intensity
  factor. The single-asset grid comparison is a model for Stage 2a's S3 *design* (exact grid vs
  closed form), but it gives no numbers to compare against.

### Direct quotes (for the draft)

> "The existence and uniqueness of solutions in general remains an open problem for matrix DREs with indefinite matrix coefficients." (p. 3)

> "We use the approximation method introduced in Bergault et al. (2018) to obtain a quoting and hedging strategy that can efficiently be computed by solving the DRE (1)." (p. 9)

> "It is beyond the scope of this paper to provide a formal solution to the optimal quote problem and we focus on the approximation technique (see Barzykin et al., 2023, for a rigorous solution to a similar problem)." (p. 13)

> "To obtain the optimal quote shifts δ^{b,⋆} and δ^{a,⋆}, one should employ a numerical scheme in dimension five; one for time, two for inventory in both assets, and two for the asset prices of both assets, which becomes rapidly intractable with fine grids. In contrast, the approximated shifts (26) are quickly computed with Riccati ODE solvers." (p. 21)

> "Most importantly, the approximated quotes capture all the relevant financial effects of the optimal quoting strategy." (p. 20)

### Examples & illustrations (for later drafting)

- Figure 4 (p. 21) with its text (p. 20): optimal vs approximate quotes, single asset. Deviations
  appear where inventory and price displacement push the shadow price far from the Taylor point.
  It is a ready illustration of "accuracy of a $p=0$ expansion depends on the state".
- Eq. (24)–(25) (p. 16): the $U$ matrix with a negative inventory block and a positive price block is
  a compact example of an indefinite market-making Riccati.
- The cointegration example (Fig. 5, p. 22): quotes driven by $S^1-S^2$. It shows cross-asset quote
  effects arising from the drift alone, as distinct from flow contagion.

### Boundary of this focus

The source has no excitation and no intensity state. The additive/multiplicative distinction
(focus item 2), the link to Barzykin 2022 and every Stage 2a remark are the project's inferences.
Its accuracy evidence is qualitative and single-asset, so it cannot inform the regret comparison.

## Mentioned entities

- Models: [[begv-2021-model]] (extended), [[glft-2013-model]] (lineage, via Guéant et al. 2013), [[cartea-jaimungal-ricci-model]] (cited, not used)
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[who-excites-the-flow]], [[shadow-price]], [[hawkes-process]] (absent from the source; used only in the focus inference)
- Sources: [[bergault-2021-closed-form-approximations]], [[barzykin-2022-multi-currency-inventory]], [[gueant-2013-dealing-inventory-risk]], [[cartea-2014-buy-low-sell]]; contrast pages [[zhang-2020-backward-stochastic-riccati]] (random-coefficient, definite LQ Riccati), [[fujii-2015-optimal-position-management]] (multi-asset stochastic Riccati with exogenous flow)
- Works cited by the source, not in the library: Bergault, Drissi & Guéant 2021 (multi-asset execution under OU, arXiv 2103.13773); Barzykin, Bergault & Guéant 2023 (dealer markets with hedging, Math. Finance); Bismuth, Guéant & Pu 2019 (drift uncertainty); Guéant 2017 (optimal market making); Guéant & Manziuk 2019; Cartea, Gan & Jaimungal 2019 (co-integrated assets); Jacobson 1973; Whittle 1990; Lim & Zhou 2005; Chen, Li & Zhou 1998; Rami et al. 2001; Hu & Zhou 2003; Brémaud & Jacod 1977.

## Connections

- Builds on: [[begv-2021-model]] / [[hamiltonian-quadratic-approximation]], extended by multi-OU
  prices, signals, hedging, client tiers and RFQ sizes; [[matrix-riccati-equation]], here in an
  indefinite, state-augmented form.
- Compare: [[zhang-2020-backward-stochastic-riccati]]. Zhang has random coefficients but a definite
  LQ Riccati; Drissi has deterministic time-varying coefficients, an indefinite Riccati, and a CARA
  origin.
- Compare: [[fujii-2015-optimal-position-management]], a multi-asset inventory problem with exogenous
  flow and an exact (stochastic) Riccati; here the flow is quote-controlled and the Riccati is
  approximate.
- Compare: [[barzykin-2022-multi-currency-inventory]], same BEGV approximation family; both report
  degradation when the shadow price moves far from the expansion point.
