---
title: "Shen & Zou 2022 — Mean-Variance Portfolio Selection in Contagious Markets"
type: source
created: 2026-10-25
updated: 2026-10-26
status: review
author: llm
bibkey: shen-2022-mean-variance-portfolio
depth: standard
tags: [portfolio-selection, mean-variance, hawkes, mutual-excitation, lq-control, bsde, nonlocal-pde, multi-asset, non-market-making]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Price jumps are driven by an m-dimensional exponential Hawkes process, eq. (2.2)–(2.3): «a jump of N_l at time t not only increases its own instantaneous intensity λ_l(t) by β_ll (self-excitation) but also increases the instantaneous intensities λ_j(t) of other processes N_j by β_jl (cross-excitation)» (p. 6)."
  - target: branching-matrix
    type: mentions
    confidence: inferred
    because: "The jump matrix β = [β_lj] (eq. 2.4, p. 6) is the excitation matrix; the paper states no spectral-radius / stationarity condition, it works on a finite horizon [0,T]."
  - target: markov-lift
    type: mentions
    confidence: extracted
    because: "Exponential decay makes the pair Markov: «The dynamics of λ in (2.3) indicate that (N, λ) is a joint Markov process» (p. 6); the non-Markovian (non-exponential) case is left to future work (p. 29)."
  - target: matrix-riccati-equation
    type: supports
    confidence: inferred
    because: "Value function quadratic in the state with an intensity-dependent coefficient, V = e^{2r(T−t)+g(t,λ)} x² (App. C, p. 34), whose coefficient solves the nonlocal Riccati-type PDE (3.24) (p. 16); a non-market-making precedent for Riccati coefficients that are functions of λ."
  - target: problem-anatomy
    type: supports
    confidence: inferred
    because: "§3a predicts that a quadratic ansatz with A(t,λ) closes in the state but leaves a nonlocal jump equation in λ; SZ show exactly this in an LQ portfolio problem: «In (3.24), U has a non-local dependence on g (see (3.19)), which originates from the mutual-excitation feature of the Hawkes process» (p. 17)."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Excitation is exogenous to the control: «a price-taker in the economy (i.e., her trading does not move the prices of the assets)» (p. 9); the intensity (2.3) contains no control."
  - target: aitsahalia-2016-portfolio-choice-markets
    type: builds-on
    confidence: extracted
    because: "«ours shall follow the work of Aït-Sahalia and Hurd (2016) by modeling the contagion risk via a Hawkes process, but with significant differences» (p. 4); market model «similar to that of Aït-Sahalia and Hurd (2016)» (p. 7)."
based_on: preprint
---

# Shen & Zou 2022 — Mean-Variance Portfolio Selection in Contagious Markets

## Bibliographic Details

Shen, Yang and Bin Zou. 2022. "Mean-Variance Portfolio Selection in Contagious Markets."
*SIAM Journal on Financial Mathematics* 13(2): 391–425. DOI 10.1137/20M1320560.

