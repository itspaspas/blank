---
title: "Jusselin 2021 — Optimal Market Making with Persistent Order Flow"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: jusselin-2021-persistent-order-flow
depth: deep
based_on: preprint
tags: [market-making, hawkes, completely-monotone-kernel, path-dependent-control, viscosity-solutions, markov-lift, branching-diffusion, single-asset, lob]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«We consider a market model with one market maker and order flows driven by general Hawkes processes» (abstract, p. 1); intensity e^{-kδ/σ}Φ(∫K dN), K completely monotone (p. 2)."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "«when K(t)=Σα_i e^{-γ_i t}, there exists a Markovian representation of the model in dimension 2n+2» (p. 3); exact for sums of exponentials (Thm 3.1 iv, p. 9), dense in completely monotone L1 kernels (Lemma 3.1, p. 10), value and control converge (Props 3.1–3.2, pp. 7–8). Infinite-dimensional exact lift = the function-valued state θ_t (p. 2)."
  - target: shadow-price
    type: supports
    confidence: extracted
    because: "Optimal quotes are δ^a = (σ/k − D^a_K U^K)_+ and δ^b = (σ/k − D^b_K U^K)_+ (eq. 5, p. 7): the value jump over one fill (inventory and memory jump together) plays the shadow-price role."
  - target: hamiltonian-quadratic-approximation
    type: mentions
    confidence: inferred
    because: "For the branching-diffusion numerics «we approximate the generator of the PIDE by a second order polynomial» in U and D^α U (App. H, p. 35). A numerical device, not a closure; BEGV is not cited (identification with the concept is ours)."
  - target: intensity-forecast
    type: mentions
    confidence: inferred
    because: "The state θ_t(u)=∫_0^t K(u−s)dN_s (p. 2) is the past-event contribution to the future intensity curve, not the full conditional forecast (no resolvent of future self-excitation); the link to m_t(u) is drawn by the ingester."
  - target: branching-matrix
    type: mentions
    confidence: inferred
    because: "Each side excites only itself with the same scalar kernel K (p. 2); the implied branching matrix is diag(‖K‖₁, ‖K‖₁) for linear Φ; no cross-side or cross-asset terms."
  - target: matrix-riccati-equation
    type: mentions
    confidence: inferred
    because: "No ODE, Riccati or closed form appears; even the Poisson comparator is solved by finite differences (p. 11). Verified by full-text read."
  - target: volterra-riccati
    type: mentions
    confidence: inferred
    because: "Power-law-type kernels are handled by sum-of-exponentials approximation plus convergence (pp. 7–10, 12), not by any Volterra/Riccati reduction."
  - target: regret
    type: mentions
    confidence: inferred
    because: "Reports value-function gaps of misspecified controls δ⁰ (Poisson) and δ¹ (one exponential) against δ² (true kernel), Figs 1–3 (pp. 12–13); the word regret is not used."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "«Hence in this paper we extend the works [3, 6, 11] to market order flows driven by Hawkes processes with general kernels» (p. 2); [3] = Avellaneda–Stoikov 2008; spreads controlled «As in [3]» (p. 2)."
  - target: glft-2013-model
    type: builds-on
    confidence: extracted
    because: "Same sentence (p. 2): [11] = Guéant–Lehalle–Fernandez-Tapia 2013, cited as the Poisson inventory-risk benchmark (p. 1)."
  - target: cartea-jaimungal-ricci-model
    type: builds-on
    confidence: extracted
    because: "«the authors of [6, 27] use a refined model based on Hawkes processes with exponential kernels» (p. 1); [6] = Cartea–Jaimungal–Ricci 2014 «Buy low, sell high»; extended to general kernels (p. 2)."
---

# Optimal Market Making with Persistent Order Flow

## Bibliographic Details

Jusselin, Paul. 2021. "Optimal Market Making with Persistent Order Flow." *SIAM Journal on
Financial Mathematics* 12 (3): 1150–1200. DOI 10.1137/20M1376054. Author affiliation: École
Polytechnique, CMAP. Funding: ERC Grant 679836 Staqamof; chair "Analytics and Models for
Regulation" (p. 14).

**Read:** arXiv 2003.05958v2 [q-fin.TR], stamped 26 Oct 2020 (title page dated 27 Oct 2020),
38 pp. — a **user-approved substitute**; the published SIFIN version (pp. 1150–1200) could not be
obtained. **All page numbers, equation numbers, theorem numbers and figure numbers on this page
follow the preprint v2.** The preprint's printed page numbers equal the PDF page numbers. The
proofs (Sect. 5, pp. 15–27) and Appendices A–H (pp. 27–37) were read in full; references pp. 37–38.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $N^a_t$, $N^b_t$ | number of buy (resp. sell) market orders up to $t$; buy orders hit the MM's ask | fill counts on ask / bid |
| $i_t=N^b_t-N^a_t$ | MM inventory, $i_0=0$ (p. 2) | $q_t$. ⚠ sign is reversed in Sect. 5.1 ($di=dN^a-dN^b$, p. 15) — typo |
| $\delta^a,\delta^b\ge0$ | ask / bid spreads around fundamental price $P$ (p. 2) | $\delta^a,\delta^b$ |
| $P_t$, $d(t,P)$, $\sigma$ | fundamental price, Lipschitz drift, volatility, eq. (1) | $S_t$, $\sigma$ |
| $e^{-\frac{k}{\sigma}\delta}$ | fill-intensity factor; $k/\sigma$ is the decay in the spread | GLFT $e^{-k\delta}$ with project $k\equiv k/\sigma$ |
| $\Phi(\cdot)$ | continuous (in proofs: nondecreasing, linear-growth) link function; $\Phi(x)=\mu+x$ in the numerics | baseline $\mu$ + linear Hawkes; plays GLFT's $\Lambda$ |
| $K$ | **scalar** completely monotone $L^1$ kernel, same for both sides | ⚠ clashes with project $K$ (branching matrix); $\lVert K\rVert_1$ ≈ scalar branching ratio |
| $\theta^{K,j}_t(u)=\int_0^tK(u-s)\,dN^j_s$ | function-valued memory state (p. 2); $\theta^{K,j}_t(t)$ = current excitation | ⚠ clashes with project $\theta(t,q,\lambda)$ (reduced value function) |
| $X^K=(P,i,\theta^{K,a},\theta^{K,b})$, $\mathcal E^K$, $\Theta^K_t$ | infinite-dimensional Markov state, its locally compact domain (pp. 2–4) | exact (non-finite) lift |
| $K_{\alpha,\gamma}=\sum_{i=1}^n\alpha_ie^{-\gamma_it}$, $c^j_{t,i}$ | sum-of-exponentials kernel and its factor states (pp. 8–9) | ⚠ $\gamma_i$ = decays (project $\beta$, $D=\mathrm{diag}(\beta)$), not risk aversion |
| $\mathcal{SE}$ | positive combinations of decreasing exponentials (p. 8) | — |
| $m(du)$ | Bernstein measure, $K(x)=\int_0^\infty e^{-ux}m(du)$, eq. (7) | — |
| $r$, $g$, $G$ | discount rate, running reward, terminal payoff (eq. 2) | no project symbol; $g=-\mu i^2$ in Sect. 4 |
| $\mu$ | **two meanings**: inventory penalty in $(N)$ and Hawkes baseline in $\Phi(x)=\mu+x$, both $=0.1$ (p. 11) | ⚠ penalty ≈ $\tfrac12\gamma\sigma^2$; baseline = $\mu$ |
| $U^K$, $U^{\alpha,\gamma}$ | value functions on $\mathcal E^K$ and $E_n$ | value function (not reduced) |
| $D^a_K\varphi,\ D^b_K\varphi$ | jump operators: value after one buy/sell order minus value now (p. 5) | $-p^j$ (shadow price with sign flipped) |
| $\mathcal R_{\alpha,\gamma}$ | continuous map from function-state to factor-state (App. E) | — |

