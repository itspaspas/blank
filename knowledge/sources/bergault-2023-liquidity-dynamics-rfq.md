---
title: "Bergault & Guéant 2023 — Liquidity Dynamics in RFQ Markets and Impact on Pricing"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: bergault-2023-liquidity-dynamics-rfq
depth: standard
tags: [market-making, otc, rfq, corporate-bonds, markov-modulated-poisson, regime-switching, liquidity-imbalance, micro-price, fair-transfer-price, em-algorithm, quadratic-hamiltonian-approximation]
relations:
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "«Using the same approach as in [6], we propose in the following paragraphs a quadratic approximation of the value functions» with Taylor coefficients α_i = H^(i)(0) (p. 26); applied per liquidity regime."
  - target: bergault-2021-closed-form-approximations
    type: builds-on
    confidence: extracted
    because: "Ref. [6] (BEGV 2021) is named as the source of the quadratic approximation used to avoid Euler schemes that are «unfeasible if the one-asset market-making model is replaced by a multi-asset one» (p. 26)."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "The FTP market maker is a one-asset BEGV/Guéant-type model with S-curve fills and quadratic running penalty, solved by the BEGV quadratic approximation (pp. 12, 26)."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: inferred
    because: "The quadratic approximation yields m_b·m_a scalar Riccati ODEs for A_{j_b,j_a} coupled linearly through the generator Q (p. 27); the paper does not use the word 'Riccati' and has no matrix (multi-asset) version."
  - target: hawkes-process
    type: contradicts
    confidence: extracted
    because: "Rejects Hawkes for RFQ flow: «in a market with limited post-trade transparency, we argue that it is odd to assume that an RFQ sent by a client is the consequence of an RFQ sent by another client» (p. 4); uses an MMPP instead."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "FTP is motivated by «market making models à la Avellaneda-Stoikov [1]» in which asymmetric flows make the maker skew quotes even at zero inventory (p. 4)."
  - target: cartea-2014-buy-low-sell
    type: cites
    confidence: extracted
    because: "Objective uses «the quadratic running penalty – linked to the objective function proposed in [11]» (pp. 13–14), [11] = Cartea–Jaimungal–Ricci 2014."
  - target: markov-lift
    type: mentions
    confidence: inferred
    because: "The finite-state chain is the intensity state itself, so no lift of a path-dependent intensity is needed: the HJB is indexed by regime (p. 12). Finite-state analogue of a lifted intensity, not stated by the authors."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Neither convention: RFQ intensities are an exogenous continuous-time Markov chain (p. 4); no order (fill or not) moves the intensity."
  - target: khabou-2025-markov-approximation-hawkes
    type: mentions
    confidence: inferred
    because: "Not cited. A finite-state Markov approximation of a Hawkes intensity would turn this paper's regime-indexed Riccati system into a benchmark for Hawkes; project inference."
---

# Liquidity Dynamics in RFQ Markets and Impact on Pricing

## Bibliographic Details

Bergault, Philippe and Olivier Guéant. 2023. *Liquidity Dynamics in RFQ Markets and Impact on
Pricing*. arXiv:2309.04216 [q-fin.TR]; v3 dated 19 June 2024. 34 pp. (incl. Appendix A). Affiliations:
Université Paris Dauphine-PSL (Ceremade); Université Paris 1 Panthéon-Sorbonne (CES). Research
supported by J.P. Morgan (anonymised high-yield corporate-bond RFQ data).

