---
title: "Bergault et al. 2024 — Price-Aware Automated Market Makers: Models Beyond Brownian Prices and Static Liquidity"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: bergault-2024-price-aware-automated
depth: deep
tags: [market-making, amm, defi, hawkes, markov-modulated-poisson, quadratic-hamiltonian-approximation, stochastic-volatility, curse-of-dimensionality, closure-breakdown]
relations:
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "«they do not preclude the use of the quadratic Hamiltonian approximation technique introduced in [7] to approximate value functions» (p. 2); applied in eqs. (7), (15), (23), (31), (42); shown to fail for trade-excited Hawkes liquidity (p. 17)."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "Ref. [7] = Bergault–Evangelista–Guéant–Vieira 2021; «the quadratic Hamiltonian approximation technique introduced in [7]» (p. 2, p. 10) is the reduction used throughout Sections 3–4."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Uses exponential Hawkes for price jumps (Sec. 3.4, p. 11) and for liquidity «impacted by trades themselves» (Sec. 4.2, p. 16), and argues the latter is «inadequate for our stochastic optimal control problems» (p. 17)."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "Only exponential kernels keep the intensity a Markov state variable: «Power law kernels may be more realistic than exponential ones, but they do not lead to Markovian setups» (p. 11, fn. 8)."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "«the resulting Riccati equations are replaced by nonlinear parabolic partial differential equations» (p. 2); with MMPP liquidity the A-equation becomes p² scalar Riccati ODEs coupled through Q, eq. (43), p. 19."
  - target: intensity-forecast
    type: mentions
    confidence: inferred
    because: "The intensity state (λ̄ or the MMPP regime) is either filtered in real time or statistically estimated (p. 12; p. 18 fn. 16); no forecast object m_t(u) is used."
  - target: branching-matrix
    type: mentions
    confidence: inferred
    because: "Scalar branching ratios only (𝔪 per side, p. 16; 𝔫 for price jumps, p. 11): the implied liquidity branching matrix is diag(𝔪, 𝔪), no cross-side or cross-asset entries."
  - target: volterra-riccati
    type: mentions
    confidence: inferred
    because: "Power-law kernels are excluded as non-Markovian (p. 11, fn. 8); the Volterra–Riccati route that handles them is not discussed in the source."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Cited as ref. [21] among inventory-management extensions «(see [2, 4, 8, 12, 14, 15, 19, 21])» (p. 2)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "Cited as ref. [15] in the same list of model enrichments (p. 2)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«Avellaneda and Stoikov's 2008 article [1], which reinvigorated the modeling framework originally introduced by Ho and Stoll» (p. 2)."
---

# Price-Aware Automated Market Makers: Models Beyond Brownian Prices and Static Liquidity

## Bibliographic Details

Bergault, Philippe; Bertucci, Louis; Bouba, David; Guéant, Olivier; Guilbert, Julien. 2024.
*Price-Aware Automated Market Makers: Models Beyond Brownian Prices and Static Liquidity.*
arXiv:2405.03496v3 [q-fin.TR], 18 May 2024. 21 pp. https://arxiv.org/abs/2405.03496

- **Read:** arXiv 2405.03496v3. Page and equation numbers on this page follow that version.
  No published version was found; under the project's preprint policy this preprint is the
  original (B1 core work).
- **Affiliations:** Université Paris Dauphine-PSL (Bergault), Institut Louis Bachelier (Bertucci),
  Swaap Labs (Bouba, Guilbert), Université Paris 1 Panthéon-Sorbonne (Guéant).
- **Funding / interest:** Research Program "Decentralized Finance and Automated Market Makers"
  (Institut Europlace de Finance) in partnership with Swaap Labs. Two authors are Swaap Labs
  staff, an "actor of the DeFi industry" (p. 20).
- **Data:** none. «No data involved in this study.» (p. 20). The paper is purely about modelling
  and numerical method. It has no simulations, no calibration and no performance numbers.

### Notation map (source → project, CLAUDE.md § Notation)