### Equation index (source numbering)

(1) price SDE · (2) control problem · (3) rewritten problem with compensators · (HJB)$_K$
(unnumbered, p. 5) · (4) Hamiltonian maximisers · (5) optimal feedback · (6) value convergence ·
(HJB)$_{\alpha,\gamma}$ (p. 9) · (7) Bernstein representation · (8) Markov property · (9)–(14)
comparison proof · (15) value function · (16) sub-solution proof · (17) lift correspondence ·
(18)–(21) a-priori bounds · (22)–(24) Crandall–Ishii adaptation · (25) derivatives of $\theta$ ·
(26)–(27) branching representation · (LHJB)$_K$ (p. 25).

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract, keywords | 1 |
| ✓ F1 | 1 Introduction: stylised facts, market model, eqs. (1)–(2), function-valued lift, three-step approximation strategy | 1–3 |
| ✓ F1 | 2.1 Appropriate set for $X^K$ (Lemma 2.1, domain $\mathcal E^K$) | 3–4 |
| ✓ F1 | 2.2 HJB equation, eq. (3), (HJB)$_K$, maximisers (4) | 4–5 |
| ✓ F1 | 2.3 Viscosity solutions: Definitions 2.1–2.2, semi-jets | 5–6 |
| ✓ F1 | 2.4 Existence of an optimal control: Theorem 2.1, eq. (5) | 6–7 |
| ✓ F1 | 3 How to approximate the optimal control (three steps) | 7 |
| ✓ F1 | 3.1 Convergence of solutions and controls: Props 3.1–3.2, eq. (6) | 7–8 |
| ✓ F1 | 3.2 Solving the problem when $K\in\mathcal{SE}$: lift, (HJB)$_{\alpha,\gamma}$, Theorem 3.1 | 8–10 |
| ✓ F1 | 3.3 Density of $\mathcal{SE}$ in completely monotone $L^1$: eq. (7), Lemma 3.1 | 10 |
| ✓ F1 | 3.4 Conclusion: recipe; dimension $2n+2$ problem | 10–11 |
| ✓ F1 | 4 Numerical applications: problem $(N)$ | 11 |
| ✓ F1 | 4.1 Impact of self-excitation: controls $\delta^0,\delta^1,\delta^2$, Figs 1–3 | 11–13 |
| ✓ F1 | 4.2 Numerical illustration of Sect. 3.4: power-law-type kernel, Fig. 4 | 12, 14 |
| ✓ F1 | 5.1 Formal probability space, change of measure, eq. (8) | 15 |
| ✓ F1 | 5.2 Proof of Theorem 2.1 (comparison, value function, DPP, verification, (LHJB)) | 16–25 |
| ✓ F1 | 5.3 Proof of Proposition 3.1 | 25–26 |
| ✓ F1 | 5.4 Proof of Theorem 3.1 (iv) | 26–27 |
| ✓ F1 | App. A Proof of Lemma 2.1 | 27 |
| ✓ F1 | App. B A-priori inequalities (Hawkes moments, Lemma B.1, utility rewriting) | 27–30 |
| ✓ F1 | App. C Equivalence of the two viscosity definitions | 30–31 |
| ✓ F1 | App. D Crandall–Ishii lemma on the non-standard domain | 32–33 |
| ✓ F1 | App. E Existence of $\mathcal R_{\alpha,\gamma}$ (Vandermonde) | 34 |
| ✓ F1 | App. F Proof of Lemma 3.1 (Riemann sums of the Bernstein measure) | 34 |
| ✓ F1 | App. G Approximating sequence for Sect. 4.2 (Mittag-Leffler) | 35 |
| ✓ F1 | App. H Probabilistic (branching) representation of the PIDE; H.1 measure | 35–37 |
| ✓ (list only) | Acknowledgments, References [1]–[27] | 14, 37–38 |

## Kernthesen

### 1. ⭐ Market makers must account for both clustering and long memory of market-order flow (pp. 1–2)

Two stylised facts: clustering («after a buy (for say) market order it is likely that a new one is
going to be sent shortly», p. 1) and long memory (the autocorrelation of trade signs has a
power-law tail, Lillo & Farmer 2004, p. 1). «Poisson processes neither reproduce the clustering
nor the long memory property of market order flows» (p. 1). Exponential-kernel Hawkes models
(Cartea–Jaimungal–Ricci 2014; Chen et al., working paper) reproduce clustering «but not its long
memory. However when the kernel has a power law tail, both properties are reproduced» (p. 2).
Hence the stated goal: «we extend the works [3, 6, 11] to market order flows driven by Hawkes
processes with general kernels» (p. 2) — [3] Avellaneda–Stoikov, [6] CJR 2014, [11] GLFT 2013.

