---
title: "Bathini et al. 2026 — Dynamic Market Making under Stochastic Liquidity and Inventory Risk"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: bathini-2026-dynamic-market-making
depth: standard
tags: [market-making, hawkes-process, empirical, backtest, crypto, adverse-selection, regime-switching, bellman-recursion, single-asset, benchmark]
relations:
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "Classical AS (M0) is a primary comparator: «These two papers supply our main strategy comparators, and they also shape the structure of our own finite HJB model» (p. 3); M4 «underperforms classical Avellaneda–Stoikov (AS) by 0.496 USDT per hour» (p. 1)."
  - target: glft-2013-model
    type: builds-on
    confidence: extracted
    because: "Stationary GLFT (B3) is the second primary comparator; «Our implemented B3 actually uses the finite-horizon numerical solution rather than this asymptotic expansion» (p. 10); M4 «improves stationary Guéant–Lehalle–Fernandez-Tapia (GLFT) by 0.105 USDT per hour» (p. 1)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Buy and sell aggressive batches «are fitted separately with exponential Hawkes intensities» eq. (12) (p. 10); branching ratios 0.556 and 0.586 (p. 10)."
  - target: intensity-forecast
    type: supports
    confidence: extracted
    because: "«We treat Hawkes intensity as a causal clustering forecast here, not as a complete data-generating mechanism» (p. 11); intensities enter as frozen bucketed parameters re-solved each minute (p. 12)."
  - target: jusselin-2021-persistent-order-flow
    type: builds-on
    confidence: extracted
    because: "«Our own finite-state, finite-difference HJB is a simplified variant of that construction. We use bucketed exponential Hawkes intensities as a surface parameter, instead of solving the fully coupled Hawkes-augmented value function» (p. 4)."
---

# Dynamic Market Making under Stochastic Liquidity and Inventory Risk

## Bibliographic Details

Bathini, Venkatanath; Kathane, Raghav; Pandey, Pranita; Yadav, Priyanshu; Mehta, Mehul. 2026.
*Dynamic Market Making Under Stochastic Liquidity and Inventory Risk: An Event-Driven Evaluation
with Depth-Conditioned Adverse Selection.* SSRN working paper, doi:10.2139/ssrn.7625720. 19 pp.

**Read:** the SSRN working paper in `library/pdf/` (19 pp.); no published version is known. Page
numbers follow the paper's own "Page n of 19" footer. Non-core work; the working paper is accepted
under the project's preprint policy. Equations are numbered (1)–(21); several are garbled in the text
layer and were read off the rendered pages.

### Notation map (source → project)

| Source | Meaning | Project |
|---|---|---|
| $q$ (lots of 0.001 BTC), bound 20 | inventory | $q_t$, $Q$ |
| $\gamma$, $\sigma$ | risk aversion, "fractional" volatility | $\gamma$, $\sigma$ |
| $\lambda_s(t)$, $n_s=\alpha_s/\beta_s$ | side-$s$ Hawkes intensity, branching ratio | $\lambda_t$, $\rho(K)$ (diagonal only) |
| $\kappa$ (≈ 0.0022/tick) | depth-decay of the reach curve $e^{-\kappa d}$ | $k$ in $\Lambda e^{-k\delta}$ |
| $l\in\{1,2,3\}$, $P$ | liquidity regime, transition matrix (eq. 16) | none |
| $\eta_l$ | scalar adverse-selection cost per expected fill (regime $l$) | none |
| $\bar M(d,h)$ | cumulative reach-conditioned markout at depth $d$, horizon $h$ (eq. 3) | none |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (two questions; bounded contributions) | 2–3 |
| ✓ F1 | 2 Related literature (AS/GLFT, Bergault–Guéant, Barzykin–Bergault–Guéant; adverse selection; Hawkes control incl. Jusselin; queue-reactive; multiple testing) | 3–5 |
| ✓ | 3 Data, event units, research sequence (Binance BTCUSDT/ETHUSDT perpetuals; batches; protocol chronology) | 5–7 |
| ✓ | 4 Depth-conditioned adverse selection (eqs. 1–8, Tables 2–3, Figs. 1–2) | 7–10 |
| ✓ F1 | 5.1 AS and GLFT benchmarks (eqs. 9–11) | 10 |
| ✓ F1 | 5.2 Hawkes order flow (eqs. 12–15) | 10–11 |
| ✓ F1 | 5.3 Liquidity regimes and HJB control (eqs. 16–19) | 11–12 |
| ✓ F1 | 5.4 Execution and inference (eqs. 20–21) | 12–13 |
| ✓ F1 | 6 Strategy results (Tables 4–5, Fig. 3; sensitivities, policy support) | 13–15 |
| ✓ F1 | 7 Integrated interpretation (Hawkes channel, measurement–control mismatch, 7-point benchmark standard) | 15–16 |
| ✓ F1 | 8 Limitations and future work | 16–17 |
| ✓ | 9 Conclusion; Data and reproducibility; References | 17–19 |