| Source | Meaning in source | Project symbol / remark |
|---|---|---|
| $S_t$ | reference price of currency 1 in currency 0 | $S_t$ |
| $q^1_t - q^1_0$ | reserve of currency 1 relative to its initial value (Hodl) | inventory $q_t$ |
| $Y_t=(q^1_t-q^1_0)S_t$ | "spread to Hodl", inventory **in value** | $q_t S_t$ (value inventory) |
| $X_t$ | accumulated markups | cash-like $X_t$ (markups only, reserves kept apart) |
| $\delta^{0,1}$, $\delta^{1,0}$ | markups on trades where the AMM sells currency 1 resp. currency 0 | $\delta^{a}$ resp. $\delta^{b}$ (for currency 1) |
| $\Lambda^{i,j}(t,z,\delta)=\lambda^{i,j}_t\phi^{i,j}(z)f^{i,j}(z,\delta)$ | intensity kernel; $f$ logistic | GLFT $\Lambda e^{-k\delta}$ with a logistic $f$ in place of the exponential |
| $\lambda^{0,1}_t,\lambda^{1,0}_t$ | height of the demand curve per side (order-flow intensity) | $\lambda_t$ (two components, one per side) |
| $\lambda^{i,j}_\infty$ | Hawkes baseline (Sec. 4.2) | $\mu$ |
| $\kappa$ | Hawkes decay of liquidity (Sec. 4.2) | $\beta$ |
| $\mathfrak m\in(0,1)$ | branching ratio of liquidity (jump $\kappa\mathfrak m$ per trade) | diagonal entries of $K$, $\rho(K)=\mathfrak m$ |
| $\bar\lambda_t$, $\beta$, $\mathfrak n$ | **price-jump** intensity, its decay and endogeneity ratio (Sec. 3.4) | no project analogue (price, not order flow) |
| $H^{i,j}(z,p)$; $\check H^{i,j}=\alpha_0+\alpha_1p+\tfrac12\alpha_2p^2$ | Hamiltonian; its quadratic approximation | $H^{i,s}$; $\alpha_2^{i,j}\leftrightarrow h_2^{i,s}=H''(0)$ |
| $\theta$; $\check\theta=-Ay^2-By-C$ | value function; its quadratic ansatz | $\theta$; $A,B,C$ |
| $\gamma$ | risk-aversion / variance-penalty parameter | $\gamma$ |
| $Q\in M_{p^2}$ | **MMPP rate matrix** (Sec. 4.3) | ⚠ clashes with project $Q$ (inventory bound) |
| $k$ | mean-reversion of the variance/volatility (Sec. 3.2–3.3) | ⚠ clashes with GLFT $k$ |

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction | 1–2 |
| ✓ F1 | 2 General modelling framework (two-currency AMM, intensity kernels, excess PnL vs Hodl, eqs. (1)–(2)) | 3–5 |
| ✓ F1 | 3.1 Introduction (Markovian low-dimensional price models) | 5–6 |
| ✓ F1 | 3.2 Heston–Bates model: HJB (4), markups (5)–(6), quadratic approximation (7)–(10) | 6–8 |
| ✓ F1 | 3.3 Stein–Stein (Schöbel–Zhu) volatility with jumps: (11)–(18) | 8–10 |
| ✓ F1 | 3.4 "A simple Markovian Hawkes framework" for prices: (19)–(26) | 11–13 |
| ✓ F1 | 3.5 Extension to quadratic (Z-)Hawkes processes: (27)–(34) | 13–15 |
| ✓ F1 | 3.6 Conclusion on advanced price dynamics models | 15 |
| ✓ F1 | 4.1 Introduction (varying liquidity) | 16 |
| ✓ F1 | 4.2 Hawkes models for liquidity and the curse of dimensionality: (35)–(38), §4.2.2 | 16–17 |
| ✓ F1 | 4.3 Markov-modulated Poisson processes as a reasonable alternative: (39)–(45) | 17–19 |
| ✓ F1 | Conclusion; acknowledgement; funding; data statement | 19–20 |
| — | References [1]–[29] | 20–21 |

## Kernthesen

### 1. A price-aware AMM can be written as an OTC-style market-making control problem on a two-currency pool (pp. 2–3)

The paper takes the inventory-management line of market making (Ho–Stoll, Avellaneda–Stoikov,
Guéant and co-authors) and transfers it to "price-aware" automated market makers. Unlike constant
function market makers (CFMMs), which «leave price discovery to liquidity takers, including
arbitrageurs, and stay passive in the price formation process, price-aware AMMs utilize current
market estimates to inform their pricing strategies» (p. 2). The AMM quotes around an exogenous
reference price $S_t$ (an off-chain feed or on-chain oracle, fn. 2) plus a markup per trade
size $z$. Trades are two $\mathbb R_+^*$-marked point processes $J^{0,1}$, $J^{1,0}$. Markups go
into a separate account $X_t$, and reserves move as
$dq^1_t=\int \frac{z}{S_t}(J^{1,0}-J^{0,1})(dt,dz)$ (p. 3). The paper extends the
authors' earlier AMM paper (ref. [6], Digital Finance 2023, not in the library), which assumed
log-normal prices and static liquidity (p. 2).

### 2. Liquidity enters only through the multiplicative height $\lambda_t$ of a logistic demand curve (p. 4)

The intensity kernels are
$\zeta^{0,1}_t(dz)=\Lambda^{0,1}(t,z,\delta^{0,1}(t,z))\mathbb 1_{\{q^1_{t-}\ge z/S_t\}}m(dz)$,
with $\Lambda^{i,j}(t,z,\delta)=\lambda^{i,j}_t\,\phi^{i,j}(z)\,f^{i,j}(z,\delta)$. Here
$\phi^{i,j}$ is the trade-size density and
$f^{i,j}(z,\delta)=1/(1+e^{a^{i,j}(z)+b^{i,j}(z)\delta})$ is a logistic, size-dependent markup
sensitivity (p. 4). The factorisation matters for everything later. Because $\lambda^{i,j}_t$
enters linearly, the Hamiltonian factors as $z\lambda^{i,j}\phi^{i,j}(z)H^{i,j}(z,p)$. A stochastic
$\lambda_t$ therefore just multiplies the Hamiltonian, but it becomes a state variable.

### 3. The LP's objective is excess PnL relative to the buy-and-hold ("Hodl") benchmark, eq. (1) (p. 4)

Marking reserves at the reference price and subtracting the value of the initial reserves gives
$\Pi_T=\int_0^T\!\int z\delta^{0,1}J^{0,1}+\int_0^T\!\int z\delta^{1,0}J^{1,0}+\int_0^T(q^1_t-q^1_0)\,dS_t$ (eq. (1), p. 4).
So the LP earns the markups and carries the price risk of the deviation of reserves from their
initial values. Hodl is the right benchmark for price-aware AMMs. Loss-versus-rebalancing is
called «an extreme one due to its assumption of back-to-back trading» (p. 3, fn. 4).

### 4. The variance penalty is replaced by a quadratic-variation penalty to get a time-consistent problem (pp. 4–5)

"Efficient" strategies maximise $\mathbb E[\Pi_T]-\frac\gamma2\mathbb V[\Pi_T]$. But «Traditional
optimization problems of this form are known to suffer from time inconsistency due to the variance
term» (p. 4). The authors argue that «price risk is the dominant factor» (p. 5, citing
`gueant-2017-optimal-market-making` and the Barzykin–Bergault–Guéant FX work). They therefore
replace the variance with the quadratic variation $\int_0^T(q^1_t-q^1_0)^2\,d\langle S\rangle_t$,
which gives the running-penalty objective (2) (p. 5). For the project's objective field this is a
**risk-adjusted expectation** (mean minus a quadratic inventory penalty), not CARA utility.

