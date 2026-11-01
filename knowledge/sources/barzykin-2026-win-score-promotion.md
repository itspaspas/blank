---
title: "Barzykin 2026 — Win-Score Promotion Gates in Aggregator-Routed RFQ Markets: A Two-Tier Stochastic Control Model"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: barzykin-2026-win-score-promotion
depth: standard
tags: [market-making, rfq, otc, fx, aggregator, win-score, state-dependent-intensity, adiabatic-approximation, bifurcation, hamiltonian-approximation, single-asset]
relations:
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "«A quadratic inventory ansatz and quadratic Hamiltonian expansion à la Bergault et al. [7] yield an LQ-like closure, stationary Riccati scaling for the inventory curvature» (p. 2); expansion eq. (19), p. 4."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "Quadratic ansatz (17) taken «In the spirit of [7]» = Bergault–Evangelista–Guéant–Vieira 2021 (p. 4); curvature equation «follow[s] the standard Bergault-Guéant calculations» (fn. 5, p. 5)."
  - target: bergault-2021-closed-form-approximations
    type: builds-on
    confidence: extracted
    because: "Reference [7] (p. 12) is the BEGV paper; its ansatz and Hamiltonian expansion are used in Sec. 3.1, eqs. (17)–(20) (p. 4)."
  - target: who-excites-the-flow
    type: supports
    confidence: inferred
    because: "Tier-A intensity Λ^A_z G(R) depends on a score R updated by the dealer's own wins and losses (eqs. 2–3, p. 3): the control feeds the intensity. The quadratic closure (18) is obtained only after dropping the α A_R q² term (v_R ≈ B_R, p. 4) — consistent with the concept page's claim that outcome-driven feedback breaks exact quadratic closure."
  - target: matrix-riccati-equation
    type: builds-on
    confidence: inferred
    because: "Scalar case only: «Matching q² coefficients … yields a Riccati-type relation» with stationary A∞(R) ∝ (γσ²/2ξ(R))^{1/2} (eq. 21, p. 5); the equation itself is not written out (fn. 5)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "Objective (4): «We assume a standard linear wealth objective with quadratic inventory penalties [10]» (p. 2), [10] = Cartea, Jaimungal & Ricci 2014 (p. 12)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Cited in «stochastic optimal control approaches to market making combine inventory management with quote-dependent order arrivals [21, 2, 20, 10]» (p. 1), [20] = Guéant–Lehalle–Fernandez-Tapia 2013."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "Same citation cluster «[21, 2, 20, 10]» (p. 1), [2] = Avellaneda & Stoikov 2008 (p. 12)."
---

# Win-Score Promotion Gates in Aggregator-Routed RFQ Markets

## Bibliographic Details

Barzykin, Alexander. 2026. *Win-score promotion gates in aggregator-routed RFQ markets: A
two-tier stochastic control model*. arXiv:2603.10569v1 [q-fin.RM], 11 March 2026 (title page
dated 12 March 2026). 12 pp. + blank. Author affiliation: HSBC, London.

