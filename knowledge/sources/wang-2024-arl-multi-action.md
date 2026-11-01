---
title: "Wang–Ventre–Polukarov 2024 — ARL-Based Multi-Action Market Making with Hawkes Processes and Variable Volatility"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: wang-2024-arl-multi-action
depth: standard
based_on: preprint
read: arXiv 2508.16589v1
tags: [market-making, hawkes, adversarial-reinforcement-learning, multi-action, quoting-decision, sac, dqn, volatility, single-asset, fill-driven, mbt-gym]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Hawkes_intensity update «+ mean_reversion_speed × (baseline_arrival_rate − Hawkes_intensity) × dt + jump_size × last_match_result» (eq. 1, p. 3), taken from mbt-gym's HawkesArrivalModel."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Fill-driven: «last_match_result: The outcome of the most recent trade, where 1 indicates a successful trade and 0 indicates no trade» (p. 3); «A completed trade increases the probability of at least one subsequent trade, directly affecting the market maker's quoting strategy» (p. 7)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "«Our model draws inspiration from the market-making framework proposed by [3]» (p. 2), i.e. Avellaneda–Stoikov; exponential fill law in offset (p. 3)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Ref. [13], cited for addressing «inventory constraints in market-making models» (p. 2); not used."
---

# ARL-Based Multi-Action Market Making with Hawkes Processes and Variable Volatility

## Bibliographic Details

Wang, Ziyi, Carmine Ventre, and Maria Polukarov. 2024. "ARL-Based Multi-Action Market Making with
Hawkes Processes and Variable Volatility." In *Proceedings of the 5th ACM International Conference
on AI in Finance (ICAIF '24)*, Brooklyn, NY, 14–17 November 2024, pp. 437–444 (page range per
Yang–Xu 2026, ref. [36]). doi:10.1145/3677052.3698695. Preprint arXiv:2508.16589v1 [q-fin.TR],
7 August 2025. 8 pp. King's College London.

**Read: arXiv 2508.16589v1 (preprint); page numbers follow it.** The arXiv copy has no printed
page numbers; "p. N" is the PDF page N of 8 (published p. 436 + N, if the layout is identical,
unverified). Non-core work; preprint accepted under the project's preprint policy.

### Notation map (source → project, CLAUDE.md § Notation)

Most mathematical glyphs are lost in the PDF text layer (Unicode math-italic). The symbols below are
reconstructed from the prose and the Spooner–Savani/mbt-gym convention [I].

| Source term | Meaning in source | Project symbol / remark |
|---|---|---|
| price $Z_n$ (glyph lost) | arithmetic Brownian mid-price with drift $b$, volatility $\sigma$ | $S_t$ |
| bid / ask offset $\delta^\pm$ | $\pm(Z_n-p^\pm_n)\ge0$ | $\delta^b,\delta^a$ |
| `Hawkes_intensity` | self-exciting intensity (eq. 1) | $\lambda_t$ |
| `baseline_arrival_rate` $A^\pm$ | baseline, 10.0; adversary range [7.5, 12.5] | $\mu$ ⚠ not the GLFT amplitude $\Lambda$ |
| `mean_reversion_speed` | 60.0 | decay $\beta$ |
| `jump_size` | 40.0 per successful trade | jump $K\beta$ (scalar) |
| $k^\pm$ | depth sensitivity ("distribution of volume in the order book"); called "decay" in §4 | $k$ |
| inventory $Q_n\in[\underline Q,\bar Q]$ | bought minus sold | $q_t$, bound $Q$ |
| $\Pi=X+QZ$ | wealth | $X_t+q_tS_t$ |
| two risk coefficients (glyphs lost) | running / terminal quadratic inventory penalties in the reward | ≈ $\tfrac12\gamma\sigma^2$-type penalty, not CARA $\gamma$ |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction | 1–2 |
| ✓ | 2 Related work (stochastic control; RL; Hawkes processes in market dynamics) | 2 |
| ✓ F1 | 3.1 Market dynamics: price, execution (Hawkes, eq. 1), inventory | 2–3 |
| ✓ F1 | 3.2 Market participants: adversaries (fixed / random / strategic / single-parameter), three maker types | 4 |
| ✓ F1 | 4 Training process overview (reward; SAC adversary → SAC always-quoting → DQN multi-action) | 4–5 |
| ✓ F1 | 5.1 Metrics; Tables 1–7 (seven risk settings) | 5–6 |
| ✓ F1 | 5.2 Results analysis (always-quoting; Hawkes vs Poisson; multi-action; volatility), Figs. 2–7 | 5–8 |
| ✓ | 6 Conclusions | 8 |
| — | References | 8 |