**Read: arXiv 2110.09417v1 (preprint, dated "This Version: October 19, 2021", marked "Accepted to
SIAM Journal on Financial Mathematics"); page/equation numbers follow it.** 38 pp. incl. appendices
A–C (pp. 30–35) and references (pp. 35–38). PDF page = printed page. Non-core work; preprint
accepted under the project's preprint policy.

### Notation map (source → project)

| Source | Meaning | Project symbol / remark |
|---|---|---|
| $N=(N_1,\dots,N_m)$, $\lambda$ | Hawkes jump counts and intensities | $\lambda_t$ |
| $\lambda_\infty$, $\alpha=\mathrm{Diag}(\alpha_l)$ | long-run level, mean-reversion speed | $\mu$, $D=\mathrm{diag}(\beta)$ ⚠ source's $\alpha$ is the project's decay $\beta$ |
| $\beta=[\beta_{lj}]$, $\beta_{(l)}$ | jump of $\lambda_l$ caused by an $N_j$ event; $l$-th column | jump sizes of $K$ (exponential kernel $\beta_{lj}e^{-\alpha_l u}$) ⚠ clashes with project decay $\beta$ |
| $k$, $n$, $m$ | # risky assets, # Brownian motions, # Hawkes components | $d$ = $k$ |
| $\pi$ | dollar amounts in risky assets (control) | no project analogue (quotes $\delta$ in MM) |
| $X$, $\hat X=X-ce^{-r(T-t)}$ | wealth, shifted wealth | ⚠ $X$ is cash/wealth, not inventory |
| $\eta(z)=[J_{il}z_l]$ | $k\times m$ jump-size matrix | — |
| $\Sigma(t)$, $\Gamma(t,\lambda)$, $\hat Z(t,\lambda)$ | generalised covariance (2.9); ratio-weighted covariance (3.20); adjusted premium (3.21) | ⚠ not the price covariance $\Sigma$ alone |
| $g(t,\lambda)$, $\tilde g=e^g$ | log-coefficient of the quadratic value function | plays the role of $A(t,\lambda)$ (scalar) |
| $U(t,\lambda)$ | vector of $e^{g(\lambda+\beta_{(l)})-g(\lambda)}-1$ | post-/pre-jump coefficient ratio minus one |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (contagion evidence, Fig. 1 Feb-2018 sell-off; precommitment vs equilibrium MV; contributions) | 1–4 |
| ✓ F1 | 2.1 Probabilistic setup and Hawkes jump modeling (eqs. 2.1–2.4, Remark 2.1) | 5–6 |
| ✓ F1 | 2.2 Financial market with contagion risk (eqs. 2.5–2.12, Assumption 2.1, Lemma 2.1, Remark 2.2) | 7–10 |
| ✓ F1 | Problem 2.1 (MV, eq. 2.13), Lagrangian reduction (2.14)–(2.16) | 10–11 |
| ✓ F1, F2 | 3 Heuristic derivations: Steps 1–4 via stochastic maximum principle and BSDE (eqs. 3.1–3.24); Lemmas 3.1–3.2; remarks (3.25) | 12–18 |
| ✓ F1, F2 | 4 Efficient strategy and frontier: Theorem 4.1 (eqs. 4.1–4.8), Poisson Corollary 4.1, Remark 4.1 (eq. 4.12) | 18–23 |
| ✓ F1, F2 | 5 Numerical analysis: 5.1 solving (3.24) by Monte Carlo (Table 1, Fig. 1, Remark 5.1); 5.2 sensitivities (Figs. 2–3); 5.3 Poisson comparison (Figs. 4–5), Remark 5.2 (curse of dimensionality) | 23–29 |
| ✓ F1 | 6 Conclusion | 29 |
| ✓ F1, F2 | App. A proof of Lemma 3.1; App. B proof of Lemma 3.2 (Schauder fixed point, eq. B.1); App. C HJB connection (C.1–C.3) | 30–35 |
| — | References | 35–38 |

## Kernthesen

### 1. ⭐ Contagion is modelled by an m-dimensional exponential Hawkes process with a full excitation matrix (pp. 5–6)

$d\lambda(t)=\alpha(\lambda_\infty-\lambda(t))\,dt+\beta\,dN(t)$ (2.3), $\alpha$ diagonal, $\beta=[\beta_{lj}]\ge0$
full. A jump of $N_l$ raises $\lambda_l$ by $\beta_{ll}$ (self) and $\lambda_j$ by $\beta_{jl}$ (cross),
the impact decaying at rate $\alpha_l$; «(N, λ) is a joint Markov process» (Remark 2.1, p. 6). The
same specification is used by Aït-Sahalia–Hurd, Cao et al. 2020, Liu et al. 2021 (p. 6). No
stationarity condition on $\beta$ is imposed; the horizon is finite.

### 2. Prices are k-asset jump-diffusions whose jumps are the Hawkes events (pp. 7–8)

$dS_i=S_i(t-)[\mu_i dt+\sum_j\sigma_{ij}dW_j+\sum_l J_{il}(Z_l dN_l-E[Z_l]\lambda_l dt)]$ (2.5), with
$J_{il}\in[0,1]$, $Z_l$ i.i.d. on $(-1,\infty)$ (both signs, unlike AH's negative jumps, Remark 2.2,
p. 8). $W$, $N$, $Z$ are mutually independent (Assumption 2.1, p. 7). Hence one Hawkes event $l$
moves **every** asset $i$ with $J_{il}>0$ simultaneously; contagion across assets runs through both
the loading matrix $J$ and the excitation matrix $\beta$.

### 3. The jump risk makes the effective covariance intensity-dependent (Lemma 2.1, p. 8)

$\Sigma(t)=\sigma\sigma^\top+\int\eta(z)\,\mathrm{Diag}[\lambda(t)\bullet\nu(dz)]\,\eta(z)^\top$ (2.9) is
positive definite and its inverse positive semi-definite. In the Poisson case this matrix, at the
deterministic intensity, is what enters the efficient strategy (Cor. 4.1).

### 4. ⭐ The investor is a price-taker: the control does not touch the intensities (p. 9)

«We consider a representative agent (investor), who is a price-taker in the economy (i.e., her
trading does not move the prices of the assets)» (p. 9). The control is the dollar vector $\pi$; the
wealth SDE (2.12) is **linear in $(X,\pi)$**, and $\pi$ scales the size of each jump
($\pi^\top\eta(z)$) but neither its probability nor the intensity dynamics (2.3).

### 5. MV is solved as a precommitment problem through a Lagrangian and a quadratic-loss problem (pp. 3, 10–11)

Problem 2.1: min $E[(X(T)-\xi)^2]$ s.t. $E[X(T)]=\xi$ (2.13). Lagrangian duality turns it into the
unconstrained $\min E[(X(T)-c)^2]$ (2.15) with a free $c$, then a scalar maximisation over the
multiplier $\theta$ (2.16), following Lim–Zhou 2002, Zhou–Yin 2003 (p. 11). Time inconsistency is
handled by precommitment, not equilibrium (p. 3).

### 6. Method: stochastic maximum principle + BSDE, chosen because it extends to non-Markovian Hawkes (pp. 4, 12, 29)

«Given that the stochastic maximum principle can be applied to deal with non-Markovian control
systems with random coefficients, our approach has the potential to tackle portfolio selection
problems under a more general setup with non-Markovian Hawkes processes» (p. 4). Existing SMP
sufficiency results cannot be applied directly «since the Hawkes intensity process is unbounded»
(p. 12); optimality is proved instead by completing the square (Sec. 4).

### 7. ⭐⭐ The adjoint ansatz makes the value coefficient a function of the intensity only (pp. 13–16)

$p=Y\hat X$ (3.5), with $Y$ solving a BSDE driven by $\tilde N$ only (3.6). Ansatz (3.16)–(3.17):
$$Y(t)=2e^{2r(T-t)+g(t,\lambda(t))},\qquad V_l(t)=Y(t)\big(e^{g(t,\lambda(t)+\beta_{(l)})-g(t,\lambda(t))}-1\big).$$
«It is important to notice that, with the ansatz of Y and V in (3.16) and (3.17), Γ and Ẑ defined
above are indeed functions of t and λ only, and are independent of Y and V» (p. 16). The jump
component $V_l$ of the coefficient is the **ratio of post-jump to pre-jump coefficient**, minus one.

### 8. ⭐ The efficient strategy is linear feedback in shifted wealth, with ratio-weighted covariance and premium (pp. 15–16, 18)

$\pi^*_c=-\Gamma(t,\lambda)^{-1}\hat Z(t,\lambda)\,\hat X^*(t-)$ (3.22), where
$\Gamma=\sigma\sigma^\top+\int\eta\,\mathrm{Diag}[(U+1_m)\bullet\lambda\bullet\nu]\eta^\top$ (3.20) and
$\hat Z=B+\int\eta\,\mathrm{Diag}[\lambda\bullet\nu]\,U$ (3.21). Each jump channel $l$ is weighted by
the factor $e^{g(\lambda+\beta_{(l)})-g(\lambda)}$, i.e. by how much worse (or better) the post-jump
state is. Theorem 4.1: $\pi^*=-\Gamma^{-1}\hat Z\,(X^*(t-)-(\xi-\theta^*)e^{-r(T-t)})$ (4.1).

### 9. ⭐⭐ The coefficient solves a nonlocal PDE whose nonlocality is the mutual excitation (pp. 16–17)

Matching drifts gives (3.24):
$$g_t+g_\lambda^\top\alpha(\lambda_\infty-\lambda)+U(t,\lambda)^\top\lambda=\hat Z^\top\Gamma^{-1}\hat Z,\qquad g(T,\cdot)=0.$$
«In (3.24), U has a non-local dependence on g (see (3.19)), which originates from the
mutual-excitation feature of the Hawkes process» (p. 17). The equation couples $g(t,\lambda)$ to its
values at the $m$ post-jump points $\lambda+\beta_{(l)}$ (p. 23).

### 10. Well-posedness: bounds, existence by Schauder, uniqueness from LQ uniqueness (pp. 17, 30–33)

Lemma 3.1: $\epsilon\le e^{g(t,\lambda(t))}\le1$ and $e^{g(0,\lambda_0)}<1$ (proof App. A via a
sub-martingale argument). Lemma 3.2: (3.24) has a unique solution; existence by Schauder's fixed
point on $\tilde g=e^g$ (B.1), uniqueness by contradiction with the uniqueness of the stochastic LQ
optimal control (Zhang et al. 2020) (App. B, pp. 31–33).

### 11. ⭐ Completing the square gives sufficiency and the frontier depends on one number, $e^{g(0,\lambda_0)}$ (pp. 18–21)

$\tfrac12E[Y(T)\hat X(T)^2]-\tfrac12Y(0)\hat X(0)^2=\tfrac12E\int Y\,\Upsilon^\top\Gamma\Upsilon\,dt$ with
$\Upsilon=\pi+\Gamma^{-1}\hat Z\hat X$ (4.4)–(4.5); sufficiency «is guaranteed by the facts that Y > 0
and Γ is positive definite» (p. 20). Frontier (4.2):
$\mathrm{Var}[X^*(T)]=\frac{e^{g(0,\lambda_0)}}{1-e^{g(0,\lambda_0)}}(x_0e^{rT}-\xi)^2$, $\xi\ge x_0e^{rT}$.
Admissibility is the technical hurdle (Step 3, pp. 20–21).

### 12. Without excitation the PDE collapses to an ODE with a closed-form solution (pp. 21–23)

With $\beta_{lj}=0$, (3.24) becomes $\dot g=B^\top\Gamma_P(\lambda_P(t))^{-1}B$, so
$g(t)=-\int_t^TB^\top\Gamma_P(\lambda_P(s))^{-1}B\,ds$ (4.12), recovering Framstad et al. 2004 and
Shen–Siu 2013 (Cor. 4.1, Remark 4.1). The Hawkes strategy differs from Poisson only through the
nonlocal terms in $U$ (p. 23).

### 13. ⭐ (3.24) has no analytic solution; it is solved by an exponential transform, Feynman–Kac and Monte Carlo on a growing grid (pp. 23–25)

«Equation (3.24) does not have an analytic solution and is difficult to solve numerically as well,
due to the presence of the non-local component» (p. 23). With $\tilde g=e^g$, (B.1) reads
$\tilde g(t,\lambda)=1-E_{t,\lambda}\int_t^T\tilde g\,\hat Z_{\tilde g}^\top\Gamma_{\tilde g}^{-1}\hat Z_{\tilde g}\,ds$;
it is evaluated backwards by simulating $M$ intensity paths per grid point (pp. 23–24). The spatial
grid must grow over time because both the intensity dynamics and the post-jump arguments
$\lambda+\beta$ create new points (Remark 5.1, pp. 24–25).

### 14. Sensitivities (univariate, $m=k=1$): more or more persistent intensity hurts, faster mean reversion helps (pp. 23, 25–26)

Table 1 (p. 23): $r=2\%$, $\mu=9\%$, $\sigma=20\%$, $J=1$, $E[Z]=-2\%$, $E[Z^2]=6\%$, $\alpha=5$,
$\beta=0.1$, $\lambda_\infty=0.48$, $T=2$, $x_0=1$. The frontier deteriorates as $\lambda_0$,
$\lambda_\infty$ or $\beta$ rise and improves as $\alpha$ rises; $\lambda_\infty$ matters more than
$\lambda_0$ (Figs. 2–3, pp. 25–26). $e^{g}$ increases in $t$ and $\lambda$ (Fig. 1, p. 24).

### 15. Hawkes vs Poisson: the ranking depends on $\lambda_0$ versus $\lambda_\infty$; pure self-excitation always worsens the frontier (pp. 26–28)

With $\lambda_P=\lambda_0$, Hawkes is worse if $\lambda_0<\lambda_\infty$ and better if
$\lambda_0>\lambda_\infty$ (Fig. 4); the Hawkes frontiers at $\lambda_0=0.3$ / $0.7$ are «very close»
to Poisson at $\lambda_P=0.47$ / $0.51$ (p. 27). At $\lambda_0=\lambda_\infty$ and $\beta=2$
self-excitation raises terminal variance for every target (Fig. 5, pp. 27–28).

### 16. ⭐⭐ Curse of dimensionality: the two-asset bivariate case could not be computed (pp. 28–29)

Univariate cost ≈ $100\times235\times5000=1.175\cdot10^8$ simulations; for $m=k=2$ with
$\beta_{11}=\beta_{22}=0.1$, $\beta_{12}=\beta_{21}=0.08$ ≈ $100\times300^2\times5000=4.5\cdot10^{10}$
plus a matrix inversion per step. «In fact, the computation is so complex that we cannot even obtain
$e^{g(0,\lambda_0)}$ for a single set of parameter configuration in three days on a personal laptop»
(p. 29). «solving a multi-dimensional partial differential equation with a non-local component
remains an open question to our knowledge» (p. 29).

### 17. SMP and HJB give the same solution: the value function is $e^{2r(T-t)+g(t,\lambda)}x^2$ (App. C, pp. 33–35)

Ansatz $V(t,x,\lambda)=e^{2r(T-t)+\kappa(t,\lambda)}x^2$, $\kappa(T,\cdot)=0$; the jump part of the
generator moves wealth and intensity **simultaneously**,
$\phi(t,x+(\pi^\top\eta(z))_{(j)},\lambda+\beta_{(j)})$ (p. 34); the first-order condition gives
$\pi=-\Gamma_\kappa^{-1}\hat Z_\kappa x$ and (C.3) is identical to (3.24), so $\kappa=g$ (p. 35). The
adjoint is $p=V_x$ (p. 35).

### 18. Future direction: non-exponential (non-Markovian) Hawkes via SMP/BSDE (p. 29)

«An interesting future research direction is to consider non-Markovian Hawkes processes with
non-exponential decay functions. In that case, the HJB equation approach will not be applicable,
while the stochastic maximum principle together with BSDEs still works» (p. 29).

## What this source does not address

- **Market making / point-process fills.** The control scales jump sizes; there are no quotes, no
  fill probabilities $f(\delta)$, no inventory jumps of controlled probability.
- **Control-dependent intensities.** Excluded by the price-taker assumption (p. 9).
- **Non-exponential kernels, stationarity / spectral-radius conditions.** Only exponential decay;
  no condition on $\rho(\beta\alpha^{-1})$ is stated (finite horizon).
- **Utility objectives (CARA etc.), time-consistent MV.** Only precommitted MV.
- **Any computed multivariate result.** The $m=k=2$ case is shown to be infeasible with their
  method (p. 29); no approximation (e.g. frozen intensity, quadratic-in-λ expansion) is tried.
- **Empirical estimation.** Parameters are taken from Aït-Sahalia et al. 2015 and Liu et al. 2021
  (p. 23); no fit.

## Model card

- **Assets:** $k$ risky assets + 1 riskless; numerics only $k=1$.
- **Kernel:** exponential Hawkes (Markov in $\lambda$), $m$ components.
- **Excitation:** self and cross between Hawkes components; cross-asset through $\beta$ and the
  loading matrix $J$.
- **Who excites the flow:** exogenous price-jump events; the control does not affect any intensity
  (price-taker, p. 9). n/a in the fill-/flow-driven sense — there are no orders.
- **Objective:** precommitted mean-variance on terminal wealth (2.13).
- **Solution method:** stochastic maximum principle + BSDE + completing the square; semi-closed form
  subject to a nonlocal PDE (3.24), solved by Feynman–Kac Monte Carlo.
- **Benchmark:** Poisson jump-diffusion (Cor. 4.1).
- **Reported numbers:** frontiers only (Figs. 2–5), no regret; Hawkes $\lambda_0=0.3/0.7$ ≈ Poisson
  $\lambda_P=0.47/0.51$; bivariate case not computable in 3 days (p. 29).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

*Read as a non-market-making source: what its control machinery says about the closures.*

**Carries Kernthesen 1, 2, 4, 7, 8, 9, 10, 12, 13, 16, 17.**

### What this focus needs beyond the Kernthesen

1. **Does the control affect the intensities? No.** The intensity SDE (2.3) has no control; the
   investor «does not move the prices» (p. 9). The control enters only the *size* of each jump of
   the controlled state ($\pi^\top\eta(z)$), linearly. Every Hawkes event moves the state and the
   intensity at the same instant (App. C, p. 34). In the project's language this is closest to
   **exogenous, flow-driven excitation with a deterministic (control-scaled) state jump at each
   event** — there is no "unfilled" event and no controlled jump probability.
2. **Why the quadratic closure is exact here [I].** Three ingredients make the state-quadratic ansatz
   close without approximation: linear state dynamics, a quadratic terminal loss, and a control
   that enters the jump linearly. The intensity never has to be expanded: it stays a full state
   variable, and the price is a scalar coefficient $P(t,\lambda)=e^{2r(T-t)+g(t,\lambda)}$ that solves
   a nonlocal equation in $\lambda$. This is structurally the outcome §3a of [[problem-anatomy]]
   predicts for the flow-driven BEGV ansatz ($A,B,C$ functions of $\lambda$, nonlocal through
   $A(\lambda^{+j})$). The market-making case needs the [[hamiltonian-quadratic-approximation]] first
   to reach LQ form; Shen–Zou start from an LQ problem.
3. **The equation for the coefficient is Riccati-type, written out [D].** With $\tilde g=e^g$ the
   left side of (3.24) times $\tilde g$ is the generator of $\lambda$:
   $e^g(g_t+g_\lambda^\top\alpha(\lambda_\infty-\lambda)+U^\top\lambda)=\partial_t\tilde g+\mathcal A\tilde g$, with
   $\mathcal A\tilde g=\sum_l[\alpha_l(\lambda_{l\infty}-\lambda_l)\partial_l\tilde g+\lambda_l(\tilde g(\lambda+\beta_{(l)})-\tilde g(\lambda))]$. So
   $$(\partial_t+\mathcal A)\tilde g=(\tilde g\hat Z)^\top(\tilde g\Gamma)^{-1}(\tilde g\hat Z),$$
   where $\tilde g\Gamma=\tilde g\,\sigma\sigma^\top+\int\eta\,\mathrm{Diag}[\tilde g(\lambda+\beta_{(\cdot)})\bullet\lambda\bullet\nu]\eta^\top$ and
   $\tilde g\hat Z=\tilde gB+\int\eta\,\mathrm{Diag}[\lambda\bullet\nu](\tilde g(\lambda+\beta_{(\cdot)})-\tilde g(\lambda))$ are
   **linear** in the values of $\tilde g$ at $\lambda$ and at the post-jump points. The right side is
   $-\inf_\pi[2\pi^\top(\tilde g\hat Z)+\pi^\top(\tilde g\Gamma)\pi]$, i.e. the LQ "$-b^\top a^{-1}b$" term.
   Scalar case ($k=m=1$, $m_1=E[JZ]$, $m_2=E[(JZ)^2]$, $\tilde g^+=\tilde g(\lambda+\beta)$):
   $$(\partial_t+\mathcal A)\tilde g=\frac{\big(B\tilde g+\lambda m_1(\tilde g^+-\tilde g)\big)^2}{\sigma^2\tilde g+\lambda m_2\tilde g^+}.$$
   The nonlinearity is the Riccati quotient; the nonlocality is $\tilde g^+$ inside it. With
   $\beta=0$ we get $\tilde g^+=\tilde g$ and the equation becomes the scalar ODE of Remark 4.1.
   *This rewrite is the project's; to be re-derived before use (proposal p. 21 rule).*
4. **Where it breaks: dimension, not closure.** The closure in the state holds for every $m,k$;
   what fails is solving the $m$-dimensional nonlocal PDE (Kernthese 16). That is the same object
   the project's D2 produces, and Shen–Zou are a measured data point that brute-force Feynman–Kac
   on a grid already fails at $m=2$ (p. 29). A frozen-forecast route ([[volterra-riccati]],
   [[intensity-forecast]]) or a finite-regime approximation is not tried by the authors.
5. **What carries over to several assets with cross-asset excitation [I].** (a) Cross-excitation
   enters the coefficient equation only through the post-jump points $\lambda+\beta_{(l)}$: an off-
   diagonal $\beta_{jl}$ moves the argument in direction $j$ when $l$ jumps, exactly the structure a
   cross-asset kernel would give in market making. (b) Here the state is scalar wealth, so the
   coefficient is scalar even with $k$ assets; in market making the state is the inventory vector
   $q\in\mathbb R^d$, so the analogue would be a $d\times d$ matrix $A(t,\lambda)$ with
   $A(\lambda+\beta_{(l)})$ inside a nonlocal matrix Riccati system. Shen–Zou do **not** treat a
   vector state; the literature guide's statement that the $d\times d$ inventory-matrix version
   «was not found» stands. (c) The positivity argument (Lemma 3.1, $Y>0$, $\Gamma\succ0$) has a
   matrix analogue only if $A(t,\lambda)\succeq0$ is preserved, which would need its own proof.
6. **Closure classes.** Linear ODE: only without excitation (Remark 4.1). Quadratic-Riccati: holds
   exactly in the state, nonlocal in $\lambda$. Lift: the exponential kernel is its own one-factor
   lift per component ([[markov-lift]]); non-exponential kernels are left to SMP/BSDE (p. 29).

### Direct quotes (for the draft)

> "In (3.24), U has a non-local dependence on g (see (3.19)), which originates from the mutual-excitation feature of the Hawkes process." (p. 17)

> "It is important to notice that, with the ansatz of Y and V in (3.16) and (3.17), Γ and Ẑ defined above are indeed functions of t and λ only, and are independent of Y and V." (p. 16)

> "We consider a representative agent (investor), who is a price-taker in the economy (i.e., her trading does not move the prices of the assets)." (p. 9)

> "Equation (3.24) does not have an analytic solution and is difficult to solve numerically as well, due to the presence of the non-local component." (p. 23)

> "In fact, the computation is so complex that we cannot even obtain e^{g(0,λ0)} for a single set of parameter configuration in three days on a personal laptop […]. This is not entirely surprising though, as solving a multi-dimensional partial differential equation with a non-local component remains an open question to our knowledge, and there are no universally efficient numerical methods to tackle such a problem." (p. 29)

### Examples & illustrations (for later drafting)

- Fig. 1 (p. 24): $e^{g(t,\lambda)}$ over $(t,\lambda)\in[0,2]\times[0.1,2]$, range ≈ 0.85–1, increasing in
  both — a picture of an intensity-dependent Riccati coefficient.
- Remark 5.1 (pp. 24–25): the grid must grow because the coefficient at $\lambda$ needs its value at
  $\lambda+\beta$ — a concrete illustration of what "nonlocal in $\lambda$" costs.
- Remark 5.2 (pp. 28–29): 1.175·10⁸ vs 4.5·10¹⁰ simulations, univariate vs bivariate — the
  dimensionality argument in one line.

### Boundary of this focus

Shen–Zou is a portfolio problem: no fills, no quotes, no controlled jump probabilities. Everything
said here about market making, D2 and $d\times d$ inventory matrices is the project's analogy
([I]/[D]), not a claim of the source. The source proves the closure for an LQ problem with a scalar
state; it says nothing about a quadratic *approximation* of a non-quadratic Hamiltonian.

## Focus: Perturbative/asymptotic closed forms for multi-asset market making with a stochastic intensity factor (Hawkes or Markov-modulated): which expansion, around which point, with which small parameter and error order; whether it closes into finite matrix ODEs; how accuracy is tested; how much of Stage 2a it already covers. — 2026-10-26

**Carries Kernthesen 4, 7, 9, 12, 13, 16, 17.**

### What this focus needs beyond the Kernthesen

1. **Which expansion?** None. The authors solve (3.24) exactly (existence by Schauder, App. B) and
   numerically (Feynman–Kac Monte Carlo, §5.1). There is no small parameter, no asymptotic order and
   no truncation (Kernthese 13).
2. **Does an exponential-affine ansatz close (3.24) exactly? No, in general.** The
   source's own claim is only «Equation (3.24) does not have an analytic solution» (p. 23). The
   reason below is the project's derivation [D]. Put $g=a(t)+b(t)^\top\lambda$. Then
   $U_l=e^{b^\top\beta_{(l)}}-1$ no longer depends on $\lambda$, and the left side of (3.24) is affine in
   $\lambda$. But the right side is $(B+L\lambda)^\top(S_0+\sum_l\lambda_lS_l)^{-1}(B+L\lambda)$:
   (3.20)–(3.21) make $\hat Z$ affine and $\Gamma$ affine in $\lambda$, so the right side is a
   *rational* function of $\lambda$. Scalar case:
   $\frac{(B+\lambda m_1u)^2}{\sigma^2+\lambda m_2(u+1)}$. Matching fails unless the case is
   degenerate. With no jumps ($\eta=0$) or no excitation ($\beta=0$) $g$ depends on $t$ only
   (Remark 4.1). With $\sigma=0$ and $B=0$ the scalar right side is
   $\lambda m_1^2u^2/(m_2(u+1))$, so an affine $g$ closes with a scalar ODE for $b$. That case has
   no Brownian risk and no risk premium.
3. **Would it transfer to market making? No [I].** In market making $\lambda_j$ multiplies a
   Hamiltonian in $p_j$, and $p_j$ is linear in $q$ with coefficients from $A(t,\lambda)$ at the
   post-jump point. Even with BEGV's quadratic Hamiltonian, an ansatz with $A$ affine in $\lambda$
   produces $\lambda_j\,h_2\,(A\text{-terms})^2$. That is cubic in $\lambda$, so a finite polynomial
   ansatz does not close. The exact exponential Hamiltonian is worse. Closure therefore needs a
   truncation in $\lambda-m_t$, which is Stage 2a's route. Shen–Zou's exact *state*-quadratic
   closure holds because the control scales jump *sizes* linearly and never multiplies the intensity
   (Kernthese 4).

### Overlap with Stage 2a

| Element | Verdict | Evidence |
|---|---|---|
| (a) multi-asset matrix Riccati with a stochastic intensity factor | **partly** | Quadratic value with coefficient $e^{2r(T-t)+g(t,\lambda)}$ (App. C, p. 34). $k$ assets, but the state is scalar wealth, so the coefficient is scalar, not a $d\times d$ inventory matrix. |
| (b) perturbative/asymptotic expansion in the factor | **not** | «does not have an analytic solution and is difficult to solve numerically as well» (p. 23); solved by Monte Carlo. |
| (c) order-1 system linear given order 0 | **not** | no orders. |
| (d) explicit small parameter + error order | **not** | none. |
| (e) accuracy test | **not** (no approximation to test) | numerics compare Hawkes with Poisson frontiers (Figs. 4–5, pp. 27–28). The bivariate case could not be computed (p. 29). |
| (f) cross-asset coupling of the factor | **covered (structure)** | «U has a non-local dependence on g … which originates from the mutual-excitation feature» (p. 17); off-diagonal $\beta_{jl}$ moves the post-jump argument $\lambda+\beta_{(l)}$. |

### What this changes for Stage 2a [I]

Nothing in the design. It strengthens the motivation: exact $\lambda$-dependent coefficients give a
nonlocal PDE with no affine closure even in an LQ problem. That PDE could not be computed at $m=2$
(p. 29). A first-order expansion around $m_t$ is the natural escape and is not tried here.

### Direct quotes (for the draft)

> "In (3.24), U has a non-local dependence on g (see (3.19)), which originates from the mutual-excitation feature of the Hawkes process." (p. 17)

> "Equation (3.24) does not have an analytic solution and is difficult to solve numerically as well, due to the presence of the non-local component." (p. 23)

### Boundary of this focus

The source only claims that no analytic solution exists. The affine-ansatz test, the degenerate
closed case and the market-making transfer are all the project's derivations, and must be re-derived
before use.

## Mentioned entities

- Concepts: [[hawkes-process]], [[branching-matrix]], [[markov-lift]], [[matrix-riccati-equation]], [[hamiltonian-quadratic-approximation]], [[volterra-riccati]], [[intensity-forecast]], [[who-excites-the-flow]]
- Synthesis: [[problem-anatomy]]
- Other works (bibkeys): [[aitsahalia-2016-portfolio-choice-markets]], `zhang-2020-backward-stochastic-riccati` (LQ uniqueness used in App. B), `hawkes-1971-spectra-self-exciting`, `bacry-2015-hawkes-processes-finance`, `errais-2010-affine-point-processes`. Cited but not in the library: Aït-Sahalia–Cacho-Diaz–Laeven 2015 (parameters, contagion evidence), Zhou–Li 2000 and Lim–Zhou 2002 (MV/LQ embedding), Framstad–Øksendal–Sulem 2004 (sufficient SMP with jumps), Gao–Zhou–Zhu 2018 (non-Markovian Hawkes), Cao et al. 2020 and Liu et al. 2021 (Hawkes HJB in insurance / household problems).

## Connections

- Builds on: [[aitsahalia-2016-portfolio-choice-markets]] (same Hawkes jump-diffusion market; HJB/utility there, SMP/MV here).
- Supports (by analogy, not cited): [[problem-anatomy]] §3a — quadratic ansatz closes in the state, coefficient nonlocal in $\lambda$; [[matrix-riccati-equation]] — a λ-dependent Riccati coefficient outside market making.
- Compare: [[begv-2021-model]] (state-quadratic closure with constant intensities; here the intensity is a state); [[barzykin-2026-hawkes-driven-otc]] (avoids the nonlocal λ-equation by freezing the forecast); [[bergault-2024-price-aware-automated]] (finite-regime escape route).
