---
title: "Tarditi 2026 — Hawkes Process Models of Limit Order Books for Optimal Market Making (MSc thesis)"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: tarditi-2026-hawkes-process-models
depth: standard
tags: [market-making, hawkes-process, markov-lift, cara, hjb, verification, finite-difference, lobster, single-asset, thesis]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«we assume (N+, N−) is a bivariate Hawkes process (Definition 3.2) satisfying the stability/subcriticality condition», dynamics eq. (11) (p. 9)."
  - target: markov-lift
    type: builds-on
    confidence: extracted
    because: "«Choosing an exponential (or a sum of exponentials) kernel is therefore a tractability commitment: the convolution admits a finite-dimensional Markov embedding» (p. 7); Proposition 3.1, eq. (8)."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Branching matrix K = ∫φ, «Assumption 3.4 (Hawkes stability / subcriticality). We assume ρ(K) < 1» (p. 5); estimated K with ρ(K) ≈ 0.538 (Fig. 9, p. 42)."
  - target: who-excites-the-flow
    type: builds-on
    confidence: extracted
    because: "Flow-driven convention: «The aggressive order flow (N+, N−) drives the Hawkes intensity state (λ+, λ−) via (11). The market maker is price-taking and does not affect (N+, N−) nor (λ+, λ−)» (Remark 4.4, p. 12); missed orders also shift λ in J+0, J−0 of eq. (60) (p. 33)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«A canonical benchmark is Avellaneda–Stoikov … executions at the dealer's quotes arrive as Poisson processes with quote-dependent intensities» (p. 4)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "«Many extensions preserve the same control-theoretic structure while refining modelling ingredients e.g. (Guéant et al., 2013)» (p. 4)."
---

# Hawkes Process Models of Limit Order Books for Optimal Market Making: A Stochastic Control Approach

## Bibliographic Details

Tarditi, Andrea. 2026. *Hawkes process models of limit order books for optimal market making: a
stochastic control approach.* MSc thesis, Politecnico di Milano (a.y. 2024–2025; supervisor Fulvia
Confortola). <https://hdl.handle.net/10589/253302>. 58 PDF pages, 55 numbered.

**Read:** the thesis copy in `library/pdf/`. A thesis is its own original; no preprint question
arises. Page numbers are the **printed** page numbers (PDF page = printed + 3). Code:
github.com/andreatrdt/HawkesOptimalControl (p. 51).

### Notation map (source → project)

| Source | Meaning | Project |
|---|---|---|
| $\delta^a,\delta^b$, $\mathcal D=[0,\delta_{\max}]^2$ | quote offsets, admissible set | $\delta^a,\delta^b$ |
| $Q_t$, $q_0$, $Q_{\max}$ | inventory, trade size, bound | $q_t$, $Q$ |
| $X_t$, $S_t$, $\sigma$ | cash, midprice, diffusive vol | $X_t$, $S_t$, $\sigma$ |
| $\lambda^\pm$, $\mu^\pm$, $a^{\pm\pm}$, $\beta_\pm$ | buy/sell intensities, baselines, jump sizes, decays | $\lambda_t$, $\mu$, $K\!\cdot\!D$, $\beta$ |
| $K=A/\beta$ (columnwise), $\rho(K)$ | branching matrix | $K$, $\rho(K)$ |
| $f_a,f_b$; $A_{\rm fill}e^{-k_{\rm fill}d}$ | fill probability | $f(\delta)$ ($\Lambda e^{-k\delta}$ shape) |
| $p^\pm$, $\kappa$ | price-move probability per market order, tick size | none ⚠ $\kappa$ is the tick, not a penalty |
| $\eta$ | terminal quadratic inventory penalty (eq. 20) | none |
| $\gamma$ | CARA risk aversion | $\gamma$ |
| $\Theta(t,q,\lambda^+,\lambda^-)$ | reduced value, $V=-e^{-\gamma x}e^{-\gamma qs}\Theta$ (eq. 53) | $\theta(t,q,\lambda)$ (multiplicative, not additive form) |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | 1 Introduction (question, contributions) | 1–3 |
| ✓ | 2 State of the art (LOB model families, Hawkes, AS/GLFT, gap) | 3–4 |
| ✓ F1 | 3 Point processes, Hawkes, stability, Markov embedding, thinning | 4–8 |
| ✓ F1 | 4 Market model and control problem (bivariate Hawkes, thinning, marking, CARA objective) | 8–14 |
| ✓ | 5 Semimartingale calculus, PRM embedding, triangular well-posedness, generator (44) | 14–27 |
| ✓ | 6 Stopping-time DPP | 27–29 |
| ✓ F1 | 7 HJB derivation | 29–30 |
| ✓ | 8 Verification theorem | 31–32 |
| ✓ F1 | 9 CARA factorisation, reduced HJB (60), exponential moments, finite-grid verification | 32–36 |
| ✓ F1 | 10 Empirical pipeline (LOBSTER events, Hawkes calibration, fill/impact proxies, IMEX solver, backtests) | 36–51 |
| ✓ F1 | 11 Results; 12 Conclusion | 51–53 |
| ✓ F1 | 13 Future work (kernels, queues, viscosity, numerics/ADP, cross-asset) | 53–54 |