## Kernthesen

### 1. The paper combines two earlier ARL lines: adversarial training (Spooner–Savani 2020) and a maker who may decline to quote (Wang et al. 2023) (pp. 1–2)

Spooner–Savani show that adversarial RL «can produce market-making agents that exhibit strong
robustness under epistemic uncertainty» (p. 1). Wang et al. 2023 «extends the action space of
market makers by relaxing the assumption that they must always quote at each time step», allowing
two-sided, bid-only, ask-only or no quotes (p. 1). The present paper keeps both features and changes
the market model: Hawkes instead of Poisson execution, and two volatility levels (p. 1).

### 2. ⭐⭐ Executions follow a discrete-time exponential Hawkes intensity excited by the maker's last successful trade, taken from mbt-gym (p. 3)

Eq. (1): `Hawkes_intensity = Hawkes_intensity + mean_reversion_speed × (baseline_arrival_rate −
Hawkes_intensity) × dt + jump_size × last_match_result`, with mean reversion 60.0, baseline 10.0,
jump 40.0, $dt=0.005$, and `last_match_result` = 1 after a successful trade, 0 otherwise (p. 3). The
update is «inspired by the HawkesArrivalModel class in [20]» (mbt-gym) and uses its parameters
(p. 3). The excitation is **fill-driven**: only the maker's own matches raise the intensity. The
text does not say whether there is one intensity for both sides or one per side; the formula uses a
single `Hawkes_intensity` for both $\lambda^\pm$ [ambiguous].

### 3. Fill intensity is the Hawkes level times the Avellaneda–Stoikov exponential in the quote offset (p. 3)

«The trade arrival intensity is given by: $\lambda^\pm_n$ = Hawkes_intensity $\cdot\,e^{-k^\pm\delta^\pm}$»
(p. 3), with $k^\pm>0$ describing «the distribution of volume in the order book». The text claims
that the approach «accounts for both the current market conditions and the market maker's
inventory» (p. 3), but no inventory term appears in the formula.

### 4. Prices are arithmetic Brownian motion with drift and no price impact; volatility is 2 or 200 (pp. 2–3, 7)

$Z_{n+1}=Z_n+b_n\Delta t+\sigma_nW_n$, $W_n\sim N(0,\Delta t)$, initial price 100, $\sigma=2$ in the base
case (pp. 2–3). The high-volatility case sets $\sigma=200$ (p. 7). Executions do not move the price.

### 5. ⭐ The adversary controls drift, Hawkes baseline and depth sensitivity, in fixed, random, strategic or single-parameter variants (pp. 4–5)

Fixed: $b=0$, $A^\pm=10$, $k^\pm=1.5$. Random: uniform per episode on $b\in[-5,5]$,
$A^\pm\in[7.5,12.5]$, $k^\pm\in[1.125,1.875]$. Strategic ("All"): chooses all three to minimise the
maker's reward; single-parameter adversaries ("A", "B", "K") control one each (p. 4). The
self-excitation parameters (jump size, mean reversion) are not adversarial. Two internal
inconsistencies: §4 describes the action as «the drift, Hawkes baseline rate and decay», although
$k$ is the depth parameter, and says the adversary acts «at each time step», whereas Random fixes
parameters per episode (p. 4).

### 6. ⭐ Three maker types differ in action space: always-quoting (continuous offsets), 2-action (quote / not) and 4-action (both / ask only / bid only / none) (p. 4)

