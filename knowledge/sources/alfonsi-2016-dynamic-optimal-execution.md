---
title: "Alfonsi & Blanc 2016 — Dynamic optimal execution in a mixed-market-impact Hawkes price model"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: alfonsi-2016-dynamic-optimal-execution
depth: standard
based_on: preprint
tags: [optimal-execution, hawkes-process, self-exciting-order-flow, cross-side-excitation, transient-price-impact, obizhaeva-wang, price-manipulation, quadratic-value-function, closed-form, flow-driven]
relations:
  - target: who-excites-the-flow
    type: supports
    confidence: extracted
    because: "Flow-driven by construction: «the orders of the strategic trader do not impact the jump rates κ+ and κ− (there is no dXt term) … The first reason for this modeling choice is tractability» (Remark 2.8, pp. 7–8), justified by Tóth et al.: splitting dominates cross-trader excitation (p. 8)."
  - target: markov-lift
    type: mentions
    confidence: extracted
    because: "Exponential kernel chosen «so that (N+, N−, κ+, κ−) is Markovian» (p. 7); multi-exponential approximation of completely monotone kernels «preserving a Markovian framework, at the cost of increasing the dimension of the state space» left for future work (p. 7)."
  - target: intensity-forecast
    type: mentions
    confidence: inferred
    because: "The strategy loads on the intensity imbalance δ through k(T−t) (eqs. 36, 40–41, pp. 22–23), i.e. on the expected future signed flow over the remaining horizon; the paper does not use the term 'forecast'."
  - target: zarezade-2018-steering-social-activity
    type: mentions
    confidence: inferred
    because: "Not cited. Same structural reason for exact quadratic closure under Hawkes: intensity-weighted jump terms are affine in the state and the control never touches the intensity (eqs. 9, 22–25, pp. 7, 19–20)."
---

# Dynamic optimal execution in a mixed-market-impact Hawkes price model

## Bibliographic Details

Alfonsi, Aurélien, and Pierre Blanc. 2016. "Dynamic optimal execution in a mixed-market-impact
Hawkes price model." *Finance and Stochastics* 20(1): 183–218. doi:10.1007/s00780-015-0282-y.
arXiv:1404.0648.