### 2. ⭐⭐ One market maker supplies all liquidity, so every market order is one of his fills — and fills drive the excitation (p. 2)

«We consider a market with one market maker controlling the best bid and ask prices and with
market takers sending only market orders of unit volume» (p. 2). $N^a$ ($N^b$) counts buy (sell)
market orders, and «$i_t=N^b_t-N^a_t$ the market maker's inventory» (p. 2). There is no
competing liquidity and no distinction between orders and the maker's fills: the counting process
that excites future flow *is* the maker's fill process. Since the intensity of $N^j$ is damped by
the maker's own spread (Kernthese 3), **the maker's quotes shape future intensity through his own
executions**: wider quotes now mean fewer fills now and therefore less self-excitation later.
(The source does not comment on this feedback channel; the observation is the ingester's reading
of the model, p. 2, eq. (3).)

### 3. ⭐⭐ Intensity = exponential spread response × nonlinear function of a completely monotone Hawkes convolution, per side, no cross-excitation (p. 2)

$$\lambda^{a,\delta}_t=e^{-\frac{k}{\sigma}\delta^a_t}\lambda^{a,0}_t,\qquad \lambda^{b,\delta}_t=e^{-\frac{k}{\sigma}\delta^b_t}\lambda^{b,0}_t,\qquad \lambda^{j,0}_t=\Phi\Big(\int_0^tK(t-s)\,dN^j_s\Big),$$
«where Φ is a continuous function and K a completely monotone $L^1$ function» (p. 2; complete
monotonicity on $\mathbb R_+$, fn. 1). The dependence on the spread-to-volatility ratio is
motivated by «classical financial economics results» (Dayri & Rosenbaum 2015; Madhavan et al.
1997; Wyart et al. 2008): «the average number of trades per unit of time is a decreasing function
of the ratio between spread and volatility» (p. 2). Buy orders excite only buy orders and sell
only sell, with **the same** $K$ and $\Phi$ on both sides; there is no cross-side kernel and one
asset. For the a-priori bounds $\Phi$ is assumed nondecreasing with $|\Phi(x)|\le C(1+|x|)$ and
$K$ bounded (App. B.1, p. 28).

### 4. The objective is a discounted, risk-neutral expected P&L with general running and terminal rewards (pp. 2, 4)

Eq. (2): $\sup_{\delta\in\mathcal A}\mathbb E^\delta\big[G(i_T,P_T)e^{-rT}+\int_0^Te^{-rs}\big(g(i_s,P_s)\,ds+\delta^a_s\,dN^a_s+\delta^b_s\,dN^b_s\big)\big]$,
with $r>0$, $g,G$ continuous of at most quadratic growth; «Typical choices would be $G(x,y)=xy$
and $g(x,y)=-x^2$» (p. 2). Price $dP_t=d(t,P_t)dt+\sigma dW_t$ (eq. 1), independent of order flow.
Admissible controls are nonnegative predictable spreads w.r.t. the filtration of $(P,N^a,N^b)$
(p. 2). Replacing $dN$ by compensators gives the equivalent problem (3) (p. 4; martingale property
App. B.3, p. 30). No CARA utility appears.

### 5. ⭐⭐ The exact Markov state is function-valued: the kernel-weighted history $\theta^K_t(\cdot)$ (pp. 2–3)

«when $N^a$ and $N^b$ are general Hawkes processes $(P,i,N^a,N^b)$ is not Markovian. In order to
circumvent this issue we need to consider auxiliary state variables» (p. 2): $X^K=(P,i,\theta^{K,a},\theta^{K,b})$
with $\theta^{K,j}_t(u)=\int_0^tK(u-s)\,dN^j_s$, «random functions from $\mathbb R_+$ into
$\mathbb R_+$» such that $(t,X^K_t)$ «is Markovian» (p. 3). The current intensity is
$\Phi(\theta^{K,j}_t(t))$; the rest of the function carries how past orders will keep contributing.
In the exponential case $(P,i,N^a,N^b,\lambda^b,\lambda^a)$ is already Markovian (fn. 2, p. 2).

### 6. ⭐ A locally compact domain makes viscosity theory usable on an infinite-dimensional state (pp. 3–4, App. A)

$L^1$ is not locally compact, so the memory lives in $\Theta^K_t=\{\sum_{i=1}^nK(\cdot-T_i),\ n\in\mathbb N,\ T_1\le\dots\le T_n\le t\}$.
Lemma 2.1 (i): «The set $\Theta^K_T$ is a locally compact closed subset of $L^1$» (p. 3). The proof
uses that $\lVert\theta\rVert_1=n\lVert K\rVert_1$ pins down the number of events, so bounded
sequences have finitely many atoms whose times converge (App. A, p. 27). The domain
$\mathcal E^K=\{(t,x)\in[0,T]\times\mathcal X^K_T:\ x\in\mathcal X^K_t\}$ is «the appropriate domain
to use the theory of viscosity solutions» (p. 4).

### 7. ⭐⭐ The HJB is a nonlocal PIDE whose jump operators move inventory and memory together (pp. 4–5)

Jump operators (p. 5): $D^a_K\varphi(t,x)=\varphi(t,p,i-1,\theta^a+K(\cdot-t),\theta^b)-\varphi(t,p,i,\theta^a,\theta^b)$
and symmetrically $D^b_K$ with $i+1$ and $\theta^b+K(\cdot-t)$. (HJB)$_K$:
$F(x,U,\nabla U,\partial^2_{pp}U,D_KU)=0$ on $\mathcal E^K$, $U(T,\cdot)=G$, with
$$F(x,u,q,A,I)=ru-q_1-d(t,p)q_2-\tfrac12\sigma^2A-g(i,p)-\sup_{\delta\ge0}\Phi(\theta^a(t))e^{-\frac k\sigma\delta}(\delta+I_1)-\sup_{\delta\ge0}\Phi(\theta^b(t))e^{-\frac k\sigma\delta}(\delta+I_2).$$
«Note that the dependence in K of (HJB)$_K$ lies in the operator $D_K$» (p. 5). There is no
transport term in $\theta$: between events the function $\theta$ does not change; only the
evaluation point $t$ moves. «For such general partial-integro differential equation (PIDE for
short) it is a priori impossible to prove existence of a smooth solution» (p. 5).