**Read: arXiv 2309.04216v3 (preprint); page/equation numbers follow it.** Printed page numbers
coincide with PDF page numbers. Whether a journal version exists was not verified in this ingest
(the library entry records only the preprint); if one exists, add `based_on: preprint`.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $(\lambda^b_t,\lambda^a_t)$ | bidimensional RFQ intensity, a continuous-time Markov chain on $\{\lambda^{1,b},\dots,\lambda^{m_b,b}\}\times\{\lambda^{1,a},\dots,\lambda^{m_a,a}\}$ | $\lambda_t$, but **finite-state**, exogenous, no excitation |
| $Q\in M_{m_bm_a}$ | rate (generator) matrix of the chain, lexicographic state order | ⚠ clashes with project $Q$ (inventory bound) |
| $\Lambda^b,\Lambda^a$; $\tilde\Lambda^b=\Lambda^b\otimes I_{m_a}$ | diagonal intensity matrices | ⚠ not the GLFT amplitude $\Lambda$ |
| $\kappa$ | price-drift loading on intensity imbalance, $dS_t=\sigma dW_t+\kappa(\lambda^a_t-\lambda^b_t)dt$ | no project symbol (alpha signal); ⚠ not a GLFT decay $k$ |
| $\sigma,\gamma$ | arithmetic volatility; risk aversion (quadratic penalty $\tfrac\gamma2\sigma^2q^2$) | $\sigma,\gamma$ (risk-adjusted objective) |
| $z$ | single constant RFQ size | — |
| $\delta^b,\delta^a$; $f^b,f^a$ | quote distances; S-curve (fill probability) | $\delta^b,\delta^a$; $f(\delta)$ |
| $H^{b/a}(p)=\sup_\delta f^{b/a}(\delta)(\delta-p)$ | Hamiltonian | $H$ (scalar, one asset) |
| $\alpha^{b/a}_i=H^{b/a(i)}(0)$; $\Delta^{b/a}_{i,k}=\alpha^{b/a}_iz^k$ | Taylor coefficients of $H$ at 0 | $\alpha_2\leftrightarrow h_2$ |
| $\theta^{j_b,j_a}(t,q)$; $\check\theta^{j_b,j_a}=-q^2A_{j_b,j_a}-qB_{j_b,j_a}-C_{j_b,j_a}$ | value function per regime; quadratic approximation | $\theta(t,q,\lambda)$ with $\lambda$ restricted to regimes; $A,B,C$ scalar |
| $\pi$ (vector), $\pi^{1,2},\pi^{2,1}$ | filtered posterior over regimes (eq. 2); probabilities of the two imbalanced states | — |
| $\beta^{i,b},\beta^{i,a}$ | asset loadings on the aggregate chain (App. A.2) | ⚠ not a Hawkes decay $\beta$ |
| $v(\lambda^b,\lambda^a)$ | long-run cumulative expected imbalance (eq. 3) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (mid-price, weighted mid-price, micro-price; RFQ information; two ideas) | 1–4 |
| ✓ F1 | 2.1 Modelling framework: bidimensional MMPP, why not Hawkes | 4 |
| — | 2.2.1 Likelihood of a sample ($G(t)=\exp((Q-\tilde\Lambda^b-\tilde\Lambda^a)t)$) | 4–6 |
| — | 2.2.2 EM algorithm (hidden regime path; updates for $\Lambda^b,\Lambda^a,Q$) | 6–9 |
| ✓ | 2.2.3 Estimating the current state (filter, eq. 2) | 9–10 |
| ✓ | 3.1 Micro-price for RFQ markets: definition, $v_T$ linear ODE, eq. (3)–(4), assumptions | 10–11 |
| ✓ F1 | 3.2.1 From a market-making model to a fair transfer price: regime-indexed HJB, quotes, ergodic skew, FTP eq. (5) | 11–13 |
| ✓ | 3.2.2 Remarks on FTP (relation to LOB imbalance, reference-price shift, $z$, $\gamma$ as degree of freedom) | 13–14 |
| — | 4.1–4.2 Data (J.P. Morgan HY bonds, 4 sectors); MMPP estimates (Table 1, Figs. 1–8) | 14–19 |
| — | 4.3 Micro-price: estimation of $\kappa$ (Table 2), micro-prices (Table 3, Figs. 9–14) | 20–24 |
| ✓ F1 | 4.4.1 S-curves (logistic); 4.4.2 Solving HJB: Euler scheme, risk limits, **quadratic approximation** ($A,B,C$ ODEs) | 25–27 |
| ✓ F1 | 4.4.3 FTP in practice: **Euler vs quadratic approximation** (Table 4), Figs. 16–17 | 27–29 |
| ✓ | Conclusion | 29 |
| — | A.1 Exchangeability assumption (symmetric EM) | 32 |
| ✓ F1 | A.2 Multi-asset one-factor liquidity extension (estimation only) | 33–34 |

## Kernthesen

### 1. ⭐⭐ RFQ liquidity is a bidimensional Markov-modulated Poisson process, not a Hawkes process (p. 4)

