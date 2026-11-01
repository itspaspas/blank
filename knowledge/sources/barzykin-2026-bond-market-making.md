---
title: "Barzykin & Ciceri 2026 — Bond Market Making with a Hit-Ratio Target"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: barzykin-2026-bond-market-making
depth: standard
tags: [market-making, otc, rfq, corporate-bonds, hit-ratio, size-ladder, multi-asset, multi-tier, dualization, matrix-riccati, begv, closed-form, poisson-flow]
relations:
  - target: bergault-2021-closed-form-approximations
    type: builds-on
    confidence: extracted
    because: "«Following Bergault et al. (BEGV) [5], we expand the Hamiltonians to the second order in p around 0» (eq. 20, p. 5); [5] = Bergault, Evangelista, Guéant, Vieira 2021 (p. 13). Quadratic ansatz (22) → matrix Riccati (29) and closed form (32)–(33)."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "M-bond quadratic ansatz u ≈ −½qᵀA(t)q − C(t) (22) with BEGV Hamiltonian expansion gives A′ = ADA − ϕΣ (29), solved in closed form (32); for M = 1 it «reduces to the classical one-dimensional BEGV equation» (p. 7)."
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "Second-order expansion (20) (p. 5); refined variant keeps the quadratic value but uses the exact Hamiltonian response in the dual closure: «the value function is kept quadratic, while the nonlinear quote-to-intensity map is preserved exactly» (p. 6). Accuracy vs exact HJB shown in Figs. 1–3 (pp. 7–9)."
  - target: matrix-riccati-equation
    type: supports
    confidence: extracted
    because: "«matching the quadratic terms then yields the matrix Riccati equation A′(t) = A(t)DA(t) − ϕΣ, A(T) = ηΣ» with diagonal D (eqs. 29–30, p. 6); explicit sinh/cosh solution (32) and stationary A = ϕD^{-1/2}(D^{1/2}ΣD^{1/2})^{1/2}D^{-1/2} (33). Non-symmetric case: modified D̃ ≻ 0 proved (Appendix A, pp. 14–15)."
  - target: barzykin-2026-win-score-promotion
    type: cites
    confidence: extracted
    because: "«Barzykin [3] further investigates the role of the win-score promotion gates in aggregator-routed RFQ markets» (p. 1); [3] = arXiv:2603.10569 (p. 13)."
  - target: bergault-2023-liquidity-dynamics-rfq
    type: cites
    confidence: extracted
    because: "«Bergault and Guéant [6] further study liquidity dynamics and pricing in RFQ markets using Markov-modulated order-flow models» (p. 2); [6] = arXiv:2309.04216 (p. 13)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "Ref. [9] (p. 13), cited among stochastic-control approaches to OTC market making [1, 13, 9, 10, 14] (p. 2)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Ref. [13] (p. 13), cited among stochastic-control approaches to OTC market making (p. 2)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "Ref. [1] (p. 13), cited among stochastic-control approaches to OTC market making (p. 2)."
  - target: shadow-price
    type: mentions
    confidence: extracted
    because: "Shadow price p (16) = reduced increment Δu minus the optimal dual variable ξ̃_τ for targeted tiers; the hit-ratio target acts as a tier-wide shift of the shadow price (eqs. 16, 18, 38, pp. 4, 7)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Neither convention applies: RFQ arrivals are exogenous constant intensities λ^m_{s,k,τ} (p. 3, eq. 3), so nothing excites the flow; the only flow-related feedback is a penalty on the expected hit ratio in the objective (8)."
---

# Bond Market Making with a Hit-Ratio Target

## Bibliographic Details

Barzykin, Alexander, and Axel Ciceri. 2026. *Bond Market Making with a Hit-Ratio Target*.
arXiv:2604.20406v2 [q-fin.RM], 27 July 2026. 17 pp. Affiliation: HSBC, London.

