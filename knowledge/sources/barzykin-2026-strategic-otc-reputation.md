---
title: "Barzykin 2026 — Strategic OTC Market Making with Reputation Feedback"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: barzykin-2026-strategic-otc-reputation
depth: standard
tags: [market-making, rfq, streaming, last-look, otc, fx, reputation, win-ratio, fill-ratio, state-dependent-intensity, adiabatic-approximation, bistability, hamiltonian-approximation, single-asset]
relations:
  - target: barzykin-2026-win-score-promotion
    type: builds-on
    confidence: extracted
    because: "Ref. [17] (p. 11) supplies the win-ratio score and gate for tier A: «Tier A represents RFQ flow, where the relevant long-run score is the dealer's win ratio [17]» (p. 1); fixed-point loci «depend on the gate contrast and smoothness [17]» (p. 8). Here extended to a second (streaming) score."
  - target: barzykin-2026-dynamic-slippage-control
    type: builds-on
    confidence: extracted
    because: "Ref. [18] (p. 11) supplies the streaming tier's joint quote/last-look threshold: «the dealer jointly optimizes quotes and an option-like last-look threshold [18]» (p. 2), and the barrier/cap protocol «tied to last-look risk control [18]» (p. 3)."
  - target: hamiltonian-quadratic-approximation
    type: builds-on
    confidence: extracted
    because: "«To obtain explicit controls, we combine the BEGV quadratic Hamiltonian expansion with a quadratic ansatz for the value function [19]» (p. 6); expansion eq. (28), Riccati relation (29); quotes still from the exact maximisers (14)–(15)."
  - target: bergault-2021-closed-form-approximations
    type: builds-on
    confidence: extracted
    because: "Ref. [19] (p. 11) = Bergault, Evangelista, Guéant, Vieira 2021; its quadratic ansatz and Hamiltonian expansion are used in eqs. (26)–(29) (p. 6)."
  - target: begv-2021-model
    type: builds-on
    confidence: extracted
    because: "«Quadratic BEGV approximation of the fast problem» (p. 6): side-symmetric quadratic ansatz (26) and expansion (28) give the frozen-score Riccati relation (29)."
  - target: who-excites-the-flow
    type: supports
    confidence: inferred
    because: "Both gated intensities λ^{τ,s}G^τ(R^τ) depend on scores moved by the dealer's own wins/losses and fills/rejections (eq. 1, p. 3): controlled, outcome-driven feedback. Quadratic closure is reached only after an O(α) adiabatic truncation (eqs. 16–21, 29, pp. 5–6), consistent with the concept page's claim that control-fed intensity breaks exact quadratic closure."
  - target: matrix-riccati-equation
    type: mentions
    confidence: extracted
    because: "Scalar case only: «matching the coefficients of q² yields the stationary Riccati relation» ½γσ² = A(R)² Σ_τ λ^τ G^τ(R^τ) z^τ h_{τ,2} + O(α_A+α_B) (eq. 29, p. 6)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "Objective (2) is «expected terminal mark-to-market wealth penalized by running and terminal inventory risk [3]» (p. 3), [3] = Cartea, Jaimungal & Ricci 2014 (p. 11)."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Cited among classical models with «exogenous request intensities and fill probabilities [1–4]» (p. 1), [2] = Guéant–Lehalle–Fernandez-Tapia 2013 (p. 11)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "Ref. [1] (p. 11), cited as a classical model with exogenous request intensities (p. 1)."
  - target: shadow-price
    type: mentions
    confidence: extracted
    because: "Reduced state p^τ_s (eq. 6, p. 4) is a shadow price; its first-order score-gradient correction p^τ_s ≈ p^{τ,R}_{s,0} − α_τ χ^{τ,R}_s (eq. 30, p. 6) is what the controls use."
---

# Strategic OTC Market Making with Reputation Feedback

## Bibliographic Details

Barzykin, Alexander. 2026. *Strategic OTC market making with reputation feedback*.
arXiv:2607.11328v2 [q-fin.MF], 15 July 2026 (paper dated 16 July 2026). 11 pp. Author affiliation:
HSBC, London.

