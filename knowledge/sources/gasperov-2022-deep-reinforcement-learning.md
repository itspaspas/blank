---
title: "Gašperov–Kostanjčar 2022 — Deep Reinforcement Learning for Market Making Under a Hawkes Process-Based Limit Order Book Model"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: gasperov-2022-deep-reinforcement-learning
depth: standard
tags: [market-making, hawkes, limit-order-book, reinforcement-learning, soft-actor-critic, weakly-consistent-lob, single-asset, benchmark]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«A multivariate linear Hawkes process with exponential kernels is used to model dependencies, namely cross-excitation and self-excitation effects, between different LOB order arrivals» (PDF p. 4); eqs. (1)–(2), (4)–(5)."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "«The model is also interactive in the sense that the market maker's controls (choice of placed limit and market orders) affect the order arrival intensities» (PDF p. 3) — asserted, but no equation specifies the feedback."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Benchmark class «linear in inventory and including inventory constraints … also includes the state-of-the-art Gueant-Lehalle-Fernandez-Tapia (GLFT) [3] approximations» (PDF p. 5)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«Standard MM benchmarks like the AS [1] approximations are ill-suited for our framework since they take into account neither the existence of the bid-ask spread nor the discrete nature of the underlying LOB» (PDF p. 5)."
  - target: cartea-jaimungal-ricci-model
    type: mentions
    confidence: ambiguous
    because: "The reward follows «the commonly used MM formulation described in [4]» (PDF p. 4), which is Cartea–Jaimungal–Ricci 2018 SIAM Review, not the 2014 paper the entity page describes."
based_on: preprint
---

# Deep Reinforcement Learning for Market Making Under a Hawkes Process-Based Limit Order Book Model

## Bibliographic Details

Gašperov, Bruno; Kostanjčar, Zvonko. 2022. "Deep Reinforcement Learning for Market Making Under a
Hawkes Process-Based Limit Order Book Model." *IEEE Control Systems Letters* 6: 2485–2490.
DOI 10.1109/LCSYS.2022.3166446. Laboratory for Financial and Risk Analytics, FER, University of
Zagreb. Code: github.com/BGasperov/drlformm (PDF p. 7).

**Read: arXiv 2207.09951v1 (preprint); page/equation numbers follow it.** The preprint has an IEEE
cover sheet as PDF p. 1 and no printed page numbers; the article runs PDF pp. 2–7 (presumably
journal pp. 2485–2490 in order, not verified). Page references below are **PDF pages**. Non-core
work; preprint accepted under the project's preprint policy.

### Notation map (source → project)

| Source | Meaning | Project |
|---|---|---|
| $I_t$, $X_t$, $W_t=I_tP_t+X_t$ | inventory, cash, wealth | $q_t$, $X_t$ |
| $\lambda_k(t)$, $\mu_k$ | Hawkes intensity, baseline of event type $k$ | $\lambda_t$, $\mu$ |
| $\alpha_{k,l}$, $\beta_{k,l}$ | excitation and decay of kernel $(k,l)$ (eq. 2) | $K$ entries ~ $\alpha_{k,l}/\beta_{k,l}$; $\beta$ |
| $\phi$ | running absolute-inventory penalty (eq. 12) | no project symbol |
| $\Delta_t$ | bid-ask spread (ticks) | — |
| $\alpha_t$ | "trend": net buy-minus-sell market-order intensity | ⚠ not the project's $\alpha$ |
| $Q^a_t, Q^b_t$; $A_t$ | agent's quotes; action = offsets from best prices (eq. 11) | $\delta^a,\delta^b$ (measured from the **touch**, not the mid) |
| $\delta$ | tick size | ⚠ clashes with project quote $\delta$ |
| $\mu,\beta$ (Appendix) | location/scale of the **jump-size** distribution | ⚠ not Hawkes baseline/decay |
| $Z_1,Z_2,Z_3$ | aggressiveness probabilities, fill probability at the touch | ~ $f(\delta)$ at the touch |
| $c$ | inventory bound | $Q$ |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | PDF pp. |
|---|---|---|
| — | IEEE preprint cover sheet | 1 |
| ✓ F1 | Abstract; I Introduction (RL for MM; LOB-model consistency; contribution) | 2–3 |
| ✓ F1 | II.A Multivariate Hawkes processes (eqs. 1–2) | 3 |
| ✓ F1 | III.A Event types (Biais 12 → 8; eqs. 3–6, Fig. 1) | 3 |
| ✓ F1 | III.B Simulation procedure (exponential kernels, Ogata thinning) | 4 |
| ✓ F1 | III.C Market making procedure (eqs. 7–9, simplifying assumptions) | 4 |
| ✓ F1 | IV.A–C State, action, reward (eqs. 10–13) | 4–5 |
| ✓ F1 | IV.D–E Controller design, SAC training | 5 |
| ✓ F1 | V Experiments: benchmarks, metrics (eqs. 14–15), Table I, Fig. 2 | 5–6 |
| ✓ F1 | V.C Sensitivity: background-intensity noise (Table II), fees (Fig. 4) | 6–7 |
| ✓ F1 | VI Conclusion; Appendix (hyperparameters) | 7 |
| — | References | 7 |