**Read: arXiv 1404.0648v2 (9 June 2015, 27 pp.); page and equation numbers follow that version.**
Non-core work; preprint accepted under the project's preprint policy. A published version exists,
hence `based_on: preprint`.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $X_t$ | strategic trader's position (liquidation programme, $X_{T+}=0$) | $q_t$ (but here an execution position, not a maker's inventory) |
| $\kappa^+_t,\kappa^-_t$ | intensities of other traders' buy/sell market orders | $\lambda_t$ (two components, buy/sell) |
| $\kappa_\infty$ | common baseline | $\mu$ |
| $\beta$ | Hawkes decay | $\beta$ (one decay for both components) |
| $\varphi_s,\varphi_c$; $\iota_s,\iota_c$ | volume-dependent self/cross excitation; their means over the mark law | branching matrix $K=\frac1\beta\begin{pmatrix}\iota_s&\iota_c\\\iota_c&\iota_s\end{pmatrix}$ (p. 8) |
| $\delta_t=\kappa^+-\kappa^-$, $\Sigma_t=\kappa^++\kappa^-$ | intensity imbalance and total intensity (eq. 10) | ⚠ $\delta$ is **not** a quote; $\Sigma$ is **not** a covariance |
| $\alpha=\iota_s-\iota_c$, $\eta=\beta-\alpha$ | net directional excitation; decay of $\delta$ net of excitation | no project symbol |
| $\mu$, $m_k$ | law of order volumes (marks), its moments | ⚠ $\mu$ is the **mark law**, not the baseline |
| $q$ | depth of the block-shaped LOB (impact $1/q$) | ⚠ **not** inventory |
| $\nu$, $\epsilon$ | permanent share of impact (other traders / strategic trader) | — |
| $\rho$ | resilience speed of transient impact | ⚠ **not** the spectral radius $\rho(K)$ |
| $D_t$, $S_t$ | transient price deviation, fundamental (permanent) price | ⚠ $D$ is **not** $\mathrm{diag}(\beta)$ |
| $C(t,x,d,z,\delta,\Sigma)$ | minimal expected cost (value, minimised) | $\theta=-C$ up to cash; cost convention |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (price-impact models vs Hawkes high-frequency models; bridging aim) | 1–3 |
| ✓ F1 | 2.1 General price model: $P=S+D$, Obizhaeva–Wang permanent/transient linear impact; Remark 2.1 | 3 |
| ✓ F1 | 2.2 Optimal execution framework: admissible strategies, block-LOB cost (4), symmetry/scaling (5)–(6), PMS definition, Thm 2.1, Remarks 2.6–2.7 | 4–6 |
| ✓ F1 | 2.3.1 MIH model: symmetric 2-d marked Hawkes, exponential kernel, (9); Remark 2.8 | 6–8 |
| ✓ | 2.3.2 Stationarity (Prop. 2.1) and low-frequency asymptotics | 8 |
| ✓ F1 | 3 Main results (summary) | 8–9 |
| ✓ F1 | 4 The optimal strategy: (10)–(13), Thm 4.1, (14), value function, Fig. 1, reaction to other trades, Remarks 4.1–4.2 | 9–13 |
| ✓ | 5.1 MIHM model: Prop. 5.1 (15), Remark 5.1, discussion; wPMS, Cor. 5.1 (16) | 13–15 |
| ✓ | 5.2 Poisson model: (17), Prop. 5.2 | 15–16 |
| ✓ | Appendix A: explicit formulas (18)–(20) | 16–18 |
| ✓ F1 | Appendix B: verification proof — quadratic ansatz (22), ODE system (27)–(33), solution (34)–(39), strategy (40)–(43) | 18–25 |
| — | Appendix C: proof of Thm 2.1 | 25 |
| — | References | 26–27 |

## Kernthesen

### 1. ⭐ The price is an Obizhaeva–Wang linear-impact price driven by *other traders'* market orders: a share $\nu$ is permanent, $1-\nu$ transient with exponential resilience $\rho$ (p. 3)

$P_t=S_t+D_t$ (eq. 1), $dS_t=\frac\nu q dN_t$, $dD_t=-\rho D_tdt+\frac{1-\nu}q dN_t$, where $N$ is the
signed volume of all past market orders. The block-shaped LOB makes impact proportional to size.
The share $\nu$ is read as "real" or exogenous information, the rest as endogenous and vanishing
(p. 3). The new feature against the execution literature is the explicit flow of others' orders;
linear impact and exponential decay are kept «that give analytical tractability, which is important
to calculate the optimal execution strategy in real time» (Remark 2.1, p. 3).

### 2. The strategic trader's trades enter the same impact equations, possibly with a different permanent share $\epsilon$; costs are quadratic (pp. 4–5)

$dS_t=\frac1q(\nu dN_t+\epsilon dX_t)$, $dD_t=-\rho D_tdt+\frac1q((1-\nu)dN_t+(1-\epsilon)dX_t)$
(eqs. 2–3). A block trade $v$ costs $P_tv+v^2/(2q)$, so the total cost (4) is quadratic in the
strategy. Strategies are càglàd and adapted to the order flow, so the trader «can react instantly
to the market orders issued by other traders» (p. 4). The objective is the **expected cost**
$\mathbb E[C(X)]$: risk-neutral, no inventory penalty.

### 3. ⭐ No price manipulation iff the unaffected price is a martingale; then the Obizhaeva–Wang strategy is optimal and ignores the order flow (p. 5)

Theorem 2.1: «The model does not admit PMS if, and only if the process P is a $(\mathcal F_t)$-martingale
when $X\equiv0$» (p. 5). In that case the optimal strategy is the static OW strategy (7), which «does
not depend on N» (p. 5). Unlike standard execution models, the unaffected price is *not* assumed to
be a martingale; this is what lets the order flow matter (p. 5). The question becomes which flows $N$
give a martingale price and how to trade when they do not (p. 6).