### 5. Reserve constraints are dropped, which also lowers the dimension (p. 5)

The penalty keeps reserves near their initial values, so «it is justified, following the approach
by [6], to simplify the problem by omitting the indicator functions. This removal of indicator
functions also reduces the dimensionality of the problem, as it decreases the number of state
variables required» (p. 5). In practice requests that would empty one side «can simply be
prohibited» (fn. 5). The inventory is therefore unbounded in the model, so there is no $Q$-grid
on inventory.

### 6. ⭐ Dynamic price models must be Markovian and low-dimensional, or control becomes infeasible (p. 5)

«To effectively integrate a dynamic price model into our optimal control framework and avoid the
curse of dimensionality, it is crucial to employ continuous-time price models that are both
Markovian and low-dimensional» (p. 5). This is the selection criterion for every model in
Section 3. It explains why only exponential Hawkes kernels appear (fn. 8, Kernthese 14) and why
liquidity is later moved to a finite-state Markov chain (Kernthese 22).

### 7. Under Heston–Bates prices the value function lives on $(t,y,\nu)$ with the inventory in value $Y_t$ as the key state (pp. 6–7)

The price is $dS_t=\mu S_tdt+\sqrt{\nu_t}S_tdW^S_t+S_t\int\eta\bar J(dt,d\eta)$ with CIR variance
and compound-Poisson jumps of rate $\bar\lambda$ (p. 6). The trick is to use
$Y_t=(q^1_t-q^1_0)S_t$, so that $(Y_t,\nu_t)$ is Markovian. The penalty becomes
$\frac\gamma2\int(\nu_t+\bar\lambda\bar\eta^2)Y_t^2dt$ with $\bar\eta=(\int\eta^2\zeta(d\eta))^{1/2}$
(eq. (3)). The HJB (4) is a PIDE in $(t,y,\nu)$. It has a cross-derivative term
$\rho\nu y\xi\partial^2_{y\nu}\theta$, a nonlocal jump term
$\bar\lambda\int(\theta(t,y(1+\eta),\nu)-\theta)\zeta(d\eta)$, and the Hamiltonian term
$\int z\lambda^{0,1}\phi^{0,1}(z)H^{0,1}\big(z,\frac{\theta(t,y,\nu)-\theta(t,y-z,\nu)}{z}\big)m(dz)$ + the symmetric term (p. 6).

### 8. Optimal markups are feedback functions of a finite-difference "shadow price" of inventory, eqs. (5)–(6) (p. 7)

With $H^{i,j}(z,p)=\sup_\delta f^{i,j}(z,\delta)(\delta-p)$, the maximiser is unique:
$\bar\delta^{i,j}(z,p)=(f^{i,j})^{-1}(z,-\partial_pH^{i,j}(z,p))$. The optimal markups are
$\delta^{0,1*}(t,z)=\bar\delta^{0,1}\big(z,\frac{\theta(t,Y_{t-},\nu_t)-\theta(t,Y_{t-}-z,\nu_t)}{z}\big)$
and the mirror image (eqs. (5)–(6), p. 7). This feedback structure repeats in every model:
(13)–(14), (21)–(22), (29)–(30), (37)–(38), (40)–(41).

### 9. The full PIDE is solvable by standard finite differences, but correlation makes the grid awkward (p. 7)

«the value function θ cannot be determined in closed form». It can be approximated «using a
finite difference scheme on a rectangular grid, employing classical numerical methods such as
operator splitting, discrete approximation of the integral terms, and an implicit scheme for the
differential terms». When $|\rho|$ is close to 1, «the use of an isotropic 9-point stencil is
recommended» (p. 7).

### 10. ⭐⭐ The BEGV quadratic Hamiltonian approximation survives stochastic volatility and jumps: the Riccati ODE becomes a PDE in the extra factor (pp. 7–8)

The Hamiltonians are replaced by
$\check H^{i,j}(z,p)=\alpha^{i,j}_0(z)+\alpha^{i,j}_1(z)p+\tfrac12\alpha^{i,j}_2(z)p^2$, «A natural
choice» being the Taylor expansion around $p=0$ (p. 7). Then (7) has an exact solution
$\check\theta(t,y,\nu)=-A(t,\nu)y^2-B(t,\nu)y-C(t,\nu)$ (p. 8). Here $A$ solves
$\partial_tA=2A^2\int z(\lambda^{0,1}\phi^{0,1}\alpha^{0,1}_2+\lambda^{1,0}\phi^{1,0}\alpha^{1,0}_2)m(dz)-(2\mu+\nu+\bar\lambda\bar\eta^2)A-(2\rho\nu\xi+k(\bar\nu-\nu))\partial_\nu A-\tfrac12\nu\xi^2\partial^2_{\nu\nu}A-\tfrac\gamma2(\nu+\bar\lambda\bar\eta^2)$,
and $B$ solves a linear PDE driven by $A$ (eq. (8)). Section 1 sums this up: «while these models
necessitate the addition of a state variable, they do not preclude the use of the quadratic
Hamiltonian approximation technique introduced in [7] to approximate value functions. However,
the resulting Riccati equations are replaced by nonlinear parabolic partial differential
equations» (p. 2).

### 11. The approximated system is triangular and loses the cross-derivative (p. 8)

«The PDE system (8) can be solved numerically far more easily than Eq. (4). Indeed, the
dimensionality of the problem has been reduced and there is no more cross derivatives terms,
hence no more geometric problem related to the numerical grid. Furthermore, the system is
triangular» (p. 8). The $A$-equation is «a nonlinear parabolic PDE with one state variable whose
only nonlinear term is of order 0», so an implicit scheme fits. $B$ then solves a linear
parabolic PDE (p. 8).

### 12. Approximate markups are affine in the inventory in value, eqs. (9)–(10) (p. 8)