### 8. ⭐ The Hamiltonian factorises: intensity level × a function of the value jump, with explicit maximiser (p. 5)

«A straightforward computation gives the maximizers $\delta^*_a=(\sigma/k-I_1)_+$ and
$\delta^*_b=(\sigma/k-I_2)_+$» (eq. 4, p. 5). Because the intensity level $\Phi(\theta^j(t))$
multiplies the whole sup, the optimal quote does **not** depend on the current intensity directly,
only on the value jump $I_j=D^j_KU$, which itself depends on the memory state. (Derivation by the
ingester: for $I<\sigma/k$ the sup equals $\Phi(\theta^j(t))\,\tfrac{\sigma}{k}e^{-1+kI/\sigma}$;
for $I\ge\sigma/k$ it equals $\Phi(\theta^j(t))\,I$. The Hamiltonian is therefore piecewise
exponential/linear in $I$, the same separable form as GLFT with intensity amplitude $\Phi(\theta^j(t))$.)

### 9. Viscosity solutions are defined with the nonlocal term evaluated on $U$ itself (pp. 5–6, App. C)

Definitions 2.1 (test functions) and 2.2 (semi-jets $\bar J^{\pm}$ with a continuous "$h$" component
on $\mathcal Z^K_T$) are shown equivalent (App. C, pp. 30–31). The nonlocal operator is left on $U$:
«This is because $D_KU$ only requires finiteness of U to be defined» (p. 6).

### 10. ⭐⭐ Theorem 2.1: existence, uniqueness in polynomial growth, and an optimal feedback control (p. 7)

«(i) There exists a unique viscosity solution $U^K$ with polynomial growth to (HJB)$_K$. (ii) This
solution satisfies: $U^K(0)=\sup_{\delta\in\mathcal A}\mathbb E^\delta[\dots]$ (iii) Problem (2) admits a
solution given by $\delta^{K,*}_t=\delta^K(t,X^K_t)$», with
$\delta^K_a=(\sigma/k-D^a_KU^K)_+$, $\delta^K_b=(\sigma/k-D^b_KU^K)_+$ (eq. 5, p. 7). Proof
route (p. 6; Sect. 5.2, pp. 16–25): comparison for bounded (Prop. 5.1) then polynomial-growth
(Prop. 5.2) semi-solutions; dynamic programming principle (Thm 5.1, after Touzi 2012);
verification that $U^K_*$, $U^{K*}$ are super/sub-solutions (Prop. 5.3); the feedback is shown
optimal via the linear equation (LHJB)$_K$ (p. 25). «The main difficulty is to adapt the
Crandall-Ishi's lemma to our framework» (p. 6), done in App. D by exploiting that the only
second-order derivative is in the scalar price $p$ (p. 32).

### 11. Assumptions behind Theorem 2.1 (pp. 2, 15, 28–30)

Collected from the text: $K$ completely monotone, $L^1$ (bounded, continuous; $\lVert K\rVert_1>0$ is
used in Lemma 2.1); $\Phi$ continuous, nondecreasing, linear growth (App. B.1); $d$ Lipschitz; $g,G$
continuous, at most quadratic growth; $r>0$ (used in the comparison step $r(U-V)\le\dots$, p. 17);
unit order size; controls $\delta\ge0$ predictable. The probability space is canonical with a
reference measure $\mathbb P_0$ under which $N^a,N^b$ are Poisson with rate $\lambda_0$; controlled
laws come from a Doléans-Dade change of measure, a true martingale by Sokol's Novikov-type
criterion because $\lambda^j(t,x,\delta)\le C(1+\lVert x\rVert)$ (p. 15). Lemma B.1:
$|U^K(t,x)|\le C(1+\lVert x\rVert^2)$ (p. 28). No assumption of stationarity ($\lVert K\rVert_1<1$)
is needed on the finite horizon (ingester's observation: none is stated; App. B.1 dominates by a
linear-kernel Hawkes process).

### 12. Counting processes make the optimal control admissible without regularity (p. 7)

«in order to obtain existence of an admissible optimal control we have benefited from the fact that
we are dealing with counting processes, whose infinitesimal generators are defined for any finite
functions independently of their regularity» (p. 7). Implementing it means monitoring
$\theta^a,\theta^b$, «equivalent to monitor the list of arrival times of buy and sell market orders»
(p. 7).

### 13. ⭐ The exact HJB is not computable: its domain is infinite-dimensional (pp. 3, 7)

«$\mathcal E^K$ is a subset of an infinite dimensional vector space. So we cannot compute $U^K$ using
classic numerical methods» (p. 7). This motivates the three-step approximation (pp. 3, 7):
(1) value/control stability under kernel convergence, (2) finite lift for sums of exponentials,
(3) density of sums of exponentials among completely monotone kernels.

### 14. ⭐⭐ Value functions and optimal controls are stable under kernel approximation (Props 3.1–3.2, pp. 7–8)