## Kernthesen

### 1. Most LOB models used for MM are inconsistent in direction, timing and volume, which creates phantom backtest gains (PDF pp. 2–3)

LOB models underlying MM «remain inconsistent with respect to direction, timing, and volume,
leading to phantom gains under backtesting and preposterous events [16], such as price decreases
after a large buy market order» (p. 2). In Avellaneda–Stoikov, price moves are «completely
independent of the arrivals of market orders and the LOB dynamics» (p. 2). Law & Viens's
weakly consistent model fixes direction and timing but «still assumes constant order arrival
intensities» (p. 3).

### 2. ⭐ Contribution: the first DRL market maker on a weakly consistent multivariate Hawkes LOB, deliberately reduced-form (PDF p. 3)

«To the authors' knowledge, our approach is the first to wed DRL to MM under such a model» (p. 3).
Full LOB models are avoided «because of the associated complexities and issues»; a reduced-form
model and «a number of additional simplifying assumptions about microstructural dynamics» balance
realism and tractability (p. 3).

### 3. ⭐⭐ The authors claim the market responds to the maker's orders, but specify no mechanism (PDF p. 3)

«The model is also interactive in the sense that the market maker's controls (choice of placed
limit and market orders) affect the order arrival intensities, i.e., the market responds
dynamically to the market maker's control strategy» (p. 3). No equation shows how the agent's
orders enter $N(t)$ or $\lambda(t)$: eqs. (4)–(5) define the 8 market event counts, and eqs.
(7)–(9) define the agent's fills as indicator-thinned market orders (eq. 8). The agent's market
orders are «aggressive with probability $Z_1$» and its cancellations «with probability $Z_2$»
(p. 4), which suggests they are classified as Biais events, but whether they are then fed into the
Hawkes history is not stated. The published code (not consulted) would settle it.

### 4. ⭐ Eight-variate exponential Hawkes process with full self- and cross-excitation across event types (PDF pp. 3–4)

From Biais–Hillion–Spatt's 12 LOB event types, the four non-aggressive limit orders and
cancellations (types 9–12) are dropped as affecting neither prices nor top-of-book volume, leaving
(eq. 3) $E_{all}=\{M^a_b,M^a_s,L^a_b,L^a_s,C^a_b,C^a_s,M^n_b,M^n_s\}$: aggressive market, limit and
cancel orders per side and non-aggressive market orders per side (p. 3). Intensity (eq. 2):
$\lambda_k(t)=\mu_k+\sum_{l=1}^p\int_0^{t-}\alpha_{k,l}e^{-\beta_{k,l}(t-s)}dN_l(s)$ with $p=8$ and
pair-specific decays. «A multivariate linear Hawkes process with exponential kernels is used to
model dependencies, namely cross-excitation and self-excitation effects» (p. 4); exponentials are
chosen for simulation tractability, short memory, and «the Markovian properties of the process»
(p. 4). Simulation by Ogata's thinning (p. 4). **The values of $\mu_k,\alpha_{k,l},\beta_{k,l}$ are
not reported anywhere in the paper**; the Appendix's $\mu=0.01$, $\beta=0.08$ are jump-size
parameters (p. 7).

### 5. Mid-price is the signed sum of i.i.d. jump sizes of aggressive events (PDF p. 3)

Eq. (6): $P_t=P_0+(\sum_{E_{inc}}J_e-\sum_{E_{dec}}J_e)\,\delta/2$, $E_{inc}=\{M^a_b,L^a_b,C^a_s\}$,
$E_{dec}=\{M^a_s,L^a_s,C^a_b\}$; jumps i.i.d., independent of timing (p. 3), exponential (truncated
where needed) with location $\mu$ and scale $\beta$ (p. 4). Price impact is therefore entirely
event-driven: the excitation structure determines price dynamics.

