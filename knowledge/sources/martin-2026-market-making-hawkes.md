---
title: "Martin & Tse 2026 — Optimal Market-Making with Hawkes Process via Mercer's Expansion"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: martin-2026-market-making-hawkes
depth: deep
tags: [market-making, hawkes-process, markov-lift, mercer-expansion, stochastic-liquidity, hjb, pinn, single-asset, non-exponential-kernel]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Order flow is «a pair Hawkes processes with some memory kernels» (p. 2); intensity eq. (2.1) with general decreasing kernels g± (p. 4)."
  - target: markov-lift
    type: builds-on
    confidence: extracted
    because: "«Our second contribution is to overcome this challenge by a Markovian lift technique. The theoretical foundation of this approach is based on the Mercer's expansion» (p. 3); lifted system eq. (2.10) (p. 7)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "Exponential conditional fill probability p± = exp(−κ±δ±), «widely considered in the literature - see for example Avellaneda and Stoikov (2008)» (p. 4); microfoundation recalled in Remark 2.1 (pp. 4–5)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Cited for exponential fill probability («Guéant et al. (2013)», p. 4) and for position limits (p. 2); inventory bounds q̲ < 0 < q̄ adopted (p. 5)."
  - target: begv-2021-model
    type: cites
    confidence: extracted
    because: "Listed only as an extension in the literature: «multi-asset market-making (Bergault et al. (2021))» (p. 2); the paper itself stays single-asset."
  - target: cartea-jaimungal-ricci-model
    type: builds-on
    confidence: inferred
    because: "Remark 2.2 (p. 5) positions the model against «Cartea et al. (2018)» (SIAM Review), whose jump-intensities and liquidity mean-revert «but they do not use memory kernels with decay»; identifying that SIAM Review paper with the CJR 2014 model entity is the wiki's inference."
  - target: branching-matrix
    type: mentions
    confidence: inferred
    because: "Only the scalar, per-side stability condition ||g±||₁ < 1/aλ± appears (p. 4); no off-diagonal (cross) branching terms, so this is the 1×1 diagonal special case of a branching matrix."
---

# Optimal Market-Making with Hawkes Process: A Markovian Approximation Approach via Mercer's Expansion

## Bibliographic Details
Martin, Nicholas, and Alex S. L. Tse. 2026. "Optimal Market-Making with Hawkes Process: A Markovian Approximation Approach via Mercer's Expansion." Preprint, 24 March 2026. SSRN 6451058, doi:10.2139/ssrn.6451058. Department of Mathematics, University College London. 34 pp. (19 pp. main text and references + Appendix A, pp. 19–34).

**read:** SSRN preprint dated 24 March 2026. Under the project's preprint policy this preprint *is* the original (no published version exists). All page and equation numbers below follow this version.

Keywords given by the authors (p. 1): market-making, Hawkes process, algorithmic trading, kernel decomposition, HJB equation, deep learning, physics-informed neural network.

### Notation mapping (source → project, CLAUDE.md § Notation)