## Kernthesen

### 1. The question: how to quote when arrivals are self- and cross-exciting, with a rigorous control layer (pp. 1–2)

«How should a market maker choose bid and ask quote offsets over time, balancing spread capture against
inventory risk, when the order-arrival mechanism is strongly time-dependent and exhibits self- and
cross-excitation?» (p. 1). The stated novelty is the end-to-end chain data → Hawkes model → rigorous
DPP/HJB/verification → numerical policy → backtest (p. 2).

### 2. ⭐ Exponential kernels are a tractability commitment: they give a finite Markov lift, general kernels give an infinite-dimensional HJB (pp. 1, 7)

«without a Markov representation, the value function would depend on the full event history» (p. 1).
For general kernels «the associated dynamic programming equation would become a functional/infinite-
dimensional HJB» (p. 7). With $\phi(u)=Ae^{-Bu}$, $d\lambda_t=B(\mu-\lambda_t)dt+A\,dN_t$ (eq. 8,
Prop. 3.1); a sum of $M$ exponentials multiplies the state dimension by $M$ (p. 7).

### 3. ⭐ Order flow is a bivariate exponential Hawkes process of buy and sell market orders with cross-excitation (p. 9)

$d\lambda^+=-\beta_+(\lambda^+-\mu^+)dt+a^{++}dN^++a^{+-}dN^-$,
$d\lambda^-=-\beta_-(\lambda^--\mu^-)dt+a^{-+}dN^++a^{--}dN^-$ (eq. 11), subcritical $\rho(K)<1$
(Assumption 3.4, p. 5). Stationary mean $\bar\lambda=(I-K)^{-1}\mu$ (p. 5).

### 4. ⭐⭐ The maker is a price taker: quotes thin the market flow, they never excite it (pp. 9, 11–12, 16)

Executions are predictable Bernoulli thinnings: $\Lambda^a=f_a(\delta^a)\lambda^+$, $\Lambda^{+,0}=(1-f_a(\delta^a))\lambda^+$ (eq. 13, p. 9).
«The control δ affects only the thinning/marking probabilities … It does not change the existence of
market orders (N+, N−) nor the Hawkes dynamics of (λ+, λ−)» (p. 16). This triangular structure is
what makes well-posedness provable layer by layer (pp. 16–22).

### 5. Adverse selection enters as one-tick price jumps whose probability depends on intensity imbalance (pp. 10–11)

Imbalance $\iota=(\lambda^+-\lambda^-)/(\lambda^++\lambda^-)$ (eq. 14); $p^\pm=\bar p/(1+e^{\mp k(\iota-\theta)})$
(eq. 15); $dS=\sigma dW+\kappa(dM^+-dM^-)$ (eq. 17), $M^\pm$ the price-moving subflows. The marking is
«a reduced-form adverse-selection channel, not as a structural model of price formation» (p. 10).

### 6. The objective is CARA utility of terminal marked-to-market wealth with a quadratic terminal penalty (pp. 12–13)

$W_T=X_T+Q_TS_T-\tfrac\eta2Q_T^2$ (eq. 20), $U(w)=-e^{-\gamma w}$ (eq. 21). Finiteness needs bounded
inventory and exponential moments of $X_T$ and $S_T$ (Assumption 4.8, Lemma 4.9, p. 13).

### 7. The thesis proves the dynamic-programming machinery for a Hawkes-driven (non-Lévy) controlled state (pp. 14–29)

PRM/Ogata embedding (pp. 15–16), triangular strong existence and integrability (pp. 16–22), Itô/Dynkin
(pp. 23–26), the generator (44) with four disjoint channels (ask fill, bid fill, missed buy, missed
sell; each with a price mark) (pp. 26–27), and a stopping-time DPP following Pham (Thm. 6.3, p. 28).

### 8. The HJB is derived classically; viscosity is acknowledged as the right framework but not used (pp. 27, 29–30)