### 6. Discrete-time MM procedure: cancel, observe, quote, process events, reward (PDF p. 4)

At each step the agent cancels outstanding limit orders, observes $S_t$, posts a limit-order pair
or a market order; inventory bound $|I|\le c$; simulated events are then processed; filled orders
are not replaced within the step (p. 4). Fills (eq. 8): $dN^b_t=dN_{M^a_s}\mathbb 1_{fill}+dN_{M^n_s}\mathbb 1_{fill}$;
at the touch, a non-aggressive MO fills the agent with fixed probability $Z_3$, all or nothing
(p. 4). Unit order size (p. 5).

### 7. ⭐ The state is only (inventory, spread, trend), and the trend is the net market-order intensity (PDF p. 4)

Eq. (10) $S_t=(I_t,\Delta_t,\alpha_t)$ with $\alpha_t=\lambda_{M^a_b}+\lambda_{M^n_b}-\lambda_{M^a_s}-\lambda_{M^n_s}$
(p. 4). So the controller sees the Hawkes state only through **one scalar projection** of the
eight intensities; limit- and cancel-order intensities and the buy/sell level are not observed.
Spread and trend are z-scored using a 100,000-step random-action trajectory (p. 4).

### 8. Action = continuous offsets from the best quotes, rounded to ticks; crossing quotes become market orders (PDF p. 4)

Eq. (11) $A_t=(Q^a_t-P^a_t,\;P^b_t-Q^b_t)$; negative quoted spreads ignored; a bid at or above the
best ask is a market buy (p. 4).

### 9. Objective: expected terminal wealth minus an absolute-inventory running penalty (PDF pp. 4–5)

Eq. (12) $\mathbb E^\pi[W_T-\phi\int_0^T|I_t|dt]$, inspired by Cartea–Jaimungal–Ricci 2018, but with
$|I|$ «instead of the quadratic inventory penalty to obtain a convenient value at risk (VaR)
interpretation» (p. 5). Reward (13): $\Delta W-\phi\int|I|$. Not CARA. $\phi=0.01$, $T=100$,
$\Delta t=1$, $c=3$ (p. 7).

### 10. SAC with a 2×64 MLP; DQN unstable, TD3 inferior (PDF p. 5)

SAC (Stable Baselines), $10^6$ training steps, discount $\gamma=1$ (p. 5, p. 7). «DQN … suffers
from severe instability issues, especially in its vanilla variant. TD3 … was eventually excluded
due to its inferior performance» (p. 5).

### 11. ⭐ Benchmarks are heuristic: SYM (always at the touch) and LIN (best inventory-linear rule, a class containing GLFT-form approximations); AS is rejected (PDF p. 5)

«Standard MM benchmarks like the AS [1] approximations are ill-suited for our framework since they
take into account neither the existence of the bid-ask spread nor the discrete nature of the
underlying LOB» (p. 5). The authors «consider a class of MM strategies linear in inventory and
including inventory constraints. Among the members of this class we denote the best performing one
as the LIN strategy. Note that this class of strategies also includes the state-of-the-art
Gueant-Lehalle-Fernandez-Tapia (GLFT) [3] approximations» (p. 5). How LIN was selected (grid,
in-sample) is not stated; no GLFT formula is evaluated with model parameters, and no benchmark uses
the Hawkes state.

### 12. ⭐⭐ DRL beats both benchmarks on mean PnL, Sharpe and lower tail over 1,000 Monte Carlo episodes (PDF pp. 5–6)

Table I (p. 5), $10^3$ simulations; Sharpe defined as mean/std of terminal PnL per episode (eq. 15),
**not annualised**:

| Metric | DRL | SYM | LIN |
|---|---|---|---|
| Mean episode return | 13.3378 | 8.3913 | 7.6772 |
| Mean PnL | 13.7567 | 9.8686 | 8.2105 |
| Std PnL | 8.4952 | 8.2443 | 5.7884 |
| Sharpe | **1.6193** | 1.1970 | 1.4184 |
| 10th pct PnL | 4.9445 | 1.6775 | 2.7400 |
| Kurtosis PnL | 4.2083 | 6.0552 | 10.5585 |
| Abs. mean terminal inv. | 0.454 | 1.46 | 0.56 |
| Mean absolute position (MAP) | 0.4232 | 1.4659 | 0.5478 |
| Mean PnL / MAP | 32.5064 | 6.7321 | 14.9881 |

