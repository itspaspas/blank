---
title: "Rosenbaum & Zhang 2022 — Multi-asset market making under the quadratic rough Heston"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: rosenbaum-2022-multi-asset-market
depth: standard
tags: [market-making, multi-asset, rough-volatility, quadratic-rough-heston, spx-vix, options-market-making, quadratic-hamiltonian, large-tick, limit-order-book, asymptotic-riccati, frozen-factor]
relations:
  - target: bergault-2021-closed-form-approximations
    type: builds-on
    confidence: extracted
    because: "«Here we follow the idea of [6] that is approximating the Hamiltonian functions H^{j,k}(·) with quadratic ones … most of the development in this part follows the same methodologies as in [6]» (pp. 8–9); [6] = BEGV 2021. The asymptotic A, B are BEGV's T→∞ formulas with D_± built from the binary-control Hamiltonian."
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "Proposes a quadratic surrogate Ĥ^{j,k}(p)=Λ^{j,k}(α^j p²/2 − p + D^j/2) matching value and slope at 0 of a non-smooth (indicator) Hamiltonian, because «Taylor expansions … Clearly this do not apply for (3.4)» (p. 9). Extends the concept to non-C² Hamiltonians."
  - target: matrix-riccati-equation
    type: cites
    confidence: extracted
    because: "v̂(t,q)=−qᵀA(t)q−qᵀB(t)−C(t) with A, B, C «given by the unique solution of a system of ODEs» (p. 9); only the T→∞ limit A(0)→(σ/2)√κ Γ is written out."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "Applies the BEGV quadratic-Hamiltonian closed form to a large-tick, binary-quote (join best limit or not) setting on SPX and SPX/VIX derivatives (pp. 3, 8–9)."
  - target: volterra-riccati
    type: mentions
    confidence: inferred
    because: "The Volterra (rough) kernel sits in the volatility of the underlying, not in order flow, and is frozen before the control problem is solved (Approximation 3.1, p. 6); no Volterra–Riccati appears."
---

# Multi-asset market making under the quadratic rough Heston

## Bibliographic Details

Rosenbaum, Mathieu; Zhang, Jianfei. 2022. *Multi-asset market making under the quadratic rough
Heston*. arXiv:2212.10164v1 [q-fin.MF], 20 December 2022 (dated 21 December 2022 on p. 1). 20 pp.
Affiliations: École polytechnique, CMAP (both); Exoduspoint Capital Management (Zhang).
Citation key `@rosenbaum-2022-multi-asset-market`.

