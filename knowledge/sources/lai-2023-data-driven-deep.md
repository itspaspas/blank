---
title: "Lai, Gao & Li 2023 — A Data-Driven Deep Learning Approach for Options Market Making"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: lai-2023-data-driven-deep
depth: standard
tags: [market-making, options, hawkes, power-law-kernel, deep-learning, policy-gradient, cara, multi-instrument, empirical, cboe]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«a Hawkes process with a time-varying baseline intensity and the power law kernel provides a good fit to the data of market order flows for stock options» (p. 777); kernel eq. (3), Table 1 KS pass rates (p. 782)."
  - target: intensity-forecast
    type: supports
    confidence: extracted
    because: "Feature ExpN = E[N_{k,k+1}|F_k] via the Volterra equation (16) and eq. (15) (p. 785); «utilizing the Hawkes process intensity or the expected number of market order arrivals ... as an additional input feature can boost the performance» (p. 777)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "«We follow Avellaneda and Stoikov (2008) and assume that the size Q of a market order follows the power law distribution»; execution probability Pr(δp > ε) = e^{−κε}, eq. (13) (pp. 783–784)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Market-order paths are simulated from the fitted Hawkes model before and independently of the quotes (Sec. 3.3 step 1, p. 786); fills are a Bernoulli thinning of exogenous market orders (eq. 14, p. 784) — flow-driven, the maker cannot excite the flow. Not discussed by the authors."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "«Guéant et al. (2013) further introduced a bound on the inventory into the framework» (p. 777)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "Cartea et al. (2014) is cited in Remark 7 as a way «to introduce dependence» between option prices and market orders (p. 787); Cartea et al. 2018b (SIAM Review) in the introduction (p. 777)."
  - target: kumar-2024-deep-hawkes-process
    type: cites
    confidence: extracted
    because: "«Kumar (2021) studied market making in a limit order book model with event arrivals modeled by deep Hawkes processes» (p. 777); reference list cites arXiv:2109.15110 (p. 797)."
---

# A Data-Driven Deep Learning Approach for Options Market Making

## Bibliographic Details

Lai, Qianhui; Gao, Xuefeng; Li, Lingfei. 2023. "A data-driven deep learning approach for options
market making." *Quantitative Finance* 23(5): 777–797. DOI 10.1080/14697688.2023.2186257.
Received 11 Apr 2022, accepted 24 Feb 2023, published online 16 Mar 2023. Affiliations: Qingdao
University; The Chinese University of Hong Kong. Funding: HK RGC GRF 14206020.