Substituting $\check\theta$ gives
$\check\delta^{0,1*}(t,z)=\bar\delta^{0,1}\big(z,A(t,\nu_t)(z-2Y_{t-})-B(t,\nu_t)\big)$ and
$\check\delta^{1,0*}(t,z)=\bar\delta^{1,0}\big(z,A(t,\nu_t)(z+2Y_{t-})+B(t,\nu_t)\big)$ (p. 8).
The finite-difference argument $A(z\mp2Y)\mp B$ is **affine** in $Y$, and that is exactly what the
quadratic ansatz needs (see the focus block). The same form recurs as (17)–(18), (25)–(26),
(33)–(34) and (44)–(45), with the coefficient arguments changed.

### 13. A Stein–Stein / Schöbel–Zhu volatility with jumps gives the same structure with $\sigma$ in place of $\nu$ (pp. 8–10)

Here $d\sigma_t=k(\bar\sigma-\sigma_t)dt+\xi dW^\sigma_t$ (OU volatility, arbitrary correlation
$\rho$) plus compound-Poisson price jumps (p. 8). The state $(Y_t,\sigma_t)$ is Markovian, the HJB
(12) mirrors (4), and «the quadratic Hamiltonian approximation technique introduced in [7] is
applicable» (p. 10). The result is the triangular PDE system (16) in $(t,\sigma)$ and markups
(17)–(18). Volatility (like variance) is not directly observable and must be estimated (p. 10).

### 14. ⭐ A pure-jump price with exponential-Hawkes jump intensity keeps $(Y_t,\bar\lambda_t)$ Markovian; power-law kernels are excluded (p. 11)

The price is $dS_t=S_t\int\eta\bar J(dt,d\eta)$ with intensity $\bar\lambda_t\zeta(d\eta)$ and
$d\bar\lambda_t=-\beta(\bar\lambda_t-\bar\lambda_\infty)dt+\beta\mathfrak n\int\bar J(dt,d\eta)$.
Here $\mathfrak n\in(0,1)$ is «the percentage of price moves that are purely endogenous» (p. 11).
Such microstructure models «can more effectively capture certain stylized facts, like time
reversal asymmetries, compared to traditional stochastic volatility models» (p. 11). The kernel
choice is forced by Markovianity: «Power law kernels may be more realistic than exponential ones,
but they do not lead to Markovian setups» (p. 11, fn. 8). The penalty is
$\frac\gamma2\int\bar\lambda_t\bar\eta^2Y_t^2dt$ (eq. (19)). The HJB (20) carries the nonlocal
term $\bar\lambda\int(\theta(t,y(1+\eta),\bar\lambda+\beta\mathfrak n)-\theta(t,y,\bar\lambda))\zeta(d\eta)$
(p. 11). **In this model the exciting events are price jumps, not trades with the AMM.**

### 15. The Hawkes intensity can be treated as observed (filtered) or as estimated (p. 12)

«The first approach starts with an initial value $\bar\lambda_0$ (whose influence diminishes over
time) and treats $\bar\lambda$ as an observable variable that evolves in real-time with market
dynamics. The second approach uses statistical methods to estimate the current value of
$\bar\lambda$ based on recent historical price data», as with instantaneous volatility (p. 12).
For the quadratic-Hawkes drivers $h,\xi$ the same holds (p. 14, fn. 11).

### 16. ⭐⭐ For Hawkes prices the quadratic approximation still closes, with nonlocal shifts in $\bar\lambda$ (pp. 12–13)

«to reduce the dimensionality of equations by 1, one can again use the quadratic Hamiltonian
approximation technique, although it leads to more complex equations than in the case of
stochastic volatility models because of the nonlocal term in $\bar\lambda$» (p. 12). Eq. (23) has
the solution $\check\theta=-A(t,\bar\lambda)y^2-B(t,\bar\lambda)y-C(t,\bar\lambda)$, with
$\partial_tA=2A^2\int z(\dots)\alpha_2\,m(dz)-\tfrac\gamma2\bar\lambda\bar\eta^2+\beta(\bar\lambda-\bar\lambda_\infty)\partial_{\bar\lambda}A-\bar\lambda\big(A(t,\bar\lambda+\beta\mathfrak n)(1+\bar\eta^2)-A(t,\bar\lambda)\big)$
(eq. (24), p. 12). This is a delay/shift-type PDE in one variable, «triangular … with nonlocal
terms», solvable by an implicit scheme (p. 13). Markups (25)–(26).

### 17. A quadratic (Zumbach) Hawkes price needs two intensity drivers, which leaves a two-dimensional nonlocal PDE even after approximation (pp. 13–15)

Following Blanc–Donier–Bouchaud's Z-Hawkes (ref. [10], not in the library), the intensity is
$\bar\lambda_t=\bar\lambda_\infty+h_t+\xi_t^2$ with
$dh_t=-\kappa h_tdt+\kappa\mathfrak n_H\int\bar J$ and
$d\xi_t=-\omega\xi_tdt+\sqrt{2\mathfrak n_Z\omega}\int\mathrm{sign}(\eta)\bar J$,
$\mathfrak n_H+\mathfrak n_Z<1$ (p. 13). It contains Section 3.4 as the case $\xi_0=\omega=0$
(fn. 10). The state $(Y,h,\xi)$ gives the HJB (28). «Due to its high dimensionality, this equation
poses significant challenges for numerical solutions» (p. 14). The quadratic approximation removes
$y$ but leaves the PDE system (32) in $(t,h,\xi)$, with sign-dependent shifts
$\xi\pm\sqrt{2\mathfrak n_Z\omega}$. Markups (33)–(34).

### 18. ⭐ Summary of Section 3: three models reduce to one spatial dimension, quadratic Hawkes does not (p. 15)

«Once the quadratic Hamiltonian approximation technique is applied, for the first three models,
these PDEs involve time and one spatial dimension, enabling the use of fast numerical methods.
However, this task becomes more complex with models such as the quadratic Hawkes model, which
presents greater computational challenges to be used in practice» (p. 15).

