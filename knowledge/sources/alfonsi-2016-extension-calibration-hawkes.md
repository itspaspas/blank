---
title: "Alfonsi & Blanc 2016 — Extension and calibration of a Hawkes-based optimal execution model"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: alfonsi-2016-extension-calibration-hawkes
depth: standard
based_on: preprint
tags: [optimal-execution, hawkes-process, multi-exponential-kernel, sum-of-exponentials, propagator, calibration, directional-branching-ratio, price-manipulation, backtest, flow-driven, closed-form]
relations:
  - target: alfonsi-2016-dynamic-optimal-execution
    type: builds-on
    confidence: extracted
    because: "«We provide some theoretical extensions and a calibration protocol for our former dynamic optimal execution model» (abstract, p. 1); the model «extends the one considered in [1] to general decay kernels» (p. 2)."
  - target: markov-lift
    type: builds-on
    confidence: extracted
    because: "Completely monotone kernels with finite-support mixtures give a Markov state (S, D^i, κ±(i)): «the process (P, S, D^i, κ±(i)) satisfies the Markov property» (§2.1, pp. 3–4)."
  - target: who-excites-the-flow
    type: supports
    confidence: extracted
    because: "Flow-driven: the strategic trader's trades «affect the price in the same fashion as other trades, but leave unchanged the flow of orders N» (p. 5)."
  - target: matrix-riccati-equation
    type: mentions
    confidence: extracted
    because: "With a multi-exponential propagator the optimal strategy «is characterized through a matrix Riccati equation» even without order flow, and the cost ODEs «would be much more intricated» (p. 7); the closed form is kept only for a mono-exponential propagator."
  - target: branching-matrix
    type: mentions
    confidence: extracted
    because: "Defines the directional branching ratio DBR = (ιs−ιc)∫K = (ιs−ιc)/(ιs+ιc)·BR (eq. 19, p. 6); estimates BR ≈ 80% vs DBR ≈ 40% for BNP Paribas (p. 20)."
  - target: intensity-forecast
    type: mentions
    confidence: inferred
    because: "The strategy (23) loads on δ_t through ζ((T−t)H), the time-average of the deterministic imbalance propagator e^{−sH^T} (pp. 7–8, eq. 43 p. 38); the paper does not call it a forecast."
---

# Extension and calibration of a Hawkes-based optimal execution model

## Bibliographic Details

Alfonsi, Aurélien, and Pierre Blanc. 2016. "Extension and Calibration of a Hawkes-Based Optimal
Execution Model." *Market Microstructure and Liquidity* 2(2): 1650005.
doi:10.1142/S2382626616500052. arXiv:1506.08740.

**Read: arXiv 1506.08740v1 (29 June 2015, 40 pp.); page and equation numbers follow that version.**
Non-core work; preprint accepted under the project's preprint policy. A published version exists,
hence `based_on: preprint`.

### Notation map (source → project, CLAUDE.md § Notation)