**Read:** arXiv 2603.10569v1. No published version is recorded; the preprint is its own
original (non-core work; no `based_on`). Page and equation numbers follow v1; printed page
numbers coincide with PDF pages. The text layer drops some radicals: the square roots in
eqs. (21), (27) are reconstructed from eqs. (28)–(29) (a «√» and an exponent −3/2 survive there).

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $i\in\{A,B\}$ | tier: aggregator (gated) / background | — ⚠ $A,B$ also used for curvature $A(t,R)$, constant $B(t,R)$ and the constants in (27) |
| $j\in\{b,a\}$, $z\in\{z_1..z_K\}$ | side, RFQ size | $\delta^b,\delta^a$; $K$ = number of sizes ⚠ clashes with branching matrix $K$ |
| $p_z(\delta)$ | win probability | $f(\delta)$ ⚠ not the shadow price $p^j$ |
| $\Lambda^i_z$, $\lambda^i_z(R)$ | baseline RFQ intensity; tier intensity $\lambda^A_z=\Lambda^A_zG(R)$ (eq. 2) | $\lambda_t$, $\mu$ ⚠ $\Lambda$ is not the GLFT amplitude |
| $\mu_z(\delta)\le0$, $\theta_z$ | adverse-selection edge correction; constant slippage | ⚠ not the Hawkes baseline $\mu$ |
| $R$, $\alpha$ | win score (EMA of tier-A wins), EMA weight | no project symbol |
| $G(R)$, $\beta$, $R_0$, $G_{\min}$, $\Delta G$ | promotion gate, logistic steepness, midpoint, floor, contrast (eq. 25) | ⚠ $\beta$ is not a Hawkes decay |
| $\gamma$, $\sigma$, $\eta$ | risk aversion, volatility, terminal penalty | $\gamma,\sigma$ |
| $H_z(x)$, $k^i_z=H''_z(x^i_{0,z})$ | reduced scalar Hamiltonian (eq. 11), its curvature | $H^{i,s}$, $h_2^{i,s}$ |
| $x^i_{z,j}$ | Hamiltonian argument (eq. 14) | (minus) shadow price $p^j$ |
| $A(t,R)$, $B(t,R)$ | quadratic ansatz coefficients (eq. 17) | $A$, $C$ (no linear term) |
| $\xi(R)$ | intensity-weighted liquidity $\sum\lambda^i_zk^i_zz^2$ (eq. 21) | scalar analogue of BEGV $D_+$ |
| $\Phi(R)$, $\rho$, $\zeta$ | continuation term, discount, damping (eqs. 31–32) | ⚠ $\rho$ is not the spectral radius |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (RFQ, aggregators, last look, winner's curse, competition literature, two-tier idea) | 1–2 |
| ✓ F1 | 2 Model: win probability, slippage, gated intensities (eq. 2), EMA score (eq. 3), objective (eq. 4) | 2–3 |
| ✓ F1 | 2.1 Reduced HJB, Bergault–Guéant operator with win/lose branches (eqs. 5–10) | 3 |
| ✓ F1 | 2.2 Envelope theorem and optimal controls (eqs. 11–14) | 4 |
| ✓ F1 | 3 Adiabatic quadratic approximation; 3.1 small-α expansion and quadratic ansatz (eqs. 15–20) | 4 |
| ✓ F1 | 3.2 Ergodic curvature scaling (eq. 21) | 5 |
| ✓ F1 | 3.3 Slow score dynamics and phase transitions (eqs. 22–24) | 5 |
| ✓ F1 | 3.4 Logistic gate and phase-portrait closure (eqs. 25–29) | 5–6 |
| ✓ F1 | 4 Numerical examples (parameters, interval fixed-point scheme eqs. 31–32, eq. 33, Figs. 1–8) | 6–11 |
| ✓ F1 | 5 Concluding remarks (extensions) | 9–10 |
| — | Acknowledgment, References | 11–12 |

## Kernthesen

### 1. ⭐ Aggregator routing makes a dealer's future opportunity flow depend on a slowly varying performance score, which existing control models do not treat as a state (pp. 1–2)

Two empirical facts frame the paper: the competitive set is a ranked subset of LPs («top list +
exploration»), and «inclusion and rank depend on slowly varying performance scores (e.g.,
long-run win ratio, response quality), which in turn depend on how aggressively the LP quotes»
(p. 2). There is «limited academic control literature that treats platform shortlisting driven by
a slow win-score as an explicit state variable feeding back into the LP's future opportunity
intensity» (p. 2).

### 2. ⭐⭐ Two tiers: gated aggregator flow whose outcomes update the score, and ungated background flow that does not (pp. 2–3)

Intensities (eq. 2): $\lambda^A_z(R)=\Lambda^A_zG(R)$, $\lambda^B_z(R)=\Lambda^B_z$, per side and
size, symmetric across sides. The gate $G(R)\ge0$ is monotone; it stands for a game among LPs
that «In the mean-field regime … can be represented as a single-LP stochastic control with a
monotone G(R)» (p. 3). Tier B exists because «inventory risk is managed against all trading
opportunities, not only the ranked stream» (p. 2) and it stabilises the analysis (Kernthese 7).

### 3. ⭐⭐ The score is an event-time EMA of tier-A wins: the dealer's own outcomes feed the intensity (p. 3)

$R\to R^\pm(R):=(1-\alpha)R+\alpha w$, $w\in\{0,1\}$ the win indicator of a tier-A RFQ (eq. 3);
«Tier B outcomes do not update R. When α is small, the score evolves slowly relative to
inventory dynamics» (p. 3). Every tier-A RFQ moves $R$ — up on a win, down on a loss — so the
quote controls both the trade and the future intensity $\Lambda^A_zG(R)$. Size-weighted updates
$w_z=z/z_{\max}$ are mentioned as an option (fn. 3). The score does not decay in calendar time
between RFQs.

### 4. Objective: linear wealth with running and terminal quadratic inventory penalty, latency slippage as an edge correction (pp. 2–3)

$\sup_\delta\mathbb E\big[X_T+q_TS_T-\tfrac\eta2q_T^2-\tfrac{\gamma\sigma^2}2\int_0^Tq_t^2dt\big]$
(eq. 4), after Cartea–Jaimungal–Ricci. Edge on a won RFQ is $\delta+\mu_z(\delta)$ with
$\mu_z\le0$; the benchmark is constant slippage $\mu_z\equiv-\theta_z$ (p. 3). Post-trade price jumps
are excluded «To keep the analysis focused on win-score feedback» (p. 3).

### 5. ⭐⭐ The reduced HJB has a Bergault–Guéant operator with explicit win and lose branches in the score (p. 3)

With $V=x+qS+v(t,q,R)$, $L:=v(t,q,R^-)-v(t,q,R)$ (eq. 5) and
$\Delta^A_{z,j}:=v(t,q\pm z,R^+)-v(t,q,R)$ (eq. 6),
$H^A_z(\Delta)=\sup_\delta\{p_z(\delta)[z(\delta+\mu_z(\delta))+\Delta]+(1-p_z(\delta))L\}=L+\sup_\delta p_z(\delta)[z(\delta+\mu_z)+\Delta-L]$ (eq. 7);
tier B has the standard operator (eqs. 8–9); HJB
$0=\partial_tv-\tfrac\gamma2\sigma^2q^2+\sum_{z,i,j}\lambda^i_z(R)H^i_z(\Delta^i_{z,j})$ (eq. 10).
«with probability $p_z(\delta)$ the dealer wins and trades … while with probability $1-p_z(\delta)$
the dealer loses and only incurs the score downgrade» (p. 3). Here an *unfilled* request also
moves a state variable, but the jump is outcome-dependent ($R^+$ vs $R^-$), unlike Hawkes
flow-driven excitation where filled and unfilled requests move the intensity identically.

### 6. ⭐ Controls follow from the derivative of one scalar Hamiltonian; the score enters only through its argument (p. 4)

$H_z(x):=\sup_\delta p_z(\delta)[z(\delta+\mu_z(\delta))+x]$ (eq. 11); then $H^A_z(\Delta)=L+H_z(\Delta-L)$,
$H^B_z=H_z$. Envelope theorem: $H'_z(x)=p_z(\hat\delta_z(x))$, $\hat\delta_z(x)=p_z^{-1}(H'_z(x))$
(eq. 12), with arguments $x^A_{z,j}=\Delta^A_{z,j}-L$, $x^B_{z,j}=\Delta^B_{z,j}$ (eq. 14). «the
dependence on the non-local value function enters only through the one-dimensional arguments»
(p. 4). Note $x^A=v(q\pm z,R^+)-v(q,R^-)$: the win-versus-lose score difference acts as an extra
"prize" in the shadow price.