### 19. The model should be chosen per pair, trading realism against computational cost (p. 15)

«pools involving a stablecoin and a major cryptocurrency might utilize a different model than pools
for two independent cryptocurrencies, or pairs of cryptocurrencies that are highly correlated due
to shared risk factors» (p. 15). «For each cryptocurrency pair, there is a significant trade-off
between the simplicity of the model and its capacity to realistically capture market dynamics»,
which affects computational efficiency and risk management (p. 15). Every pool is still modelled
on its own. There is no joint model across pools.

### 20. Stochastic liquidity has been "largely overlooked" in market making (p. 16)

«In most academic papers on market making, liquidity at the bid and the offer is assumed to be
constant. However, this simplification can be detrimental when fluctuations in liquidity are
significant» (p. 16). There are periods of high and low liquidity and times when one side
dominates. The named exceptions are the MRR model on trade-sign autocorrelation (ref. [11],
Bouchaud et al. book) and `bergault-2023-liquidity-dynamics-rfq` (ref. [9]), which uses an MMPP
(p. 16). Deterministic intraday liquidity patterns «can be incorporated without increasing modeling
complexity» (p. 16, fn. 12).

### 21. ⭐⭐ Hawkes liquidity excited by the AMM's own trades makes the problem three-dimensional (or more), eqs. (35)–(38) (pp. 16–17)

«it is natural to assume that $(\lambda^{0,1}_t)$ and $(\lambda^{1,0}_t)$ are stochastic processes
impacted by trades themselves» (p. 16):
$d\lambda^{0,1}_t=-\kappa(\lambda^{0,1}_t-\lambda^{0,1}_\infty)dt+\kappa\mathfrak m\int J^{0,1}(dt,dz)$
and likewise for $\lambda^{1,0}$ with $J^{1,0}$, where $\kappa>0$ and $0<\mathfrak m<1$. Each side
is **self-exciting only**: there is no cross-side term. The jump size $\kappa\mathfrak m$ does not
depend on the trade size $z$. With GBM prices, $(Y_t,\lambda^{0,1}_t,\lambda^{1,0}_t)$ is Markovian,
and the HJB (36) is a PIDE in $(t,y,\lambda^{0,1},\lambda^{1,0})$. In it **the intensity shift sits
inside the Hamiltonian argument**:
$H^{0,1}\big(z,\frac{\theta(t,y,\lambda^{0,1},\lambda^{1,0})-\theta(t,y-z,\lambda^{0,1}+\kappa\mathfrak m,\lambda^{1,0})}{z}\big)$
(p. 17). Footnote 13: «More complex settings can be considered but they all suffer from the curse
of dimensionality» (p. 16).

### 22. ⭐⭐ The quadratic Hamiltonian approximation cannot remove the dimension under trade-excited Hawkes liquidity (p. 17)

«In the basic geometric Brownian setting for prices, solving the optimal stochastic control
problems (35) necessitates a value function with time and three state variables. Incorporating the
models from Section 3 would increase the number of state variables to four or even five» (p. 17).
«Moreover, the situation becomes even more critical as the quadratic Hamiltonian approximation
technique, often utilized in Section 3, does not provide a means to reduce this dimensionality.
This limitation arises because assuming the value function to be quadratic in y does not result in
linear terms in y when computing finite differences in the Hamiltonian terms, due to simultaneous
jumps in both the y variable and the intensity variables» (p. 17). Verdict: «While liquidity models
based on Hawkes processes may offer a good statistical representation, they prove inadequate for
our stochastic optimal control problems» (p. 17). See the focus block for the step-by-step
reconstruction.

### 23. ⭐⭐ Markov-modulated Poisson liquidity separates intensity changes from trades and restores tractability (pp. 17–18)

«The main challenge with the liquidity model based on Hawkes processes is the simultaneity of
trades and changes in intensities. To disentangle these two aspects and thus circumvent the curse
of dimensionality, we can adopt a framework involving Markov-modulated Poisson processes» (p. 17).
$(\lambda^{0,1}_t,\lambda^{1,0}_t)$ is a continuous-time Markov chain on
$\{\lambda_1,\dots,\lambda_p\}^2$ with «p is small, typically 2 or 3, to represent low, high, and
possibly medium levels of liquidity», and rate matrix $Q\in M_{p^2}$ (p. 17). The HJB (39) couples
the $p^2$ regimes **linearly** through
$\sum_{k^{0,1},k^{1,0}}Q_{(j^{0,1}-1)p+j^{1,0},(k^{0,1}-1)p+k^{1,0}}\theta(t,y,\lambda_{k^{0,1}},\lambda_{k^{1,0}})$.
The Hamiltonian differences are taken **within** the current regime (p. 18). «Notably, there are no
partial derivative terms with respect to the intensities. Consequently, Eq. (39) should be regarded
as a system of partial integro-differential equations in two dimensions: time and the spread to
Hodl (y)» (p. 18). It can be solved by operator splitting on $p^2$ rectangular grids. One «could
even consider extending the price model using those discussed in Section 3» (p. 18).

### 24. ⭐⭐ With MMPP liquidity and log-normal prices the quadratic approximation yields ODEs: $p^2$ coupled Riccati equations, eq. (43) (pp. 18–19)

«Interestingly, the quadratic Hamiltonian approximation technique works very well here and it leads
to a system of ODEs when prices are log-normal (we would obtain PDEs with the price models of
Section 3)» (p. 18). For each regime $(j^{0,1},j^{1,0})$:
$\partial_tA(t,j)=2A(t,j)^2\int z\big(\lambda_{j^{0,1}}\phi^{0,1}\alpha^{0,1}_2+\lambda_{j^{1,0}}\phi^{1,0}\alpha^{1,0}_2\big)m(dz)-\tfrac\gamma2\sigma^2-\sum_kQ_{j,k}A(t,k)$,
and $B$ is linear with the same $Q$-coupling (eq. (43), p. 19). «The system of ODEs (43) can be
solved straightforwardly» (p. 19). The markups (44)–(45) have the affine form of Kernthese 12, with
$A,B$ evaluated at the current regime. The current regime must be estimated, by the techniques of
`bergault-2023-liquidity-dynamics-rfq` (fn. 16, p. 18).

