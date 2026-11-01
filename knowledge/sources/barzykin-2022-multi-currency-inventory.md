---
title: "Barzykin, Bergault, Guéant 2022 — Dealing with Multi-Currency Inventory Risk in FX Cash Markets"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: barzykin-2022-multi-currency-inventory
depth: standard
tags: [market-making, multi-asset, fx, closed-form, hamiltonian-approximation, riccati, internalization, externalization, hedging, poisson, logistic-intensity]
relations:
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "«Following the same ideas as in [4] [BEGV], we now approximate … the Hamiltonian function H^{n,i,j} by a quadratic function» with the Taylor coefficients at p = 0 (p. 5); hedging Hamiltonians are approximated by 0 (p. 5)."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "Eq. (5): A' = 2AMA − Σ⊙A − 2D(μ)A − (γ/2)Σ, called «a matrix Riccati-like differential equation whose solution can be approximated very easily using an Euler scheme» (p. 6)."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "Ref. [4] = BEGV 2021; «the techniques proposed in [4] can be adapted so that approximations of the optimal strategies can be obtained by solving a low-dimensional matrix Riccati-like differential equation» (p. 2)."
  - target: bergault-2021-closed-form-approximations
    type: builds-on
    confidence: extracted
    because: "Same as above: the quadratic-Hamiltonian reduction of [4] (p. 2, p. 5) is transferred to a currency-labelled state Y = (q^i S^i) with multiplicative noise and crosses."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Neither convention: client intensities Λ^{n,i,j}(z,δ) = λ^{n,i,j}(z) f(z,δ) have deterministic, constant amplitudes (p. 3); no excitation of any kind."
---

# Dealing with Multi-Currency Inventory Risk in FX Cash Markets

## Bibliographic Details

Barzykin, Alexander, Philippe Bergault, and Olivier Guéant. 2022. *Dealing with multi-currency
inventory risk in FX cash markets*. arXiv:2207.04100v4 [q-fin.TR], 30 October 2023. 11 pp.
(10 pp. text + references). Affiliations: HSBC London; École Polytechnique (CMAP); Université
Paris 1 Panthéon-Sorbonne. Part of the HSBC FX Research Initiative (p. 10).