Always-quoting chooses two continuous offsets in $[0,3]$. The 2-action maker chooses $\{0,1\}$ = no
quote / both sides. The 4-action maker chooses $\{0,1,2,3\}$ = none / both / ask only / bid only
(p. 4). The multi-action agents decide only *whether* to quote. Prices come from the trained
always-quoting policy: «If the decision is to quote, they use the well-trained Always Quoting MM
strategy to set the specific prices» (p. 7).

### 7. Training is sequential, not simultaneous: adversary first (SAC), then the always-quoting maker (SAC) against it, then the multi-action maker (DQN) (pp. 4–5)

«Since we define the adversary and the market maker in a zero-sum game, we first train the
adversary agent» with SAC for at least 50,000 episodes, policy updates every 1000 steps, learning
rate $3\times10^{-4}$, batch 64 (p. 4). The always-quoting maker is then trained with SAC «leveraging
the trained adversary strategy» (p. 4). The multi-action makers are trained with DQN (≥50,000
episodes, learning rate $10^{-4}$, batch 64) on top of both (pp. 4–5). The paper does not say how
the adversary can be trained before any maker policy exists.

### 8. Reward: change in wealth minus quadratic inventory penalties; risk-neutral and six risk-averse settings (pp. 4–5)

$r_t=\Delta\Pi_t$ minus two quadratic inventory terms (running and terminal; glyphs lost). With
both coefficients zero the setting is risk-neutral (RN), otherwise risk-averse (RA) (p. 4). Tables
1–7 cover coefficient pairs (0, 0), (0.01, 0), (0.1, 0), (0.5, 0), (1.0, 0), (0, 0.01), (0, 0.001)
(pp. 5–6). The text says «six different sets of RA coefficients» (p. 4) and «seven different sets of
risk coefficients» (p. 5), which agree if RN is counted.

### 9. Evaluation: every strategy is tested 100 × 1000 episodes against the fixed adversary on wealth, Sharpe, terminal inventory and quoting ratio (p. 5)

«All strategies were then evaluated 100 times, each with 1000 episodes, in a fixed adversarial
environment for testing» (p. 5). Terminal wealth is reported as «the mean ± the variance» (p. 5).
Sharpe is mean over standard deviation of terminal wealth. The quoting ratio is «no-quote ratio +
bilateral quote ratio + ask-only ratio + bid-only ratio» (p. 5). The text announces «six market
makers» but lists five. It also describes the 4-action (Train & Test @ vol=200) maker as «ultimately
tested in an environment with Volatility=2» (p. 5), contradicting its label.

### 10. ⭐ Adversarial training still pays under Hawkes execution: "All" adversary gives the best Sharpe, ahead of random and fixed training (pp. 5–6)

The always-quoting maker «under All Adversary training with three controlled parameters, it achieves
the best Sharpe ratio, outperforming the results from Random Adversary training, which in turn are
superior to those from Fixed Adversary training» (p. 5). Table 1 (RN): Sharpe 1.0351 (All), 0.7933
(Random), 0.6729 (Fixed); terminal wealth 3.8587 ± 3.7280 vs 2.1945 ± 3.2613 (Fixed) (p. 5). The
drift-only ("B") adversary beats Random; the baseline-only and depth-only adversaries show «no
significant advantage» (p. 5).

### 11. ⭐ The Hawkes-based maker earns less, with lower Sharpe, than Poisson-based makers in earlier papers; the authors attribute this to Hawkes complexity (p. 6)

«The market maker in this study performs worse overall in terms of wealth mean … and Sharpe ratio
compared to results using the Poisson process» (p. 6). Reasons offered: Hawkes «introduces more
complex dynamics and higher volatility», implementation differences, and parameters that need
re-tuning (p. 6). [I] The comparison is confounded: the Hawkes baseline is 10 (p. 3), whereas the
ARLMM Poisson baseline is 140 (as in Yang–Xu 2026, p. 6). The stationary Hawkes level stays far
below 140, so fewer fills, not clustering, may explain most of the drop.

### 12. ⭐ Given the option, the multi-action makers still quote both sides over 90 % of the time, in line with exchange market-maker obligations (p. 7)

