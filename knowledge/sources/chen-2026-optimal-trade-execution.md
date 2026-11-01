---
title: "Chen, Horst & Tran 2026 — Optimal Trade Execution Under Endogenous Order Flow"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: chen-2026-optimal-trade-execution
depth: standard
tags: [optimal-execution, hawkes, endogenous-order-flow, risk-neutral, deterministic-strategy, wiener-hopf, closed-form, statistical-arbitrage, nasdaq]
relations:
  - target: who-excites-the-flow
    type: supports
    confidence: extracted
    because: "Control feeds the intensity: «his trading activity triggers child orders and endogenously affects future order flow» (abstract, p. 1); base intensities become µ^s = µ + ξ_t 1{ξ_t>0} (p. 5)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«market buy/sell orders arrive according to independent exponential Hawkes processes» with intensity µ + α∫e^{-β(t-u)}dN_u (Sec. 2.1, p. 5)."
  - target: intensity-forecast
    type: builds-on
    confidence: inferred
    because: "Only expected intensities enter: E[I_t] = E[µ_t] + α∫e^{-β(t-u)}E[I_u]du and the expected child-order count C_t with resolvent kernel e^{-ω(s-r)} (eq. 2.2, p. 5) — a deterministic forecast, as in the forecast-curve concept."
based_on: preprint
---

# Optimal Trade Execution Under Endogenous Order Flow

## Bibliographic Details

Chen, Ying; Horst, Ulrich; Tran, Hoang Hai. 2026. "Optimal Trade Execution Under Endogenous
Order Flow." *Operations Research* 74(1): 72–92. doi:10.1287/opre.2023.0151.

**Read:** LMU/HU Berlin CRC TRR 190 Discussion Paper No. 368, dated 20 January 2023 (paper dated
9 January 2023), epub.ub.uni-muenchen.de/94308. 41 PDF pages: cover page + 40 numbered pages.
**Page numbers below are the printed numbers (= PDF page − 1)**; equation numbers follow this
version. Accepted under the preprint policy (non-core work); the OR version may differ (three
years later, different page count).

### Notation map (source → project)

| Source | Meaning in source | Project symbol / remark |
|---|---|---|
| $x_0$, $X_t$, $\xi_t$ | initial position, remaining position, selling rate | ⚠ project $X_t$ = cash; here position. $q_t$ ↔ $X_t$ |
| $I^{b/s}_t$, $\mu$, $\alpha$, $\beta$ | Hawkes intensities, baseline, jump, decay | $\lambda_t$, $\mu$, kernel $\alpha e^{-\beta u}$ |
| $\omega:=\beta-\alpha$ | called "self-exciting ratio" (eq. 2.1) | ⚠ not the branching ratio $\alpha/\beta=\rho(K)$ (fn. 7, p. 9) |
| $\eta$ | instantaneous impact (bps/share) | — |
| $\lambda$ | permanent impact per share (bps) | ⚠ not an intensity |
| $\gamma:=\lambda\alpha/\omega$ | child-order permanent impact | ⚠ not risk aversion |
| $\zeta=\gamma/\eta$ | cost ratio | — |
| $\theta:=-\omega(\omega-\gamma/\eta)$ | sign factor of the ODE (eq. 3.3) | ⚠ not the reduced value function |
| $k$, $C,C_1,C_2,C_3$ | ODE frequency, solution constants | ⚠ $k$ not the GLFT decay |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (endogeneity, detection of meta-orders, contributions, fn. 3 on Fu et al.) | 1–4 |
| ✓ F1 | 2 The liquidation model: position ODE, transaction price (p. 4–5) | 4–5 |
| ✓ F1 | 2.1 Permanent impact: Hawkes flow, baseline shift by own trading, child orders (eqs. 2.1–2.3, Remark 1, Assumption 1) | 5–6 |
| ✓ F1 | 2.2 Execution cost (eq. 2.4, Remarks 2–3, TWAP eq. 2.5) | 6–7 |
| ✓ F1 | 3 Optimal execution strategy: cost functional (3.1) | 7 |
| ✓ F1 | 3.1 First and second order conditions (Wiener–Hopf eq. 3.2, θ eq. 3.3, ODE 3.4–3.5) | 8 |
| ✓ F1 | 3.2 Small feedback θ < 0: Theorem 1 (eqs. 3.6–3.7), numerics Figs. 1–3 | 8–11 |
| ✓ F1 | Critical feedback θ = 0: Theorem 2 (eq. 3.8), Fig. 4 | 12 |
| ✓ F1 | Strong feedback θ > 0: Example 1 round trip, Fig. 5, Theorem 3, Fig. 6 | 13–14 |
| ✓ F1 | 4 Empirical implementation: data, LOB-based η, OFI-based λ, Hawkes MLE, Tables 1–4, Figs. 7–8 | 14–21 |
| ✓ F1 | 5 Counterfactual experiments and sensitivity (Tables 5–8, Fig. 9) | 22–24 |
| ✓ F1 | 6 Conclusion | 24 |
| ✓ F1 (A.2 optimality) | Appendix A: proof of Theorem 1 (A.1 FOC, Plancherel/Lorentzian argument, A.3 positivity) | 27–31 |
| — | Appendix B–D: square-root benchmark, per-stock estimates and costs (Tables 9–18) | 31–40 |