### 4. ⭐⭐ Order flow is a symmetric two-dimensional marked Hawkes process with volume-dependent self- and cross-side excitation and an exponential kernel (pp. 6–7)

$d\kappa^+_t=-\beta(\kappa^+_t-\kappa_\infty)dt+\varphi_s(dN^+_t/m_1)+\varphi_c(dN^-_t/m_1)$, symmetrically for
$\kappa^-$ (eq. 9). Marks (volumes) are i.i.d. with law $\mu$. The exponential kernel is chosen «so that
$(N^+,N^-,\kappa^+,\kappa^-)$ is Markovian» (p. 7). Interpretation: $\varphi_s$ encodes meta-order splitting
and herding; $\varphi_c$ «describes opportunistic traders that sell (resp. buy) after a sudden rise
(resp. fall) of the price» (p. 7). Excitation is cross-side (buy↔sell) within one asset, not
cross-asset. Power-law kernels fit data better; multi-exponential approximation is possible at the
cost of state dimension and is left for future research (p. 7).

### 5. ⭐⭐ The strategic trader does not excite the flow; justified by tractability and by the dominance of order splitting (pp. 7–8)

«As one can see in Equation (9), the orders of the strategic trader do not impact the jump rates
$\kappa^+$ and $\kappa^-$ (there is no $dX_t$ term), as opposed to the market orders issued by other traders.
The first reason for this modeling choice is tractability» (Remark 2.8, pp. 7–8). The empirical
argument: Tóth et al. find that self-excitation stems mainly from splitting, which «is significantly
stronger than the mutual excitation between different traders» (p. 8). A unified model treating all
orders equally is named as open (p. 8).

### 6. Stationarity holds iff $\iota_s+\iota_c<\beta$; the price then has a Brownian low-frequency limit (p. 8)

Proposition 2.1: the largest eigenvalue of $\frac1\beta\begin{pmatrix}\iota_s&\iota_c\\\iota_c&\iota_s\end{pmatrix}$
must be below one (p. 8). Stationarity is not needed for the optimal strategy (p. 8). Under it, the
transient part vanishes in the rescaled limit and the rescaled price converges to a non-standard
Brownian motion (adaptation of Bacry et al., p. 8).

### 7. ⭐⭐ The optimal strategy is explicit and linear in $(x_0,D_0,\delta_0,I,N)$: Obizhaeva–Wang plus a trend part plus a dynamic part (pp. 10–11)

Theorem 4.1 (for $\epsilon\in[0,1)$): $X^*=X^{OW}+X^{trend}+X^{dyn}$, where $X^{trend}$ is linear in
$(D_0,\delta_0)$ and $X^{dyn}$ linear in the processes $I$ (intensity-jump process of $\delta$, eq. 11)
and $N$ (p. 10). At each order the block reaction is eq. (14) (p. 10). «It is worth to notice that the
strategy is linear with respect to $x_0,D_0,\delta_0,I$ and $N$. This property is due to the affine
structure of the model and the quadratic costs. In particular, the reaction of the optimal strategy to
the other trades does not depend on $x_0$» (p. 11). Explicitness matters because the strategy must be
recomputed faster than the inter-arrival time of orders (p. 11).

### 8. ⭐⭐ The value function is exactly quadratic in $(d,x,z,\delta)$ and linear in total intensity $\Sigma$; one Riccati coefficient, all intensity coefficients from linear ODEs (pp. 11, 19–22)