### 25. Conclusion: sophistication costs computation, and the choice is left to AMM developers (pp. 19–20)

«the adoption of these sophisticated models brings challenges, particularly in terms of higher
computational costs, which must be considered as they can restrict practical application» (p. 19).
Developers «must balance the benefits of detailed, complex modeling against computational
efficiency and the operational constraints of their systems» (p. 20). The paper gives a menu of
HJB formulations, not a numerical comparison.

## Figures and tables

None. The paper has no figures, tables or numerical experiments; its content is equations
(1)–(45).

## What this source does not address

- **No numerics or benchmarks.** No implemented solver, no simulated PnL, no comparison of
  approximate against exact markups, no regret/gap numbers («No data involved in this study», p. 20).
  The size of the quadratic-approximation error under Hawkes prices or MMPP liquidity is not
  measured. Error analysis of the BEGV approximation belongs to [[begv-2021-model]].
- **No multi-asset model.** One two-currency pool. Multi-asset market making is cited only
  (BEGV, `barzykin-2022-multi-currency-inventory`, `bergault-2020-size-matters-otc`,
  `gueant-2017-optimal-market-making`, `gueant-2019-deep-reinforcement-learning`, p. 2), and
  `rosenbaum-2022-multi-asset-market` is cited for stochastic volatility (p. 2). There is no
  cross-asset excitation. Cross-asset Hawkes networks are the subject of
  [[acero-2026-hawkes-structured-networks]].
- **No cross-side excitation.** The Hawkes liquidity in Sec. 4.2 is diagonal (each side excites
  only itself). Cross-side dependence appears only implicitly, through the joint MMPP generator $Q$.
- **No treatment of trade-excited Hawkes flow beyond "it breaks".** There are no approximations
  for the Sec. 4.2 model (no Markov/Volterra lift, no intensity forecast, no perturbation in
  $\mathfrak m$, no neural or RL solver). Approaches that do solve it:
  [[barzykin-2026-hawkes-driven-otc]] (Volterra–Riccati) and [[martin-2026-market-making-hawkes]]
  (Mercer-expansion Markov approximation). `jusselin-2021-persistent-order-flow` is cited for
  Hawkes liquidity (p. 2) but not used.
- **No non-exponential kernels** (fn. 8). **No adverse selection or informed flow**: price and flow
  are independent. **No CARA utility**: the objective is a quadratic-variation penalty.
- **No AMM-specific constraints in the solved problems**: nonnegative reserves are dropped (p. 5).

## Model card

Common to all models: **objective** = risk-adjusted expected excess PnL vs Hodl,
$\mathbb E[\text{markups}+\int(q^1-q^1_0)dS-\tfrac\gamma2\int(q^1-q^1_0)^2d\langle S\rangle]$, eq. (2)
(a quadratic-variation proxy for mean–variance, not CARA). **Benchmark** = the Hodl portfolio as a
PnL reference. There is no benchmark *strategy* (exact vs approximate, RL, etc.) — n/a, no
numerics. **Reported regret/gap numbers** = n/a, no numerical results (p. 20). **Assets** = one
currency pair (two-currency pool) in every model. Intensities are logistic in the markup and
size-dependent, $\Lambda=\lambda_t\phi(z)f(z,\delta)$.

| Model (Sec.) | Kernel of order flow | Excitation | Who excites | State of $\theta$ | Exact method | After quadratic approx. ($\check\theta=-Ay^2-By-C$) |
|---|---|---|---|---|---|---|
| Heston–Bates price (3.2) | Poisson, constant $\lambda^{i,j}$ | none in flow (price jumps compound Poisson) | n/a — flow not excited | $(t,y,\nu)$ | FD PIDE (4), operator splitting, 9-point stencil | closes: triangular PDE in $(t,\nu)$, eq. (8) |
| Stein–Stein–Schöbel–Zhu + jumps (3.3) | Poisson, constant | none in flow | n/a | $(t,y,\sigma)$ | FD PIDE (12) | closes: PDE in $(t,\sigma)$, eq. (16) |
| Hawkes price (3.4) | Poisson flow; **price jumps** exponential Hawkes, ratio $\mathfrak n$ | self (price jumps → price-jump intensity) | market price jumps (exogenous to the AMM) | $(t,y,\bar\lambda)$ | PIDE (20) | closes: nonlocal PDE in $(t,\bar\lambda)$, eq. (24) |
| Quadratic (Z-)Hawkes price (3.5) | Poisson flow; price jumps quadratic Hawkes ($h,\xi$) | self + Zumbach (sign-dependent) on price jumps | market price jumps | $(t,y,h,\xi)$ | PIDE (28), "significant challenges" | closes but 2-D nonlocal PDE in $(t,h,\xi)$, eq. (32) |
| **Hawkes liquidity (4.2)** | **exponential Hawkes**, decay $\kappa$, branching $\mathfrak m$, jump $\kappa\mathfrak m$ | **self only** per side (no cross-side, no cross-asset) | **the AMM's own fills** ($J^{0,1}$, $J^{1,0}$) | $(t,y,\lambda^{0,1},\lambda^{1,0})$; 4–5 states with Sec. 3 prices | high-dim PIDE (36), no method proposed | **breaks**: ansatz not closed (p. 17) |
| **MMPP liquidity (4.3)** | Markov-modulated Poisson, $p^2$ regimes, generator $Q$ | regime switching (cross-side via joint $Q$); not excited by trades | n/a — exogenous chain | $(t,y)\times p^2$ regimes | $p^2$ coupled PIDEs (39) on $p^2$ grids | closes: $p^2$ coupled Riccati ODEs (A) + linear ODEs (B), eq. (43); PDEs with Sec. 3 prices |

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 6, 10, 12, 14, 16, 18, 21, 22, 23, 24** (with 4 and 19 as context).