**Read: arXiv 2212.10164v1 (preprint); page/equation numbers follow it.** Printed page numbers
coincide with physical PDF pages. Non-core work; preprint accepted under the project's preprint
policy. Whether a journal version exists was not verified (see report) — no `based_on` set.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $d$ | number of traded assets (SPX + derivatives) | $d$ |
| $S_t$, $V_t=a(Z_t-b)^2+c$ | SPX price and spot variance (QRH) | $S_t$; $\sigma_t=S_t\sqrt{V_t}$ is the **price** volatility of SPX |
| $Z_t=\sum_i c_i Z^i_t$, $(c_i,\gamma_i)$ | multi-factor (sum-of-exponentials) Markov approximation of the fractional kernel (eq. 2.1) | ⚠ $\gamma_i$ is a kernel decay, **not** risk aversion $\gamma$ |
| $\delta^j_t=\partial P^j/\partial S+\sum_i\partial P^j/\partial Z^i\cdot(\ldots)$ | sensitivity of asset $j$ to SPX ("Delta", $dP=\delta\,dS$) | ⚠ **not** a quote $\delta^b,\delta^a$ |
| $l^{j,b},l^{j,a}\in\{0,1\}$ | binary control: post a limit order at the best limit or not | replaces the continuous quotes $\delta^{b},\delta^{a}$ |
| $\Lambda^{j,k}$ | constant execution intensity (also called «execution probability», p. 5) | not the GLFT amplitude $\Lambda e^{-k\delta}$; constant, no Hawkes |
| $m^j$, $D^j$, $Q^j$ | order size, tick size, inventory bound | $Q$ |
| $\kappa_j$, $\kappa$ | asset-level and portfolio-level inventory penalties (eq. 2.3) | $\approx\gamma$ in the risk-adjusted objective |
| $q$, $Y_t$, $\Pi_t$ | inventory, cash, mark-to-market value | $q_t$, $X_t$ |
| $H^{j,k}(p)$, $\hat H^{j,k}(p)$, $\alpha^j$ | exact (indicator) and quadratic surrogate Hamiltonian (3.4), (3.6) | $H^{i,s}$; $\alpha^j$ plays the role of $h_2=H''(0)$ |
| $\hat v=-q^\top Aq-q^\top B-C$ | approximate value function | identical to project ansatz $\theta$ (no $\lambda$-dependence) |
| $\phi^k=\pm1$ | side sign ($b=+1$, $a=-1$) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction: QRH model (eq. 1.1), Zumbach effect, literature (GLFT, BEGV, Baldacci options MM), large-tick binary quoting, the two dimensionality sources | 1–4 |
| ✓ F1 | 2.1 Multi-factor approximation of QRH (2.1); derivative prices as $P(t,X)$, $X=(S,Z^1,\ldots,Z^n)$; pricing PDE (2.2) | 4–5 |
| ✓ F1 | 2.2 Multi-asset market making: binary limit-order control, inventory/cash dynamics, objective (2.3), value function $u$ with $2+n+d$ variables | 5–6 |
| ✓ F1 | 3.1 HJB: Approximation 3.1 (freeze $Z$, $\delta$, $V$); reduced value $v(t,q)$ (3.1); HJB (3.2)–(3.4); Thm. 3.1 (existence), Thm. 3.2 (optimal controls); Remark 3.1 (net-risk reduction to one variable $r$, eq. 3.5) | 6–8 |
| ✓ F1 | 3.2 Quadratic approximation: surrogate Hamiltonian (3.6); quadratic $\hat v$; $T\to\infty$ asymptotics of $A$, $B$; greedy affine-hyperplane decisions; Remark 3.2 | 8–10 |
| ✓ F1 | 4.1 Daily hedging with SPX (Figs. 4.1–4.2) | 10–11 |
| ✓ F1 | 4.2.1 Example 1 (SPX + VIX future): grid vs. asymptotic $\hat v$, backtest (Figs. 4.3–4.7) | 11–14 |
| ✓ F1 | 4.2.2 Example 2 (four options, net risk only) (Figs. 4.8–4.9) | 14–17 |
| ✓ F1 | 4.3 Example 3 (six assets, online recalibration vs. uni-asset) (Fig. 4.10) | 16–18 |
| — | References | 19–20 |

## Kernthesen

### 1. ⭐ The QRH model makes all SPX-derivative risk one-dimensional: every price change is a multiple of $dS$ (pp. 2, 4)

Under QRH, $dS_t=S_t\sqrt{V_t}dW_t$, $V_t=a(Z_t-b)^2+c$, with a single Brownian motion; «the dynamic of
the volatility can be fully explained by past returns» (p. 2). With the multi-factor approximation,
derivative prices are functions $P(t,X)$ and $dP(t,X)=\delta_t\,dS_t$ (p. 4). Hence «the principal
inventory risk is summarized by the sensitivities of their price change with respect to that of SPX»
(p. 3). Cross-asset risk is perfectly correlated through one factor; the covariance is rank one plus
asset-specific penalty terms.

### 2. ⭐ The rough kernel is made Markov by a sum of exponentials, adding $n$ state variables (p. 4)