Ansatz (22): $C=a(T-t)(d-(1-\epsilon)x)^2+\dots+b(T-t)\,\delta\,(d-(1-\epsilon)x)+c(T-t)\delta^2+e(T-t)\Sigma+g(T-t)$.
Terms odd in $(x,d,z,\delta)$ vanish by the buy/sell symmetry $C(t,x,d,z,\delta,\Sigma)=C(t,-x,-d,-z,-\delta,\Sigma)$,
and the $\Sigma^2$ coefficient is zero (p. 19). Matching terms gives (27)–(33) (p. 21): the impact
coefficient solves the Riccati-type equation $\dot j=-\rho j^2$, so $j(u)=1/(2+\rho u)$ and $a$ is
explicit (29); $b$ solves the **linear** ODE (30) $\dot b=-(\beta-\alpha)b-\frac{\rho}{2+\rho u}b+\frac{m_1}{1-\epsilon}\frac{1+\nu\rho u}{2+\rho u}$;
$c,e,g$ solve linear ODEs (31)–(33) driven by $b$. The system has a unique solution (pp. 21–22).
$b$ and $k$ are explicit through $\zeta,\omega$ (eqs. 35–36, p. 22); $c,e,g$ need the exponential
integral and are «very cumbersome» but do not affect the strategy (p. 11).

### 9. ⭐ How to react to another trader's order depends on its size: follow small orders (splitting), fade large ones (resilience) (p. 12)

For general $\varphi_s,\varphi_c$ the block reaction's sign depends on the observed volume. For long
horizons the jump part is about $\frac{m_1}{2\rho}(1+\frac{\nu\rho}\eta)dI_t-(1-\nu)dN_t$ (p. 12). With only
self-excitation: «if a market buy order is relatively small, it may be a part of a big split order …
and the strategic trader has interest to follow this trend. However, if a market buy order is
relatively big, the price resilience effect is likely to dominate» (p. 12). «The optimal strategy only
depends on $(\varphi_s,\varphi_c)$ through $\varphi_s-\varphi_c$» (p. 12). Figure 1 shows mean-reverting vs
trend-following regimes for resilience $\rho=25$ vs $\rho=16$ at $\beta=20$, $\iota_s=16$ (p. 12).

### 10. ⭐ Poisson order flow necessarily creates robust, parameter-free price manipulation (pp. 12–13, 15–16)

With independent compound Poisson flows the price mean-reverts when the trader is passive, so the
optimum posts an opposite order after each observed order (Remark 4.1, pp. 12–13): «Such an obvious
Price Manipulation Strategy is unrealistic, therefore modeling the order flow with Poisson processes is
not satisfactory» (p. 13). Proposition 5.2: trading $-\lambda\frac{1-\nu}{1-\epsilon}\Delta N$ ($\lambda\in(0,1)$) at each order is a PMS
with explicit negative expected cost, best at $\lambda=1/2$, without knowing $qD_0$ or $\rho$ (p. 16).
Self-excitation is therefore needed for a viable market.

### 11. ⭐ The MIHM conditions exclude PMS: $\beta=\rho$, $\alpha=(1-\nu)\rho$, $\varphi_s-\varphi_c$ linear on the mark support, and a steady-state start (pp. 13–14)

Proposition 5.1, eq. (15) (p. 13). Readings (p. 14): $\beta=\rho$ means liquidity providers' mean
reversion compensates the sign autocorrelation of liquidity takers (cf. Bouchaud et al.). With
$\iota_c=0$, the Hawkes norm $\iota_s/\beta$ (share of endogenous orders) must equal the transient share
$1-\nu$. Positivity of $\alpha$ keeps opportunistic cross-excitation small; under (15) stationarity
reduces to $2\iota_c<\beta$ (p. 14).

### 12. "No reaction to others' trades" (no weak PMS) and "no free profit" are essentially the same condition (p. 15)

Definition 5.1: weak PMS if liquidation cost can be cut by a block trade answering another
trader's order (p. 15). Corollary 5.1: no wPMS iff $\beta=\rho$, $\alpha=(1-\nu)\rho$, $\varphi_s-\varphi_c$ linear
(16), which equals (15) up to the start condition (p. 15). The authors read this as a link between
the absence of free income and market stability, since reacting to others' orders can trigger chain
reactions (pp. 9, 15).

### 13. Calibrated parameters will deviate from MIHM, so the dynamic strategy has practical value (p. 14)