### What this focus needs beyond the Kernthesen

1. **Step-by-step reconstruction of why closure breaks (Sec. 4.2.2, p. 17).** This is reconstructed
   from eqs. (36), (42)–(45). The source states only the conclusion (Kernthese 22).
   - *(i) Ansatz.* Take $\check\theta(t,y,\lambda)=-A(t,\lambda)y^2-B(t,\lambda)y-C(t,\lambda)$ with
     $\lambda=(\lambda^{0,1},\lambda^{1,0})$, as in Secs. 3–4.3.
   - *(ii) The Hamiltonian argument in (36).* A fill on the $0,1$ side moves $y\to y-z$ **and**
     $\lambda^{0,1}\to\lambda^{0,1}+\kappa\mathfrak m$ in the same instant. So
     $p^{0,1}=\frac1z\big[\check\theta(t,y,\lambda)-\check\theta(t,y-z,\lambda^+)\big]$ with
     $\lambda^+=\lambda+\kappa\mathfrak m e_1$. Write $A^+=A(t,\lambda^+)$, etc.
   - *(iii) Expansion.* $z\,p^{0,1}=(A^+-A)\,y^2+(B^+-B-2zA^+)\,y+(z^2A^+-zB^++C^+-C)$.
   - *(iv) Without the simultaneous intensity jump* ($\lambda^+=\lambda$, as in Secs. 3.2–3.4 and
     inside each regime of 4.3), $A^+=A$, $B^+=B$, so $p^{0,1}=A(z-2y)-B$. That is **affine in
     $y$**, exactly the argument of (9), (25), (44). Then
     $\check H(p)=\alpha_0+\alpha_1p+\tfrac12\alpha_2p^2$ is quadratic in $y$. Every other HJB term
     is at most quadratic in $y$. Matching the coefficients of $y^2,y^1,y^0$ gives closed equations
     for $A,B,C$ (the Riccati structure).
   - *(v) With the jump*, $p^{0,1}$ contains $\frac{A^+-A}{z}y^2$. The curvature term
     $\tfrac12\alpha_2p^2$ then produces $\frac{\alpha_2}{2z^2}(A^+-A)^2y^4$ and $y^3$ terms. Nothing
     else in the HJB can balance them, so the quadratic ansatz is not a solution of the
     approximated HJB. The only escape is $A(t,\lambda^+)=A(t,\lambda)$, i.e. $A$ independent of
     $\lambda$. But the $A$-equation contains $\lambda^{0,1}\alpha_2^{0,1}$ in its Riccati
     coefficient, so $A$ must depend on $\lambda$. This is what the paper means by «does not
     result in linear terms in y when computing finite differences in the Hamiltonian terms»
     (p. 17).
   - *(vi) Why Hawkes **prices** (3.4) escape.* There the intensity jump $\bar\lambda\to\bar\lambda+\beta\mathfrak n$
     happens in the **linear** nonlocal term
     $\bar\lambda\int(\check\theta(t,y(1+\eta),\bar\lambda+\beta\mathfrak n)-\check\theta(t,y,\bar\lambda))\zeta(d\eta)$,
     which maps $y^2\mapsto(1+\eta)^2y^2$, so it stays quadratic. In the Hamiltonian argument the
     intensity is unchanged, because trades do not excite price jumps. Why **MMPP** (4.3) escapes:
     intensity changes enter only via the linear $\sum_kQ_{j,k}\check\theta(t,y,k)$, and the
     Hamiltonian difference is taken at a fixed regime.
   - *(vii) Diagnosis.* Closure needs (a) the intensity jump not to coincide with the inventory jump
     **inside the nonlinear Hamiltonian**, and (b) non-zero curvature $\alpha_2$ is what makes a
     coincidence fatal. The paper names only (a), as «simultaneity of trades and changes in
     intensities» (p. 17).
2. **Inference, not in the source.** Two corollaries follow from step (v) for the project. First,
   with a *linearised* Hamiltonian ($\alpha_2=0$) the $y^2$-term from $A^+-A$ would be harmless and
   the ansatz would close, but the optimal quotes would no longer depend on inventory through the
   curvature. Second, if the exciting events were **all market orders** (exogenous to the maker's
   quotes) rather than **the maker's own fills**, the intensity jump would sit in a linear
   compensator term, as in 3.4, and quadratic closure would survive. The obstruction is therefore
   specifically "fills excite flow". Barzykin 2026's Volterra–Riccati is the obvious comparison
   ([[barzykin-2026-hawkes-driven-otc]]).
3. **Which models keep a Riccati/ODE structure (Kernthesen 10, 16, 18, 24).** True ODEs (Riccati in
   $A$, linear in $B$) appear only for MMPP liquidity with log-normal prices, eq. (43). SV and Hawkes
   prices give Riccati-type PDEs in one extra variable ((8), (16), (24)). Quadratic Hawkes gives a
   2-D nonlocal PDE (32). Trade-excited Hawkes liquidity gives no reduction: a full 3-D PIDE (36),
   4–5-D with Sec. 3 prices (p. 17).
4. **Why MMPP and not Hawkes (Kernthese 23).** The argument is structural (disentangle trades from
   intensity changes), not statistical. The authors concede Hawkes «may offer a good statistical
   representation» (p. 17). The MMPP *chain* can still carry dependence between bid and ask
   liquidity through the joint $p^2\times p^2$ generator $Q$. That is the only cross-side channel in
   the paper.