**Read: arXiv 2604.20406v2 (preprint); page/equation numbers follow it.** No published version is
known at ingest (2026-10-26), so under the project's preprint policy the preprint is its own
original (no `based_on`). Non-core work.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $m\in\mathcal M=\{1,\dots,M\}$ | bond index | asset index; $M\leftrightarrow d$ |
| $\tau\in\mathcal T$, $\mathcal A\subseteq\mathcal T$ | client tier; targeted tiers | ⚠ $\tau$ is not a time |
| $k$, $z_k$ | size-ladder rung, size | — |
| $S^m_t$, $\sigma^m$, $\Sigma$ | mid prices, vols, covariance | $S_t,\sigma,\Sigma$ |
| $Q_t$, $q$, $X_t$ | inventory vector, cash | $q_t$, $X_t$ |
| $\delta^m_{s,k,\tau}$ | quote offset | $\delta^b,\delta^a$ |
| $\lambda^m_{s,k,\tau}$ | exogenous constant RFQ intensity | ⚠ constant, not a Hawkes $\lambda_t$ |
| $f^m_{s,k,\tau}(\delta)$, $\Lambda^m_{s,k,\tau}=\lambda f$ | fill probability, fill intensity | $f(\delta)$; ⚠ $\Lambda$ here is the fill intensity, not the GLFT amplitude |
| $W_\tau$, $r_\tau(\delta)$, $r^\star_\tau$, $\kappa_\tau$ | notional-arrival scale (6), size-weighted instantaneous hit ratio (7), target, penalty weight | — |
| $\phi$, $\eta$ | running / terminal inventory-penalty coefficients on $q^\top\Sigma q$ | $\phi\approx\gamma$ in a risk-adjusted objective; ⚠ $\eta$ not a threshold |
| $u(t,q)$ | reduced value function | $\theta$ |
| $\Delta^m_{s,k}u$, $p^m_{s,k,\tau}$ | reduced increment (11), shadow price (16) | $p$ |
| $H^m_{s,k,\tau}(p)$ | Hamiltonian (14), with $\lambda$ inside | $H$; $H''(0)\leftrightarrow h_2$ (×λ) |
| $\xi_\tau$, $\tilde\xi_\tau$ | dual variable of the hit-ratio penalty; its optimum | ⚠ not Barzykin 2026's score increment |
| $A(t)$, $B(t)$, $C(t)$ | quadratic, linear, constant value coefficients (22), (41) | $A,B,C$ (same sign convention as BEGV) |
| $D=\mathrm{diag}(d_m)$, $G$ | curvature matrix (30); $G=(D^{1/2}\phi\Sigma D^{1/2})^{1/2}$ (31) | ⚠ $D$ is **not** $\mathrm{diag}(\beta)$ |
| $\tilde\delta_0$, $c$ | riskless spread (34), linearisation constant (36) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (bond RFQ microstructure; hit ratio as an equilibrium object and a routing KPI; credit-spread/DV01 convention) | 1–2 |
| ✓ F1 | 2.1 State dynamics and objective (1)–(8); Markovian surrogate for the hit-ratio KPI | 2–4 |
| ✓ F1 | 2.2 Reduced HJB (9)–(11), dualisation (12)–(14), exact controls (15)–(19) | 4–5 |
| ✓ F1 | 2.3 Quadratic approximation: ansatz (22), dual closure (26)–(28), matrix Riccati (29)–(30), closed form (31)–(33), refined closures | 5–6 |
| ✓ F1 | 2.4 Linearised quotes (34)–(38) | 6–7 |
| ✓ F1 | 3 Numerical examples: single bond/tier, exact vs BEGV levels (Figs. 1–3); κ sweep and forward Kolmogorov evaluation (39)–(40), Figs. 4–5; background tier (Figs. 6–7); correlated background bond (Figs. 8–9) | 7–10 |
| ✓ F1 | 4 Concluding remarks | 10–12 |
| — | References | 13–14 |
| ✓ F1 | Appendix A: non-symmetric intensities — linear term, $q$-dependent dual, modified $\tilde D\succ0$, $B(t)$ ODE (41)–(55) | 14–16 |
| ✓ | Appendix B: local quadratic expansion of the dual variable (56)–(66) | 16–17 |