Reasons given: fitting a PMS-free market need not give a PMS-free model; the model ignores the
bid-ask spread and gives the trader instant reaction (latency); temporary high-frequency arbitrage
exists in practice (p. 14). Estimation on market data is deferred, and carried out in
[[alfonsi-2016-extension-calibration-hawkes]].

### 14. Choosing the initial position: the cost-minimising $x_0$ relative to mark-to-market sells into a negative trend (p. 13)

Remark 4.2 gives the $x_0$ minimising $\mathbb E[C(X)]+P_0x_0$ in closed form; when $D_0\ge0$ and
$\delta_0\le0$ the price trend is negative and selling is favoured (p. 13).

## Figures and tables

- Fig. 1 (p. 12): optimal strategy vs OW under a simulated Hawkes path, mean-reverting ($\iota_s<\beta<\rho=25$) and
  trend-following ($\rho=\iota_s=16<\beta=20$) regimes; parameters in caption.

## What this source does not address

- **Market making / quote control.** The trader executes or round-trips with market orders and
  continuous trading; there are no quotes, no fill probability $f(\delta)$, no Hamiltonian. Quote-controlled
  Hawkes market making: [[barzykin-2026-hawkes-driven-otc]], [[cartea-2014-buy-low-sell]],
  [[martin-2026-market-making-hawkes]].
- **Several assets.** One asset; excitation is buy↔sell only. Cross-asset Hawkes:
  [[acero-2026-hawkes-structured-networks]], [[rosenbaum-2022-multi-asset-market]].
- **Risk aversion.** Risk-neutral expected cost; no inventory penalty or CARA.
- **Fill-driven excitation.** Excluded by Remark 2.8 (pp. 7–8); see [[jusselin-2021-persistent-order-flow]]
  and [[bergault-2024-price-aware-automated]] for the fill-driven side.
- **Non-exponential kernels, nonlinear impact, bid-ask spread.** Named as limitations or future work
  (pp. 3, 7, 14); multi-exponential kernels and calibration follow in
  [[alfonsi-2016-extension-calibration-hawkes]].
- **Numerical experiments / data.** Only an illustrative simulation (Fig. 1).

## Model card

*Execution model, not market making; card filled for comparability.*

| Field | Value |
|---|---|
| Assets | 1 |
| Kernel | exponential Hawkes, $e^{-\beta t}$, volume-marked jumps $\varphi_s(v/m_1),\varphi_c(v/m_1)$ (eq. 9, pp. 6–7) |
| Excitation | self + cross-side (buy↔sell); no cross-asset |
| Who excites the flow | other traders' market orders only; the strategic trader's orders do not (Remark 2.8, pp. 7–8) — flow-driven |
| Objective | minimise expected execution cost under linear permanent + transient impact; risk-neutral |
| Solution method | closed form: quadratic value ansatz + verification; one explicit Riccati-type coefficient, linear ODEs for intensity coefficients (App. B, pp. 18–25) |
| Benchmark | Obizhaeva–Wang static strategy (Thm 2.1, Fig. 1) |
| Reported regret or gap numbers | n/a — no numerical study beyond Fig. 1; PMS costs given as formulas (17), Prop. 5.2 |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 4, 5, 7, 8, 9.**

### What this focus needs beyond the Kernthesen

1. **Why the quadratic closure is exact [I from eqs. 9, 22, Z on p. 20].** The jump term is
   $\frac{\Sigma\pm\delta}2\,\mathbb E[C(\text{state}+\text{jump})-C]$. For a quadratic $C$ the difference is affine in the
   state, and the prefactor is affine in $(\delta,\Sigma)$, so the product stays quadratic. Three
   conditions make this work: the control enters linearly through impact with a quadratic cost; the
   control never changes the intensities (Kernthese 5); and marks are i.i.d. and independent of the
   state. Quote-controlled market making breaks the first condition: the control enters through a
   nonlinear fill probability multiplied by the intensity. This is the same verdict as for Fujii
   ([[fujii-2015-optimal-position-management]], focus 1, item 3) and Zarezade
   ([[zarezade-2018-steering-social-activity]]).
