---
title: "Barzykin 2026 — Dynamic Slippage Control and Rejection Feedback in Spot FX Market Making"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: barzykin-2026-dynamic-slippage-control
depth: standard
tags: [market-making, fx, last-look, rejection, reputation-feedback, adiabatic-approximation, riccati, decision-driven-feedback, single-asset]
relations:
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "«Following Bergault et al. (2021) we expand the Hamiltonians in p up to the second order» eq. (25), then quadratic ansatz (26) → Riccati ODE (27) (p. 6)."
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "Second-order expansion of the rejection-augmented Hamiltonians H_n(p,J) in p, eq. (25) (p. 6); closed-form H_pp at the myopic point, eqs. (36), (55) (pp. 7, 14)."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "«matching the coefficients of q2 yields the Riccati ODE for A(t)» eq. (27), scalar case, stationary root eq. (28) (p. 6)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "«we propose a tractable stochastic-control framework for D2C market making with latency that builds on the Avellaneda-Stoikov tradition» (p. 2)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Limit case: «the model collapses to the standard OTC HJB (without rejection control) and the familiar δ = 1/κn + D±V regime (Guéant et al. 2013)» (p. 6)."
  - target: cartea-2014-buy-low-sell
    type: cites
    confidence: extracted
    because: "Objective «expected terminal mark-to-market wealth penalized by running inventory risk (Cartea et al. 2014)» eq. (9) (p. 4)."
  - target: who-excites-the-flow
    type: supports
    confidence: inferred
    because: "Decision-driven feedback: the accept shadow price (14) compares V(q,R) with V(q±z,R_acc(R)), i.e. inventory and the flow state jump together — the fill-driven structure; the quadratic closure is obtained only after freezing R (p. 6)."
  - target: barzykin-2026-hawkes-driven-otc
    type: mentions
    confidence: inferred
    because: "Same author; the later Hawkes paper excludes «last-look feedback, relationship scores» from the memory (its p. 6) — exactly the channel this paper models; not cited here (this paper is earlier)."
---

# Dynamic Slippage Control and Rejection Feedback in Spot FX Market Making

## Bibliographic Details

Barzykin, Alexander. 2026. *Dynamic slippage control and rejection feedback in spot FX market
making*. arXiv:2603.07752v1 [q-fin.RM], 8 March 2026 (title page dated 10 March 2026). 18 pp.
Affiliation: HSBC, London. The proposal cites it as "Barzykin 2026a".

**Read:** arXiv 2603.07752v1. No published version is recorded (`library/references.bib`: misc,
preprint). The preprint is the original. Page and equation numbers follow v1 (printed page =
PDF page).

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\sigma$, $\gamma$ | mid volatility (eq. 1), risk aversion (eq. 9) | $\sigma$, $\gamma$ |
| $q_t$, $X_t$ | inventory, cash (eqs. 7–8) | $q_t$, $X_t$ |
| $\delta^{n,i}_t$, $i\in\{b,a\}$, $z_n$ | quote offset per size bucket $n$ and side; size | $\delta^b,\delta^a$ |
| $\lambda^{n,i}_t=g(R_t)\Lambda^0_ne^{-\kappa_n\delta}$ | request intensity (eq. 3) | GLFT $\Lambda e^{-k\delta}$, $\kappa_n\leftrightarrow k$, times a gate |
| $R_t$, $\rho$ | rejection score (EMA), EMA coefficient (eq. 5) | no project symbol; ⚠ $\rho$ clashes with $\rho(K)$ |
| $g(R)=e^{-\rho_gR}$ | reputation gate (p. 8) | — |
| $\ell^{n,i}_t\in\{0,1\}$ | accept (1) / reject (0) decision | — |
| $Y^{n,i}$, $m_n(\delta)$, $\nu_n=\sigma\sqrt{\tau_n}$ | latency mark, its mean (adverse selection), its sd | ⚠ $m_n$ is **not** the forecast $m_t(u)$ |
| $\theta_n$ | constant slippage $m_n\equiv-\theta_n$ (eq. 29) | ⚠ not the value function $\theta$ |
| $V(t,q,R)$ | reduced value function (eq. 11) | $\theta(t,q,\lambda)$ with $R$ in place of $\lambda$ |
| $p^{n,i}=D^\pm_nV$, $J=\mathcal J_RV$ | accept shadow price (eq. 14), reject continuation jump (eq. 15) | $p^j$; $J$ has no project symbol |
| $H_n(p,J)$, $\Sigma(J)=\sum_nH^n_{pp}(0,J)$ | bucket Hamiltonian (eq. 19), summed curvature (eq. 27) | $H^{i,s}$, $h_2$; ⚠ $\Sigma$ is not the price covariance |
| $A(t)$, $C(t)$ | quadratic coefficients, ansatz $V=-Aq^2-C$ (eq. 26) | $A$, $C$ (no $B$: symmetric) |
| $\epsilon$ | fair-protocol symmetric tolerance (Sec. 3.1) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (last look / price validation, two gaps: endogenous rejection policy, rejection → future flow) | 1–2 |
| ✓ F1 | 2.1 Problem setup (eqs. 1–9) | 3–4 |
| ✓ F1 | 2.2 HJB and optimal controls (eqs. 10–24, Fig. 1) | 4–6 |
| ✓ F1 | 2.3 Adiabatic quadratic approximation (eqs. 25–28); special case constant slippage (eqs. 29–39); calibration of $J$ (eq. 40) | 6–7 |
| ✓ F1 | 2.4 Numerical examples (Figs. 2–6, eq. 41) | 8–12 |
| ✓ F1 | 3 Towards fair execution; 3.1 symmetric tolerance with capped slippage (eqs. 42–50, Fig. 7) | 10–13 |
| ✓ F1 | 3.2 Adiabatic quadratic approximation and constant slippage (eqs. 51–57) | 12–14 |
| ✓ F1 | 3.3 Numerical examples (Fig. 8, Table 1); Simulation (eqs. 58–59, Figs. 9–10) | 14–17 |
| ✓ F1 | 4 Concluding remarks | 16–17 |
| — | Acknowledgments, References | 17–18 |