«Despite having the option to refrain from quoting or to quote unilaterally, the agents choose to
provide both ask and bid prices over 90% of the time» (p. 7). The authors relate this to the London
Stock Exchange's 90 % quoting rule and Deutsche Börse's MiFID II regulated-market-maker requirement
of 50 % (p. 7). Both multi-action makers improve Sharpe slightly over always-quoting (p. 7); e.g.
Table 1, Fixed: 0.6934 (2-action) vs 0.6729 (p. 5).

### 13. ⭐⭐ Fill-driven self-excitation is argued to reward active quoting: a fill raises the chance of the next fill (p. 7)

«In the Hawkes process, the probability of order matching is significantly influenced by the
outcome of the previous trade. A completed trade increases the probability of at least one
subsequent trade, directly affecting the market maker's quoting strategy» (p. 7). With «rapid
intensity increase and slow intensity decay», this «encourages market makers to quote more
actively. Even in low liquidity environments, market makers are more willing to quote prices that
facilitate trades» (p. 7). This is a verbal statement of the fill-driven incentive: tighter quotes
buy future intensity. The paper does not isolate it experimentally (no Poisson control with the same
mean intensity).

### 14. A quoting-decision policy trained at low volatility transfers to high volatility; one trained at high volatility on low-volatility prices becomes conservative (pp. 1, 7–8)

The 4-action maker trained at $\sigma=2$ and tested at $\sigma=200$ «maintains relatively stable
performance» and provides «two-sided quotes at least 92% of the time» (p. 1; e.g. Table 5 Random:
94.63 % bilateral, Sharpe 1.1745, p. 6). The 4-action maker trained at $\sigma=200$, but using the
$\sigma=2$ always-quoting prices and adversary, often refuses or quotes one side and has lower Sharpe
(e.g. Table 1, Fixed: 74.19 % bilateral, 25.81 % bid only, Sharpe 0.6132, p. 5). The authors
attribute this to «misalignment with quoting strategies under high volatility» (p. 8). [I] With
$\Delta t=0.005$, $\sigma=200$ means a per-step price s.d. of about 14 on a price of 100.

### 15. Future work: train the 4-action maker entirely at high volatility (p. 8)

The conclusion proposes to «train a 4-Action MM under a volatility of 200 and examine whether it
chooses to quote and, if so, provides specific prices using strategies trained under this high
volatility» (p. 8). No extension to several assets or to cross-excitation is mentioned.

## Figures and tables

- Fig. 1 (p. 3): training/testing pipeline across volatility levels.
- Tables 1–7 (pp. 5–6): five maker types × adversary types × seven risk settings (wealth, Sharpe,
  terminal inventory, quoting ratios).
- Figs. 2–7 (pp. 6–7): terminal-wealth densities by maker and adversary (RN case).

## What this source does not address

- **Any control-theoretic solution.** No HJB, value function, closed form or equilibrium analysis;
  everything is model-free RL. For the single-stage game analysis in the same ARL line see
  [[yang-2026-robust-market-making]].
- **Flow-driven or cross-excitation.** One scalar self-exciting intensity driven by the maker's
  matches; no cross-side or cross-asset terms. Cross-excitation in RL:
  [[gasperov-2022-deep-reinforcement-learning]].
- **Several assets.** Single asset; not mentioned as future work.
- **Price impact / adverse selection.** None; added by [[yang-2026-robust-market-making]].
- **Comparison with an analytical policy** ([[avellaneda-stoikov-model]], [[glft-2013-model]]) or
  regret against an optimum.
- **Hawkes parameters as adversarial or estimated quantities.** Jump size and mean reversion are fixed.

## Model card