### 7. ⭐⭐ Adiabatic split: for small α the score is quasi-static on the inventory time scale, and the score effect is an O(α) additive prize (p. 4)

«we separate: (i) a fast inventory problem conditional on quasi-static R, and (ii) a slow score
dynamics driven by the induced average win probability on tier A» (p. 4), following the
two-scale approach of `barzykin-2026-dynamic-slippage-control`. First order in α (eq. 15):
$v(R^+)\approx v+\alpha(1-R)v_R$; then
$x^A_{z,j}=v(q\pm z,R)-v(q,R)+\alpha[(1-R)v_R(q\pm z,R)+Rv_R(q,R)]+O(\alpha^2)$ (eq. 16). «The
O(α) term acts as an additive reward for winning, a slowly varying "prize" for reaching higher
R … Tight quoting can be optimal even when locally unprofitable because it increases future
tier-A access through R» (p. 4).

### 8. ⭐⭐ Quadratic ansatz with score-dependent coefficients; the score enters the gaps only through $\alpha B_R$ (p. 4)

$v(t,q,R)\approx-\tfrac12A(t,R)q^2+B(t,R)$, $A(T,R)=\eta$, $B(T,R)=0$ (eq. 17; no linear term
by symmetry, fn. 4). «for small q», $v(q\pm z)-v(q)\approx-\tfrac12A(t,R)z(z\pm2q)$ and
$v_R\approx B_R$, so $x^A_{z,j}\approx-\tfrac12A(t,R)z(z\pm2q)+\alpha B_R(t,R)$,
$x^B_{z,j}\approx-\tfrac12A(t,R)z(z\pm2q)$ (eq. 18). Expanding $H_z$ around $x^i_{0,z}$ (eq. 19)
gives win probabilities $\hat y^i_{z,j}\approx y^i_{0,z}(t,R)\mp k^i_z(t,R)\,zq\,A(t,R)$ (eq. 20): the
familiar inventory tilt, with an $O(\alpha)$ level shift on tier A.