$K(t)=\nu t^{\alpha-1}/\Gamma(\alpha)$ is replaced by $K^n(t)=\sum_{i=1}^n c_ie^{-\gamma_it}$, giving
$dZ^i_t=(-\gamma_iZ^i_t-\lambda\sum_ic_iZ^i_t)dt+\nu\sqrt{V_t}dW_t$ (2.1), with $(c_i,\gamma_i)$ explicit
functions of $(\alpha,\nu)$, not free parameters (p. 4). The tests use $n=10$ (p. 11). This is the same
lifting device the project uses for power-law Hawkes kernels ([[markov-lift]]), but here applied to
volatility, and its state is then frozen (Kernthese 4).

### 3. ⭐⭐ Large-tick quoting: the control is binary (join the best limit or not), intensities are constant (pp. 3, 5)

«The quoting strategy … consists in whether to send limit orders on the two best limits given its
portfolio inventory … instead of choosing the optimal quoting price» (p. 3), «in the spirit of» Guilbaud–Pham
(p. 3). $\lambda^{j,k}_t=l^{j,k}_t\Lambda^{j,k}\mathbb 1_{\{q^j\pm m^j\in\mathcal Q^j\}}$ with constant
$\Lambda^{j,k}$; «We do not differentiate the queue positions of the orders» (p. 5). Order flow has no
memory, no excitation, no stochastic intensity.

### 4. ⭐⭐ The stochastic factor is frozen, not expanded: Approximation 3.1 (pp. 6–7)

«We approximate $(Z^i_t)$ and $(\delta^j_t)$ by its initial value» and replace SPX by arithmetic Brownian
motion $dS_t=\mu dt+\sigma dW_t$, $\sigma=S_0\sqrt{V_0}$ (p. 6). Justification is horizon-based:
«relevant when the time horizon of the problem is relatively short» (p. 7); in practice «the market
maker can always reset the algorithm with updated parameters» (p. 7). The value function collapses
from $2+n+d$ to $1+d$ variables, $u(t,S,Z,q)=v(t,q)$ (p. 7). No error estimate for this freezing is
given; it is supported empirically by daily hedging (§4.1).

### 5. The reduced problem has a unique bounded solution and threshold controls (pp. 7–8)

HJB (3.2) with $H^{j,k}(p)=\Lambda^{j,k}\mathbb 1_{\{p\le D^j/2\}}(D^j/2-p)$ (3.4). Thm. 3.1: unique $C^1$-in-time
solution, by Cauchy–Lipschitz plus a supersolution bound $\sup_qv\le\sum_j(H^{j,b}(0)+H^{j,a}(0)+|\mu\delta^j|Q^j)(T-t)$
(p. 8), «following the same steps as in [19]» (Guéant 2017). Thm. 3.2: post at side $k$ iff the
inventory stays admissible and $(v(t,q)-v(t,q+\phi^km^je^j))/m^j\le D^j/2$ (p. 8).

### 6. Controlling only portfolio net risk reduces the state to one scalar (p. 8)

Remark 3.1: with $\kappa_j=0$ and $Q^j\to\infty$, the state is $r_t=\sum_jq^j_t\delta^j$ and the HJB is
one-dimensional in $r$ (3.5). This is what makes the four-asset grid benchmark of Example 2 feasible.

### 7. ⭐⭐ The surrogate Hamiltonian for a non-smooth $H$: match value and slope at 0, choose curvature $\alpha^j\sim1/D^j$ (p. 9)

BEGV's Taylor expansion fails because (3.4) is not $C^2$: «Clearly this do not apply for (3.4)» (p. 9).
Proposal (3.6): $\hat H^{j,k}(p)=\Lambda^{j,k}(\frac{\alpha^j}2p^2-p+\frac{D^j}2)$ with
$\hat H(0)=H(0)$, $\hat H'(0)=H'(0)$, and «We can choose $\alpha^j\sim\frac1{D^j}$ to make $\hat H^{j,\cdot}$
close to $H^{j,\cdot}$ around 0» (p. 9). The tests use $\alpha^j=1/(4D^j)$ (p. 12). The curvature is a
**tuning choice**, not derived; no criterion for optimality of $\alpha$ is given.

