---
title: "Yang–Xu 2026 — Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: yang-2026-robust-market-making
depth: standard
tags: [market-making, hawkes, adversarial-reinforcement-learning, zero-sum-game, robustness, price-impact, ppo, lstm, cvar, single-asset, fill-driven]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Bilateral discrete-time Hawkes intensities «λ±_{n+1} = λ±_n + κ_{H,n}(A_n − λ±_n)Δt + γ_{H,n}ΔN±_n» (eq. 4, p. 4); Poisson recovered at γ_H = 0."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Fill-driven: the same counts ΔN± that move inventory (eq. 6) drive the intensity jump (eq. 4, p. 4); Table 1 lists «Trade-to-arrival-intensity feedback» (p. 2)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "Extends ARLMM, which «converts the Avellaneda–Stoikov model into a zero-sum stochastic game between a market maker and an environmental adversary» (p. 2); execution intensity λe^{−kδ} (eq. 5, p. 4)."
  - target: wang-2024-arl-multi-action
    type: cites
    confidence: extracted
    because: "Cited as ref. [36] (p. 18) in the line of ARL market making with Hawkes arrivals; Yang–Xu add trade-induced price impact and an LSTM state (Table 1, p. 2)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Ref. [3] (p. 16), among optimal-control extensions of Avellaneda–Stoikov «to alternative utility functions, risk preferences, and market settings» (p. 1)."
  - target: jusselin-2021-persistent-order-flow
    type: cites
    confidence: extracted
    because: "Ref. [19] (p. 17), cited for «Hawkes processes for persistent order flow» (p. 3); not used in the model."
  - target: fujii-2015-optimal-position-management
    type: cites
    confidence: extracted
    because: "Ref. [20] (p. 17), cited among «models of price impact» (p. 3); not used in the model."
  - target: gasperov-2022-deep-reinforcement-learning
    type: mentions
    confidence: inferred
    because: "Not cited. Both train model-free RL quoting policies in a single-asset Hawkes environment; Gašperov–Kostanjčar use a multivariate LOB Hawkes model, Yang–Xu a two-intensity fill-driven one with an adversary."
---

# Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning

## Bibliographic Details

Yang, Hao, and Zhenguo Xu. 2026. *Robust Market Making with Hawkes Order Flow and Price Impact via
Adversarial Reinforcement Learning*. arXiv:2609.22785v1 [cs.LG], 19 September 2026. 18 pp.
Affiliations: North China Institute of Computer System Engineering (Beijing); University of
Science and Technology of China (Hefei).

**Read: arXiv 2609.22785v1.** No published version is known; the preprint is its own original
under the project's preprint policy. Page numbers are the printed ones (they coincide with the PDF
pages).

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $Z_n$ | mid-price (discrete time) | $S_t$ |
| $H_n$ | inventory | $q_t$ ⚠ **not** a Hamiltonian $H^{i,s}$ |
| $X_n$ | cash | $X_t$ |
| $\delta^\pm_n$ | quote depths; $+$ = bid, $-$ = ask (eq. 2) | $\delta^b,\delta^a$ |
| $\lambda^\pm_n$ | Hawkes conditional intensity per side (eq. 4) | $\lambda_t$ (one component per side) |
| $A_n$ | baseline liquidity, mean-reversion target of $\lambda$ | $\mu$ (baseline) ⚠ not the GLFT amplitude $\Lambda$ and not the Riccati coefficient $A$ |
| $\kappa_{H}$ | mean-reversion speed of $\lambda$ | decay $\beta$ |
| $\gamma_{H}$ | jump of $\lambda$ per own fill | scalar branching entry $K\beta$ (jump size) ⚠ **not** risk aversion $\gamma$ |
| $k^\pm$ | depth sensitivity in $\lambda e^{-k\delta}$ | $k$ |
| $\Lambda^\pm_n=\lambda^\pm_n e^{-k^\pm\delta^\pm_n}$ | effective execution intensity (eq. 5) | $\lambda_t f(\delta)$ with $\Lambda\equiv1$ |
| $\xi_n$ | price impact per unit net execution (eq. 1) | no project symbol |
| $b_n$ | mid-price drift; also the adversary's choice in the single-stage game | — |
| $\Pi=X+HZ$ | mark-to-market value (eq. 8) | $X_t+q_tS_t$ |
| $\Delta N^\pm_n$ | executions on each side in step $n$ | the maker's fills $dN^b,dN^a$ |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (ARLMM; Hawkes and impact as missing effects; Table 1); 1.1 Contributions; 1.2 Related work | 1–3 |
| ✓ F1 | 2 Trading model, eqs. (1)–(8) | 4 |
| ✓ F1 | 3 Game formulation and single-stage analysis: Def. 1, payoff (9), Lemma 1, Thms. 1–2 | 5 |
| ✓ F1 | 4 Adversarial training: Fixed / Random / ARLMM / Ours; 4.1 learning configuration, reward (13) | 5–6 |
| ✓ F1 | 5 Experiments: setup; 5.1 robustness metrics (CVaR, bootstrap test (14)); Table 2; 5.2 results RQ1–RQ6, Figs. 1–2 | 7–11 |
| ✓ | 6 Conclusion | 11 |
| ✓ F1 | App. A derivation of payoff (9); B–D proofs of Lemma 1, Thms. 1–2 | 11–13 |
| — | App. E complete results, Table 3 (19 environments) | 13–15 |
| — | References | 16–18 |