## Kernthesen

### 1. ⭐ The hit ratio is an equilibrium object and a routing KPI, but the control literature treats execution probability only in reduced form (pp. 1–2)

The cited RFQ literature implies «that the dealer's hit ratio is not an exogenous statistic, but an
equilibrium object shaped by platform design, client search, and rival participation» (p. 1).
Control models treat execution probability «in reduced form—typically through quote-dependent
intensities or fill probabilities—rather than elevating hit ratio itself to an explicit control
target» (p. 2). In practice historical hit ratios are used to select dealers and route RFQs (p. 2).

### 2. ⭐⭐ Multi-bond, multi-tier, size-ladder model with exogenous constant RFQ intensities and quote-dependent fill probabilities (pp. 2–3)

$dS^m_t=\sigma^m dB^m_t$, covariance Σ (1). RFQs for bond $m$, tier τ, side $s$, size $k$ arrive at
«exogenous intensity» $\lambda^m_{s,k,\tau}\ge0$; fill probability $f^m_{s,k,\tau}(\delta)$ (2); fill
intensity $\Lambda=\lambda f$ (3); inventory and cash (4)–(5) (p. 3). Flow is Poisson: no memory, no
excitation, no regime.

### 3. ⭐⭐ Objective: risk-adjusted P&L with Σ-weighted inventory penalties plus a quadratic penalty on the size-weighted instantaneous hit ratio per targeted tier (p. 3)

$r_\tau(\delta)=\frac1{W_\tau}\sum_{m,s,k}z_k\Lambda^m_{s,k,\tau}(\delta)$ with $W_\tau=\sum z_k\lambda$
(6)–(7). Objective (8): $\sup_\delta\mathbb E[X_T+Q_T^\top S_T-\frac\eta2Q_T^\top\Sigma Q_T-\int_0^T(\frac\phi2Q_t^\top\Sigma Q_t+\sum_{\tau\in\mathcal A}\frac{\kappa_\tau}2W_\tau(r_\tau(\delta_t)-r^\star_\tau)^2)dt]$.
Sub-tier targets by splitting a tier (fn. 2, p. 3).

### 4. The instantaneous expected hit ratio is a Markovian surrogate for the windowed desk KPI (pp. 3–4)

A literal windowed hit ratio «would therefore require additional state variables describing
cumulative request and trade counts, and the objective would involve a ratio of counting
processes. While feasible in principle, this would significantly complicate the stochastic-control
problem and break much of the tractability sought here» (p. 3). The surrogate is justified «when
RFQs arrive at high frequency and market conditions vary more slowly than individual request
outcomes» (p. 4).

### 5. ⭐⭐ Dualising the quadratic target restores separability of the Hamiltonians (p. 4)

The penalty is nonlinear in the sum of fill intensities, so the HJB (9) does not split by
bond/side/size. Using $-\frac\kappa2(r-r^\star)^2=\inf_\xi[\xi(r-r^\star)+\xi^2/(2\kappa)]$ (12) gives
(13), where each targeted tier contributes $\inf_{\xi_\tau}W_\tau[-\xi_\tau r^\star_\tau+\xi_\tau^2/(2\kappa_\tau)+\frac1{W_\tau}\sum z_kH^m_{s,k,\tau}(\Delta^m_{s,k}u-\xi_\tau)]$
with the standard Hamiltonian $H(p)=\sup_\delta\Lambda(\delta)(\delta-p)$ (14). The target acts as a
**tier-wide shift of the shadow price** by $\tilde\xi_\tau$ (16).

### 6. ⭐ Exact optimal quotes follow from the inverse fill function and the Hamiltonian derivative; the dual is an implicit fixed point (pp. 4–5)