2. **Triangular structure [D from eqs. 27–33, p. 21].** The only nonlinear (Riccati-type) equation is
   for the price/position curvature $a$ (via $j$); every coefficient that loads on intensity
   ($b$, $c$, $e$) solves a linear ODE given $a$. This is the exact counterpart of the
   order-0 Riccati / order-1 linear split that Stage 2a must justify asymptotically.
3. **Only the imbalance moves the strategy [D from (22), (40), pp. 19, 23].** By buy/sell symmetry,
   total intensity $\Sigma$ enters the value only linearly through $e$ and never the strategy. The
   imbalance $\delta$ enters both.
4. **Multi-asset carry-over [I].** Nothing is multi-asset, but the mechanism carries over directly. For
   $d$ assets with a cross-asset excitation matrix, intensity enters affinely and the control does not
   touch it. The ansatz would then be quadratic in (positions, deviations, imbalances) and linear in
   total intensities. Curvature would solve a matrix Riccati; intensity loadings would solve a linear
   matrix ODE in the decay-minus-excitation operator. The companion paper shows this structure for a
   $p$-dimensional intensity state ([[alfonsi-2016-extension-calibration-hawkes]], Kernthese 7).

### Direct quotes (for the draft)

> "It is worth to notice that the strategy is linear with respect to x0, D0, δ0, I and N. This property is due to the affine structure of the model and the quadratic costs." (p. 11)

> "As one can see in Equation (9), the orders of the strategic trader do not impact the jump rates κ+ and κ− (there is no dXt term), as opposed to the market orders issued by other traders. The first reason for this modeling choice is tractability." (pp. 7–8)

> "Of course, it would be nice to find in the future a tractable model that gives a unified framework for the mutual excitation that considers equally all the market orders." (p. 8)

> "Such an obvious Price Manipulation Strategy is unrealistic, therefore modeling the order flow with Poisson processes is not satisfactory." (p. 13)

### Examples & illustrations (for later drafting)

- Fig. 1 (p. 12): one simulated Hawkes path, two parameter sets. The optimal trader fades each
  order when $\rho=25$ and follows it when $\rho=16$ (with $\beta=20$). This is a compact picture of how excitation
  vs resilience sets the sign of the reaction.
- Eq. (22) with the symmetry argument (p. 19): a one-page model of how a quadratic ansatz in
  (state, intensity imbalance) plus a linear term in total intensity closes under Hawkes flow.

### Boundary of this focus

The source is an execution problem with linear impact. It has no quotes, no fill probabilities and
no several assets. Items 1 and 4 are the project's inferences from its equations.

## Mentioned entities

- Concepts: [[hawkes-process]], [[who-excites-the-flow]], [[markov-lift]], [[intensity-forecast]], [[branching-matrix]] (2×2 self/cross matrix, Prop. 2.1).
- Sources in this wiki: [[alfonsi-2016-extension-calibration-hawkes]] (companion paper, later); [[fujii-2015-optimal-position-management]] and [[zarezade-2018-steering-social-activity]] (not cited; structural comparison).
- Other works (not in this wiki): Obizhaeva & Wang 2013; Huberman & Stanzl 2004 (PMS); Alfonsi & Schied 2013 (completely monotone kernels); Gatheral, Schied & Slynko 2012; Bacry et al. 2013; Bacry & Muzy 2013; Tóth et al. 2011 (splitting); Bouchaud et al. 2004; Filimonov & Sornette 2012; Hardiman, Bercot & Bouchaud 2013.

## Connections

- Supports [[who-excites-the-flow]]: an explicit, argued flow-driven choice (Remark 2.8).
- Builds-on relation runs the other way: [[alfonsi-2016-extension-calibration-hawkes]] extends this model and calibrates it.
- Structural parallel (not cited) to [[fujii-2015-optimal-position-management]] and [[zarezade-2018-steering-social-activity]]: exact quadratic closure because the control does not multiply the intensity.
- Cited as the dynamic-arbitrage precedent by [[jain-2025-impulse-control-hawkes]] (via the companion paper) and listed by [[chen-2026-optimal-trade-execution]].