## Kernthesen

### 1. ⭐⭐ The trader's own trading raises the Hawkes baseline: the control feeds the intensity (pp. 1, 5)

Buy/sell market orders are independent exponential Hawkes processes,
$I^{b/s}_t=\mu^{b/s}_t+\alpha\int_0^te^{-\beta(t-u)}dN^{b/s}_u$ (p. 5), symmetric in equilibrium
($\mu^b=\mu^s=\mu$), so other traders' net flow is a martingale. With the large trader present,
«the buy/sell base intensities change to $\mu^s_t=\mu+\xi_t1_{\{\xi_t>0\}}$ and
$\mu^b_t=\mu-\xi_t1_{\{\xi_t<0\}}$» (p. 5). His selling rate is added to the sell-order stream and
then self-excites: «his trading activity triggers child orders and endogenously affects future order
flow, both instantaneously and permanently» (abstract, p. 1).

### 2. ⭐ Only expected order counts matter; their Volterra equation has the resolvent kernel $e^{-\omega t}$, $\omega=\beta-\alpha$ (p. 5)

Expected intensities solve $\mathbb E[I_t]=\mathbb E[\mu_t]+\alpha\int_0^te^{-\beta(t-u)}\mathbb E[I_u]du$; the
expected net-sell count from the trader's activity is
$H_t=\int_0^t\xi_sds+\alpha\int_0^t\int_0^se^{-\omega(s-r)}\xi_rdrds=:\int_0^t\xi_sds+C_t$ (eq. 2.2),
$C$ the expected number of **child orders** (p. 5). Stability: Assumption 1, $\omega\ge0$ (p. 6).

### 3. Permanent impact is linear in own plus child orders (p. 6)

With $\lambda$ bps per share and $\gamma:=\lambda\alpha/\omega$:
$D^\xi_t=\lambda\int_0^t\xi_sds+\gamma\int_0^t\xi_s(1-e^{-\omega(t-s)})ds$ (eq. 2.3). The transaction price is
$S_t=S_0+B_t-\eta\xi_t-D^\xi_t$ with $B$ a Brownian martingale (p. 5). For $\alpha=0$ the optimum is
TWAP (Remark 1, p. 6).

### 4. ⭐⭐ Self-excitation turns into a fixed cost plus a "rebate": the controllable cost is a non-convex quadratic functional (pp. 6–7)

Eq. (2.4): $TC=\eta\int_0^T\xi_t^2dt-\gamma\int_0^T\xi_t\int_0^t\xi_se^{-\omega(t-s)}dsdt+(\gamma+\lambda)x_0^2/2$. «the
self-exciting order flow dynamics increases the fix-cost from λ to λ + γ bsp per share in exchange for
a "rebate" that takes the form of a negative exponential impact cost» (p. 6). Remark 2: the
controllable cost is a difference of two non-negative costs, so the problem «is not convex» (p. 7).

### 5. Risk neutrality and deterministic strategies are what make the problem deterministic (pp. 3–4)

Strategies are deterministic, and fn. 4 claims this is w.l.o.g. within the framework (p. 4). Fn. 3:
Fu et al. (2020) let base intensities depend on own trading rates too, but their verification
«requires both risk aversion and transient (rather than permanent) impact»; «Focusing on a
deterministic setup and permanent rather than transient impact allows us to obtain closed-form
solutions» (p. 3).

### 6. ⭐⭐ First-order condition: a Wiener–Hopf integral equation, reduced to a linear second-order ODE (p. 8)

Variational FOC: $\hat\xi_t-\tfrac{\gamma}{2\eta}\int_0^T\hat\xi_se^{-\omega|t-s|}ds=C$ (eq. 3.2), «a
Wiener-Hopf integral equation of the second kind» (p. 8). Differentiating twice:
$\xi''_t+\omega(\gamma/\eta-\omega)\xi_t=-\omega^2C$ (eq. 3.4) with Robin boundary conditions
$\xi'_0-\omega\xi_0=-\omega C$, $\xi'_T+\omega\xi_T=\omega C$ (eq. 3.5). The sign of
$\theta=-\omega(\omega-\gamma/\eta)$ (eq. 3.3) decides the solution type.