RFQ counts at bid and ask are point processes whose intensities must be stochastic. The authors
reject Hawkes explicitly: Hawkes processes are «self-excited processes and, in a market with
limited post-trade transparency, we argue that it is odd to assume that an RFQ sent by a client is
the consequence of an RFQ sent by another client» (p. 4). Instead the pair $(\lambda^b,\lambda^a)$ is
a continuous-time Markov chain on a product of finite sets with generator $Q$, so that liquidity
shocks can be «sometimes symmetric and sometimes asymmetric» (p. 4). Independence of the two
sides is the special case $Q=Q^b\otimes I+I\otimes Q^a$ (fn. 10, p. 4).

### 2. The MMPP likelihood is a product of matrix exponentials and is maximised by an EM algorithm over the hidden regime path (pp. 4–9)

The no-arrival transition matrix solves $G'=G(Q-\tilde\Lambda^b-\tilde\Lambda^a)$, so
$G(t)=\exp((Q-\tilde\Lambda^b-\tilde\Lambda^a)t)$ (p. 5) and the sample likelihood is
$\pi_0^\top\prod_n\exp((Q-\tilde\Lambda^b-\tilde\Lambda^a)(t_n-t_{n-1}))\tilde\Lambda^{s_n}e$ (p. 6).
Direct maximisation is hard; an EM algorithm (generalising Rydén 1996) treats the regime path as
hidden and updates intensities as expected counts over expected sojourn times and $Q$ off-diagonals
as expected transitions over sojourn times (pp. 6–9). «The only computational difficulty lies in
finding a scaling factor to avoid ending up with very low or very high values» (p. 9).

### 3. The current regime is never observed; it is filtered as a posterior vector (pp. 9–10, 17)

Given parameters, the posterior over regimes at time $t$ is the normalised forward product (eq. 2,
p. 10). Empirically the probabilities of being in an imbalanced state rarely approach 1: «it is
hard to be certain that a disequilibrium in RFQs indeed corresponds to an underlying asymmetric
regime» (p. 17). All price notions are therefore reported as posterior means with a standard
deviation reflecting regime uncertainty only (pp. 11, 13).

### 4. ⭐ A micro-price for RFQ markets: price drifts in proportion to the intensity imbalance (pp. 10–11)

With $dS_t=\sigma dW_t+\kappa(\lambda^a_t-\lambda^b_t)dt$, the micro-price is
$S^{\rm micro}_t=\lim_{T\to\infty}E[S_T\mid S_t,\lambda^b_t,\lambda^a_t]=S_t+\kappa v(\lambda^b_t,\lambda^a_t)$.
$v_T$ solves a linear ODE driven by $Q$; under exchangeability and the assumption that every
asymmetric state can return to a symmetric one, $Q^{ns}$ is strictly diagonally dominant
(Gershgorin) and $v=-(Q^{ns})^{-1}(I\otimes\lambda^{vec}-\lambda^{vec}\otimes I)^{ns}$ (eq. 3, p. 11).
The authors flag the linear-drift assumption as the questionable one: «Parsimony clearly guided our
modeling choice» (p. 11).

### 5. ⭐⭐ Fair Transfer Price = mid of a zero-inventory, infinite-horizon market maker who knows the liquidity regime (pp. 11–13)

A one-asset market maker with S-curve fills, constant size $z$, objective
$E\int_0^T(z\lambda^b\delta^bf^b+z\lambda^a\delta^af^a+\kappa(\lambda^a-\lambda^b)q-\tfrac\gamma2\sigma^2q^2)dt$
(p. 12) has one value function per regime, solving a system of HJB equations coupled through $Q$.
If $Q$ is irreducible an ergodic limit exists and a time-independent skew is defined; then
$S^{\rm FTP}_t=S_t+\tfrac12{\rm skew}$ (p. 13). The skew «"projects" the asymmetry of the market
liquidity into the price space» (p. 13).

### 6. ⭐⭐ The regime-indexed HJB: intensities enter as multipliers of the Hamiltonian; regimes are coupled linearly by the generator (p. 12)