| Source (Martin–Tse) | Meaning | Project symbol / remark |
|---|---|---|
| $M^\pm(t)$ | cumulative market buy (+) / sell (−) orders | counting processes of the Hawkes flow |
| $\lambda^\pm(t)$, $\lambda^\pm_0(t)$ | Hawkes intensity, deterministic baseline | $\lambda_t$, $\mu$ |
| $a_{\lambda^\pm}\,g^\pm(\lvert t-s\rvert)$ | excitation size × memory kernel | one diagonal entry of the kernel matrix; $a_{\lambda}\lVert g\rVert_1$ plays the role of $\rho(K)$ (scalar case) |
| $\kappa^\pm(t)$ | "liquidity level" = fill elasticity, itself Hawkes-driven | GLFT decay $k$ in $\Lambda e^{-k\delta}$, here stochastic |
| $p^\pm=e^{-\kappa^\pm\delta^\pm}$ | conditional fill prob. per market order | $f(\delta)$; fill intensity $\lambda^\pm e^{-\kappa^\pm\delta^\pm}$ ↔ $\Lambda e^{-k\delta}$ with $\Lambda\to\lambda_t$ |
| $\delta^+$ / $\delta^-$ | ask / bid depth | $\delta^a$ / $\delta^b$ (note: $\delta^+$ is hit by buy orders $M^+$) |
| $Q$, $\underline q<0<\bar q$, $X$, $S$, $\sigma$ | inventory, position limits, cash, mid, vol | $q_t$, $\pm Q$, $X_t$, $S_t$, $\sigma$ |
| $\epsilon^\pm$ | permanent price impact per market order | no project symbol (adverse-selection channel) |
| $\alpha$, $\beta$ | terminal / running inventory penalty | **clash:** project $\beta$ = Hawkes decays; there is no risk aversion $\gamma$ in the source |
| $\phi^\pm_\lambda(t),\phi^\pm_\kappa(t)\in\mathbb R^n$ | Mercer feature maps $\phi_j=\sqrt{\xi_j}\varphi_j$ | — |
| $\Lambda^\pm_\lambda(t),\Lambda^\pm_\kappa(t)\in\mathbb R^n$ | lifted states $\int_0^t\phi(s)\,dM(s)$ | **clash:** project $\Lambda$ = GLFT intensity scale |
| $H(t,s,z)$; $h(t,z)$ | value function; reduced value function | $\theta(t,q,\lambda)$ ↔ $h$; **clash:** project $H$ = Hamiltonian |
| $J(y,\kappa)$ | $\sup_{\delta\in[0,C]}e^{-\kappa\delta}(\delta+y)$ | per-unit-intensity Hamiltonian $H^{i,s}$ (exact, capped at $C$) |
| $\gamma$ (Sec. 4.2) | PINN loss weight | **clash:** project $\gamma$ = risk aversion |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (HFT motivation; Hawkes market-making literature; "liquidity" response to order flow; three contributions) | 1–3 |
| ✓ F1 | 2.1 Modelling setup (Hawkes order flow (2.1), price, fill probability, liquidity (2.2), thinning (2.3), objective (2.4)–(2.5)) | 4–6 |
| ✓ F1 | 2.2 A Markovian approximation of the problem (Mercer Thm 2.3, truncation (2.8)–(2.9), lifted system (2.10)–(2.11), convergence Thm 2.4, Remark 2.5, Lemma 2.6) | 6–8 |
| ✓ F1 | 3 Derivation of the HJB equation under Markovian approximation (generator (3.1), HJB (3.2)–(3.5), feedback quotes (3.4)) | 9–11 |
| ✓ F1 | 4.1 Learning the kernel feature maps | 11–12 |
| ✓ F1 | 4.2 Solving the HJB equation via physics-informed neural network ((4.1)–(4.2)) | 12 |
| ✓ F1 | 4.3 Configurations of the numerical experiments (Table 1, Fig. 1, network sizes) | 12–13 |
| ✓ F1 | 4.4 The numerical results (Figs. 2–8) | 14–16 |
| ✓ F1 | 5 Conclusion and further work | 16–17 |
| — | References | 17–19 |
| ✓ F1 | Appendix A (intro, standing assumptions, class $\mathcal H_\rho$ (A.1)) | 19 |
| ✓ F1 | A.1 Construction of a parameterised family of the state processes | 19–21 |
| ✓ F1 | A.2 Some estimates and the uniform convergence of the approximating processes in expectation (Prop. A.1, Cor. A.2, Prop. A.3) | 21–27 |
| ✓ F1 | A.3 Almost-sure uniform convergence of the approximating state processes (Prop. A.4, A.5) | 27–31 |
| ✓ F1 | A.4 Convergence of the approximating value functions (Prop. A.6, proof of Thm 2.4) | 31–34 |

## Kernthesen

### 1. ⭐ Self-exciting order flow does not by itself raise the maker's fill chance, because liquidity reacts to the same flow (p. 2)

The motivating argument of the paper: one might expect that, with clustered market orders, a market order arriving raises the probability that the maker's resting quote is executed soon. The authors reject this as a general implication: «This however is not necessarily true because the conditional filled probability of a limit order (i.e. the probability of successful limit order execution conditional on the arrival of a directionally-matched market order) in general depends on both the quoted spread as well as an array of "liquidity" factors, and the latter could change dynamically in response to the arrival of the market orders» (p. 2). "Liquidity" is defined broadly as external market characteristics influencing the conditional fill probability — LOB shape, size distribution of incoming orders, competing limit-order traffic (p. 2). Empirical support cited: market orders tend to be followed by new limit orders at the same price (Bonart and Gould 2017; Weber and Rosenow 2005), which signals improved liquidity and pushes the maker to quote more competitively (p. 2).

### 2. Most market-making models fix the fill-probability function; the paper makes its elasticity a Hawkes-driven state (pp. 2–3, 5)

The literature (CJR being the noted exception) «model[s] the conditional filled probability as a static function of the quoted spread with constant parameters» (p. 2). Martin–Tse instead parameterise $p^\pm=\exp(-\kappa^\pm\delta^\pm)$ (p. 4) by a stochastic liquidity level that follows «a Volterra-type dynamics which will jump upon the arrival of a market order but the shock will decay over time as prescribed by another memory kernel» (p. 3), eq. (2.2): $\kappa^\pm(t)=\kappa^\pm_0(t)+a_{\kappa^\pm}\int_0^t K^\pm_\kappa(t,s)\,dM^\pm_s$ (p. 5). Large $\kappa$ = liquid market = fill probability very sensitive to the quoted depth (p. 4). The separate $\kappa^+,\kappa^-$ «further distinguish the demand and supply side of the market liquidity» (p. 4). No $L^1$ constraint is imposed on $g_\kappa$ at this point (p. 5; but see Kernthese 10 and "Contested" in the focus).

### 3. Order flow: two independent Hawkes processes with general decreasing kernels and a scalar stability condition (p. 4, eq. 2.1)

$\lambda^\pm(t)=\lambda^\pm_0(t)+a_{\lambda^\pm}\int_0^t K^\pm(t,s)\,dM^\pm(s)$, $K^\pm(t,s)=g^\pm(\lvert t-s\rvert)$ with $g^\pm$ continuous, decreasing, and «L1 norms satisfy the stability conditions $\lVert g^\pm\rVert_1:=\int_0^T g^\pm(u)du<1/a_{\lambda^\pm}$» (p. 4). Buy orders excite buy orders, sell orders excite sell orders — no cross term between $M^+$ and $M^-$ in (2.1). Baselines $\lambda^\pm_0(t)$ are strictly positive, bounded, deterministic (p. 4).