### 7. ⭐ Second-order condition = no beneficial round trip (p. 8)

The second variation equals $\eta\int(\nu'_t)^2dt-\gamma\int\nu'_t\int_0^t\nu'_se^{-\omega(t-s)}dsdt$: «the cost
of a round-trip. This shows that the candidate strategy is optimal if and only if no beneficial
round-trip/statistical arbitrage exists» (p. 8).

### 8. ⭐⭐ Small feedback ($\theta<0$): closed-form hyperbolic strategy, inverted-U trading rate (pp. 9–11)

Theorem 1: $\hat\xi_t=C_1\cosh(kt)+C_2\sinh(kt)+C_3$, $k=\sqrt{\omega(\omega-\gamma/\eta)}$, explicit
$C,C_1,C_2,C_3$ (eq. 3.6, p. 9); the running cost (3.7) is strictly positive for $x_0>0$. The
solution depends only on $\zeta=\gamma/\eta$ and $\omega$ (p. 9). The rate peaks mid-horizon to
harvest the decaying "rebate" (pp. 9–11).

### 9. ⭐ Optimality is proved by a Fourier (Plancherel) positivity argument, not by verification of an HJB (pp. 29–30)

Writing $e^{-\omega|x|}=\int\frac{2\omega}{\omega^2+4\pi^2t^2}e^{-2\pi itx}dt$ (Lemma 1, p. 29),
$L(\xi)=\int|\hat\Xi_z|^2\big(\eta-\gamma\frac{\omega}{\omega^2+4\pi^2z^2}\big)dz$, hence «L(ξ) ≥ 0 if
ω ≥ γ/η. In particular, the cost of any round-trip is non-negative» (p. 30).

### 10. Critical case $\theta=0$: parabolic strategy (p. 12)

Theorem 2: $\xi_t=C_1+C_2t+C_3t^2$ with $C=12x_0/(T(12+\omega T(6+\omega T)))$ (eq. 3.8). For
$\omega=0$ the cost reduces to $x_0^2+\eta\int\xi^2$ and TWAP is optimal (p. 12).

### 11. ⭐ Strong feedback ($\theta>0$): trigonometric candidate and profitable round trips (pp. 13–14)

Example 1 shows a buy-then-sell round trip with negative cost when $\gamma/\eta>\omega$ (Fig. 5,
p. 13); Theorem 3 gives the cyclic candidate $\hat\xi_t=C_1\cos(kt)+C_2\sin(kt)+C_3$ (p. 14), which
need not be optimal. The paper treats it as «a mere illustration of the rich dynamics» since
empirically $\theta<0$ (p. 13).

### 12. ⭐ Empirics: 110 NASDAQ stocks, θ always negative, 12–24% cost reduction against TWAP (pp. 14–21)

Five days of ITCH data (1–7 Oct 2019), 10:00–15:00, 1-hour bins, liquidation of 10% of hourly volume
(pp. 14–15). $\eta$ from a kernel-density LOB model, $\lambda$ from an OFI regression
($R^2$ 41–71%), exponential Hawkes by MLE (pp. 15–18). Table 2 (p. 19): $\alpha$ 4.60–5.43,
$\omega$ 5.84–6.65, $\zeta$ 5.47–6.32, $\theta$ −1.82 to −4.85 by tick group. Optimal vs TWAP:
$r_{TWAP}$ 12.15–24.40% (Table 3, p. 20); fitted $r_{TWAP}=-36.483\omega+42.436\gamma/\eta$, $R^2=85\%$
(p. 19). Counterfactuals: 50% lower $\omega$ → 20.14–33.93%; 50% higher cost ratio → 61.22–64.20%;
$\theta=0$ → 66.68–69.57% (pp. 22–23).

## What this source does not address

- **Market making, quotes, fill probabilities.** Single-sided liquidation with market orders only.
- **Risk aversion, CARA, HJB.** Risk-neutral, deterministic strategies; no dynamic programming at all.
- **Stochastic (feedback) control on the realised intensity.** Strategies do not react to realised
  order flow (fn. 4 asserts w.l.o.g.).
- **Several assets or cross-excitation.** One asset; buy and sell Hawkes processes are independent
  (no cross-side excitation).
- **Non-exponential kernels.** Power-law kernels are acknowledged (fn. 12, p. 18) but excluded; the
  exponential kernel «allows us to obtain closed-form solutions».

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

Read as an outside-MM source: what its control machinery says about exponential transforms,
Riccati/LQ closures, lifts, and whether the control feeds the intensity.

**Carries Kernthesen 1, 2, 4, 5, 6, 9.**

### What this focus needs beyond the Kernthesen

1. **D1 analogue: absent.** There is no HJB and no change of variables. The closure comes from a
   different route: risk neutrality + deterministic strategies + impact linear in expected order
   counts → the self-excitation collapses into a deterministic linear Volterra kernel
   $e^{-\omega(t-s)}$ acting on the control, the cost is a quadratic functional, and its FOC is a
   Wiener–Hopf equation equivalent to a linear second-order ODE (eqs. 3.2–3.5, p. 8). The control
   feeds the intensity (Kernthese 1), i.e. the excitation is "self-inflicted" as in the fill-driven
   convention, but the closure never meets the jump structure that D1 is about.
2. **What would break the closure (the authors' own diagnosis, p. 3, fn. 3):** risk aversion and a
   stochastic, intensity-dependent strategy. Then the realised intensity is a state, and the
   problem returns to a controlled-intensity HJB as in `fu-2022-portfolio-liquidation-games`. The
   expected-value collapse used here is exactly the "freeze the forecast" step on the
   [[intensity-forecast]] page, made exact by risk neutrality and deterministic controls.
3. **Carries over to several assets [I].** The structure is LQ in expectations, so a $d$-asset
   version with a Hawkes branching matrix $K$ would replace $e^{-\omega t}$ by the matrix resolvent
   $e^{-(D-K)t}$ and the scalar ODE (3.4) by a linear second-order system; the
   positivity condition (Kernthese 9) would become positive-definiteness of a matrix symbol. Not in
   the paper.
4. **Statistical-arbitrage boundary as a stability condition.** $\theta<0$ is a condition mixing
   Hawkes stability ($\omega$) with impact ratios ($\gamma/\eta$); it is the execution analogue of a
   well-posedness threshold beyond Hawkes subcriticality. Empirically never violated (Table 2).

### Direct quotes (for the draft)

> "Under the assumptions of risk neutrality and deterministic constants of the impact parameters, we provide closed-form solutions and illustrate the relationship between trading strategies and feedback effects." (abstract, p. 1)

> "In the presence of the large trader the buy/sell base intensities change to µs_t = µ + ξ_t 1{ξt>0} and µb_t = µ − ξ_t 1{ξt<0}." (p. 5)

> "Moreover the verification argument in Fu et al. (2020) requires both risk aversion and transient (rather than permanent) impact and therefore do not apply to our setup. Focusing on a deterministic setup and permanent rather than transient impact allows us to obtain closed-form solutions with parameters that can be calibrated from market data." (fn. 3, p. 3)

> "The preceding equation is a Wiener-Hopf integral equation of the second kind with constants limits of integration." (p. 8)

### Examples & illustrations (for later drafting)

- Fig. 1 (p. 10): inverted-U optimal trading rate against flat TWAP — the visible effect of
  self-inflicted excitation on a closed-form policy.
- Table 3 (p. 20): 12.15–24.40% cost improvement against TWAP across tick groups — an empirical
  "value of modelling endogeneity" figure comparable in role to Barzykin's Poisson-regret column.

### Boundary of this focus

Execution, not market making; deterministic and risk-neutral. Its closed form says nothing about
CARA linearisation (D1) or $\lambda$-dependent Riccati coefficients (D2); it shows only that
self-inflicted Hawkes excitation stays LQ-tractable once the problem is reduced to expectations.
All page numbers are those of the 2023 discussion paper.

## Mentioned entities

- Concepts: [[hawkes-process]], [[who-excites-the-flow]], [[intensity-forecast]]
- Other works (bibkeys): `fu-2022-portfolio-liquidation-games` (the paper cites the 2020 preprint),
  `alfonsi-2016-dynamic-optimal-execution`, `cartea-2018-algorithmic-trading-stochastic`; not in the
  library: Gatheral–Schied–Slynko 2012, Obizhaeva–Wang 2013, Almgren–Chriss 2000, Amaral–Papanicolaou
  2019, Cont–Kukanov–Stoikov 2013, Filimonov–Sornette 2015, Polyanin–Manzhirov 1998.

## Connections

- Supports: [[who-excites-the-flow]] — an execution example where the controller's own trades
  excite the flow.
- Compare: [[yuan-2026-dynamic-pricing-self]] (also self-inflicted excitation, risk-neutral, but
  solved by an HJB in the excitement level), [[jusselin-2021-persistent-order-flow]] (fill-driven,
  path-dependent HJB), [[barzykin-2026-hawkes-driven-otc]] (forecast-based closure; cites the
  LQ-Volterra execution precedent).