## Kernthesen

### 1. The question is whether richer state conditioning beats strong inventory benchmarks when every policy sees the same realised events (pp. 1–3)

The paper asks «whether adding self-exciting order flow and stochastic liquidity to a finite-horizon
market-making controller improves established inventory-aware benchmarks» (p. 1). The answer is a
bounded negative: «richer state conditioning alone does not provide robust benchmark improvement when
execution opportunity and fill-conditional toxicity are not estimated at the same depth and event
resolution» (p. 1).

### 2. A quote at depth $d$ is exposed to every aggressive event that reaches at least $d$; exclusive sweep bins understate toxicity (pp. 7–8)

The estimand (eq. 3) weights all events with reach $\ge d$. With exclusive bins, «using only the
shallowest exclusive bin removes the most toxic events from the touch sample»; a superseded
exclusive-bin analysis gave a next-to-touch ratio near 11, the corrected cumulative 60-s ratio is 3.608
(p. 8).

### 3. Deeper reach comes with much larger adverse markouts, a replicated direction but not a stable coefficient (pp. 8–9)

The 10-s markout difference (1.5 minus 0.5 ticks) is 31.385 ticks in validation and 37.764 in the
final holdout (Table 2, p. 8), positive on 47/47 original days; the frozen extension gives 42.963
(BTCUSDT) and 22.467 (ETHUSDT) (Table 3, p. 8). «this is best described as a replicated direction,
not a fixed structural coefficient» (p. 8).

### 4. Reach, queue capture and markout must refer to the same depth, event unit and quote lifecycle (pp. 9–10)

The per-opportunity edge (eq. 8) combines reach probability, capture probability and the conditional
markout at depth $d$; «reach, queue capture, and adverse markout all need to refer to the same depth,
the same event unit, and the same quote lifecycle» (p. 10). The no-quote action (value 0) must stay
available.

### 5. ⭐ The Hawkes model is two independent univariate exponential fits, adequate as a forecast and rejected as a generator (pp. 10–11)

Buy and sell batches are fitted separately (eq. 12); branching ratios 0.556 (buy) and 0.586 (sell)
(p. 10). Held-out time-rescaling KS statistics ≈ 0.11 against critical values ≈ 0.002, «so every
side-day rejects» (p. 11). Independent Hawkes improves held-out log-likelihood over Poisson by 0.325
per event; a bivariate (cross-exciting) fit adds 0.0092 per event, positive in all 19 folds, but
«This later bivariate diagnostic was never deployed in the frozen controller itself» (p. 11).

### 6. Liquidity is a three-state Markov regime estimated from training quantiles (p. 11)

Transition matrix eq. (16) (diagonal 0.509, 0.371, 0.514); arrival multipliers 0.635, 0.863, 1.502;
fill-decay rates 0.00282, 0.00218, 0.00218 per tick; scalar adverse-selection inputs 0.493, 0.538,
0.449 ticks per expected fill, «scalar in quote depth» (p. 11).