## Kernthesen

### 1. ⭐ Robustness to model misspecification is sought by training the maker against an environmental adversary in a zero-sum game (pp. 1–2, 5)

The paper continues Spooner–Savani's ARLMM (arXiv 2003.01820), which «converts the
Avellaneda–Stoikov model into a zero-sum stochastic game between a market maker and an
environmental adversary» (p. 2). The adversary picks the episode's market parameters to minimise
the maker's return, so the maker learns a policy that «remains effective under these unfavorable
regimes» (p. 2). Def. 1 makes the stage payoff the expected change in mark-to-market value
$\mathbb E[\Delta\Pi]$, with the adversary receiving its negative (p. 5). The adversary «may be
interpreted as a proxy for the rest of the market» (p. 5).

### 2. ⭐⭐ Order flow is a pair of one-sided, discrete-time exponential Hawkes intensities excited by the maker's own executions (p. 4)

Eq. (4): $\lambda^\pm_{n+1}=\lambda^\pm_n+\kappa_{H,n}(A_n-\lambda^\pm_n)\Delta t+\gamma_{H,n}\Delta N^\pm_n$,
with baseline $A_n>0$, mean reversion $\kappa_{H,n}>0$ and self-excitation $\gamma_{H,n}\ge0$. This is
an Euler step of an exponential-kernel Hawkes intensity. Each side excites only itself: there is no
cross-side term. The counts $\Delta N^\pm$ are the same ones that move inventory,
$H_{n+1}=H_n+\Delta N^+_n-\Delta N^-_n$ (eq. 6), so the excitation is **fill-driven**: the maker's
fills raise its own future fill intensity. Table 1 names this «Trade-to-arrival-intensity feedback»
as a new mechanism relative to ARLMM (p. 2). «The Poisson model is recovered as the special case
$\gamma_{H,n}=0$ and $\lambda^\pm_n\equiv A_n$» (p. 4).

### 3. Fills follow the Avellaneda–Stoikov exponential-depth law applied to the current Hawkes intensity (p. 4)

«Conditional on quote depth, the effective execution intensity is $\Lambda^\pm_n=\lambda^\pm_ne^{-k^\pm_n\delta^\pm_n}$»
(eq. 5), with depth decay $k^\pm>0$. Quote depths are $\delta^\pm_n=\pm(Z_n-p^\pm_n)\ge0$ (eq. 2);
spread and reservation price follow (eq. 3). The intensity therefore factorises as Hawkes level
times a fill probability, as in GLFT-type models with stochastic intensity.

### 4. Each execution moves the mid-price linearly against the maker (p. 4)