**Read: arXiv 2207.04100v4 (preprint); page/equation numbers follow it.** Non-core work; preprint
accepted under the project's preprint policy. Whether a journal/Risk.net version exists was not
verified at ingest (see the bib note) — if one does, add `based_on: preprint`.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $d$ | number of **currencies**, currency 1 = reference (USD), so $d-1$ risky prices | $d$ (but note: $d$ currencies ⇒ $d-1$ risk factors and up to $d(d-1)/2$ pairs) |
| $q^i_t$ | inventory in currency $i$ | $q_t$ (native units) |
| $Y^i_t=q^i_tS^i_t$ | inventory of currency $i$ **in reference currency** — the state variable | plays the role of $q_t$ in the ansatz |
| $S^i_t$, $\mu^i_t$, $\sigma^i$, $\Sigma=(\rho^{ij}\sigma^i\sigma^j)$ | price of currency $i$ in USD (geometric BM), drift, vol, covariance | $S_t,\sigma,\Sigma$ |
| $J^{n,i,j}(dt,dz)$, tier $n\le N$, size $z$ | client trades in pair $(i,j)$ | — |
| $\Lambda^{n,i,j}(z,\delta)=\lambda^{n,i,j}(z)f^{n,i,j}(z,\delta)$ | intensity function | GLFT $\Lambda e^{-k\delta}$ replaced by $\lambda(z)\times$ logistic $f$; ⚠ $\lambda^{n,i,j}(z)$ is a **deterministic constant amplitude**, not a Hawkes $\lambda_t$ |
| $f=1/(1+e^{\alpha+\beta\delta})$ | logistic fill probability | $f(\delta)$; ⚠ $\beta$ is a logistic slope, not a Hawkes decay |
| $\delta^{n,i,j}$ | markup (quote) | $\delta^b,\delta^a$ |
| $\xi^{i,j}_t$, $L^{i,j}(\xi)=\psi|\xi|+\eta|\xi|^{1+\phi}$, $k^i$ | D2D hedging rate, execution cost, permanent impact | no project symbol |
| $H^{n,i,j}(z,p)$, $\alpha_0,\alpha_1,\alpha_2$ | client Hamiltonian and its Taylor coefficients at $p=0$ | $H^{i,s}$, $h_2=\alpha_2=H''(0)$ |
| $\gamma$, $\kappa$ | risk aversion; terminal penalty $\ell(y)=y^\top\kappa y$ | $\gamma$ |
| $\check\theta=-y^\top Ay-y^\top B-C$ | approximate value function | $\theta=-q^\top Aq-q^\top B-C$ (same signs) |
| $\overline M,\underline M,P$; $M,V,\tilde V(A)$ | intensity-weighted moments of $\alpha_2,\alpha_1$ (eq. after (5)) | ≈ BEGV's $D_+$ / $\Delta$ matrices, here pair-indexed |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; Introduction (multi-asset MM, curse of dimensionality, reduction of [4]; FX specificity of crosses; contributions) | 1–2 |
| ✓ F1 | Multi-currency model: market and dealer; exchange rates; pricing ladders and tiers (logistic $\Lambda$); D2D segment ($\xi$, $L$) | 2–3 |
| ✓ F1 | Dynamics of state variables ($q$, $X$, $S$ with permanent impact; $Y=qS$ Markovian) | 3–4 |
| ✓ F1 | Optimization problem (risk-adjusted MtM, eq. on p. 4) | 4 |
| ✓ F1 | HJB (1), optimal quotes (2), optimal hedging rates (3) | 5 |
| ✓ F1 | Approximation of the value function: quadratic $\check H$, hedging Hamiltonian set to 0, eq. (4), Riccati-like system (5) and matrices | 5–6 |
| ✓ F1 | Numerical results: $d=2$ validation vs. grid (qualitative); 5-currency illustration; Table 1; Figs 1–5 | 6–10 |
| ✓ | Concluding remarks; acknowledgment | 10 |
| — | References | 11 |

## Kernthesen

### 1. ⭐ FX market making differs from same-currency multi-asset MM because each pair values one currency in terms of another, and crosses offer redundant routes (p. 2)

«Existing multi-asset market making models consider assets labelled in the same currency … However,
the problem faced by FX dealers is different: each currency pair provides indeed a valuation of one
currency in terms of the other» (p. 2). Crosses create «both complexity and opportunities since there
are several ways to achieve the same result (e.g. buying EURGBP is equivalent to buying EURUSD and
selling GBPUSD)» (p. 2). Claimed as the first model of an FX dealer quoting directs **and** crosses
with D2D hedging (p. 2).

### 2. ⭐ The right state variable is the inventory measured in reference currency, $Y^i=q^iS^i$, which is Markovian (p. 4)

With geometric exchange rates (p. 3) the process $Y^i$ has dynamics
$dY^i=\mu^iY^idt+\sigma^iY^idW^i+k^i(\ldots)Y^idt+\int z(J^{n,i,j}-J^{n,j,i})+(\ldots)dt$ (p. 4): a
jump-diffusion with **multiplicative** Brownian noise. This «smart choice of the state variables»
lets the problem «boil down to solving a partial differential equation» in $(t,y)\in[0,T]\times\mathbb R^d$
(p. 2) without the price as a state.

### 3. Client flow: tiered, sized, pair-indexed marked point processes with logistic fill probability and constant amplitudes (p. 3)

$\nu^{n,i,j}_t(dz)=\Lambda^{n,i,j}(z,\delta^{n,i,j}(t,z))dz$ with
$\Lambda^{n,i,j}(z,\delta)=\lambda^{n,i,j}(z)f^{n,i,j}(z,\delta)$, $f=1/(1+e^{\alpha^{n,i,j}(z)+\beta^{n,i,j}(z)\delta})$
(p. 3), following [3] (Barzykin–Bergault–Guéant, Risk 2022). The amplitude $\lambda^{n,i,j}(z)$ depends
on size, tier and pair only — it is deterministic and time-constant. Table 1 gives the five-point size
ladders, e.g. EURUSD $\lambda(z)=900,540,234,90,36$ per day for $z=1,5,10,20,50$ M$ (p. 7).