$\partial_t\theta^{j_b,j_a}+\kappa(\lambda^{j_a,a}-\lambda^{j_b,b})q-\tfrac12\gamma\sigma^2q^2+\sum_kQ_{(j_b,j_a),k}\theta^k
+z\lambda^{j_b,b}H^b(\tfrac{\theta^{j_b,j_a}(t,q)-\theta^{j_b,j_a}(t,q+z)}{z})+z\lambda^{j_a,a}H^a(\cdot)=0$,
$\theta(T,q)=0$ (p. 12). The intensity state is exogenous: trades change $q$ but never the regime, so
Hamiltonian finite differences are taken within one regime. Optimal quotes are
$\tilde\delta^{b}(p)=f^{b-1}(-H^{b\prime}(p))$ evaluated at the regime's finite difference (p. 12).

### 7. ⭐⭐ Quadratic Hamiltonian approximation per regime yields coupled scalar Riccati ODEs for $A$ and linear ODEs for $B,C$ (pp. 26–27)

Euler schemes become costly when $m_b\times m_a$ is large «or even unfeasible if the one-asset
market-making model is replaced by a multi-asset one» (p. 26). Following BEGV [6], $H^{b/a}$ is
replaced by its second-order Taylor polynomial at $p=0$ (p. 26). With $\Delta_{i,k}=\alpha_iz^k$, the
approximation $\check\theta^{j_b,j_a}=-q^2A_{j_b,j_a}-qB_{j_b,j_a}-C_{j_b,j_a}$ is exact for the
approximate HJB, with
$A'_{j}=2(\lambda^{j_b,b}\Delta^b_{2,1}+\lambda^{j_a,a}\Delta^a_{2,1})A_j^2-\tfrac12\gamma\sigma^2-\sum_kQ_{jk}A_k$,
$B_j$ linear given $A$ (carrying the drift term $\kappa(\lambda^{j_a,a}-\lambda^{j_b,b})$ and an
$A^2$ term from $\Delta_{2,2}$ asymmetry), and $C_j$ linear given $A,B$ (p. 27). So the system is
$3m_bm_a$ scalar ODEs; the factor is handled **exactly** by enumeration, not by expansion.

### 8. ⭐ The quadratic approximation preserves the ergodic results and is judged good by FTP agreement with an implicit Euler scheme (pp. 27–28)

«Moreover, asymptotic results on value functions continue to hold on their approximations» (p. 27),
with no error bound. The test (Table 4, p. 28): for 16 bonds, $\gamma$ is calibrated separately for
each method so that zero-inventory quotes match composite bid/ask; the resulting FTPs in the two
fully imbalanced states agree to at most about 0.01 price points (e.g. bond 4.2: 104.691 vs
104.701), although the calibrated $\gamma$ differ by up to a factor ≈ 1.9 (bond 1.4:
$8.5\times10^{-7}$ vs $1.6\times10^{-6}$). Bond 3.2 shows 92.423 vs 94.422, outside the bid–ask
range, almost surely a typo.

### 9. FTP adjustments are small, smaller than micro-price adjustments (pp. 27, 29)

«We see that adjustments are always small», because an imbalanced-market maker «can slightly skew
their quotes to deter risk-increasing trades and transform requests into trades when trades would
result in a less risky position» (p. 27). This rests on S-curves being regime-independent; the
authors «found no empirical evidence of the influence of intensities on fill rates» (p. 27).

### 10. Imbalance has positive (if often insignificant) predictive power for bond prices (p. 20)

$\kappa$ is estimated by regressing price moves on posterior-weighted $v$; all 16 estimates are
positive though «not all significantly different for 0» (Table 2, p. 20). Micro-prices leave the
composite bid–ask spread only when one is nearly sure the flow is imbalanced (pp. 21–24).

### 11. ⭐ Multi-asset liquidity as a one-factor, CAPM-like aggregate chain (pp. 33–34)

App. A.2: $(\lambda^{i,b}_t,\lambda^{i,a}_t)=(\beta^{i,b}\lambda^b_t,\beta^{i,a}\lambda^a_t)$, one common
regime chain with asset loadings normalised to sum to 1 (fn. 21, p. 33). The likelihood factorises,
so RFQs can be pooled across assets to estimate $Q,\Lambda$ by the one-asset EM, and the loadings
are just RFQ shares $\beta^{i,b}=K^{i,b}/\sum_jK^{j,b}$ (p. 34). This is used for sector-level
estimation (p. 14); the control problem stays one-asset.