### 4. The mid-price jumps with each market order — permanent impact is the adverse-selection channel (p. 4)

$dS(t)=\sigma\,dW(t)+\epsilon^+dM^+(t)-\epsilon^-dM^-(t)$ with $W$ independent of $M^\pm$ and $\epsilon^\pm\ge 0$ «capturing the (permanent) price impact caused by each unit of the incoming order flows» (p. 4). Because the same market order that may fill the maker also moves the mid against the filled side, $\epsilon^\pm$ enters the optimal quote directly (Kernthese 17); the abstract's claim that ignoring persistence «underestimates adverse selection risk» (p. 1) rests on this coupling.

### 5. Fills are an independent thinning of the market-order stream, gated by inventory limits (p. 5, eq. 2.3)

Each arriving buy (sell) market order fills the maker's one-unit ask (bid) with probability $p^+(t-)$ ($p^-(t-)$) provided $Q(t-)>\underline q$ ($Q(t-)<\bar q$): $N^+(t)=\sum_{i=1}^{M^+_t}\mathbf 1\{U^+_i<p^+(\tau^+_i-),Q(\tau^+_i-)>\underline q\}$ with i.i.d. uniforms $U$ (p. 5). Thus all market orders — filled or not — drive intensities and liquidity; the maker's own fills do not feed back into $\lambda$ or $\kappa$. The unconstrained case $\underline q=-\infty$, $\bar q=+\infty$ «can simplify some of our theoretical results» (p. 5).

### 6. Objective: risk-neutral expected P&L with terminal and running inventory penalties, depths capped at $C$ (p. 6, eqs. 2.4–2.5)

$V:=\sup_{\delta\in\mathcal A}\mathbb E\big[X(T)+Q(T)(S(T)-\alpha Q(T))-\beta\int_0^T Q(u)\,du\big]$ (p. 6, as printed; the HJB later uses $-\beta q^2$, so a squared running penalty is evidently intended — see "Contested"). Admissible strategies are predictable with $\delta^\pm_t\in[0,C]$ (2.5). There is no exponential (CARA) utility: the criterion is the Cartea–Jaimungal style "expected wealth minus inventory penalty".

### 7. ⭐ Away from exponential kernels the control problem is non-Markovian — this is the obstacle the paper addresses (pp. 3, 6)

«Away from exponential memory kernel, it is generally difficult to approach a stochastic control problem featuring Hawkes processes due to the lack of Markovian properties» (p. 3). «It is theoretically and numerically challenging to solve (2.4) directly because the underlying dynamics are not Markovian due to the presence of the kernels $K^\pm(\cdot)$ and $K^\pm_\kappa(\cdot)$» (p. 6). The paper does not exploit the exact one-dimensional Markov structure of the exponential case; it treats OU as just one kernel to be expanded.

### 8. ⭐⭐ Truncated Mercer expansion factorises each kernel and turns the intensity into a linear read-out of pure-jump lifted states (pp. 6–7, eqs. 2.6–2.10)

Mercer's theorem (Thm 2.3, p. 6): a continuous, symmetric, positive-semidefinite $F$ on $[0,T]^2$ has $F(t,s)=\sum_n\xi_n\varphi_n(t)\varphi_n(s)$, uniformly convergent. Truncating at $n$ gives $K^\pm_n(t,s)=\phi^{\pm\top}_\lambda(t)\phi^\pm_\lambda(s)$ with $\phi_j=\sqrt{\xi_j}\varphi_j$ (2.8), likewise $K^\pm_{\kappa,n}$ (2.9). Then $\lambda^\pm(t)\approx\lambda^\pm_0(t)+a_{\lambda^\pm}\phi^{\pm\top}_\lambda(t)\Lambda^\pm_\lambda(t)$ with $\Lambda^\pm_\lambda(t):=\int_0^t\phi^\pm_\lambda(s)\,dM^\pm(s)\in\mathbb R^n$ (pp. 6–7). The lifted states only jump, $d\Lambda^\pm_\lambda=\phi^\pm_\lambda(t)\,dM^\pm(t)$; the time-decay of memory is carried by the deterministic feature vector $\phi(t)$, so $d\lambda^\pm=[\partial_t\lambda^\pm_0+a_{\lambda^\pm}(\partial_t\phi^{\pm\top}_\lambda)\Lambda^\pm_\lambda]dt+a_{\lambda^\pm}\phi^{\pm\top}_\lambda\phi^\pm_\lambda\,dM^\pm$ (p. 7). The approximated problem (2.11) is posed on the Markov state $(S_n,X_n,Q_n,\lambda^\pm_n,\kappa^\pm_n,\Lambda^\pm_{\lambda,n},\Lambda^\pm_{\kappa,n})$ of (2.10) (p. 7).

### 9. ⭐ The lift adds $n$ states per kernel, i.e. $4n$ for the four kernels of the single-asset model (pp. 7, 9, 12)