### 8. ⭐⭐ "Asymptotic closed form" = the $T\to\infty$ limit of BEGV's matrix Riccati, nothing else (p. 9)

With $Q^j=+\infty$, «following the same computations as in [6]», $\hat v(t,q)=-q^\top A(t)q-q^\top B(t)-C(t)$
with $A,B,C$ from «a system of ODEs» (not written). «Since we are more interested in the behavior of
$\hat v$ as $T\to+\infty$, we focus mostly on the asymptotic formulas of $A$ and $B$» (p. 9):
$A(0)\xrightarrow{T\to\infty}\frac\sigma2\sqrt\kappa\,\Gamma$,
$\Gamma=D_+^{-1/2}(D_+^{1/2}\Sigma D_+^{1/2})^{1/2}D_+^{-1/2}$,
$\Sigma=\mathrm{diag}(\kappa_j(\delta^j)^2/\kappa)+\delta\delta^\top$,
$D_+=\mathrm{diag}((\Lambda^{j,b}+\Lambda^{j,a})\alpha^jz^j)$, and $B(0)$ by a Moore–Penrose formula
involving $\mu$, $D_-$, $V_-$ (p. 9). The expansion "parameter" is the horizon $T$; there is no small
parameter, no order, no error bound. ($z^j$ is undefined in the text; context suggests $m^j$ — see notes.)

### 9. Greedy decisions from $\hat v$ are separated by an affine hyperplane in inventory space (pp. 9–10)

$\tilde l^{j,k*}(q)=\mathbb 1_{\{\ldots,\,2\phi^k(e^j)^\top Aq+m^j(e^j)^\top Ae^j+\phi^k(e^j)^\top B\le D^j/2\}}$ (p. 9);
in the net-risk case $\tilde l^{j,k*}(r)=\mathbb 1_{\{2Dr\delta^j+(\delta^j)^2m^j\le D^j/2\}}$ with
$D=\frac\sigma2\sqrt{\kappa/(2\sum_j(\delta^j)^2\Lambda^jm^j\alpha^j)}$ (p. 10) — a one-line scalar rule.

### 10. ⭐ Closed form is valued for online recalibration, not for accuracy per se (pp. 3, 16)

«Having closed-form approximate solutions makes the recalibration of the algorithm very efficient,
and thus it is even possible to design an "online" market making algorithm» (p. 3). Example 3 updates
$(\delta^j)$ and $\sigma$ every 100 s from the running QRH state (p. 16). This is the paper's actual answer
to the stochastic factor: **re-freeze periodically** (piecewise-constant parameters), not expand.

### 11. Daily Delta-hedging with QRH tracks market prices of SPX call, VIX call, VIX future (pp. 10–11)

Two 2017 experiments (Figs. 4.1–4.2): «the hedging portfolios can follow well the market price's
evolution with daily rebalancing for all assets», which «verifies the rationality of Approximation 3.1
over the time horizon of the considered market making problem» (p. 10). Note this tests the hedge,
not the market-making value function under a moving factor.

### 12. ⭐ Accuracy of $\hat v$: visual comparison with the Euler-grid solution and mean–std backtests (pp. 12–16)

Example 1 ($d=2$, SPX + VIX future, $T=300$ s): $\hat v(0,q)$ «is very close to that of $v(0,q)$»
(Fig. 4.5, with $C(0)$ shifted to match maxima) and greedy decisions «very similar» (p. 12). Backtest
with $\kappa\in[10^{-4},1]$, $N=5000$ paths, $T_b=T/2$: «slight deviations … the global mean-risk
profile of its performance is not significantly degraded» (p. 13; Fig. 4.7). Example 2 ($d=4$ options,
net risk, $T=600$ s): same conclusion (Figs. 4.8–4.9). Benchmarks are the exact solution of the
**frozen** HJB (3.2)/(3.5). No numerical regret or gap figure is reported; results are plots only.