$\tilde\delta(p)=f^{-1}(-H'(p)/\lambda)$ (15); $\delta^\star=\tilde\delta(p(t,q))$ (18), «an exact
formula». $\tilde\xi_\tau=\kappa_\tau(r^\star_\tau+\frac1{W_\tau}\sum z_kH'(p))$ (19) — «an implicit
characterization because $p^m_{s,k,\tau}$ itself depends on $\tilde\xi_\tau$» (p. 5).

### 7. ⭐⭐ Under BEGV the dual becomes inventory-independent and the curvature solves a matrix Riccati with diagonal D summing all tiers (pp. 5–6)

With the quadratic ansatz (22) and expansion (20), «the q-terms cancel bond by bond in (19) after
summing bid and ask contributions», giving $\tilde\xi_\tau(t)=\tilde\kappa_\tau y_\tau(t)$ (26)–(28),
where $y_\tau$ depends on $A_{mm}(t)$ (p. 5). Matching $q^2$: $A'(t)=A(t)DA(t)-\phi\Sigma$,
$A(T)=\eta\Sigma$, $D=\mathrm{diag}(d_m)$, $d_m=\sum_{\tau,s,k}z_kH''^m_{s,k,\tau}(0)$ (29)–(30).
«Thus all available bonds contribute to the inventory curvature, regardless of their belonging
to a target tier» (p. 6). The hit-ratio target does not enter $A$ in the symmetric case.

### 8. ⭐⭐ The matrix Riccati has an explicit sinh/cosh solution and a stationary limit (p. 6)

With $D\succ0$, $\tilde t=T-t$, $G=(D^{1/2}\phi\Sigma D^{1/2})^{1/2}$ (31):
$A(t)=D^{-1/2}G[\sinh(\tilde tG)+\frac\eta\phi G\cosh(\tilde tG)][\cosh(\tilde tG)+\frac\eta\phi G\sinh(\tilde tG)]^{-1}D^{-1/2}$
(32); as $\tilde t\to\infty$, $A=\phi D^{-1/2}(D^{1/2}\Sigma D^{1/2})^{1/2}D^{-1/2}$ (33). «The matrix
Riccati equation can be readily solved» (p. 6).

### 9. ⭐ Refined closures keep the quadratic value but use the exact Hamiltonian response in the dual; ξ(q) is strongly nonlinear (pp. 6, 8–9, App. B)

«A more accurate approach keeps the value-function as derived above in terms of A(t) in (32), but
revisits the dual variable closure (19) with the exact nonlinear Hamiltonian response» — a scalar
fixed point per targeted tier and $q$, «fully in the spirit of BEGV» (p. 6). Appendix B expands it
around $q=0$: $\nabla_q\xi_\tau(t,0)=0$ by side symmetry, so «the first nontrivial correction is
quadratic» (p. 17), $\xi_\tau\approx\xi_\tau(t)+\frac12q^\top\mathcal B_\tau(t)q$ (65)–(66), with
$\mathcal B_\tau$ driven by $H'''$. Fig. 3: «the exact ξ(q) is indeed strongly nonlinear
(approximately quadratic), explaining why the constant closure approximation is poor» (p. 7).

### 10. ⭐ Linearised quotes decompose into riskless spread, inventory skew and a hit-ratio correction (pp. 6–7)

Linearising (15) at $p=0$: $\tilde\delta\approx\tilde\delta_0+p/c$ (35)–(36), with $H'(0)=-\Lambda(\tilde\delta_0)$,
$H''(0)=\Lambda(\tilde\delta_0)/(\tilde\delta_0c)$ (37). Quotes (38): $\tilde\delta_0+\frac1c e_m^\top A(\pm q+\frac12z_ke_m)-\frac1c\tilde\xi_\tau$
for targeted tiers. «The sign and magnitude of each $\tilde\xi_\tau$ summarize whether the
corresponding targeted RFQ flow must be subsidized or harvested relative to the riskless-spread
benchmark» (p. 7).

### 11. ⭐⭐ Against the exact HJB (one bond, one tier), the quadratic value with the exact quote map and exact dual closure is «impressively accurate»; cruder closures degrade with inventory (p. 7, Figs. 1–3)

Size ladder $z=(1,5,20)$M, $\lambda=(500,200,50)$/day, sigmoid win probability, $r^\star=0.1$,
$\phi=1$, $T=1$ day, $q_{\max}=100$M, explicit Euler in JAX (p. 7). Exact closure $\xi(q)$:
«impressively accurate»; second-order closure $\xi_0+\xi_2q^2$: deviation «somewhat significant
only for larger inventories»; constant $\xi_0$: «good only for small inventories»; linearised quote
map: «any nonlinearity is lost by construction» (p. 7). Comparison is visual; no error number.

### 12. Hit-ratio targeting trades P&L against target attainment; desk statistics come from the forward Kolmogorov law of inventory (pp. 7–9, Figs. 4–5)

Larger κ tightens prices most at small inventory (Fig. 4). The stationary policy induces a
Markov chain on the inventory grid; its law solves (39), and the expected size-weighted hit ratio
is (40) (pp. 8–9). «spending more on target generally implies less P&L» (p. 9, Fig. 5).

### 13. ⭐ Untargeted tiers and correlated bonds share inventory risk and relieve the targeted tier (pp. 9–10, Figs. 6–9)

Background tier: $D$ sums all tiers, the dual only the targeted one, so «untargeted tiers
contribute to the inventory curvature but not directly to the hit-ratio correction» (p. 10); pricing
becomes less skewed and the expected hit ratio improves with the background share (Figs. 6–7).
Two bonds, correlation ρ = 0.8: «the quote on bond m depends on the full inventory vector through
$e_m^\top A(t)q$» and «the skew of the bond in the targeted tier is significantly reduced when there
is an offsetting inventory in the background bond» (p. 10, Figs. 8–9).

### 14. ⭐ Asymmetric intensities add a linear term, a q-dependent dual, and a rank-corrected curvature matrix that stays positive definite (pp. 14–16, App. A)

$u\approx-\frac12q^\top Aq-B^\top q-C$ (41). $\tilde\xi_\tau(t,q)=\tilde\kappa_\tau y_\tau+\frac{\tilde\kappa_\tau}{W_\tau}\sum_mh^{m,\tau}_{12}(e_m^\top Aq+B_m)$
(43): «the q-dependence is generically present» (p. 14). Riccati (45) with
$\tilde D=D-\sum_{\tau\in\mathcal A}\frac{\tilde\kappa_\tau}{W_\tau}\sum_{m,m'}h^{m,\tau}_{12}h^{m',\tau}_{12}e_me_{m'}^\top$ (46);
strict convexity of $H$ gives $|h^{m,\tau}_{12}|<d_{m,\tau}$ and hence $\tilde D\succ0$ (47) (p. 15). So the
target couples bonds in the curvature (a rank-one correction per tier) only when intensities are
asymmetric. $B$ solves a linear ODE (51)–(53), stationary $B=D^{-1/2}G^{-1}D^{1/2}Y$ (54).

### 15. The analysis is not bond-specific (p. 12)

«Although the discussion was motivated in part by bond RFQ workflows, the analysis is not
bond-specific. The same modelling ideas apply more broadly to RFQ markets» (p. 12). Bonds are risk
managed in credit-spread terms; the price formulation is consistent with that if DV01 is constant
on the risk-management timescale (p. 2).

## Figures and tables

Not extracted (exact-vs-approximation plots are qualitative). Parameter sets are transcribed in
Kernthesen 11 and 13.

## What this source does not address

- **Self- or cross-exciting flow, or any stochastic intensity.** RFQ intensities are constant and
  exogenous (p. 3). Markov-modulated liquidity is only cited ([6], p. 2).
- **Hit ratio as a state.** The windowed KPI is replaced by an instantaneous expected hit ratio,
  explicitly to avoid extra counting-process states (p. 3).
- **Quantified approximation error.** Exact-vs-BEGV comparison is visual and only for one bond and
  one tier (Figs. 1–3); no regret or gap numbers, and no exact solution for $M>1$.
- **Competition, client search, hedging** (cited, not modelled).
- **CARA utility, RL/neural methods.** None.

## Model card

| Field | Value |
|---|---|
| Assets | $M$ bonds (numerics: 1 or 2), multiple client tiers, size ladder $K$ rungs |
| Kernel | Poisson — constant exogenous RFQ intensities $\lambda^m_{s,k,\tau}$ (p. 3) |
| Excitation | none (no self, cross-side or cross-asset excitation) |
| Who excites the flow | n/a — flow is exogenous; quotes affect only the fill probability |
| Objective | risk-adjusted: P&L minus $\frac\phi2\int q^\top\Sigma q$, $\frac\eta2q_T^\top\Sigma q_T$, and $\frac{\kappa_\tau}2W_\tau(r_\tau-r^\star_\tau)^2$ per targeted tier (eq. 8); not CARA |
| Solution method | exact reduced HJB with dualised hit-ratio penalty (13) solved by explicit Euler (JAX) for $M=1$; BEGV quadratic ansatz + Hamiltonian expansion → matrix Riccati (29) with closed-form sinh/cosh solution (32)/(33); refined closures for the dual (exact scalar fixed point; local quadratic expansion, App. B); linearised quotes (38) |
| Benchmark | exact numerical HJB solution (single bond, single tier) |
| Reported regret / gap numbers | none — visual comparison only (Figs. 1–3) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 2, 5, 7, 8, 9, 11, 13, 14.** No excitation: read under the focus as a
current multi-asset BEGV closed form under Poisson flow, with one extra nonlinearity in the
objective.

### What this focus needs beyond the Kernthesen

1. **Excitation: none.** Constant exogenous RFQ intensities (p. 3). The paper is relevant for the
   *closure* half of the focus only.
2. **Where the closure holds.** With constant intensities, BEGV gives an exact-in-structure matrix
   Riccati (29) with a constant diagonal $D$ and therefore a closed form (32)–(33). The extra
   nonlinearity (a quadratic penalty on a sum of fill intensities) is removed by Legendre
   dualisation and enters only as a tier-wide shadow-price shift. Under side symmetry that shift
   is $q$-independent and leaves $A$ untouched (Kernthese 7).
3. **Where it breaks.** (a) The constant dual closure fails at larger inventory because the exact
   $\xi(q)$ is about quadratic in $q$ (Fig. 3, p. 9); the fix is to keep $A$ and solve the dual
   pointwise. (b) Asymmetric intensities make the dual $q$-dependent and push a rank-one term into
   the curvature, $\tilde D=D-\dots$ (46), which is proved to stay $\succ0$ (Appendix A).
4. **Multi-asset carry-over.** Cross-asset coupling comes only from Σ in the Riccati (and, in the
   asymmetric case, from the target's rank-one term in $\tilde D$). Fig. 8–9 show a correlated
   background bond reducing the targeted bond's skew (p. 10). [I] With diagonal Σ and symmetric
   intensities, (33) gives a diagonal $A$ — consistent with the Stage 2a lemma S4a (diagonal Σ,
   separable penalty ⇒ $A$ diagonal) in the constant-intensity case.

### Bearing on Stage 2a (perturbative closed form)

- **Order-0 closed form [I].** If Stage 2a's deterministic forecast starts at the stationary
  intensity $m_\infty$, then $m(t)\equiv m_\infty$, the order-0 curvature matrix
  $D^0=\sum_jm_{\infty,j}h_2(\cdot)$ is constant, and $A^0(t)$ is exactly (32) with
  $G=(D^{0\,1/2}\phi\Sigma D^{0\,1/2})^{1/2}$. Off stationarity, $D^0(t)$ varies and (32) no longer
  applies. Use (32)/(33) as the $K\to0$ and stationary-start check in S2.
- **Positive-definiteness technique for S1.** Appendix A proves that a diagonal $D$ minus a rank
  correction stays positive definite from strict convexity of $H$ (47). A similar argument may bound
  the order-1 perturbation $A^0+\varepsilon\sum\tilde\Delta_kA^1_k$ [I].
- **Accuracy protocol.** The three-level comparison (exact HJB; quadratic value + exact quote map;
  linearised map) matches Stage 2a's split of perturbation error from Hamiltonian-expansion error.
  The paper finds the quadratic value with the exact quote map «impressively accurate» at $M=1$
  under Poisson flow (p. 7) — a qualitative prior for the size of the Hamiltonian layer.
- **No prior art for the $d>1$ Hawkes result.** Intensities are constant.

### Direct quotes (for the draft)

> "However, despite the practical salience of hit ratio in bond RFQ workflows, most of this literature treats execution probability in reduced form—typically through quote-dependent intensities or fill probabilities—rather than elevating hit ratio itself to an explicit control target." (p. 2)

> "Thus all available bonds contribute to the inventory curvature, regardless of their belonging to a target tier." (p. 6)

> "While this procedure is no longer analytical, it is still fully in the spirit of BEGV: the value function is kept quadratic, while the nonlinear quote-to-intensity map is preserved exactly." (p. 6)

> "For BEGV where the exact nonlinear quote-to-intensity map is preserved and the exact closure for ξ̃ is used (labeled as ξ(q)), the approximation is impressively accurate." (p. 7)

### Examples & illustrations (for later drafting)

- Eqs. (31)–(33) (p. 6): the cleanest statement in the wiki of the closed-form multi-asset BEGV
  curvature with Σ and a diagonal liquidity matrix.
- Fig. 8 (p. 12): targeted-bond quote surface over a two-bond inventory grid at ρ = 0.8 — a concrete
  illustration of cross-asset inventory skew driven by Σ alone.
- Eq. (12) (p. 4): one-line Legendre trick that removes a nonlinear function of fill intensities
  from the Hamiltonian.

### Boundary of this focus

The source has no self-exciting flow and no stochastic intensity. The Stage 2a bearings are the
project's inferences from eqs. (29)–(33), (46)–(47) and Figs. 1–3.

## Mentioned entities

- Models: [[begv-2021-model]], [[glft-2013-model]], [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]].
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[shadow-price]], [[who-excites-the-flow]] (n/a here).
- Other works (bibkeys / not in wiki): Bergault & Guéant 2021 *Size matters* (ref. [4]); Barzykin, Bergault & Guéant 2023 *Algorithmic market making in dealer markets with hedging and market impact* (ref. [2]); `gueant-2019-deep-reinforcement-learning` (Guéant & Manziuk, ref. [15]); Fermanian, Guéant & Pu 2016; Hendershott & Madhavan 2015; Wang 2023; Kargar et al. 2025; Marín Martínez et al. 2026; Oomen 2017; Bessembinder et al. 2018, 2020; Goldstein & Hotchkiss 2020; O'Hara et al. 2018, 2021; Jurkatis et al. 2023; Cartea, Jaimungal & Penalva 2015; Guéant 2016.

## Connections

- Builds on: [[bergault-2021-closed-form-approximations]] / [[begv-2021-model]] via [[hamiltonian-quadratic-approximation]]; supports [[matrix-riccati-equation]] (closed form with Σ).
- Cites: [[barzykin-2026-win-score-promotion]] (win-score gates), [[bergault-2023-liquidity-dynamics-rfq]] (MMPP liquidity).
- Same desk line: [[barzykin-2026-strategic-otc-reputation]] lets the win ratio gate future flow (a state); here it is a target in the objective (no state).
- Contrast: [[barzykin-2022-multi-currency-inventory]] — another multi-asset BEGV-type closed form under constant intensities.