The state vector is $z=(x,q,\lambda^+,\lambda^-,\kappa^+,\kappa^-,\Lambda^+_\lambda,\Lambda^-_\lambda,\Lambda^+_\kappa,\Lambda^-_\kappa)$ (p. 9). With four kernels ($K^\pm$, $K^\pm_\kappa$) and $n$ features each, the lifted part has $4n$ coordinates; $\lambda^\pm,\kappa^\pm$ are kept as additional (functionally redundant) coordinates, generated in training from $\Lambda$ (p. 12, fn. 4). In the experiments $n=4$ (p. 13), so $h$ takes $t$, $x$, $q$, four intensity/liquidity coordinates and 16 lifted coordinates. The paper calls (3.5) high-dimensional «due to the possibly large number of state variables» (p. 11) but gives no scaling analysis.

### 10. ⭐⭐ Convergence theorem: the lifted value function converges to the true one as the truncation order grows — no rate (pp. 7–8, Thm 2.4)

Assumptions: kernels admit Mercer expansions (continuous, symmetric, PSD), a stability-type bound on $\lVert g^\pm\rVert_1$ and $\lVert g^\pm_\kappa\rVert_1$, and *either* (1) no position limits *or* (2) the eigenvalue tail condition (2.12) on the order-flow kernels. Conclusion: $\lim_{n\to\infty}\lvert V_n-V\rvert=0$ (p. 8). The statement is qualitative: no convergence rate in $n$ and no bound on the error of the induced feedback control are given. «The proof is long and technical, and is therefore deferred to the appendix» (p. 7).

### 11. Inventory limits require fast eigenvalue decay; Gaussian, OU and fractional kernels qualify (pp. 7–8, eq. 2.12, Lemma 2.6)

Condition (2.12): $\sum_{i\ge1}\big(\sum_{j>i}(\xi^\pm_j)^2\big)^{1/2}<\infty$ — imposed only on the order-flow kernels, not on the liquidity kernels (fn. 3, p. 8). Sufficient: $\xi_n\le c\,n^{-\alpha}$ with $\alpha>3/2$ (p. 8). Gaussian kernel: super-exponential decay; OU kernel as Matérn-1/2: $\xi_n=O(n^{-2})$; fractional $(1+z/a)^{-r}$ as generalised Cauchy: $\xi_n=O(n^{-2})$ (p. 8). Heuristically «this condition will hold if the eigenvalues (sorted in descending order) ... are decaying sufficiently fast» (p. 8).

### 12. Singular power-law kernels are outside the theorem; complete monotonicity is not needed (p. 8, Remark 2.5)

«Theorem 2.3 does not cover singular kernel with $g(0+)=+\infty$» because $K(t,s)=g(\lvert t-s\rvert)$ would be discontinuous on the diagonal; the power-law $g(z)=\frac{c}{\Gamma(\alpha)}z^{-\alpha}$ is the example, to be regularised as $\frac{c}{\Gamma(\alpha)}(z+\varepsilon)^{-\alpha}$, «equivalent to a fractional kernel» (p. 8). Contrast with Bernstein-type lifts (sums of exponentials): «our approach does not require the kernel to be completely monotone» (p. 8) — e.g. the Gaussian kernel, which is not completely monotone, is admissible. The method is placed in the Volterra-lift tradition of transient impact and rough volatility (Buet-Golfouse and Martin 2023; Hamaguchi 2024) (p. 3).

### 13. The proof couples all kernel-indexed models pathwise on one Poisson random measure (pp. 19–21, App. A.1)

Hawkes processes are built by Poisson embedding, $M^\pm(t)=\int_0^t\int\mathbf 1\{u\le\lambda^\pm(s-)\}\mathcal N^\pm(ds,du)$ (A.2), so that the true model $Y$ and all truncated models $Y_n$ «are all constructed pathwise against the same $W(\omega,\cdot)$ and $\mathcal N^\pm(\omega;\cdot,\cdot)$» (p. 21). Without loss of generality $a_\lambda=a_\kappa=1$ (p. 19); kernels live in a class $\mathcal H_\rho$ (A.1) with row and column $L^1$ norms below $\rho<1$ (p. 19). Finite exponential moments follow Leblanc (2024) (p. 20, (A.5)).

### 14. Kernel error controls counting-process, intensity, fill-probability and price errors in $L^1/L^2$ (pp. 21–25, Prop. A.1, Cor. A.2)

With $\epsilon_n(t)=\int_0^t\lvert K-K_n\rvert du$, $E_n(t)$ a column-sup $L^1$ error and $E_{\kappa,n}$ the sup error of the liquidity kernel, Prop. A.1 bounds $\mathbb E\sup\lvert M-M_n\rvert$, $\mathbb E\int\lvert\lambda-\lambda_n\rvert$, $\mathbb E\sup\lvert\kappa-\kappa_n\rvert$, $\mathbb E\sup\lvert p-p_n\rvert$ (using $\lvert e^{-x}-e^{-y}\rvert\le\lvert x-y\rvert$ and $\delta\le C$) and $\mathbb E\sup\lvert S-S_n\rvert^2$ (pp. 22–25). Cor. A.2: if $E_n(T)\to0$ and $E_{\kappa,n}\to0$ (A.20), all these converge (p. 25). Without inventory limits, Prop. A.3 extends this to $N^\pm$ and $Q$ via a conditional-Poisson argument and BDG (pp. 25–27).