### 7. ⭐⭐ The "HJB" is a discrete-time Bellman recursion on (time, inventory, regime) with the Hawkes intensity frozen as a parameter (pp. 11–12)

$V_n(q,l)=\max_{bid,ask}\{\mathbb E[\text{spread edge}-\eta_l\cdot\text{fills}-\gamma(q\cdot\text{size}\cdot S\cdot\sigma)^2]+\mathbb E[V_{n+1}(q+N_{bid}-N_{ask},L_{n+1})]\}$
(eq. 17, p. 11). Fill counts per step are conditionally Poisson, so the net fill is Skellam (eq. 18);
inventory is truncated at $|q|\le20$; the terminal condition charges half-spread plus size-dependent
impact (eq. 19, p. 12). «Volatility and buy/sell Hawkes intensities enter as training-bucketed surface
parameters, held fixed through each 30-minute solve, and refreshed each minute in a receding horizon.
Thus, the HJB does condition on a clustering forecast, but it never evolves intensity inside the
Bellman state itself, and it does not value the option to simply wait for that intensity to decay»
(p. 12).

### 8. The study is a clean eight-policy ablation under common realised events (pp. 10, 12)

B1 naive symmetric, B2 inventory skew, B3 stationary GLFT (finite-horizon numerical solution, not the
asymptotic formula eq. 11), M0 classical AS (eqs. 9–10), M1 dynamic-volatility AS, M2 Hawkes-only HJB,
M3 liquidity-only HJB, M4 full HJB (pp. 10, 12). Fills are tied to realised event reach with a common
deterministic binomial capture draw across policies (p. 6).

### 9. The replay is a stale-quote stress test, not a low-latency simulation (p. 12)

0.001 BTC order, 30-min planning horizon, 20-lot bound, zero maker fee, 1% queue capture, quotes fixed
for one minute and replenished immediately after a capture; inference over 19 market days with 20
common seeds averaged within day (p. 12).

### 10. ⭐⭐ Every policy loses money; full HJB beats stationary GLFT but loses to classical AS (pp. 13–14, Tables 4–5)

MM PnL/hour: B3 −4.990, M0 −4.389, M4 −4.885 (Table 4, p. 13). Paired M4 − M0 = −0.496 USDT/h
(familywise [−0.742, −0.251], 0/19 positive days); M4 − B3 = +0.105 ([0.017, 0.193], 15/19). Per USD
1m turnover: M4 − M0 = −7.583, M4 − B3 = +11.596 (Table 5, p. 13). «M4 beats stationary GLFT on both
endpoints, but it is worse than classical AS on both endpoints too. Therefore, it fails our co-primary
improvement gate» (p. 14).

### 11. ⭐ The HJB policy is boundary-seeking, so no unrestricted optimum is located (pp. 14–15)

«M4 chooses its maximum HJB action on at least one side in 96.7% of quote intervals», median retained
bid and ask depths 384.5 ticks; «this experiment compares two bounded policy families against each
other, it does not locate an unrestricted HJB optimum» (p. 14). Cause: the empirical reach tail is
almost flat (κ ≈ 0.0022/tick) because a one-minute fixed quote is reached by large moves (pp. 14–15).

### 12. ⭐ The side-specific Hawkes channel is not inert: imbalance moves the action far more than common scaling (p. 15)

Post-outcome diagnostic: scaling both intensities together changed an HJB action in 20–25% of states;
moving directional imbalance at fixed total changed an action in roughly 89% of states (p. 15). «the
side-specific Hawkes channel is not inert» (p. 15); no confirmatory standing.

### 13. The controller's adverse-selection cost and fill curve are measured on incompatible supports (pp. 15–16)