Prop. 3.1: for continuous $L^1$ kernels $K_n\to K$ in $L^1$ and uniformly on $[0,T]$, $K$ completely
monotone, «for any $x\in\mathcal E^K$ we have $U^K(x)=\lim_{(y,n)\in\bar{\mathcal E}\to(x,+\infty)}U^{K_n}(y)$»
(eq. 6, p. 7), with $\bar{\mathcal E}=\bigcup_n\mathcal E^{K_n}\times\{n\}\cup\mathcal E^K\times\{+\infty\}$.
«The main technical difficulty … is that the functions $(U^{K_n})_{n\ge0}$ are defined on different
domains» (p. 8). Prop. 3.2: «for any t we have almost surely $\lim_{n\to+\infty}\delta^{K_n,*}_t=\delta^{K,*}_t$»
(p. 8). Proof by half-relaxed limits (extension of Touzi's Thm 5.8), Sect. 5.3 (pp. 25–26).
**No convergence rate is given.**

### 15. ⭐⭐ For sums of exponentials the model has an exact finite Markov lift of dimension $2n+2$ (pp. 8–10)

For $K_{\alpha,\gamma}(t)=\sum_{i=1}^n\alpha_ie^{-\gamma_it}$: $c^j_{t,i}=\int_0^t\alpha_ie^{-\gamma_i(t-s)}dN^j_s$,
$\lambda^{j,0}_t=\Phi(\sum_ic^j_{t,i})$, $dc^j_{t,i}=-\gamma_ic^j_{t,i}dt+\alpha_idN^j_t$ (p. 9);
domain $E_n=[0,T]\times\mathbb R\times\mathbb Z\times\mathbb R^n_+\times\mathbb R^n_+$. The lifted
(HJB)$_{\alpha,\gamma}$ adds transport terms $-\langle\gamma,\nabla_{c^a}U\rangle-\langle\gamma,\nabla_{c^b}U\rangle$
and jumps $c^j\mapsto c^j+\alpha$ (p. 9). Theorem 3.1: unique viscosity solution, optimal feedback
$\delta^{\alpha,\gamma}_j=(\sigma/k-D^\alpha_jU^{\alpha,\gamma})_+$, and «(iv) We have
$U^{K_{\alpha,\gamma}}=U^{\alpha,\gamma}\circ\mathcal R_{\alpha,\gamma}$» (p. 9), so «the controls …
are actually the same» (p. 10). $\mathcal R_{\alpha,\gamma}$ recovers the $c$'s from derivatives
$\theta^{(j)}(T)$ by inverting a Vandermonde matrix (App. E, p. 34). The factor representation «is
somehow larger than the first one» (p. 9).

### 16. ⭐⭐ Sums of exponentials are dense in completely monotone $L^1$ kernels, preserving $K(0)$ and $\lVert K\rVert_1$ (Lemma 3.1, pp. 10, 34)

Bernstein: «any completely monotone function can be written as the Laplace transform of a positive
measure m» (eq. 7, p. 10). Riemann sums of $m$ on a grid of $[0,\sqrt n]$ with mesh $1/\sqrt n$ give
$K_n\le K$ converging uniformly on compacts and in $L^1$; one extra exponential
$\alpha_ne^{-\beta_n\cdot}$ restores «$\lVert K_{\alpha_n,\gamma_n}\rVert_1=\lVert K\rVert_1$ and
$K_{\alpha_n,\gamma_n}(0)=K(0)$» (Lemma 3.1 iii, p. 10; App. F, p. 34). Inspired by Abi Jaber's
lifting of rough Heston (p. 3). **Complete monotonicity is used here, and only here, in an
essential way** (ingester's reading: Sects. 2 and 3.2 use only continuity, boundedness,
integrability and positivity of $K$).

### 17. The practical recipe: fit a sum of exponentials, solve the finite PIDE, monitor the factors (p. 10)

«1. Fix n positive and find α, γ … such that $K_{\alpha,\gamma}$ is the closest possible from K.
2. Approximate numerically $U^{\alpha,\gamma}$ … 3. Monitor $Y^{\alpha,\gamma}$ and apply the control
$\delta^{\alpha,\gamma}(t,Y^{\alpha,\gamma})$» (p. 10).

### 18. ⭐⭐ The lift's only flaw is its dimension: beyond $n=2$ finite differences fail (pp. 3, 11)

«The only flaw of this method is that the set $E_n$ is a subset of a vector space of dimension
$2n+2$. Hence when n is larger than 2 it is very unlikely that simple finite differences methods can
be used to solve numerically (HJB)$_{\alpha,\gamma}$» (p. 11). Alternatives: neural networks
(Huré et al. 2018) or the branching probabilistic representation (Henry-Labordère et al. 2019),
the latter used here (p. 11).

### 19. Numerical problem: risk-neutral P&L with quadratic inventory penalty, no price state (p. 11)

$(N):\ \sup_\delta\mathbb E^\delta[\int_0^T\delta^a_sdN^a_s+\delta^b_sdN^b_s-\mu i_s^2ds]$, i.e. $G=0$,
$g=-\mu i^2$; «We take $k/\sigma=20$ and $\mu=0.1$» and «discard the price variable from the PIDEs
since it does not appear in the optimization problem» (p. 11). (No discount appears in $(N)$
although $r>0$ is assumed in Sect. 2.)

### 20. ⭐⭐ Hawkes-aware vs Poisson controls: claimed 10% + 10% value gains (pp. 11–13, Figs 1–3)

$\Phi(x)=\mu+x$, $K=\alpha_1e^{-\gamma_1t}+\alpha_2e^{-\gamma_2t}$. Three controls (p. 11): «δ⁰ is the
optimal control of a market maker believing that buy and sell market order flows are Poisson
processes with intensity µ₀», δ¹ for a one-exponential Hawkes model, δ² $=\delta^{K,*}$. Parameters:
«(a) µ₀ = 1, (b) µ₁ = 0.1, γ₁ = 1 and α₁ = 0.9, (c) µ = 0.1, γ₂ = (1, 1) and α₂ = (0.45, 0.45)»;
all HJBs solved «using finite differences methods» (p. 11). Result: «considering an exponential
kernel Hawkes model for the order flows leads to a 10% gain compared with a strategy considering
that market order flows is a Poisson process. Using two exponentials leads to another 10% gain»
(p. 12). Value functions are compared *under the true model* (the misspecified makers'
controls evaluated in the true dynamics; implied, not spelled out). Grid sizes, horizon and
inventory bounds are not reported; Fig. 1 runs to $T-t=5$, Figs 2–3 to $|i|\le10$. See
"Contested" below for why these numbers do not match the figure.

### 21. ⭐ Convergence demonstrated numerically for a power-law-tailed kernel with up to ~1000 exponentials (pp. 12, 14, 35)

Kernel $K(t)=\dfrac{\lambda}{\lambda+(t+\varepsilon)^\alpha}\dfrac{1}{(t+\varepsilon)^\beta}\mathbf 1_{\mathbb R_+}(t)$,
$\lambda=0.1$, $\alpha=0.7$, $\beta=0.4$, «$\varepsilon=0.01$ is a small shift used for numerical
purposes» (p. 12) — tail $\sim t^{-1.1}$. It is the Laplace transform of a fractional derivative of a
Mittag-Leffler density, so the approximants come from Riemann sums of that density (App. G,
p. 35). Values at $x_0=(0,0,5K,0)$, $x_1=(0,5,5K,0)$, $x_2=(0,-5,5K,0)$ (inventory 0, ±5, five
buy orders at time 0) converge: Fig. 4 shows the log relative error between $U^{K_n}(x^n_i)$ and
$U^K(x_i)$ falling from about −2 to about −3.3 by linear regression as $n$ goes to ≈1100, with
Monte-Carlo scatter (read off the plot, p. 14; $T=1$). «This proves the tractability of the method»
(p. 12). How $U^K$ itself (the reference) was computed is not stated beyond «we used the
probabilistic representation» (p. 12).

### 22. ⭐ The "fully consistent" numerics need an extra polynomial approximation of the Hamiltonian (App. H, pp. 35–37)

The branching method «is insensitive to the dimension of the domain of the PIDE. Theoretically the
method works for any semi-linear PIDE admitting a strong solution and with a generator that can be
written as a power serie. Thought this is not the case for (HJB)$_{\alpha,\gamma}$, in order to
implement this method we approximate the generator of the PIDE by a second order polynomial and
assume that the approximated PIDE have a strong solution» (p. 35). The surrogate nonlinearity is
$f=f_0+f_1U+\sum_jf^j_{2,1}D^\alpha_jU+f^j_{2,2}(D^\alpha_jU)^2$; particles move along the
deterministic decay $dc=-\gamma c\,dt$ and branch into children displaced by
$\Delta^a=(-1,\alpha,0)$, $\Delta^b=(1,0,\alpha)$ (pp. 35–36). The method also assumes the number
of descendants before $T$ is a.s. finite (p. 36). Neither approximation is quantified.

### 23. ⭐ No closed form, ODE or Riccati structure is derived at any point

The paper never reduces the value function: not in the Poisson case (solved by finite differences,
p. 11), not for one exponential, and not via an ansatz in inventory. The only explicit formula is
the pointwise maximiser (4). (Verified by full-text read; this is a negative finding, not a claim of
the author.)

### 24. Several typographical inconsistencies in the preprint (pp. 2, 8, 9, 11, 12, 15, 35)

(a) inventory sign $i=N^b-N^a$ (p. 2) vs $di=dN^a-dN^b$ (p. 15) and $X^{K,+a}$ with $i+1$ (p. 8) vs
$D^a_K$ with $i-1$ (p. 5); (b) p. 8 writes $\delta^{K,a,*}_t=D^a_KU^K$ instead of $(\sigma/k-D^a_KU^K)_+$;
(c) Thm 3.1 (iii) lists $(\delta^{\delta,\gamma}_a,\delta^{\delta,\gamma}_a)$; (d) $\mu$ used for both
penalty and baseline (p. 11); (e) Sect. 4.2 defines $x_2$ twice (p. 12); (f) App. G swaps the roles
of $\alpha^n_i$ (weights) and $\gamma^n_i$ (decays) (p. 35); (g) Sect. 3.4 writes (HJB)$_{\alpha,\beta}$.
Whether the SIFIN version corrects these is unknown (preprint read).

## Figures and tables

- Fig. 1 (p. 12): value functions vs $T-t\in[0,5]$ for $\delta^0,\delta^1,\delta^2$ at $c^a=(0,10)$,
  $c^b=(0,10)$, $i=-10$. Read off the plot at $T-t=5$: ≈107 ($\delta^0$), ≈110 ($\delta^1$), ≈114 ($\delta^2$).
- Fig. 2 (p. 13): surface of $U^{\delta^2}-U^{\delta^1}$ over $i\in[-10,10]$ and $c^{b,2}\in[0,\approx10]$,
  $c^a=(10,0)$, $c^{b,1}=10$; max ≈2.5, near zero for central inventories, largest at $i=-10$.
- Fig. 3 (p. 13): same for $U^{\delta^2}-U^{\delta^0}$; max ≈25 at $i=-10$, small rise at $i=+10$.
- Fig. 4 (p. 14): log relative error of $U^{K_n}$ vs $U^K$ at three states, $n$ up to ≈1100, with
  regression line (≈ −1.9 → −3.3); $T=1$.
- No tables.

No figures extracted to `knowledge/assets/` (write scope limited to this page).

## What this source does not address

- **Several assets.** One asset, one price $P$, one inventory $i$. No portfolio risk, no correlation,
  no cross-asset kernel. For the multi-asset Poisson closed form see [[begv-2021-model]]
  ([[bergault-2021-closed-form-approximations]]); for multi-asset Hawkes market making see
  [[acero-2026-hawkes-structured-networks]].
- **Cross-side excitation.** Buy orders excite only buy orders and sell only sell, with one shared
  kernel $K$ (p. 2). No mutual excitation, no matrix kernel.
- **Closed forms / ODE / Riccati reductions.** None (Kernthese 23).
- **Order flow that is not the maker's fills.** With one maker every market order is his fill; there is
  no exogenous request/order stream that excites independently of his quotes.
- **Non-completely-monotone kernels** (e.g. kernels with a hump) for the approximation step;
  existence (Thm 2.1) is stated for completely monotone $K$ only.
- **Price–flow coupling, adverse selection, order sizes.** Price is an independent diffusion, orders
  have unit size, no informed flow.
- **CARA utility.** Only discounted expected reward with running/terminal terms.
- **Rates of convergence** of $U^{K_n}\to U^K$ or of the branching scheme; **calibration to data**
  (no empirical section).
- **Reinforcement learning.** Neural networks are mentioned only as an alternative PDE solver (p. 11).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

> [!warning] Provenance: based on the **preprint** (arXiv 2003.05958v2), not the published original (SIFIN 12, 1150–1200).
> Pagination and final claims may differ. Re-ingest the original when acquired (set `based_on: original`).

All page numbers in this block are preprint pages.

**Carries Kernthesen 2, 3, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 18, 20, 21, 22, 23.**

### What this focus needs beyond the Kernthesen

1. **How excitation enters the control problem.** Self-excitation per side only (Kernthese 3); the
   excitation is driven by the maker's own fills because he is the only liquidity provider
   (Kernthese 2). Hence the flow's future intensity is **policy-dependent**: the control enters the
   intensity multiplicatively via $e^{-k\delta/\sigma}$ and therefore enters the memory. This is the
   opposite convention to [[barzykin-2026-hawkes-driven-otc]], where requests, not fills, drive the
   memory and the forecast is quote-independent. For the project this matters directly: any
   forecast-freezing / Riccati scheme that treats the intensity forecast as an exogenous input is not
   exact in Jusselin's model, because the forecast depends on future quotes (ingester's inference).