5. **Several assets (inference; the source has one pair).** The source says nothing about several
   pairs beyond fitting a model per pool (p. 15). Carrying the MMPP route to $d$ assets with BEGV's
   matrix $A$ would give one **matrix** Riccati ODE per regime, coupled linearly by $Q$. But the
   regime count grows like $p^{2d}$ if every side of every asset has its own level, so the curse of
   dimensionality moves into the regime space. Cross-asset *excitation* (fills on asset $i$ raising
   intensity on asset $j$) would bring back the simultaneity of step (ii) across assets. Under
   step (v) it would break the multi-asset quadratic ansatz in the same way (inferred).

### Direct quotes (for the draft)

> "Moreover, the situation becomes even more critical as the quadratic Hamiltonian approximation
> technique, often utilized in Section 3, does not provide a means to reduce this dimensionality.
> This limitation arises because assuming the value function to be quadratic in y does not result
> in linear terms in y when computing finite differences in the Hamiltonian terms, due to
> simultaneous jumps in both the y variable and the intensity variables." (p. 17)

> "The main challenge with the liquidity model based on Hawkes processes is the simultaneity of
> trades and changes in intensities. To disentangle these two aspects and thus circumvent the curse
> of dimensionality, we can adopt a framework involving Markov-modulated Poisson processes, as
> proposed in [9]." (p. 17)

> "However, employing Hawkes processes presents a challenge as it conflicts with the quadratic
> Hamiltonian approximation technique, which reduces computational complexity. As an alternative,
> we propose Markov-modulated Poisson processes (MMPPs), as explored in the recent paper [9]." (p. 2)

> "Interestingly, the quadratic Hamiltonian approximation technique works very well here and it
> leads to a system of ODEs when prices are log-normal (we would obtain PDEs with the price models
> of Section 3)." (p. 18)

> "Notably, there are no partial derivative terms with respect to the intensities. Consequently,
> Eq. (39) should be regarded as a system of partial integro-differential equations in two
> dimensions: time and the spread to Hodl (y)." (p. 18)

### Examples & illustrations (for later drafting)

- Dimension count for trade-excited Hawkes liquidity: time + 3 states with GBM, «four or even five»
  with the Section 3 price models (p. 17). This is a concrete figure for "how fast it blows up".
- MMPP regime grid: $p=2$ or $3$ levels per side, so 4 or 9 joint regimes. The states are ordered
  lexicographically $(\lambda_1,\lambda_1),\dots,(\lambda_p,\lambda_p)$ (p. 17, fn. 15). This is a
  worked example of a finite-state "lift" replacing a continuous intensity.
- Pair-dependent model choice: stablecoin/major vs. two independent cryptocurrencies vs. highly
  correlated pairs (p. 15). This is the paper's only nod to several assets.

### Boundary of this focus

The paper diagnoses the closure failure but does not quantify it. It gives no numerical comparison
between the exact PIDE (36) and any approximation, so it cannot say *how wrong* a Poisson or MMPP
proxy is under true Hawkes flow. It has no cross-side Hawkes term, no cross-asset excitation and no
lift or forecast technique. For those see [[barzykin-2026-hawkes-driven-otc]],
[[martin-2026-market-making-hawkes]] and [[acero-2026-hawkes-structured-networks]].

## Mentioned entities

- Models: [[begv-2021-model]], [[glft-2013-model]], [[avellaneda-stoikov-model]],
  [[cartea-jaimungal-ricci-model]]
- Concepts: [[hamiltonian-quadratic-approximation]], [[hawkes-process]], [[matrix-riccati-equation]],
  [[markov-lift]], [[branching-matrix]], [[intensity-forecast]], [[volterra-riccati]]
- Not yet pages (prose only): Markov-modulated Poisson process; Heston–Bates; Stein–Stein /
  Schöbel–Zhu; quadratic (Z-)Hawkes (Blanc–Donier–Bouchaud 2017); Hodl benchmark; price-aware AMM;
  loss-versus-rebalancing.

## Connections

- **Builds on** [[begv-2021-model]] / [[hamiltonian-quadratic-approximation]]: it extends the
  quadratic-Hamiltonian reduction from Brownian prices to SV, jumps, Hawkes prices and MMPP
  liquidity, and identifies where it fails (trade-excited Hawkes liquidity, p. 17).
- **Builds on** `bergault-2023-liquidity-dynamics-rfq` (ref. [9]) for the MMPP liquidity model and
  its estimation (pp. 16–18, fn. 16).
- **Builds on** [[matrix-riccati-equation]]: the scalar Riccati ODE of the Brownian case becomes a
  Riccati PDE (SV/Hawkes price) or $p^2$ $Q$-coupled Riccati ODEs (MMPP).
- **Supports** [[markov-lift]]: only exponential kernels keep a Markov state (fn. 8, p. 11).
- **Supplemented by (inferred)** [[barzykin-2026-hawkes-driven-otc]] and
  [[martin-2026-market-making-hawkes]], which tackle exactly the trade-excited Hawkes control
  problem this paper declares intractable. Their solutions should be checked against the
  closure-failure argument reconstructed above.
- **Contrast (inferred)** [[acero-2026-hawkes-structured-networks]]: cross-asset Hawkes structure,
  which this single-pair paper does not touch.
- **Cites** [[glft-2013-model]] (ref. [21]), [[cartea-jaimungal-ricci-model]] (ref. [15]),
  [[avellaneda-stoikov-model]] (ref. [1]), `gueant-2017-optimal-market-making` (ref. [20], source of
  the $\bar\delta=(f)^{-1}(-\partial_pH)$ result), `bergault-2020-size-matters-otc` (ref. [8]),
  `drissi-2022-solvability-differential-riccati` (ref. [17]), `rosenbaum-2022-multi-asset-market`
  (ref. [27]), `jusselin-2021-persistent-order-flow` (ref. [25]),
  `barzykin-2022-algorithmic-market-making` (ref. [2]), `barzykin-2022-multi-currency-inventory`
  (ref. [3]), `gueant-2019-deep-reinforcement-learning` (ref. [22]),
  `cartea-2015-algorithmic-high-frequency` (ref. [14]).