«the DRL strategy outperforms both of the benchmarks with respect to the vast majority of the
considered metrics» (p. 5). LIN has the lowest PnL std; DRL wins on Sharpe by 0.20 over LIN. No
standard errors or significance tests on the differences.

### 13. Robustness to perturbed background intensities: Sharpe degrades monotonically with noise (PDF p. 6)

Gaussian noise (variance 0.1/0.2/0.3) added to all baselines $\mu_k$: Sharpe 1.3766 / 1.0175 /
0.8638; MAP 0.4443 / 0.5038 / 0.5486; mean PnL 13.21 / 13.26 / 15.51 (Table II, p. 6). The
excitation matrix is not perturbed.

### 14. Fee tolerance: DRL survives limit-order fees to about 0.6 %, LIN to below 0.4 %, SYM below 0.2 % (PDF pp. 6–7)

Fig. 4: DRL «capable of tolerating the inclusion of fees for limit order transactions, up to the fee
of around 0.6%», LIN negative at 0.4 %, SYM already at 0.2 % (p. 6). Retrained DRL trades less as
fees rise: 24.54 / 15.0 / 11.28 / 7.85 transactions per episode at 0 / 0.2 / 0.4 / 0.6 % (pp. 6–7).

### 15. Future work: full LOB, power-law kernels, robust adversarial RL (PDF p. 7)

«Further research might consider more advanced MM models which take into account the full limit
order book, or are based on Hawkes processes with alternative (power-law or polynomial) kernels.
Finally, robust adversarial RL [31] might be used» (p. 7).

## What this source does not address

- **More than one asset.** Single asset; the 8 dimensions are event types.
- **Any HJB, value function or closed form.** The control problem is posed as an MDP and solved
  only by RL; no Riccati, ODE or lift. GLFT appears only as a member of the LIN benchmark class.
- **An optimum or regret.** No exact solution exists in the paper; all comparisons are against
  heuristics.
- **Hawkes parameters and calibration.** $\mu,\alpha,\beta$ of the Hawkes process are not given;
  no calibration to data; kernel stability ($\rho(K)<1$) not discussed.
- **A specified feedback from the agent to the intensities** (Kernthese 3).
- **CARA utility**; quote-dependent fill probability beyond the fixed $Z_3$ at the touch.

## Model card

- **Assets:** 1.
- **Kernel:** single exponential per pair $(k,l)$, $\alpha_{k,l}e^{-\beta_{k,l}t}$ (eq. 2); parameter
  values not reported.
- **Excitation:** 8-variate, self and cross across event types (aggressive MO/LO/CO per side,
  non-aggressive MO per side), i.e. cross-side and cross-order-type; no cross-asset.
- **Who excites the flow:** all market events; the authors additionally *claim* the maker's limit and
  market orders affect intensities (p. 3) without giving the mechanism → order-driven feedback
  asserted, unspecified.
- **Objective:** risk-adjusted, $\mathbb E[W_T-\phi\int|I_t|dt]$ (absolute, not quadratic, penalty);
  not CARA.
- **Solution method:** model-free deep RL (SAC, 2×64 MLP, $10^6$ steps); DQN/TD3 tried and dropped.
- **Benchmark:** SYM (touch quoting), LIN (best inventory-linear rule with constraints; class contains
  GLFT-form quotes). AS rejected as ill-suited.
- **Reported numbers:** per-episode Sharpe DRL 1.62 vs LIN 1.42 vs SYM 1.20; mean PnL 13.76 / 8.21 /
  9.87; MAP 0.42 / 0.55 / 1.47; fee break-even ≈ 0.6 % / < 0.4 % / < 0.2 %; no regret.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 3, 4, 7, 9, 11, 12, 13.**

### What this focus needs beyond the Kernthesen

1. **Closure: not attempted.** The paper never writes a value function. It is an RL-only data point;
   its relevance is as a **benchmark design** precedent, not a closure result.
