---
title: "Barzykin 2026 — Hawkes-Driven OTC Market Making: Volterra–Riccati Approximation"
type: source
created: 2026-10-25
updated: 2026-11-01
status: review
author: llm
bibkey: barzykin-2026-hawkes-driven-otc
depth: deep
tags: [market-making, hawkes, rfq, otc, volterra-riccati, path-dependent-control, single-asset, fx]
relations:
  - target: volterra-riccati
    type: supports
    confidence: extracted
    because: "Source introduces the hierarchy: «We therefore develop a hierarchy of Volterra–Riccati approximations» (p. 1); defined in Sec. 4 (pp. 8–12)."
  - target: intensity-forecast
    type: builds-on
    confidence: extracted
    because: "Reduced state is the forecast curve m_t(u), eq. (19)–(20): «we treat the conditional forecast curve as the economically relevant reduced state» (p. 3)."
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "«The BEGV approximation (Bergault et al. 2021) expands hk locally in the shadow price» eq. (25) (p. 9); used only for the continuation value, quotes from the exact optimizer (p. 10)."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "«Substitution of (25) and (27) into (23), followed by coefficient matching in q, gives a backward Riccati system» (p. 9); scalar (single-inventory) case, eqs. (29)–(31)."
  - target: markov-lift
    type: builds-on
    confidence: extracted
    because: "Exponential lift (45)–(46) is the exact validation benchmark (p. 13), but «A Markovian lift combined with a quadratic approximation in inventory does not remove this difficulty» (p. 8)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "RFQ intensities are «Hawkes processes with general kernels» eq. (7), side- and size-marked (p. 6)."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Kernel-mass matrix B with «spectral radius r(B) < 1» drives the power-law tail result (53) (p. 18) and the experiment B = [[0.55,0.05],[0.05,0.55]], r(B)=0.60 (p. 19)."
  - target: shadow-price
    type: builds-on
    confidence: extracted
    because: "Post-request shadow price eq. (17) (p. 8) and state-feedback shadow price eq. (42)–(43) (p. 12) carry the whole quote rule."
  - target: regret
    type: builds-on
    confidence: extracted
    because: "Accuracy «is reported through paired regret, i.e. the difference between the exact lifted HJB objective and the approximate policy objective» (p. 15); Table 3 (p. 16)."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "«we seek a low-dimensional and interpretable quote rule by combining the conditional Hawkes forecast with the quadratic/Riccati approximation of Bergault et al. (2021)» (p. 2)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Cited as part of «the Hamiltonian framework (Guéant et al. 2013, Guéant 2016, Cartea et al. 2015)» (p. 1)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«This approach originates in dealer models such as Ho–Stoll (1981) and Avellaneda–Stoikov (2008)» (p. 1)."
  - target: cartea-jaimungal-ricci-model
    type: mentions
    confidence: ambiguous
    because: "Source cites Cartea, Jaimungal & Ricci 2018 (SIAM Review, «mutually exciting market-order and book-shape models», p. 2), not the 2014 paper the entity page describes; same authors, related model family."
  - target: jusselin-2021-persistent-order-flow
    type: cites
    confidence: extracted
    because: "«The closest market-making reference is Jusselin (2021), who ... proves existence and uniqueness of a viscosity solution to the associated HJB equation, and develops a consistent numerical approximation» (p. 2); the source offers no error theory of its own (p. 22)."
  - target: martin-2026-market-making-hawkes
    type: cites
    confidence: extracted
    because: "«Martin and Tse (2026) use a Markovian approximation of Hawkes kernels via Mercer's expansion and solve the resulting high-dimensional HJB with a PINN» (p. 2)."
---

# Hawkes-Driven OTC Market Making: Volterra–Riccati Approximation

## Bibliographic Details

Barzykin, Alexander. 2026. *Hawkes-Driven OTC Market Making: Volterra–Riccati Approximation*.
arXiv:2608.02002v2 [q-fin.RM], dated 27 August 2026 (arXiv stamp 25 Aug 2026). 24 pp. Author
affiliation: HSBC, London.

**Read:** arXiv 2608.02002v2. No published version exists. Under the project's preprint
policy this preprint is the original (B1 core work). All page and equation numbers on this page
follow v2. The paper has **no appendices**: pp. 23–24 are the references.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\sigma$, $\gamma$ | mid-price volatility (eq. 6), risk aversion (eq. 14) | $\sigma$, $\gamma$ |
| $\kappa := \tfrac12\gamma\sigma^2$, $\kappa_T$ | running and terminal quadratic penalty (eq. 18; $\ell(q)=\kappa_T q^2$) | no project symbol; equals $\tfrac12\gamma\sigma^2$ |
| $q_t$, $X_t$ | inventory; **cash** in Sec. 3 (eq. 12) but **scalar Hawkes memory** in Sec. 5 (eq. 45) | $q_t$; $X_t$ = cash only. ⚠ source reuses $X_t$ |
| $\delta^{s,k}_t$, $s\in\{b,a\}$ | quote offset per side $s$ and size $z_k$ | $\delta^b,\delta^a$ |
| $f_k(\delta)$ | win probability for an RFQ (sigmoid in the numerics) | $f(\delta)$ |
| $\Lambda^{s,k}_t=\lambda^{s,k}_t f_k(\delta)$ | fill intensity (eq. 10) | ⚠ not the GLFT amplitude $\Lambda$ |
| $\lambda^{s,k}_t$, $\mu^{s,k}$ | RFQ (request) intensity, baseline | $\lambda_t$, $\mu$ |
| $\varphi^{s,k;r,\ell}$, $\Phi$ | kernel entries, matrix kernel | kernel matrix |
| $\mathcal B=\int_0^\infty\Phi$, $r(\mathcal B)$; $\eta=\alpha/\beta$ | kernel-mass matrix, spectral radius; scalar branching ratio | $K$, $\rho(K)$ |
| $\beta$, $\alpha$ | exponential decay, jump of memory (Sec. 5) | $\beta$, $D=\mathrm{diag}(\beta)$ |
| $K$ (source) | **number of size buckets** | ⚠ clashes with project $K$ (branching matrix) |
| $m^{s,k}_t(u)$ | conditional forecast curve (eq. 19) | $m_t(u)$ |
| $\rho_i(u)$ | resolvent forecast response to a type-$i$ RFQ (eq. 22) | ⚠ clashes with $\rho(K)$; no project symbol |
| $h_k(p)$, $h_{k,0},h_{k,1},h_{k,2}$ | per-size Hamiltonian (eq. 16) and its Taylor coefficients (eq. 25) | $H^{i,s}$, $h_2^{i,s}=H''(0)$ |
| $p^s_k$, $\Delta^s_k v$ | shadow price (eq. 17), finite difference (eq. 24) | $p^j$ |
| $v_0(\tau,q;m_t)$; $A_0,B_0,C_0$ | mean VR value; quadratic coefficients (eq. 26) | $\theta(t,q,\lambda)$ (approximate); $A,B,C$ |
| $\Sigma_t(u,v)$ | conditional covariance of future intensities (eq. 34) | ⚠ not the price covariance $\Sigma$ |
| $D_i$, $K_{ij}$ | first/second functional sensitivities of $V_0$ in $m$ (eq. 36) | ⚠ $K_{ij}$ clashes with $K$ |
| $\epsilon_s$, $z_k$ | side sign ($+1$ bid, $-1$ ask), RFQ size | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (Poisson vs Hawkes, non-causal reading of Hawkes, Jusselin 2021, related work, LQ-Volterra precedent) | 1–3 |
| ✓ F1 | 2 Empirical motivation: persistent RFQ activity (activity time, Table 1, Fig. 1) | 3–5 |
| ✓ F1 | 3.1 Request flow and dealer objective (eqs. 6–14) | 5–7 |
| ✓ F1 F2 | 3.2 Path-dependent dynamic program and limits of exact lifting (eqs. 15–18) | 7–8 |
| ✓ F1 F2 | 4.1 Conditional Volterra forecast (eqs. 19–22) | 8–9 |
| ✓ F1 F2 | 4.2 Mean Volterra–Riccati approximation (eqs. 23–32) | 9–10 |
| ✓ F1 F2 | 4.3 Noise-aware second-order correction (eqs. 33–39) | 10–11 |
| ✓ F1 F2 | 4.4 State-feedback stochastic Volterra–Riccati approximation (eqs. 40–44, Fig. 2) | 11–13 |
| ✓ F1 F2 | 5 Exponential Hawkes validation benchmark (eqs. 45–49, Table 2) | 12–14 |
| ✓ F1 F2 | 5.1 Numerical results (eq. 50, Fig. 3, Table 3, Fig. 4) | 14–17 |
| ✓ F1 F2 | 6 Power-law RFQ memory and endogenous OTC impact; 6.1 Linearized RFQ-information impact (eqs. 51–54) | 17–18 |
| ✓ F1 F2 | Numerical experiment (unnumbered; power-law mixture, Figs. 5–7) | 18–21 |
| ✓ F1 F2 | Concluding remarks (unnumbered) | 21–22 |
| — | Acknowledgment, References | 23–24 |

## Kernthesen

### 1. ⭐ Spot-FX RFQ activity is strongly self-exciting and multi-scale even after deseasonalisation (pp. 3–5)

On three years of anonymised HSBC spot-FX RFQs (EURUSD, GBPUSD, USDJPY; >5·10⁵ qualified events
per pair after filtering out small requests < 0.25m and clients with < 1% historical fill ratio,
p. 3), a marked Hawkes model (eq. 2) with a three-exponential unit-mass kernel (half-lives 1, 10,
60 minutes, eq. 3) yields size-weighted branching ratios $\eta$ of 0.862 (USDJPY), 0.895
(GBPUSD), 0.880 (EURUSD) (Table 1, p. 4). «Across all three major pairs, the fitted branching
ratio is consistently high, around 0.86–0.90, even after filtering and activity-time
transformation» (p. 5). The cumulative kernel (Fig. 1, GBPUSD) shows that «a material fraction
persists over economically relevant intraday horizons» (p. 5), which makes the forecast of
future RFQ activity a state variable for a finite-horizon dealer. The data are **two-way
activity only**, not signed flow (p. 3, p. 5).