### 4. Hedging (externalization) is a continuous D2D trading rate with linear + quadratic cost and linear permanent impact (pp. 3–4)

$\xi^{i,j}_t$ for $i<j$; cost $L^{i,j}(\xi)=\psi^{i,j}|\xi|+\eta^{i,j}|\xi|^{1+\phi^{i,j}}$, $\phi=1$ (p. 3);
impact $k^i$ on $S^i$ (p. 3). Unavailable D2D pairs are modelled by very high cost (fn. 4, p. 3).
Only the dealer's own D2D trades move prices; client-flow adverse selection is explicitly left out
(fn. 5, p. 4).

### 5. Objective: risk-adjusted (mean–running-variance) mark-to-market, not CARA (p. 4)

Maximise $\mathbb E[X_T+\sum_iY^i_T-\frac\gamma2\int_0^TY_t^\top\Sigma Y_tdt-\ell(Y_T)]$ (p. 4), which after
Itô becomes a running-reward problem with spread income, drift, impact and cost terms (p. 4).
This is the Cartea–Jaimungal-type objective used in BEGV's "model B".

### 6. HJB and exact optimal controls are the standard finite-difference/shadow-price forms (p. 5)

HJB (1) on $(t,y)$ with diffusion term $\frac12\mathrm{Tr}(\mathcal D(y)\Sigma\mathcal D(y)D^2_{yy}\theta)$,
client Hamiltonians $H^{n,i,j}(z,p)=\sup_\delta f(z,\delta)(\delta-p)$ and hedging Hamiltonians
$\mathcal H^{i,j}(p)=\sup_\xi p\xi-L(\xi)$. Quotes (2): $\delta^*=\bar\delta(z,[\theta(t,Y)-\theta(t,Y+ze^i-ze^j)]/z)$;
hedge rates (3) via $\mathcal H^{i,j\prime}$ of a gradient difference plus impact terms (p. 5). Solving (1)
on an inventory grid suffers the curse of dimensionality (p. 1, p. 6).

### 7. ⭐⭐ Approximation: replace client Hamiltonians by their second-order Taylor polynomial at $p=0$ and drop the hedging Hamiltonians entirely (p. 5)

«Following the same ideas as in [4], we now approximate … the Hamiltonian function $H^{n,i,j}$ by a
quadratic function $\check H^{n,i,j}(z,p)=\alpha_0+\alpha_1p+\frac12\alpha_2p^2$», with «a natural choice»
$\alpha_k=\partial^k_pH(z,0)$ (p. 5). «The structure of the problem leads us to approximate the Hamiltonian
terms associated with $\mathcal H^{i,j}$ by 0 since $\mathcal H^{i,j}$ is typically flat around 0 when
$\psi^{i,j}>0$» (p. 5). **Consequence:** neither hedging costs nor permanent impact $k^i$ enter $A$ or
$B$; externalization is computed afterwards from $(A,B)$ (p. 6). No error estimate or small parameter
is given for either approximation.

### 8. ⭐⭐ With quadratic terminal penalty the approximate HJB is solved exactly by a quadratic ansatz; $A$ solves a matrix Riccati-like ODE with a Hadamard term (pp. 5–6)

If $\ell(y)=y^\top\kappa y$, (4) is solved by $\check\theta=-y^\top Ay-y^\top B-C$ with (5):
$A'=2AMA-\Sigma\odot A-2\mathcal D(\mu)A-\frac\gamma2\Sigma$,
$B'=\mu-\mathcal D(\mu)B+2AV+2A\tilde V(A)+2AMB$, $A(T)=\kappa$, $B(T)=0$ (p. 5), with
$M=\mathcal D((\overline M+\overline M^\top)U)-(\overline M+\overline M^\top)$, $V=(\underline M-\underline M^\top)U$,
$\tilde V(A)=(\overline V(A)-\overline V(A)^\top)U$, $\overline V(A)=\overline{\mathcal D}(A)P+P\overline{\mathcal D}(A)-2P\odot A$ (p. 6).
The $\Sigma\odot A$ term comes from the multiplicative noise of $Y$ (Kernthese 2) and is what makes the
equation "Riccati-*like*" rather than BEGV's $A'=2AD_+A-\frac12\gamma\Sigma$; $M$ is a
graph-Laplacian-type matrix over currency pairs, so crosses couple currencies inside the quadratic
term. $B$ depends on $A$ nonlinearly only through $\tilde V(A)$ (size-squared moments $P$). [I: the
printed $-2\mathcal D(\mu)A$ is not symmetric; presumably $-\mathcal D(\mu)A-A\mathcal D(\mu)$ is meant.
Irrelevant numerically since $\mu=0$ (p. 6).]