### 9. ⭐ Ergodic curvature: $A_\infty(R)$ is set by the total liquidity of both tiers, and tier B keeps it bounded when the gate closes (p. 5)

Matching $q^2$ terms gives «a Riccati-type relation in which the stabilizing contribution comes from
both tiers» with stationary scaling $A_\infty(R)\approx\big(\gamma\sigma^2/2\xi(R)\big)^{1/2}$,
$\xi(R):=\sum_{z,i}\lambda^i_z(R)k^i_z(R)z^2$ (eq. 21; root reconstructed, see Bibliographic
Details). «higher flow makes inventory easier to manage (smaller curvature)» (p. 5). «the
presence of tier B prevents the singular $A_\infty\propto1/\sqrt{G(R)}$ behavior that arises when all
flow is gated» (p. 5). The Riccati equation itself is not displayed (fn. 5).

### 10. ⭐⭐ The slow layer is a one-dimensional score ODE whose fixed points are $\bar y^A(R)=R$ (p. 5)

Tier-A RFQ rate $\lambda^A_{RFQ}(R)=2G(R)\sum_z\Lambda^A_z$ (eq. 22); event-time EMA
$\Delta R_k=\alpha(w_k-R_k)$ gives the drift $\dot R\approx\alpha\lambda^A_{RFQ}(R)\,[\bar y^A(R)-R]$
(eq. 23), with $\bar y^A$ the intensity-weighted tier-A win probability at $q\approx0$ (eq. 24).
«Equilibria satisfy $\bar y^A(R)=R$, and stability is determined by $\bar y^{A\prime}(R)-1$» (p. 5).
Tier B enters «indirectly through the fast-scale coefficients $A_\infty(R)$» (p. 5).

### 11. ⭐ A postulated reduced-form closure for $\bar y^A$ plus a logistic gate yields fold bifurcations, bistability and hysteresis (pp. 5–6)

Gate $G(R)=G_{\min}+\Delta G\,u$, $u=(1+e^{-\beta(R-R_0)})^{-1}$ (eq. 25). «one may postulate a
reduced-form closure» $\bar y^A(R)\approx\bar y^\star+\mathcal A[\xi(R_0)^{-1/2}-\xi(R)^{-1/2}]+\alpha\mathcal BG'(R)$
(eq. 27), constants $\mathcal A,\mathcal B>0$ «can be estimated from the quadratic expansion»
(p. 6). With frozen curvatures $k^A_z\approx k^B_z$ this gives the scalar fixed-point equation
(28) and fold condition (29). At least one fixed point exists; «For sufficiently strong score
feedback (large α and/or steep β), the bell-shaped campaign term can generate two additional fixed
points through a fold bifurcation, producing a hysteresis loop» (p. 6). The phase-portrait
closure is heuristic, not derived.

### 12. ⭐ Numerics solve the full $(t,q,R)$ HJB with a block-interval fixed point that propagates multi-day score incentives (pp. 6–7)

Time-scale problem: for α = 0.01 the EMA half-life is ≈ 70 trades ≈ 3.5 days at $G_{\min}$, while
$dt\ll 1/\sum\Lambda_z\approx30$ s, so ≳ $10^6$ steps (p. 6). Instead the HJB is solved on short
blocks $[0,T]$ with terminal condition $v(T,q,R)=-\tfrac12\eta q^2+e^{-\rho T}\Phi(R)$, iterating
$\Phi^{(n+1)}=(1-\zeta)\Phi^{(n)}+\zeta v^{(n)}(0,0,R)$ (eqs. 31–32), with Anderson acceleration;
$T=0.05$ day, $10^4$ steps (p. 7). This introduces a discount rate ρ absent from objective (4).