### 12. Empirical liquidity regimes differ by sector; two intensities suffice to separate low and high liquidity (pp. 14–17)

With $m=2$ and exchangeability, EM converges in about 50 steps; Table 1 shows low/high intensities
from ≈ 7–16 to ≈ 28–82 RFQs/day and sector-specific transition structures (e.g. a very stable
low/low state in sector 2, slow transitions in sector 4) (p. 17).

### 13. FTP is a valuation tool, so the market-making model may stay simple; $\gamma$ is a calibration knob (pp. 13–14)

«The role of the market making model here is not to provide quotes that will be used inside a
trading algorithm, but rather to project information regarding liquidity levels, liquidity
imbalances, and volatility into the price space» (p. 14). $\gamma$ is fitted to observed spreads; the
FTP is invariant to constant shifts of the reference price (p. 13). Multi-asset models ([5],[6],[23])
are named as possible replacements but not used (p. 14).

## Figures and tables

- Figs. 1–4 (pp. 15–17): RFQs per day, bid vs ask, four sectors — simultaneous and one-sided liquidity bumps.
- Table 1 (p. 17): estimated two-state intensities and $4\times4$ generators per sector.
- Figs. 5–8 (pp. 18–19): histograms of filtered imbalanced-state probabilities.
- Table 2 (p. 20): $\beta,\kappa,\sigma$ per bond. Table 3 (p. 21): micro-prices in imbalanced states.
- Figs. 9–14 (pp. 22–24): micro-price vs state probabilities.
- Fig. 15 (p. 25): logistic S-curves per sector.
- **Table 4 (p. 28): calibrated $\gamma$ and FTP, Euler (a) vs quadratic approximation (b)** — the accuracy test.
- Figs. 16–17 (pp. 28–29): FTP vs state probabilities.

## What this source does not address

- **Self- or cross-exciting flow.** Hawkes is rejected on modelling grounds (p. 4); intensities are
  an exogenous finite-state chain. For Hawkes-driven OTC flow see
  [[barzykin-2026-hawkes-driven-otc]]; for why Hawkes liquidity breaks the closure when fills
  excite see [[bergault-2024-price-aware-automated]] (which cites this paper and reuses the MMPP).
- **Multi-asset control.** The market maker is one-asset; multi-asset appears only in estimation
  (App. A.2). Matrix Riccati closures for $d$ assets: [[bergault-2021-closed-form-approximations]].
- **Perturbation or asymptotics in the intensity.** None; the factor is enumerated exactly.
- **Error bounds** for the quadratic Hamiltonian approximation; **value or P&L comparisons** of
  the approximate vs exact strategy at nonzero inventory; regret.
- **Regime-dependent fill curves** (assumed away, p. 27); multiple sizes; client tiering (named as
  extensions, p. 13).

## Model card

| Field | Value |
|---|---|
| Assets | 1 in the control problem; $d$ in estimation only (one-factor aggregate chain, App. A.2, pp. 33–34) |
| Kernel | n/a — no excitation kernel; intensities follow a finite-state continuous-time Markov chain (bidimensional MMPP, $m=2$ per side in the data) |
| Excitation | none (self, cross-side, cross-asset); cross-side dependence only through the joint generator $Q$; cross-asset co-movement only via the common chain with loadings $\beta^i$ |
| Who excites the flow | n/a — nobody; flow is exogenous regime-modulated Poisson |
| Objective | risk-adjusted expected P&L, quadratic running penalty $\tfrac\gamma2\sigma^2q^2$, plus imbalance-drift term $\kappa(\lambda^a-\lambda^b)q$ (p. 12) |
| Solution method | (a) implicit Euler on the regime-indexed HJB with risk limits; (b) BEGV quadratic Hamiltonian approximation → $m_bm_a$ coupled scalar Riccati ODEs + linear ODEs (pp. 26–27); ergodic limit for FTP |
| Benchmark | (b) vs (a), compared on FTP only, $\gamma$ recalibrated per method (Table 4, p. 28) |
| Reported regret / gap numbers | none; FTP differences ≤ ≈ 0.01 price points across 16 bonds (bond 3.2 entry a typo) |

<!-- ═══ FOKUS ═══ -->