Eq. (1): $Z_{n+1}=Z_n+b_n\Delta t+\sigma_nW_n+\xi_n(\Delta N^-_n-\Delta N^+_n)$, with «$\xi_n\ge0$ the
price impact induced by one unit of net execution» (p. 4). A bid fill (the maker buys) lowers the
mid; an ask fill raises it. This is an adverse-selection channel: «executions may themselves affect
short-run prices, feeding trading activity back into inventory valuation and mark-to-market returns»
(p. 2). The impact is permanent in the model (no decay term).

### 5. ⭐⭐ In the single-stage game the Hawkes state enters only through the current intensities, and the payoff is linear in them (pp. 4–5, 11–12)

«Once current inventory $H$ and the current Hawkes state are fixed, the effects of
$(A,\kappa_H,\gamma_H)$ on the current-period payoff are summarized by $(\lambda^+,\lambda^-)$» (p. 5).
After dropping $\Delta t$, eqs. (1)–(8) give
$f(\delta^\pm;b,\lambda^\pm,k^\pm,\xi)=\Lambda^+(\delta^++b-\xi)+\Lambda^-(\delta^--b-\xi)+bH$ (eq. 9),
derived in App. A from $\mathbb E[\Delta N^\pm]=\Lambda^\pm\Delta t$ and $\mathbb E[\Delta N^+\Delta N^-]=o(\Delta t)$
(pp. 11–12). The stage payoff contains no inventory penalty and no term for how a fill changes the
next intensity.

### 6. ⭐⭐ A pure-strategy Nash equilibrium exists for fixed intensities, and the interior best response does not depend on the intensity (p. 5, App. B–C)