As in [[alfonsi-2016-dynamic-optimal-execution]] (same authors, same symbols), plus:

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $G(t)$ | price propagator, $G(0)=1$ (eq. 4) | — |
| $K(t)$ | Hawkes **decay kernel** (function), $K(0)=1$ (eq. 5) | ⚠ **not** the branching matrix $K$ |
| $\lambda_i,\rho_i$ | weights and speeds of the propagator mixture (eq. 7) | ⚠ $\lambda_i$ **not** an intensity; $\rho_i$ **not** a spectral radius |
| $w_i,\beta_i$ | weights and decays of the Hawkes-kernel mixture (eq. 20) | sum-of-exponentials decays $\beta$ |
| $\kappa^\pm(i)$, $\delta^i,\Sigma^i$ | intensity components per exponential; imbalance / total per component | $\lambda_t$ lifted to $2p$ components |
| $\alpha_i=w_i(\iota_s-\iota_c)$, $H_{ij}=\mathbb 1_{i=j}\beta_i-\alpha_j$ | net directional excitation per component; coupling matrix (eq. 21) | $H^\top$ plays the role of $D(I-K)$ for the imbalance [I] |
| $\zeta(M),\omega(M)$ | $M^{-1}(I-e^{-M})$, $M^{-2}(e^{-M}-I+M)$ (eq. 22) | — |
| BR, DBR | branching ratio $(\iota_s+\iota_c)\int K$; directional branching ratio $(\iota_s-\iota_c)\int K$ (eq. 19) | BR $\approx\rho(K)$ for the 2×2 symmetric case |
| $\mathcal C(\tau)$ | autocovariance of event-count increments (eq. 12) | — |
| $\sigma W$ | additive Brownian noise in the price (eq. 4) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (recap of the MIH model, eqs. 1–3; aim: calibration without trading) | 1–2 |
| ✓ F1 | 2 Model settings: propagator $G$ + noise, general kernel $K$ (eqs. 4–5) | 3 |
| ✓ F1 | 2.1 Markovian specification: completely monotone kernels, finite mixtures (6)–(11); autocovariance (12)–(14), Prop. 2.1 | 3–5 |
| ✓ | 2.2 Trading strategies and generalised no-arbitrage: Thm 2.1, (16)–(19), DBR, power-law case | 5–7 |
| ✓ F1 | 2.3 Optimal execution strategy: multi-exponential Hawkes, mono-exponential propagator, Thm 2.2 (20)–(23) | 7–8 |
| ✓ | 3.1 Dataset (Natixis tick data, BNP Paribas and Total, 11:00–13:00, 2012–2013); Table 1 | 8–9 |
| ✓ | 3.2 Overview of calibration (separate Hawkes and propagator estimation) | 9 |
| ✓ | 3.3 Propagator estimation: regression window, adjustment lag, mono/multi-exponential resilience (24)–(32) | 10–13 |
| ✓ | 3.4 Hawkes estimation: affine marks (33)–(34), GMM for total intensity, MLE for self/cross split, multi-exponential weights | 14–16 |
| ✓ | 4.1–4.2 Results on simulated data (Tables 2–3) | 16–17 |
| ✓ | 4.3 BNP Paribas (Tables 4–6, Figs. 1–3) | 18–20 |
| ✓ | 4.4 Total (Tables 7–9) | 20–22 |
| ✓ | 5 Backtest of round trips: scaling (36), methodology, simulated data, BNP, Total (Tables 10–13, Figs. 4–7) | 23–29 |
| ✓ | 6 Conclusion | 30 |
| — | References | 31–32 |
| — | Appendix A: Newton–Raphson for the propagator | 33–34 |
| — | Appendix B: MLE for the Hawkes intensity | 35–36 |
| ✓ F1 | Appendix C: C.1 proof of Thm 2.1; C.2 proof of Thm 2.2 — ansatz (44), (45)–(50) | 37–40 |

## Kernthesen

### 1. The MIH model is generalised to a propagator price with Brownian noise and a general Hawkes decay kernel (p. 3)

$P_t=\frac1q\sum_{\tau<t}\Delta N_\tau G(t-\tau)+\sigma W_t$ (eq. 4), with intensities
$\kappa^\pm_t=\kappa_\infty+\sum_{\tau<t}[\dots]K(t-\tau)$ (eq. 5). The noise is added because the pure
trade-driven price (1) «is probably too restrictive» and does not change the main results (p. 3).
Exponential $G$ and $K$ recover the companion paper ([[alfonsi-2016-dynamic-optimal-execution]]).

### 2. ⭐⭐ Completely monotone kernels with finitely many exponentials restore a Markov state (pp. 3–4)

General kernels drop the Markov property, «which is important in the context of optimal execution»
(p. 3). With $G(u)=\nu+\sum\lambda_ie^{-\rho_iu}$ and $K(u)=\sum w_ie^{-\rho_iu}$ (eq. 7), one tracks
$D^i$ and $\kappa^\pm(i)$ per speed (eqs. 8–10), and «the process $(P,S,D^i,\kappa^\pm(i))$ satisfies the Markov
property» (p. 4). In the Markov case stationarity is no longer needed for well-posedness (Remark 2.1,
p. 4).

### 3. The event-count autocovariance of a multi-exponential Hawkes process is a sum of $p$ exponentials with explicit rates (pp. 4–5)