## Focus: Perturbative/asymptotic closed forms for multi-asset market making with a stochastic intensity factor (Hawkes or Markov-modulated): which expansion, around which point, with which small parameter and error order; whether it closes into finite matrix ODEs; how accuracy is tested; how much of Stage 2a it already covers. — 2026-10-26

**Carries Kernthesen 1, 6, 7, 8, 11, 13.**

### What this focus needs beyond the Kernthesen

1. **Which expansion, around which point.** Only one expansion: the Hamiltonian $H(p)$ to second
   order around $p=0$ (p. 26), exactly BEGV's. There is **no** expansion in the intensity factor;
   the factor is finite-state and the value function is carried exactly per regime (Kernthese 7).
   Small parameter / error order: none stated; the only accuracy statement is that ergodic
   results «continue to hold» (p. 27).
2. **Closure into finite ODEs.** Yes, but scalar: $m_bm_a$ Riccati ODEs for $A_j$ coupled by the
   linear term $-\sum_kQ_{jk}A_k$, then linear ODEs for $B_j$ given $A$ and $C_j$ given $(A,B)$
   (p. 27). The $A$-equation's quadratic coefficient is **linear in the regime intensities**,
   $2(\lambda^{j_b,b}\Delta^b_{2,1}+\lambda^{j_a,a}\Delta^a_{2,1})$, the same place where Stage 2a's
   $\lambda$-dependence of $A$ originates [I]. The regime coupling plays the role that the
   generator of the lifted Hawkes intensity plays in Stage 2a's $A(t,\lambda)$ PDE [I].
3. **Accuracy test design and its limits.** Table 4 compares FTPs (zero-inventory mid quotes in the
   two fully imbalanced regimes) from the quadratic approximation and from an implicit Euler
   scheme, after recalibrating $\gamma$ separately for each (p. 27). This tests the
   approximation's skew at $q=0$ after a refit; it does not test the value function, the inventory
   skew at $q\neq0$, or P&L. Stage 2a's planned test against an exact solution would be a
   stricter design.
4. **Bearing on Stage 2a: a ready-made exact-in-factor comparator [I].** For a finite-state
   intensity, the regime-indexed system closes without perturbation. A $d$-asset version (not in
   the paper) would replace each scalar $A_j$ by a $d\times d$ matrix: $m$ coupled matrix Riccati
   ODEs. Paired with a Markov-chain approximation of the Hawkes intensity
   ([[khabou-2025-markov-approximation-hawkes]]), that gives a benchmark against which Stage 2a's
   first-order expansion around $m_t$ could be checked, and it competes with it as a closure. Its
   cost scales with the number of regimes, which explodes for $\lambda\in\mathbb R^{2d}$ — the
   argument for perturbation rather than enumeration.
5. **Modelling stance to answer in Stage 2a.** The authors' objection to Hawkes (RFQs do not cause
   RFQs under limited transparency, p. 4) is market-specific; Stage 2a needs a sentence on which
   market's flow it models. Bergault et al. 2024 later switch from Hawkes to MMPP for a different,
   technical reason (fills exciting flow), which Stage 2a avoids by the flow-driven convention.

### Overlap with Stage 2a

| Element | Verdict | Evidence |
|---|---|---|
| (a) multi-asset matrix Riccati with a stochastic intensity/liquidity factor | **partly** | Stochastic factor yes, Riccati system yes, but one asset: scalar $A_{j_b,j_a}$ per regime (p. 27). Multi-asset only named as motivation: Euler «unfeasible if the one-asset market-making model is replaced by a multi-asset one» (p. 26). |
| (b) perturbative/asymptotic expansion in that factor | **not** | Factor enumerated exactly; the only expansion is $H$ around $p=0$: «A natural choice for the functions $\check H^b$ and $\check H^a$ derives from Taylor expansions around $p=0$» (p. 26). |
| (c) order-1 system linear given order 0 | **not** (no orders in the factor) | The only linear-given-nonlinear cascade is $A\to B\to C$ in inventory powers (p. 27), which BEGV already has. |
| (d) explicit small parameter + error order | **not** | «Moreover, asymptotic results on value functions continue to hold on their approximations» (p. 27) is the only claim; no small parameter, no bound. |
| (e) accuracy test against an exact/numerical solution | **partly** | Euler vs quadratic approximation, on FTP only, with $\gamma$ refitted per method: «in terms of FTP, the results obtained with the two numerical methods are almost identical» (p. 27, Table 4 p. 28). |
| (f) cross-asset coupling of the factor | **partly** (estimation only) | One common chain with loadings: «$(\lambda^i_t)_t=(\beta^{i,b}\lambda^b_t,\beta^{i,a}\lambda^a_t)_t$» (p. 33) — perfectly comonotone, no excitation, not in the control problem. |