### 13. Parameters: a narrow-size aggregator client on top of a large background franchise (p. 6)

Sizes $z=(1,2,5,10)$M; $\Lambda^B_z=(1000,800,600,400)$/day; $\bar\Lambda^A_z=(0,0,0,50)$/day
(only the 10M bucket is gated); sigmoid $p_z(\delta)=(1+e^{\kappa_z(\delta-\bar\delta_z)})^{-1}$,
$\kappa_z=(5.0,4.5,4.0,3.5)$/bp, $\bar\delta_z=(0.3,0.4,0.5,0.6)$; $\theta_z=0.2$ bp; daily vol 100
bp; $\gamma=10^{-3}$/(bp·M); $G_{\min}=0.2$, $R_0=0.6$, $\beta=40$, $\alpha=0.01$ (p. 6) — «≈ 2
billion notional» daily turnover, top-of-book spread ≈ 1 bp.

### 14. ⭐⭐ Optimal policy alternates "campaign" (tighten near the gate midpoint) and "harvest" (widen above it, but not to the no-feedback level) (pp. 7–9, Figs. 2–5)

Fig. 2 shows «a dip in quote offset for tier A at zero inventory in the vicinity of $R_0$ — the
signature of campaigning. Above $R_0$, the dealer would like to "harvest" and widens spread, but
clearly not fully back to the level without feedback (α = 0)» (p. 7). «high score is not a
riskless asset and maintenance costs» (p. 7). Tier-A instantaneous PnL (eq. 33) drops during the
campaign and «rises sharply to enjoy harvesting» (Fig. 4); campaign ↔ positive $\dot R$ and low
PnL (Fig. 5, p. 7).

### 15. ⭐ Score feedback creates bistability; steeper gates widen it (pp. 7–8, 11, Figs. 6–8)

«While the myopic model with α = 0 exhibits a single fixed point, the score feedback can give
rise to bistable behavior with three fixed points and two basins of attraction» (p. 7). Fig. 7
(slow ODE (23) with optimal controls): below the lower fold campaigning is not worth it; inside
the bistable region an aggressive campaign can cross the unstable point (p. 8). Fig. 8: «As β
decreases, a stable + unstable pair annihilates leaving one stable branch, which further gradually
evolves to the myopic limit» (p. 8).

### 16. Background flow is the stabiliser, and residual flow shapes behaviour on the ranked stream (pp. 2, 10)

«Even when the promotion gate is near its minimum, the background stream maintains a baseline of
inventory-mixing opportunities, preventing pathological blow-ups in the effective inventory
curvature» (p. 10).

### 17. Extensions named: finite-N shortlisting and competition, informational adverse selection, multi-dimensional scores, calibration from RFQ logs (p. 10)

The gate «can be endogenized further by linking it to explicit top-list + exploration rules …
and to cross-sectional competition»; «the score itself could be multi-dimensional (wins, response
times, hold times, reject rates)»; calibrate $p_z$, $G$ and α from RFQ logs and test predicted
campaign/harvest regimes (p. 10).

## What this source does not address

- **Hawkes or any self-exciting request flow.** RFQ opportunities are Poisson given $R$; the only
  memory is the EMA score.
- **Several assets.** One instrument; "multi" means sizes × sides × two tiers.
- **Accuracy of the adiabatic approximation.** No regret, value gap or quote error of the
  adiabatic/quadratic closure against the full HJB is reported; the reduced closure (27) is
  postulated and its constants are not computed.
- **Equilibrium among LPs.** The gate is a mean-field reduced form (p. 3); no game is solved.
- **CARA utility, price dynamics coupled to flow, post-trade informational drift** (p. 3, p. 10).

## Model card

