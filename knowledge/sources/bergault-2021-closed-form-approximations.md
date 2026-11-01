---
title: "Bergault, Evangelista, Guéant, Vieira 2021 — Closed-form Approximations in Multi-asset Market Making"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: bergault-2021-closed-form-approximations
depth: deep
tags: [market-making, multi-asset, closed-form, hamiltonian-approximation, riccati, ergodic, otc, rfq, poisson, greedy-policy]
relations:
  - target: begv-2021-model
    type: supports
    confidence: extracted
    because: "This is the paper that defines the model: «we propose closed-form approximations for the value functions of many multi-asset extensions of the Avellaneda–Stoikov model» (abstract, p. 101); Props 1–6 (pp. 110–128)."
  - target: hamiltonian-quadratic-approximation
    type: supports
    confidence: extracted
    because: "«The main idea of this paper consists in replacing the Hamiltonian functions associated with our market making problem by quadratic functions that approximate them» (p. 109); Taylor at p = 0 is «A natural choice» (Remark 1, p. 109)."
  - target: matrix-riccati-equation
    type: supports
    confidence: extracted
    because: "Prop. 1–2 (pp. 110–113): A' = 2A D_+ A − ½γΣ, solved by a tanh formula (13); «can be simplified into a Riccati equation and two linear ordinary differential equations, all solvable in closed form» (p. 138)."
  - target: shadow-price
    type: supports
    confidence: inferred
    because: "Quotes are δ̃(p) evaluated at the finite difference p = (θ(t,q) − θ(t,q ± z^i e^i))/z^i (Thms 1–2, eqs. 7–8, p. 108); the paper never uses the term 'shadow price'."
  - target: glft-2013-model
    type: builds-on
    confidence: extracted
    because: "For d = 1, Model A, unit size, the quotes «coincide with the affine closed-form approximations obtained in the paper (Guéant, Lehalle, and Fernandez-Tapia 2013)», obtained «in a fundamentally different manner» (p. 118)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "«A large proportion of market making models derive from the seminal model of Avellaneda and Stoikov» (abstract, p. 101); Model A uses the Avellaneda–Stoikov CARA objective (p. 105)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "Model B: «as proposed by Cartea et al. in (Cartea, Jaimungal, and Ricci 2014), we can consider a risk-adjusted expectation for the objective function» (p. 105); CJR 2014/2018 also cited for alpha signals and ambiguity aversion (p. 101)."
  - target: hawkes-process
    type: mentions
    confidence: inferred
    because: "The word 'Hawkes' never occurs. Self-exciting flow enters only through citations: «persistence of the order flow in (Jusselin 2020)» (p. 102) and CJR 2018 «Mutually Exciting Processes» (reference list, p. 140). All intensities in the model are deterministic functions of the quote (p. 104)."
---

# Closed-form Approximations in Multi-asset Market Making

## Bibliographic Details

Bergault, Philippe, David Evangelista, Olivier Guéant, and Douglas Vieira. 2021. "Closed-form
Approximations in Multi-asset Market Making." *Applied Mathematical Finance* 28 (2): 101–142.
https://doi.org/10.1080/1350486X.2021.1949359. Received 5 Sep 2020, accepted 24 Jun 2021,
published online 10 Mar 2022. Affiliations: Paris 1 Panthéon-Sorbonne (Bergault, Guéant), FGV Rio
(Evangelista), Imperial College London (Vieira).