2. **Who excites the flow — a third convention, asserted.** Kernthese 3 places the paper outside
   both conventions in [[who-excites-the-flow]]: neither purely flow-driven (exogenous) nor
   fill-driven, but **order-driven** (the maker's placed orders feed intensities). If true, the
   control enters the intensity dynamics directly, which is the case where neither the GLFT
   linearisation nor the BEGV quadratic closure is expected to survive, because the policy shapes
   the forecast (inference; cf. [[barzykin-2026-hawkes-driven-otc]] Kernthese 4, where the
   opposite convention is chosen precisely to keep the forecast quote-independent). Since the
   mechanism is unspecified, this should be treated as unverified until the code is checked.
3. **The RL agent sees almost none of the Hawkes state.** Only the scalar net MO intensity
   $\alpha_t$ enters (eq. 10). Any advantage over LIN therefore comes from conditioning on one
   linear functional of $\lambda$ plus the spread. For the project's RL design this is a lower bound
   on state richness; Jain et al.'s ablation ([[jain-2025-impulse-control-hawkes]], Kernthese 15)
   shows that removing intensities entirely turns Sharpe negative.
4. **Benchmark weakness relevant to the gap claim.** The only "closed-form" comparator is the best
   member of an inventory-linear class that "includes" GLFT-type rules; it is not a Hawkes-aware
   closed form, and there is no exact solution. The paper therefore does **not** contain the
   project's three-way comparison (Hawkes closed form vs exact vs RL); it is a two-way RL-vs-heuristic
   comparison with Sharpe gaps of 0.20 (vs LIN) and 0.42 (vs SYM) per episode.
5. **Cross-asset.** Nothing carries over directly; the 8×8 cross-type excitation is single-asset.
   The pair-specific decays $\beta_{k,l}$ mean an exact Markov lift would need up to 64 states
   ([[markov-lift]]) — same arithmetic as Jain et al.'s 144 for 12 types (inference).

### Direct quotes (for the draft)

> "The model is also interactive in the sense that the market maker's controls (choice of placed limit and market orders) affect the order arrival intensities, i.e., the market responds dynamically to the market maker's control strategy." (PDF p. 3)

> "Standard MM benchmarks like the AS [1] approximations are ill-suited for our framework since they take into account neither the existence of the bid-ask spread nor the discrete nature of the underlying LOB [29]." (PDF p. 5)

> "We consider a class of MM strategies linear in inventory and including inventory constraints. Among the members of this class we denote the best performing one as the LIN strategy. Note that this class of strategies also includes the state-of-the-art Gueant-Lehalle-Fernandez-Tapia (GLFT) [3] approximations." (PDF p. 5)

### Examples & illustrations (for later drafting)

- Table I (PDF p. 5): DRL vs LIN vs SYM — Sharpe 1.62 / 1.42 / 1.20; 10th-percentile PnL 4.94 /
  2.74 / 1.68: RL's gain sits mostly in the lower tail.
- Fig. 4 (PDF p. 7): Sharpe vs limit-order fee for the three strategies; fee break-evens ≈ 0.6 %,
  0.4 %, 0.2 %.

### Boundary of this focus

Single-asset, reduced-form LOB, RL vs heuristics, short episodes ($T=100$ steps), Hawkes
parameters unreported. Whatever is said here about closure or lift dimension is the project's
inference; the paper is silent on value functions.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]], [[glft-2013-model]], [[cartea-jaimungal-ricci-model]] (the 2018 SIAM Review paper is what is cited)
- Concepts: [[hawkes-process]], [[who-excites-the-flow]], [[markov-lift]]
- Sources in this wiki: [[jain-2025-impulse-control-hawkes]] (cites this paper)
- Other works (not in library): Law & Viens 2019 (weakly consistent LOB); Biais, Hillion & Spatt 1995 (event taxonomy); Ogata 1981; Bacry, Mastromatteo & Muzy 2015; Lu & Abergel 2018; Guéant & Manziuk 2019 (multi-asset DRL MM in corporate bonds); Spooner et al. 2018; Lim & Gorse 2018; Sadighian 2019; Gašperov & Kostanjčar 2021 (MM with signals via DRL); Guéant 2016.

## Connections

- Cited by [[jain-2025-impulse-control-hawkes]] (p. 2), which describes the LIN/SYM benchmarks as «a stochastic control baseline» — an overstatement: the baselines are heuristic rules, one class merely containing GLFT-form quotes.
- Compare [[acero-2026-hawkes-structured-networks]]: also RL on Hawkes flow, but with neural baselines only and one 2-asset configuration.
- Cites [[glft-2013-model]] as a member of its benchmark class; rejects [[avellaneda-stoikov-model]] as a benchmark.