2. **Path dependence and how it is made Markov.**
   - *Exact, infinite-dimensional:* state $(P,i,\theta^a,\theta^b)$ with $\theta^j_t(\cdot)\in\Theta^K_t\subset L^1$
     (p. 2), domain made locally compact by Lemma 2.1 (p. 3).
   - *Exact, finite, for $K\in\mathcal{SE}$:* $n$ factors per side, dimension $2n+2$ $(P,i,c^a\in\mathbb R^n,c^b\in\mathbb R^n)$,
     plus time (p. 9). With the price dropped (numerics) the spatial dimension is $2n+1$.
   - *Approximation of the kernel:* Riemann sums of the Bernstein measure, matching $K(0)$ and
     $\lVert K\rVert_1$ (Lemma 3.1, App. F); for the power-law-type example, Riemann sums of a
     Mittag-Leffler-derived density (App. G).
   - *Convergence result:* $U^{K_n}\to U^K$ along converging states (Prop. 3.1, eq. 6) and
     $\delta^{K_n,*}_t\to\delta^{K,*}_t$ a.s. (Prop. 3.2), for $K_n\to K$ in $L^1$ and uniformly on
     $[0,T]$; no rate. Empirically ≈ one order of magnitude of relative error from $n\approx0$ to
     $n\approx1100$ (Fig. 4, p. 14).
