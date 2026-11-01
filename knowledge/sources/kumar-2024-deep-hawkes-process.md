---
title: "Kumar 2024 — Deep Hawkes Process for High-Frequency Market Making"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: kumar-2024-deep-hawkes-process
depth: standard
tags: [market-making, hawkes, neural-hawkes, lstm, agent-based-simulation, limit-order-book, single-asset, prediction-based-quoting]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Multivariate (marked) Hawkes intensities eqs. (2.4)–(2.5) (p. 9) are generalised to a neural intensity «λk(t) = fk(w⊤k h(t))» eq. (4.1) (p. 18), extending the neurally self-modulating process of Mei & Eisner (p. 4)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«By integrating a utility framework into the microstructure of LOB, Avellaneda and Stoikov (2008) were able to analytically derive optimal bid and ask quotes» (p. 13); criticised as relying on «unrealistic assumptions» (p. 13)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "«(Cartea et al., 2014) used a multivariate Hawkes process to capture the interaction between market orders and state of LOB. However, the constraints placed on parametric specification ... limit the model's eloquence» (p. 14)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Cited for the stochastic-control framing: market makers «maximise the expected utility of their profit and loss under inventory constraints (Guéant et al., 2013)» (p. 3)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "The DHP is fitted to all LOB events from ITCH data (p. 29–30) and its predictions drive the maker's quotes (eq. 5.3, p. 24); whether the maker's own orders feed back into the learned intensity inside the simulator is not stated. No stance taken by the author."
based_on: preprint
---

# Deep Hawkes Process for High-Frequency Market Making

## Bibliographic Details

Kumar, Pankaj. 2024. "Deep Hawkes Process for High-Frequency Market Making." *Journal of Banking
and Financial Technology* 8(1). DOI 10.1007/s42786-024-00049-8. Preprint: arXiv:2109.15110v1
[cs.CE], 30 Sep 2021, 49 pp. Author affiliation: Copenhagen Business School.

**Read: arXiv 2109.15110v1 (preprint); page/equation numbers follow it.** Under the project's
preprint policy this is accepted (non-core work). The published 2024 version may differ (three
years between versions); claims here are about v1. Printed page numbers equal PDF page numbers.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\lambda_k(t)=f_k(w_k^\top h(t))$ | neural intensity of event type $k$ (eq. 4.1) | $\lambda_t$ (no Hawkes kernel) |
| $\mu_i$, $\phi_{i,j}$ | baseline and matrix kernel of the classical multivariate Hawkes (eq. 2.4) | $\mu$, entries behind $K$ |
| $h(t)$, $c(t)$ | LSTM hidden state and memory cell (eqs. 4.2–4.4) | — (lift-like latent state, learned) |
| $p_t$ | mid price | $S_t$ |
| $\delta$ (eq. 5.3) | maximum jump size in ticks | ⚠ not a quote offset |
| $J^{i,u}_t, J^{i,d}_t$ | counts of up/down $i$-tick jumps, intensities $\lambda_{k,u},\lambda_{k,d}$ (eq. 5.4) | — |
| $I_t$, $\bar I$ | inventory, maximum inventory (eq. 5.5) | $q_t$, $Q$ |
| $\Gamma(\alpha,\beta)$ | q-Gamma order-size distribution (eq. 5.5) | ⚠ $\beta$ not a decay |
| $K$ (source) | number of event marks | ⚠ clashes with project $K$ |
| ℸ | quadratic transaction-cost coefficient (eq. 5.21) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction; 1.1 Contribution; 1.2 Structure | 1–5 |
| ✓ F1 | 2 Background: 2.1 LOB, 2.2 HF market making, 2.3 Hawkes process (eqs. 2.1–2.5), 2.4 Neural Hawkes process (eqs. 2.6–2.8), 2.5 LSTM (eq. 2.9) | 5–13 |
| ✓ F1 | 3 Literature review: 3.1 stochastic optimal control, 3.2 agent-based models, 3.3 AI | 13–16 |
| ✓ F1 | 4 Deep Hawkes Process: 4.1 DLSTM, 4.2 DLSTM-SDAE, 4.3 Model formulation (eqs. 4.1–4.4), 4.4 Feedback-loop exploration (eq. 4.5), 4.5 Estimation (eq. 4.6) | 16–21 |
| ✓ F1 | 5 Multi-agent simulation framework: 5.1 market simulator, 5.2 market ecology (DHMM eqs. 5.1–5.7, PMM eqs. 5.8–5.9, fundamental / chartist / noise traders eqs. 5.10–5.18), 5.3 reward (eqs. 5.19–5.22), 5.4 capital | 21–29 |
| ✓ F1 | 6 Experiments: 6.1 data (Table 1), 6.2 metrics, 6.3 benchmarks, 6.4 training (Table 2) | 29–33 |
| ✓ F1 | 7 Results: 7.1 prediction (Figs. 5–6), 7.2 trading (Fig. 7, Table 3), 7.3 cancellations (eq. 7.1, Table 4, Fig. 8), 7.4 sensitivity (Table 5), 7.5 stylised facts (Fig. 9) | 33–41 |
| ✓ F1 | 8 Conclusions (five future directions) | 41–42 |
| — | References | 43–49 |