**Read: arXiv 2607.11328v2 (preprint); page/equation numbers follow it.** No published version is
known at ingest (2026-10-26), so under the project's preprint policy the preprint is its own
original (no `based_on`). Non-core work.

Keywords (author): Market Making, Stochastic Optimal Control, Algorithmic Trading, Last Look,
Adverse Selection, Latency, Win Ratio, Fill Ratio, Bifurcation, Bistability (p. 1).

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\tau\in\{A,B\}$ | tier: A = RFQ, B = streaming | ⚠ $\tau$ is not a time; no project symbol |
| $\delta^{\tau,s}_t$, $\epsilon_b=+1,\epsilon_a=-1$ | quote offset per tier and side | $\delta^b,\delta^a$ |
| $\eta^{B,s}_t\ge0$ | last-look rejection threshold (tier B) | no project symbol |
| $\lambda^{\tau,s}$ | baseline request intensity (constant) | ⚠ constant baseline, not a Hawkes $\lambda_t$; closer to $\mu$ |
| $G^\tau(R^\tau)$ | performance gate multiplying the intensity (logistic, eq. 39) | no project symbol |
| $f^{\tau,s}(\delta)$ | RFQ win probability (A) / sensitivity of trade-request flow (B) | $f(\delta)$ |
| $R=(R^A,R^B)$, $\alpha_\tau$ | win-ratio and fill-ratio scores; EMA memory coefficient | ⚠ $R$ is a memory state; $\alpha_\tau$ is the jump size of that state |
| $Y^\tau\sim\mathcal N(m_\tau,\nu_\tau^2)$ | sign-adjusted latency mark | ⚠ $m_\tau$ is a mean slippage, **not** the forecast $m_t(u)$ |
| $z^\tau$ | single trade size per tier | — |
| $\theta(t,q,R)$ | reduced value function | $\theta$ |
| $\xi^\tau$, $p^\tau_s$ | score-loss increment (5); shadow price (6) | $p^\tau_s\leftrightarrow p$ (shadow price) |
| $H^\tau_s(\xi,p)$, $\mathcal H^A_s(p)$, $h_{\tau,i}$ | tier Hamiltonians; expansion coefficients (28) | $H$, $h_2=H''(0)$ |
| $A(R)$, $C(R)$ | frozen-score quadratic coefficients (26) | $A$, $C$ |
| $\gamma$, $\ell$ | risk aversion (bp$^{-1}$M$^{-1}$), terminal penalty | $\gamma$ |
| $U(t,R)$, $\vartheta_R(q)$ | slow score value; frozen-score stationary inventory corrector (22) | — |
| $\mu_R$ | invariant inventory law under frozen-score policy | ⚠ **not** the Hawkes baseline $\mu$ |
| $\chi^\tau_s$ | first-order score-gradient correction (20) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; Introduction (access to flow as a state; two tiers; slow–fast reduction) | 1–2 |
| ✓ F1 | Model formulation: tiers, gated intensities, latency mark, fair last-look protocol, option interpretation, inventory/cash, score dynamics (1), objective (2) | 2–3 |
| ✓ F1 | HJB and optimal controls: increments (3)–(6), HJB (7), RFQ Hamiltonian (8)–(9), streaming kernel and Hamiltonian (10)–(13), maximisers (14)–(15) | 3–5 |
| ✓ F1 | Adiabatic approximation: first order in α (16)–(21); frozen-score ergodic problem (22)–(25); quadratic BEGV fast problem (26)–(31); slow score drift (32)–(34); reduced stationary score problem (policy iteration) | 5–7 |
| ✓ F1 | Numerical results: grids, Lambert-W RFQ quote (36), streaming quote (38), logistic gate (39), Table 1, Figs. 1–4 | 7–9 |
| ✓ F1 | Concluding remarks | 9–10 |
| — | Acknowledgment, References | 10–11 |

## Kernthesen

### 1. ⭐ Access to future flow is a state variable moved by today's quoting and acceptance decisions (p. 1)

«Yet most tractable control models still treat access to future flow as exogenous, whereas in
practice access is itself a state variable influenced by today's quoting and acceptance
decisions» (p. 1). RFQ platforms, aggregators and streaming channels «allocate attention and flow
according to recent execution quality» (p. 1). The paper models this as a franchise trade-off
between immediate spread capture and long-term flow access.