### 13. Portfolio-level risk mutualisation beats asset-by-asset market making (pp. 16–18)

Example 3 (six assets, $T_b=2000$ s): multi-asset strategy with periodic recalibration vs. $\kappa=0$
uni-asset grid strategies summed; «Clearly, the performance of uni-asset market making is suboptimal»
(p. 16; Fig. 4.10).

### 14. Extensions claimed without proof: deeper limits (Remark 3.2, p. 10)

«The problem can be easily extended to cover other limits … a closed-form asymptotic solution can be
obtained in a similar manner» (p. 10). Not carried out.

## What this source does not address

- **Stochastic or self-exciting order flow.** Execution intensities $\Lambda^{j,k}$ are constants (p. 5);
  no Hawkes, no Markov-modulated intensity, no cross-asset flow coupling.
- **Any expansion around a stochastic factor.** The factor (QRH $Z$, hence $V$, $\delta$) is frozen at its
  initial value (Approximation 3.1, p. 6), with no perturbative correction and no error order.
- **Explicit finite-$T$ Riccati system.** Only stated to exist (p. 9); not written down.
- **Quantitative accuracy metrics.** No regret, no relative value gap; plots only (pp. 12–18).
- **CARA utility.** Risk-adjusted objective only; CARA equivalence deferred to Guéant 2017 (p. 6).
- **Continuous quotes / fill-probability curves.** Binary best-limit participation only.

## Model card

| Field | Value |
|---|---|
| Assets | $d$ (SPX + VIX futures, SPX and VIX options); tests with $d=2,4,6$ (pp. 11–16) |
| Kernel | n/a — order flow is Poisson with constant intensities $\Lambda^{j,k}$ (p. 5). (A sum-of-exponentials kernel exists, but in the *volatility* model, eq. 2.1, and is frozen.) |
| Excitation | none in order flow; cross-asset coupling only through the common SPX risk factor $\delta\delta^\top$ in $\Sigma$ (p. 9) |
| Who excites the flow | n/a — flow is not excited; the maker's binary participation gates fills (p. 5) |
| Objective | risk-adjusted: $\mathbb E[\Pi_T]-\sum_j\frac{\kappa_j}2\int\sigma^2(q^j\delta^j)^2-\frac\kappa2\int\sigma^2(\sum_jq^j\delta^j)^2$ (eq. 2.3) |
| Solution method | closed form (quadratic-Hamiltonian surrogate à la BEGV, $T\to\infty$ asymptotics of $A,B$) after freezing the stochastic-volatility state; exact benchmark by Euler scheme on the inventory grid (pp. 9, 12, 15) |
| Benchmark | Euler-grid solution of the frozen HJB (3.2)/(3.5); uni-asset grid strategies (Ex. 3) |
| Reported regret or gap numbers | none numeric — mean/std frontier plots (Figs. 4.7, 4.9, 4.10) and value-function overlays (Figs. 4.5, 4.8) only |

<!-- ═══ FOKUS ═══ -->

## Focus: Perturbative/asymptotic closed forms for multi-asset market making with a stochastic intensity factor (Hawkes or Markov-modulated): which expansion, around which point, with which small parameter and error order; whether it closes into finite matrix ODEs; how accuracy is tested; how much of Stage 2a it already covers. — 2026-10-26

**Carries Kernthesen 3, 4, 7, 8, 10, 12.**

### What this focus needs beyond the Kernthesen

1. **Which expansion, around which point, which parameter, which error order.** Two distinct
   approximations, neither perturbative in a stochastic factor:
   - *Freezing* (Approximation 3.1, p. 6): the stochastic-**volatility** state $(Z,\delta,V)$ is set to its
     time-0 value. This is the zeroth-order term of a would-be expansion in the factor, with **no
     higher orders and no error estimate**; the justification is a short horizon (p. 7).
   - *Quadratic Hamiltonian surrogate* (3.6, p. 9): not a Taylor expansion (impossible for the
     indicator $H$), but a moment-matching quadratic with free curvature $\alpha^j$. No error order.
   - *"Asymptotic"* (p. 9) refers to $T\to+\infty$ of the BEGV Riccati solution — a long-horizon limit,
     not an asymptotic expansion in a small parameter.