### 2. Kernels must be estimated in deterministic "activity time", and every rate in the control problem must use the same clock (p. 4)

Calendar time is mapped to activity time $\tau^c(t)=\int_0^t\bar\lambda^c(\theta(u))\,du$ (eq. 1)
using the average intraday profile, so seasonality is not confounded with excitation. The
clock is deterministic, unlike event-time clocks, so the fitted kernel is «an activity-time
predictive memory kernel rather than a wall-clock causal response» (p. 4). Volatility must be
transformed accordingly; the paper does not estimate the transformed volatility and treats
constant volatility in activity time as a separate modelling approximation (p. 4).

### 3. ⭐ The Hawkes fit is a predictive, not a causal, model of RFQ flow (pp. 2, 5, 21–22)

The author refuses a contagion reading: «Correlated RFQs may be reactions to a common
unobserved cause» and, if such variation is omitted from the baseline, «a fitted Hawkes model
may absorb part of it into the excitation kernel and thereby produce a large branching ratio»
(p. 2). «The control problem depends on that conditional forecast, not on a causal
interpretation of its statistical decomposition» (p. 2). This is linked to generalized Langevin
"effective memory" views (Itkin 2026a,b, p. 2, p. 22) and motivates future comparisons with
latent-factor/Cox specifications (p. 22).

### 4. ⭐⭐ Requests, not the dealer's fills, drive the Hawkes memory (p. 6)

«The important modelling convention is that requests, not the dealer's controlled executions,
drive the Hawkes memory» (p. 6). An RFQ is an information event; the quote only controls the
conversion probability. Fills $N^{s,k}$ are controlled thinnings of the request processes
$M^{s,k}$ with intensity $\Lambda^{s,k}_t=\lambda^{s,k}_t f_k(\delta^{s,k}_t)$ (eq. 10). The
convention «prevents the dealer from mechanically controlling future RFQ intensity through their
own fill decisions» (p. 6) and implies that the forecast curve «is independent of the dealer's
future quotes» (p. 9). It can be relaxed for public prints, last-look feedback, relationship
scores or hedging flow, which are deliberately excluded (p. 6).

### 5. The model admits general matrix kernels across sides and sizes, stable when the kernel-mass spectral radius is below one (p. 6)

Intensities (eq. 7): $\lambda^{s,k}_t=\mu^{s,k}(t)+\sum_{r\in\{b,a\}}\sum_{\ell=1}^K\int_0^t\varphi^{s,k;r,\ell}(t-u)\,dM^{r,\ell}_u$.
Kernels «may be exponential, sums of exponentials, power-law-like, cross-exciting or
side-asymmetric», and «stability requires the spectral radius of the matrix of $L^1$ kernel
masses to be less than one» (p. 6). Baselines are deterministic; a stochastic baseline would be
an extra state and is excluded (p. 6). Types are (side, size); there is **one asset**.

### 6. Win-probability regularity gives a finite Hamiltonian with a unique optimizer; numerics use a compact quote set and a sigmoid (p. 6)