Lemma 1: $f$ is concave in $\delta^+$ on $[0,2/k^+-b+\xi]$ and in $\delta^-$ on $[0,2/k^-+b+\xi]$
(eq. 10); the Hessian is diagonal (App. B, p. 12). Thm. 1: for drift $b\in[\underline b,\bar b]$ there
is a pure Nash equilibrium (Sion's minimax theorem, since $f$ is affine in $b$; App. C, p. 12). At an
interior equilibrium «the market maker's best response satisfies $\delta^+=\frac1{k^+}-b+\xi$,
$\delta^-=\frac1{k^-}+b+\xi$» (eq. 11), and the adversary picks $b$ minimising the resulting payoff
(eq. 12). Since $\lambda^\pm$ only multiplies each side's payoff, it scales the payoff but leaves
the maximiser unchanged. Inventory $H$ enters only through $bH$, which does not depend on $\delta$.

### 7. A mixed-strategy equilibrium exists for the general reduced-form game (p. 5, App. D)

Thm. 2: if $(b,\lambda^+,\lambda^-,\xi)$ ranges over a product of bounded closed intervals and $k^\pm$
is fixed, the single-stage game has a mixed Nash equilibrium. Proof by Glicksberg's theorem for
continuous games on compact sets (App. D, p. 13). No equilibrium result is given for the
200-stage game.

### 8. ⭐ Enlarging the adversary's parameter space strengthens non-stationarity, which the authors address with an LSTM over the observation window (pp. 2, 5–6)

The adversary now picks $(b,A,k,\kappa_H,\gamma_H,\xi)$ per episode instead of $(b,A,k)$ (p. 2). This
«makes it easier for training to concentrate on a small number of adverse regimes, which can amplify
non-stationarity from the market maker's perspective» (p. 2). The maker observes only inventory and
time, $o^{MM}_t=(H_t,t)$, over a window of $K=40$ steps: «The environment's full internal state
contains price, inventory, cash, and bilateral conditional intensities, but only inventory and time
are exposed to the policy» (p. 6). The proposed method ("Ours") encodes this window with a
one-layer LSTM of 32 units (p. 6). The intensity is thus a hidden state that the network has to
infer from the inventory path.

### 9. Training: PPO for both players, with a reward that penalises running and terminal inventory quadratically (pp. 6–7)

Reward (eq. 13): $r^{MM}_t=\Delta\Pi_t-\phi H_t^2-\mathbb 1_{\{t=T\}}\psi H_T^2$, with coefficients
$10^{-4}$ and $10^{-2}$ (the coefficient glyphs are lost in the PDF text layer; $\phi,\psi$ is the
mbt-gym convention [I]). The adversary receives $-R^{MM}$ (p. 6). Actor and critic: one hidden layer
of 64 units; learning rate $3\times10^{-4}$; discount 0.999; $T=1$, $\Delta t=0.005$ (200 steps);
800,000 environment steps; $\sigma=2$, initial price 100, inventory bound 50 (p. 7). Parameter
ranges (p. 6): $b\in[-5,5]$, $A\in[105,175]$, $k\in[1.125,1.875]$, $\kappa_H\in[35,60]$,
$\gamma_H\in[0,40]$, $\xi\in[0,1]$. The Fixed environment $(0,140,1.5,60,0,0)$ has Hawkes and impact
switched off.

### 10. ⭐ Robustness is evaluated by left-tail CVaR and a bootstrap test that higher returns are not bought with directional inventory (pp. 2–3, 7)

Because adversarial training targets bad episodes, «a left-tail statistic is more informative than a
metric such as the Sharpe ratio that mixes both tails» (p. 2). CVaR$_{10\%}$ is primary, CVaR$_{30\%}$
secondary. A one-sided bootstrap test ($B=20{,}000$, $\alpha=0.05$) compares absolute mean terminal
inventory between methods, $D_{obs}=T_{Ours}-T_{Ref}$ (eq. 14), under $H_0:D\le0$ (p. 7). Operational
definition: «a method is more robust when it has higher CVaR10% and there is no evidence that the
improvement is purchased by stronger terminal directional inventory bias» (p. 3).

### 11. ⭐ Plain ARLMM is not uniformly better than random-parameter training once Hawkes and impact are added (pp. 9–10)

On CVaR$_{10\%}$, «ARLMM outperforms Random in 9 of the 19 environments and is worse in the remaining
10» (p. 9). The failures cluster in Hawkes-dominated regimes (G6, G11, G19), in high-drift /
high-execution-pressure regimes (G10, G14, G16) and in liquidity-structure regimes (G1, G4, G5)
(pp. 9–10). For the Hawkes case: «risk is driven by clustered order flow and propagates across time
steps; a flattened history window has difficulty reliably distinguishing whether a burst is
beginning, expanding, or decaying» (p. 9). Example, G6 (Hawkes only, $\gamma_H=20$): CVaR$_{10\%}$
15.15 (ARLMM) vs 15.25 (Random) (Table 2, p. 8).

### 12. ⭐ The LSTM variant improves the left tail in all 19 test environments against ARLMM and 18 of 19 against Random (pp. 8, 10)

«Relative to ARLMM, Ours has higher CVaR10% in 19/19 environments. Relative to Random, Ours is better
in 18/19 environments» (p. 10). The exception, G3 (drift down), «contains neither Hawkes clustering
nor price impact, so sequential structure provides less additional information» (p. 10). Examples
(Table 2, p. 8): G1 standard, CVaR$_{10\%}$ 3.89 / 9.37 / 8.17 / 14.63 for Fixed / Random / ARLMM /
Ours; G6 Hawkes-only, 7.42 / 15.25 / 15.15 / 24.49. The bootstrap gives $D_{obs}=-1.30$ ($p=0.504$)
against Random and $D_{obs}=-0.38$ ($p=0.501$) against ARLMM (p. 10).

### 13. Gains are largest at medium-to-high self-excitation with low impact and shrink at high impact (p. 10)

On a 5×5 grid over $(\gamma_H,\xi)$, Ours beats ARLMM at all 25 points (Fig. 2). The largest gains
are near $(\gamma_H,\xi)=(20,0)$ and $(30,0.25)$; the smallest near $(20,1.0)$ (p. 10). Explanation:
under Hawkes clustering «liquidity can build up over several steps before receding, creating
cumulative inventory risk whose phase is observable from recent trajectories». At $\xi=1$ «a larger
fraction of loss comes from the immediate execution itself rather than multi-step risk propagation»
(p. 10).

### 14. Approximate Nash equilibrium is treated as evidence of training stability, not as the definition of robustness (p. 11)

«The true Nash gap in a multi-stage continuous-action game is difficult to compute exactly, so
empirical best-response analysis only provides an approximate equilibrium diagnostic» (p. 11). Both
ARLMM and Ours look approximately in equilibrium, yet ARLMM still deteriorates more in the left tail
out of sample (p. 11). No Nash-gap numbers are reported.

### 15. Future work: several competing makers, data-driven order books, multi-asset market making, convergence guarantees (p. 11)

«Future work can proceed in three directions: extending the single-market-maker model to
oligopolistic competition among multiple market makers; applying the framework to data-driven
limit-order-book environments and multi-asset market making; and developing stronger convergence
guarantees for multi-stage adversarial games with complex microstructure» (p. 11).

## Figures and tables

- Table 1 (p. 2): mechanisms in ARLMM vs this paper.
- Table 2 (p. 8): seven representative environments × four methods (terminal wealth, Sharpe,
  CVaR$_{10/30\%}$, terminal inventory). Table 3 (pp. 13–15): all 19 environments. The PDF text layer
  scrambles the columns; the values quoted above were checked against the RQ2 and bootstrap
  statements.
- Fig. 1 (p. 9): KDE of terminal wealth in G19. Fig. 2 (p. 10): CVaR$_{10\%}$ heatmaps over
  $(\gamma_H,\xi)$.

## What this source does not address

- **Any value function or HJB.** The multi-stage problem is solved only by model-free RL (PPO); the
  analytical part is a one-step game (eqs. 9–12). For a Hawkes market-making HJB see
  [[barzykin-2026-hawkes-driven-otc]], [[jusselin-2021-persistent-order-flow]],
  [[martin-2026-market-making-hawkes]].
- **Flow-driven or cross-excitation.** Only own-fill, same-side self-excitation (eq. 4); no
  cross-side term, no market orders that miss the maker. Cross-excitation in an RL setting:
  [[gasperov-2022-deep-reinforcement-learning]].
- **Several assets.** Single asset; multi-asset is future work (p. 11).
- **Comparison with an analytical policy.** No Avellaneda–Stoikov / GLFT benchmark and no regret
  against an exact solution; baselines are other RL training schemes only.
- **Estimation on data.** All environments are simulated with chosen parameters.

## Model card

| Field | Value |
|---|---|
| Assets | 1 |
| Kernel | exponential, in discrete time: Euler step $\lambda^\pm_{n+1}=\lambda^\pm_n+\kappa_H(A-\lambda^\pm_n)\Delta t+\gamma_H\Delta N^\pm_n$ (eq. 4) |
| Excitation | self only, per side (bid fills excite bid intensity, ask fills ask intensity); no cross-side, no cross-asset |
| Who excites the flow | the maker's own fills ($\Delta N^\pm$ of eq. 6) → fill-driven |
| Objective | game: expected $\Delta\Pi$ (single stage, eq. 9); RL: $\sum_t[\Delta\Pi_t-\phi H_t^2]-\psi H_T^2$ (eq. 13), risk-adjusted, not CARA; zero-sum against an adversary choosing $(b,A,k,\kappa_H,\gamma_H,\xi)$ |
| Solution method | RL: PPO, LSTM(32) over 40-step window of (inventory, time); single-stage game: closed-form best response (eq. 11), existence via Sion / Glicksberg |
| Benchmark | Fixed-environment RL, Random-environment RL, ARLMM (Spooner–Savani 2020) |
| Reported regret / gap numbers | none vs an optimum; CVaR$_{10\%}$ gains, e.g. G6: 24.49 (Ours) vs 15.15 (ARLMM), G1: 14.63 vs 8.17 (Table 2, p. 8); bootstrap $p\approx0.50$ (p. 10) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 2, 3, 5, 6, 8, 11, 12, 15.**

### What this focus needs beyond the Kernthesen

1. **No closure to evaluate.** The control problem is never written as an HJB; the only analytical
   object is the myopic one-stage game (Kernthese 5). The question "where does the closure hold or
   break" does not apply: the paper sidesteps it with PPO.
2. **Why the best response ignores the intensity, and what that shows [I].** In eq. (9) the intensity
   only multiplies each side's payoff, so the myopic quote is $1/k\mp b+\xi$ for any $\lambda$
   (Kernthese 6). In a fill-driven model, quotes should depend on $\lambda$ only through the
   continuation value, i.e. the gain from raising future intensity by $\gamma_H$ after a fill. The
   single-stage game drops this term (and the inventory penalty). That is exactly the term a
   value-function closure would have to carry, and its absence is why the one-step answer coincides
   with the Poisson risk-neutral quote.
3. **Effective branching ratio under fill-driven excitation [I].** Per unit time, a fill adds
   $\gamma_H$ to an intensity that decays at rate $\kappa_H$, but only a fraction $e^{-k\delta}$ of the
   intensity becomes fills. The effective branching ratio is therefore about
   $\gamma_He^{-k\delta}/\kappa_H$, which the quotes control. Example: G11 ($\gamma_H=40$,
   $\kappa_H=45$, $k=1.5$) has $\gamma_H/\kappa_H\approx0.89$, but at $\delta\approx1/k$ the effective
   ratio is about 0.33. The paper does not discuss stationarity.
4. **Multi-asset carry-over: none.** Single asset, two intensities with no cross-terms; multi-asset
   is listed as future work only (p. 11).

### Direct quotes (for the draft)

> "First, real order flow is often clustered and self-exciting, meaning that one trade can increase the short-run probability of subsequent trades; Hawkes processes provide a natural representation of this effect [7, 8]." (p. 2)

> "The single-stage game in Section 3 conditions on the current state (Hn, λ+n, λ−n), so the Hawkes extension enters the one-stage payoff through current conditional intensities." (p. 4)

> "In these environments, risk is driven by clustered order flow and propagates across time steps; a flattened history window has difficulty reliably distinguishing whether a burst is beginning, expanding, or decaying." (p. 9)

> "A static window representation primarily captures what happened recently, while the LSTM can encode how those events are evolving over time." (p. 10)

### Examples & illustrations (for later drafting)

- G6 vs G1 (Table 2, p. 8): switching on self-excitation ($\gamma_H=20$) raises every method's
  terminal wealth (e.g. Ours 27.0 → 39.2) because there are more fills. The Hawkes regime is
  "harder" only in its left tail relative to the training scheme, not in level.
- The heatmap reading (p. 10): a burst builds up "over several steps before receding". It gives a
  concrete picture of why a policy that does not see $\lambda$ needs memory. A policy that observes
  $\lambda$, as a closed-form feedback would, does not.

### Boundary of this focus

The paper gives neither a value function nor an equilibrium for the multi-stage game, so it cannot
inform the closed-form vs exact comparison. Its Hawkes flow is fill-driven, single-asset and
same-side only, the opposite of the project's flow-driven, cross-asset setting.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]] (base of ARLMM), [[glft-2013-model]] (cited only).
- Concepts: [[hawkes-process]], [[who-excites-the-flow]], [[branching-matrix]] (scalar, effective ratio inferred), [[regret]] (not reported).
- Related sources: [[wang-2024-arl-multi-action]] (cited, same ARL line), [[jusselin-2021-persistent-order-flow]] and [[fujii-2015-optimal-position-management]] (cited only), [[gasperov-2022-deep-reinforcement-learning]] (not cited; RL under Hawkes).
- Other works (not in library): Spooner & Savani 2020 (ARLMM, arXiv 2003.01820); Jerome et al. 2022 (mbt-gym); Cartea, Donnelly & Jaimungal 2017 (model uncertainty); Pinto et al. 2017 (RARL); Schulman et al. 2017 (PPO); Rockafellar & Uryasev 2000 (CVaR); Lalor & Swishchuk 2025.

## Connections

- Builds on: [[avellaneda-stoikov-model]] via ARLMM; [[hawkes-process]] (exponential, discrete-time, fill-driven).
- Cites: [[wang-2024-arl-multi-action]] (the other ARL + Hawkes paper; same mbt-gym-style intensity update), [[glft-2013-model]], [[jusselin-2021-persistent-order-flow]], [[fujii-2015-optimal-position-management]].
- Contrast with: [[gasperov-2022-deep-reinforcement-learning]]: also model-free RL under Hawkes, but there with multivariate cross-excitation of LOB events and no adversary.
- Contrast with: [[barzykin-2026-hawkes-driven-otc]]: Hawkes market making solved through the value function. Here the value function is never formed.