2. **Closure into finite matrix ODEs.** Yes, but trivially: after freezing, the system is BEGV's
   constant-coefficient $d\times d$ Riccati for $A$, linear ODE for $B$, scalar for $C$ (p. 9). The factor
   never enters the ODEs as a state variable; there is no $A(t,\lambda)$ or $A(t,Z)$.
3. **How accuracy is tested.** Against the exact (Euler-grid) solution of the *frozen* problem, by
   value-function overlay and mean–std backtests on 5000 simulated paths (pp. 12–16). Only Example 3
   lets the factor move (recalibration every 100 s), and it compares against uni-asset strategies,
   not against an exact solution of the unfrozen problem. So the error from freezing the factor is
   never measured inside the control problem.
4. **Stochastic factor ≠ intensity factor.** The stochastic factor here drives *price volatility and
   Deltas* (risk), not *order-arrival intensity* (liquidity). In Stage 2a's terms, it would enter the
   running penalty ($\Sigma$) rather than the Hamiltonian terms ($D_+$). Even if expanded, it would act
   on a different block of the Riccati.

### Overlap with Stage 2a

| Element | Verdict | Evidence |
|---|---|---|
| (a) multi-asset matrix Riccati with a stochastic intensity/liquidity factor | **not** (multi-asset Riccati: yes; stochastic factor: volatility, frozen; intensities constant) | «We approximate $(Z^i_t)$ … and $(\delta^j_t)$ … by its initial value» (p. 6); $\Lambda^{j,k}$ constant, «constant execution probability» (p. 5) |
| (b) perturbative/asymptotic expansion in that factor | **not** — zeroth-order freezing only; "asymptotic" means $T\to\infty$ | «we focus mostly on the asymptotic formulas of $A$ and $B$» as $T\to+\infty$ (p. 9) |
| (c) order-1 system linear given order 0 | **not** — no order-1 system exists | — (no correction beyond Approximation 3.1, pp. 6–9) |
| (d) explicit small parameter + error order | **not** — justification is qualitative («relatively short» horizon) | «The above approximation is relevant when the time horizon of the problem is relatively short» (p. 7) |
| (e) accuracy test against exact/numerical solution | **partly** — yes against the grid solution of the *frozen* HJB, plots only, no numeric gap; freezing error untested | «Its shape is very close to that of $v(0,q)$» (p. 12); «the global mean-risk profile … is not significantly degraded» (p. 13) |
| (f) cross-asset coupling of the factor | **partly** — one common factor (SPX) couples all assets via $\Sigma=\mathrm{diag}(\cdot)+\delta\delta^\top$, but in risk, not in intensity | «the principal inventory risk is summarized by the sensitivities of their price change with respect to that of SPX» (p. 3); $\Sigma$ (p. 9) |

**Net verdict: Stage 2a is not pre-empted.** This paper is a BEGV application (binary-control
Hamiltonian surrogate + $T\to\infty$ Riccati) with a frozen, periodically recalibrated volatility
factor. Its "periodic re-freeze" (Kernthese 10) is the natural **baseline** Stage 2a's order-1
correction must beat: the order-0 Stage 2a solution with $m_t$ held at its current value and
recomputed online is essentially this paper's scheme transposed to intensities [I].

### Relevance for the Stage 2a design [I]