### 15. With inventory limits, convergence is obtained by eventual path coincidence (Borel–Cantelli) and induction over jump times (pp. 27–31, Props. A.4–A.5)

Because a position limit makes fills path-dependent through $Q$, $L^1$ closeness is not enough. Under the summability condition (A.23) — $\min(\sum_n E_n(T),\sum_n\int_0^T\epsilon_n)<\infty$ and $E_{\kappa,n}\to0$ — Markov's inequality and Borel–Cantelli give that $\sup_t\lvert M^\pm-M^\pm_n\rvert=0$ for all large $n$ almost surely, since it is integer-valued (p. 28). Jump times then coincide, and an induction over the ordered jump times of $Q$ shows $N_n,Q_n$ eventually equal $N,Q$ (p. 29). Prop. A.5 upgrades this to $L^2$ convergence of $N^\pm$ by dominated convergence (pp. 30–31). Condition (2.12) is exactly what delivers (A.23) for truncated Mercer series (p. 34).

### 16. Value-function convergence follows from objective convergence for each strategy (pp. 31–34, Prop. A.6)

Prop. A.6: under (A.23), or under (A.20) without limits, $\lvert J(\delta)-J_n(\delta)\rvert\to0$ «for any admissible $\delta\in\mathcal A$» (p. 31). The proof of Thm 2.4 shows the truncated Mercer kernels eventually lie in $\mathcal H_\rho$ by uniform convergence, verifies (A.20) and, under (2.12), (A.23) (pp. 33–34), and concludes $\lvert V-V_n\rvert=\lvert\sup_\delta J(\delta)-\sup_\delta J_n(\delta)\rvert\le\sup_\delta\lvert J(\delta)-J_n(\delta)\rvert\to0$ (p. 34).

### 17. ⭐ Cash and price drop out of the value function; optimal depths are in feedback form with an adverse-selection add-on (pp. 10–11, eqs. 3.2–3.4)

The HJB is $\partial_tH-\beta q^2+\sup_{(\delta^+,\delta^-)\in[0,C]^2}\mathcal L^{\delta^+,\delta^-}H=0$ (3.2), with generator (3.1) distinguishing post-jump states with fill ($z^\pm$: cash, inventory, price, $\lambda$, $\kappa$, $\Lambda$ all updated) and without fill ($\tilde z^\pm$: only price, $\lambda$, $\kappa$, $\Lambda$ updated) (p. 10). The ansatz $H(t,s,z)=x+qs+h(t,z)$, terminal $h(T,z)=-\alpha q^2$ (p. 10) yields (3.4): $\delta^{+,\star}=\min\big(C,\max\big(\tfrac{1}{\kappa^+}+\epsilon^+-h(t,z^+)+h(t,\tilde z^+),0\big)\big)$, $q>\underline q$, and symmetrically for $\delta^{-,\star}$ (p. 11). The depth is the GLFT/AS-type $1/\kappa$ term, plus the price impact $\epsilon$ the maker will suffer, minus the value gain from the inventory move — with $\kappa=\kappa(t)$ now stochastic.

### 18. ⭐ The reduced HJB keeps the exact exponential Hamiltonian and admits no closed form; it is too high-dimensional for finite differences (pp. 3, 11, eq. 3.5)

(3.5) contains drift terms $(\partial_t\nu_0+a_\nu\partial_t\phi_\nu^\top\Lambda_\nu)\partial_\nu h$ for $\nu\in\{\lambda^\pm,\kappa^\pm\}$, non-local jump differences $\lambda^\pm(\pm q\epsilon^\pm+h(\tilde z^\pm)-h(z))$, and the optimised fill terms $\lambda^\pm J(h(z^\pm)-h(\tilde z^\pm)-\epsilon^\pm,\kappa^\pm)$ with the three-regime function $J(y,\kappa)=y$ for $y\ge 1/\kappa$, $e^{-1+\kappa y}/\kappa$ for $1/\kappa-C<y<1/\kappa$, $e^{-\kappa C}(C+y)$ for $y\le1/\kappa-C$ (p. 11). No polynomial-in-$q$ ansatz, quadratic Hamiltonian approximation or Riccati reduction is attempted. «The resulting HJB equation is a high-dimensional one and it cannot be conveniently solved by traditional numerical methods like finite difference» (p. 3).

### 19. Feature maps are learned by a neural network, not computed as eigenfunctions (pp. 11–12, Sec. 4.1)

A feedforward network $\phi_\theta:[0,T]\to\mathbb R^n$ is fitted so that $K(t,s)\approx\phi_\theta(t)^\top\phi_\theta(s)$, minimising squared error on points sampled from $\{t\ge s\}$ plus a penalty on $1-\lVert\phi_\theta(t)\rVert_2^2$, because all kernels are normalised to $K(t,t)=g(0)=1$ (p. 12). This follows Joseph and Jain (2024) and Buet-Golfouse and Martin (2023) (p. 3). One network per kernel ($K^\pm$, $K^\pm_\kappa$), shared architecture (p. 12). The learned factorisation is a rank-$n$ PSD approximation, not necessarily the Mercer truncation that Thm 2.4 is about.

### 20. The lifted HJB is solved by a physics-informed neural network on sampled states (pp. 12–13, eqs. 4.1–4.2)