The controller's cost is scalar in depth, the validated markout varies sharply between 0.5 and 1.5
ticks, and the HJB «goes on to select quotes around 340–384 ticks, far outside the roughly 34-tick
region our depth surface actually covers» (p. 15).

### 14. A seven-point standard for claiming benchmark improvement (p. 16)

Causal forecasts; common realised opportunities; depth-aligned execution and adverse selection;
day-level inference; strong AS/GLFT comparators plus ablations; full reporting incl. boundary rates;
«Withhold optimality claims whenever the selected policy sits on the edge of its tested support»
(p. 16).

### 15. Limitations point to the fully coupled Hawkes–HJB as future work (pp. 16–17)

Level-I data only; one contract over 29 days; frozen, bucketed intensities; the fully coupled
construction of Jusselin (2020) is named as the more faithful alternative, «but any added complexity
needs to earn its place out of sample» (p. 17).

## Figures and tables

- Tables 2–3 (p. 8): markout differences by stage. Figs. 1–2 (p. 9): day-level markout series.
- Table 4 (p. 13): eight-policy PnL decomposition. Table 5 (p. 13): paired M4 contrasts.
- Fig. 3 (p. 14): ranking, decomposition, contrasts, action-support diagnostics.

No figures extracted (write scope limited to this page).

## What this source does not address

- **A continuous-time HJB or a lifted Hawkes state.** The intensity is a frozen parameter of a
  discrete-time Bellman recursion (p. 12); no lift, no Riccati, no closed form.
- **Cross-excitation in the controller.** Buy and sell are independent univariate fits; the bivariate
  model is diagnostic only (p. 11).
- **More than one asset.** One contract in the strategy study; ETHUSDT appears only in the measurement
  extension, reported separately (pp. 4, 8).
- **Optimality gaps or regret.** No exact benchmark; comparisons are realised replay PnL against
  heuristic and closed-form-family policies; RL is cited in the references (Gašperov & Kostanjčar 2022)
  but not used or discussed in the text.
- **CARA utility.** The objective is expected edge minus a running quadratic inventory penalty.

## Model card

| Field | Entry |
|---|---|
| Assets | 1 (BTCUSDT perpetual in the strategy study; ETHUSDT only in the markout measurement) |
| Kernel | exponential, one decay per side (eq. 12); bivariate exponential fit as diagnostic only |
| Excitation | self only in the deployed controller (two independent univariate fits); cross-side estimated but not deployed (p. 11) |
| Who excites the flow | all market-wide aggressive batches (flow-driven); maker fills do not feed back; intensity frozen inside each solve |
| Objective | discrete-time expected spread edge − regime adverse-selection cost $\eta_l$ − running penalty $\gamma(q\cdot\text{size}\cdot S\sigma)^2$, terminal liquidation cost (eqs. 17, 19); not CARA |
| Solution method | finite-state backward induction on (step $n$, $q$, regime $l$), Skellam net fills, 14-level action grid + no-quote; Hawkes intensities and volatility bucketed and frozen for each 30-min solve, re-solved each minute (receding horizon) |
| Benchmark | naive symmetric, inventory skew, stationary GLFT (finite-horizon numerical), classical AS, dynamic-vol AS, Hawkes-only and liquidity-only ablations |
| Reported numbers | all MM PnL negative; M4 − B3 = +0.105 USDT/h [0.017, 0.193]; M4 − M0 = −0.496 USDT/h [−0.742, −0.251]; per USD 1m: +11.596 vs B3, −7.583 vs M0; boundary action in 96.7% of intervals; no regret / optimality gap (no exact benchmark) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 5, 7, 8, 10, 11, 12, 15.**

### What this focus needs beyond the Kernthesen

1. **No closure is attempted.** The value function is computed by brute-force backward induction on
   a small grid ($n$, $|q|\le20$, 3 regimes) with a finite action set of 14 depths per side (p. 12).
   The Hawkes state is removed from the state by freezing it at its current bucketed value for the
   whole 30-minute solve; this is the "freeze the forecast at a constant" device, a cruder relative of
   the forecast-curve freezing in [[barzykin-2026-hawkes-driven-otc]] (there the frozen object is the
   whole decaying forecast curve $m_t(u)$; here it is a constant level, so decay is ignored, p. 12).