## Kernthesen

### 1. Rejection (slippage tolerance) is a control, optimised jointly with quotes, under zero hold time (pp. 1–3)

Current practice has «reduce[d] post-request hold time to zero» so "last look" is really price
validation, but the dealer «keeps slippage tolerance as a control parameter» (p. 2). Against Olding
(2022), where last-look parameters «are treated as given, while the dealer optimizes quotes»
(p. 2), the paper makes the accept/reject rule a state-dependent control: «the trade economically
akin to an embedded option written on the latency price move» (abstract, p. 1).

### 2. Requests are Poisson with a GLFT-type quote response multiplied by a reputation gate (p. 3)

$\lambda^{n,i}_t=g(R_t)\Lambda^0_ne^{-\kappa_n\delta^{n,i}_t}$ (eq. 3), $g$ decreasing on $[0,1]$.
Arriving requests carry a Gaussian latency mark $Y^{n,i}(\delta)=m_n(\delta)+\nu_n\xi$,
$\nu_n=\sigma\sqrt{\tau_n}$ (eq. 4), observed before the decision; a quote-dependent mean $m_n(\delta)$
encodes selective client reaction to stale quotes (p. 3). There is no self-excitation in the
Hawkes sense; the only feedback is through $R$.

### 3. ⭐⭐ The reputation state is an event-clock EMA of the dealer's own reject decisions (p. 3)

«Reputation (rejection score) is updated per request $R_+=(1-\rho)R+\rho(1-\ell)$» (eq. 5), with
maps $R_{acc}(R)=(1-\rho)R$, $R_{rej}(R)=(1-\rho)R+\rho$ (eq. 6). $R$ does **not** decay in calendar
time: it moves only when a request arrives, and every request (accepted or rejected) moves it.
An OU process driven by rejections is mentioned as an alternative (fn. 4), and the presence of the
effect can be tested by regressing request counts on the previous period's reject rate (fn. 2).

### 4. The affine ansatz removes the mid price; the exact reduced problem is an HJB on $(t,q,R)$ (pp. 4–5)

Objective: $\sup\mathbb E[X_T+q_TS_T-\tfrac12\gamma\sigma^2\int_0^Tq_t^2dt]$ (eq. 9), «possibly with a
terminal penalty». With $U=x+qS+V(t,q,R)$ (eq. 11) the reduced HJB is
$0=\partial_tV-\tfrac12\gamma\sigma^2q^2+g(R)\sum_{i,n}H_n\big(p^{n,i}(t,q,R),J(t,q,R)\big)$ (eq. 20).

### 5. ⭐⭐ Accepting moves inventory **and** reputation in one jump; rejecting moves reputation only (p. 4)