$h$ is a network $h_\psi$; the residual $\mathcal F[h_\psi]$ (4.1) uses autodiff for $\partial_t h$, $\partial_\nu h$ and $\partial_t\phi$, and the loss (4.2) is mean squared residual plus $\gamma$ × mean squared terminal error $(h_\psi(T,z)+\alpha q^2)^2$ (p. 12), following Raissi et al. (2019). Interior and terminal points are sampled uniformly over $[0,T)\times\mathcal Z$ with $\Lambda$ in $[-20,20]$ (pp. 12–13, fn. 4). Network: 1 hidden layer, 32 ReLU neurons; $M_{\rm int}=M_{\rm term}=100{,}000$; $\gamma=3\times10^{-4}$; Adam, gradient clipping, Xavier init (p. 13). Quotes follow from (3.4) with the trained $h_{\hat\psi}$ (p. 12).

### 21. Experiments use one shared kernel for flow and liquidity, three kernel families, $n=4$ features (pp. 12–13, Table 1, Fig. 1)

«To simplify the analysis, we assume the four different kernels in our market-making model are identical» (p. 12). Kernels: OU $e^{-\lvert t-s\rvert/a}$, $a=0.1$; Gaussian $e^{-(t-s)^2/(2b^2)}$, $b=0.316$; fractional $(1+\lvert t-s\rvert)^{-r}$, $r=0.51$ (Table 1, p. 13). Parameters: $\lambda_0^\pm=30$, $\kappa_0^\pm=100$, $\underline q=-10$, $\bar q=10$, $a_\lambda^\pm=a_\kappa^\pm=2$, $\alpha=0.001$, $\beta=0.01$, $\epsilon^\pm=0.005$, $T=1$ (p. 13). Feature networks: 4 outputs, 1 hidden layer of 64 ReLU, $M_{\rm kernel}=25{,}000$ (p. 13); Fig. 1 shows learned vs exact kernels visually close.

### 22. Without excitation, quotes are inventory-skewed at the start and settle quickly (p. 14, Fig. 2)

With $a_\lambda=a_\kappa=0$: for $Q(0)<0$ the ask depth $\delta^+$ is initially large and $\delta^-$ small (and conversely), «driven by the market-maker's incentive to keep the inventory level neutral», and «The spreads are stabilised quickly as the trading session goes on once the inventory balance has been restored» (p. 14). Depths are of order 0.01–0.02 (Fig. 2).

### 23. Short-memory (OU) excitation makes the optimal quotes oscillate (p. 14, Fig. 3)

Under OU kernels the depths are of similar magnitude to the no-kernel case but «exhibit significant oscillations»: the maker reacts to jumps in intensity and liquidity, then unwinds the adjustment because the influence dissipates fast. «Consequently, the market-marker's quotes will oscillate over time as a result of their continual adjustment in presence of self-exciting order flow and liquidity under weak persistence» (p. 14).

### 24. Kernel persistence shapes quoting: long memory gives smooth quotes, the Gaussian is in between (pp. 14–15, Figs. 4–5)

«More generally, the qualitative features of the quotes depend crucially on the kernels used» (p. 14). Under the fractional kernel shocks dissipate slowly, adjustments are gradual and quotes «more stable over the trading session» (Fig. 4); the Gaussian kernel gives «mild oscillation with relatively stable trajectories» (Fig. 5) (p. 14).

### 25. ⭐ Two competing effects of an incoming market order; at high persistence the liquidity effect dominates and quotes tighten (p. 15, Figs. 6–7)

As the OU parameter $a$ rises (0.1 → 10), quotes become less oscillatory and drift slightly down over time (Fig. 7). «On the one hand, the clustering of market orders suggest that that number of market orders will increase on average following an incoming market order which in turn improves the fill probability of the market-maker's order. On the other hand, the increase in the overall liquidity level triggered by an incoming market order will reduce the conditional fill probability of the market-maker's limit order because of the improved liquidity provision elsewhere. In this particular numerical example, the effect from the rise in liquidity level dominates under high persistence parameter» (p. 15). The intro summarises: self-exciting liquidity makes makers «more proactively time the widening and tightening of the quoted spreads» (p. 3).

### 26. ⭐ Ignoring excitation costs performance and worsens tail risk (p. 16, Fig. 8)

Strategies trained under OU $a=1.0$ ("sophisticated") vs. as if no kernel ("naive"), both evaluated in an OU $a=1.0$ environment over 1000 paths: naive mean −0.700, median −0.432; sophisticated mean 0.727, median −0.064 (Fig. 8, p. 16). The sophisticated distribution is positively skewed and the naive one negatively skewed, «indicating that the appropriate incorporation of the kernels not only improves the average performance but also helps controlling the downside risk» (p. 16). This is the paper's only quantitative performance comparison; there is no comparison with an exact or reference optimum.

### 27. Hawkes market-making literature so far is mostly learning-based; CJR is the structural precursor (pp. 2–3, 5)

Lai et al. (2023) — deep hedging for option market-making under Hawkes; Kumar (2024) — neural Hawkes in an agent-based simulator; Jain et al. (2025) — impulse control under exponential Hawkes, solved by RL (p. 2). Cartea–Jaimungal–Ricci (2018) model mutually exciting arrival rates and LOB-shape jumps with mean reversion; Martin–Tse replace this by «a generic memory kernel under a full-fledged Hawkes process» (p. 3; Remark 2.2, p. 5).

