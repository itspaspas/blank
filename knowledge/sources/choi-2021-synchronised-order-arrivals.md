---
title: "Choi, Jang, Lee & Zheng 2021 — Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: choi-2021-synchronised-order-arrivals
depth: standard
tags: [market-making, hawkes, mutually-exciting, synchronising-factor, single-asset, limit-order-book, deep-galerkin, neural-pde, empirical-calibration, us-equities]
relations:
  - target: cartea-2014-buy-low-sell
    type: builds-on
    confidence: extracted
    because: "Model and HJB follow CJR: fill probability as in «Avellaneda and Stoikov (2008) and Cartea et al. (2014)» (p. 8); Lemma 1 proof «Similar to the scheme of Cartea et al. (2014)» (p. 37); Appendix C benchmarks against «the asymptotic formula of Cartea et al. (2014), when kappa = kappa_c = 0» (p. 42)."
  - target: cartea-jaimungal-ricci-model
    type: builds-on
    confidence: extracted
    because: "Eq. (3) is CJR (2.2) with rho = 1, separate baselines theta^+-, and an added drift coupling kappa*lambda^-+ (p. 8); eq. (4) is CJR (3.1) with an added coupling kappa_c (p. 9); «This is a one-way effect because market orders cause jumps in subsequent limit orders» (p. 9)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«we propose a model for market order arrivals and limit order book dynamics based on the Hawkes process with the addition of a novel variable, referred to as a synchronising factor» (p. 3)."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Lemma 1: «The mean future rates ... are bounded for all u >= t if and only if (1 - kappa)beta > eta + nu» (p. 37); Table 2 reports the ratio (1 - kappa)beta/(eta + nu) per stock, e.g. 2.4274 overall in 2018 (p. 15) — the reciprocal of the spectral radius (reader's mapping)."
  - target: intensity-forecast
    type: builds-on
    confidence: extracted
    because: "(A.2), p. 37: m_t(u) = e^{-D(u-t)}[lambda_t - D^{-1}pi] + D^{-1}pi; the depth forecast n_t(u) in Remark 2, (A.3)-(A.4), p. 38, is driven by m_t."
  - target: who-excites-the-flow
    type: supports
    confidence: extracted
    because: "Flow-driven: «Let the counting processes M^+_t and M^-_t with intensities lambda^+_t and lambda^-_t denote the arrival of other participants' buy and sell market orders» (p. 7); the maker's fills are Bernoulli thinnings of M with probability h(delta, c), eqs. (1)-(2), p. 7."
  - target: markov-lift
    type: mentions
    confidence: inferred
    because: "No lift is needed or discussed: the kernel is the matrix exponential e^{-Bt}J of a 2x2 linear system, so (lambda^-, lambda^+, c^-, c^+) are themselves Markov states of HJB (7), p. 10."
  - target: regret
    type: mentions
    confidence: inferred
    because: "No regret against an exact optimum: comparisons are PnL statistics of DNN-optimal vs constant/linear heuristics (Table 3, p. 24), vs misspecified-synchrony strategies (Tables 4, 7, pp. 27, 30) and vs the CJR asymptotic formula at kappa = 0 (Table C.11, p. 46)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "«Gueant et al. (2013) study the same problem as Avellaneda and Stoikov (2008) by adding inventory volume constraints and then approximate the optimal control with asymptotic limits over an infinite time horizon» (p. 5)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«Avellaneda and Stoikov (2008) propose a market-making model in an order book by employing a diffusion process for a mid-price and a Poisson process for executed limit orders» (p. 5)."
  - target: cartea-2018-algorithmic-trading-stochastic
    type: mentions
    confidence: inferred
    because: "Choi et al. cite only the 2014 SIFIN version of CJR (reference list, p. 33); the 2018 SIAM Review reprint has the same model and formulas."
based_on: preprint
---

# Optimal Market-Making Strategies under Synchronised Order Arrivals with Deep Neural Networks

## Bibliographic Details

Choi, So Eun; Jang, Hyun Jin; Lee, Kyungsub; Zheng, Harry. 2021. "Optimal Market-Making Strategies
under Synchronised Order Arrivals with Deep Neural Networks." *Journal of Economic Dynamics and
Control* 125: 104098. DOI 10.1016/j.jedc.2021.104098. Affiliations: KAIST, UNIST (corresponding
author Jang), Yeungnam University, Imperial College London (p. 1).

**Read: author preprint ("Preprint submitted to Elsevier", dated 25 January 2021, p. 1), not the
JEDC typeset version; page, equation, table and figure numbers follow that preprint (46 pp.).**
The library copy at `library/pdf/choi-2021-synchronised-order-arrivals.pdf` is this preprint
(`library/references.bib` note). The acknowledgements thank reviewers for comments on «the previous
three versions» (p. 32), so this is probably the accepted manuscript; whether the printed version
differs was not checked.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $S_t$, $\sigma$; $dS_t=\sigma S_tdW_t$ | midprice, geometric BM, no drift (p. 7) | $S_t,\sigma$ |
| $\delta^-_t,\delta^+_t$ | depth of buy LO at $S-\delta^-$, sell LO at $S+\delta^+$ | $\delta^b,\delta^a$ |
| $M^\pm_t$, $\lambda^\pm_t$ | other participants' market buy (+) / sell (−) orders and their intensities | $\lambda_t$; ⚠ "+" = buy MO = ask-side fill (as in CJR) |
| $\theta^\pm$ | constant mean levels of $\lambda^\pm$ | baseline $\mu$ (but the stationary mean is $D^{-1}\pi$, not $\theta$) |
| $\beta$ | mean-reversion speed of $\lambda$ | decay $\beta$ |
| $\eta$, $\nu$ | self- and cross-side jump of $\lambda$ per MO | entries of the jump matrix $J=\begin{pmatrix}\eta&\nu\\\nu&\eta\end{pmatrix}$ |
| $\kappa$ | **synchronising factor**: drift coupling $\beta\kappa\lambda^\pm$ in $d\lambda^\mp$ (3) | off-diagonal of a non-diagonal decay matrix $B=\beta\begin{pmatrix}1&-\kappa\\-\kappa&1\end{pmatrix}$ (reader's mapping) |
| $D$ (Lemma 1) | drift matrix $\begin{pmatrix}\beta-\eta&-\kappa\beta-\nu\\-\kappa\beta-\nu&\beta-\eta\end{pmatrix}$ of $m_t(u)$ | $=B-J$; ⚠ not the project's $D=\mathrm{diag}(\beta)$ |
| $c^\pm_t$; $\alpha,\xi,\kappa_c,\eta_c,\nu_c$ | LOB depth (fill-probability scale); its long-run level, speed, synchronising factor, jumps (4) | GLFT $k$ made stochastic (CJR's $\kappa^\pm$); ⚠ $\alpha$ is not CJR's short-term alpha |
| $h(\delta,c)=e^{-\delta c}$ | fill probability given an MO (p. 8) | $f(\delta)$ with $k=c$ |
| $\phi$ | terminal liquidation cost $q_T(S_T-\phi q_T)$ (5) | ⚠ CJR's $\phi$ is the running penalty |
| $\psi$ | running inventory penalty $\psi\int q^2$ (5) | CJR's $\phi$; plays $\tfrac12\gamma\sigma^2$ |
| $V$, $g$; $\Delta^\pm_{q,\lambda,c}$, $\Delta^\pm_{\lambda,c}$ | value function, $V=x+qs+g$ (9); shift operators (p. 10) | $g\approx\theta(t,q,\lambda)$; post-event differences ↔ shadow price $p^j$ |
| $m^\pm_t(u)$, $n^\pm_t(u)$ | $\mathbb E[\lambda^\pm_u\mid\mathcal F_t]$, $\mathbb E[c^\pm_u\mid\mathcal F_t]$ (p. 9) | $m_t(u)$ |
| $f(\cdot;\Theta)$ | DNN approximation of $g$ (p. 16) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract, keywords | 1 |
| ✓ F1 | 1 Introduction (HFT, synchrony vs excitation, three contributions) | 1–4 |
| ✓ F1 | 2 Literature review (ML in finance, market-making models, cointegration and flocking) | 5–6 |
| ✓ F1 | 3 Market models and optimisation problems; 3.1 Model setup: fills (1)–(2), intensities (3), depth (4), stability | 6–9 |
| ✓ F1 | 3.2 Optimisation problem: objective (5), value function (6), HJB (7)–(8), ansatz (9), reduced HJB (10), optimal controls (11), closed HJB (12) | 9–11 |
| ✓ F1 | 4 Evidence of synchrony: Fig. 1 (IBM intensities), MLE (13), data, Table 1 (order counts), Table 2 ($\kappa$, significance, stability) | 12–15 |
| ✓ F1 | 5 Neural-network approximation; 5.1 DGM loss (15), Algorithm 1, architecture (17), parameters, Fig. 2 (optimal quotes) | 16–19 |
| ✓ F1 | 5.2 Training loss, Figs. 3–7 (loss curves, solution, terminal error) | 19–21 |
| ✓ F1 | 6 Simulation; 6.1 optimal vs constant vs asymmetric-linear (18), Table 3, Figs. 8–10; full/half/no synchrony, Table 4 | 21–27 |
| ✓ F1 | 6.2 Calibrated full/half/no synchrony (Tables 5–7, Figs. 11–12); stability levels (Table 8) | 27–30 |
| ✓ F1 | 7 Conclusion | 31–32 |
| — | Acknowledgements, References | 32–37 |
| ✓ F1 | Appendix A.1 Lemma 1 (A.1)–(A.2), Remark 2 (A.3)–(A.4) | 37–38 |
| ✓ F1 | Appendix A.2 Closed form of the intensities (A.5)–(A.9) | 38–39 |
| ✓ F1 | Appendix A.3 Theorem 3 (loss can be made small), operator (A.10), proof | 39–42 |
| ✓ F1 | Appendix A.4 Thinning algorithm (Algorithm 2) | 42–43 |
| ✓ F1 | Appendix B Table B.9 (MLE statistics 2008, 2018) | 44 |
| ✓ F1 | Appendix C Comparison with the CJR asymptotic formula (Tables C.10–C.11, Fig. C.13) | 42, 45–46 |

## Kernthesen

### 1. ⭐ HFT makes buy and sell order flow "synchronised", and this is a different mechanism from excitation (pp. 2–3)

Synchronisation «makes contemporaneous interactions between buy and sell orders feasible and also
enables the interacting effect to remain permanent in the long-term mean of order flows» (p. 3).
«Exciting events are activated by certain external stimulations ... By contrast, the synchronising
factor enhances the likelihood of integrating two processes irrespective of exogenous events» (p. 3).
The motivation is Gerig's SEC working paper on HFT synchrony (p. 2).

### 2. ⭐⭐ Market-order intensities: exponential self- and cross-excitation plus a drift coupling $\kappa$ (eq. (3), p. 8)

$$d\lambda^-_t=\beta(\theta^--\lambda^-_t+\kappa\lambda^+_t)dt+\eta\,dM^-_t+\nu\,dM^+_t,\qquad d\lambda^+_t=\beta(\theta^+-\lambda^+_t+\kappa\lambda^-_t)dt+\eta\,dM^+_t+\nu\,dM^-_t.$$
«Unlike existing models, we take the stochastic mean-reversion level of $\theta^-+\kappa\lambda^+_t$ for
the sell intensity and $\theta^++\kappa\lambda^-_t$ for the buy intensity» (p. 8). Every market order
excites (no influential/non-influential mark, i.e. CJR with $\rho=1$); baselines differ by side.
Reader's mapping: this is a linear bivariate Hawkes process with kernel $\phi(t)=e^{-Bt}J$,
$B=\beta\begin{pmatrix}1&-\kappa\\-\kappa&1\end{pmatrix}$, $J=\begin{pmatrix}\eta&\nu\\\nu&\eta\end{pmatrix}$:
a sum of two exponentials with rates $\beta(1-\kappa)$ (common mode) and $\beta(1+\kappa)$
(imbalance mode), exactly the rates that appear in (A.7)–(A.9) and Algorithm 2 (pp. 39, 43).

### 3. ⭐ LOB depth is excited by market orders and synchronised across sides, one-way (eq. (4), p. 9)

$dc^\mp_t=\xi(\alpha-c^\mp_t+\kappa_cc^\pm_t)dt+\eta_c\,dM^\mp_t+\nu_c\,dM^\pm_t$. «This is a one-way effect
because market orders cause jumps in subsequent limit orders, whereas jumps in limit orders do not
induce jumps in market order arrivals (Large, 2007).» (p. 9). Fill probability
$h(\delta,c)=e^{-\delta c}$ under i.i.d. exponential MO volumes and a flat book (p. 8).

### 4. ⭐⭐ Stability: bounded mean forecast iff $(1-\kappa)\beta>\eta+\nu$ (Lemma 1, pp. 9, 37)

ODE (A.1) gives $m_t(u)=e^{-D(u-t)}(\lambda_t-D^{-1}\pi)+D^{-1}\pi$ (A.2); «Since the eigenvalues of $D$
are $(1\pm\kappa)\beta-(\eta\mp\nu)$, $\lim_{u\to\infty}m_t(u)$ converges to $D^{-1}\pi$ if and only if
$(1\pm\kappa)\beta>\eta\mp\nu$. It implies $(1-\kappa)\beta>\eta+\nu$» (p. 37). Reader's mapping:
spectral radius of the kernel-mass matrix $K=B^{-1}J$ is $\rho(K)=(\eta+\nu)/((1-\kappa)\beta)$, so
the paper's "stability" ratio is $1/\rho(K)$. Synchronisation **lowers** the stability margin: it
adds mass to the common mode.

### 5. ⭐⭐ Who excites: other participants' market orders; the maker's fills are Bernoulli thinnings (pp. 7–8)

$N^-_t=\int_0^tI^-_sdM^-_s$, $N^+_t=\int_0^tI^+_sdM^+_s$ (1), with $I^\pm$ Bernoulli of probability
$h(\delta^\pm_{t-},c^\pm_{t-})$ (2) (p. 7). The shift operators in HJB (7) move $\lambda$ and $c$ on
every MO, filled or not (p. 10). Quotes do not feed the intensity.

### 6. Objective: risk-neutral terminal wealth with liquidation cost and running inventory penalty (eq. (5), p. 10)

$\Phi_T=X_T+q_T(S_T-\phi q_T)-\psi\int_t^Tq_u^2du$, $V=\max\mathbb E[\Phi_T\mid\cdot]$ (6). Terminal
inventory is liquidated by market orders «at a price lower than the mid-price» (p. 9). No CARA
utility. Same structure as CJR (5.2) plus a quadratic terminal cost.

### 7. ⭐⭐ The HJB is a 6-variable nonlinear PIDE with explicit feedback quotes but no closed-form solution (eqs. (7)–(12), pp. 10–11)

State $(t,q,\lambda^-,\lambda^+,c^-,c^+)$ after the ansatz $V=x+qs+g(t,q,\lambda,c)$ (9) (p. 10).
First-order conditions give (11): $\delta^{\mp*}=\frac1{c^\mp}-(\Delta^\mp_{q,\lambda,c}g-\Delta^\mp_{\lambda,c}g)$
on $\{c^\mp(\Delta_qg-\Delta_\lambda g)<1\}$, else 0 (p. 11) — the CJR exact feedback form (C.1a). The PDE
«is generally known to be difficult to solve analytically» (p. 4). No expansion, ansatz in $q$, or
Riccati reduction is attempted.

### 8. ⭐⭐ Empirics: the synchronising factor rose about eightfold from 2008 to 2018 on six US large caps (pp. 12–15)

Daily MLE (13) of $(\theta^\pm,\eta,\nu,\beta,\kappa)$ by BFGS on Lee–Ready-signed trades, 10:30–15:30,
IBM, Chevron, Apple, Amazon, JP Morgan, Microsoft, 2008 and 2018 (pp. 12–14). Table 2 (p. 15):
mean $\hat\kappa$ overall 0.50% (2008) → 4.00% (2018); significant days 152 (10.1%) → 775 (51.5%);
JP Morgan 0.00% → 8.48%, IBM 0.13% → 7.03%, Chevron 0.34% → 5.97%; Amazon falls 1.66% → 0.21%.
«the synchronising level in 2018 jumped by about eight times than that in 2008 on average» (p. 14).

### 9. ⭐⭐ Fitted branching: stability ratio ≈ 2.4 on average, self-excitation dominates cross-excitation (pp. 14–15, 44)

Stability $(1-\kappa)\beta/(\eta+\nu)$, Table 2 (p. 15): overall 2.37 (2008), 2.43 (2018), i.e.
$\rho(K)\approx0.42$ and $0.41$ (reader's reciprocal); per stock 2018 between 1.65 (Amazon,
Microsoft; $\rho(K)\approx0.61$) and 3.44 (JP Morgan; ≈ 0.29); lowest in the sample Microsoft 2008,
1.19 ($\rho(K)\approx0.84$). «the self-exciting factor $\eta$ has a remarkably higher value than the
mutually-exciting factor $\nu$ across all the stock samples» (p. 15). Table B.9 (p. 44), 2018 means:
IBM $\eta=224$, $\nu=27.4$, $\beta=749$; Apple 3447 / 435 / 7030; Microsoft 4849 / 723 / 9146 —
cross/self ≈ 0.12–0.15, decays of $10^2$–$10^4$ per second. Between 2008 and 2018 $\theta^\pm$ fell
57%, $\eta$ 26%, $\nu$ 33%, $\beta$ 10% on average (p. 15).

### 10. ⭐ Ignoring synchronisation inflates the fitted excitation and decay (Table 5, p. 28)

Without $\kappa$, 2018 means: IBM $\eta$ 224 → 828, $\nu$ 27.4 → 140, $\beta$ 749 → 1916; JP Morgan
$\eta$ 156 → 1377, $\beta$ 684 → 3055 (p. 28). «the no synchrony model leads to sharp increases in not
only the self- and mutually-exciting effects but also the mean-reverting speed compared with the
synchrony model ... From a stability perspective, the long-term moving patterns under the two models
do not change considerably» (p. 27). Reader's note: consistent with $\kappa$ acting as a second,
slower exponential that a one-exponential fit must absorb.

### 11. ⭐⭐ Solution method: deep Galerkin network on a bounded domain, $q$ treated as continuous (pp. 16–19)

Loss (15): $\|\partial_tf+\mathcal Lf\|^2_{\tilde D_T,\mu_1}+\|f(T,\cdot)+\phi q^2\|^2_{\tilde D,\mu_2}$ on
$\tilde D=[-N_1,N_1]\times[n_2,N_2]^2\times[n_3,N_3]^2$ (pp. 16–17); domain $D=(-\infty,\infty)\times[0,\infty)^4$,
i.e. inventory is a real variable (p. 16). Fully connected tanh network, 3 hidden layers × 900 units,
batch 25,000 uniform samples, Adam, learning rate $10^{-4}$ (pp. 18); «this DNN-training takes 35.83
seconds per 100 iterations. In total, iterations are run 170,000 times» (p. 18), on one Titan V GPU.
Loss 180,244 → 189.7 (p. 19).

### 12. Theorem 3 is an existence result: some network makes the loss arbitrarily small (pp. 16, 39–42)

By Hornik's universal approximation (with first derivatives) and a case split on the indicator sets
of (11), «there exists a function $f\in\mathcal N^k(\varphi)$ such that $L(f)\le\epsilon$» (p. 39), assuming a
unique $C^1$ solution $u=g$ exists (p. 16). It says nothing about whether training finds that $f$,
or how the loss bounds the error in $g$ or in the quotes.

### 13. ⭐ Accuracy is reported only as residual loss and terminal-condition error (pp. 19–21)

On $|q|\le50$ the loss ends at 47.70, on $|q|\le10$ at 10.62 (p. 20); «the error in the case of
$|q|=100$ is about 14, whereas the true values are -1000» (p. 21). There is no comparison with a
finite-difference or other exact solution of (12) for $\kappa>0$.

### 14. ⭐ The DNN-optimal quotes beat constant and inventory-linear heuristics (Table 3, p. 24)

$T=10{,}800$ s, $\beta=100$, $\theta^-=0.5$, $\theta^+=0.4$, $\kappa=0.2$, $\eta=20$, $\nu=15$; depth $\xi=40$,
$\alpha=0.3$, $\kappa_c=0.1$, $\eta_c=8$, $\nu_c=5$; $\phi=0.1$, $\psi=0.01$; 50,000 paths (pp. 19, 24).
Mean (SD): optimal 12,333 (183); asymmetric linear (18) 8,902 (146); best constant $d_0=5$: 7,578
(1,346) (p. 24). «the optimal posting case significantly outperforms the others in all the samples,
considering the minimum PnL of the optimal strategy and maximum PnLs of all the other constant
cases» (p. 24). Inventory stays within ±7 (p. 25). Reader: $\rho(K)=35/80\approx0.44$.

### 15. ⭐⭐ Ignoring synchronisation costs 9–42% of PnL in a strongly synchronised toy market (Table 4, p. 27)

$T=1800$, $\beta=50$, $\eta=4$, $\nu=0.1$, $\kappa=\kappa_c=0.9$ in the data. Mean PnL of the strategy
optimal under full synchrony 801.9, half ($\kappa=0$, $\kappa_c=0.9$) 734.5, none 564.0: «the
market-maker's PnL of case (i) outperforms those of cases (ii) and (iii) by 9.2% and 42.2%,
respectively. Indeed, the worst scenario of case (i) is better than the best of case (iii).» (p. 27).
Reader: $\rho(K)=4.1/5=0.82$, close to critical.

### 16. ⭐⭐ At calibrated scales the gain shrinks to about 1–2% of mean PnL (Table 7, pp. 29–30)

Parameters at the scale of IBM/Chevron/JP Morgan 2018 (Table 6, p. 28: $\eta=200$, $\nu=20$,
$\beta=700$, $\kappa=0.1$), $T=300$ s, 30,000 paths: mean 209.8 / 206.8 / 205.1, SD 26.23 / 30.13 /
31.20 (p. 30). «The full synchrony model creates +2.9 (+1.4%) and +4.7 (+2.3%) higher returns than
the half and no synchrony models» (p. 29). The main effect is lower dispersion and a shorter left tail.

### 17. Less stable markets give higher market-making PnL (Table 8, p. 30)

With $\theta=0.3$, $\kappa=0.1$: stability 3.5 / 2.9 / 1.6 → mean PnL 204.7 / 209.8 / 214.1 (p. 30).
«a higher expected return is more likely to occur in the optimal market-making as market instability
rises» (p. 30), because orders arrive «more frequently and irregularly».

### 18. ⭐⭐ At $\kappa=0$ the DNN solution and the CJR asymptotic formula give statistically identical PnL (Appendix C, pp. 31, 42, 45–46)

Four parameter sets near CJR's ($\beta\in\{60,100,150\}$, $\eta/\nu=4$), $\psi=10^{-5}$, $T=180$, no
liquidation cost (p. 42; Table C.10, p. 45). Expected PnL DNN vs asymptotic: 133.67 vs 133.74;
133.82 vs 133.78; 122.24 vs 122.15; 122.34 vs 122.41; absolute differences 0.04–0.09; Kruskal–Wallis
p-values 0.24–0.57 (Table C.11, p. 46). «the optimal controls estimated by the DNN method and existing
method (Cartea et al., 2014) produce statistically non-distinguishable distributions for the
market-maker's profits» (p. 31).

### 19. Printed inconsistencies and one methodological doubt (pp. 23–30, 33, 43; reader's observations)

(i) Section 6.1 says «Table 4 presents the terminal wealth PnL achieved under the three strategies»
(p. 24); that table is Table 3. (ii) Table 7 (p. 30) gives SD 26.23 / 30.13 / 31.20, so full synchrony
has 3.90 less SD than half and 4.97 less than none; the text (p. 29) attributes «-4.97 (-15.9%)» to
half and «-3.89 (-12.9%)» to none — swapped. (iii) Section 6.2 defines «the synchrony model with
$\kappa = 0$ and $\kappa_c = 0$» and «the half synchrony model with $\kappa = 0$ and $\kappa = 0$» (pp. 27),
evidently meaning $\kappa,\kappa_c\neq0$ and $\kappa=0,\kappa_c\neq0$. (iv) The CJR reference gives
*SIAM J. Financial Math.* volume «60» (p. 33); it is volume 5 (60 is the SIAM Review reprint's
volume). (v) Algorithm 2 (p. 43) draws candidate times with rate $\lambda^\mp_{t_n}$ and accepts with
$U\le\lambda_{\text{new}}$. That is valid thinning only if the intensity cannot rise between events. With
$\kappa>0$ the drift $\beta(\theta^\mp-\lambda^\mp+\kappa\lambda^\pm)$ is positive whenever
$\lambda^\mp<\theta^\mp+\kappa\lambda^\pm$, so the current value need not bound the path; simulated
arrivals may be too few in those stretches. The paper does not discuss this.

## What this source does not address

- **More than one asset.** One stock, two sides; no cross-asset excitation, no portfolio inventory
  risk. The synchronising coupling is between the buy and sell sides of one book.
- **Non-exponential kernels.** All kernels are (matrix) exponentials; no power laws, no lift.
- **Fill-driven excitation.** Excitation is by all market orders; the maker's quotes never change
  the intensities.
- **Any closed form or approximation of the value function.** No expansion in $\psi$, no ansatz in $q$,
  no Riccati system; the HJB is handed to a neural solver.
- **An exact benchmark.** No grid solution of (12); the CJR comparison (Appendix C) is only at
  $\kappa=0$ and against another approximation; the measure is PnL, not value-function or quote error.
- **Reinforcement learning, regret, CARA utility, latency, market orders by the maker.**
- **Online filtering / intraday estimation.** Parameters are fitted per day and used as known.

## Model card

- **Assets:** 1 (one stock; buy and sell sides).
- **Kernel:** exponential, generalised to a matrix exponential by the synchronising drift: kernel
  $e^{-Bt}J$ with rates $\beta(1\mp\kappa)$ (reader's mapping); same structure for LOB depth with
  $\xi,\kappa_c$.
- **Excitation:** self-side ($\eta$) and cross-side ($\nu$) jumps plus cross-side drift coupling
  ($\kappa$, "synchronisation"); MOs excite LOB depth one-way ($\eta_c,\nu_c,\kappa_c$). No cross-asset.
- **Who excites:** all market orders of other participants, filled or not; fills are Bernoulli
  thinnings with $e^{-\delta c}$.
- **Objective:** expected terminal wealth with quadratic liquidation cost $\phi q_T^2$ and running
  penalty $\psi\int q^2$ (5); risk-neutral, no CARA.
- **Solution method:** neural PDE — deep-Galerkin-type fully connected tanh network (3×900) trained on
  the residual of the 6-variable HJB (12); quotes from the explicit feedback (11).
- **Benchmark:** constant and inventory-linear heuristics (Table 3); strategies optimal under half or
  no synchrony (Tables 4, 7); CJR 2014 first-order formula at $\kappa=0$ (Table C.11).
- **Reported numbers:** PnL 12,333 vs 8,902 vs 7,578 (Table 3); +9.2% / +42.2% (Table 4, $\kappa=0.9$);
  +1.4% / +2.3% (Table 7, calibrated scale); DNN vs CJR mean-PnL differences ≤ 0.09 on ≈ 122–134
  (≤ 0.07%), KW p ≥ 0.24 (Table C.11). Regret against an exact optimum: n/a — none computed.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 3, 4, 5, 7, 9, 10, 11, 13, 15, 16, 18.**

### What this focus needs beyond the Kernthesen

1. **"Synchronisation" is a non-diagonal decay matrix.** In the project's notation the intensity is
   $d\lambda_t=(\beta\theta-B\lambda_t)dt+J\,dM_t$ with $B=\beta(I-\kappa P)$, $P$ the swap matrix.
   Standard multi-asset Hawkes models (and the project's $D=\mathrm{diag}(\beta)$) take $B$ diagonal;
   Choi et al. are a worked one-asset example of a full $B$. The cost is nothing for the Markov
   property: the state is still $(\lambda^-,\lambda^+)$, two numbers, because $e^{-Bt}J$ is the
   kernel of a 2-dimensional linear system. For several assets with cross-asset excitation this is
   the natural place to put "slow common-mode" coupling without adding states (reader's inference).
2. **The forecast stays linear, so a CJR-type linear closure would still exist.** (A.2) is
   $m_t(u)=e^{-D(u-t)}(\lambda_t-D^{-1}\pi)+D^{-1}\pi$ with $D=B-J$ — the same structure as CJR's (B.2)
   with a different matrix. The CJR expansion only needs $m_t(u)$ (Theorem 5.2 there), so the
   first-order quotes would follow with $D$ in place of $A$. The paper does not do this; it solves the
   full HJB numerically and compares with CJR only at $\kappa=0$ (Appendix C). This is the project's
   inference, not the source's claim.
3. **What Appendix C shows about the closure.** At $\kappa=0$, with small $\psi=10^{-5}$ and
   $T=180$ s, the first-order CJR formula and the DNN solution of the full HJB give PnL that agree
   to 0.07% (Table C.11, p. 46). Read as evidence, it says the linear closure is accurate in that
   regime (or that both are equally inaccurate). It is not a value-function comparison, the regime
   has a tiny penalty, and the DNN's own error is unknown (Kernthesen 12–13).
4. **Branching values for the project's parameter choices.** Fitted 2018 $\rho(K)$ ≈ 0.29–0.61 per
   stock, ≈ 0.41 on average; cross/self ≈ 0.1–0.15 on IBM, Apple, Microsoft (Table B.9); decays
   $\beta$ of several hundred to several thousand per second. The simulation parameters are at
   $\rho(K)\approx0.44$ (Table 3) and $\approx0.82$ (Table 4). These are within-book (buy/sell)
   numbers, not cross-asset ones.
5. **Who excites.** Flow-driven, like CJR (Kernthese 5). So nothing here bears on D1 (fill-driven CARA
   linearisation). For D2 (λ-dependent Riccati coefficients): the paper has no Riccati system; the
   feedback (11) depends on $\lambda$ only through $g$'s finite differences.
6. **Three-way comparison.** The paper has two of the project's three legs in one study on one
   asset: a neural PDE solution and a closed-form approximation (CJR, at $\kappa=0$). It has no exact
   solution (grid) and no RL. It does not threaten the gap claim; it is the nearest precedent for
   "neural solver vs closed form" on Hawkes market making.

### Direct quotes (for the draft)

> "Unlike existing models, we take the stochastic mean-reversion level of $\theta^- + \kappa\lambda^+_t$ for the sell intensity and $\theta^+ + \kappa\lambda^-_t$ for the buy intensity, where $\theta^\pm$ are constant mean levels." (p. 8)

> "Since the eigenvalues of D are $(1 \pm \kappa)\beta - (\eta \mp \nu)$, $\lim_{u\to\infty} m_t(u)$ converges to $D^{-1}\pi$ if and only if $(1 \pm \kappa)\beta > \eta \mp \nu$. It implies $(1 - \kappa)\beta > \eta + \nu$ since $\beta, \eta, \nu, \kappa > 0$." (p. 37)

> "To solve the PDE numerically, we propose the DNN-based approximation inspired by the deep Galerkin method (Sirignano and Spiliopoulos, 2018), a mesh-free simulation suitable for applying to high-dimensional PDE problems." (p. 4)

> "As a complementary test, we observe that the optimal controls estimated by the DNN method and existing method (Cartea et al., 2014) produce statistically non-distinguishable distributions for the market-maker's profits (Appendix C)." (p. 31)

> "In addition, we can see that the self-exciting factor $\eta$ has a remarkably higher value than the mutually-exciting factor $\nu$ across all the stock samples." (p. 15)

### Examples & illustrations (for later drafting)

- Fig. 1 (p. 12): IBM buy and sell intensities on 3 Jan 2018, two windows, spikes to 800–1000 per
  second that die within seconds, buy and sell bursts nearly simultaneous.
- Fig. 2 (p. 19): contour plots of $\delta^\mp(q,t)$ — quotes widen sharply on the side that would
  increase a large inventory near $T$.
- Table 4 vs Table 7 (pp. 27, 30): the same comparison gives +42% in a near-critical toy market and
  +2% at calibrated scale — a useful example of how model misspecification costs depend on the
  branching ratio.
- Table C.11 (p. 46): a four-row DNN-vs-closed-form table, the format the project's comparison could
  extend with an exact (grid) column.

### Boundary of this focus

One asset. The synchrony coupling is buy/sell, not cross-asset. The multi-asset reading of $B$ and
the claim that a CJR-type closure would carry over to $\kappa>0$ are the reader's inferences. Read
from the preprint; the JEDC version was not compared.

## Mentioned entities

- Models: [[cartea-jaimungal-ricci-model]] (extended here), [[glft-2013-model]],
  [[avellaneda-stoikov-model]].
- Concepts: [[hawkes-process]], [[branching-matrix]], [[intensity-forecast]], [[who-excites-the-flow]],
  [[markov-lift]], [[regret]].
- Library works cited: `cartea-2014-buy-low-sell` ([[cartea-2014-buy-low-sell]]),
  `gueant-2013-dealing-inventory-risk` ([[gueant-2013-dealing-inventory-risk]]),
  `avellaneda-2008-high-frequency-trading`, `ho-1981-optimal-dealer-pricing`,
  `guilbaud-2011-optimal-high-frequency` (cited as the 2013 Quant. Finance version),
  `bacry-2016-estimation-slowly-decreasing`.
- Cited, not in the library: Sirignano–Spiliopoulos 2018 (DGM); Hornik 1991; Gerig 2015; Large 2007;
  Bowsher 2007; Hawkes 1971 "Point spectra of some mutually exciting point processes" (JRSS B — not
  the Biometrika paper `hawkes-1971-spectra-self-exciting`); Hawkes–Oakes 1974; Ogata 1978 (MLE
  asymptotics, not `ogata-1981-lewis-simulation-method`); Ha–Kim–Lee 2015; Lee–Seo 2017;
  Da Fonseca–Zaatour 2014; Bacry–Muzy 2014; E–Han–Jentzen 2017; Kingma–Ba 2014.

## Connections

- Extends: [[cartea-2014-buy-low-sell]] / [[cartea-2018-algorithmic-trading-stochastic]] (same model
  family; adds the synchronising drift, drops the influential mark, swaps the expansion for a neural
  PDE solver; benchmarks against the CJR formula).
- Contrast on method: [[martin-2026-market-making-hawkes]] (general kernels, Mercer lift + PINN) —
  another neural PDE route, there for non-Markov kernels; [[barzykin-2026-hawkes-driven-otc]]
  (Volterra–Riccati approximation, no neural solver).
- Contrast on closure: [[begv-2021-model]] (multi-asset Riccati, Poisson flow).
- Cited: [[glft-2013-model]], [[avellaneda-stoikov-model]].