«in this thesis the viscosity perspective is discussed to clarify the proper PDE framework, while the
main derivation and verification argument is presented in the classical smooth-candidate setting»
(p. 2). HJB (51)–(52), p. 30; Remark 7.1: «rigorously, the DPP implies that V is a viscosity solution»
(p. 30).

### 9. Verification is conditional: a smooth solution, if it exists, is the value function (pp. 31–32)

Thm. 8.1 needs $C^1$ in $t$, $C^2$ in $s$, $C^1$ in $(\lambda^+,\lambda^-)$ and a measurable maximiser;
«Theorem 8.1 is conditional: it does not provide a solution of the HJB» (p. 32).

### 10. ⭐⭐ CARA factorisation removes cash and price, leaving a reduced HJB in $(t,q,\lambda^+,\lambda^-)$ (pp. 32–33)

$V=-e^{-\gamma x}e^{-\gamma qs}\Theta(t,q,\lambda^+,\lambda^-)$ (eq. 53), $\Theta(T,\cdot)=\exp(\tfrac{\gamma\eta}{2}q^2)$ (eq. 54).
Reduced HJB (eq. 60, p. 33):
$0=\partial_t\Theta+\tfrac12\sigma^2\gamma^2q^2\Theta-\beta_+(\lambda^+-\mu^+)\partial_{\lambda^+}\Theta-\beta_-(\lambda^--\mu^-)\partial_{\lambda^-}\Theta+\sup_{\delta}\{\mathcal J^\delta_a\Theta+\mathcal J^\delta_b\Theta+\mathcal J^\delta_{+0}\Theta+\mathcal J^\delta_{-0}\Theta\}$,
with e.g. $\mathcal J^\delta_a\Theta=\Lambda^a\big(e^{-\gamma q_0\delta^a}[(1-p^+)+p^+e^{-\gamma\kappa(q-q_0)}]\Theta(t,q-q_0,\lambda^{(+)})-\Theta(t,q,\lambda)\big)$
and $\mathcal J^\delta_{+0}\Theta=\Lambda^{+,0}\big([(1-p^+)+p^+e^{-\gamma\kappa q}]\Theta(t,q,\lambda^{(+)})-\Theta(t,q,\lambda)\big)$,
$\lambda^{(+)}=(\lambda^++a^{++},\lambda^-+a^{-+})$. Diffusive risk appears as an endogenous running
term $\tfrac12\sigma^2\gamma^2q^2\Theta$ (Remark 9.1). Only the price-level dimensions are removed; the
lifted intensity dimensions remain.

### 11. CARA verification needs exponential moments of Hawkes counts, supplied by Leblanc (2024) (pp. 34–36)

Lemma 9.3: subcritical stationary Hawkes has $\mathbb E\exp(\theta(N^+_T+N^-_T))<\infty$ for small
$\theta$; with bounded inventory and offsets this gives the Dynkin $L^2$ condition (Lemma 9.7) and
Prop. 9.1: the grid maximiser is optimal **for the finite-control-grid problem** (p. 36).

### 12. Data: LOBSTER messages for one stock, reduced to 2-D aggressive execution flow (pp. 36–40)

Events are mapped from LOBSTER codes; the control layer keeps only buy/sell market orders
$(N^+,N^-)$ (p. 38). Fano factors well above 1 and growing with bin width motivate Hawkes (p. 38–39,
Fig. 5). The stock and dates are not named; figures show a single intraday episode with mid ≈ 222.

### 13. ⭐ Calibration: weak cross-excitation, ms-scale memory, ρ(K) ≈ 0.54, and KS checks that formally reject (pp. 41–43)

Fig. 9 (p. 42), read off the heatmap: $K_{--}=0.538$, $K_{-+}=0.001$, $K_{+-}=0.030$, $K_{++}=0.432$,
$\rho(K)\approx0.538$. Decays ≈ $2.6\cdot10^2$ and $4.2\cdot10^2$ s⁻¹, so «most self- and
cross-excitation effects are realized within a few milliseconds» (p. 43). Time-rescaling KS: D = 0.092
(p = 0.0039) and D = 0.086 (p = 0.0049) (Fig. 12, p. 44), described only as a «calibration sanity
check» (p. 44). Stability is enforced by a barrier at $\rho_{\max}$; simulation optionally rescales $A$
to $\rho_{\rm sim}=0.9$ (p. 42).

### 14. Fills and price moves are reduced-form proxies calibrated from executions (pp. 44–46)

Fill proxy $f(\delta)=A_{\rm fill}e^{-k_{\rm fill}\max(\delta-\delta_0,0)}$ fitted to level-consumption
fractions (p. 44); logistic one-tick move probability in book imbalance fitted by MLE (p. 45). «selection
effects are possible because we only observe fills when trades occur» (p. 46).