**Net:** the source does not pre-empt Stage 2a's contribution (perturbation in a continuous
intensity factor, linear order-1 system, explicit scaling and error order, $d$ assets). It is the
finite-state, one-asset, exact-in-factor precedent for "quadratic Hamiltonian + stochastic
liquidity ⇒ coupled Riccati ODEs", and must be cited as such, together with
[[bergault-2024-price-aware-automated]] eq. (43), which reuses the same construction.

### Direct quotes (for the draft)

> "Hawkes processes are indeed very good at modeling events that may happen in clusters. However, they are self-excited processes and, in a market with limited post-trade transparency, we argue that it is odd to assume that an RFQ sent by a client is the consequence of an RFQ sent by another client." (p. 4)

> "Euler schemes can be time-consuming when the number of states $m_b\times m_a$ is large, or even unfeasible if the one-asset market-making model is replaced by a multi-asset one. Using the same approach as in [6], we propose in the following paragraphs a quadratic approximation of the value functions." (p. 26)

> "Moreover, asymptotic results on value functions continue to hold on their approximations. This kind of approximations has been used in [3, 5] with great success in terms of risk management. We investigate the quality of the approximation in terms of FTPs below." (p. 27)

> "Depending on the numerical method we use, γ calibrated to composite bid and ask prices takes different values. However, in terms of FTP, the results obtained with the two numerical methods are almost identical, as shown in Table 4." (p. 27)

### Examples & illustrations (for later drafting)

- Table 4 (p. 28): bond 1.1, imbalanced states, FTP 103.458/103.458 and 103.728/103.729 (Euler / quadratic) — a concrete instance of near-identical outputs after refitting $\gamma$; bond 1.4 shows the larger $\gamma$ gap (×1.9) with FTP within 0.005.
- The $A$-ODE (p. 27): a two-line display showing intensity entering the Riccati coefficient linearly and regimes coupling through $Q$ — usable to introduce why a stochastic intensity makes $A$ state-dependent.

### Boundary of this focus

The paper has no perturbation in the factor, no multi-asset control and no error analysis; items
2 and 4 above (comparator construction, link to Stage 2a's PDE) are project inference.

## Mentioned entities

- Models: [[begv-2021-model]], [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]] (objective lineage via ref. [11]).
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[hawkes-process]] (rejected), [[markov-lift]], [[who-excites-the-flow]].
- Other works (not in wiki): Stoikov 2018 (micro-price); Rydén 1996 (EM for MMPP); Fischer & Meier-Hellstern 1993 (MMPP cookbook); Guéant & Manziuk 2020 (ergodic control on graphs); Barzykin–Bergault–Guéant 2022/2023 (FX market making with quadratic approximation, refs. [3]–[5]); Bergault & Guéant 2021 (size matters, `bergault-2020-size-matters-otc` in library); Guéant & Pu 2018 (particle filtering for bond mid-prices).

## Connections

- Builds on: [[bergault-2021-closed-form-approximations]] / [[begv-2021-model]] — same quadratic Hamiltonian approximation, applied per liquidity regime (p. 26).
- Builds on: [[hamiltonian-quadratic-approximation]] (Taylor at $p=0$), and yields a regime-coupled form of [[matrix-riccati-equation]] (scalar here).
- Contradicts (modelling stance): [[hawkes-process]] for RFQ flow (p. 4).
- Cites: [[avellaneda-stoikov-model]] (p. 4), [[cartea-2014-buy-low-sell]] (objective, pp. 13–14).
- Cited by / reused in: [[bergault-2024-price-aware-automated]] (MMPP liquidity, eq. 43).
- Possible benchmark pairing (project inference): [[khabou-2025-markov-approximation-hawkes]].