- **Assets:** 1 (FX-style instrument); size ladder $z\in\{1,2,5,10\}$M, two sides, two tiers.
- **Kernel:** n/a — no Hawkes kernel. Tier-A intensity $\Lambda^A_zG(R)$ is modulated by a score $R$ with geometric memory in RFQ event count (EMA weight α, eq. 3); tier B constant Poisson.
- **Excitation:** self-feedback through the score on tier A only (wins raise future tier-A flow, losses lower it); no cross-side or cross-asset excitation.
- **Who excites the flow:** the dealer's own *outcomes* (wins vs losses) on every tier-A request — controlled, outcome-driven; neither pure flow-driven nor pure fill-driven, since a lost request also moves $R$ (downwards).
- **Objective:** risk-adjusted linear wealth with running and terminal quadratic inventory penalty (eq. 4), not CARA; numerics add a discount ρ (eq. 31).
- **Solution method:** full HJB on a $(q,R)$ grid, explicit backward Euler on short blocks with a stationary continuation fixed point and Anderson acceleration (eqs. 31–32, p. 7); analytically an adiabatic small-α expansion + BEGV quadratic ansatz/Hamiltonian expansion giving $A_\infty(R)$ and a 1-D score ODE (Sec. 3).
- **Benchmark:** the no-feedback (α = 0, «myopic») policy; background tier B quotes.
- **Reported numbers:** none for regret or approximation gap; qualitative figures (quote dips, PnL, phase portraits, bifurcation diagram).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 3, 5, 6, 7, 8, 9, 10, 11, 12.** The paper has no Hawkes flow; read under
the focus as a control-feeds-the-intensity model with a slow memory state.

### What this focus needs beyond the Kernthesen

1. **How the slow score enters.** $R$ is a genuine state of the value function $v(t,q,R)$; the
   intensity $\Lambda^A_zG(R)$ is a deterministic function of that state, and the state jumps by
   $\pm$ on every tier-A request, with the sign set by the controlled win/loss (eqs. 3, 5–7). The
   control therefore feeds the intensity — the case `barzykin-2026-hawkes-driven-otc` excludes by
   construction («requests, not the dealer's controlled executions, drive the Hawkes memory», that
   paper p. 6).
2. **How it is frozen.** Three separate freezing steps, in order: (a) *small-α Taylor step* (eq. 15)
   turns the nonlocal score jumps $R^\pm$ into a local first-order term $\alpha v_R$, so the
   score effect becomes an additive prize $\alpha B_R$ in the Hamiltonian argument (eqs. 16, 18);
   (b) *quasi-static R* on the fast scale — the fast inventory problem is solved «conditional on
   quasi-static R» and $A(t,R)$ «relaxes quickly to a quasi-stationary value at fixed R», giving
   $A_\infty(R)$ (eq. 21) with $R$ acting as a parameter; (c) *frozen microstructure curvatures*
   $k^A_z\approx k^B_z\approx k_z$ near the fast equilibrium (p. 6) plus the postulated closure
   (27) for the score drift. This is structurally the same move as Barzykin's forecast freezing
   (state → parameter), but here justified by a time-scale separation (α small) rather than by a
   certainty-equivalent argument.
3. **Where the quadratic closure breaks, and how the paper hides it (inference).** With
   $v=-\tfrac12A(t,R)q^2+B(t,R)$, the exact tier-A argument is
   $x^A=v(q\pm z,R^+)-v(q,R^-)$, which contains $-\tfrac12[A(R^+)-A(R^-)]q^2\approx-\tfrac12\alpha A_Rq^2$
   (+ cross terms). Inserting it into the curvature term $\tfrac12k(x-x_0)^2$ produces $q^3$ and
   $q^4$ terms — exactly the fill-driven non-closure recorded on [[who-excites-the-flow]] and in
   [[problem-anatomy]] §3a. The paper drops it by setting $v_R\approx B_R$ «for small q» (p. 4).
   So the BEGV closure here is exact in $q$ only up to $O(\alpha q^2)$; it holds in the adiabatic
   limit, not in general. *Not stated by the author.*
4. **D2 — score-dependent Riccati coefficients.** The coefficients $A(t,R)$, $B(t,R)$ are
   functions of the memory state, i.e. the analogue of $\lambda$-dependent Riccati coefficients.
   The paper never writes the PDE in $R$ for them (fn. 5: «Details follow the standard
   Bergault-Guéant calculations»); it only uses the stationary $A_\infty(R)$ pointwise in $R$. With
   the small-α step the jump in $R$ becomes a drift-type term, so the full coefficient system would
   be a first-order transport PDE in $R$ (inference), not a nonlocal transport-jump system. That is
   a cleaner analogue of D2 than the Hawkes case: one memory variable, local after Taylor
   expansion.