## Kernthesen

### 1. ⭐ Parametric Hawkes models are too rigid for LOB flow: they miss the feedback loop between order arrival and book state, and inhibition (pp. 3, 10, 14)

«In these models, the arrival rate of orders is not dependent on the state of the limit order book.
However, the empirical results suggest the existence of feedback loop between order arrival and the
state of the limit order book, together with self- and cross-excitation effects, for which current
models fail to account» (p. 3, citing Gonzalez–Schervish 2017, Morariu-Patrichi–Pakkanen 2018).
Positivity of $\mu,\phi$ rules out inhibition, e.g. «the massive cancellation of orders in LOB might
inhibit price rather than exciting it» (p. 10). Cartea et al. 2014 is criticised on the same ground
(p. 14).

### 2. ⭐⭐ The "Deep Hawkes Process" is a neural point process with no Hawkes kernel: intensities are a softplus readout of a stacked LSTM state (pp. 16, 18–19)

«The basic idea behind our approach is to view the conditional intensity of the Hawkes process as a
nonlinear deterministic function of past history, and to use DLSTM to automatically learn a
high-dimensional representation from the data» (p. 16). Intensity $\lambda_k(t)=f_k(w_k^\top h(t))$
(eq. 4.1), $h(t)=o_n\odot\phi(c(t))$ (eq. 4.2), LSTM updates at events (eq. 4.3) with scaled softplus
$f(x)=s\log(1+e^{x/s})$, and between events a memory cell that decays «from $c_{n+1}$ to $\bar c_{n+1}$»
as $c(t)=\bar c_{n+1}+(c_{n+1}-\bar c_{n+1})(t-t_n)^{-\bar p_{n+1}}$ (eq. 4.4) — a power-law variant of
the exponential decay in Mei & Eisner's continuous-time LSTM. Self- and cross-excitation exist only
implicitly in the learned weights; no kernel or branching matrix is recoverable.

### 3. The architecture stacks denoising autoencoders under a deep LSTM to fight noisy data and poor initialisation (pp. 4, 16–18)

Three-layer SDAE pre-trained greedily, then three LSTM layers (DLSTM-SDAE, Fig. 3, p. 17), to avoid
backpropagation «trapped within multiple local minima» and to filter «ultra-noisy order book data»
(pp. 16–17). Training: pre-training then fine-tuning by Adam, early stopping, isotropic Gaussian
input noise (p. 32); 1024 hidden units per layer (Table 2, p. 33).

### 4. A block-structured group-sparsity penalty is meant to "explore" feedback loops between event types and book state (pp. 19–20)

Eq. (4.5): $\mathcal L=\min_{W_{xB}}\mathcal L+\lambda_1\sum_{B\in S}\|W_{xB}\|_1+\lambda_2\sum_{B\in S}\sum_{b=1}^B\|W^{\,b}_{xB}\|_{2,1}$
over blocks of neurons, «to take into account different combinations of feedback loops» (p. 20).
The resulting feedback structure is never reported.

### 5. Estimation is maximum likelihood of the point process, simulation by thinning (pp. 20–21)

$\mathcal L=\sum_{n:t_n\le T}\log\lambda_{k_n}(t_n)-\int_0^T\lambda(t)\,dt$ (eq. 4.6), Adam plus Monte Carlo
for the compensator (Mei–Eisner), and «The frequently used thinning algorithm adapted from
multivariate Hawkes process is then used to sample random sequence from the model» (pp. 20–21).

### 6. ⭐ The market maker trades one security; the "multi-asset" claim concerns only the simulator (pp. 5, 21, 24)

Contribution 1: «We designed a multi-asset simulation framework that is scalable» (p. 5); the
simulator has one matching engine per instrument (p. 22). But for the strategy: «We also assume that
the high-frequency market maker is trading a single security in a market whose price at time $t$ is
denoted by $p_t$» (p. 24). Event types are restricted to «limit order buy/sell, market order
buy/sell, and partial/full cancellations» (p. 24) — six marks of one book.