| Field | Value |
|---|---|
| Assets | 1 |
| Kernel | exponential in discrete time (Euler step, eq. 1): mean reversion 60, baseline 10, jump 40, $dt=0.005$ (mbt-gym HawkesArrivalModel) |
| Excitation | self only; whether bid and ask share one intensity is not stated (formula uses a single `Hawkes_intensity`); no cross-asset |
| Who excites the flow | the maker's own last match (`last_match_result` ∈ {0,1}) → fill-driven |
| Objective | $\Delta\Pi$ minus running and terminal quadratic inventory penalties (RN and six RA settings); zero-sum against an adversary choosing $(b,A,k)$; not CARA |
| Solution method | model-free RL: SAC (adversary, always-quoting offsets), DQN (2-/4-action quoting decision), trained sequentially |
| Benchmark | fixed vs random vs strategic adversary training; always-quoting vs multi-action makers; no analytical benchmark |
| Reported regret / gap numbers | none vs an optimum; e.g. RN always-quoting Sharpe 1.0351 (All adversary) vs 0.6729 (Fixed) (Table 1, p. 5); bilateral quoting ≥ 92 % when transferring $\sigma=2\to200$ (p. 1) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 2, 3, 5, 11, 13.**

### What this focus needs beyond the Kernthesen

1. **No closure.** The problem is never posed as a control problem with a value function; the
   question of closure does not arise. The paper is relevant only as a statement of the fill-driven
   convention in an RL environment (Kernthesen 2, 13).
2. **Branching ratio [I].** Unthinned, jump/decay = 40/60 ≈ 0.67 per unit of intensity; thinned by the
   fill probability $e^{-k\delta}$ the effective ratio is lower and depends on the quotes, as in
   [[yang-2026-robust-market-making]] (focus item 3). The stationary mean intensity therefore lies
   between 10 and about 30 (unthinned bound $10/(1-0.67)$), far below the Poisson baseline 140 of the
   ARLMM line. This supports the confound noted in Kernthese 11.
3. **Multi-asset carry-over: none.**

### Direct quotes (for the draft)

> "Firstly, we transition from using a Poisson process to a Hawkes process for modeling execution dynamics. The Hawkes process, with its self-exciting feature, has the potential to capture price jumps and self-reinforcing trading behaviors observed in real markets, which may enhance the alignment of our market model with actual market conditions." (p. 1)

> "In the Hawkes process, the probability of order matching is significantly influenced by the outcome of the previous trade. A completed trade increases the probability of at least one subsequent trade, directly affecting the market maker's quoting strategy." (p. 7)

> "This mechanism in the Hawkes process encourages market makers to quote more actively. Even in low liquidity environments, market makers are more willing to quote prices that facilitate trades, thereby enhancing liquidity." (p. 7)

### Examples & illustrations (for later drafting)

- The quoting-ratio columns (Tables 1–7, pp. 5–6): a ready, if anecdotal, illustration that an
  RL maker facing fill-driven Hawkes flow rarely withdraws its quotes.

### Boundary of this focus

No value function, no cross-excitation, no multi-asset content. The fill-driven mechanism is
asserted verbally (p. 7), not isolated by an experiment.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]] (base model), [[glft-2013-model]] (cited only).
- Concepts: [[hawkes-process]], [[who-excites-the-flow]], [[branching-matrix]] (scalar, inferred).
- Related sources: [[yang-2026-robust-market-making]] (later; cites this paper and adds impact + LSTM), [[gasperov-2022-deep-reinforcement-learning]] (RL under multivariate Hawkes).
- Other works (not in library): Spooner & Savani 2020 (ARLMM); Wang, Ventre & Polukarov 2023 (to quote or not to quote, ICAIF '23); Jerome et al. 2023 (mbt-gym, ICAIF '23); Haarnoja et al. 2018 (SAC); Roldan Contreras & Swishchuk 2022 (Hawkes HFT control); Abergel & Jedidi 2015.

## Connections

- Builds on: [[avellaneda-stoikov-model]]; [[hawkes-process]] (exponential, fill-driven, mbt-gym implementation).
- Extended by: [[yang-2026-robust-market-making]], which cites it (ref. [36]), adds per-side intensities, price impact, an adversary over the Hawkes parameters and an LSTM.
- Contrast with: [[gasperov-2022-deep-reinforcement-learning]]: RL with a multivariate cross-exciting LOB Hawkes model instead of a single fill-driven intensity.