Proposition 2.1: $\mathcal C(\tau)=\sum_ja_je^{-b_j|\tau|}$, where $b_j$ are the roots of an explicit polynomial,
interlaced with the $\rho_i$ ($0<b_1<\rho_1<b_2<\dots<b_p<\rho_p$), and $a$ follows from a Cauchy matrix
(pp. 4–5). For $p=1$ it reduces to Hawkes's formula with rate $\rho-\iota$ (p. 5). This is the basis
of the GMM calibration.

### 4. ⭐ No price manipulation iff the unaffected price is a martingale; for multi-exponential kernels this ties each Hawkes weight to a propagator weight (pp. 6–7)

Theorem 2.1: no PMS iff $P$ is a martingale when $X\equiv0$. Under (9)–(11) this holds iff
$(\iota_s-\iota_c)w_i=\lambda_i\rho_i$ for all $i$, a start condition holds, and $\varphi_s-\varphi_c$ is linear on the
mark support (eq. 16, p. 6). For general completely monotone kernels: $(\iota_s-\iota_c)\tilde w(d\rho)=(1-\nu)\rho\tilde\lambda(d\rho)$
(eq. 17). Hence «the decay speed of K should be higher than that of G, whatever their functional
form» (p. 6).

### 5. ⭐ Necessary martingale condition: the transient share of impact equals the directional branching ratio (pp. 6–7)

Integrating (17) gives $1-\nu=(\iota_s-\iota_c)\int_0^\infty K=:\mathrm{DBR}$ (eq. 18), with
$\mathrm{DBR}=\frac{\iota_s-\iota_c}{\iota_s+\iota_c}\mathrm{BR}$ (eq. 19, p. 6). DBR is «the average number of
"children trades of the same sign" for each trade» (p. 6). It is a simple empirical test: a price is
persistent if DBR $>1-\nu$ and mean-reverting if DBR $<1-\nu$ (p. 6). For power-law kernels the
condition forces equal exponents and scales, matching Bouchaud et al.'s diffusive-price condition by
a different route (pp. 6–7).

### 6. ⭐⭐ The closed form survives a multi-exponential Hawkes kernel but not a multi-exponential propagator (pp. 7–8)

«In fact, the model is still Markovian and Affine with respect to the state variable
$(X_t,P_t,S_t,D^i_t,\kappa^\pm_t(i))$, and the cost is still quadratic» (p. 7). But with several propagator
exponentials the problem without order flow is «already quite involved and is characterized through
a matrix Riccati equation» (Alfonsi–Schied), and the full ODE system «would presumably have to [be
solved] with numerical methods» (p. 7). For a mono-exponential propagator and $K=\sum w_ie^{-\beta_iu}$
(eq. 20), Theorem 2.2 gives the strategy explicitly (eq. 23, p. 8):
$(1-\nu)X^*_t=-[1+\rho(T-t)]D_t+\frac{m_1}{2\rho}[2+\rho(T-t)]\,\delta_t^\top\big[I_p+\frac{2\rho(T-t)}{2+\rho(T-t)}\{\zeta((T-t)H)+\nu\rho(T-t)\omega((T-t)H)\}\big]\mathbf 1$,
with $H_{ij}=\mathbb 1_{i=j}\beta_i-\alpha_j$ (eq. 21).

### 7. ⭐⭐ In the proof the intensity loadings solve a linear vector ODE closed by matrix exponentials; the remaining coefficients solve linear ODEs (pp. 38–40)

Ansatz (44): quadratic in $(y,\xi)$ with cross terms $(d-(1-\nu)x)\sum b_i\delta^i$, a full quadratic form
$\sum c_{ij}\delta^i\delta^j$, and terms linear in $\Sigma^i$ (p. 38). The impact coefficient is unchanged from
the companion paper: $j=1/(2+\rho u)$ (eq. 47, p. 39). The loading vector solves
$\dot b=-(H+\frac{\rho}{2+\rho u}I_p)b+\frac{m_1}{1-\nu}\frac{1+\nu\rho u}{2+\rho u}\mathbf 1$ (eq. 48), solved by
$b(u)=\frac{m_1u}{1-\nu}\frac1{2+\rho u}[\zeta(uH)+\nu\rho u\,\omega(uH)]\mathbf 1$ (eq. 49) and $k$ by (50) (pp. 39–40).
«Thus, the functions j and k involved in (46) are explicit, which guarantees that the optimal strategy
is obtained as a closed formula» (p. 40). The $c_{ij},e_i,g$ «solve a system of linear ODEs» and do not
affect the strategy (p. 40).