### 7. ⭐⭐ The DHMM quote rule is a prediction-based pricing formula, not the solution of a control problem (pp. 23–24)

Next-event prediction: $\hat t_n=\int_{t_{n-1}}^\infty tf_n(t)\,dt$, $\hat k_n=\arg\max_k\int\frac{\lambda_k}{\lambda}f_n\,dt$
(eqs. 5.1–5.2, pp. 23–24). Quote: $p^{a,b}_t=p_t+\sum_{i=1}^\delta i\,J^{i,u}_t-\sum_{i=1}^\delta i\,J^{i,d}_t$
(eq. 5.3), with up/down tick-jump intensities given by the DHP (eq. 5.4). Order sizes are drawn from
a q-Gamma (limit), truncated geometric (cancellation) and geometric–Dirac mixture (market) scaled by
$(I_t\pm\bar I)/\bar I$ (eqs. 5.5–5.7). There is no value function, no optimisation over quotes and
no inventory-risk objective in the quote rule; the abstract's «post the optimal price, order type and
execution time» (p. 1) is not backed by an optimality criterion.

### 8. The reward is instantaneous P&L plus inventory revaluation minus a quadratic transaction cost (pp. 28–29)

$R_{t;j}=\mathrm{PnL}_{t;j}+\mathrm{IC}_{t;j}-\mathrm{TC}_{t;j}$ (eq. 5.22) with $\mathrm{PnL}=q^a(p^a-\bar p)+q^b(\bar p-p^b)$
(5.19), $\mathrm{IC}=I_t(\bar p_t-\bar p_{t-1})$ (5.20), $\mathrm{TC}=ℸ(q^e)^2$, ℸ = 0.06 (5.21, Table 2). It is
used for evaluation; no agent maximises it by RL — «Embedding DHP within the reinforcement learning
framework to learn the optimal policy» is listed as future work (p. 41).

### 9. The artificial market is an agent-based ecology of ~13,000 heterogeneous traders around three market makers (pp. 22–29, 33)

Agents: 3 market makers (DHMM, NHMM, PMM), 3000 fundamental, 6000 chartist, 4000 noise traders
(Table 2, p. 33); FIX-protocol kernel, price–time matching (pp. 21–22); power-law initial capital
with exponent 2.3 (p. 29). The benchmark PMM is Das's (2005) Glosten–Milgrom learning market maker
(eq. 5.8, p. 26).

### 10. Data: Nasdaq TotalView-ITCH sample, 100 most liquid securities over eight days, ~1 billion records (pp. 29–30)

«we have sampled high frequency data for hundred most liquid securities over eight days from
reconstructed orderbook. The extracted sample data consists of approximately a billion transaction
records at nanosecond resolutions» (p. 30). Table 1 (p. 30) gives, «For a single security», ≈9.2 m /
0.92 m / 2.3 m training / validation / test events at nanosecond and ≈0.43 m / 42 k / 108 k at
millisecond resolution. How (or whether) the 100 securities enter a joint model is not stated.

### 11. ⭐ Prediction: neither DHP nor NHP works at nanosecond resolution; at millisecond resolution DHP beats NHP (pp. 34–35, 40)

«neither model is invariably better at predicting events or, in particular, time ... The event
dynamics at nanosecond timestamps need much more sophisticated models» (p. 34, Fig. 5). At
millisecond resolution «the DHP model's performance has drastically increased. In addition, the
time prediction is consistently better than with the NHP» (pp. 34–35, Fig. 6). Sensitivity (Table 5,
p. 40): with 3 DAE layers RMSE 1.5–2.0 and event error rate 34–37.5%.

### 12. ⭐ Trading: DHMM has the highest normalised P&L, but with large dispersion and larger positions than NHMM (pp. 35–37, Table 3)

Test, 300 simulated days (Table 3, p. 37): NPnL [10⁵] mean (std) DHMM 2.1 (±18.26), NHMM 1.1 (±4.09),
PMM −1.6 (±79.55); mean absolute position DHMM 17 (±20), NHMM 4 (±6), PMM 41 (±74). «our proposed agent
using DHP (DHMM) consistently outperforms the PMM and NHMM» (p. 35). PMM earns more early in
training and then falls (Fig. 7, p. 36). No significance test is reported.

### 13. Removing cancellations enlarges queues and spreads and lowers profit (pp. 37–39, Table 4, Fig. 8)