5. **Closure status of the exact problem.** The exact problem is a 2-D $(q,R)$ HJB solved on a
   grid (Kernthese 12); the adiabatic layer is never quantitatively compared with it. No regret
   numbers exist.
6. **Multi-asset carry-over: not discussed.** One asset. *Inference:* with several assets and a
   shared platform score, $R$ would couple assets through the gate even without cross-asset
   excitation (a win in asset $i$ raises flow in asset $j$), giving a fill-/outcome-driven
   cross-asset channel; the curvature would become BEGV's matrix $A$ with $D_+(R)$. The paper's
   «multi-dimensional score» extension (p. 10) is about score components, not assets.

### Direct quotes (for the draft)

> "When α is small, score changes are slow relative to inventory dynamics. Following the two-scale philosophy used in our earlier last look reputation study [5], we separate: (i) a fast inventory problem conditional on quasi-static R, and (ii) a slow score dynamics driven by the induced average win probability on tier A." (p. 4)

> "The O(α) term acts as an additive reward for winning, a slowly varying "prize" for reaching higher R. It is proportional to the marginal value vR and is strongest where vR is large, which in turn is tied to the steepness of the routing gate G(R). Tight quoting can be optimal even when locally unprofitable because it increases future tier-A access through R." (p. 4)

> "On the fast scale, A(t, R) relaxes quickly to a quasi-stationary value at fixed R. Matching q² coefficients in the reduced HJB under the quadratic Hamiltonian expansion yields a Riccati-type relation in which the stabilizing contribution comes from both tiers." (p. 5)

> "the presence of tier B prevents the singular A∞ ∝ 1/√G(R) behavior that arises when all flow is gated" (p. 5)

### Examples & illustrations (for later drafting)

- Fig. 2 (p. 8): tier-A 10M offset at $q=0$ vs $R$ — a dip near $R_0=0.6$ for α = 0.01, flat for
  α = 0: the cleanest picture of a control that buys future intensity.
- Fig. 6 / Fig. 8 (pp. 10–11): three fixed points of $\dot R$ for β = 40; pair annihilation as $1/\beta$
  grows — an example of how intensity feedback through the control changes the qualitative
  dynamics, not only the quote level.
- Time-scale arithmetic (p. 6): score half-life ≈ 70 trades ≈ 3.5 days vs quote step ≪ 30 s — why
  freezing the slow state is natural here.

### Boundary of this focus

No self-/cross-exciting point process appears; the "excitation" is a deterministic gate of a
controlled score. The closure analysis (item 3) and the multi-asset reading (item 6) are the
project's inference. No accuracy numbers exist for the adiabatic approximation.

## Mentioned entities

- Models: [[begv-2021-model]], [[glft-2013-model]], [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]]
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[who-excites-the-flow]], [[shadow-price]]
- Other works (bibkeys): `barzykin-2026-dynamic-slippage-control` (two-scale precedent, ref. [5]), `bergault-2021-size-matters-otc` (Bergault & Guéant 2021, size ladders, ref. [6]; key not verified), `barzykin-2023-algorithmic-market-making` (ref. [3]; key not verified), `barzykin-2025-optimal-quoting-adverse` (ref. [4]), `oomen-2017-execution-aggregator`, `oomen-2017-last-look`, `fermanian-2016-behavior-dealers-clients`, `boyce-2024-market-making-exogenous`; not in the wiki: Walker & Ni 2011 (Anderson acceleration).

## Connections

- Builds on: [[bergault-2021-closed-form-approximations]] / [[begv-2021-model]] (quadratic ansatz and Hamiltonian expansion, here with score-dependent coefficients).
- Cites: [[cartea-2014-buy-low-sell]] (objective), [[gueant-2013-dealing-inventory-risk]], [[avellaneda-stoikov-model]].
- Cited by and continued in: [[barzykin-2026-bond-market-making]] (ref. [3] there; same HSBC desk line, hit ratio as a control target rather than a state).
- Contrast: [[barzykin-2026-hawkes-driven-otc]] — there requests drive the memory and the forecast is quote-independent; here the dealer's outcomes drive the memory. Both freeze the memory state to reach a Riccati layer.
- Evidence for [[who-excites-the-flow]] (outcome-driven case) and for D2 in [[problem-anatomy]].