### 28. Declared extensions: stochastic baselines, buy–sell cross-excitation, RL on the Mercer state, and market orders (pp. 16–17)

«In terms of avenue of future research, one could explore stochastic baseline intensities, cross-excitation between buy and sell flows, or reinforcement learning methods that build directly on the Mercer's representation» (p. 16). Allowing market orders as well would make the problem «a hybrid of market-making and optimal execution problem» (pp. 16–17).

## Figures and tables

- Table 1 (p. 13): the three kernels and their parameters.
- Fig. 1 (p. 13): exact vs NN-learned kernels $K(t,0)$ (legend reads "OU Kernel: a = 1.0" while Table 1 says $a=0.1$).
- Fig. 2 (p. 14): mean ± 1 sd depth paths, no kernel, $Q(0)\in\{-3,0,3\}$.
- Fig. 3 (p. 14): same, OU $a=0.1$.
- Fig. 4 (p. 15): fractional $r=0.51$. Fig. 5 (p. 15): Gaussian $b=0.316$.
- Fig. 6 (p. 15): OU kernel shapes for $a\in\{0.1,0.5,1,10\}$. Fig. 7 (p. 15): depths for $Q(0)=0$ under those $a$.
- Fig. 8 (p. 16): histograms of penalised P&L, naive vs sophisticated, OU $a=1.0$.
- No figures extracted to `knowledge/assets/` in this pass.

## What this source does not address