Conditions (9): $f_k\in C^2(\mathbb R;(0,1))$, $f_k'<0$, $\lim_{\delta\to\infty}\delta f_k(\delta)=0$,
$\sup f_k f_k''/(f_k')^2<2$. Numerically quotes lie in $[\underline\delta,\bar\delta]$; «For RFQ
markets a sigmoid win probability is often natural» (p. 6). Win probabilities are side-symmetric
«for simplicity» (fn. 2).

### 7. The objective is the risk-adjusted (not CARA) expected mark-to-market (p. 7)

Eq. (14): $\sup_\delta\mathbb E\big[\int_0^T\sum_{s,k}z_k\delta^{s,k}_t\,dN^{s,k}_t-\tfrac12\gamma\int_0^T\sigma^2q_t^2\,dt-\ell(q_T)\big]$,
justified via Cartea et al. (2015) and Guéant (2016) under a martingale mid-price (p. 7).

### 8. ⭐⭐ The exact problem is a deterministic HJB on the history space, splitting information value from conversion value (pp. 7–8)

The state is $(t,q,H)$ with $H$ the marked RFQ history and the intensity a functional
$\lambda^{s,k}(t,H)$ (eq. 15). With the post-request shadow price
$p^s_k=[V(t,q,H\oplus(t,s,k))-V(t,q+\epsilon_sz_k,H\oplus(t,s,k))]/z_k$ (eq. 17), the
path-dependent HJB (eq. 18) is
$0=\partial_tV-\kappa q^2+\sum_{s,k}\lambda^{s,k}(t,H)\big[V(t,q,H\oplus(t,s,k))-V(t,q,H)+z_kh_k(p^s_k)\big]$.
«The first difference inside the brackets is the value effect of observing a request even if it
is not won; the Hamiltonian is the incremental value of optimally converting that request into a
trade» (p. 8). The OTC novelty relative to Jusselin (2021) is that «the history is updated by the
request itself, whereas inventory is updated only by the controlled Bernoulli conversion» (p. 8).

### 9. ⭐⭐ Exact Markov lifting is finite-dimensional only for exponentials and explodes in dimension otherwise (p. 8)

«Equation (18) is the exact control problem, but it is not computationally viable for general
kernels» (p. 8). Sums of exponentials give one state per factor, side and size: «a d-factor
approximation of a two-sided, K-size Hawkes model already introduces 2Kd flow-memory variables
in addition to inventory. A power-law kernel requires either a large exponential mixture or a
genuinely infinite-dimensional Volterra state» (p. 8).

### 10. ⭐⭐ A Markov lift plus a quadratic-in-inventory expansion yields transport-jump equations, not a small Riccati system (p. 8)

«A Markovian lift combined with a quadratic approximation in inventory does not remove this
difficulty because the expansion coefficients remain functions of the entire lifted Hawkes
state. Moreover, RFQ arrivals jump both the inventory and the memory state, producing nonlocal
terms in the coefficient equations. One therefore obtains a system of transport-jump equations in
the memory variables, not a small Riccati system» (p. 8). The same objection is raised against ML
solvers: they may fit a lifted benchmark but give no «transparent low-dimensional quote formula»
(p. 8).

### 11. ⭐ Memory alone does not destroy tractability; nonlinear quote response and controlled jumps do (pp. 3, 8)

In linear-quadratic execution with transient impact (Abi Jaber & Neuman 2025), first-order
conditions lead to Fredholm/Volterra/Riccati–Volterra equations without a lift: «Memory therefore
does not by itself preclude tractable control» (p. 3). Market making differs because «the control
acts through nonlinear quote-response functions and controlled jump intensities; after an RFQ, the
value of a possible inventory jump has to be evaluated under an updated Hawkes forecast. A direct
maximum-principle route therefore does not yield the same closed finite-dimensional structure»
(p. 8).

### 12. ⭐⭐ The economically relevant reduced state is the conditional forecast curve, which solves a deterministic Volterra equation (pp. 3, 8–9)

$m^{s,k}_t(u)=\mathbb E[\lambda^{s,k}_{t+u}\mid\mathcal F_t]$ (eq. 19) satisfies
$m_t(u)=\zeta_t(u)+\int_0^u\Phi(u-v)m_t(v)\,dv$ (eq. 20), with past contribution
$\zeta_t(u)=\mu(t+u)+\int_0^t\Phi(t+u-r)\,dM_r$ (eq. 21). A new type-$i$ request shifts the curve
by the resolvent response $\rho_i(u)=\Phi(u)e_i+\int_0^u\Phi(u-v)\rho_i(v)\,dv$ (eq. 22):
«immediately after observing a type-i request, the forward forecast curve changes from $m_t$ to
$m_t+\rho_i$» (p. 9). A finite lift, when it exists, is «an alternative computational
representation rather than a prerequisite for the control construction» (p. 3).

### 13. ⭐⭐ Level 1 (mean VR) freezes the forecast: a certainty-equivalent, not an HJB and not time-consistent (p. 9)

«the mean Volterra approximation freezes the conditional forecast curve $m_t$ and replaces the
random future RFQ intensity by this deterministic curve» (p. 9). Eq. (23):
$0=\partial_\tau v_0-\kappa q^2+\sum_{s,k}m^{s,k}_t(\tau-t)\,z_kh_k(\Delta^s_kv_0)$, $v_0(T,q)=-\ell(q)$.
«Equation (23) is not claimed to be the HJB equation of the original Hawkes control problem, nor a
time-consistent auxiliary value function as the conditioning time t changes. It is a
certainty-equivalent approximation» (p. 9). Feedback comes only from re-solving: «the forecast
curve and backward Riccati system are recomputed as new information arrives, yielding a
receding-horizon feedback policy» (p. 9). Once $m_t$ is given, neither $\Phi$ nor $M$ appears in
(23).

### 14. ⭐⭐ With the BEGV Hamiltonian expansion and a quadratic ansatz, level 1 closes into a scalar Riccati system with time-varying forecast intensities (pp. 9–10)

Expansion $h_k(p)\approx h_{k,0}+h_{k,1}p+\tfrac12h_{k,2}p^2$ (eq. 25) and ansatz
$v_0\approx-\tfrac12A_0q^2+B_0q+C_0$ (eq. 26) give $\Delta^s_kv_0=\epsilon_sA_0q-\epsilon_sB_0+\tfrac12A_0z_k$ (eq. 27) and, «in representative form»,
$\dot A_0=-2\kappa+A_0^2\sum_{s,k}m^{s,k}_t(\tau-t)z_kh_{k,2}$ (eq. 29),
$\dot B_0=-A_0\sum_{s,k}\epsilon_sm^{s,k}_t(\tau-t)z_k(h_{k,1}+h_{k,2}d_{s,k})$ (eq. 30),
$\dot C_0=-\sum_{s,k}m^{s,k}_t(\tau-t)z_k(h_{k,0}+h_{k,1}d_{s,k}+\tfrac12h_{k,2}d_{s,k}^2)$ (eq. 31),
with $d_{s,k}=-\epsilon_sB_0+\tfrac12A_0z_k$ (eq. 28). «For symmetric side intensities and
penalties the skew coefficient $B_0$ is zero; for directional bursts it becomes the dominant
quote-skew term» (p. 10). The BEGV constant intensities are replaced by the forecast curve
$m_t(\tau-t)$; otherwise the structure is the BEGV one specialised to one asset.

### 15. The Hamiltonian expansion approximates the continuation value only; the quote uses the exact optimizer (pp. 10–12)

$\delta^{s,k}_t=\delta^*_k(\Delta^s_kv_0(t,q_t;m_t))$ (eq. 32): «the Hamiltonian expansion is used
to approximate the continuation value, not to impose a linear quote rule» (p. 10). The same holds
at levels 2 and 3 (pp. 11–12).

### 16. Clean closure needs a quadratic terminal penalty (p. 10, fn. 3)

«The coefficient equations close cleanly when the terminal penalty is quadratic, e.g.
$\ell(q)=\kappa_Tq^2$, with terminal conditions $A_0(T)=2\kappa_T$, $B_0(T)=C_0(T)=0$. If $\ell(q)$
is general then the quadratic ansatz requires a terminal quadratic projection» (fn. 3, p. 10).

### 17. ⭐ Level 2 (noise-aware) adds a functional-delta-method covariance correction, with no sign guarantee (pp. 10–11)

With $\xi_t(u)=\lambda_{t+u}-m_t(u)$ (eq. 33) and $\Sigma_t(u,v)=\mathrm{Cov}_t(\lambda_{t+u},\lambda_{t+v})$ (eq. 34),
a second-order expansion of the deterministic-intensity value map $m\mapsto V_0(t,q;m)$ (eqs. 36–37)
gives $\bar V\approx v_0+\tfrac12\sum_{ij}\iint K_{ij}(t,q;u,v)\Sigma_{t,ij}(u,v)\,du\,dv$ (eq. 38).
«It is not an exact value function and is not claimed to restore a dynamic-programming or
time-consistency property. Its sign is governed by the curvature of the deterministic-intensity
value map with respect to the forecast curve; it is not assumed to be positive in general» (p. 11).
Sensitivities come from differentiating the Riccati system w.r.t. a finite parametrisation of the
forecast curve (p. 11). Level 2 still ignores the post-request forecast update (p. 11).

### 18. ⭐⭐ Level 3 (state feedback) evaluates the continuation value under the post-request forecast — the "information value" of an RFQ (pp. 11–12)

Post-request forecast $m^{i,+}_t=m_t+\rho_i$ (eqs. 40–41); mean state-feedback shadow price
$p^{SF,0}_i\approx[v_0(t,q;m^{i,+}_t)-v_0(t,q+\epsilon_iz_i;m^{i,+}_t)]/z_i$ (eq. 42), linearised as
the mean-forecast shadow price plus
$\tfrac1{z_i}\sum_j\int_0^{T-t}[D_j(t,q;u)-D_j(t,q+\epsilon_iz_i;u)]\rho_{i,j}(u)\,du$ (eq. 43).
«The second term is the incremental information value of the RFQ: the request is not treated only
as a possible inventory jump, but also as a signal that changes the conditional distribution of
future RFQ flow» (p. 12). «It is the main channel through which the approximation closes the gap
to the exact lifted HJB in directional Hawkes regimes» (p. 12). A noise-aware version (eq. 44)
uses $(m^{i,+}_t,\Sigma^{i,+}_t)$, optionally $\Sigma^{i,+}_t\approx\Sigma_t$.

### 19. ⭐ The Riccati control layer is modular in the flow model: it needs only $m_t$, $\Sigma_t$ and $m^{i,+}_t$ (pp. 1, 11–12, 22)

«the mean approximation requires $m_t$, the covariance correction additionally requires $\Sigma_t$,
and state feedback requires the post-request update $m^{i,+}_t$. Hawkes dynamics provide these
objects through the Volterra equation and resolvent, but another exogenous-intensity model could
in principle supply the same conditional inputs» (pp. 11–12; repeated in the abstract, p. 1, and
p. 22).

### 20. The exponential benchmark has an exact 2-D lifted HJB and closed moment ODEs (pp. 12–14)

Unit size $z_1=1$. Scalar memory $dX_t=-\beta X_t\,dt+\sum_s\alpha_s\,dM^s_t$, $\lambda^s_t=\lambda^s(X_t)$
(eq. 45); the memory jumps «irrespective of whether the dealer wins the request» (p. 13). Lifted
HJB (eq. 46):
$0=\partial_tV-\beta x\partial_xV-\kappa q^2+\sum_s\lambda^s(x)\big[V(t,q,x+\alpha_s)-V(t,q,x)+h_1\big(V(t,q,x+\alpha_s)-V(t,q+\epsilon_s,x+\alpha_s)\big)\big]$.
For $\lambda=\mu+X$: $\dot x=\alpha\mu-(\beta-\alpha)x$ (eq. 48), $\dot y=-2(\beta-\alpha)y+\alpha^2(\mu+x)$
(eq. 49), $\eta=\alpha/\beta$. Three regimes (Table 2, p. 14): benign common-mode ($\eta=0.65$),
near-critical common-mode ($\eta=0.92$), directional one-sided ($\eta=0.92$, only the bid side
excited, $\mu^b=5,\mu^a=20$). Grid: $q_{\max}=50$, 1000-point memory grid to $X_{\max}=800$,
$\Delta t=10^{-4}$, sigmoid $f(\delta)=(1+\exp(\delta-1.2))^{-1}$, $\kappa=\kappa_T=0.2$, $2\cdot10^4$
MC paths (p. 15).

### 21. ⭐⭐ State-feedback VR is within ~0.1–0.2% of the exact lifted HJB in all regimes; the memory-free Poisson policy loses 6–27% (pp. 15–16, Table 3)

Relative paired regret (Table 3, p. 16): **Benign** — Poisson 6.138%, Mean VR 0.182%, Noise-aware
0.151%, State-feedback 0.080%. **Near-critical** — Poisson 12.742%, Mean VR 0.884%, Noise-aware
0.513%, State-feedback 0.083%. **Directional** — Poisson 27.312%, Mean VR 2.498%, Noise-aware
2.159%, State-feedback 0.170%. Absolute regrets e.g. directional Poisson $12.617\pm0.119$ vs
state-feedback $0.079\pm0.020$ on an exact objective of $46.20\pm0.10$. Common random numbers
and paired regret are used to remove sampling noise (p. 15).

### 22. ⭐ The Poisson comparator is exactly optimal in its own misspecified model and uses the *baseline* intensities (p. 15)

«we do not use the Riccati approximation for the Poisson policy but rather solve the underlying
exact one-dimensional HJB on the inventory grid» (eq. 50, p. 15). «In the experiments below this
is the baseline intensity of the corresponding side, so the Poisson policy deliberately ignores the
realized Hawkes excitation» (p. 15). Hence «its error is due to model misspecification rather than
to a weak numerical implementation» (p. 16). Note the experiment starts at $X_0=120$ against
baselines $\mu\le20$ (Table 2), so this comparator also under-states the *level* of flow.

### 23. ⭐ Mechanism: in the directional regime only policies that condition on the realized memory reproduce the exact quote skew (pp. 16–17, Fig. 4)

Fig. 4 shows initial-time quotes vs inventory for $X=60,120,240$: exact HJB and state-feedback VR
move with $X$; «The mean Volterra–Riccati policy, on the other hand, does not condition on the
realized value of X» (p. 16). Common-mode excitation «mainly changes the amount of future RFQ
opportunity flow», so mean VR captures much of it; covariance correction helps more near
criticality; in the directional regime «the realized Hawkes memory is itself a control-relevant
state variable» (p. 16).

### 24. ⭐ Quote impact inherits the power-law tail of the RFQ kernel (pp. 17–18)

Linearising (42) around the unperturbed forecast gives the shadow-price impact (eq. 51), a
Volterra filter of the resolvent response; the quote impact is
$\Delta\delta_i\approx(\delta^*_i)'(p^0_i)\,\Delta p_i$ (eq. 52). For a subcritical kernel with
$\Phi(u)\sim C_\Phi u^{-\chi}L(u)$, $\chi>1$, $r(\mathcal B)<1$:
$\rho_i(u)\sim(I-\mathcal B)^{-1}C_\Phi(I-\mathcal B)^{-1}e_iu^{-\chi}L(u)$ (eq. 53), hence
$\Delta\delta_i(t,q)\sim C^{imp}_{i,i_0}(q)\,t^{-\chi}L(t)$ (eq. 54), provided the Riccati
sensitivity kernel is integrable and the horizon is long. «the Volterra–Riccati quote impact has
the same long-lag decay exponent as the conditional RFQ-flow response» (p. 18). The mechanism is
claimed to be forecast-based; only the amplitude formula (53) is Hawkes-specific.

### 25. The power-law experiment is two-sided, size-marked, with weak cross-side excitation and a Poisson comparator calibrated to the stationary mean (pp. 18–20)

Sizes $\{1,2,5\}$ with probabilities $(0.65,0.25,0.10)$; sigmoid $f(\delta)=(1+\exp(3(\delta-1)))^{-1}$,
$\delta^*(0)=0.85$ bp (p. 18). Kernel $\Phi(u)=g_N(u)\mathcal B$, $g_N$ an $N=8$ exponential mixture with
$\beta_n$ log-spaced on $[2,2500]$ and $w_n\propto\beta_n^{-0.65}$, giving $g_N(u)\propto u^{-0.35}$
over an intermediate range; $\mathcal B=\begin{pmatrix}0.55&0.05\\0.05&0.55\end{pmatrix}$,
$r(\mathcal B)=0.60$; $\mu^b=\mu^a=155$, $\bar\lambda=388$/day (p. 19). «we do not solve a lifted HJB in
the exponential factors» (p. 19). The Poisson benchmark «is calibrated to the same stationary side
intensities $\bar\lambda^b=\bar\lambda^a$. Its misspecification is therefore not the unconditional
level of RFQ activity, but the absence of conditioning on the realized Hawkes memory» (p. 19).
$\kappa=2.0$, $\kappa_T=0.01$, $T_{eval}=0.1$ day, burn-in 0.1, continuation horizon 0.1, forecast
grid $N_f=12$, $10^5$ paths, default burst of 50 bid RFQs (pp. 19–20).

### 26. ⭐ Conditioning on RFQ memory mainly reduces inventory and P&L risk, increasingly with burst size (pp. 20–21, Figs. 6–7)

After a bid burst, the Poisson dealer drifts to a mean inventory of ≈2.4 while the VR dealer stays
near zero, and RMS inventory is lower (Fig. 6, p. 20). «This is the most robust economic effect in
the experiment: conditioning on the RFQ memory primarily improves inventory-risk control» (p. 20).
Relative P&L-std reduction $1-\mathrm{StDev}(P\&L_{VR})/\mathrm{StDev}(P\&L_{Poisson})$ rises from
≈3% (burst 0–10) to ≈8% (50) and ≈19% (100) (Fig. 7, read off the plot, p. 21). «Mean P&L
differences are less stable and are not the main message» (p. 20). No regret against an optimum is
reported here, because no exact benchmark exists (p. 21).

### 27. RFQ memory gives an endogenous OTC market-impact mechanism, distinct from inventory-based impact (pp. 17, 20–21)

«quote impact is generated endogenously by optimal conditioning on RFQ information, rather than
being imposed as an exogenous price-impact function» (p. 17). It is framed as an OTC version of
Jaisson (2015) and consistent with Jusselin & Rosenbaum (2020), Muhle-Karbe et al. (2026) and
Eisler & Bouchaud (2016), and «complementary to, the inventory-based impact of a trade (Barzykin
2026)» (p. 21) — i.e. `barzykin-2026-market-making-transient`.

### 28. No well-posedness or convergence theory is offered; validation is numerical (pp. 14, 22)

«We do not pursue a general well-posedness theorem for the full path-dependent Hawkes control
problem» (p. 14). «A frozen conditional forecast does not satisfy an intertemporal
dynamic-programming principle … a general error or convergence theory remains open» (p. 22);
pseudo-chaotic expansions (Hillairet & Réveillac 2024) are suggested as a route (p. 22).

### 29. Production use would require a directional-flow filtering layer and richer coupled point processes (p. 22)

Limitations: (i) directionality of two-way RFQs is «a statistical filtering problem, not an
assumption that can be taken for granted» (p. 22); (ii) win probabilities do not depend on Hawkes
memory, while in stress competition, urgency, toxicity or last look may shift them; (iii) fills,
hedging and public-market signals should form «a coupled marked point process or Volterra system»
(p. 22). Exact DP for such enriched models «is unlikely to be feasible» (p. 22).

### 30. Relation to Jusselin (2021) and the wider Hawkes-MM literature (pp. 2–3, 8)

Jusselin 2021 (`jusselin-2021-persistent-order-flow`) is «The closest market-making reference»:
general Hawkes market-order flow, viscosity solution of the path-dependent HJB, consistent
numerics (p. 2). This paper differs by the OTC request/conversion split and by seeking «a
low-dimensional and interpretable quote rule» rather than approximating the full value function
(p. 2). [[martin-2026-market-making-hawkes]] is cited for Mercer-expansion Markov approximation
solved by PINN; [[bergault-2024-price-aware-automated]] for the point that «when order-flow states
jump together with inventory, exact dynamic programming becomes high-dimensional» (p. 2).

### 31. ⭐ A finite exponential mixture with power-weighted, log-spaced decay rates imitates a power law only over an intermediate range; kernel, forecast grid and simulation step are three separate discretisations (pp. 18–20)

*Added 2026-11-01 (second focus pass).* The long-memory kernel of §6.2 is built as
$\Phi(u)=g_N(u)\mathcal B$, $g_N(u)=\sum_{n=1}^Nw_n\beta_ne^{-\beta_nu}$, $\sum_nw_n=1$, so that
$\mathcal B$ is the kernel-mass matrix (p. 18), with $\beta_n$ log-spaced and
$w_n=\beta_n^{-\nu_{\rm mix}}/\sum_{\ell}\beta_\ell^{-\nu_{\rm mix}}$ (p. 19). On a log grid the sum
approximates $C\int\beta^{-\nu_{\rm mix}}e^{-\beta u}d\beta\propto u^{-(1-\nu_{\rm mix})}$: «This
construction allocates more mass to slower factors and makes the finite mixture behave like a
slowly decaying power law over the relevant intraday range» (p. 19). The author bounds the claim
himself: «Since the mixture is finite, the power-law behaviour should be read as an
intermediate-range approximation: the fastest exponential creates a short-time cut-off and the
slowest exponential eventually dominates at very long lags» (p. 19). He keeps three numerical
resolutions apart — the forecast grid $N_f=12$ «is distinct from both the Monte Carlo time step
∆t and the N = 8 exponential factors used to represent the Hawkes kernel» (p. 20) — but reports
no accuracy figure for any of them, and no result for another $N$.

## Figures and tables

- Table 1 (p. 4): Hawkes estimates per FX pair ($\eta$, $w_1,w_{10},w_{60}$).
- Fig. 1 (p. 5): cumulative RFQ kernel mass, GBPUSD, lag 0–200 min.
- Fig. 2 (p. 13): diagram of the approximation hierarchy (mean → noise-aware → state-feedback; Poisson and exact lifted HJB as comparators).
- Table 2 (p. 14): parameters of the three exponential regimes.
- Fig. 3 (p. 15): relative paired regret (log scale) per policy and regime.
- Table 3 (p. 16): objectives, absolute and relative regrets.
- Fig. 4 (p. 17): ask and minus-bid offsets vs inventory at $X=60,120,240$ (exact, state-feedback, mean VR).
- Fig. 5 (p. 19): conditional imbalance after a burst (log-log, slope −0.35) and RFQ quote impact.
- Fig. 6 (p. 20): mean and RMS inventory paths, VR vs Poisson.
- Fig. 7 (p. 21): relative P&L-std reduction vs burst size (0–100).

No figures extracted to `knowledge/assets/` in this pass (write scope limited to this page).

## What this source does not address

- **More than one asset.** The model has a single inventory $q$; "multi" in the paper means
  sides × size buckets. Cross-asset excitation, a matrix $A$ and portfolio risk are not discussed
  anywhere (the empirical part fits each FX pair separately, p. 4). For the multi-asset closed form
  see [[begv-2021-model]]; for multi-asset Hawkes with network structure see
  [[acero-2026-hawkes-structured-networks]].
- **Fill-driven (self-inflicted) excitation.** Excluded by construction (p. 6); flagged as future
  work (p. 22).
- **CARA utility.** Only the risk-adjusted objective (eq. 14).
- **Exact solution for non-exponential kernels and RL.** No grid-lifted benchmark for the power-law
  case (p. 21) and no RL policy; for a neural-PDE treatment of the lifted HJB see
  [[martin-2026-market-making-hawkes]]; for a general path-dependent viscosity treatment see
  `jusselin-2021-persistent-order-flow`.
- **Theory of approximation error.** No bounds or convergence results (p. 22).
- **Price dynamics coupled to flow.** Mid-price is Brownian and independent of RFQs (eq. 6).
- **Signed empirical flow.** Data are two-way activity; no signed kernel is estimated (p. 5).
- **The number of memory factors as a variable** *(added 2026-11-01)*. One exponential in §5, eight
  fixed in §6.2; no kernel-, forecast- or value-error is reported against the number of factors
  (pp. 13, 18–20). A regret bound in the number of factors via the kernel $L^2$ error is
  [[acero-2026-hawkes-structured-networks]]'s subject (Thm. 1); value convergence under kernel
  $L^1$ error, without a rate in the number of exponentials, is
  [[khabou-2025-markov-approximation-hawkes]]'s.

## Model card

| Field | Theory (§§3–4) | §5 exponential benchmark | §6.2 power-law-like experiment |
|---|---|---|---|
| Assets | 1 (types = side × size bucket) | 1, unit size $z=1$ | 1, sizes $\{1,2,5\}$ |
| Kernel | general matrix kernel $\Phi$, eq. (7): exponential, sum-of-exp, power-law-like, cross-exciting, side-asymmetric | one exponential, $\alpha e^{-\beta u}$ (eq. 45) | 8-exponential mixture $g_N(u)\mathcal B$, $\beta_n$ log-spaced on $[2,2500]$, $w_n\propto\beta_n^{-0.65}$ (pp. 18–19) |
| Excitation | self, cross-side, cross-size all allowed | common-mode ($\alpha_b=\alpha_a=\alpha$, one shared memory) or directional (bid self-excitation only) | self 0.55 + cross-side 0.05 via $\mathcal B$, $r(\mathcal B)=0.60$ |
| Who excites the flow | all requests (RFQs), not the dealer's fills (p. 6) | same; memory jumps «irrespective of whether the dealer wins the request» (p. 13) | same |
| Objective | risk-adjusted, eq. (14); $\kappa=\tfrac12\gamma\sigma^2$, $\ell(q)=\kappa_Tq^2$ | $\kappa=\kappa_T=0.2$ | $\kappa=2.0$, $\kappa_T=0.01$ |
| Fill model | win probability $f_k(\delta)$ with conditions (9); sigmoid in the numerics | $f(\delta)=\{1+\exp(\delta-1.2)\}^{-1}$ | $f(\delta)=\{1+\exp(3(\delta-1))\}^{-1}$ |
| Solution method | Volterra–Riccati hierarchy: forecast (20)–(22) → BEGV-quadratic scalar Riccati (29)–(31) → exact optimizer (32); receding horizon; levels 2–3 add (38), (42)–(44) | exact lifted HJB (46) on a $(q,x)$ grid; Poisson 1-D HJB (50); VR levels 1–3 | state-feedback VR only; «we do not solve a lifted HJB in the exponential factors» (p. 19) |
| Benchmark | n/a — no error theory (p. 22) | exact lifted HJB (46) | Poisson HJB calibrated to $\bar\lambda^b=\bar\lambda^a=388$/day only |
| Reported regret / gap | n/a | Table 3 relative regret (benign / near-critical / directional): state-feedback VR 0.080 / 0.083 / 0.170 %; mean VR 0.182 / 0.884 / 2.498 %; Poisson 6.138 / 12.742 / 27.312 % | no regret; relative P&L-std reduction vs Poisson ≈ 3 % → 19 % as the burst grows 0 → 100 RFQs (Fig. 7, read off the plot) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 4, 5, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 25.**

### What this focus needs beyond the Kernthesen

1. **Status of the exact (lifted) HJB.** For general kernels the exact object is the
   history-space HJB (18), stated only "formally" with no well-posedness claim (pp. 8, 14). For the
   one-factor exponential case the lift (46) is exact, 2-D in $(q,x)$, and solved on a grid; it is
   the only ground truth in the paper (pp. 13–14). For the power-law case no exact solution is
   computed (p. 19, p. 21).
2. **Exactly where the closure becomes approximate.** Three separate steps, in order: (a)
   *forecast freezing* — replacing the random intensity by the deterministic curve $m_t$ in (23)
   is the step that leaves the true HJB and loses time consistency (p. 9); (b) *Hamiltonian
   expansion* (25) plus quadratic ansatz (26) — the BEGV step that turns (23) into the Riccati
   system (29)–(31) (pp. 9–10), exact only for a quadratic $\ell$ (fn. 3); (c) the *covariance
   correction* (38) is itself a second-order perturbative patch on (a), not a restoration of
   exactness (p. 11). State feedback (42) reduces the cost of (a) by re-conditioning on the
   post-request forecast. Given $m_t$, the inner backward system is a genuine (scalar,
   time-inhomogeneous) Riccati ODE; the approximation lives in (a) and (b), not in solving it.
3. **Lift + quadratic does not close.** The paper's explicit claim (p. 8, Kernthese 10): with a lift,
   $A,B,C$ become functions of the lifted memory and RFQ jumps shift both $q$ and memory, giving
   transport-jump PDEs in the memory variables. The VR construction avoids this by making the
   coefficients depend on a *parameter* ($m_t$) rather than on a *state* (p. 9).
4. **Multi-asset / cross-asset extension: not discussed by the author.** No sentence of the paper
   addresses several assets (verified by full-text search). What *is* already multi-type: the
   matrix kernel over (side, size) types (eq. 7), the vector Volterra equation (20) and resolvent
   (22), and a cross-side $\mathcal B$ in the experiment (p. 19). *Inference (not the author's):*
   the forecast layer (19)–(22) carries over unchanged if types become (asset, side, size) and
   $\Phi$ gains cross-asset blocks, so a cross-asset burst would enter through $\rho_i$; the Riccati
   layer would become the BEGV matrix Riccati with $A$ a $d\times d$ matrix and intensities replaced
   by $m^{j,s}_t(\tau-t)$; the state-feedback term (43) would then transmit a burst in asset $i$ into
   the shadow prices of asset $j$ via $D_j$ and the cross-asset components of $\rho_i$. Whether
   the "lift + quadratic → transport-jump" obstruction becomes worse with $d$ (lift dimension
   grows with $d$ × sides × factors) is implied by p. 8 but not quantified.
5. **Who excites the flow and why it matters for closure.** Because requests, not fills, excite,
   $m_t$ is quote-independent (p. 9); that is what allows freezing $m_t$ as an exogenous input to a
   Riccati system. With fill-driven excitation the forecast would depend on the policy and this
   decoupling would fail (inference; the author only notes the convention «prevents the dealer from
   mechanically controlling future RFQ intensity», p. 6).

### Direct quotes (for the draft)

> "A Markovian lift combined with a quadratic approximation in inventory does not remove this difficulty because the expansion coefficients remain functions of the entire lifted Hawkes state. Moreover, RFQ arrivals jump both the inventory and the memory state, producing nonlocal terms in the coefficient equations. One therefore obtains a system of transport-jump equations in the memory variables, not a small Riccati system." (p. 8)

> "Equation (23) is not claimed to be the HJB equation of the original Hawkes control problem, nor a time-consistent auxiliary value function as the conditioning time t changes. It is a certainty-equivalent approximation to the continuation value conditional on the information available at time t." (p. 9)

> "The second term is the incremental information value of the RFQ: the request is not treated only as a possible inventory jump, but also as a signal that changes the conditional distribution of future RFQ flow." (p. 12)

> "In this paper the Hawkes specification is therefore used primarily as a predictive model for the conditional distribution of future RFQ flow. The control problem depends on that conditional forecast, not on a causal interpretation of its statistical decomposition." (p. 2)

> "Thus the Poisson dealer is optimal within their own misspecified memory-free model, but their quotes depend only on time and inventory, not on the realized Hawkes memory." (p. 15)

### Examples & illustrations (for later drafting)

- Directional regime, Table 3 (p. 16): Poisson 27.312% vs mean VR 2.498% vs noise-aware 2.159% vs
  state-feedback 0.170% relative regret — a clean ladder showing which approximation step matters.
- Fig. 4 (p. 17): quote skew moving with realized memory $X$ for exact and state-feedback, flat for
  mean VR — the visual argument that memory is a control state.
- Fig. 6 (p. 20): after a 50-RFQ bid burst the Poisson dealer's mean inventory peaks near 2.4 while
  the VR dealer stays near 0.

### Boundary of this focus

The paper is single-asset; everything said here about several assets with cross-asset excitation
is the project's inference from the type-indexed structure, not a claim of the source. Regret
numbers exist only for the one-factor exponential benchmark with unit size; the power-law
experiment reports risk reduction against Poisson, not regret against an optimum.

## Focus: p-sweep / error theory: how many exponential memory factors p a market maker needs under power-law or long-memory Hawkes flow — what the source reports about value, reward or regret as a function of p or of the kernel/forecast approximation error; which error or convergence theory it offers (rates, exponents, constants, conditions such as subcriticality); which functional of the flow history the optimal quote depends on; and which parameters and equations a reproduction needs. — 2026-11-01

**Carries Kernthesen 9, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 28, 31.**

Read for `input/ideas/lai2023-gaps-and-memory-plan.md`, Task 2 (novelty check, stop rule) and
Task 4 (reproduction inputs); recorded only, the plan is not changed. **Pages:** the printed page
number equals the physical PDF page throughout (checked pp. 1, 9–16, 18–23). All numbers in the
parameter tables and Table 3 were read off the page images (pp. 9–11, 13–16, 18–22), not only
from pdftotext. Equation numbers are the source's (arXiv v2). **Section numbering:** the PDF
numbers the power-law experiment **§6.2** (p. 18) and the conclusion **§7** (p. 21); the section
map above lists both as "unnumbered".

### What this focus needs beyond the Kernthesen

1. **p is never swept.** §5 has exactly one exponential (scalar memory $X_t$, eq. 45, p. 13); §6.2
   fixes $N=8$ (pp. 18–19). The only quantity varied in §6.2 is the burst size (Fig. 7, p. 21);
   across §5 the regimes change $\eta$, $\mu$ and $\beta$ together (Table 2), so not even $\eta$ is
   swept cleanly. No kernel error, forecast error, value, reward or regret is reported as a
   function of the number of factors anywhere. The only statement about factor count is a
   dimension count (p. 8, quote below).
2. **No error or convergence theory**: no rates, exponents or constants (pp. 14, 22, quotes below).
   The only conditions stated are stability, «the spectral radius of the matrix of $L^1$ kernel
   masses to be less than one» (p. 6), and, for the impact-tail result (53)–(54) only, $r(\mathcal
   B)<1$, a power-law tail with exponent $\chi>1$, an integrable Riccati sensitivity kernel and a
   long continuation horizon (p. 18). These concern the decay of quote impact, not approximation
   error.
3. **No exact or near-exact reference for long memory; the comparator is Poisson only.** «we do not
   solve a lifted HJB in the exponential factors» (p. 19); «In the present power-law case, an exact
   lifted benchmark is not available at comparable complexity» (p. 21). §6.2 reports no objective,
   no regret, no SE — only Figs. 5–7.
4. **$K_{ij}$ is a covariance-correction kernel, not a regret kernel.** It is defined in (36) as the
   second functional derivative of the *optimal* deterministic-intensity value map $\mathcal V_0$
   and is used only in (37)–(38), contracted with the conditional covariance $\Sigma_t$ of
   intensity *noise* around a *correct* forecast (p. 11). The source states no formula for the loss
   of a policy fed a *mis-specified* forecast. *Inference (project, for plan Task 6):* by the
   envelope argument the second-order loss of using $\hat m$ when $m$ is true has kernel
   $K-\partial^2_mJ\vert_{\pi\,\text{fixed}}$ (value Hessian minus the fixed-policy curvature in
   $m$), which equals $K$ only if a fixed policy's value is linear in $m$.
5. **The §6.2 "power law" is $u^{-0.35}$-like over an intermediate range and exponential beyond.**
   The heuristic exponent is $1-\nu_{\rm mix}=0.35<1$ (p. 19, Fig. 5); the asymptotic tail is
   $e^{-2u}$ (slowest $\beta_n=2$). So the kernel lies neither in the regime of (53) ($\chi>1$) nor
   in the plan's grid ($b\in\{1.15,\dots,1.8\}$). *Inference; the numbers in section E below are
   project computations from the stated recipe.*

### A. Notation map for this focus (source → project / plan)

| Source | Meaning | Project / plan |
|---|---|---|
| $\lambda^{s,k}_t$, $\mu^{s,k}(t)$ | request intensity, deterministic baseline (constant in numerics, p. 6) | $\lambda_t$, $\mu$ |
| $\Phi(u)$ | matrix kernel over (side, size); §5: $\alpha e^{-\beta u}$; §6.2: $g_N(u)\mathcal B$ | kernel $g$ (plan) |
| $\eta=\alpha/\beta$ (§5); $r(\mathcal B)$ (§6.2) | scalar branching ratio; spectral radius of kernel masses | $\rho=\lVert g\rVert_1$ (plan) |
| $\rho_i(u)$ | resolvent response to one type-$i$ request (eq. 22) | ⚠ **not** the plan's $\rho$; write $R(u)e_i$ |
| $N$ (§6.2), $d$ (p. 8) | number of exponential factors | $p$ |
| $\beta_n$, $w_n$, $\nu_{\rm mix}$ | factor decays, weights, weight exponent | $\beta_j$, lift weights; $b\approx1-\nu_{\rm mix}$ over the intermediate range only |
| $m_t(u)$, $m^{i,+}_t(u)$ | forecast curve, post-request forecast | $m_t(u)$ |
| $\mathcal V_0(t,q;m)$, $D_i$, $K_{ij}$ | value map of the frozen-forecast Riccati system, its first and second functional derivatives (eq. 36) | $K(u,v)$ in plan H1; ⚠ source also uses $K$ for the number of size buckets |
| $\kappa=\tfrac12\gamma\sigma^2$, $\kappa_T$ | running and terminal quadratic penalty | $\gamma$, $\sigma$ (never given separately) |

### B. The forecast curve $m_t(u)$ (§4.1, eqs. 19–22, pp. 8–9; §4.4, eqs. 40–41, p. 11)

$$m^{s,k}_t(u)=\mathbb E\big[\lambda^{s,k}_{t+u}\mid\mathcal F_t\big],\qquad u\ge0 \tag{19}$$

$$m_t(u)=\zeta_t(u)+\int_0^u\Phi(u-v)\,m_t(v)\,dv \tag{20}$$

$$\zeta_t(u)=\mu(t+u)+\int_0^t\Phi(t+u-r)\,dM_r \tag{21}$$

$$\rho_i(u)=\Phi(u)e_i+\int_0^u\Phi(u-v)\,\rho_i(v)\,dv \tag{22}$$

$$m^{i,+}_t(u)=\mathbb E\big[\lambda_{t+u}\mid\mathcal F^{i,+}_t\big],\qquad m^{i,+}_t(u)=m_t(u)+\rho_i(u) \tag{40–41}$$

- **Conditioning:** on $\mathcal F_t$ (eq. 19); $\mathcal F^{i,+}_t$ = information immediately after a
  type-$i$ RFQ at $t$ (p. 11). $m_t$ is a vector over side-size types (p. 9).
- **Integration variables:** in (20) the future lag $v\in[0,u]$; in (21) past request times
  $r\in[0,t]$ against the counting vector $M$ (history starts at $0$).
- **Kernel:** the full matrix kernel $\Phi$ (all side-size cross-excitations).
- **Baseline:** included — $m_t$ is the full conditional intensity, baseline $\mu(t+u)$ enters via
  $\zeta_t$ (21). Not the excess intensity.
- **Quote independence:** «This forecast is independent of the dealer's future quotes because
  quotes thin requests into executions but do not create requests» (p. 9).
- **Resolvent:** the source does not name a resolvent matrix; (22) says $\rho_i=Re_i$ with
  $R=\Phi+\Phi*R$, hence $m_t=\zeta_t+R*\zeta_t$ (project rewriting, not in the source).
- **Discretisation in the numerics.** §5: none — «Since the Hawkes memory is one-dimensional in
  this validation experiment, the conditional forecast curve is represented by the current memory
  state $X_t$» (p. 15). §6.2: «discretised with $N_f=12$ future-lag grid points» (p. 20) on the
  solver horizon $T_{\rm eval}+T_{\rm cont}=0.2$; **not stated:** the placement of the 12 points,
  the quadrature for (20), and whether $\zeta_t$ is computed from the 8×2 exponential factor
  states or by direct summation over the history.
- **Closed forms for testing a Volterra solver** (project, derived from (45), (48)): one-sided
  exponential $\Phi(u)=\alpha e^{-\beta u}$ gives $\rho(u)=\alpha e^{-(\beta-\alpha)u}$ and
  $m_t(u)=\frac{\mu}{1-\eta}+\big(X_t-\frac{\eta\mu}{1-\eta}\big)e^{-\beta(1-\eta)u}$. Note that §5
  starts from $X_0=120$, an initial memory that an empty history in (21) cannot produce; a Volterra
  reproduction must add $X_0e^{-\beta(t+u)}$ to $\zeta_t$ (inference).

### C. Riccati layer, levels 1–3 (eqs. 16, 23–44, pp. 7–12)

Hamiltonian $h_k(p)=\sup_{\delta}f_k(\delta)(\delta-p)$ (16), optimizer $\delta^*_k(p)$; on a
compact quote set the sup is over $A=[\underline\delta,\bar\delta]$ (p. 8). $\kappa:=\tfrac12\gamma\sigma^2$.

**Level 1 — mean VR** (p. 9), for $\tau\in[t,T]$:

$$0=\partial_\tau v_0(\tau,q)-\kappa q^2+\sum_{s,k}m^{s,k}_t(\tau-t)\,z_k\,h_k\big(\Delta^s_kv_0(\tau,q)\big),\qquad v_0(T,q;m_t)=-\ell(q) \tag{23}$$

$$\Delta^s_kv(\tau,q)=\frac{v(\tau,q)-v(\tau,q+\epsilon_sz_k)}{z_k} \tag{24}$$

$$h_k(p)\approx h_{k,0}+h_{k,1}p+\tfrac12h_{k,2}p^2 \tag{25}$$

$$v_0(\tau,q;m_t)\approx-\tfrac12A_0(\tau)q^2+B_0(\tau)q+C_0(\tau) \tag{26}$$

$$\Delta^s_kv_0(\tau,q)=\epsilon_sA_0(\tau)q-\epsilon_sB_0(\tau)+\tfrac12A_0(\tau)z_k \tag{27}$$

$$d_{s,k}(\tau)=-\epsilon_sB_0(\tau)+\tfrac12A_0(\tau)z_k \tag{28}$$

$$\dot A_0(\tau)=-2\kappa+A_0(\tau)^2\sum_{s,k}m^{s,k}_t(\tau-t)\,z_k\,h_{k,2} \tag{29}$$

$$\dot B_0(\tau)=-A_0(\tau)\sum_{s,k}\epsilon_s\,m^{s,k}_t(\tau-t)\,z_k\big(h_{k,1}+h_{k,2}d_{s,k}(\tau)\big) \tag{30}$$

$$\dot C_0(\tau)=-\sum_{s,k}m^{s,k}_t(\tau-t)\,z_k\Big(h_{k,0}+h_{k,1}d_{s,k}(\tau)+\tfrac12h_{k,2}d_{s,k}(\tau)^2\Big) \tag{31}$$

Terminal values for $\ell(q)=\kappa_Tq^2$: $A_0(T)=2\kappa_T$, $B_0(T)=C_0(T)=0$ (fn. 3, p. 10).
Quote map:

$$\delta^{s,k}_t=\delta^*_k\big(\Delta^s_kv_0(t,q_t;m_t)\big) \tag{32}$$

The author calls (29)–(31) «the representative form» (p. 10); substituting (25)–(27) into (23) and
matching $q^2$, $q$, $1$ (with $\epsilon_s^2=1$) reproduces them exactly (project check). The form of
(25) implies expansion at $p=0$; the numerical values of $h_{k,0},h_{k,1},h_{k,2}$ are not reported.
Re-solve rule: «the forecast curve and backward Riccati system are recomputed as new information
arrives, yielding a receding-horizon feedback policy» (p. 9); the re-solve frequency used in the
numerics (per event or per $\Delta t$) is **not stated**.

**Level 2 — noise-aware** (pp. 10–11):

$$\xi_t(u)=\lambda_{t+u}-m_t(u) \tag{33}$$
$$\Sigma_t(u,v)=\mathrm{Cov}_t(\lambda_{t+u},\lambda_{t+v}),\qquad \Sigma_{t,ij}(u,v)=\mathbb E_t[\xi_{t,i}(u)\xi_{t,j}(v)] \tag{34–35}$$

$$D_i(t,q;u)=\frac{\delta\mathcal V_0(t,q;m)}{\delta m_i(u)}\Big|_{m=m_t},\qquad K_{ij}(t,q;u,v)=\frac{\delta^2\mathcal V_0(t,q;m)}{\delta m_i(u)\,\delta m_j(v)}\Big|_{m=m_t} \tag{36}$$

$$\mathcal V_0(t,q;m_t+\xi_t)\approx v_0(t,q;m_t)+\sum_i\int_0^{T-t}D_i(t,q;u)\xi_{t,i}(u)\,du+\frac12\sum_{i,j}\int_0^{T-t}\!\!\int_0^{T-t}K_{ij}(t,q;u,v)\xi_{t,i}(u)\xi_{t,j}(v)\,du\,dv \tag{37}$$

$$\bar V(t,q)\approx v_0(t,q;m_t)+\frac12\sum_{i,j}\int_0^{T-t}\!\!\int_0^{T-t}K_{ij}(t,q;u,v)\,\Sigma_{t,ij}(u,v)\,du\,dv \tag{38}$$

$$\bar p_i(t,q)=\frac{\bar V(t,q)-\bar V(t,q+\epsilon_iz_i)}{z_i},\qquad \delta_i(t,q)=\delta^*_i(\bar p_i(t,q)) \tag{39}$$

$\mathcal V_0(t,q;m)$ is «the value obtained by solving the mean Volterra–Riccati system on $[t,T]$
with forecast curve $m$» (p. 10), assumed twice functionally differentiable near $m_t$. How $D,K$
are computed: «by differentiating the Riccati system with respect to a finite-dimensional
parametrization of the forecast curve. In an exponential Markovian benchmark, the same quantities
can equivalently be obtained by differentiating the lifted Riccati coefficients with respect to
the Hawkes memory state» (p. 11). **Not stated:** the parametrisation used, and how the two-time
covariance $\Sigma_t(u,v)$ is computed (only the one-time variance ODE (49) is given).

**Level 3 — state feedback** (p. 12):

$$p^{SF,0}_i(t,q)\approx\frac{v_0(t,q;m^{i,+}_t)-v_0(t,q+\epsilon_iz_i;m^{i,+}_t)}{z_i} \tag{42}$$

$$p^{SF,0}_i(t,q)\approx\Delta_iv_0(t,q;m_t)+\frac1{z_i}\sum_j\int_0^{T-t}\big[D_j(t,q;u)-D_j(t,q+\epsilon_iz_i;u)\big]\rho_{i,j}(u)\,du \tag{43}$$

$$p^{SF}_i(t,q)\approx\frac{\bar V(t,q;m^{i,+}_t,\Sigma^{i,+}_t)-\bar V(t,q+\epsilon_iz_i;m^{i,+}_t,\Sigma^{i,+}_t)}{z_i} \tag{44}$$

Quote $\delta_i=\delta^*_i(p^{SF}_i)$, or $\delta^*_i(p^{SF,0}_i)$ in the mean version (p. 12).
**Not stated:** whether the "State-feedback VR" row of Table 3 is (42) or (44), and whether
$\Sigma^{i,+}_t\approx\Sigma_t$ was used.

### D. Exact lifted HJB (§5, eqs. 45–47, p. 13) and Poisson HJB (eq. 50, p. 15)

$$dX_t=-\beta X_t\,dt+\sum_{s\in\{b,a\}}\alpha_s\,dM^s_t,\qquad \lambda^s_t=\lambda^s(X_t) \tag{45}$$

$$0=\partial_tV(t,q,x)-\beta x\,\partial_xV(t,q,x)-\kappa q^2+\sum_s\lambda^s(x)\Big[V(t,q,x+\alpha_s)-V(t,q,x)+h_1\big(V(t,q,x+\alpha_s)-V(t,q+\epsilon_s,x+\alpha_s)\big)\Big] \tag{46}$$

$$V(T,q,x)=-\ell(q) \tag{47}$$

$$0=\partial_tV^P(t,q)-\kappa q^2+\sum_s\bar\lambda^s(t)\,h_1\big(V^P(t,q)-V^P(t,q+\epsilon_s)\big),\qquad V^P(T,q)=-\ell(q) \tag{50}$$

- **State:** $(t,q,x)$, unit size; memory jumps $x\to x+\alpha_s$ on every request, inventory only
  on a win (p. 13). Directional: $\alpha_b=\alpha$, $\alpha_a=0$, $\lambda^b(x)=\mu^b+x$,
  $\lambda^a(x)=\mu^a$ (p. 13). Common-mode: $\alpha_b=\alpha_a=\alpha$ (p. 13); **$\lambda^s(x)$ is
  not stated.** With $\lambda^s(x)=\mu^s+x$ on both sides the memory would mean-revert at
  $\beta-2\alpha<0$ (8 − 10.4; 10 − 18.4), i.e. explode, contradicting $\eta=\alpha/\beta<1$; a reading
  consistent with Table 2 is $\lambda^s(x)=\mu^s+x/2$ (inference, to be confirmed against Table 3's
  exact objectives 42.46 and 48.80).
- **Moment ODEs** (one-sided, $\lambda_t=\mu+X_t$): $\dot x_t=\alpha\mu-(\beta-\alpha)x_t$ (48),
  $\dot y_t=-2(\beta-\alpha)y_t+\alpha^2(\mu+x_t)$ (49), $x_t=\mathbb E[X_t\mid X_0]$,
  $y_t=\mathrm{Var}(X_t\mid X_0)$ (p. 14).
- **Grids (p. 15):** $T=1$ day, $\Delta t=10^{-4}$; integer inventory grid, $q_{\max}=50$; 1000-point
  memory grid, $X_{\max}=800$; quote grid $\delta\in[-5,20]$ bp, 5000 points; shadow-price grid
  $p\in[-10,14]$, 2400 points (optimizer «precomputed on a shadow-price grid», p. 14). After
  truncation the lifted HJB «reduces to a finite system of backward ordinary differential
  equations» (p. 14).
- **Not stated:** lower inventory bound (presumably $-50$), memory grid spacing and lower bound,
  boundary conditions at $\pm q_{\max}$ and $X_{\max}$, treatment of $x+\alpha_s$ off-grid and of
  the transport term $-\beta x\partial_x$, time-stepping scheme.
- **Poisson comparator in §5:** $\bar\lambda^s$ = «the baseline intensity of the corresponding
  side» (p. 15), solved exactly on the inventory grid, not by Riccati.

### E. Reproduction parameters

**§5 exponential benchmark** (Table 2, p. 14; §5.1 text, p. 15):

| Parameter | Benign | Near-critical | Directional | Source |
|---|---|---|---|---|
| Excitation | common-mode, $\alpha_b=\alpha_a$ | common-mode, $\alpha_b=\alpha_a$ | bid only, $\alpha_a=0$ | p. 13–14 |
| $q_0$ | 10 | 10 | 0 | Table 2 |
| $X_0$ | 120 | 120 | 120 | Table 2 |
| $\mu^b$ | 10 | 1.5 | 5 | Table 2 |
| $\mu^a$ | 10 | 1.5 | 20 | Table 2 |
| $\beta$ | 8 | 10 | 10 | Table 2 |
| $\alpha$ | 5.2 | 9.2 | 9.2 | Table 2 |
| $\eta=\alpha/\beta$ | 0.65 | 0.92 | 0.92 | Table 2 |
| Clock, units | 1 day; size 1m notional; price in bp | same | same | p. 15 |
| $T$, $\Delta t$ | 1 day, $10^{-4}$ | same | same | p. 15 |
| Win probability | $f(\delta)=\{1+\exp(\delta-1.2)\}^{-1}$ | same | same | p. 15 |
| $\kappa$, $\kappa_T$, $\ell$ | 0.2, 0.2, $\kappa_Tq^2$ | same | same | p. 15 |
| Grids | $q$ integer, $q_{\max}=50$; $X$ 1000 pts to 800; $\delta\in[-5,20]$ (5000); $p\in[-10,14]$ (2400) | same | same | p. 15 |
| MC paths | $2\cdot10^4$, common random numbers, paired regret | same | same | p. 15 |
| Not given | $\sigma$, $\gamma$ separately; seeds; common-mode $\lambda^s(x)$; boundary conditions | | | — |

*Project computations:* myopic quote for this sigmoid $\delta^*(0)\approx1.64$ bp, $f\approx0.39$.
Table 3's 95 % half-widths imply paired SEs of ≈ 0.012–0.061, i.e. 0.03–0.13 % of $\lvert J\rvert$.

**§6.2 power-law-like experiment** (pp. 18–20):

| Parameter | Value | Source |
|---|---|---|
| Sizes, probabilities | $\{1,2,5\}$, $(0.65,0.25,0.10)$; $\mathbb E[z]=1.65$, $\mathbb E[z^2]=4.15$ (1m notional) | p. 18 |
| Win probability | $f(\delta)=\{1+\exp(3(\delta-1))\}^{-1}$; $\delta^*(0)=0.85$ bp, $f(\delta^*(0))=0.61$ | p. 18 |
| Kernel | $\Phi(u)=g_N(u)\mathcal B$, $g_N(u)=\sum_{n=1}^Nw_n\beta_ne^{-\beta_nu}$, $\sum w_n=1$ | p. 18 |
| Factors | $N=8$; $\beta_n$ log-spaced on $[2,2500]$; $w_n=\beta_n^{-\nu_{\rm mix}}/\sum_\ell\beta_\ell^{-\nu_{\rm mix}}$, $\nu_{\rm mix}=0.65$ | p. 19 |
| Kernel masses | $\mathcal B=\begin{pmatrix}0.55&0.05\\0.05&0.55\end{pmatrix}$, $r(\mathcal B)=0.60$; side-level (no size dependence) | pp. 18–19 |
| Baseline, stationary level | $\mu^b=\mu^a=155$; $\bar\lambda^b=\bar\lambda^a=388$/day; executed notional ≈ 780m/day | p. 19 |
| Penalties | $\kappa=2.0$; $\ell(q)=\kappa_Tq^2$, $\kappa_T=0.01$ | p. 19 |
| Horizons, step | $T_{\rm eval}=0.1$ day, $\Delta t=5\cdot10^{-5}$ (2000 steps); burn-in $T_{\rm burn}=0.1$ (discarded); continuation $T_{\rm cont}=0.1$ (Riccati solved on $T_{\rm eval}+T_{\rm cont}$) | pp. 19–20 |
| Forecast grid | $N_f=12$ future-lag points | p. 20 |
| Optimizer tables | $\delta\in[-1,12]$ bp, 30001 pts; $p\in[-15,25]$, 5201 pts | p. 20 |
| Shock | one-sided bid burst at time 0 after burn-in, default 50 RFQs; Fig. 7 uses 0, 5, 10, 25, 50, 75, 100 (read off) | pp. 20–21 |
| MC | $10^5$ paths, common random numbers, Poisson vs state-feedback VR | p. 20 |
| Comparator | Poisson HJB, same sizes, win probability and penalty, calibrated to $\bar\lambda^b=\bar\lambda^a$ | p. 19 |
| $q_0$ | 0 (read off Fig. 6) | p. 20 |
| Not given | seeds; $\sigma,\gamma$ separately; $N_f$ placement; how $m_t$ is evaluated; whether the 50 burst RFQs are simultaneous and fillable; state-feedback variant (42) vs (44) | — |

*Project computations from the stated recipe (not printed in the source):*
$\beta_n=$ 2.000, 5.539, 15.341, 42.489, 117.677, 325.918, 902.660, 2500.000;
$w_n=$ 0.4867, 0.2510, 0.1295, 0.0668, 0.0344, 0.0178, 0.0092, 0.0047. Mean lag
$\sum w_n/\beta_n=0.30$ day; kernel mass beyond lag 0.1 = 0.57, beyond 0.2 = 0.42. Local log-log
slope of $g_N$: −0.24 ($10^{-4}$–$10^{-3}$), −0.42 ($10^{-3}$–$10^{-2}$), −0.55
($10^{-2}$–$10^{-1}$), −1.18 ($10^{-1}$–$1$) — the −0.35 of Fig. 5 is the continuum heuristic,
fitted there to the conditional imbalance, not to $g_N$. Checks: $155/(1-0.6)=387.5$;
$2\cdot387.5\cdot0.61\cdot1.65\approx780$; $\delta^*(0)=0.852$, $f=0.609$.

### F. Table 3 (p. 16), complete

Objectives ± standard error; absolute regrets ± 95 % confidence; relative regret = absolute paired
regret / exact objective (p. 15).

| Scenario | Policy | Objective | Absolute regret | Relative regret (%) |
|---|---|---|---|---|
| Benign | Exact lifted HJB | 42.46 ± 0.12 | 0.000 ± 0.000 | 0.000 |
| Benign | Poisson HJB | 39.86 ± 0.11 | 2.606 ± 0.059 | 6.138 |
| Benign | Mean VR | 42.38 ± 0.12 | 0.077 ± 0.027 | 0.182 |
| Benign | Noise-aware VR | 42.40 ± 0.12 | 0.064 ± 0.026 | 0.151 |
| Benign | State-feedback VR | 42.43 ± 0.12 | 0.034 ± 0.024 | 0.080 |
| Near-critical | Exact lifted HJB | 48.80 ± 0.24 | 0.000 ± 0.000 | 0.000 |
| Near-critical | Poisson HJB | 42.58 ± 0.22 | 6.218 ± 0.085 | 12.742 |
| Near-critical | Mean VR | 48.37 ± 0.25 | 0.432 ± 0.042 | 0.884 |
| Near-critical | Noise-aware VR | 48.55 ± 0.24 | 0.250 ± 0.036 | 0.513 |
| Near-critical | State-feedback VR | 48.76 ± 0.24 | 0.041 ± 0.025 | 0.083 |
| Directional | Exact lifted HJB | 46.20 ± 0.10 | 0.000 ± 0.000 | 0.000 |
| Directional | Poisson HJB | 33.58 ± 0.08 | 12.617 ± 0.119 | 27.312 |
| Directional | Mean VR | 45.04 ± 0.10 | 1.154 ± 0.054 | 2.498 |
| Directional | Noise-aware VR | 45.20 ± 0.10 | 0.997 ± 0.049 | 2.159 |
| Directional | State-feedback VR | 46.12 ± 0.10 | 0.079 ± 0.020 | 0.170 |

Fig. 3 (p. 15) plots the same relative regrets on a log scale. In Table 3 the memory error (VR vs
exact) and the Riccati/quadratic approximation error are not separated: every VR row carries both.

### G. Error / convergence theory offered

None. §5.1 opens: «We do not pursue a general well-posedness theorem for the full path-dependent
Hawkes control problem» and closes the paragraph «The focus of the paper is therefore not a general
convergence theorem, but a controlled numerical validation of the approximation hierarchy» (p. 14).
The level-2 correction «is not an exact value function and is not claimed to restore a
dynamic-programming or time-consistency property. Its sign is governed by the curvature of the
deterministic-intensity value map with respect to the forecast curve; it is not assumed to be
positive in general» (p. 11). Near criticality: «As η approaches one, intensity uncertainty becomes
persistent and the mean forecast alone can become insufficient» (p. 14) — qualitative, no rate.
Conclusion: see the first quote below (p. 22). Route suggested, not pursued: pseudo-chaotic
expansions of point-process functionals (Hillairet & Réveillac 2024, p. 22). For an exact-problem
convergence result the source points to [[jusselin-2021-persistent-order-flow]] (viscosity
solution, consistent numerics, p. 2).

### H. Which functional of the history the quote depends on

- **Exact problem:** the whole marked history $H$, via $V(t,q,H)$ (eq. 18, p. 8).
- **Source's reduced state:** the forecast curve $u\mapsto m_t(u)$ on $[0,T-t]$ — «we treat the
  conditional forecast curve as the economically relevant reduced state» (p. 3); «In a
  general-kernel Hawkes model, the state variable is the updated forecast curve. In an exponential
  benchmark, the same update is represented by the finite-dimensional Hawkes memory state» (p. 12).
- **Level 1:** history enters only through $m_t$; via (27) and (32) the quote depends on the curve
  only through the two scalars $A_0(t)$ and $B_0(t)$ ($C_0$ drops out of $\Delta v_0$). $A_0$ is
  driven by the size- and $h_{k,2}$-weighted **total** forecast $\sum_{s,k}m^{s,k}_tz_kh_{k,2}$ (29);
  $B_0$ by the **signed** forecast $\sum_{s,k}\epsilon_sm^{s,k}_tz_k(\dots)$ (30) — «For symmetric side
  intensities and penalties the skew coefficient $B_0$ is zero; for directional bursts it becomes
  the dominant quote-skew term» (p. 10). *(Reading of (29)–(30), project.)*
- **Level 2:** additionally the two-time covariance $\Sigma_t(u,v)$, weighted by $K_{ij}$ (38).
- **Level 3:** additionally the post-request curve $m_t+\rho_i$; to first order the lag weighting is
  the Riccati sensitivity difference $D_j(t,q;u)-D_j(t,q+\epsilon_iz_i;u)$ applied to $\rho_{i,j}(u)$
  (43) — the «Riccati sensitivity kernel» that (51) uses as a «Volterra filter» (pp. 17–18).
- No explicit lag weights, integrated forecast or finite set of statistics is derived beyond this.

### Direct quotes (for the draft)

> "A frozen conditional forecast does not satisfy an intertemporal dynamic-programming principle; the implemented policy obtains feedback by reconditioning and resolving as the history evolves. The exponential benchmark provides numerical evidence that this receding horizon construction is accurate in the regimes studied, but a general error or convergence theory remains open." (p. 22)

> "Thus a d-factor approximation of a two-sided, K-size Hawkes model already introduces 2Kd flow-memory variables in addition to inventory. A power-law kernel requires either a large exponential mixture or a genuinely infinite-dimensional Volterra state." (p. 8)

> "In the present power-law case, an exact lifted benchmark is not available at comparable complexity. The role of the experiment is therefore to apply the validated approximation to the genuinely non-Markovian setting." (p. 21)

> "Since the mixture is finite, the power-law behaviour should be read as an intermediate-range approximation: the fastest exponential creates a short-time cut-off and the slowest exponential eventually dominates at very long lags." (p. 19)

> "In a general-kernel Hawkes model, the state variable is the updated forecast curve. In an exponential benchmark, the same update is represented by the finite-dimensional Hawkes memory state." (p. 12)

### Examples & illustrations (for later drafting)

- Table 3 (p. 16): the regret ladder Poisson → mean VR → noise-aware → state feedback in three
  regimes, the only exact-anchored regret numbers in the paper (one exponential).
- Fig. 5 (p. 19): conditional imbalance after a 50-RFQ bid burst on a log-log axis against a guide
  slope −0.35, and the quote skew $\delta^a_t(0)-\delta^b_t(0)$ decaying from ≈ 0.33 to ≈ 0.07 over
  0.1 day (read off).
- Fig. 7 (p. 21): relative P&L-std reduction vs burst size, ≈ 0.034, 0.030, 0.033, 0.044, 0.084,
  0.141, 0.192 at bursts 0, 5, 10, 25, 50, 75, 100 (read off the plot).

### Boundary of this focus

The source cannot supply a regret-vs-$p$ curve, a kernel- or forecast-error measure, an error
bound, a power-law kernel with tail exponent above one, or any long-memory reference other than
Poisson. Its exact-anchored numbers (Table 3) are for one exponential and mix forecast and
Riccati error. Reproduction gaps (common-mode $\lambda^s(x)$, boundary conditions, seeds, $N_f$
placement, SF variant) are listed in D and E.

### Bearing on the memory-regret gap (plan Task 2 stop rule)

**No — this source does not close the gap.** The stop rule needs regret/reward vs $p$ on a
power-law kernel with an exact or near-exact reference **and** a second-order regret law. (i) $p$ is
never swept: one exponential in §5, $N=8$ fixed in §6.2, only the burst size varied (pp. 13,
18–21). (ii) No exact or near-exact long-memory reference: «we do not solve a lifted HJB in the
exponential factors» (p. 19), «an exact lifted benchmark is not available» (p. 21); the comparator is
Poisson, and §6.2 reports risk reduction, not regret. (iii) No regret law: the second-order kernel
$K_{ij}$ (36) enters only the covariance correction (38), never a loss formula for a mis-specified
forecast, and «a general error or convergence theory remains open» (p. 22). In addition, the §6.2
kernel is $u^{-0.35}$-like over an intermediate range, i.e. outside the plan's $b>1$ grid (inference,
item 5 above).

## Mentioned entities

- Models: [[begv-2021-model]], [[glft-2013-model]], [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]] (the 2018 SIAM Review paper by the same authors is what is cited)
- Concepts: [[hawkes-process]], [[branching-matrix]], [[markov-lift]], [[intensity-forecast]], [[volterra-riccati]], [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[shadow-price]], [[regret]]
- Other works (bibkeys): `jusselin-2021-persistent-order-flow`, `bergault-2023-liquidity-dynamics-rfq`, `barzykin-2026-market-making-transient`, `muhlekarbe-2026-unified-theory-order`, `bacry-2015-hawkes-processes-finance`, `cartea-2015-algorithmic-high-frequency`, `ho-1981-optimal-dealer-pricing`, `avellaneda-2008-high-frequency-trading`, `gueant-2013-dealing-inventory-risk`, `bergault-2021-closed-form-approximations`, `kumar-2024-deep-hawkes-process`, `jain-2025-impulse-control-hawkes`; not in the library: Abi Jaber & Neuman 2025, Jaisson 2015, Jusselin & Rosenbaum 2020, Eisler & Bouchaud 2016, Hillairet & Réveillac 2024, Itkin 2026a,b.