3. **HJB and viscosity result (statement + assumptions).** Theorem 2.1 (p. 7): unique viscosity
   solution with polynomial growth on $\mathcal E^K$, equal to the value, optimal feedback (5).
   Assumptions: Kernthese 11. Same result for the lift, Theorem 3.1 (p. 9), with identity
   $U^{K_{\alpha,\gamma}}=U^{\alpha,\gamma}\circ\mathcal R_{\alpha,\gamma}$. Comparison relies on an
   adapted Crandall–Ishii lemma that works because the diffusion is one-dimensional (the price), App. D.
4. **What the "fully consistent numerical method" actually is.** Two different solvers:
   (i) **finite differences** for $n\le2$ (Sect. 4.1: two-exponential kernel, state $(i,c^a_1,c^a_2,c^b_1,c^b_2)$,
   5 spatial dimensions + time; grid not reported); (ii) **branching-diffusion Monte Carlo**
   (Henry-Labordère et al. 2019) for large $n$ (Sect. 4.2, App. H), which requires replacing the
   Hamiltonian by a **second-order polynomial in $D^\alpha U$** and assuming a strong solution
   (p. 35). "Consistent" refers to the convergence chain Prop. 3.1 → Thm 3.1 → Lemma 3.1, not to the
   branching scheme, whose polynomial truncation is not covered by any theorem in the paper.
5. **Hawkes-aware vs Poisson comparison.** Setup and numbers: Kernthese 20 and Figs 1–3. The Poisson
   rate $\mu_0=1$ equals the stationary mean intensity of the true model, $\mu/(1-\lVert K\rVert_1)=0.1/(1-0.9)=1$
   (ingester's computation; the source does not say it was calibrated this way). So, as in Barzykin's
   power-law experiment, the Poisson maker gets the *level* right and misses only the conditioning on
   memory. The stated gains (10% + 10%) do not match the plotted values (≈3% + ≈4%, Fig. 1); see
   Contested.
6. **Closure: where it holds and breaks.** No closure is attempted. Ingester's analysis of why the
   GLFT/BEGV route does not transfer directly here: (a) the objective is risk-neutral with a running
   penalty $g$, not CARA, so the GLFT exponential change of variables that linearises the inventory
   ODE system is not available; (b) the Hamiltonian is GLFT-shaped (Kernthese 8) but with the
   positivity constraint $\delta\ge0$ it is piecewise exponential/linear in the jump; (c) a fill moves
   both $i$ and the memory ($c^j\mapsto c^j+\alpha$), so a quadratic-in-$i$ ansatz would have
   coefficients depending on $c$ and jumping with it — the same transport-jump obstruction Barzykin
   states (his p. 8). The source's own quadratic step (App. H) approximates the Hamiltonian, not the
   value function, and keeps the full lifted state.
7. **Several assets with cross-asset excitation (not discussed by the author; all inference).**
   - The Markov-function construction generalises formally: for $d$ assets and $2d$ order types with a
     matrix of completely monotone kernels $K_{jk}$, the state would be $(P\in\mathbb R^d,\,q\in\mathbb Z^d,\,\theta^{jk})$
     and each fill of type $k$ would shift every $\theta^{jk}$ by $K_{jk}(\cdot-t)$.
   - Lift dimension: with $n$ exponentials per kernel and general decays, $(2d)^2n$ factor states; if all
     kernels share the same decay grid $\gamma$ (as the Bernstein-quadrature construction naturally
     allows) one can carry factors per *source* type, $2dn$ states, since
     $\sum_k\int\alpha^{jk}_ie^{-\gamma_i(t-s)}dN^k_s$ is linear in per-source filters. Total
     $d+2dn$ (+ $d$ prices).
   - The comparison proof's key adaptation (Crandall–Ishii only in the price) extends to a
     $d$-dimensional diffusion with the standard lemma; the local-compactness lemma needs each
     $\lVert K_{jk}\rVert_1>0$ or a per-source counting argument. Neither is checked by the source.
   - The density result (Lemma 3.1) is per scalar kernel and would apply entrywise.
   - The fill-driven excitation convention would make cross-asset excitation *policy-dependent*:
     quoting wide in asset $i$ would reduce flow in asset $j$ through $K_{ji}$. This is a qualitatively
     new channel for the multi-asset problem that a request-driven model does not have.
   - Grid methods are already infeasible at $n>2$ for one asset (p. 11); multi-asset makes the
     exact benchmark a high-dimensional problem for Monte-Carlo, neural or RL solvers.

### Direct quotes (for the draft)

> "However when $N^a$ and $N^b$ are general Hawkes processes $(P,i,N^a,N^b)$ is not Markovian. In order to circumvent this issue we need to consider auxiliary state variables enabling us to work in a Markovian setting." (p. 2)

> "Those three points show that if $K_n$ is close from $K$ then $\delta^{K_n,*}$, which is related to a finite dimensional HJB equation, is good approximation of $\delta^{K,*}$. However when n is large we cannot rely on finite differences methods to compute the feedback control $\delta^{K_n}$ since the dimension of the associated HJB equation is too large." (p. 3)

> "It is important to note that in order to obtain existence of an admissible optimal control we have benefited from the fact that we are dealing with counting processes, whose infinitesimal generators are defined for any finite functions independently of their regularity." (p. 7)

> "The only flaw of this method is that the set $E_n$ is a subset of a vector space of dimension $2n+2$. Hence when n is larger than 2 it is very unlikely that simple finite differences methods can be used to solve numerically (HJB)$_{\alpha,\gamma}$." (p. 11)

> "Moreover we observe in Figure 1 that considering an exponential kernel Hawkes model for the order flows leads to a 10% gain compared with a strategy considering that market order flows is a Poisson process. Using two exponentials leads to another 10% gain." (p. 12)

> "Thought this is not the case for (HJB)$_{\alpha,\gamma}$, in order to implement this method we approximate the generator of the PIDE by a second order polynomial and assume that the approximated PIDE have a strong solution." (p. 35)

### Examples & illustrations (for later drafting)

- Fig. 3 (p. 13): the Poisson maker's value loss is concentrated at extreme inventories (up to ≈25 at
  $i=-10$) and is close to zero near $i=0$ — memory matters most when inventory must be unwound.