With the Moallemi–Yuan (2017) queue-value model $V_t=FP_t(LSP_t-ASC_t)$ (eq. 7.1, p. 38), the
no-cancellation scenario shows a «drastic increase in the average queue size» (p. 38), wider spreads
and lower DHMM profit; order value falls with queue position (Fig. 8, p. 39). The author concedes:
«It is difficult to infer causal relationships between cancellations and market microstructure
variables based on artificially created scenarios» (p. 39).

### 14. The simulator reproduces heavy-tailed returns (tail exponent 2.8) and fast-decaying return autocorrelation (pp. 40–41, Fig. 9)

Cumulative return tails follow a power law «with α = 2.8» and the return ACF «drastically decays
to zero in few lags» at $\Delta t$ = 1 min (p. 40), which the author takes as validation that
simulated and real data are «generated from the same mechanisms» (p. 32).

## Figures and tables

- Fig. 3 (p. 17): DLSTM-SDAE architecture. Fig. 4 (p. 22): simulator architecture.
- Table 1 (p. 30): event counts. Table 2 (p. 33): simulation and network parameters.
- Figs. 5–6 (pp. 34–35): time/event prediction at ns and ms resolution.
- Fig. 7 (p. 36), Table 3 (p. 37): NPnL and MAP of DHMM, NHMM, PMM.
- Table 4, Fig. 8 (pp. 38–39): cancellation scenarios. Table 5 (p. 40): sensitivity. Fig. 9 (p. 41):
  stylised facts.

No figures extracted to `knowledge/assets/` in this pass.

## What this source does not address

- **Any optimal-control formulation or closed form.** No HJB, no value function, no Riccati, no
  utility; the quote rule (5.3) is a heuristic built on predicted tick jumps.
- **Several quoted assets / cross-asset excitation.** One security is traded (p. 24); no
  cross-security excitation is estimated, despite data on 100 securities.
- **Interpretable excitation estimates.** No kernel, branching ratio or cross-excitation value is
  reported; the "feedback loop" is asserted, not measured.
- **Reinforcement learning.** Future work (p. 41).
- **Comparison with model-based market makers** (AS, GLFT, CJR) — only PMM and NHMM are benchmarks.
- **Statistical significance** of the P&L differences.

## Model card

- **Assets:** 1 security quoted (p. 24); simulator "multi-asset" in design (p. 5); ITCH sample of 100
  securities used for training data (p. 30), role in the model unspecified.
- **Kernel:** other — neural (stacked-LSTM) intensity with power-law memory-cell decay (eq. 4.4); no
  parametric kernel.
- **Excitation:** self and cross between six event types of one book (limit/market buy/sell,
  partial/full cancel), implicit in network weights; claimed feedback from book state; **no
  cross-asset**; no values.
- **Who excites the flow:** all LOB events in the training data; in the simulator, unspecified whether
  the maker's own orders enter the DHP history (n/a — not stated).
- **Objective:** none optimised; evaluation reward = PnL + inventory revaluation − quadratic
  transaction cost (eq. 5.22); normalised P&L and mean absolute position as metrics.
- **Solution method:** other — supervised point-process learning (MLE) + prediction-based quote rule;
  no RL, no DP.
- **Benchmark:** PMM (Das 2005 Glosten–Milgrom learner) and NHMM (Mei–Eisner neural Hawkes).
- **Reported numbers:** NPnL [10⁵] 2.1 ± 18.26 (DHMM) vs 1.1 ± 4.09 (NHMM) vs −1.6 ± 79.55 (PMM); MAP
  17 / 4 / 41 (Table 3, p. 37). No regret (n/a — no optimum).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 2, 6, 7, 8, 11, 12.**

### What this focus needs beyond the Kernthesen

1. **There is no control problem, so no closure question arises.** The paper replaces the
   stochastic-control route (criticised for «unrealistic assumptions», p. 13, and because the
   resulting «control algorithms are associated with continuous semi-martingales, which are hard to
   solve recursively», p. 15) by a learned intensity and a heuristic quote. It is therefore evidence
   about *flow modelling*, not about where a closed form holds or breaks.
2. **The LSTM state as an implicit lift.** *Inference:* the hidden state $(h,c)$ with deterministic
   inter-event decay (eq. 4.4) and jumps at events (eq. 4.3) is a learned, finite-dimensional,
   nonlinear Markov state for the flow — structurally the role a [[markov-lift]] plays for a Hawkes
   kernel, but without linearity in the intensity, so neither the GLFT linearisation nor a quadratic
   ansatz could exploit it. The power-law decay in (4.4) is singular at $t=t_n^+$ for $\bar p>0$ and
   departs from the exponential decay of Mei–Eisner; the paper does not discuss this.