### 9. ⭐ The reduction scales quadratically in the number of currencies and is solved by an explicit Euler scheme (pp. 2, 6)

«The dimensionality of the differential equations to solve only grows quadratically with the number
of currencies, hence linearly with the maximal number of currency pairs» (p. 2). (5) «can be
approximated very easily using an Euler scheme (i.e. without suffering from the curse of
dimensionality …)» (p. 6). No closed tanh form is given (the Hadamard term prevents BEGV's formula).
Approximate quotes and hedge rates follow by plugging $\check\theta$ into (2)–(3) (p. 6).

### 10. ⭐ Accuracy was checked only for $d=2$ against a monotone implicit grid scheme, reported qualitatively (p. 6)

«we have validated, when $d=2$, our approximations against the optimal strategy computed thanks to the
solution of Eq. (1) approximated with a monotone implicit Euler scheme on an inventory grid … Only under
extreme conditions which are not practically relevant, such as strong order flow asymmetry (as high as
fivefold) and very high or very low risk aversion, have we detected significant deviations» (p. 6).
No numbers, tables or figures of the gap are shown.

### 11. Correlation and crosses tilt pricing of other pairs: positive correlation yields protective EURUSD skew on GBP inventory (pp. 6–7)

Fig. 1: «Without correlation and without the cross, EURUSD pricing would be unaffected by GBP
inventory. Here, instead, positive correlation leads to a protective pricing strategy for EURUSD. The
pricing of the cross pair EURGBP also attracts or diverts the flow as a function of the GBP inventory»
(p. 7). Stationary quotes are taken from $A(0),B(0)$ with $T=0.05$ days (p. 6).

### 12. Externalization: a pure internalization zone, slanted by correlation and by the cross even at zero correlation (pp. 8–9)

Fig. 2: pure internalization in the middle, near-linear hedging beyond; large positions offloaded also
into correlated directs and crosses because «the price skew has likely already been exploited» (p. 8).
Fig. 3: «the presence of the cross influences the internalization zone even without correlation: it is
slanted and not horizontal even when $\rho=0$» (p. 8).

### 13. Portfolio-level risk decorrelates faster than individual positions, saving costs; internalization ≈ 80 % (pp. 8–10)

Monte Carlo (Figs 4–5): the inventory distribution follows the risk contours $\frac\gamma2y^\top\Sigma y$;
«the inventory autocorrelation functions of individual pairs decay much slower than the risk
autocorrelation function. This means that the dealer is able to offload risk fast while essentially
trading slower» (p. 8); the internalization ratio matches reported ~80 % for G10 (p. 8).

## What this source does not address

- **Any stochastic, time-varying or self-exciting liquidity.** Amplitudes $\lambda^{n,i,j}(z)$ are
  constants (p. 3, Table 1 p. 7); no Hawkes, no regime, no intensity state variable.
- **Perturbation theory.** The two approximations (quadratic $\check H$, $\mathcal H\approx0$) carry no
  small parameter and no error order (p. 5).
- **Adverse selection / client-flow impact** — explicitly excluded (fn. 5, p. 4).
- **Quantitative accuracy reporting** — the $d=2$ validation is verbal only (p. 6).
- **CARA utility, RL, neural methods** — none.

## Model card

| Field | Value |
|---|---|
| Assets | $d$ currencies (reference + $d-1$ risky), all $d(d-1)$ ordered pairs incl. crosses; illustration $d=5$ (USD, EUR, JPY, GBP, CHF) (pp. 2, 6) |
| Kernel | Poisson — constant size/tier/pair amplitudes $\lambda^{n,i,j}(z)$ with logistic fill $f$ (p. 3) |
| Excitation | none |
| Who excites the flow | n/a — no excitation; flow responds only to the current quote |
| Objective | risk-adjusted MtM with running penalty $\frac\gamma2Y^\top\Sigma Y$ and terminal $\ell(Y_T)$ (p. 4); not CARA |
| Solution method | closed-form approximation: quadratic Taylor of client Hamiltonians at $p=0$, hedging Hamiltonian set to 0, matrix Riccati-like ODE (5) for $A$ + linear-in-$B$ ODE, solved by Euler (pp. 5–6) |
| Benchmark | $d=2$: monotone implicit Euler scheme for the exact HJB (1) on an inventory grid (p. 6) |
| Reported regret or gap numbers | none — "significant deviations" only under extreme asymmetry/risk aversion, stated verbally (p. 6) |

<!-- ═══ FOKUS ═══ -->

## Focus: Perturbative/asymptotic closed forms for multi-asset market making with a stochastic intensity factor (Hawkes or Markov-modulated): which expansion, around which point, with which small parameter and error order; whether it closes into finite matrix ODEs; how accuracy is tested; how much of Stage 2a it already covers. — 2026-10-26

**Carries Kernthesen 2, 3, 7, 8, 9, 10.**

### What this focus needs beyond the Kernthesen

1. **Which expansion, around which point.** Only one expansion, in the *Hamiltonian's argument*:
   second-order Taylor of $H^{n,i,j}(z,\cdot)$ at $p=0$ (p. 5), exactly as BEGV. There is no expansion
   in an intensity or liquidity factor, because the paper has no such factor: amplitudes are constants
   (p. 3). The hedging Hamiltonian is truncated at order 0 (p. 5).
2. **Small parameter and error order.** None stated. The approximation is justified heuristically
   («a natural choice», «typically flat around 0», p. 5).
3. **Closure into finite matrix ODEs.** Yes, for the deterministic-intensity problem: a $d\times d$
   Riccati-like ODE for $A$ plus an ODE for $B$ that is linear in $B$ given $A$ (eq. 5, p. 5). New
   relative to BEGV: a Hadamard term $\Sigma\odot A$ from multiplicative noise and pair-graph coupling
   in $M$ — so the closure survives a non-standard (non-Riccati) linear term. [I] This is a small but
   useful datum for Stage 2a: the quadratic ansatz tolerates extra linear-in-$A$ operators
   (Hadamard products) without losing closure.
4. **Accuracy test.** $d=2$ against a monotone implicit grid solver of the exact HJB (1), comparing
   strategies and efficient frontiers, reported only verbally (p. 6). The regime where it fails —
   strong flow asymmetry (≈5×) and extreme $\gamma$ — is the regime where $p$ is far from 0, i.e. the
   Taylor point is bad. [I] Stage 2a's intensity spikes produce exactly such asymmetry transiently, so
   this failure mode is a warning to test.

### Overlap with Stage 2a

| Element | Verdict | Evidence |
|---|---|---|
| (a) multi-asset matrix Riccati with a stochastic intensity/liquidity factor | **partly** — multi-asset Riccati(-like) yes, stochastic factor **no** | eq. (5), p. 5; amplitudes $\lambda^{n,i,j}(z)$ constant: «$\Lambda^{n,i,j}(z,\delta)=\lambda^{n,i,j}(z)f^{n,i,j}(z,\delta)$» (p. 3) |
| (b) perturbative/asymptotic expansion in that factor | **not** | only expansion is in $p$: «$\check H^{n,i,j}(z,p)=\alpha_0+\alpha_1p+\frac12\alpha_2p^2$» (p. 5) |
| (c) order-1 system linear given order 0 | **not** (no factor expansion). Only the generic analogue: $B$-ODE linear in $B$ given $A$ (eq. 5, p. 5) | — |
| (d) explicit small parameter + error order | **not** | «a natural choice is of course» (p. 5); «$\mathcal H^{i,j}$ is typically flat around 0» (p. 5) |
| (e) accuracy test against exact/numerical solution | **partly** — $d=2$ grid benchmark, qualitative only | «we have validated, when $d=2$, our approximations against the optimal strategy computed thanks to the solution of Eq. (1) approximated with a monotone implicit Euler scheme on an inventory grid» (p. 6) |
| (f) cross-asset coupling of the factor | **not** — coupling is via $\Sigma$ and cross pairs in $M$, not via intensities | «positive correlation leads to a protective pricing strategy for EURUSD» (p. 7) |

**Verdict:** this paper does **not** pre-empt Stage 2a. It is a deterministic-intensity BEGV
transfer to FX with a new state variable. It should be cited as (i) a further instance of the
quadratic-Hamiltonian closure at scale (5 currencies, 10 pairs, 2 tiers, 5 sizes), (ii) a precedent
for a Riccati with a Hadamard term, and (iii) a precedent for dropping hedging Hamiltonians at order
0.

### Direct quotes (for the draft)

> "the techniques proposed in [4] can be adapted so that approximations of the optimal strategies can be obtained by solving a low-dimensional matrix Riccati-like differential equation (the dimensionality of the differential equations to solve only grows quadratically with the number of currencies, hence linearly with the maximal number of currency pairs)." (p. 2)

> "The structure of the problem leads us to approximate the Hamiltonian terms associated with $\mathcal H^{i,j}$ by 0 since $\mathcal H^{i,j}$ is typically flat around 0 when $\psi^{i,j}>0$." (p. 5)

> "The ODE system (5) involves a matrix Riccati-like differential equation whose solution can be approximated very easily using an Euler scheme (i.e. without suffering from the curse of dimensionality, unlike when using an inventory grid as in the case of the original Hamilton-Jacobi-Bellman equation)." (p. 6)

> "Only under extreme conditions which are not practically relevant, such as strong order flow asymmetry (as high as fivefold) and very high or very low risk aversion, have we detected significant deviations." (p. 6)

### Examples & illustrations (for later drafting)

- Eq. (5) vs BEGV's $A'=2AD_+A-\frac12\gamma\Sigma$: the extra $\Sigma\odot A$ term shows how a change of
  state variable (USD-valued inventory, geometric prices) alters the Riccati while keeping closure.
- Table 1 (p. 7): realistic FX size ladders and logistic parameters — a ready calibration template for
  a constant-intensity baseline in numerical experiments.
- Fig. 3 (p. 9): the slanted internalization zone as an intuitive picture of cross-asset coupling via
  correlation and redundant instruments.

### Boundary of this focus

The source has no stochastic intensity, no perturbation in a factor, no error order and no numerical
gap figures. Every statement above about Hawkes or Stage 2a is the project's inference.

## Mentioned entities

- Models: [[begv-2021-model]] (ref. [4], method transferred), [[glft-2013-model]] (ref. [10]), [[avellaneda-stoikov-model]] (ref. [1]), [[cartea-jaimungal-ricci-model]] (ref. [7], objective type).
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[shadow-price]] (finite-difference argument of $\bar\delta$ in (2)), [[who-excites-the-flow]], [[hawkes-process]] (absent).
- Other works (bibkeys / not in wiki): `barzykin-2022-algorithmic-market-making` (ref. [2]); `barzykin-2021-market-making-fx` (probably ref. [3], Risk.net 2022 — unverified match — logistic intensity and calibration); Guéant 2016 book, Guéant 2017 (ref. [9], existence of $\bar\delta$); Butz & Oomen 2019 (internalisation); Schrimpf & Sushko 2019 (BIS).

## Connections

- Builds on: [[bergault-2021-closed-form-approximations]] / [[begv-2021-model]] — same reduction, new state variable and pair structure.
- Same Taylor-at-zero closure, deterministic intensities; contrast with [[barzykin-2026-hawkes-driven-otc]], where intensities are stochastic and enter $A$.
- Relevant to [[intensity-forecast]] only negatively: no forecast $m_t$, intensities are constant.