### 15. ⭐⭐ Numerics: an IMEX finite-difference scheme on a $(q,\lambda^+,\lambda^-)$ grid with a finite tick grid of quotes (p. 46)

«inventory q on a bounded grid and Hawkes intensities (λ+, λ−) on bounded grids centered around fitted
stationary scales»; «quote offsets discretized on the empirical grid … so the HJB maximization is a
finite search»; «an IMEX scheme stabilizes stiff intensity drifts while keeping jump/control terms
explicit»; «post-jump intensity values are interpolated and clamped to grid bounds» (p. 46). Grid sizes,
time step and convergence checks are not reported.

### 16. ⭐ Evaluation is qualitative and against a fixed-skew baseline only (pp. 46–52)

Replay mode (historical mid) and simulation mode (fitted Hawkes) (p. 46). The only benchmark is
FixedSkew, «deliberately crude» (p. 47). Findings are reported as figures: the HJB policy skews and
protects in one-sided bursts and has a tighter inventory distribution (pp. 48–50, Figs. 16–20). «the main
outcome is a policy mechanism rather than a single headline P&L number» (p. 52). No PnL table, no
AS/GLFT/Poisson comparison, no regret.

### 17. Future work names exactly the scaling routes: sums of exponentials, sparse excitation, ADP/RL benchmarked against the HJB, cross-asset transfer (pp. 53–54)

«approximate dynamic programming methods can be used to learn policies from simulation on Hawkes
states and benchmark them against HJB-based policies in the current framework» (p. 54); «sum-of-
exponentials with a sparse excitation structure is often the sweet spot» (p. 53). Cross-asset is meant
as calibration transfer across assets, not a multi-asset control problem (p. 54).

## Figures and tables

- Fig. 9 (p. 42): branching-matrix heatmap. Fig. 11 (p. 43): fitted kernels. Fig. 12 (p. 44): KS checks.
- Fig. 15 (p. 46): optimal offsets vs inventory on a state slice.
- Figs. 16–20 (pp. 47–50): replay paths, P&L decomposition, quote ranks, inventory histogram (HJB vs FixedSkew).

No figures extracted (write scope limited to this page).

## What this source does not address

- **Any closed form or approximation.** Neither GLFT linearisation nor a quadratic/Riccati ansatz is
  attempted; the reduced HJB is solved directly on a grid.
- **Quantitative benchmarking.** No numbers against AS, GLFT, a Poisson-optimal policy or RL; no
  regret or optimality gap; no convergence study of the grid solver.
- **More than one asset.** Single stock; cross-excitation is buy↔sell only.
- **Fill-driven excitation.** Excluded by the price-taker convention (p. 16).
- **Non-exponential kernels.** Only mentioned as future work (p. 53).

## Model card

| Field | Entry |
|---|---|
| Assets | 1 (unnamed LOBSTER stock, single intraday episodes) |
| Kernel | exponential, one decay per source component (bivariate); sum-of-exponentials only discussed |
| Excitation | self and cross-side (buy↔sell), full 2×2 matrix (eq. 11); estimated cross terms small (0.030, 0.001) |
| Who excites the flow | all market orders, filled or missed (flow-driven); maker is a price taker (Remark 4.4, p. 12) |
| Objective | CARA utility of terminal MtM wealth with quadratic terminal penalty (eqs. 20–21) |
| Solution method | exact Markov lift in $(\lambda^+,\lambda^-)$, CARA factorisation to $\Theta(t,q,\lambda^+,\lambda^-)$, IMEX finite differences on a 3-D grid with finite tick control set; classical verification for the finite-grid problem |
| Benchmark | FixedSkew (static offsets, optional static inventory tilt) |
| Reported numbers | none in tables; qualitative figures only (tighter inventory, burst-dependent skew); calibration $\rho(K)\approx0.538$ |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 3, 4, 5, 6, 10, 13, 15, 16, 17.**

### What this focus needs beyond the Kernthesen

1. **Closure status: exact lift, no reduction.** The thesis keeps the full lifted state
   $(q,\lambda^+,\lambda^-)$ and solves eq. (60) numerically. CARA removes $x$ and $s$ exactly
   (Kernthese 10), as in GLFT, but the intensity coordinates stay. No attempt at a GLFT-type
   substitution that would linearise in $q$, and none at a quadratic ansatz.