## Connections

- Builds on: [[begv-2021-model]] (Hamiltonian expansion → Riccati, now with forecast-driven time-varying intensities, single asset).
- Builds on / argues against relying on: [[markov-lift]] (used as exact benchmark; lift + quadratic yields transport-jump equations, p. 8).
- Cites: [[glft-2013-model]], [[avellaneda-stoikov-model]].
- Supplements: [[martin-2026-market-making-hawkes]] (cited, p. 2: Mercer-expansion lift + PINN — the "large lifted state" route this paper avoids); [[bergault-2024-price-aware-automated]] (cited, p. 2: joint jumps of flow state and inventory make exact DP high-dimensional).
- Compare (not cited by the source): [[acero-2026-hawkes-structured-networks]] for multi-asset Hawkes structure that this paper lacks.
- Closest exact-treatment reference (no page yet): `jusselin-2021-persistent-order-flow`.
- Cites (2026-11-01, p-sweep focus): [[jusselin-2021-persistent-order-flow]] — «The closest market-making reference» (p. 2), and the only pointer the source gives to a convergence result (viscosity solution and consistent numerics of the exact problem); that page now exists, so the line above is superseded. [[martin-2026-market-making-hawkes]] — Mercer-expansion Markov approximation solved by PINN (p. 2).
- Compare (not cited by the source): [[acero-2026-hawkes-structured-networks]] (regret bound via kernel $L^2$ error in the number of factors) and [[khabou-2025-markov-approximation-hawkes]] (value convergence under kernel $L^1$ error) — the factor-count error results this source lacks.