$p^{n,i}=D^\pm_nV:=[V(t,q,R)-V(t,q\pm z_n,R_{acc}(R))]/z_n$ (eq. 14) and
$J=V(t,q,R_{rej}(R))-V(t,q,R)$ (eq. 15). «Under this monotonicity, $J(t,q,R)\le0$. We can interpret
$J$ as the continuation loss from worsening reputation» (p. 4). The shadow price is therefore a
difference across two reputation levels, not a finite difference in $q$ at fixed state.

### 6. The accept decision is an option on the latency mark; the Hamiltonian is closed-form in $\Phi,\varphi$ (pp. 4–6)

With $\Psi_n(\mu)=\nu_n\varphi(\mu/\nu_n)+\mu\Phi(\mu/\nu_n)$ (eq. 17),
$\mathbb E\max[z_n(\delta+Y-p),J]=J+z_n\Psi_n(\delta+m_n-p-J/z_n)$ (eq. 18) and
$H_n(p,J)=\sup_\delta\Lambda^0_ne^{-\kappa_n\delta}[J+z_n\Psi_n(\cdot)]$ (eq. 19). The FOC is eq. (22);
accept iff $z_n(\delta^*+Y-p)\ge J$ (eq. 24). With $J\equiv0$, $m_n\equiv0$, $\nu_n\to0$ the GLFT
rule $\delta^*=1/\kappa_n+D^\pm_nV$ is recovered (p. 6).

### 7. ⭐⭐ Adiabatic-quadratic approximation: freeze $R$, replace $J$ by a constant, then BEGV → scalar Riccati (p. 6)

«The full problem thus couples a fast inventory control with a slow reputation state. In the
adiabatic regime, we approximate R as quasi-static over the quoting horizon, set g(R) =: g and drop
R-dependence from the value function. In the self-consistent closure, we replace the continuation
difference by a constant J ≤ 0 calibrated to match the corresponding rejection rate. HJB becomes
inventory-only» (p. 6). Then (25)–(26) give $A'(t)+\tfrac12\gamma\sigma^2=4gA(t)^2\Sigma(J)$ (eq. 27)
and, stationary, $A=\sqrt{\gamma\sigma^2/(8g\Sigma(J))}$ (eq. 28), with $p^{n,i}(q)=A(z_n\pm2q)$.
The reputation level enters the Riccati coefficient only through $g=g(R)$ and $J$.

### 8. ⭐ The constant $J$ is fixed by a self-consistency condition on reject rates, not by $\partial_RV$ (p. 7)

$\bar r(J)$ = intensity-weighted reject probability at the myopic point $p=0$ (eq. 40); «we set J
such that $\bar r(J)=R$ … Under slow reputation dynamics, we solve the fast inventory-control
problem at frozen R, compute the resulting stationary reject frequency $\bar r(J)$, and choose J so
that this stationary reject frequency matches the current reputation level. This provides a
self-consistent local closure linking the fast control problem to the slow reputation state»
(p. 7). (The true $J=V(R_{rej})-V(R)\approx\rho(1-R)\partial_RV$ is not used; see Kernthese 18.)

### 9. Constant slippage gives a shift rule and explicit quotes and thresholds (p. 7)

With $m_n\equiv-\theta_n$: $H_n(p,J)=e^{-\kappa_np}H_n(0,J)$ (eq. 31), $\delta^*_n(p,J)=\bar\delta_n(J)+p$
(eq. 32), $H^n_{pp}(0,J)=\Lambda^0_ne^{-\kappa_n\bar\delta_n}z_n\kappa_n\Phi(\tilde\mu_n)$ (eq. 36), and
«the adiabatic optimal quotes become explicit» $\delta^{n,i}=\bar\delta_n(J)+A(z_n\pm2q)$ (eq. 38),
accept iff $Y\ge y^*_n=J/z_n-\bar\delta_n(J)$ (eq. 39). The threshold is inventory-independent in
this approximation.

### 10. Latency leads to rejection and tighter spreads; optimal thresholds are deep (pp. 8–9)

Calibration (p. 8): sizes $(1,2,5,10,20)$M, $\Lambda^0=(2000,800,600,400,100)$/day,
$\kappa=(3.0,2.5,2.0,1.5,1.0)$ bp⁻¹, daily vol 100 bp, $\gamma=10^{-3}$. Below ~100 ms latency there
is «no point for the dealer to reject»; with more latency «the MM starts rejecting, and the spread
tightens» (p. 8, Fig. 2). With quote-dependent toxicity, «even an unconstrained MM does not reject
immediately upon observing adverse slippage» (p. 8, Fig. 3).