2. **The flow-driven structure is visible in eq. (60).** For buy orders, fill and miss terms combine
   to $\lambda^+\big[f_a(\delta^a)e^{-\gamma q_0\delta^a}c_1\,\Theta(q-q_0,\lambda^{(+)})+(1-f_a(\delta^a))c_0\,\Theta(q,\lambda^{(+)})-\Theta(q,\lambda)\big]$
   (with $c_0,c_1$ the price-mark factors). *Inference:* the optimiser compares $\Theta(q-q_0,\lambda^{(+)})$
   with $\Theta(q,\lambda^{(+)})$, both at the **post-order** intensity, which is the flow-driven shadow
   price of [[who-excites-the-flow]] and `problem-anatomy` §3. The extra $-\Theta(q,\lambda)$ term is
   what blocks an exact exponential linearisation in this convention (`problem-anatomy` §3b). The
   thesis does not discuss this.
3. **Adverse selection couples price and intensity.** Because $p^\pm$ depends on $\lambda$ through
   imbalance, even the miss terms carry $e^{\mp\gamma\kappa q}$ factors: intensity bursts move the mid
   against inventory. This is an additional $\lambda$-dependence of the coefficients that a Riccati
   ansatz would have to absorb (relevant to D2).
4. **Is it a closed-form / exact / RL three-way comparison?** No. It supplies only the "exact" leg
   (grid-lifted HJB, 2-D intensity), compared with a static FixedSkew baseline; RL/ADP is future work
   (p. 54). Even the exact leg is not validated (no grid-refinement study, interpolation and clamping
   at the boundaries, p. 46).
5. **Multi-asset.** None. *Inference:* the lift scales as $2d$ intensity coordinates plus $d$
   inventories, so the grid approach of this thesis is already 3-D for $d=1$ and becomes infeasible
   fast; the thesis itself says that beyond «a handful of variables, full grid-based PDE methods become
   expensive» (p. 54).
6. **Possible sign slip in eq. (60).** $V=-E\Theta$ with $E>0$, so dividing $\partial_tV+\sup_\delta\mathcal L^\delta V=0$
   by $-E$ should turn the $\sup$ into an $\inf$ over $\delta$ ($\Theta$ is a disutility multiplier). Eq.
   (60) keeps $\sup$ (p. 33). Whether the code minimises is not verifiable from the text.

### Direct quotes

> "Choosing an exponential (or a sum of exponentials) kernel is therefore a tractability commitment: the convolution admits a finite-dimensional Markov embedding, so the augmented state (St, Qt, Xt, λt), that will be properly defined in section 4, is Markov and admits a controlled generator." (p. 7)

> "The aggressive order flow (N+, N−) drives the Hawkes intensity state (λ+, λ−) via (11). The market maker is price-taking and does not affect (N+, N−) nor (λ+, λ−)." (p. 12)

> "As soon as the state dimension grows beyond a handful of variables, full grid-based PDE methods become expensive." (p. 54)

### Examples & illustrations

- Fig. 9 (p. 42): an empirical branching matrix with nearly zero cross terms ($0.030$, $0.001$) next to
  diagonal $0.43$–$0.54$: on this stock, buy/sell cross-excitation is weak at the ms scale.
- Fig. 15 (p. 46): HJB offsets vs inventory on a slice, skewing linearly-looking in $q\in[-30,30]$.

### Boundary of this focus

The thesis is a rigorous treatment of the exact lifted problem for one asset and exponential kernels,
not a source on closures. Its value for the project is (a) a worked CARA reduction of the flow-driven
Hawkes HJB that matches the project's generator structure, and (b) an open-source grid solver that
could serve as an exact benchmark leg. It carries no quantitative comparison.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]], [[glft-2013-model]]
- Concepts: [[hawkes-process]], [[markov-lift]], [[branching-matrix]], [[who-excites-the-flow]]
- Other works (not checked against the library): Bacry–Mastromatteo–Muzy 2015, Brémaud 1981, Brémaud & Massoulié 1996, Cartea–Jaimungal–Penalva 2015, Leblanc 2024 (exponential moments), Lu & Abergel 2018, Pham 2009, Fleming & Soner 2006, Huang–Lehalle–Rosenbaum 2015, Jain et al. 2024.

## Connections

- Builds on: [[markov-lift]] (exponential embedding as the enabling step); [[who-excites-the-flow]] (flow-driven, price-taker convention).
- Compare: [[jusselin-2021-persistent-order-flow]] (general kernels, viscosity solutions; not cited by the thesis); [[martin-2026-market-making-hawkes]] (lift + neural PDE instead of grid); [[barzykin-2026-hawkes-driven-otc]] (same exact-lift-on-a-grid as validation benchmark, plus a Riccati approximation the thesis lacks); [[bathini-2026-dynamic-market-making]] (freezes intensity instead of lifting it).