- Fig. 4 (p. 14): ≈1100-term exponential approximation of a $t^{-1.1}$-tailed kernel, solved by
  branching Monte Carlo — the only "long-memory" control computed in the paper.
- The lift-dimension count $2n+2$ (p. 9) is the cleanest single-asset baseline for the project's
  multi-asset dimension count.

### Boundary of this focus

The source is single-asset and has only same-side self-excitation driven by the maker's own fills.
Everything above on cross-side or cross-asset excitation, on lift dimensions for $d$ assets and on
why closures fail is the ingester's inference from the model's structure. The only quantitative
Hawkes-vs-Poisson evidence is Figs 1–3 (one parameter set, two exponentials, no regret table), and
its headline percentages are inconsistent with the figure.

### Contested / unclear (flag for reviewer)

- **"10% + 10%" vs Fig. 1.** At $T-t=5$ the curves read ≈107, ≈110, ≈114, i.e. gains of ≈3% and ≈4%.
  Possibly the percentages refer to another quantity or state; the text does not say.
- **Degenerate kernel in Sect. 4.1.** With $\gamma_2=(1,1)$ and $\alpha_2=(0.45,0.45)$ the "two-exponential"
  kernel equals $0.9e^{-t}=K_1$ and $\mu=\mu_1=0.1$, so $\delta^1$ and $\delta^2$ should coincide on
  consistent states. A nonzero $U^{\delta^2}-U^{\delta^1}$ (Fig. 2) suggests a typo in $\gamma_2$ (e.g.
  two distinct decays). Check against the SIFIN version.
- **"Fully consistent".** Holds for the convergence theory; the branching numerics add an
  unanalysed polynomial approximation (p. 35).

## Mentioned entities

- Models: [[avellaneda-stoikov-model]], [[glft-2013-model]] ([[gueant-2013-dealing-inventory-risk]]),
  [[cartea-jaimungal-ricci-model]] ([[cartea-2014-buy-low-sell]]); for later comparison
  [[begv-2021-model]] (not cited by the source).
- Concepts: [[hawkes-process]], [[markov-lift]], [[shadow-price]], [[hamiltonian-quadratic-approximation]],
  [[intensity-forecast]], [[branching-matrix]], [[matrix-riccati-equation]], [[volterra-riccati]], [[regret]].
- Other works (bibkeys): `avellaneda-2008-high-frequency-trading`, `bacry-2016-estimation-slowly-decreasing`,
  `cartea-2015-algorithmic-high-frequency`; not in the library (as far as checked): Abi Jaber 2019
  (lifting Heston), Alfonsi & Blanc 2016, Chen–Wang–Zhang–Zhou (thinned Hawkes, working paper),
  Crandall–Ishii–Lions 1992, Dayri & Rosenbaum 2015, Fleming & Soner 2006, Guéant 2016,
  Henry-Labordère et al. 2019, Hewlett 2006, Huré et al. 2018, Jaisson & Rosenbaum 2016, Lillo &
  Farmer 2004, Madhavan et al. 1997, Touzi 2012, Wyart et al. 2008.

## Connections

- Builds on: [[avellaneda-stoikov-model]], [[glft-2013-model]], [[cartea-jaimungal-ricci-model]] —
  «we extend the works [3, 6, 11]» (p. 2), from Poisson / exponential Hawkes to general completely
  monotone kernels.
- Supports: [[markov-lift]] — the first rigorous lift + convergence result for general-kernel Hawkes
  market making in this wiki (Props 3.1–3.2, Thm 3.1, Lemma 3.1).
- Later works that discuss it (no stance from this source, which predates them):
  [[barzykin-2026-hawkes-driven-otc]] calls it «The closest market-making reference» and departs from
  it by letting requests rather than fills drive the memory (his pp. 2, 8);
  [[bergault-2024-price-aware-automated]] cites it (ref. [25]);
  [[martin-2026-market-making-hawkes]] (Mercer lift + PINN) and
  [[acero-2026-hawkes-structured-networks]] (sum-of-exponentials features, RL) take the same lift
  idea to other solvers — compare their lift dimensions on [[markov-lift]].
- Contrast with the closed-form line: [[begv-2021-model]] / [[bergault-2021-closed-form-approximations]]
  obtain Riccati closures under Poisson flow; this source shows what the exact Hawkes problem looks
  like when no closure is sought.