- Adds a baseline: "frozen-forecast, recalibrate every $\Delta$" (this paper's method) alongside BEGV
  constant-intensity and the order-1 correction. It isolates what the first-order term adds over
  naive re-freezing.
- Kernthese 7 is a usable precedent if Stage 2a ever moves to large-tick binary quoting: a
  non-smooth Hamiltonian still admits a BEGV-type quadratic surrogate, with $\alpha^j$ as a free curvature.
- Their test protocol (grid on frozen problem only) is the weakness Stage 2a should avoid: measure
  the error against the solution *with* the moving factor (exact Hawkes-lifted grid for small $d$).

### Direct quotes (for the draft)

> "We approximate $(Z^i_t)_{t\in[0,T],i=1,\cdots,n}$ and $(\delta^j_t)_{t\in[0,T],j=1,\cdots,d}$ by its initial value" (p. 6)

> "The above approximation is relevant when the time horizon of the problem is relatively short." (p. 7)

> "The resulting Hamiltonian functions are C2 and a natural choice is to use Taylor expansions as the approximations. Clearly this do not apply for (3.4)." (p. 9)

> "Since we are more interested in the behavior of $\hat v$ as $T\to+\infty$, we focus mostly on the asymptotic formulas of A and B." (p. 9)

> "Having closed-form approximate solutions makes the recalibration of the algorithm very efficient, and thus it is even possible to design an "online" market making algorithm" (p. 3)

### Examples & illustrations (for later drafting)

- Fig. 4.5 (p. 14): asymptotic $\hat v(0,q)$ vs. grid $v(0,q)$ for SPX + VIX future — a visual-only
  accuracy check, useful as a contrast to a quantitative regret table.
- Fig. 4.10 (p. 18): multi- vs. uni-asset mean–std frontiers with 100-s recalibration — the only
  experiment in which the stochastic factor moves.
- Example 1 parameters (p. 11): $\Lambda^{1}=1\,$s$^{-1}$ (SPX), $\Lambda^2=0.1\,$s$^{-1}$ (VIX future),
  $T=300$ s — a concrete short-horizon regime where freezing is claimed to be harmless.

### Boundary of this focus

The source contains no intensity factor, so items about Stage 2a's design are inferences [I]. The
paper's "closed-form asymptotic" is BEGV's long-horizon Riccati limit and offers nothing on
perturbation orders or error bounds.

## Mentioned entities

- Models: [[begv-2021-model]] (method source), [[glft-2013-model]] (cited, [20]), [[avellaneda-stoikov-model]] (cited, [2]), [[cartea-jaimungal-ricci-model]] (cited [10], risk-adjusted objective).
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[markov-lift]] (sum-of-exponentials for the rough kernel), [[intensity-forecast]] (absent: intensities constant), [[hawkes-process]] (absent).
- Sources in wiki: [[bergault-2021-closed-form-approximations]], [[gueant-2013-dealing-inventory-risk]], [[cartea-2014-buy-low-sell]], [[cartea-2018-algorithmic-trading-stochastic]].
- Other works (not in wiki): Gatheral–Jusselin–Rosenbaum 2020 (QRH); Rosenbaum–Zhang 2022 (deep calibration of QRH, [28]); Abi Jaber–El Euch 2019 (multifactor approximation); Guéant 2017 (optimal market making); Guilbaud–Pham 2013, 2015 (limit/market orders); Baldacci–Bergault–Guéant 2021 and Baldacci–Derchu–Manziuk 2021 (options MM); Bergault–Guéant 2021 (factor decomposition); Guéant–Manziuk 2019 (deep RL); Dandapani–Jusselin–Rosenbaum 2021 (quadratic Hawkes → super-Heston).

## Connections

- Builds on: [[bergault-2021-closed-form-approximations]] — same ansatz, same $T\to\infty$ Riccati, new Hamiltonian surrogate for a binary control.
- Contrast with: [[barzykin-2026-hawkes-driven-otc]] — there intensities are stochastic (Hawkes) and enter the forecast; here the stochastic factor is volatility and is frozen.
- Contrast with: [[fujii-2015-optimal-position-management]] — Fujii keeps a stochastic factor and expands perturbatively (small diffusion, error $\epsilon^{p(N+1)}$); Rosenbaum–Zhang freeze it.
- Not to be confused with: [[volterra-riccati]] — the rough kernel sits in volatility, not order flow.