**Read:** published journal version (library PDF, Taylor & Francis). Page numbers on this page are
the **journal** page numbers (PDF page = journal page − 775; PDF p. 1 is the T&F cover sheet). The
paper is based on Lai's CUHK PhD thesis (Lai 2021, cited p. 787 fn.).

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\epsilon^b_k,\epsilon^a_k$ | quote distance to mid at decision time $t_k$ | $\delta^b,\delta^a$ |
| $\delta$ (eq. 3), $\delta p$ (eq. 13) | power-law kernel offset; depth of the farthest limit order hit by a market order | ⚠ not a quote; clashes with $\delta^{b,a}$ |
| $\mu(t)$, $\mu_m$ | deterministic piecewise baseline (eqs. 5–6) | $\mu$ (time-varying) |
| $g(t)=\alpha/(t+\delta)^\beta$ | power-law Hawkes kernel (eq. 3); exponential alternative $\alpha e^{-\beta t}$ (eq. 4) | kernel; ⚠ $\beta$ is a power-law **exponent**, not a decay rate, in eq. (3) |
| $\phi_{j,i}$ | nonparametric kernel of type $j$ on type $i$, $i\in\{0=\text{buy},1=\text{sell}\}$ (eq. 1) | entries of the kernel matrix behind $K$ |
| $\kappa$ | exponential decay of fill probability in depth (eq. 13), set to 10 | GLFT $k$ |
| $\gamma$ | CARA risk aversion, $U(y)=(1-e^{-\gamma y})/\gamma$ | $\gamma$ |
| $q^o_k$, $q^s_k$, $x_k$ | option inventory, stock (hedge) inventory, cash | $q_t$, —, $X_t$ |
| $K$ (source) | **number of decision periods** | ⚠ clashes with project $K$ (branching matrix) |
| $m$ (Sec. 5) | number of options in the portfolio | $d$ |
| $\psi^i_k$, $\nu^i_k$, $h^i_k$ | Volterra resolvent-type solution (eq. 16), past-driven intensity, kernel (Sec. 3.2) | ingredients of $m_t(u)$ |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 777 |
| ✓ F1 | 1 Introduction (MM literature, options MM: Stoikov–Sağlam, El Aoud–Abergel, Baldacci et al. ×2; contributions (1)–(3)) | 777–779 |
| ✓ F1 | 2 Empirical analysis of market orders for stock options (CBOE 2019, AAPL/BAC, Lee–Ready signing, 8 groups) | 779 |
| ✓ F1 | 2.1 Self- and cross-excitation of market orders (nonparametric Bacry–Jaisson–Muzy, Fig. 3, Remark 1) | 779–780 |
| ✓ F1 | 2.2 Estimation of parametric Hawkes processes (eqs. 2–6, KS test, Tables 1–2) | 780–783 |
| ✓ F1 | 3 Market making for a single option (eqs. 7–12, CARA) | 783 |
| ✓ F1 | 3.1 Market orders and execution of limit orders (eqs. 13–14, Remark 2) | 783–784 |
| ✓ F1 | 3.2 Neural network approximation (Han–E; features Intensity / ExpN, eqs. 15–16, Remarks 3–4) | 784–785 |
| ✓ F1 | 3.3 The deep learning algorithm (loss, Adam, relaxed Bernoulli, Remarks 5–6) | 786 |
| ✓ F1 | 4 Empirical results for single option market making (Table 3: six strategies) | 786 |
| ✓ F1 | 4.1 Experiment design (rolling monthly train/test, BS model, κ = 10, Remark 7) | 787 |
| ✓ F1 | 4.2 Convergence; 4.3 Findings (Tables 4–11, Figs. 5–8, Remark 8) | 788–794 |
| ✓ F1 | 5 Market making for multiple options with constraints; 5.1 Formulation; 5.2 Empirical results (Table 12, Fig. 9) | 794–795 |
| ✓ F1 | 6 Conclusion | 796 |
| — | Acknowledgments, Funding, References | 796–797 |

## Kernthesen

### 1. ⭐ Option market orders are strongly self-exciting but only weakly cross-exciting between buy and sell (pp. 777, 779–780, 796)

A nonparametric bivariate Hawkes estimate (Bacry, Jaisson & Muzy 2016) on pooled 2019 CBOE trades
(AAPL calls, moneyness (0.99, 1.02], TTM ≤ 10 d; BAC calls, (0.98, 1.02], TTM ≤ 5 d) shows
«pronounced self-excitation in both buy and sell orders, and the effect is stronger for AAPL ...
However, cross-excitation between buy and sell orders is insignificant compared with their
self-excitation as seen from the magnitude of the estimated kernels $\phi_{0,1}$ and $\phi_{1,0}$»
(p. 779, Fig. 3 p. 781). No numerical cross-kernel norms or test statistics are reported; the
judgement is visual from Fig. 3. The estimate assumes a constant baseline (Remark 1, p. 779–780),
which the authors argue does not overturn the conclusion.

### 2. ⭐ Hence cross-excitation is set to zero: buy and sell are two independent univariate Hawkes processes per contract (p. 780)

«As cross-excitation is insignificant, we simply assume that there is no cross-excitation in our
framework» (p. 780). Buy intensity (eq. 2) $\lambda(t)=\mu(t)+\sum_{t_v<t}g(t-t_v)$; sell has «the
same form but with different values for the parameters» (p. 781). No excitation across contracts
(strikes, maturities) or between option and underlying is ever estimated.

### 3. ⭐⭐ A power-law kernel with time-varying baseline fits; exponential Hawkes is mixed and Poisson fails (pp. 781–782, Table 1)