### 11. ⭐ "Repair–exploit": at high $R$ the dealer tightens yet rejects more selectively, because the score updates in event time (pp. 8–9)

«when the rejection score R is high, the dealer tightens spreads yet becomes more selective ex
post» (p. 8); «Tighter quoting then helps restore reputation faster through a higher arrival rate
and hence a faster dilution of past rejections in calendar time» (p. 9). The author calls this
«a structural feature of the model» and a motivation for fair protocols (p. 9); fn. 8 notes that
driving $R$ by rejections alone would also help.

### 12. Stationary reputation is a fixed point independent of the flow level (p. 9)

$\dot R\approx\rho\lambda(q,R)(\bar r(q,R)-R)$; stationary levels satisfy $R=\bar r(q,R)$ (eq. 41),
«which is independent of λ, while λρ controls the speed of convergence» (p. 9). Larger $\rho_g$ →
lower stationary reject probability and wider spread (Fig. 5, p. 11): «the dealer will try to avoid
rejection on average, even unconditionally, in the presence of reputation feedback» (p. 9).

### 13. ⭐⭐ The adiabatic surrogate is checked against the exact reduced HJB only visually, at one reputation level and one size (p. 9, Fig. 6 p. 12)

«For our parameter set (with $\rho_g$ = 0.1), the equilibrium reputation level is $R^*\simeq0.03$. This
is the value we use to evaluate pricing in Figure 6. The accuracy is reasonable, particularly for
small inventories (comparison is only demonstrated for the smallest size bucket z1). We have also
verified rejection thresholds and found a good correspondence (not shown)» (p. 9). No error metric,
no regret and no value gap is reported.

### 14. Fair protocol: symmetric tolerance with capped favourable slippage, on dealer-quote moves (pp. 10–13)

Following Oomen (2017b): reject if $Y<-\epsilon$, accept on-rate if $|Y|\le\epsilon$, rebate if
$Y>\epsilon$ (p. 11). The mark is now the dealer's own quote move, treated «as an exogenous
effective quote-revision variable», which «preserves the dynamic-programming structure» (p. 11).
Closed-form increment $G_n=J\Phi(a_n)+z_n(\delta-p)B_n+z_nC_n$ (eq. 48), Hamiltonian eq. (50).

### 15. The adiabatic closure carries over to the fair protocol unchanged in structure (pp. 12–14)

«We freeze reputation and replace the state-dependent reject jump J(t, q, R) by a constant J ≤ 0
defined with self-consistent adiabatic closure» (p. 12). Shift rule (54), $H_{pp}$ identity (55) with
acceptance probability $B_n$ in place of $\Phi(\tilde\mu_n)$, quotes again eq. (38), tolerance
$\epsilon_n=\bar\epsilon_n(J)$ (eq. 56), calibration eq. (57) (p. 14). «There is generally no closed
form for $\bar\epsilon_n(J)$, but numerical 1D maximization is cheap» (p. 14).

### 16. ⭐ Exact HJB results: reputation feedback cuts rejections sharply at small utility cost (p. 15, Table 1)

Latency $\tau=1$ s, $\theta_n=0.1$ bp (p. 14), «obtained by numerically solving the corresponding
HJB»: no rejection/no adverse selection — spread 0.69 bp, utility 235.4; no rejection — 0.89,
195.1; unconstrained, $\rho_g=0$ — spread 0.53, threshold 0.25, reject 0.33, utility 201.7;
unconstrained, $\rho_g=0.2$ — 0.80, 0.79, 0.06, 196.9; symmetric, $\rho_g=0$ — 0.71, 0.43, 0.17,
199.4; symmetric, $\rho_g=0.2$ — 0.83, 0.68, 0.05, 196.5. «Reputation feedback causes both protocols
to reduce rejections dramatically» (p. 14). Utility is $V(0,0,R)$ (fn. 11, p. 14).

### 17. Monte Carlo under exact stationary controls shows relaxation of $R$ to the stationary state (pp. 14–16)

Adverse quote selection via tilted intensities (eq. 58) with a rescaling that keeps the
unconditional rate fixed (eq. 59); $5\cdot10^4$ trajectories, $\tau=0.5$ s, $\rho=\rho_g=0.01$,
start $q=0,R=0$; «the dealer maintains the optimal rejection rate from the start» (p. 16, Fig. 9).
Fig. 10 (p. 17) plots risk-adjusted P&L against realised rejection rate — «This kind of plot can
be verified empirically» (p. 16).