Single asset only; no multi-asset portfolio, no inventory-risk coupling across assets, no cross-asset excitation (multi-asset market making is BEGV's subject, [[begv-2021-model]]; cross-asset Hawkes networks are treated in [[acero-2026-hawkes-structured-networks]]). No buy–sell cross-excitation — explicitly deferred (p. 16). No closed form, no quadratic-Hamiltonian approximation and no Riccati structure (the closed-form route is [[glft-2013-model]] / [[begv-2021-model]]; the Hawkes-with-Riccati route is [[barzykin-2026-hawkes-driven-otc]] via [[volterra-riccati]]). No CARA utility, no risk aversion parameter. No calibration to data; all experiments are simulated with chosen parameters. No convergence rate in $n$, no error bound for the PINN, no validation of the PINN against an exact solution (not even the $a=0$ case, where a low-dimensional ODE system in $q$ is available), no regret against the true optimum. No stochastic baselines, no market orders by the maker, no competition. Singular power-law kernels are excluded from the theory (p. 8).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 3, 5, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20, 26, 28.**

### What this focus needs beyond the Kernthesen

1. **Excitation inventory.** Self-excitation only: $M^+\to\lambda^+,\kappa^+$ and $M^-\to\lambda^-,\kappa^-$; no $M^-\to\lambda^+$ term (eq. 2.1, p. 4) although the introduction states that order flows show «strong self- and cross-excitation behaviours» (p. 2); buy–sell cross-excitation is listed as future work (p. 16). Liquidity (fill-decay) excitation *is* modelled, same-side only (eq. 2.2, p. 5). Who excites: all market orders, not the maker's fills (eq. 2.3, p. 5). Several assets: not modelled, not discussed beyond citing BEGV (p. 2).
2. **Where closure holds and where it breaks.** The only closure is *linear in cash and price*: $H=x+qs+h(t,z)$ (p. 10), possible because the objective is risk-neutral and the impact $\epsilon^\pm$ is additive. Beyond that it breaks for three separable reasons visible in (3.4)–(3.5) (p. 11): (a) the Hamiltonian $J$ is kept exact and exponential, not quadratised; (b) the liquidity state $\kappa$ enters inside the exponential and as $1/\kappa$ in the quote, so no polynomial ansatz can be linear in it; (c) the state $\Lambda\in\mathbb R^{4n}$ jumps by the time-dependent vector $\phi(t)$, so even the intensity dependence is a non-local difference operator in $\Lambda$, not a transport term. The paper reports no ODE or Riccati structure at any point (checked against the full text: "Riccati" never occurs, and "closed-form" only in the title of the cited BEGV paper).
3. **Lift mechanics relevant to a multi-asset extension (inferred).** The lift is generic in the kernel: a kernel $K_{ij}$ from asset $j$ into asset $i$ would need its own rank-$n$ factorisation, so the lifted dimension scales like $n\times$(number of distinct kernels) — up to $n d^2$ for $d$ assets with full cross-asset excitation plus the liquidity kernels, against $d$ (or $d$ per decay) for an exponential kernel. If all kernels from source $j$ share one feature basis, the state is $\Lambda_j=\int\phi_j\,dM_j$, i.e. $n$ per source process — the paper does not discuss this. Because $\phi(t)$ comes from Mercer on $[0,T]^2$, the lift is horizon-specific and non-stationary; even the exponential kernel, which has an exact one-dimensional lift, is approximated by an $n$-term series.
4. **Status of the theory vs. the numerics.** Thm 2.4 is about truncated *Mercer* series as $n\to\infty$ (p. 7); the numerics use an NN-learned rank-4 factorisation (p. 13) and a PINN, with no error control on either. The only validation is visual kernel fit (Fig. 1, p. 13) and a naive-vs-sophisticated P&L comparison (Fig. 8, p. 16).
5. **Parameter values sit outside the stated stability condition (inferred calculation).** With $a_\lambda=2$ and $T=1$: OU $a=0.1$ gives $a_\lambda\lVert g\rVert_1\approx0.20$, Gaussian $b=0.316$ ≈0.79, but OU $a=1.0$ (the setting of Fig. 8) ≈1.26, OU $a=10$ ≈1.90, fractional $r=0.51$ ≈1.65 — all above the bound $\lVert g\rVert_1<1/a_\lambda$ of p. 4. On a finite horizon the process does not explode, but these runs are not covered by the hypotheses of Thm 2.4.

### Direct quotes (for the draft)

> «For our market-making problem, the feature maps extracted from the Hawkes memory kernels serve as the additional auxiliary state variables such that the dynamics of the control problem can be approximated by a Markovian system. Standard dynamic programming approach then becomes applicable again which enables us to derive an HJB equation and obtain the approximated optimal quotes in feedback form.» (p. 3)

> «Furthermore, unlike the alternative Markovian lifting technique that relies on the Bernstein's theorem, our approach does not require the kernel to be completely monotone.» (p. 8)

> «Equation (3.5) cannot be solved easily by standard numerical methods due to the possibly large number of state variables. In this section, we outline a procedure based on deep neural networks.» (p. 11)

> «In terms of avenue of future research, one could explore stochastic baseline intensities, cross-excitation between buy and sell flows, or reinforcement learning methods that build directly on the Mercer's representation.» (p. 16)

> «On the other hand, the increase in the overall liquidity level triggered by an incoming market order will reduce the conditional fill probability of the market-maker's limit order because of the improved liquidity provision elsewhere.» (p. 15)

### Examples & illustrations (for later drafting)

- Competing-effects example: OU kernels with $a\in\{0.1,0.5,1,10\}$, $Q(0)=0$; at high persistence the liquidity effect dominates and the maker quotes shallower depths (Figs. 6–7, p. 15).
- Naive vs sophisticated maker in an OU $a=1.0$ world: mean penalised P&L −0.700 vs 0.727, negatively vs positively skewed (Fig. 8, p. 16) — the paper's "cost of ignoring excitation" number, usable as a rough analogue of a misspecification regret.
- Three kernel families (OU, Gaussian, fractional) fitted with $n=4$ NN features (Table 1 and Fig. 1, p. 13): a concrete instance of how small a lift the authors use in practice.

### Boundary of this focus

A reader looking for a closed-form or Riccati-type reduction under Hawkes flow, for buy–sell or cross-asset excitation, or for any multi-asset statement will not find it here: this is a single-asset, self-exciting, risk-neutral model whose lifted HJB is solved only numerically. What transfers is the *lift* (generic, non-exponential kernels, convergence of $V_n\to V$) and the idea of a Hawkes-driven fill elasticity — not a closure.

## Mentioned entities

- Models: [[glft-2013-model]], [[begv-2021-model]], [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]] (cited as Cartea et al. 2018, SIAM Review)
- Concepts: [[hawkes-process]], [[markov-lift]], [[branching-matrix]], [[hamiltonian-quadratic-approximation]] (not used — exact Hamiltonian kept), [[matrix-riccati-equation]] (absent), [[volterra-riccati]] (alternative route, not used), [[intensity-forecast]], [[regret]]
- Other works cited in the source (prose only): `jain-2025-impulse-control-hawkes`, `kumar-2024-deep-hawkes-process`, `lai-2023-data-driven-deep`, `bacry-2015-hawkes-processes-finance`, `boyce-2025-market-making-exogenous`, `cartea-2015-algorithmic-high-frequency`, `ho-1981-optimal-dealer-pricing`; Buet-Golfouse & Martin 2023, Hamaguchi 2024, Joseph & Jain 2024, Raissi et al. 2019, Leblanc 2024 (not in the library).

## Connections

- Builds on: [[hawkes-process]] (eq. 2.1), [[markov-lift]] (Mercer instead of sum-of-exponentials), [[avellaneda-stoikov-model]] (exponential fill probability), [[cartea-jaimungal-ricci-model]] (Hawkes-driven LOB response, here with general kernels).
- Cites: [[glft-2013-model]] (exponential fills, position limits), [[begv-2021-model]] (as a multi-asset extension it does not pursue).
- Contrast (wiki's reading): the closed-form route of [[glft-2013-model]] / [[begv-2021-model]] via [[hamiltonian-quadratic-approximation]] and [[matrix-riccati-equation]] is not taken; the Hawkes-plus-quadratic route of [[barzykin-2026-hawkes-driven-otc]] ([[volterra-riccati]]) handles the memory analytically where this paper lifts it and solves numerically; [[intensity-forecast]] is implicit in $\phi(t)^\top\Lambda(t)$ but not used as a state.
- Related B1 sources: [[bergault-2024-price-aware-automated]], [[acero-2026-hawkes-structured-networks]] (cross-asset Hawkes structure that this paper lacks).
- Performance gap (Fig. 8) is a misspecification comparison, not a [[regret]] against the optimum.