### 8. Data: midprice jumps caused by trades are the events; other midprice moves carry resilience (pp. 8–9)

Natixis tick data for BNP Paribas and Total, 11:00–13:00, January–September 2012 and 2013 (p. 8).
Events are midprice changes triggered by trades, with mark = price jump and executed volume; midprice
changes from cancellations and passive orders implement resilience; 1–4 s between events (pp. 8–9).

### 9. Calibration splits into independent propagator and Hawkes estimations (pp. 9–16)

The trades are a marked Hawkes process and, conditionally on them, the price is Gaussian (p. 9).
The propagator is fitted by least squares on a 30-minute regression window (eqs. 24–27, pp. 10–11),
first unconstrained, then as mono- or multi-exponential resilience on fixed speeds (10 min, 1 min,
30 s, 10 s), dropping non-positive weights (pp. 12–13). Hawkes: GMM on binned total counts gives
$\beta,\kappa_\infty,\iota$ (pp. 14–15); MLE splits $\iota$ into self/cross and constant/linear marks
(eq. 33); then multi-exponential weights by MLE (pp. 15–16). On simulations BR and DBR are recovered
«within a precision of ±0.03» (p. 17).

### 10. ⭐ The propagator rises for a few seconds after a trade, then decays on a ~1-minute scale to a non-zero permanent level (pp. 11, 18–19)

$G$ increases near zero, peaking at $\gamma\approx2$–$3$, which the authors read as the bid-ask re-forming
around the impacted price plus cancellations pushing the same way (pp. 11, 18). Adjustment lag
$L_{adj}=4$ s (2012), 2 s (2013) for BNP (p. 18). Permanent share ≈40% (2012) and ≈20% (2013);
a mono-exponential resilience fits well (pp. 18–19). This contradicts the decreasing-convex
propagator needed in idealised no-spread models (p. 11).

### 11. ⭐ Hawkes fits: volume marks beat unit and price marks; two time scales (10 min and 10 s); high BR but low DBR because of cross-excitation (pp. 19–22)

Volume marks give the highest likelihood (Table 5); linear parts of $\varphi_s$, $\varphi_c$ are non-negligible
(p. 19). Multi-exponential fits select $\beta=6$ and $\beta=360$ h$^{-1}$, carrying ≈40% and ≈60% of the norm
(p. 19). «Here, the standard branching ratio BR ≈ 80% is high, but the directional branching ratio DBR
≈ 40% is quite low, which is due to a non-negligible part of cross-excitation in the order flow»
(BNP, p. 20). Total: BR ≈ 60%, DBR ≈ 30% (p. 21). Even two exponentials do not fit the
autocorrelation well: «the functional form of the auto-correlation is more subtle than a
multi-exponential one» (p. 20).

### 12. ⭐ The martingale condition is violated in the data: prices mean-revert ($1-\nu>$ DBR) (pp. 20–21)

$1-\nu\approx60\%$ (2012), $80\%$ (2013) for BNP vs DBR ≈40% (p. 20); Total $1-\nu=84\%$/$92\%$ vs DBR ≈30%
(p. 21). «The price process is mean-reverting on average, rather than diffusive. This should lead to
the existence of PMS in practice» (p. 20).

### 13. ⭐ Round-trip backtests profit at the midprice but the profit vanishes with a half-tick cost; Hawkes and Poisson strategies perform alike (pp. 23–29)

The strategy (36) is scaled by $s$ and applied at midprice-move times outside the adjustment lag
(pp. 23–24). On real data Sharpe ratios are positive at the mid but drop to near zero or negative with
a half-tick penalty (BNP multi-exponential: 1.38 → −0.68 in-sample 2012; 2.25 → 0.42 out-of-sample
2013, Table 12, p. 26). Simulated data: 6.76 → 3.23 (Table 10, p. 25). «The main component of the
strategy is the mean-reverting one (which is common to the Poisson and Hawkes strategies), while the
trend-following one has a minor contribution» (p. 25).