### 18. ⭐ The self-consistent $J$ closure is heuristic (inference from pp. 4, 6–7)

The exact object is $J=V(R_{rej}(R))-V(R)$, an $O(\rho)$ difference of the value function in $R$
(eqs. 6, 15). The adiabatic scheme drops $R$ from $V$ and then needs $J$ back, so it reinstates it
by a rate-matching condition ($\bar r(J)=R$) that is not derived from the HJB. The paper offers no
argument why this calibration approximates $\partial_RV$; the only check is Kernthese 13.

## Figures and tables

- Fig. 1 (p. 5): latency mark density and embedded-option payoff, unrestricted rejection.
- Fig. 2 (p. 8): top-of-book spread and reject probability vs latency.
- Fig. 3 (p. 9): bid/ask rejection thresholds vs inventory (quote-dependent toxicity).
- Fig. 4 (p. 10): spread and reject probability vs rejection score $R$ at $q=0$.
- Fig. 5 (p. 11): stationary spread and reject probability vs $\rho_g$.
- Fig. 6 (p. 12): optimal quotes vs inventory at stationary $R$; dashed = adiabatic-quadratic approximation for $z_1$ (the only approximation check).
- Fig. 7 (p. 13): fair-protocol payoff diagram.
- Fig. 8 (p. 15): stationary value $V(0,q,R)$, fair protocol.
- Table 1 (p. 15): protocols × $\rho_g$ (spread, threshold, rejection, utility).
- Figs. 9–10 (pp. 16–17): MC relaxation of $R$; P&L vs realised rejection rate.

No figures extracted to `knowledge/assets/` (write scope limited to this page).

## What this source does not address

- **Self-/cross-exciting order flow.** Arrivals are Poisson; no Hawkes kernel, no branching ratio.
  The only memory is the EMA score.
- **More than one asset.** One currency pair; "multi" means a ladder of size buckets.
- **CARA utility** — only the risk-adjusted objective (eq. 9).
- **A quantitative error of the approximation.** Only a visual comparison (Fig. 6); no regret,
  no value gap, no convergence argument.
- **The grid or method for the "exact" reduced HJB** — not described beyond «solved numerically»
  (fn. 7, p. 8; p. 14).
- **Post-trade adverse selection, competition among LPs, client strategic response** — the gate
  $g(R)$ is an exogenous reduced form.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 3, 4, 5, 7, 8, 9, 12, 13, 15, 18.**

### What this focus needs beyond the Kernthesen

1. **Which convention this is.** In the terms of [[who-excites-the-flow]] the paper is
   *decision-driven*: the flow-modulating state $R$ is moved by the dealer's own accept/reject
   decisions on every arriving request (eq. 5), so quotes and thresholds change future intensity
   through $g(R)$. It is the fill-driven side of the dichotomy with two differences: the feedback
   is *inhibitory* (rejections lower flow) and *bounded* ($R\in[0,1]$, $g$ bounded), and the
   memory runs in event time, not calendar time.
2. **Why the quadratic closure would break without freezing (inference).** The accept shadow
   price (14) compares $V(q,R)$ with $V(q\pm z,R_{acc}(R))$, the same two-level mix as the
   fill-driven $\tilde p^j$ in [[problem-anatomy]] §3. With an $R$-dependent ansatz
   $V=-A(R)q^2-C(R)$ it would carry a term $[A(R_{acc})-A(R)]q^2/z\approx-\rho R\,A'(R)q^2/z$, which
   generates $q^3,q^4$ in $\tfrac12H_{pp}p^2$. The obstruction is $O(\rho)$, and $\rho=0.01$ in the
   numerics (p. 8). The adiabatic step drops exactly these $O(\rho)$ terms; the companion paper
   [[barzykin-2026-strategic-otc-reputation]] writes this expansion out (its eqs. 16–21).