3. **Multi-asset / cross-asset: number of instruments = 1.** The "multi-asset" wording (pp. 5, 21) is
   about the simulator's architecture; the strategy is single-security (p. 24). Cross-excitation is
   among six event types within one book and is never quantified. Nothing carries over directly to
   cross-asset excitation, beyond the general claim that a non-parametric intensity can absorb
   inhibition and state feedback that a positive linear Hawkes cannot (p. 10).
4. **What the learned component is compared against.** The learned *model* (DHP) is compared with
   NHP on next-event prediction (RMSE, error rate); the resulting *trader* with NHMM and the
   Glosten–Milgrom PMM on normalised P&L (Table 3). Neither a closed-form market maker nor an exact
   optimum is in the comparison.
5. **Who excites.** Not addressed ([[who-excites-the-flow]]). Because the DHP is fitted offline on
   ITCH data and then used inside an agent-based simulator, the maker's own orders presumably enter
   the simulated book and thus the event stream — but this is not stated.

### Direct quotes (for the draft)

> "The basic idea behind our approach is to view the conditional intensity of the Hawkes process as a nonlinear deterministic function of past history, and to use DLSTM to automatically learn a high-dimensional representation from the data." (p. 16)

> "We also assume that the high-frequency market maker is trading a single security in a market whose price at time t is denoted by p_t." (p. 24)

> "Embedding DHP within the reinforcement learning framework to learn the optimal policy." (p. 41, future direction 3)

### Examples & illustrations (for later drafting)

- Table 3 (p. 37): DHMM NPnL 2.1 ± 18.26 vs NHMM 1.1 ± 4.09 — a mean advantage with four-fold
  dispersion, a cautionary example of P&L comparisons without risk adjustment or tests.
- Fig. 5 vs Fig. 6 (pp. 34–35): the same model fails at nanosecond and works at millisecond
  resolution — event-time resolution is itself a modelling choice for Hawkes fits.

### Boundary of this focus

The paper is neither multi-asset nor a control-theoretic market-making model. It enters the
project's literature map as a learned-intensity, prediction-based single-security market maker cited
by [[lai-2023-data-driven-deep]] (p. 777) and in the Barzykin reference list; it bears on the gap
claim only negatively (it does not supply a closed form, an exact solution or an RL policy).

## Contested / inconsistent in the source

- **Fig. 1 description (p. 6):** bid 168.60 above ask 168.50, and mid price «150.05» — internally
  inconsistent; the example on p. 8 uses prices 100.00/100.10 «from LOB illustrated in Figure 1».
- **Training length (p. 32):** «trained in the simulation framework for 1000 trading days» vs «we train
  market makings agents using DHP and NHP for 100 trading days five times»; Table 2 says 1000 train /
  300 test.
- **Table 4 (p. 38):** two rows labelled "Simulated AV", and the text calls both NC and WC «no
  cancellation» / «without cancellation».
- **"Optimal" in the abstract** (p. 1) without an optimisation; **"multi-asset"** without a
  multi-asset strategy.
- **Eq. 5.3** gives the same formula for $p^a$ and $p^b$ (no side-specific spread term).
- **Eq. 4.4** power-law decay diverges at $t\downarrow t_n$ (see focus item 2).
- The **published 2024 version was not read**; any of these may have been corrected there.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]], [[glft-2013-model]], [[cartea-jaimungal-ricci-model]]
- Concepts: [[hawkes-process]], [[markov-lift]], [[who-excites-the-flow]]
- Other works (bibkeys): `bacry-2015-hawkes-processes-finance`, `gueant-2019-deep-reinforcement-learning` (Guéant–Manziuk, p. 15). Not in the library: Mei & Eisner 2017 (Neural Hawkes), Das 2005, Morariu-Patrichi & Pakkanen 2018, Gonzalez & Schervish 2017, Muni Toke 2011, Spooner et al. 2018, Moallemi & Yuan 2017, Lu & Abergel 2018, Sagheer & Kotb 2019, Vincent et al. 2010.

## Connections

- Builds on: [[hawkes-process]] (generalised to a neural intensity).
- Cites (critically): [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]], [[glft-2013-model]].
- Cited by: [[lai-2023-data-driven-deep]] (p. 777, as Kumar 2021).
- Compare: [[martin-2026-market-making-hawkes]] and [[acero-2026-hawkes-structured-networks]] (learned solutions of an actual Hawkes market-making control problem, with benchmarks), which this paper does not provide.