### 14. No-arbitrage at this frequency comes from impact *and* the bid-ask spread together (pp. 24, 30)

Other participants «already exploit most of the arbitrage opportunities described by our model»
(p. 24). The conclusion: the absence of PMS «stems from both market impact and bid-ask costs» (p. 30).
Proposed extensions: whole-day calibration, transaction costs in the model, and using the
instantaneous cost of not trading (eq. 46) to decide when to trade (p. 30).

## Figures and tables

- Table 1 (p. 9): data statistics (midprice, events per hour, share due to trades, $m_1$, $m_2/m_1^2$).
- Tables 2–3 (pp. 16–17): calibration on simulated data (true vs estimated).
- Tables 6, 9 (pp. 18, 22): calibrated propagator and Hawkes parameters with BR/DBR for BNP and Total.
- Fig. 1–2 (pp. 19–20): propagator curves; Fig. 3 (p. 21): event autocorrelation vs mono/multi-exponential fit.
- Tables 10–13, Figs. 4–7 (pp. 25–29): backtest Sharpe ratios, cumulative gains, gain histograms.

## What this source does not address

- **Market making / quote control.** Execution and round trips with market orders only; no fill
  probability, no Hamiltonian. Quote-controlled Hawkes market making:
  [[barzykin-2026-hawkes-driven-otc]], [[martin-2026-market-making-hawkes]].
- **Several assets.** Single asset; the multi-component intensity is a kernel mixture, not cross-asset
  excitation. Cross-asset Hawkes: [[acero-2026-hawkes-structured-networks]],
  [[rosenbaum-2022-multi-asset-market]].
- **Risk aversion.** Risk-neutral expected cost.
- **Closed form with a multi-exponential propagator.** Declared numerical (p. 7).
- **Fill-driven excitation.** Excluded (p. 5).
- **Power-law kernels in control.** Only in the no-PMS discussion (pp. 6–7); a Markov treatment needs
  a lift, see [[markov-lift]], [[jusselin-2021-persistent-order-flow]].

## Model card

*Execution model, not market making; card filled for comparability.*

| Field | Value |
|---|---|
| Assets | 1 |
| Kernel | sum-of-exponentials Hawkes $K=\sum_iw_ie^{-\beta_iu}$ (eq. 20); calibrated with 2 components (10 min, 10 s); volume-marked affine excitation (eq. 33) |
| Excitation | self + cross-side (buy↔sell); no cross-asset |
| Who excites the flow | other traders' orders only; the strategic trader's trades «leave unchanged the flow of orders N» (p. 5) — flow-driven |
| Objective | minimise expected execution cost under propagator impact; risk-neutral |
| Solution method | closed form for mono-exponential propagator + multi-exponential Hawkes (Thm 2.2; matrix functions $\zeta,\omega$ of $H$); multi-exponential propagator → matrix Riccati, numerical (p. 7) |
| Benchmark | Obizhaeva–Wang static strategy (scaling $s=0$) and a "Poisson strategy" without the trend part (p. 24) |
| Reported regret or gap numbers | n/a — no regret; backtest Sharpe ratios of round trips (Tables 10–13), e.g. BNP 2013 out-of-sample 2.25 at mid, 0.42 with half-tick cost (p. 26) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 2, 6, 7, 11.**

### What this focus needs beyond the Kernthesen

1. **Where the closure breaks: the Riccati dimension follows the price/position states, not the
   intensity states [I from p. 7 and eqs. 44–50].** Adding intensity components ($p$ exponentials)
   only enlarges a *linear* ODE system: $b$ through $H$, and $c_{ij},e_i$. Adding propagator
   components (several $D^i$) turns the curvature equation into a matrix Riccati with no closed
   form (p. 7). For Stage 2a's analogue: in a $d$-asset model, inventory dimension sets the matrix
   Riccati, while cross-asset intensity dimension adds linear structure, provided the control does
   not multiply the intensity.