2. **Who excites the flow.** Intensities are filtered from all market-wide aggressive batches (p. 10);
   the maker's fills do not feed back. This is the flow-driven convention of [[who-excites-the-flow]],
   but it is irrelevant inside the controller because the intensity never moves within a solve.
3. **Cross-excitation.** Present only as a diagnostic (bivariate fit, +0.0092 log-lik per event on top
   of independent fits, p. 11). The empirical signal that matters for quoting is *directional
   imbalance* between the two side intensities (Kernthese 12), i.e. the asymmetric excitation regime in
   which [[barzykin-2026-hawkes-driven-otc]] finds the largest gains from conditioning on memory.
4. **Comparison structure.** The comparison is closed-form family (AS, GLFT) vs a numerically solved
   frozen-intensity Bellman policy, on real data, with PnL rather than regret. It is **not** a
   closed-form vs exact vs RL comparison on one Hawkes problem: there is no exact lifted solution and
   no RL policy.
5. **Multi-asset.** None. Bergault & Guéant (2021) and Barzykin, Bergault & Guéant (2023) are cited
   only to note that higher-dimensional dealer systems «get much harder to solve and calibrate» (p. 3).

### Direct quotes

> "Thus, the HJB does condition on a clustering forecast, but it never evolves intensity inside the Bellman state itself, and it does not value the option to simply wait for that intensity to decay." (p. 12)

> "In effect, this experiment compares two bounded policy families against each other, it does not locate an unrestricted HJB optimum." (p. 14)

> "proving that a well-posed Hawkes-augmented control problem exists does not by itself guarantee that a coarsened, depth-discretized implementation of that control will recover a usable advantage over a stationary benchmark." (p. 15)

### Examples & illustrations

- Table 5 (p. 13): M4 − B3 = +0.105 USDT/h, M4 − M0 = −0.496 USDT/h: the Hawkes+regime controller sits
  between stationary GLFT and adaptive AS.
- Kernthese 12 (p. 15): 89% of states change action under imbalance shifts vs 20–25% under common
  scaling: an empirical argument that the *direction* of excitation, not its level, drives quotes.

### Boundary of this focus

Nothing here bears on a closed form: the paper neither derives nor tests one for Hawkes flow. Its use
for the project is as a cautionary empirical counterpoint (a frozen-intensity Hawkes policy does not
beat AS out of sample when the fill and toxicity inputs are misaligned) and as evidence that
directional rather than common-mode excitation drives the quote.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]], [[glft-2013-model]]
- Concepts: [[hawkes-process]], [[intensity-forecast]], [[who-excites-the-flow]]
- Other works (not checked against the library): Bergault & Guéant 2021 (size matters, OTC, p. 3), Barzykin–Bergault–Guéant 2023 (FX dealer, p. 3), Cartea–Jaimungal–Penalva 2015, Alfonsi & Blanc 2016, Capponi et al. 2021, Bacry et al. 2013/2015, Mucciante & Sancetta 2024, Gašperov & Kostanjčar 2022 (DRL, references only), Kyle & Obizhaeva 2016, Harvey & Liu 2015, Bailey & López de Prado 2014.

## Connections

- Builds on: [[jusselin-2021-persistent-order-flow]] (explicitly a "simplified variant", p. 4); uses [[avellaneda-stoikov-model]] and [[glft-2013-model]] as comparators.
- Compare: [[barzykin-2026-hawkes-driven-otc]] (forecast freezing done properly: full forecast curve, validated against an exact lift); [[tarditi-2026-hawkes-process-models]] (bivariate Hawkes intensity kept *inside* the state and solved on a grid, the step this paper skips).