**Read:** the published journal version (`library/pdf/bergault-2021-closed-form-approximations.pdf`,
43 PDF pages), full text including notes, references and Appendix A. **All page numbers on this page
are the journal's printed pages 101–142.** PDF p. 1 is a Taylor & Francis cover sheet; journal
page $n$ = PDF page $n-99$. Equation numbers are the journal's. The arXiv preprint (1810.04383v5,
`library/preprints/`) was not read.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $d$, $S^i_t$, $\sigma^i$, $\rho^{i,j}$, $\Sigma$ | assets, mid price (arithmetic BM), vol, correlation, covariance (p. 104) | same |
| $\mu^i$, $\mu$ | **price drift** (Sec. 5, p. 121) | ⚠ clashes with Hawkes baseline $\mu$ |
| $q^i_t$, $Q^i$, $z^i$, $X_t$ | inventory, risk limit, trade size, cash | $q_t$, $Q$, $z$, $X_t$ |
| $\delta^{i,b}_t,\delta^{i,a}_t$ | bid/ask distance to mid (p. 105) | $\delta^b,\delta^a$ |
| $\Lambda^{i,b}(\delta)$, $\Lambda^{i,a}(\delta)$ | intensity **function of the quote** (p. 104) | GLFT $\Lambda e^{-k\delta}$; arrival rate × fill probability $f(\delta)$ |
| $\lambda^{i,b}_t=\Lambda^{i,b}(\delta^{i,b}_t)\mathbb 1_{\{\dots\}}$ | realized fill intensity (p. 104) | ⚠ **not** a Hawkes $\lambda_t$: no memory, no state |
| $A^i$, $k^i$ | exponential intensity $A^ie^{-k^i\delta}$ (p. 118) | $\Lambda$, $k$; ⚠ $A^i$ clashes with the matrix $A(t)$ |
| $\lambda_{RFQ}$, $\alpha_\Lambda$, $\beta_\Lambda$ | logistic intensity $\lambda_{RFQ}/(1+e^{\alpha_\Lambda+\beta_\Lambda\delta})$ (p. 131) | $\lambda_{RFQ}$ = constant arrival rate; ⚠ $\beta_\Lambda$ ≠ Hawkes decay $\beta$ |
| $\xi$ | $\xi=\gamma$ (Model A, CARA), $\xi=0$ (Model B) (p. 107) | — |
| $H^{i,b}_\xi$, $H^{i,a}_\xi$ | Hamiltonians (3)–(4) | $H^{i,s}$ |
| $\alpha^{i,b}_0,\alpha^{i,b}_1,\alpha^{i,b}_2$ | coefficients of the quadratic $\breve H^{i,b}$; Taylor: $\alpha_j=H^{(j)}_\xi(0)$ (p. 109) | $h_0,h_1,h_2$; $h_2^{i,s}=H''(0)$ |
| $\theta(t,q)$, $\breve\theta(t,q)$ | reduced value function, its quadratic proxy (pp. 107, 109) | $\theta(t,q,\lambda)$ with no $\lambda$ |
| $A(t),B(t),C(t)$ | $\breve\theta=-q^\top Aq-q^\top B-C$ (Prop. 1) | $A,B,C$ |
| $\Delta^{i,b}_{j,k}=\alpha^{i,b}_j(z^i)^k$; $V^b_{j,k}$; $D^b_{j,k}$ | per-asset constants, their vector, diagonal matrix (Prop. 1) | — |
| $D_+=D^b_{2,1}+D^a_{2,1}$ | $\mathrm{diag}\big((\alpha^{i,b}_2+\alpha^{i,a}_2)z^i\big)$: curvature × size (p. 112) | the "liquidity matrix"; ⚠ the project page [[matrix-riccati-equation]] calls this $\Gamma$ |
| $D_-$, $V_-$ | bid–ask asymmetry terms $D^b_{2,2}-D^a_{2,2}$, $V^b_{1,1}-V^a_{1,1}$ | — |
| $\hat A=\sqrt\gamma(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}$ | Riccati driver (p. 112) | — |
| $\Gamma=D_+^{-1/2}(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}D_+^{-1/2}$ | ergodic matrix, $A(0)\to\frac12\sqrt\gamma\Gamma$ (p. 114) | ⚠ BEGV's $\Gamma$ is **this**, not the liquidity matrix |
| $\mathcal D(\cdot)$ | diagonal of a matrix as a vector (p. 110) | — |
| $\tilde\delta^{i,b*}_\xi(p)$ | quote map $\Lambda^{-1}(\xi zH(p)-H'(p))$ (p. 108) | $\delta^*(p)$ |
| finite difference $(\theta(t,q)-\theta(t,q+z^ie^i))/z^i$ | argument of $H$ (eq. 5) | shadow price $p^j$ |
| $N$, $n$, $\nu^{i,n,s}(dz)$, $c^{i,n,s}$ | tiers, size distribution, fixed cost (Sec. 5) | — |
| $\chi,\tilde\chi,\hat\chi,\tilde V$ | aggregated constants (Prop. 4) | — |
| $\eta$, $\epsilon$, $\breve{\mathbb P}$ | first-order correction, perturbation size, auxiliary measure (Sec. 4) | — |
| $C^i_\xi$ | constant in the exponential Hamiltonian (p. 118) | ⚠ not $C(t)$ |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 101 |
| ✓ F1 | 1 Introduction (AS lineage, multi-asset motivation, uses of a value proxy, outline) | 101–104 |
| ✓ F1 | 2.1 Model Setup (prices, quotes, intensities, risk limits, cash) | 104–105 |
| ✓ F1 | 2.2 The Optimization Problems (Model A CARA, Model B risk-adjusted) | 105–106 |
| ✓ F1 | 2.3 The Hamilton–Jacobi–Bellman and Hamilton–Jacobi Equations (eqs. 1–6) | 106–107 |
| ✓ F1 | 2.4 Existing Theoretical Results (Thms 1–2, eqs. 7–8) | 107–108 |
| ✓ F1 | 3.1 Introduction: quadratic Hamiltonians (eqs. 9–10, Remark 1) | 109–110 |
| ✓ F1 | 3.2 An Approximation of the Value Function in Closed Form (Props 1–3, eqs. 11–16) | 110–116 |
| ✓ F1 | 3.3.1 Motivation for Closed-form Approximations | 116 |
| ✓ F1 | 3.3.2 Quotes: the General Case (eqs. 17–20) | 116–117 |
| ✓ F1 | 3.3.3 Quotes: the Case of Symmetric Exponential Intensities (spread, skew) | 118–119 |
| ✓ F1 | 4 Beyond the Quadratic Approximation: towards a Correction Term | 119–121 |
| ✓ F1 | 5.1 A More General Model (drift, tiers, size distributions, fixed costs) | 121–123 |
| ✓ F1 | 5.2 The Hamilton–Jacobi Equation (eqs. 21–22, Thms 3–4) | 123–124 |
| ✓ F1 | 5.3 Quadratic Approximation (eqs. 23–26, Props 4–6, Remark 4) | 125–128 |
| ✓ F1 | 5.4.1 Quotes: the General Case (eqs. 27–30) | 128–129 |
| ✓ F1 | 5.4.2 Quotes: the Case of Symmetric Exponential Intensities | 129–130 |
| ✓ F1 | 6.1 Characteristics of Our Example with Two Assets | 130–131 |
| ✓ F1 | 6.2 Value Function and Optimal Quotes (Figs 1–4) | 131–133 |
| ✓ F1 | 6.3 Comparison with Closed-form Approximations (Figs 5–13) | 133–138 |
| ✓ F1 | 7 Conclusion | 138–139 |
| ✓ F1 | Notes 1–17 | 139 |
| — | Acknowledgments, Disclosure, References | 139–141 |
| ✓ F1 | Appendix A. On the Construction of the Processes $N^{i,b}$ and $N^{i,a}$ | 141–142 |

## Kernthesen

### 1. ⭐ Single-asset models are not operable for portfolios, and grid methods do not scale to correlated multi-asset books (p. 102)

The authors' motivation is practical: «because market making algorithms are typically built for
entire portfolios, single-asset models are not sufficient to build operable algorithms, except
under the unrealistic assumption that asset prices are uncorrelated» (p. 102). The multi-asset
extensions (Guéant & Lehalle 2015, Guéant 2017, Bergault & Guéant 2020) are characterised
mathematically, but «computing the value function and the optimal quotes is complicated in the
multi-asset case whenever the prices of the assets are correlated. The grid methods that are
classically used to tackle the single-asset case suffer indeed from the curse of dimensionality and
do not scale up to many practical multi-asset cases» (p. 102). Two existing remedies are named —
the factor method of Bergault & Guéant 2020 (`bergault-2020-size-matters-otc`) and the actor-critic
RL of Guéant & Manziuk 2019 (`gueant-2019-deep-reinforcement-learning`) — but «the computational
cost of most numerical schemes will still be prohibitive for practical use for some asset classes»
(p. 102).

### 2. ⭐⭐ The method approximates the Hamilton–Jacobi equation, not the value function: one HJ equation is replaced by another that is solvable in closed form (pp. 102–103)

«The idea behind the approach is that the value function associated with many market making
problems is the solution of a Hamilton–Jacobi equation that can be 'approximated' by another
Hamilton–Jacobi equation for which the solution can be computed in closed form. Of course, such
closed-form formula does not define a solution to the initial Hamilton–Jacobi equation, but it has
similar properties and should capture most of the relevant financial effects» (pp. 102–103). The
claim is heuristic: no error bound between $\theta$ and $\breve\theta$ is proved anywhere in the
paper. The conclusion restates it: the proxy comes from «the 'approximation' of a Hamilton–Jacobi
equation by another Hamilton–Jacobi equation that can be simplified into a Riccati equation and two
linear ordinary differential equations, all solvable in closed form» (p. 138).

### 3. ⭐ A value proxy has three uses — heuristic evaluation, initialisation of iterative/RL methods, and a greedy policy (pp. 103, 116)

Borrowing RL vocabulary (Sutton & Barto 2018; Szepesvári 2010), the proxy can be (i) a heuristic
evaluation function, e.g. a terminal value in Monte-Carlo RL, «analogous to algorithms such as Deep
Blue» (p. 116); (ii) a starting point for value iteration or actor-critic; (iii) the source of «the
greedy strategy associated with that proxy (i.e., the strategy that makes the locally optimal choice
if at each time step the value function associated with the tail problem is replaced by its proxy in
the dynamic programming equation)» (p. 103). Use (iii) «was also our initial motivation» (p. 103).
For use (i), $C(t)$ is irrelevant because «it vanishes when computing the difference in the value
function between two points», so the asymptotic quadratic form can replace $\breve\theta$ for large
$T$ (p. 116); for use (ii), $C(t)$ matters (p. 116). The greedy quotes are also proposed as starting
points for policy iteration and actor-critic (pp. 103, 117).

### 4. The base model: $d$ correlated arithmetic-Brownian assets, Poisson-type fills whose intensity depends only on the asset's own quote, hard risk limits (pp. 104–105)

$dS^i_t=\sigma^idW^i_t$ with correlation $\rho^{i,j}$ and covariance $\Sigma$; $dq^i_t=z^idN^{i,b}_t-z^idN^{i,a}_t$
with constant size $z^i$. The fill intensities are
$\lambda^{i,b}_t=\Lambda^{i,b}(\delta^{i,b}_t)\mathbb 1_{\{q^i_{t-}+z^i\le Q^i\}}$ and
$\lambda^{i,a}_t=\Lambda^{i,a}(\delta^{i,a}_t)\mathbb 1_{\{q^i_{t-}-z^i\ge -Q^i\}}$ (p. 104): the market maker
«stops proposing a bid (respectively ask) price for asset i when her position in asset i following
the transaction would exceed a given threshold $Q^i$» (p. 104). The intensity functions are assumed
$C^2$, strictly decreasing, vanishing at $+\infty$, and
$\sup_\delta \Lambda(\delta)\Lambda''(\delta)/(\Lambda'(\delta))^2<2$ (p. 105). Cash: $dX_t=\sum_i(\delta^{i,b}_tz^idN^{i,b}_t+\delta^{i,a}_tz^idN^{i,a}_t)-\sum_iS^i_tdq^i_t$
(p. 105). Liquidity of asset $i$ depends on nothing but $\delta^i$: no time, no history, no other
asset.

### 5. Two objective functions are treated in parallel: CARA utility (Model A) and risk-adjusted expectation (Model B) (pp. 105–106)

Model A, following Avellaneda–Stoikov: $\sup\mathbb E[-\exp(-\gamma(X_T+\sum_iq^i_TS^i_T))]$
(p. 105). Model B, following Cartea, Jaimungal & Ricci 2014: $\sup\mathbb E[X_T+\sum_iq^i_TS^i_T-\frac12\gamma\int_0^Tq_t^\top\Sigma q_t\,dt]$
(p. 106). Controls are predictable and bounded below (set $\mathcal A$, p. 105). There is no terminal
inventory penalty: «as we shall focus on the asymptotic regime of the optimal quotes, there is no
point considering such a penalty. However, it is noteworthy that most of our non-asymptotic results
could be generalized to the case of a quadratic terminal penalty» (note 6, p. 139).

### 6. ⭐⭐ Both models reduce to one system of ODEs (5) on the inventory grid, indexed by $\xi\in\{\gamma,0\}$ (pp. 106–107)

The HJB equations (1) (Model A, $u(t,x,q,S)$) and (2) (Model B, $v(t,x,q,S)$) are reduced with the
Guéant 2017 ansatz $u=-\exp(-\gamma(x+\sum_iq^iS^i+\theta(t,q)))$ and $v=x+\sum_iq^iS^i+\theta(t,q)$ to
the Hamilton–Jacobi equation (p. 107)

$$0=\partial_t\theta(t,q)-\tfrac12\gamma q^\top\Sigma q+\sum_{i=1}^d\mathbb 1_{\{q^i+z^i\le Q^i\}}z^iH^{i,b}_\xi\!\Big(\tfrac{\theta(t,q)-\theta(t,q+z^ie^i)}{z^i}\Big)+\sum_{i=1}^d\mathbb 1_{\{q^i-z^i\ge-Q^i\}}z^iH^{i,a}_\xi\!\Big(\tfrac{\theta(t,q)-\theta(t,q-z^ie^i)}{z^i}\Big)\quad(5)$$

with $\theta(T,q)=0$ (6), $\xi=\gamma$ for Model A and $\xi=0$ for Model B, and Hamiltonians
$H^{i,b}_\xi(p)=\sup_\delta\frac{\Lambda^{i,b}(\delta)}{\xi z^i}(1-\exp(-\xi z^i(\delta-p)))$ for $\xi>0$,
$\sup_\delta\Lambda^{i,b}(\delta)(\delta-p)$ for $\xi=0$ (3)–(4), p. 106–107. (Note 8: this $H$ differs by a factor
$z^i$ from Guéant 2017.) Existence and uniqueness of a $C^1$-in-time solution, and verification, are
imported from Guéant 2017, Thms 5.1–5.3 (p. 107) — `gueant-2017-optimal-market-making`.

### 7. Optimal quotes are a known map of the finite differences of $\theta$; approximate quotes are the greedy policy of an approximate $\theta$ (pp. 107–108)

Theorem 1 (Model A): $\delta^{i,b*}_t=\tilde\delta^{i,b*}_\gamma\big(\frac{\theta(t,q_{t-})-\theta(t,q_{t-}+z^ie^i)}{z^i}\big)$,
with $\tilde\delta^{i,b*}_\gamma(p)=\Lambda^{i,b^{-1}}(\gamma z^iH^{i,b}_\gamma(p)-H^{i,b\prime}_\gamma(p))$ (eq. 7, p. 108);
Theorem 2 (Model B): $\tilde\delta^{i,b*}_0(p)=\Lambda^{i,b^{-1}}(-H^{i,b\prime}_0(p))$ (eq. 8, p. 108). The paper then
calls $\theta$ «slightly abusively» the value function and notes that plugging an approximation of
$\theta$ into (7)–(8) gives «what the reinforcement learning community calls the greedy quoting
strategy associated with the proxy of the value function» (p. 108); the true optimum is itself the
greedy strategy w.r.t. the true $\theta$ (note 9, p. 139).

### 8. ⭐⭐ Point-process control is not LQ, but price risk enters quadratically — so only the Hamiltonian needs to be made quadratic (p. 109)

«One important exception goes with the class of Linear-Quadratic (LQ) and Linear-Quadratic-Gaussian
(LQG) problems. Of course, the above market making problem does not belong to this class of control
problems, for instance because the control of point processes is nonlinear by nature. Nevertheless,
we see that price risk appears in both Model A and Model B through the quadratic term
$\frac12\gamma q^\top\Sigma q$» (p. 109). Hence: «The main idea of this paper consists in replacing
the Hamiltonian functions associated with our market making problem by quadratic functions that
approximate them. The interest of quadratic Hamiltonian functions lies in that the resulting
Hamilton–Jacobi equations can be solved in closed-form using the same tools as for LQ/LQG problems,
i.e., Riccati equations» (p. 109).

### 9. ⭐⭐ A U-shaped approximation of a decreasing function is legitimate because the object that matters is $p\mapsto H^b(p)+H^a(-p)$ (p. 109)

The authors anticipate the objection: «the functions $H^{i,b}_\xi$ and $H^{i,a}_\xi$ are indeed
positive and decreasing and approximating them with U-shaped functions can only be valid locally.
However, one has to bear in mind that our goal is to approximate the solution of the Hamilton–Jacobi
equations and not the Hamiltonian functions» (p. 109). Under the heuristic «Assuming that
$\frac{\theta(t,q)-\theta(t,q+z^ie^i)}{z^i}\simeq-\frac{\theta(t,q)-\theta(t,q-z^ie^i)}{z^i}$», asset $i$
contributes $H^{i,b}_\xi(p)+H^{i,a}_\xi(-p)$, so «it is natural to approximate the former function with
a U-shaped one!» (p. 109). The heuristic presupposes $\theta$ locally smooth/concave in $q$ (bid and ask
finite differences of opposite sign), and it is made after discarding the indicators: «considering
the limit case where $\forall i$, $Q^i=+\infty$» (p. 109).

### 10. ⭐ The quadratic coefficients are free constants; the "natural choice" is a Taylor expansion at $p=0$ (Remark 1, p. 109)

$\breve H^{i,b}:p\mapsto\alpha^{i,b}_0+\alpha^{i,b}_1p+\frac12\alpha^{i,b}_2p^2$ (same for $a$). «A natural
choice … derives from Taylor expansions around $p=0$. In that case, $\alpha^{i,b}_j=H^{i,b(j)}_\xi(0)$»
(Remark 1, p. 109). The coefficients depend on $\xi$ (note 10, p. 139). Everything from Prop. 1 onward
holds for arbitrary constants $\alpha_j$ with $\alpha^{i,b}_2+\alpha^{i,a}_2>0$; the paper never uses
another expansion point. The approximate equation is (9), p. 110:

$$0=\partial_t\breve\theta-\tfrac12\gamma q^\top\Sigma q+\sum_iz^i(\alpha^{i,b}_0+\alpha^{i,a}_0)+\sum_i\big(\alpha^{i,b}_1(\breve\theta(t,q)-\breve\theta(t,q+z^ie^i))+\alpha^{i,a}_1(\breve\theta(t,q)-\breve\theta(t,q-z^ie^i))\big)+\tfrac12\sum_i\tfrac1{z^i}\big(\alpha^{i,b}_2(\breve\theta(t,q)-\breve\theta(t,q+z^ie^i))^2+\alpha^{i,a}_2(\breve\theta(t,q)-\breve\theta(t,q-z^ie^i))^2\big)\quad(9)$$

### 11. ⭐⭐ A quadratic ansatz solves the approximate equation exactly, through a triangular ODE system for $(A,B,C)$ (Prop. 1, pp. 110–111)

With $\Delta^{i,b}_{j,k}=\alpha^{i,b}_j(z^i)^k$, $V^b_{j,k}=(\Delta^{1,b}_{j,k},\dots,\Delta^{d,b}_{j,k})^\top$,
$D^b_{j,k}=\mathrm{diag}(\Delta^{1,b}_{j,k},\dots,\Delta^{d,b}_{j,k})$ (same for $a$), and $A:[0,T]\to S^+_d$,
$B:[0,T]\to\mathbb R^d$, $C:[0,T]\to\mathbb R$ solving (p. 110)

$$\begin{cases}A'(t)=2A(t)(D^b_{2,1}+D^a_{2,1})A(t)-\tfrac12\gamma\Sigma\\ B'(t)=2A(t)(V^b_{1,1}-V^a_{1,1})+2A(t)(D^b_{2,2}-D^a_{2,2})\mathcal D(A(t))+2A(t)(D^b_{2,1}+D^a_{2,1})B(t)\\ C'(t)=\mathrm{Tr}(D^b_{0,1}+D^a_{0,1})+\mathrm{Tr}((D^b_{1,2}+D^a_{1,2})A(t))+(V^b_{1,1}-V^a_{1,1})^\top B(t)+\tfrac12\mathcal D(A)^\top(D^b_{2,3}+D^a_{2,3})\mathcal D(A)+\tfrac12B^\top(D^b_{2,1}+D^a_{2,1})B+B^\top(D^b_{2,2}-D^a_{2,2})\mathcal D(A)\end{cases}\quad(11)$$

with $A(T)=B(T)=C(T)=0$ (12), the function $\breve\theta(t,q)=-q^\top A(t)q-q^\top B(t)-C(t)$ solves (9)–(10).
The proof is coefficient identification «of the terms of degree 0, 1, and 2 in q» (p. 111), using
$\breve\theta(t,q)-\breve\theta(t,q+z^ie^i)=2z^iq^\top Ae^i+(z^i)^2e^{i\top}Ae^i+z^ie^{i\top}B$ — affine in $q$,
so its square is quadratic. «The system of ODEs (11) being triangular – though not linear – we
tackle the equations one by one, in order» (p. 112).

### 12. ⭐⭐ The matrix Riccati equation for $A$ has an explicit tanh solution (Prop. 2, eq. 13, pp. 111–113)

Assume $\alpha^{i,b}_2+\alpha^{i,a}_2>0$ for all $i$, so $D_+=D^b_{2,1}+D^a_{2,1}=\mathrm{diag}((\alpha^{1,b}_2+\alpha^{1,a}_2)z^1,\dots)$
is positive diagonal and $\hat A=\sqrt\gamma(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}\in S^+_d$ (p. 112). The change of
variables $\mathbf a(t)=2D_+^{1/2}A(t)D_+^{1/2}$ turns the $A$-equation into $\mathbf a'=\mathbf a^2-\hat A^2$,
$\mathbf a(T)=0$ (16); with $z(t)=e^{\hat A(T-t)}+e^{-\hat A(T-t)}$ (so $z''=\hat A^2z$, $z'(T)=0$) and
Cauchy–Lipschitz, $\mathbf a=-z'z^{-1}$ (p. 112). Hence (p. 111, p. 113)

$$A(t)=\tfrac12D_+^{-1/2}\hat A\big(e^{\hat A(T-t)}-e^{-\hat A(T-t)}\big)\big(e^{\hat A(T-t)}+e^{-\hat A(T-t)}\big)^{-1}D_+^{-1/2}=\tfrac12D_+^{-1/2}\hat A\tanh(\hat A(T-t))D_+^{-1/2}.\quad(13)$$

The closed form exists because the Riccati equation has **constant** coefficients ($D_+$, $\Sigma$) and
can be symmetrised into a scalar-like equation in the single matrix $\hat A$.

### 13. ⭐ $B$ and $C$ follow by variation of parameters and integration, exploiting that all $A(s)D_+$ commute (pp. 111–113)

Since $\hat A$, $e^{\pm\hat A(T-s)}$ and their sums/inverses all commute, $A(s)D_+A(t)D_+=A(t)D_+A(s)D_+$ (p. 113),
so the linear $B$-equation has the explicit solution
$B(t)=-2e^{-2\int_t^TA(u)D_+du}\int_t^Te^{2\int_s^TA(u)D_+du}A(s)(V_-+D_-\mathcal D(A(s)))\,ds$ (14), with
$D_-=D^b_{2,2}-D^a_{2,2}$, $V_-=V^b_{1,1}-V^a_{1,1}$ (p. 112). $C$ is a plain integral (15), p. 112. With
symmetric intensities $V_-=0$, $D_-=0$, hence $B\equiv0$.

### 14. ⭐ The ergodic limit is explicit: $A(0)\to\frac12\sqrt\gamma\,\Gamma$ with $\Gamma=D_+^{-1/2}(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}D_+^{-1/2}$ (Prop. 3, pp. 113–116)

Diagonalising $\hat A=P\,\mathrm{diag}(\lambda_1,\dots,\lambda_d)P^\top$ gives $A(0)=\frac12D_+^{-1/2}P\,\mathrm{diag}(\lambda_i\tanh(\lambda_iT))P^\top D_+^{-1/2}\to\frac12\sqrt\gamma\Gamma$
(p. 114). Also $B(0)\to-D_+^{-1/2}\hat A\hat A^+D_+^{-1/2}(V_-+\frac12\sqrt\gamma D_-\mathcal D(\Gamma))$, $\hat A^+$ the
Moore–Penrose inverse, and $C(0)/T$ converges to an explicit constant (pp. 113–114). The $B$ proof
shows a remainder $J(T)\to0$ using the smallest positive eigenvalue of $\hat A$, and that
$P\,\mathrm{diag}(1-1/\cosh(\lambda_iT))P^\top$ tends to the orthogonal projector on $\mathrm{Im}(\hat A)$
(pp. 115–116). This is the "asymptotic (ergodic) regime" of the abstract (p. 101).

### 15. ⭐ Greedy quotes are explicit; in the ergodic regime the skew is linear in inventory through $\Gamma$, and cross-asset inventory enters through the off-diagonal of $\Gamma$ (pp. 116–117)

General case (p. 117): $\breve\delta^{i,b}_t=\tilde\delta^{i,b*}_\xi(2q_{t-}^\top A(t)e^i+z^ie^{i\top}A(t)e^i+e^{i\top}B(t))$,
$\breve\delta^{i,a}_t=\tilde\delta^{i,a*}_\xi(-2q_{t-}^\top A(t)e^i+z^ie^{i\top}A(t)e^i-e^{i\top}B(t))$. Ergodic (17)–(18):

$$\bar\delta^{i,b}_t=\tilde\delta^{i,b*}_\xi\Big(\sqrt\gamma\,q_{t-}^\top\Gamma e^i+\tfrac12\sqrt\gamma z^ie^{i\top}\Gamma e^i-e^{i\top}D_+^{-1/2}\hat A\hat A^+D_+^{-1/2}\big(V_-+\tfrac12\sqrt\gamma D_-\mathcal D(\Gamma)\big)\Big)\quad(17)$$

and symmetrically (18); with symmetric intensities (19)–(20) drop the last term. «the closed-form
approximation of the optimal bid and ask quotes for asset i depend on the current value of the
inventory through the term $q_{t-}^\top\Gamma e^i$» (p. 117); own-inventory dependence is monotone, while
«The dependence on the inventory in other assets is more subtle as it is linked to the matrix
$\Gamma$ … which models the complex interplay between price risk and liquidity risk» (p. 117).
As in GLFT, «the influence of the risk aversion parameter $\gamma$ is ambiguous» (p. 117).

### 16. ⭐ With exponential intensities the greedy quotes are affine and reproduce GLFT 2013 for one asset (pp. 118–119)

For $\Lambda^{i,b}=\Lambda^{i,a}=A^ie^{-k^i\delta}$: $H^{i,b}_\xi(p)=\frac{A^i}{k^i}C^i_\xi e^{-k^ip}$ with
$C^i_\xi=(1+\frac{\xi z^i}{k^i})^{-(1+\frac{k^i}{\xi z^i})}$ ($\xi>0$) or $e^{-1}$ ($\xi=0$), and
$\tilde\delta^*(p)=p+\frac1{\xi z^i}\log(1+\frac{\xi z^i}{k^i})$ or $p+\frac1{k^i}$ (p. 118). Taylor at 0 gives
$D_+=\mathrm{diag}(2A^iC^i_\xi k^iz^i)$ and
$\breve\delta^{i,b}_t=\sqrt\gamma(q_{t-}^\top\Gamma e^i+\frac12z^ie^{i\top}\Gamma e^i)+\frac1{\gamma z^i}\log(1+\frac{\gamma z^i}{k^i})$ (Model A), or
$+\frac1{k^i}$ (Model B) (p. 118). «It is noteworthy that these approximations of the optimal quotes are
affine in the current inventory. In particular, in the case of Model A, when the number of assets is
reduced to one (with unitary transaction size), they coincide with the affine closed-form
approximations obtained in the paper (Guéant, Lehalle, and Fernandez-Tapia 2013) … Their
approximations, however, are obtained in a fundamentally different manner, by using spectral
arguments and a continuous approximation of the initial discrete problem» (p. 118) — see
[[glft-2013-model]], [[gueant-2013-dealing-inventory-risk]].

### 17. Spread is constant and skew linear: the skew manages inventory risk, the spread trades frequency against margin (pp. 118–119)

Half-spread $\frac12(\breve\delta^a+\breve\delta^b)=\frac12\sqrt\gamma z^ie^{i\top}\Gamma e^i+\frac1{\gamma z^i}\log(1+\frac{\gamma z^i}{k^i})$
(Model A) or $\dots+\frac1{k^i}$ (Model B); skew $\frac12(\breve\delta^a-\breve\delta^b)=-\sqrt\gamma q_t^\top\Gamma e^i$
in both (p. 119). «These approximations give us a constant bid-ask spread and a skew linear in the
inventory. This translates well the intuition that the skew has the role of inventory risk
management, whereas the spread balances the trade-off between frequency of transactions and profit
per round-trip trade» (p. 119), plus a risk-aversion buffer $\frac12\sqrt\gamma z^ie^{i\top}\Gamma e^i$. In
Model B the spread is nondecreasing in $\gamma$ (note 12, p. 139). Multi-asset sensitivity analysis is
«less obvious» because of $\Gamma$ (p. 119).

### 18. ⭐ A first-order perturbation around the quadratic Hamiltonian gives a Monte-Carlo correction that uses the exact Hamiltonian (Sec. 4, pp. 119–121)

«we regard the real Hamiltonian functions as small perturbations of the quadratic functions used to
approximate them and consider then a first order approximation (the zeroth order approximation being
then that obtained in Section 3)» (p. 119). Writing $H=\breve H+\epsilon h$, $\theta=\breve\theta+\epsilon\eta$
in (5) (with $Q^i=+\infty$), $\eta$ solves a linear equation with sources $z^ih^{i,s}(\cdot)$ and jump
intensities $-\breve H^{i,s\prime}(\cdot)$ (p. 120); by Feynman–Kac,
$\theta(t,q)\simeq\breve\theta(t,q)+\mathbb E^{\breve{\mathbb P}}\big[\int_t^T\sum_iz^i(H^{i,b}_\xi-\breve H^{i,b})(\breve p^{i,b}_s)+z^i(H^{i,a}_\xi-\breve H^{i,a})(\breve p^{i,a}_s)\,ds\big]$,
where under $\breve{\mathbb P}$ inventory jumps with intensities $-\breve H^{i,s\prime}$ evaluated at the
proxy's finite differences (p. 121). «Of course this new approximation is not a closed-form one.
However, the correction term can be computed using a Monte-Carlo simulation for a specific (t, q)»,
e.g. «upon receiving a request for quote from a client and if time permits» (p. 121). No numerical
test of the correction is reported.

### 19. ⭐ The closed form survives drift, client tiers, distributed request sizes and fixed costs (Sec. 5, pp. 121–128)

Prices $dS^i_t=\mu^idt+\sigma^idW^i_t$; $N$ tiers; quotes $\delta^{i,n,s}_t(z)$ size-dependent and bounded
below by $-\delta_\infty$ (note 15); fills are $\mathbb R^*_+$-marked point processes with intensity kernel
$\Lambda^{i,n,b}(\delta^{i,n,b}_t(z))\mathbb 1_{\{q^i_{t-}+z\le Q^i\}}\nu^{i,n,b}(dz)$ (p. 122); fixed costs $c^{i,n,s}$
(p. 122). The HJ equation (21) gains a linear term $\mu^\top q$ and size integrals, with
$H^{i,n,b}_\xi(z,p)$ evaluated at $(\theta(t,q)-\theta(t,q+ze^i)+c^{i,n,b})/z$ (p. 123). Existence/uniqueness
follows Bergault & Guéant 2020; verification needs second moments of $\nu$ (p. 123). Quadratic
Hamiltonians with $z$-dependent coefficients (Remark 3, p. 125) give (23); the same ansatz gives the
ODE system (25), now with $B'=\mu+\dots$ and $\tilde V$, $\chi$ terms (Prop. 4, p. 126), and the closed form
(Prop. 5, p. 127) with $A$ unchanged in form (now $D_+=\sum_n\int z\,\alpha_2^{i,n,s}(z)\nu(dz)$-weighted). Quotes
(27)–(30) are size- and cost-dependent (pp. 128–129). Proportional costs can be handled by shifting
intensities (note 16, p. 139).

### 20. With a drift, the ergodic limit needs $D_+^{1/2}\mu\in\mathrm{Im}(\hat A)$; otherwise the problem has a riskless-return incentive (Remark 4, p. 128)

Prop. 6 (pp. 127–128) gives $A(0)\to\frac12\sqrt\gamma\Gamma$ and an explicit $B(0)$ limit containing
$-D_+^{-1/2}\hat A^+D_+^{1/2}\mu$, under that range condition. «The assumption … is satisfied when
$\mu=0$ or when $\Sigma$ is invertible. If this assumption is not satisfied, then it can be shown that
$\frac{B(0)}{T}\to-D_+^{-1/2}\hat A^+\hat AD_+^{1/2}\mu$. In particular, there is no constant asymptotic
approximation of the quotes. In fact, … the market maker may have an incentive to propose very good
quotes to clients in order to build portfolios bearing positive return at no risk» (p. 128). The
drift models «the views of the market maker» (p. 103).

### 21. ⭐ The two-asset benchmark: the approximate quotes match the grid optimum except at large inventory, and P&L is statistically indistinguishable (Sec. 6, pp. 130–138)

Two assets, $S_0=100$, drifts $\mu^1=0.1$, $\mu^2=-0.1$ €/day, $\sigma^1=1.2$, $\sigma^2=0.6$ €·day$^{-1/2}$, $\rho=0.5$,
$\Sigma=\begin{pmatrix}1.44&0.36\\0.36&0.36\end{pmatrix}$; Model B («The results would be similar for
Model A», note 17), $T=7$ days, $\gamma=8\cdot10^{-6}$ €$^{-1}$, one tier, no costs (pp. 130–131). Intensity
$\Lambda^{i,b}=\Lambda^{i,a}=\lambda_{RFQ}/(1+e^{\alpha_\Lambda+\beta_\Lambda\delta})$, $\lambda_{RFQ}=30$/day,
$\alpha_\Lambda=0.7$, $\beta_\Lambda=30$ €$^{-1}$ (≈33% fill at mid, ≈40% one cent better); sizes Gamma
($\alpha_\mu=4$, $\beta_\mu=4\cdot10^{-4}$, mean 10,000) discretised to 6,250/12,500/18,750/25,000 with
probabilities 0.534/0.350/0.097/0.019; $Q^1=75{,}000$, $Q^2=300{,}000$ (p. 131). Benchmark: monotone
implicit Euler on a $101\times25\times97$ grid (p. 131); the horizon is long enough to be in the asymptotic
regime (Fig. 1, pp. 131–132). Value functions: «in spite of differences in level … the shape is the
same» (p. 134). Quotes: «close to the true optimal quotes, except for large values of the inventory in
asset 2» (p. 135). P&L over 4000 MC runs: optimal mean 88,600 € (sd 86,900 €) vs closed form 89,000 €
(sd 87,500 €) (p. 135). No regret percentage, confidence interval or quote-error metric is given.

### 22. The authors extrapolate the two-asset result to higher dimension without evidence (p. 137)

«We believe that what we observe here in this two-asset example is general. In particular, the
results in higher dimensions should be just as good» (p. 137). No experiment with $d>2$ is reported,
and the grid benchmark could not provide one.

### 23. Weak formulation: controlling intensities is choosing a probability measure, which removes the independence assumption between fills and prices (note 5, Appendix A, pp. 139, 141–142)

«It is often assumed in the literature that the point processes are independent of the Brownian
motions. In that case, the quote processes … have to be independent of prices. In fact, the optimal
control problem can be written in a weak form to show that this assumption is not necessary» (note 5,
p. 139). Appendix A builds $N^b,N^a$ from unit-rate Poisson processes with the risk-limit indicators,
then changes measure (A.1) with a stochastic-exponential density driven by the compensated
processes $\tilde N^b,\tilde N^a$ and the controlled intensities $\Lambda^s(\delta^s_t)$, citing Brémaud & Jacod 1977; «our optimal control problem can be seen as the choice of an
optimal probability measure» (p. 142). One asset only, «the generalization is straightforward» (p. 141).

### 24. The paper positions itself in the Avellaneda–Stoikov / quote-driven tradition and lists the feature extensions of the literature (pp. 101–102)

Lineage: Ho & Stoll 1981/1983 → Avellaneda & Stoikov 2008 → GLFT 2013 («under inventory constraints,
the problem reduces to a system of linear ordinary differential equations in the case of exponential
intensity functions», p. 101). Cartea–Jaimungal and co-authors added «alpha signals, ambiguity
aversion, etc.» (p. 101). Further features: «general dynamics for the price in (Fodra and Labadie
2012), general intensities and partial information (Campi and Zabaljauregui 2020), persistence of the
order flow in (Jusselin 2020), several requested sizes in (Bergault and Guéant 2020), client tiering
and access to a liquidity pool in (Barzykin, Bergault, and Guéant 2021)» (p. 102). These models have
been «more useful to build market making algorithms in quote-driven markets» (RFQ bonds, FX RFQ/RFS)
than for order-driven stock markets, where LOB models are used instead (p. 102).

### 25. Closed-form quotes are valued for interpretability and as warm starts, not as the final optimum (pp. 103, 117)

A closed-form strategy «can be used directly by market practitioners», can seed policy-iteration or
actor-critic, and «has the advantage of being easily interpretable and gives insights on the true
optimal strategy such as the identification of the leading factors and the sensitivity to changes in
model parameters» (p. 103). «All these approximations of the optimal quotes can be used directly or as
starting points in iterative methods» (p. 117, repeated p. 129).

## Figures and tables

- Fig. 1 (p. 132): optimal bid quotes vs time for several inventories (very small trades), both assets — shows the asymptotic regime is reached.
- Fig. 2 (p. 132): numerical $\theta$ at $t=0$ over $(q^1,q^2)$.
- Figs 3–4 (p. 133): optimal bid quote surfaces, asset 1 and asset 2.
- Fig. 5 (p. 134): closed-form $\breve\theta$ at $t=0$ (Prop. 4).
- Figs 6–7 (pp. 134–135): closed-form bid quote surfaces.
- Figs 8–11 (pp. 136–137): optimal vs closed-form bid quotes, four sizes, along $q^1$ and $q^2$ axes — the only direct accuracy evidence.
- Figs 12–13 (p. 138): P&L histograms, optimal vs closed form, 4000 MC runs.
- No tables.

No figures extracted to `knowledge/assets/` in this pass (write scope limited to this page).

## What this source does not address

- **Stochastic, state-dependent or self-exciting intensities.** Every intensity is a deterministic,
  time-homogeneous function of the asset's own quote (p. 104). "Hawkes" never appears; persistent /
  mutually exciting flow is only cited (Jusselin 2020, p. 102; CJR 2018 in the references, p. 140).
  For forecast-driven intensities on one asset see [[barzykin-2026-hawkes-driven-otc]]; for Hawkes
  intensities as a state see [[martin-2026-market-making-hawkes]] and
  [[jusselin-2021-persistent-order-flow]]; for why fill-driven Hawkes breaks the ansatz see
  [[bergault-2024-price-aware-automated]].
- **Cross-asset liquidity coupling.** $D_+$ is diagonal: assets interact only through $\Sigma$ (and,
  in Sec. 5, the drift). For cross-asset Hawkes structure see [[acero-2026-hawkes-structured-networks]].
- **Error bounds.** No theorem relates $\breve\theta$ to $\theta$; the quality claim rests on one
  two-asset example (pp. 130–137).
- **Inventory limits in the closed form.** The proxy assumes $Q^i=+\infty$ (pp. 109, 125); limits are
  only used in the grid benchmark (p. 131).
- **Terminal penalty, price impact, adverse selection, hedging, options.** Not modelled (terminal
  penalty: note 6). Hedging and impact in FX: `barzykin-2021-market-making-fx`.
- **RL experiments.** RL use of the proxy is proposed (pp. 103, 116) but not tested; see
  `gueant-2019-deep-reinforcement-learning`.
- **Ambiguity aversion, factor models.** Only cited (pp. 101–102); factor reduction in
  `bergault-2020-size-matters-otc`.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24.**

**Short answer for this focus:** the source models **no** self- or cross-exciting flow. Its value
is that it is the exact template the project wants to extend, and that it shows precisely which
hypotheses the closure uses. Steps (a)–(e) below reconstruct the closure; the assumptions list
after them is quoted from the paper; the "would break" column is the project's inference.

### What this focus needs beyond the Kernthesen

1. **(a) HJB and reduced variables.** Full state $(t,x,q,S)$, HJB (1)/(2) (p. 106). The ansatz
   $u=-e^{-\gamma(x+q\cdot S+\theta)}$ / $v=x+q\cdot S+\theta$ (p. 107) removes $x$ and $S$; it works because
   prices are arithmetic BM with constant $\Sigma$, cash and P&L are linear in $S$, and intensities do
   not depend on $S$ or $t$. The reduced state is **$(t,q)$ only** — (5) is a finite ODE system on the
   inventory grid (p. 107). No intensity state exists to carry.
2. **(b) Where $H^{i,b},H^{i,a}$ enter and what is used about $\Lambda$.** Each enters once per
   asset and side, scaled by $z^i$, evaluated at a finite difference of $\theta$ in the direction $e^i$
   (eq. 5). The four conditions on $\Lambda$ (p. 105) make $H$ well defined, smooth, attained at a
   unique $\tilde\delta^*(p)$ (Thms 1–2, p. 108), «positive and decreasing» (p. 109). The quadratic step
   uses only $H(0),H'(0),H''(0)$ and the sign condition $\alpha^{i,b}_2+\alpha^{i,a}_2>0$ (Prop. 2, p. 111),
   which is **assumed**, not derived. Liquidity of asset $i$ depends only on $\delta^i$, so $D_+$, $D_-$,
   $V_-$ are diagonal or per-asset.
3. **(c) Quadratic replacement.** $\breve H(p)=\alpha_0+\alpha_1p+\frac12\alpha_2p^2$; the «natural choice»
   is Taylor at $p=0$, $\alpha_j=H^{(j)}_\xi(0)$ (Remark 1, p. 109) — i.e. $h_0,h_1,h_2$ in project notation,
   $h_2=H''(0)$. The expansion is around zero shadow price (a quote at its unconstrained optimum),
   not around the ergodic shadow price. The exact Hamiltonian is still used in two places: (i) the
   quote map $\tilde\delta^*_\xi$ is exact, so greedy quotes are exact optimisers at approximate shadow
   prices (p. 117); (ii) the Sec. 4 correction integrates $H_\xi-\breve H$ along paths (p. 121). For
   exponential $\Lambda$, $\tilde\delta^*(p)=p+$const, so quotes come out affine (p. 118).
4. **(d) Ansatz and ODEs.** $\breve\theta=-q^\top Aq-q^\top B-C$ (Prop. 1); finite differences are affine
   in $q$, so (9) has only degrees 0, 1, 2 in $q$ → (11). Matrix Riccati $A'=2AD_+A-\frac12\gamma\Sigma$,
   $A(T)=0$; finite horizon (13) $A(t)=\frac12D_+^{-1/2}\hat A\tanh(\hat A(T-t))D_+^{-1/2}$; ergodic
   $A(0)\to\frac12\sqrt\gamma\,D_+^{-1/2}(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}D_+^{-1/2}$ (Prop. 3). $B$ via
   variation of parameters (14), using that all $A(s)D_+$ commute (p. 113); $C$ by quadrature (15).
5. **(e) Quotes.** Greedy: $\breve\delta^{i,b}=\tilde\delta^{i,b*}_\xi(2q^\top Ae^i+z^ie^{i\top}Ae^i+e^{i\top}B)$ (p. 117);
   ergodic (17)–(20), skew $\sqrt\gamma q^\top\Gamma e^i$. Cross-asset quote dependence comes **only**
   from price correlation through $\Gamma$.

### Assumptions that make the closure work, and what a state-variable $\lambda$ would do to them

| # | Assumption (source wording, page) | Used for | If $\lambda$ became a random state that jumps after trades *(project inference)* |
|---|---|---|---|
| 1 | Intensity is a function of the own quote only: $\lambda^{i,b}_t=\Lambda^{i,b}(\delta^{i,b}_t)\mathbb 1_{\{\dots\}}$ (p. 104) | reduction to $(t,q)$; constant $\alpha_j$ | Breaks: $\theta=\theta(t,q,\lambda)$; generator gains drift and jump terms in $\lambda$; $\alpha_j$ (∝ amplitude, since $H$ is linear in a multiplicative arrival rate) become functions of $\lambda$ |
| 2 | $\Lambda$: $C^2$, decreasing, $\to0$ at $+\infty$, $\sup\Lambda\Lambda''/(\Lambda')^2<2$ (p. 105) | well-posed $H$, unique $\tilde\delta^*$ | Survives if the fill probability keeps these properties and $\lambda$ is a multiplicative amplitude |
| 3 | «the limit case where $\forall i$, $Q^i=+\infty$» (p. 109) | removes indicators so a global quadratic fits | Unaffected (already a gap) |
| 4 | «Assuming that» bid and ask finite differences are approximately opposite (p. 109) | justifies a U-shaped $H^b(p)+H^a(-p)$ | Weakens if one-sided excitation makes $\theta$ strongly asymmetric |
| 5 | Quadratic $\breve H$ with **constant** coefficients, Taylor at $p=0$ (Remark 1, p. 109) | degree-2 closure in $q$ | Coefficients become $\lambda$-dependent → $A(\lambda),B(\lambda),C(\lambda)$, coefficient PDEs in $\lambda$ (Barzykin's transport-jump obstruction, p. 8 of that paper) |
| 6 | $\alpha^{i,b}_2+\alpha^{i,a}_2>0$ (Prop. 2, p. 111) | $D_+$ invertible, $\hat A$ defined | Fails where intensity is near zero; must hold along the forecast |
| 7 | Constant $\Sigma$, arithmetic BM (p. 104); constant drift $\mu$ (p. 121) | time-homogeneous Riccati | Unaffected unless flow and price are coupled |
| 8 | Time-homogeneous constant $D_+$ | tanh formula (13); commuting $A(s)D_+$ for (14); ergodic limit | With deterministic but time-varying $D_+(t)$ (frozen forecast) the Riccati equation is still well posed but **loses (13) and the commutation trick**; it needs numerical integration or a time-ordered propagator |
| 9 | No fill-dependence of future flow (implicit in 1) | inventory jumps do not move liquidity | Fill-driven excitation couples $q$-jumps and $\lambda$-jumps: the finite difference contains $\theta(t,q+z,\lambda+\kappa)-\theta(t,q,\lambda)$ and the ansatz picks up cubic/quartic terms ([[bergault-2024-price-aware-automated]], p. 17) |
| 10 | Quadratic terminal condition (here zero; note 6, p. 139) | exact quadratic proxy | Unaffected |
| 11 | Drift range condition $D_+^{1/2}\mu\in\mathrm{Im}(\hat A)$ (Remark 4, p. 128) | ergodic $B$ | With time-varying $D_+$ the ergodic limit itself has to be redefined |

6. **What carries over to $d$ assets with cross-asset Hawkes (project inference, not the authors').**
   The algebra of Prop. 1 is untouched if the intensity of $(i,s)$ is any *deterministic* function of
   time: replace $\alpha^{i,s}_j$ by $\alpha^{i,s}_j(t)$ (linear in a forecast $m^{i,s}_t$), and (11) becomes a
   time-inhomogeneous matrix Riccati $A'=2AD_+(t)A-\frac12\gamma\Sigma$. Cross-asset excitation then enters
   **only through $D_+(t)$**: a burst in asset $i$ raises the forecast for asset $j$, raises $D_+^{jj}(t)$,
   and through $A$ (coupled by $\Sigma$) shifts the quotes of every correlated asset. $D_+$ stays diagonal,
   because each Hamiltonian belongs to one (asset, side). What is lost is items 1, 5 and 8: the tanh
   formula, the commuting propagator and the ergodic $\Gamma$ in closed form; a state-feedback version
   (re-solving from the post-event forecast) is the route of [[barzykin-2026-hawkes-driven-otc]] in one
   asset.
7. **Stochastic or state-dependent intensities mentioned anywhere?** Only through citations: Campi &
   Zabaljauregui 2020 («general intensities and partial information»), Jusselin 2020 («persistence of
   the order flow»), both p. 102; CJR 2018 «Mutually Exciting Processes» in the references (p. 140).
   Inside the model, the only state dependence is the inventory indicator (p. 104), and in Sec. 4 the
   auxiliary measure $\breve{\mathbb P}$ uses $q$-dependent intensities $-\breve H'(\cdot)$ (p. 121).
8. **Extensions the paper itself states.** Drift, tiers, size distributions, fixed costs (Sec. 5);
   quadratic terminal penalty (note 6); proportional costs via intensity shifts (note 16);
   prices–fills dependence via weak formulation (note 5, App. A); RL warm start and greedy policy
   (pp. 103, 116); MC correction (Sec. 4). Ambiguity aversion and factor models are cited, not extended
   (pp. 101–102). Other intensity shapes: any $\Lambda$ meeting the p. 105 conditions; only exponential
   (p. 118) and logistic (p. 131) are worked out.

### Direct quotes (for the draft)

> "The main idea of this paper consists in replacing the Hamiltonian functions associated with our market making problem by quadratic functions that approximate them. The interest of quadratic Hamiltonian functions lies in that the resulting Hamilton–Jacobi equations can be solved in closed-form using the same tools as for LQ/LQG problems, i.e., Riccati equations." (p. 109)

> "At first sight, approximating the Hamiltonian functions involved in Equation (5) by quadratic functions seems inappropriate. For all i ∈ {1, ..., d}, the functions $H^{i,b}_\xi$ and $H^{i,a}_\xi$ are indeed positive and decreasing and approximating them with U-shaped functions can only be valid locally. However, one has to bear in mind that our goal is to approximate the solution of the Hamilton–Jacobi equations and not the Hamiltonian functions." (p. 109)

> "Of course, such closed-form formula does not define a solution to the initial Hamilton–Jacobi equation, but it has similar properties and should capture most of the relevant financial effects." (p. 103)

> "We clearly see that, in spite of differences in level between the true value function approximated numerically and the closed-form approximation, the shape is the same. Therefore, the finite differences involved in the computation of the associated quotes should be similar." (p. 134)

> "We see that, although the closed-form approximation of optimal quotes may be inaccurate for large values of the inventory, such large inventory are seldom reached and therefore the gap between quotes does not really impact the distribution of the PnL." (p. 136)

### Examples & illustrations (for later drafting)

- Two-asset Model B example (pp. 130–138): $\rho=0.5$, opposite drifts, logistic RFQ fill curve,
  Gamma sizes; quotes agree except at large $|q^2|$ (Figs 8–11); P&L 88,600 € vs 89,000 € mean over
  4000 runs (p. 135). The P&L gap (+400 €) is far below the MC standard error of each mean
  (≈ 86,900/√4000 ≈ 1,370 €) — *project computation*, not stated by the authors.
- One-asset reduction to GLFT 2013 (p. 118): the same affine quotes reached by a different route —
  the bridge from [[glft-2013-model]] to [[begv-2021-model]].
- Remark 4 (p. 128): without the range condition the dealer would quote aggressively to build a
  riskless positive-drift portfolio — an example of a closed form signalling ill-posedness.

### Boundary of this focus

Nothing in the source is about excitation; every statement in this block about Hawkes or
cross-asset excitation (assumption-table column 3, items 6–7) is the project's inference from the
structure of eqs. (5), (9), (11), (13), (14). Accuracy evidence is one two-asset example with a
qualitative quote comparison and a P&L comparison; there is no regret number to compare with
[[regret]] figures elsewhere.

## Mentioned entities

- Models: [[begv-2021-model]], [[glft-2013-model]], [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]]
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[shadow-price]], [[hawkes-process]] (only via citations); for later comparison [[intensity-forecast]], [[markov-lift]], [[volterra-riccati]], [[branching-matrix]], [[regret]]
- Other works (bibkeys): `gueant-2017-optimal-market-making`, `bergault-2020-size-matters-otc`, `gueant-2019-deep-reinforcement-learning`, `campi-2020-optimal-market-making`, `avellaneda-2008-high-frequency-trading`, `cartea-2015-algorithmic-high-frequency`, `barzykin-2021-market-making-fx`, `guilbaud-2011-optimal-high-frequency`, `fodra-2015-high-frequency-trading`; parallel pages [[gueant-2013-dealing-inventory-risk]], [[cartea-2014-buy-low-sell]], [[jusselin-2021-persistent-order-flow]]; not in the library: Ho & Stoll 1981/1983, Guéant & Lehalle 2015, Guéant 2016 (book), Cartea–Donnelly–Jaimungal 2017, CJR 2018, Fodra & Labadie 2012, Kühn & Muhle-Karbe 2015, Lu & Abergel 2018, Baradel et al. 2018, Baldacci–Bergault–Guéant 2021, Stoikov & Sağlam 2009, El Aoud & Abergel 2015, Grossman & Miller 1988, Brémaud & Jacod 1977, Sutton & Barto 2018, Szepesvári 2010.

## Connections

- Is the model page's source: [[begv-2021-model]]; defines [[hamiltonian-quadratic-approximation]] and the constant-coefficient case of [[matrix-riccati-equation]].
- Builds on: [[glft-2013-model]] / [[gueant-2013-dealing-inventory-risk]] (reproduced for $d=1$, p. 118); Guéant 2017 (existence, verification, ansatz); [[avellaneda-stoikov-model]] (objective A); [[cartea-jaimungal-ricci-model]] / [[cartea-2014-buy-low-sell]] (objective B).
- Built on by (later, not cited here): [[barzykin-2026-hawkes-driven-otc]] (same expansion, forecast-driven time-varying coefficients, one asset); [[bergault-2024-price-aware-automated]] (same authors' closure; shows fill-driven Hawkes breaks it, p. 17 there).
- Compare: [[martin-2026-market-making-hawkes]] (exact Hamiltonian with lifted Hawkes state, numerical); [[acero-2026-hawkes-structured-networks]] (multi-asset Hawkes, no value-function closure); [[jusselin-2021-persistent-order-flow]] (cited p. 102 as "persistence of the order flow").