2. **The loading is an integrated deterministic forecast [D, project derivation from eqs. 43, 23].**
   From (43), $\mathbb E[dI_t]=(\iota_s-\iota_c)\sum_k\delta^k_tdt$, so the conditional mean imbalance obeys
   $\dot{\bar\delta}=-H^\top\bar\delta$. Then $\delta_t^\top\zeta(uH)\mathbf 1=\frac1u\int_0^u\mathbf 1^\top e^{-sH^\top}\delta_t\,ds$ is the
   time-average over the remaining horizon $u=T-t$ of the deterministic forecast of total signed
   intensity. $H^\top=\mathrm{diag}(\beta)-(\iota_s-\iota_c)w\mathbf 1^\top$ is the decay-minus-excitation operator,
   the analogue of $D(I-K)$ in the project's forecast equation $\dot m=D\mu-D(I-K)m$.
3. **Multi-asset carry-over [I].** Because the mixture components are coupled through a rank-one
   excitation term, (48)–(50) are already a worked example of a coupled multi-component intensity
   state. A cross-asset excitation matrix would replace $H$ by a full decay-minus-branching
   operator. The closed form would carry over as long as the curvature coefficient stays scalar (or
   commutes), as it does here because $j$ does not depend on $H$.

### Direct quotes (for the draft)

> "In fact, the model is still Markovian and Affine with respect to the state variable (Xt, Pt, St, Dti, κ±t(i)), and the cost is still quadratic." (p. 7)

> "However, we know from Alfonsi and Schied [3] that the optimal strategy without the flow of trades (i.e. N ≡ 0) is already quite involved and is characterized through a matrix Riccati equation. In our context, the system of ordinary differential equations that characterize the cost function would be much more intricated, and one would presumably have to solve it with numerical methods, which are less efficient than closed formulas for high-frequency trading." (p. 7)

> "Thus, the functions j and k involved in (46) are explicit, which guarantees that the optimal strategy is obtained as a closed formula." (p. 40)

> "Here, the standard branching ratio BR ≈ 80% is high, but the directional branching ratio DBR ≈ 40% is quite low, which is due to a non-negligible part of cross-excitation in the order flow." (p. 20)

### Examples & illustrations (for later drafting)

- Eqs. (48)–(49) (p. 39): a linear vector ODE with coupling matrix $H$ solved in closed form by matrix
  exponentials. This is a template for "the intensity-loading system is linear and solvable" in a
  multi-component Hawkes state.
- BNP Paribas calibration (p. 20): BR ≈ 0.8 vs DBR ≈ 0.4. A concrete case where cross-side excitation
  halves the effective directional persistence. It shows that the branching structure, not only its
  spectral radius, matters for strategy.

### Boundary of this focus

Single-asset execution with linear impact. There are no quotes and no inventory risk. Items 1–3 are
the project's inferences from the paper's equations. The backtests concern round-trip arbitrage, not
market-making regret.

## Mentioned entities

- Concepts: [[hawkes-process]], [[markov-lift]], [[who-excites-the-flow]], [[branching-matrix]], [[matrix-riccati-equation]], [[intensity-forecast]].
- Sources in this wiki: [[alfonsi-2016-dynamic-optimal-execution]] (companion, earlier; cited as [1]).
- Other works (not in this wiki): Alfonsi & Schied 2013 (completely monotone kernels, matrix Riccati); Alfonsi, Schied & Slynko 2012; Gatheral, Schied & Slynko 2012; Obizhaeva & Wang 2013; Huberman & Stanzl 2004; Bouchaud et al. 2004; Bacry & Muzy 2014; Da Fonseca & Zaatour 2013 (GMM for Hawkes); Hardiman & Bouchaud; Brémaud & Massoulié 1996/2001; Hawkes 1971.

## Connections

- Builds on [[alfonsi-2016-dynamic-optimal-execution]]: same model, general kernels, calibration, backtest.
- Builds on [[markov-lift]]: finite exponential mixtures as the Markov route for completely monotone kernels.
- Supports [[who-excites-the-flow]]: flow-driven by assumption (p. 5).
- Cited by [[jain-2025-impulse-control-hawkes]] as the dynamic-arbitrage precedent for exponential-kernel Hawkes impact models.