Kernels (3) $g=\alpha/(t-t_v+\delta)^\beta$ and (4) $g=\alpha e^{-\beta(t-t_v)}$; baseline piecewise
linear on six hourly intervals for AAPL (eq. 5, U-shape) and piecewise constant on three intervals
for BAC (eq. 6, L-shape). Daily MLE (Omi's Python package) and a KS test on the time-changed
inter-arrivals (Bowsher 2007) give pass rates (Table 1, p. 782): AAPL buy 91.4% / 36.3% / 0.094%,
AAPL sell 94.6% / 41.9% / 0.282%, BAC buy 96.3% / 83.9% / 13.7%, BAC sell 97.0% / 85.5% / 15.5%
(power-law / exponential / Poisson). «Clearly the Hawkes model with the power law kernel is the
best one in all the cases» (p. 782). The authors read this as evidence of «the non-Markov nature of
the options order data, which the existing papers fail to account for» (p. 778).

### 4. Fitted parameters: shorter maturity → larger baseline and longer memory; BAC memory is shorter (pp. 782–783, Table 2)

Averages over 2019 trading days (Table 2, p. 782): AAPL $\alpha\approx0.017$–$0.054$,
$\beta\approx1.07$–$1.74$, $\delta\approx0.0003$–$0.052$; BAC $\alpha\approx0.047$–$0.102$,
$\beta\approx1.67$–$2.22$, $\delta\approx0.027$–$0.086$. «self-excitation persists longer for
options with a shorter maturity as their estimated β is smaller. Comparing AAPL and BAC options,
self-excitation is less persistent in BAC options with a larger estimated β» (p. 783). No
branching ratio, time unit or stationarity check is reported (see Contested below).

### 5. The control problem is discrete-time CARA utility of one-day P&L with delta hedging on the grid (p. 783)

The maker posts one unit bid and one unit ask at each $t_k$ (unit size following Stoikov–Sağlam and
El Aoud–Abergel), fills can occur any time in $[t_k,t_{k+1})$ (p. 783). Inventory (7), delta hedge
$q^s_k=-q^o_k\Delta_k$ (8), cash (9), wealth (10)–(11). Objective (12):
$\max_{\epsilon^a_k,\epsilon^b_k>0}\mathbb E[U(W_K-W_0)]$, $U(y)=(1-e^{-\gamma y})/\gamma$, $\gamma\ge0$;
for $\gamma>0$ this equals CARA in terminal wealth (p. 783). The stock is assumed perfectly liquid.

### 6. ⭐ Fills are a Bernoulli thinning of the *exogenous* market-order count in each interval (p. 784)

With AS-type market-order sizes ($f_Q(x)\propto x^{-1-\nu}$) and $\delta p\propto\ln Q$,
$\Pr(\delta p>\epsilon)=e^{-\kappa\epsilon}$ (13), and
$\Pr(Q(\epsilon_j)=1\mid N^{mkt}_{j,j+1})=1-(1-e^{-\kappa\epsilon_j})^{N^{mkt}_{j,j+1}}$ (14),
assuming a resilient book that «restores its previous shape after a market order» — so (14) «is
only an approximation of the true execution probability» (p. 784). The quote changes only the
conversion probability, never the market-order process.

### 7. ⭐⭐ The policy is a stack of 2K feed-forward networks trained by direct policy optimisation (Han–E 2016), not by dynamic programming (pp. 784, 786)

«we apply the deep learning approach developed in Han and Weinan (2016), which turns a dynamic
control problem into a stochastic optimization problem» (p. 784): one FNN per side per decision
time (2 hidden layers × 64, ReLU, sigmoid output = quotes within $1 of mid). Loss
$\ell(\theta)=-\frac1N\sum_jU(W^j_K(\theta)-W_0)$ minimised by Adam on mini-batches of 128 (p. 786);
the binary fill is replaced by a relaxed Bernoulli to restore differentiability (Remark 6, p. 786).
Remark 4 (p. 785) calls this «a special deep reinforcement learning algorithm» / «deep empirical
risk minimization» (Reppen–Soner).

### 8. ⭐⭐ Value-based RL is rejected because the power-law flow is non-Markov; the BSDE route is judged impractical (pp. 778, 785)

«as the Hawkes process for option market order arrivals is non-Markovian in light of our empirical
results, the value function at a given time depends on the whole path of market orders up to that
time, making it difficult to apply value-based reinforcement learning algorithms» (p. 785).
Confortola–Fuhrman BSDEs represent such value functions, «However, it is not clear how to solve
such BSDEs and also deal with various contraints for market making» (p. 778). An RNN feature
extractor is also rejected as over-parameterised relative to the parametric Hawkes fit (p. 785).

### 9. ⭐ Hawkes information enters only as one hand-crafted feature per side: current intensity, or the expected count in the next interval via a Volterra equation (pp. 784–785)

Inputs: $(S_k,C_k,x_k,q^o_k,q^s_k,f_{\cdot,k})$ (p. 784). (1) *Intensity*: $f=\lambda^i(t_k)$. (2) *ExpN*:
$f=\mathbb E[N^i_{k,k+1}\mid\mathcal F^i_k]$, computed by Gao–Zhou–Zhu (2018) Prop. 5 as
$\int_0^{t_{k+1}-t_k}\nu^i_k(t_{k+1}-t_k-u)\psi^i_k(u)\,du$ (15) with $\psi^i_k(u)=1+\int_0^uh^i_k(u-s)\psi^i_k(s)\,ds$
(16), solved by finite differences on 2000 points and Gauss–Legendre quadrature (p. 785). Each side's
feature uses only its own side's history ($\mathcal F^i_k$).

### 10. ⭐⭐ Training on Hawkes rather than Poisson paths improves out-of-sample results significantly; a Poisson-trained network loses even to a constant quote (pp. 789, 791, Tables 4–8)

Rolling design: fit on month $n$, simulate ~100,000 daily paths (stock under Black–Scholes; market
orders from every KS-accepted daily Hawkes fit, so parameter uncertainty is sampled), test on real
CBOE data of month $n+1$, 11 test months, ~110,000 realised P&Ls per strategy, common random
numbers for fills (pp. 787). «for all option groups, the average daily profit/utility of NoF is
greater than the one of Poisson at the 1% significance level» (p. 789). «The Poisson strategy ... is
inferior to Constant in every case» (p. 791). Example, AAPL (1, 1.01], TTM 0–5, $\gamma=0$ (Table 4,
p. 788): LIF 55.38, ExpN 52.63, Intensity 52.55, NoF 52.26, Constant 51.43, Poisson 51.23.

### 11. Hawkes features add a further, smaller, statistically significant gain; ExpN avoids the quote spikes of Intensity (pp. 789, 791)

«Except for one option group of AAPL options for the risk-neutral agent, Intensity and ExpN
demonstrate improvement over NoF at the 1% significance level» (p. 789); the gain is larger for
TTM ≤ 5 d. ExpN beats Intensity by a small margin for BAC, neither dominates for AAPL; the
Intensity strategy «can generate occasional large spikes in the quotes caused by surges in the
Hawkes intensity», ExpN does not (p. 791). Quotes are U-/L-shaped intraday, matching the order
profiles (Figs. 6–7, p. 793).

### 12. ⭐ The benchmark ladder: an unattainable look-into-future bound (LIF) and a grid-optimised constant quote; no optimum is computed (pp. 786, 791)

Six strategies (Table 3, p. 786): LIF (Hawkes-trained, given the realised next-interval order count —
«an unattainable upper bound for the adapted deep learning strategies»), ExpN, Intensity, NoF,
Poisson (trained on Poisson paths), Constant (fixed $\epsilon^a,\epsilon^b$, grid search up to 100
ticks on Hawkes paths). The authors state that «the impractical upper bound LIF only outperforms
Constant by about 4.3% ∼ 5.6% for the risk-neutral agent and about 0.9% ∼ 2.2% for the risk-averse
agent» and that ExpN/Intensity are «quite close to LIF» in many cases (p. 791).

### 13. Quotes widen with the expected number of arrivals; no end-of-day tightening without constraints (p. 791)

Hawkes-trained quotes stay above $0.1 = 1/\kappa$, the one-arrival optimum, because more than one
arrival is expected per interval; the Poisson-trained net can quote inside it. «we do not observe
that the optimal bid or ask quote moves closer to the mid-price towards the end of the day. This is
because there is no constraint on the option inventory in this setting» (p. 791). P&L distributions
are positively skewed and heavy-tailed (Tables 9–11, pp. 791–792).

### 14. ⭐ Multi-option extension: m options on one underlying, 2m networks per decision time, Greeks and inventory constraints as quadratic penalties (pp. 794–795)

$m$ options on the same stock, one aggregate delta hedge $q^s_k=-\sum_lq^o_{k,l}\Delta_{k,l}$ (p. 794).
Terminal constraints $|\Gamma_K|\le M_\Gamma$, $|V_K|\le M_V$, $|q^o_{K,l}|\le M_{Q,l}$ become penalties
$P=\max\{0,x-y\}^2+\min\{0,x+y\}^2$ with $\eta_1=\eta_2=\eta_3=2000$ (p. 795). Experiment: six AAPL
calls (one per group), risk-neutral, Intensity feature, «The market orders for each option are
generated by the estimated Hawkes model for that option» (p. 795) — i.e. independent across
contracts.

### 15. Constraints cut terminal Greeks and inventory sharply at modest P&L cost (p. 795, Table 12)

PnL mean 142.11 / 140.05 / 124.99 and stdev 52.68 / 53.66 / 50.88 for no constraint / $M_\Gamma=M_V=5,M_Q=20$
/ $M_\Gamma=M_V=3,M_Q=10$; mean $|\Gamma_K|$ 1.37 → 0.71 → 0.33, mean $|V_K|$ 1.79 → 0.67 → 0.34, mean
$|q^o_{K,l}|$ 9.58 → 5.08 → 2.88; violation rates ≤ 1.64%, zero for vega (Table 12, p. 795). Under
constraints the ask moves toward mid near the close to shed inventory (Fig. 9, pp. 794–795).

### 16. Self-declared limitations: joint price–flow modelling, trading costs, frequency (pp. 787, 792–794)

Option prices and market orders are simulated independently; «It would be more realistic to model
the option prices and market orders jointly» and profits are expected to be lower if so (Remark 7,
p. 787). Quotes are set at 1-min (AAPL) / 5-min (BAC) frequency because CBOE data are 1-min; the
mid-price within an interval is unobserved (Remark 2, p. 784). Trading fees/rebates are omitted
(Remark 8, pp. 792–794). Heston was tried and was worse out of sample than Black–Scholes (fn., p. 787).

## Figures and tables

- Fig. 1 (p. 780): average daily market orders by moneyness and TTM. Fig. 2 (p. 781): one-minute
  order counts, eight groups. **Fig. 3 (p. 781): nonparametric buy/sell self- and cross-kernels,
  AAPL and BAC** — the only evidence for "insignificant cross-excitation".
- Table 1 (p. 782): KS pass rates. Table 2 (p. 782): average power-law Hawkes parameters.
- Table 3 (p. 786): six strategies. Tables 4–5 (pp. 788–789): average daily profit/utility.
  Tables 6–8 (pp. 789–790): 99% CIs of pairwise differences. Tables 9–11 (pp. 791–792): P&L moments.
- Figs. 6–8 (pp. 793–794): intraday quotes and inventories. Fig. 9, Table 12 (pp. 794–795): portfolio
  with constraints.

No figures extracted to `knowledge/assets/` in this pass (write scope limited to this page).

## What this source does not address

- **Cross-asset (cross-contract) excitation.** Never estimated or simulated; contracts are fitted
  and simulated separately (pp. 782, 795). Only buy↔sell cross-excitation *within* a contract is
  examined, and dismissed (p. 780).
- **Any closed form, HJB or exact benchmark.** No value function is written; there is no
  comparison with an optimal policy, a GLFT/BEGV approximation or a regret number. LIF is a
  non-adapted bound, not an optimum (p. 786).
- **Fill-driven excitation / market impact of the maker on flow.** Market orders are exogenous
  (Sec. 3.3, p. 786).
- **Continuous-time quoting.** Decisions on a 1- or 5-minute grid.
- **Joint dynamics of option price, underlying and order flow** (Remark 7, p. 787).
- **Branching ratios, stationarity, time units** of the fitted kernels.

## Model card

- **Assets:** one option per problem (Secs. 3–4; 8 contract groups solved separately: 6 AAPL, 2 BAC);
  Sec. 5: **m = 6** AAPL calls on one underlying, plus the stock as a delta hedge (not quoted).
- **Kernel:** power-law $\alpha/(t+\delta)^\beta$ with piecewise time-varying baseline (exponential
  and Poisson fitted for comparison only).
- **Excitation:** self only (buy→buy, sell→sell); cross-side estimated nonparametrically and set to
  zero; **no cross-asset**.
- **Who excites the flow:** all market orders, exogenous to the maker (flow-driven); fills are a
  quote-dependent thinning.
- **Objective:** CARA expected utility of one-day P&L, $\gamma\in\{0,0.05\}$; Sec. 5 adds quadratic
  penalties on terminal $\Gamma$, vega, inventory.
- **Solution method:** direct policy optimisation (Han–E deep "RL"/empirical risk minimisation):
  2K (resp. 2mK) FNNs, Adam, relaxed Bernoulli fills, trained on simulated paths.
- **Benchmark:** LIF (non-adapted upper bound), Constant (grid-optimised), Poisson-trained net, NoF;
  out-of-sample on real CBOE data.
- **Reported numbers:** average daily profit/utility with 99% CIs (Tables 4–8); e.g. ExpN − Poisson
  = 1.74–1.76 (AAPL group (a), $\gamma=0$, Table 6); no regret against an optimum (n/a — no optimum
  computed).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 2, 3, 6, 7, 8, 9, 10, 12, 14.**

### What this focus needs beyond the Kernthesen

1. **Closure status: none attempted.** The paper never writes an HJB. Its explicit reason for not
   using a value function is the non-Markov power-law flow (p. 785, Kernthese 8). It does not
   consider a sum-of-exponentials [[markov-lift]], although its own exponential fit (eq. 4) would
   give a one-factor lift per side; the poor exponential KS pass rate for AAPL (36–42%, Table 1)
   is the implicit argument against it.
2. **Where the Volterra machinery appears.** The ExpN feature (15)–(16) is exactly a one-step
   [[intensity-forecast]]: the expected count over $[t_k,t_{k+1})$ from a renewal-type Volterra
   equation for the power-law kernel. This is the same object Barzykin's Volterra–Riccati scheme
   feeds into a Riccati system ([[volterra-riccati]], [[barzykin-2026-hawkes-driven-otc]]), but
   here it is fed into a neural network, over a single interval only, not the whole forecast curve
   $m_t(u)$. *Inference:* ExpN's empirical advantage over NoF is evidence that the
   forecast-not-intensity input is the useful summary under power-law flow — the premise of the
   frozen-forecast closure.
3. **Who excites.** Flow-driven by construction ([[who-excites-the-flow]]): market-order paths are
   simulated before the quotes are applied (Sec. 3.3, step 1, p. 786). This is the convention under
   which the quadratic (BEGV) route survives in reduced form (see [[problem-anatomy]] §3a) — but the
   paper does not use it.
4. **Multi-asset / cross-asset.** The number of quoted instruments is 1 (Secs. 3–4) or 6 (Sec. 5),
   all on one underlying, coupled only through the shared delta hedge, the portfolio Γ/vega
   penalties and the common stock path. Cross-contract excitation is neither estimated nor modelled;
   each contract's order flow is an independent univariate Hawkes per side (p. 795). The only
   cross-excitation evidence (buy↔sell within a pooled contract set) is a visual nonparametric
   judgement with no reported values (Fig. 3, p. 781). *Inference:* pooling contracts across
   moneyness/TTM in the nonparametric fit (p. 779) mixes events from different contracts into one
   buy and one sell stream, so any cross-contract excitation would be absorbed into "self"-
   excitation of the pooled side — the data could not separate them.
5. **What is compared with what.** Learned policy vs LIF bound, constant quote, Poisson-trained net,
   no-feature net. No closed form and no exact solution — so none of the three legs of the project's
   comparison (closed form / exact / RL) is benchmarked against another; the paper is a "RL with
   Hawkes-vs-Poisson training data" study.

### Direct quotes (for the draft)

> "As cross-excitation is insignificant, we simply assume that there is no cross-excitation in our framework." (p. 780)

> "However, as the Hawkes process for option market order arrivals is non-Markovian in light of our empirical results, the value function at a given time depends on the whole path of market orders up to that time, making it difficult to apply value-based reinforcement learning algorithms." (p. 785)

> "We find that using the more realistic Hawkes model improves the out-of-sample performance significantly." (p. 777)

> "The market orders for each option are generated by the estimated Hawkes model for that option and we use the Hawkes intensity as an additional input to the neural networks." (p. 795)

### Examples & illustrations (for later drafting)

- Table 1 (p. 782): KS pass rates power-law 91–97% vs exponential 36–86% vs Poisson 0.09–15.5% — a
  compact empirical case that exponential (Markov) Hawkes is not enough for option flow.
- Table 4 (p. 788), AAPL (1, 1.01] TTM 0–5, risk-neutral: LIF 55.38 > ExpN 52.63 > NoF 52.26 >
  Constant 51.43 > Poisson 51.23 — the ordering of model realism vs. feature information.
- Figs. 6–7 (p. 793): Hawkes-trained quotes widen at the open (U-shape AAPL, L-shape BAC), Poisson
  quotes are flat.

### Boundary of this focus

Everything on this page about closure (HJB, Riccati, lift) and about cross-asset excitation is the
project's reading; the paper addresses neither. Its contribution to the research question is
empirical (power-law, weak cross-side excitation in option flow) and methodological (direct
policy optimisation with a Volterra forecast feature), not a closed form.

## Contested / inconsistent in the source

- **Stated LIF-over-Constant ranges do not reproduce from Tables 4–5.** Computed from the tables
  (this page, not the authors): LIF/Constant − 1 = 5.0–8.2% for $\gamma=0$ (AAPL 4.98–8.21%, BAC
  5.38–6.03%) and 1.4–4.6% for $\gamma=0.05$, vs. the text's «4.3% ∼ 5.6%» and «0.9% ∼ 2.2%»
  (p. 791). The text's ranges are closer to the ExpN-to-LIF gap (4.1–5.4%, resp. 0.85–3.7%).
- **"Quite close to LIF" is generous.** Computed from Tables 4–5: ExpN closes only 9–49% of the
  Constant→LIF gap (9–36% risk-neutral).
- **Implied branching ratios are not checked.** Plugging the *averaged* Table 2 parameters into
  $\|g\|_1=\alpha\delta^{1-\beta}/(\beta-1)$ gives values from 0.28 to 7.7, several above 1 (e.g.
  AAPL (1.01,1.02] 6–10 sell). Averages of nonlinear parameters are not the average branching ratio
  and daily fits on a finite day need not be stationary, so this is a caution, not a refutation —
  but the paper reports no stability diagnostic.
- **Cross-excitation evidence is qualitative only** (Fig. 3) and estimated with a constant baseline
  that the authors themselves say is misspecified (Remark 1).
- Minor: p. 784 gives the input vector for "the FNN of $\epsilon^a_k$" twice (one should be $\epsilon^b_k$).

## Mentioned entities

- Models: [[avellaneda-stoikov-model]] (fill-probability and order-size assumptions), [[glft-2013-model]], [[cartea-jaimungal-ricci-model]]
- Concepts: [[hawkes-process]], [[intensity-forecast]], [[who-excites-the-flow]], [[markov-lift]], [[volterra-riccati]]
- Other works (bibkeys): [[kumar-2024-deep-hawkes-process]] (cited as Kumar 2021, p. 777); `bacry-2016-estimation-slowly-decreasing` (nonparametric kernel estimator); `bacry-2015-hawkes-processes-finance`; `bergault-2020-size-matters-otc` (Bergault–Guéant, *Math. Finance* 2021; not BEGV); `gueant-2019-deep-reinforcement-learning` (Guéant–Manziuk); `choi-2021-synchronised-order-arrivals`; `gasperov-2022-deep-reinforcement-learning` (DRL in a multivariate exponential-Hawkes LOB). Not in the library: Gao, Zhou & Zhu 2018 (*Quant. Finance*, transform analysis for Hawkes; Prop. 5 behind eq. 15), Han & E 2016, Stoikov & Sağlam 2009, El Aoud & Abergel 2015, Baldacci, Bergault & Guéant 2021 (options MM), Baldacci, Derchu & Manziuk 2020, Confortola & Fuhrman 2013, Reppen & Soner 2022.

## Connections

- Builds on: [[avellaneda-stoikov-model]] (exponential fill probability per market order), [[hawkes-process]] (power-law, time-varying baseline).
- Supports: [[intensity-forecast]] — an expected-count forecast is a better control input than the raw intensity (p. 791).
- Cites: [[kumar-2024-deep-hawkes-process]] (deep Hawkes LOB market making), [[glft-2013-model]], [[cartea-jaimungal-ricci-model]].
- Compare (not cited): [[barzykin-2026-hawkes-driven-otc]] (same Volterra forecast object, fed into a Riccati system instead of a network); [[martin-2026-market-making-hawkes]] and [[acero-2026-hawkes-structured-networks]] (learned solutions with an exact or lifted benchmark, which this paper lacks).