3. **How the closure is obtained, step by step.** (a) Freeze $R$ ("quasi-static over the quoting
   horizon"), so $g(R)$ is a constant; (b) drop $R$ from $V$; (c) put back the reputation cost of a
   rejection as a constant $J$ fixed by $\bar r(J)=R$; (d) BEGV expansion (25) + quadratic ansatz (26)
   → scalar Riccati (27)/(28). Quotes then come from the exact FOC with $p=A(z\pm2q)$ (p. 6).
   Steps (a)–(c) are the approximation of the flow feedback; step (d) is the usual BEGV error.
4. **What is checked against the exact solution, and with what error.** The exact reduced HJB in
   $(t,q,R)$ — two state dimensions, one asset — is solved numerically. The surrogate is compared at
   $R^*\simeq0.03$, size $z_1$ only, quotes vs inventory (Fig. 6): «accuracy is reasonable,
   particularly for small inventories»; thresholds «good correspondence (not shown)» (p. 9). No
   number. This is the weakest validation among the Barzykin papers in the wiki; compare the
   paired-regret table of [[barzykin-2026-hawkes-driven-otc]] (Table 3, its p. 16).
5. **Bearing on D2 (λ-dependent Riccati coefficients).** The frozen-state Riccati has a coefficient
   that depends on the intensity state: $A(R)=\sqrt{\gamma\sigma^2/(8g(R)\Sigma(J))}$. This is the
   "Riccati at frozen intensity" pattern, with the intensity state here an exogenous multiplier of
   all rates. The paper does not use $A(R)$ in a correction to the shadow price (the companion paper
   does: $\partial_RA$ enters its eq. 31).
6. **Bearing on D1 (fill-driven CARA linearisation).** None directly: risk-adjusted objective, no
   exponential transform. The exact problem is solved by brute force on $(q,R)$.
7. **Several assets / cross-asset.** Not discussed. *Inference:* with $d$ assets a shared reputation
   gate $g(R)$ would scale every intensity by one factor and leave the BEGV matrix Riccati intact at
   frozen $R$ (only $\Lambda\to g\Lambda$); per-asset or per-channel scores give a vector $R$ of slow
   states, the structure of the companion paper.

### Direct quotes (for the draft)

> "The full problem thus couples a fast inventory control with a slow reputation state. In the adiabatic regime, we approximate R as quasi-static over the quoting horizon, set g(R) =: g and drop R-dependence from the value function. In the self-consistent closure, we replace the continuation difference by a constant J ≤ 0 calibrated to match the corresponding rejection rate. HJB becomes inventory-only." (p. 6)

> "Under slow reputation dynamics, we solve the fast inventory-control problem at frozen R, compute the resulting stationary reject frequency r̄(J), and choose J so that this stationary reject frequency matches the current reputation level." (p. 7)

> "The accuracy is reasonable, particularly for small inventories (comparison is only demonstrated for the smallest size bucket z1)." (p. 9)

> "Yet most tractable models do not include a reputational state variable that couples the current rejection decision to future flow intensity." (p. 2)

### Examples & illustrations (for later drafting)

- Table 1 (p. 15): unconstrained rejection with no feedback rejects 33% of requests; with
  $\rho_g=0.2$ only 6%, at a utility cost of 201.7 → 196.9 — reputation feedback as a strong
  behavioural constraint.
- Kernthese 11 (pp. 8–9): the "repair–exploit" effect, a policy feature that exists only because the
  flow state is moved by the dealer's own decisions in event time.

### Boundary of this focus

No Hawkes excitation and one asset; the bearing on Hawkes closures is by analogy (feedback state
jumping together with inventory). The validation of the closure is qualitative only.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]], [[glft-2013-model]], [[begv-2021-model]]
- Concepts: [[who-excites-the-flow]], [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[shadow-price]]
- Source pages: [[gueant-2013-dealing-inventory-risk]], [[cartea-2014-buy-low-sell]], [[bergault-2021-closed-form-approximations]]
- Other works (bibkeys): `barzykin-2025-optimal-quoting-adverse` (exponential-saturation toxicity, price reading), `bergault-2021-size-matters-otc` (size ladder; key not verified in this pass), `cartea-2015-algorithmic-high-frequency`; not in the library as checked: Oomen 2017a,b, Stevenson 2016, Cartea–Jaimungal–Walton 2019, Olding 2022, Cartea–Wang 2020, Cartea–Sánchez-Betancourt 2021, GFXC 2024.

## Connections

- Builds on: [[begv-2021-model]] (Hamiltonian expansion → Riccati, applied at frozen reputation); [[avellaneda-stoikov-model]] tradition.
- Extended by: [[barzykin-2026-strategic-otc-reputation]] (cites this paper as [18]: two scores, explicit first-order expansion in the EMA coefficient, score gradient in the shadow price).
- Contrast: [[barzykin-2026-hawkes-driven-otc]] (flow-driven Hawkes memory, forecast freezing, quantitative regret) vs this paper (decision-driven bounded score, reputation freezing, visual check).
- Instance of the fill/decision-driven side of [[who-excites-the-flow]]; see [[problem-anatomy]] §3.