### 2. ⭐⭐ Two tiers with two different event clocks: RFQ requests are thinned by a win probability; streaming trade requests already depend on the quote (p. 2)

Tier A: requests $M^{A,s}$ with predictable intensity $\lambda^{A,s}G^A(R^A_t)$; a request is won
with probability $f^{A,s}(\delta^{A,s})$, so fills are «a controlled thinning» of requests (p. 2).
Tier B: no preliminary request is observed; trade requests $M^{B,s}$ have intensity
$\lambda^{B,s}G^B(R^B_t)f^{B,s}(\delta^{B,s})$, where $f^{B,s}$ «captures the sensitivity of
observed trade-request flow to the quoted stream» (p. 2). Each tier has a single trade size $z^\tau$
(fn. 1; size ladders «well understood [4]», p. 2).

### 3. ⭐ Last look on the stream is a fair protocol that acts like a barrier/cap option on the latency mark (pp. 2–3)

Latency mark $Y^\tau\sim\mathcal N(m_\tau,\nu_\tau^2)$ with $m_\tau<0$ (winner's curse, p. 2).
Tier-B rule with threshold $\eta^{B,s}\ge0$: reject if $Y^B<-\eta$, fill at realised slippage if
$|Y^B|\le\eta$, fill with slippage capped at $\eta$ if $Y^B>\eta$ (p. 2). «Thus the dealer jointly
controls a quote offset δ and a barrier/cap level η. This option-like structure gives the
streaming Hamiltonian a familiar derivatives flavour» (p. 3). RFQ rejections and post-trade adverse
selection are ignored (fn. 2, p. 2).

### 4. ⭐⭐ Scores are event-time EMAs of the dealer's own success indicators (p. 3)

$R^\tau\to(1-\alpha_\tau)R^\tau+\alpha_\tau I^\tau$, $\alpha_\tau\in(0,1]$ «typically ≪ 1» (eq. 1,
p. 3). $I^A=1$ if the RFQ is won, $I^B=1$ if the stream request is filled (not rejected). So the
score — and through $G^\tau$ the future intensity — moves with the dealer's controlled outcomes.
The score is two-dimensional, $R=(R^A,R^B)$, but each gate depends on its own tier's score only.

### 5. Objective: linear wealth minus running and terminal inventory penalty, after CJR (p. 3)

$V=\sup_{\delta,\eta}\mathbb E[X_T+q_TS_T-\ell(q_T)-\tfrac12\gamma\sigma^2\int_t^Tq_u^2du]$ (eq. 2),
following [3] (CJR 2014). Linear in cash, so $V=x+qS+\theta(t,q,R)$ (p. 3). Risk-adjusted, not CARA.

### 6. ⭐⭐ The HJB is a sum of gated tier Hamiltonians in two reduced variables: a score-loss increment and a shadow price (pp. 3–4)

$0=\partial_t\theta-\tfrac12\gamma\sigma^2q^2+\sum_{\tau,s}\lambda^{\tau,s}G^\tau(R^\tau)z^\tau H^\tau_s(\xi^\tau,p^\tau_s)$
(eq. 7), with $\xi^\tau=\Delta^\tau_-\theta/z^\tau$ (5) and
$p^\tau_s=[\theta(t,q,R^\tau_-)-\theta(t,q+\epsilon_sz^\tau,R^\tau_+)]/z^\tau$ (6): the shadow price
compares the *lose* branch at old inventory with the *win* branch at new inventory and a raised
score. RFQ: $H^A_s(\xi,p)=\xi+\mathcal H^A_s(p-m_A)$ with
$\mathcal H^A_s(p)=\sup_\delta f^{A,s}(\delta)(\delta-p)$ (eqs. 8–9, p. 4). Streaming:
$H^B_s(\xi,p)=\sup_{\delta,\eta\ge0}f^{B,s}(\delta)[\xi+K^B(\delta,\eta,p)]$ with a Gaussian
fair-protocol kernel $K^B=\Phi^B(\eta)(\delta-p)+L^B(\eta)$ (eqs. 10–13, p. 4).

### 7. Optimal controls come pointwise from the Hamiltonians; the RFQ quote via the inverse fill function (p. 5)

(14): $\delta^{A,s}=\arg\max_\delta f^{A,s}(\delta)(\delta+m_A-p^A_s)$, by the envelope theorem
through $(f^{A,s})^{-1}$; (15): joint $(\delta^{B,s},\eta^{B,s})$ from two first-order conditions
when interior (p. 5). With a sigmoid $f^A$ the RFQ quote is closed form in the Lambert $W$
function (eq. 36, p. 7); with $f^B=e^{-\kappa_B\delta}$ the streaming quote is explicit given $\eta$,
and $\eta$ is found on a grid (eq. 38, p. 7).

### 8. ⭐⭐ Adiabatic step: keep first order in the score jump size α, turning nonlocal score jumps into score gradients (p. 5)

«Quotes and acceptance thresholds are updated request by request, whereas the score variables
$R^\tau$ move only through increments of size $\alpha_\tau\ll1$» (p. 5).
$\theta(R^\tau_+)=\theta+\alpha_\tau(1-R^\tau)\partial_{R^\tau}\theta+O(\alpha^2)$,
$\theta(R^\tau_-)=\theta-\alpha_\tau R^\tau\partial_{R^\tau}\theta+O(\alpha^2)$ (16)–(17); hence
$\xi^\tau=-\alpha_\tau\frac{R^\tau}{z^\tau}\partial_{R^\tau}\theta+O(\alpha^2)$ (18) and
$p^\tau_s=p^\tau_{s,0}-\alpha_\tau\chi^\tau_s+O(\alpha^2)$ (19)–(20). The Hamiltonians are expanded
to first order in α around $(0,p^\tau_{s,0})$ (21). No error bound is given for this truncation.

### 9. ⭐ Slow–fast decomposition: frozen-score stationary inventory corrector plus a slow score value (pp. 5–6)

$\theta(t,q,R)\approx U(t,R)+\vartheta_R(q)$ (22). The fast controls depend on inventory through
$\vartheta_R$; «the strategic value of changing the score enters through the score gradients
$\partial_{R^\tau}U$ and $\partial_{R^\tau}\vartheta_R$» (p. 5); (23)–(25) give the frozen-score
shadow price and the correction in terms of $D^\tau_R(q)=\partial_{R^\tau}U+\partial_{R^\tau}\vartheta_R(q)$.

### 10. ⭐⭐ Frozen-score BEGV closure: a stationary scalar Riccati relation in which both tiers' gated liquidity sets the inventory curvature (p. 6)

Side symmetry, $\vartheta_R(q)\approx-\tfrac12A(R)q^2+C(R)$ (26),
$p^{\tau,R}_{s,0}=\epsilon_sA(R)q+\tfrac12A(R)z^\tau$ (27), $H^\tau(p)=h_{\tau,0}+h_{\tau,1}p+\tfrac12h_{\tau,2}p^2+O(p^3)$
(28). Matching $q^2$: $\tfrac12\gamma\sigma^2=A(R)^2\sum_\tau\lambda^\tau G^\tau(R^\tau)z^\tau h_{\tau,2}+O(\alpha_A+\alpha_B)$
(eq. 29). «This equation determines the frozen-score inventory slope A(R) at leading order»
(p. 6). The score enters the curvature only through the gate values $G^\tau(R^\tau)$, pointwise
in $R$. Controls then use the corrected shadow price (30)–(31) inside the *exact* maximisers (14)–(15).

### 11. ⭐ The slow layer is a deterministic two-dimensional score drift obtained by averaging over the frozen-score invariant inventory law (pp. 6–7)

$\dot R^A=\alpha_A\sum_s\lambda^{A,s}G^A(R^A)\int[f^{A,s}(\delta^{A,s}(q,R))-R^A]\mu_R(dq)$ (32);
for tier B the fill probability is the last-look acceptance probability
$\pi^B_s=1-\Phi((-\eta^{B,s}-m_B)/\nu_B)$ (33), and $\dot R^B$ follows (34). The continuation value
$U$ is computed from a discounted stationary problem on the score grid by policy iteration with
exact policy evaluation (p. 7) — not from the finite-horizon slow equation.

### 12. ⭐⭐ Reputation-building campaigns, defence and monetisation emerge from the policy (pp. 8–9, Figs. 1–3)

The promotion value $\Delta U^\tau(R)=U(R^\tau_+)-U(R^\tau_-)$ peaks near the RFQ gate, «because a
single win matters most when the dealer is close to a promotional threshold» (p. 8, Fig. 1). RFQ
bid offset «falls near the gate midpoint, which is the signature of a campaign»; above the gate
spreads widen to monetise flow, but stay defensive (p. 8, Fig. 2). Low $R^B$: the stream is tightened
to the spread floor to create more requests and repair the fill ratio, while the last-look
threshold still protects against adverse selection (p. 8, Fig. 3).

### 13. ⭐⭐ Score feedback creates bistability and path dependence; the 2-D phase portrait has two attractors and folded nullclines (pp. 8–9, Figs. 2, 4)

The inventory-averaged win probability $\bar f^A(R)$ «can intersect the identity line three
times», giving low- and high-score stable equilibria separated by an unstable one; as the gate
steepness falls, «a stable + unstable pair annihilates leaving one stable branch» (p. 8). In two
dimensions «The RFQ nullcline can fold and form an island-like region without creating an
additional attractor», and the coupled dynamics fix «the sequence in which the dealer repairs
imbalances across client channels» (p. 9).

### 14. ⭐ Cross-tier coupling runs only through common inventory and continuation value, and is weak in the baseline (pp. 8, 10)

«The RFQ score affects the streaming policy through the common inventory and continuation value,
although this cross-tier effect is limited under the baseline calibration» (p. 8). Conclusion:
«cross-tier interaction effects arise through inventory management and continuation value»
(p. 10). There is no cross-gating ($G^A$ depends on $R^A$ only, $G^B$ on $R^B$ only, eq. 7).

### 15. Calibration is illustrative: daily vol 100 bp, γ = 5·10⁻⁴, α = 0.001 in both tiers, 100×100 score grid (pp. 7–8, Table 1)

Tier A: $z=10$M, $\lambda=100$/day, sigmoid $f^A$, $m=-0.1$ bp, $G_{\min}=0.1$, $R_0=0.35$,
steepness 60. Tier B: $z=1$M, $\lambda=500$/day, $f^B=e^{-3\delta}$, $m=-0.2$ bp, $R_0=0.8$,
steepness 10. Discount ρ = 0.05, inventory grid ±50M, spread floor 0.3 bp on tier B (pp. 7–8).

## Figures and tables

Not extracted (figures are qualitative; described in Kernthesen 12–13). Table 1 (p. 8) is
transcribed in Kernthese 15.

## What this source does not address

- **Self- or cross-exciting point processes.** No Hawkes kernel; intensities are constant baselines
  times a deterministic gate of a memory state (p. 2).
- **Several assets.** One instrument; the two dimensions are two client channels (tiers) for the
  same inventory.
- **Error of the adiabatic/BEGV layers.** The full $(t,q,R^A,R^B)$ HJB is not solved; no comparison
  of the approximation against an exact solution, no regret or gap numbers.
- **Post-trade adverse selection, RFQ rejections, size ladders, competition** (fn. 1–2, p. 2).
- **Calibration to data.** Parameters are illustrative (Table 1).
- **CARA utility, RL/neural methods.** None.

## Model card

| Field | Value |
|---|---|
| Assets | 1 (two client tiers: RFQ A, streaming B; single size per tier) |
| Kernel | n/a — no excitation kernel; intensity $\lambda^{\tau,s}G^\tau(R^\tau)$ (× $f^B(\delta)$ on tier B), $R^\tau$ an event-time EMA with geometric memory $(1-\alpha_\tau)^n$ (eq. 1) |
| Excitation | self-feedback within each tier through its score (wins/fills raise, losses/rejections lower future flow); no cross-side, no cross-tier gating, no cross-asset |
| Who excites the flow | the dealer's own controlled outcomes (RFQ win/loss; stream fill/reject) — outcome-driven, on the fill-driven side of [[who-excites-the-flow]] |
| Objective | linear terminal wealth minus terminal penalty $\ell(q_T)$ and running $\tfrac12\gamma\sigma^2\int q^2$ (eq. 2); risk-adjusted, not CARA; numerics use a discounted stationary score problem (ρ = 0.05) |
| Solution method | adiabatic first-order-in-α expansion (16)–(21) + frozen-score BEGV quadratic ansatz/Hamiltonian expansion → stationary scalar Riccati relation (29); exact pointwise quote maximisers (Lambert-W for RFQ); policy iteration for the slow value $U(R)$ on a score grid |
| Benchmark | none (no exact-HJB or no-feedback comparison reported) |
| Reported regret / gap numbers | none — qualitative figures only |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 2, 4, 6, 8, 9, 10, 11, 14.** No Hawkes flow; read under the focus as a
control-fed, finite-memory intensity model with a two-dimensional memory state.

### What this focus needs beyond the Kernthesen

1. **How the "excitation" is modelled.** Each tier's intensity is a constant baseline times a gate
   $G^\tau(R^\tau)$ of an event-time EMA of the dealer's own success indicators (eq. 1). In Hawkes
   terms this is a self-exciting (and self-inhibiting) intensity with geometric memory in event
   count, bounded by the gate, whose marks are set by the control. It is the outcome-driven
   convention of the companion [[barzykin-2026-win-score-promotion]], now with two scores. The
   streaming tier adds a second control channel: the *observed* request rate itself depends on
   the quote ($\lambda G f^B(\delta)$), and the score jump depends on the last-look threshold.
2. **Where the closure holds and where it breaks [I from eqs. 6, 16–21, 29].** The exact shadow
   price (6) mixes $\theta(q,R_-)$ and $\theta(q\pm z,R_+)$. With an $R$-dependent quadratic ansatz it
   contains $-\tfrac12[A(R_+)-A(R_-)]q^2/z$, which feeds $q^3,q^4$ into $\tfrac12h_2p^2$ — the
   fill-driven non-closure of [[who-excites-the-flow]]. Unlike the 2026 win-score paper, this paper
   **writes the truncation out**: the score jump is expanded to first order in α (16)–(19), the
   curvature relation (29) is stated with an explicit remainder $O(\alpha_A+\alpha_B)$, and the
   neglected $A_R q^2$ term reappears only inside the control correction $D^\tau_R$ (31). So the BEGV
   closure is exact in $q$ only at $\alpha=0$ (frozen score); at order α the author keeps the score
   gradient in the *quotes* but not in the *curvature*.
3. **What the closure is, in project terms [I].** $A(R)$ in (29) is the stationary scalar Riccati
   evaluated pointwise at the frozen intensity state — the exact analogue of the frozen-forecast
   policy (Riccati along a frozen intensity, [[barzykin-2026-hawkes-driven-otc]]). The order-α
   correction (30) is a shadow-price shift from the slow-state gradient, not a correction to $A$.
4. **Multi-asset / cross-asset carry-over.** Not treated: one asset. The closest structure is
   cross-*tier*: two channels with separate memories sum into one curvature,
   $A(R)^2\sum_\tau\lambda^\tau G^\tau z^\tau h_{\tau,2}$ (29), and interact only through inventory
   and continuation value, weakly in the baseline (Kernthese 14). [I] With $d$ assets this would be
   BEGV's matrix Riccati with $D(R)=\sum_\tau\lambda^\tau G^\tau(R^\tau)\,\mathrm{diag}(\cdot)$; a
   shared platform score across assets would be an outcome-driven cross-asset channel, which the
   paper does not consider.
5. **Accuracy of the closure.** Not tested. The paper solves neither the full 4-D HJB nor a
   no-feedback benchmark; Figures 1–4 use the reduced model only.

### Bearing on Stage 2a (perturbative closed form)

- **Method analogue, not prior art [I].** The adiabatic step is a first-order expansion in a small
  *jump size* α of the intensity-modulating state, around the frozen state, giving (i) a
  frozen-state Riccati at order 0 and (ii) an O(α) shadow-price correction. Stage 2a likewise
  expands in a small jump-to-mean ratio around a deterministic forecast. Differences: the small
  parameter here is the memory weight of a bounded EMA, the state is controlled (outcome-driven, not
  flow-driven), no error order is proved beyond the formal $O(\alpha^2)$ remainders, the expansion
  is single-asset, and no accuracy test exists. It does not anticipate the Stage 2a $d>1$ result.
- **A warning for S1.** The author's truncation drops the $\alpha A_R q^2$ term from the curvature
  while keeping it in the quotes (31). Stage 2a's order-1 system should state explicitly whether
  the analogous $\tilde\Delta A^1$ term enters the curvature equation or only the quotes.

### Direct quotes (for the draft)

> "Yet most tractable control models still treat access to future flow as exogenous, whereas in practice access is itself a state variable influenced by today's quoting and acceptance decisions." (p. 1)

> "Quotes and acceptance thresholds are updated request by request, whereas the score variables Rτ move only through increments of size ατ ≪ 1. This invites an adiabatic treatment in which the score is frozen when solving the fast inventory problem and then evolved on a slower time scale using the induced success rates." (p. 5)

> "To obtain explicit controls, we combine the BEGV quadratic Hamiltonian expansion with a quadratic ansatz for the value function [19]." (p. 6)

> "The RFQ score affects the streaming policy through the common inventory and continuation value, although this cross-tier effect is limited under the baseline calibration." (p. 8)

### Examples & illustrations (for later drafting)

- Eq. (29) (p. 6): one-line example of a Riccati curvature whose coefficient is a sum of
  state-gated intensities times $h_2$, evaluated pointwise in the frozen state.
- Fig. 2, right panel (p. 9): three intersections of $\bar f^A(R)$ with the identity line — a
  compact picture of how control-fed intensity changes the qualitative dynamics.
- Fig. 4 (p. 10): 2-D phase portrait with two attractors and a folded nullcline; illustrates
  ordered recovery across channels.

### Boundary of this focus

The source has no self-exciting point process, no multi-asset model and no accuracy test. Items
2–4 and the Stage 2a bearing are the project's inferences from eqs. (6), (16)–(31).

## Mentioned entities

- Models: [[begv-2021-model]], [[cartea-jaimungal-ricci-model]], [[glft-2013-model]], [[avellaneda-stoikov-model]].
- Concepts: [[hamiltonian-quadratic-approximation]], [[matrix-riccati-equation]], [[who-excites-the-flow]], [[shadow-price]], [[intensity-forecast]] (frozen-state analogue only).
- Other works (bibkeys / not in wiki): Bergault & Guéant 2021 *Size matters* (ref. [4]); Oomen 2017 *Execution in an aggregator* and *Last look* (refs. [5]–[6]); Cartea, Jaimungal & Walton 2019 (last look, ref. [7]); `barzykin-2025-optimal-quoting-adverse` (ref. [8]); Cartea & Sánchez-Betancourt 2025 (toxic flow, ref. [9]); Bank, Ekren & Muhle-Karbe 2021; Wang 2023; Boyce, Herdegen & Sánchez-Betancourt 2024; Eisler & Muhle-Karbe 2024; Cont & Xiong 2024; Marín et al. 2025; Boyce & Neuman 2026 (refs. [10]–[16]).

## Connections

- Builds on: [[barzykin-2026-win-score-promotion]] (tier-A score and gate; here a second score and the explicit O(α) expansion) and [[barzykin-2026-dynamic-slippage-control]] (streaming last-look threshold).
- Builds on: [[bergault-2021-closed-form-approximations]] / [[begv-2021-model]] via [[hamiltonian-quadratic-approximation]].
- Contrast: [[barzykin-2026-hawkes-driven-otc]] — there requests drive a Hawkes memory and the forecast is quote-independent; here outcomes drive a bounded EMA memory. Both freeze the memory state to reach a Riccati layer.
- Same desk line, different use of hit/win ratio: [[barzykin-2026-bond-market-making]] targets the hit ratio in the objective instead of letting it gate the flow.
- Evidence for [[who-excites-the-flow]] (outcome-driven case) and for D2 in [[problem-anatomy]].
