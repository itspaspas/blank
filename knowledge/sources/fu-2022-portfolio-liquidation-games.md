---
title: "Fu, Horst & Xia 2022 — Portfolio Liquidation Games with Self-Exciting Order Flow"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: fu-2022-portfolio-liquidation-games
depth: standard
based_on: preprint
read: arXiv 2011.05589v1
tags: [optimal-execution, portfolio-liquidation, hawkes, self-exciting, controlled-intensity, mean-field-game, mean-field-type-control, fbsde, singular-terminal-condition, transient-impact, lq-control]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«we assume that the market order dynamics follows a Hawkes process with exponential kernel» with intensities ζ± = μ_t + α∫e^{−β(t−s)}dN± (p. 5); the investor shifts the base intensity to μ + ξ±."
  - target: who-excites-the-flow
    type: mentions
    confidence: extracted
    because: "Neither pure convention: all market orders self-excite, and in addition the investor's own trading rate raises the base intensity — «in our model they are endogenously controlled by the large investors» (p. 2)."
  - target: intensity-forecast
    type: mentions
    confidence: inferred
    because: "Only the expected child flow C_t = α∫e^{−β(t−s)}Z̄_s ds enters the problem; it solves the linear ODE dC = (−(β−α)C + α(x₀ − EX))dt (eq. 2.6, p. 5) — the d=1, control-driven analogue of the forecast m_t; the source does not use the term."
  - target: matrix-riccati-equation
    type: mentions
    confidence: inferred
    because: "Deterministic benchmark: linear ansatz 𝔹 = D𝔽 + D⁰ gives a 3×3 (6×6 for two players) matrix Riccati ODE D' = −Dφ₀₁D − Dφ₀₀ + φ₁₁D + φ₁₀ (eqs. 5.2, 5.6, 5.8, pp. 26–30), solved through a matrix exponential; not the BEGV Hamiltonian Riccati."
  - target: cartea-2018-algorithmic-trading-stochastic
    type: cites
    confidence: extracted
    because: "«Cartea et al in [14] considered a liquidation model in which the investor placed limit orders whose fill rates depended on a mutually exciting 'influential' market order flow … the intensities of the Hawkes processes were exogenous» (p. 2)."
  - target: chen-2026-optimal-trade-execution
    type: mentions
    confidence: inferred
    because: "Later work by Horst and co-authors cites the 2020 preprint and drops risk aversion and transient impact to get closed forms (Chen et al. fn. 3); not stated in this source."
---

# Portfolio Liquidation Games with Self-Exciting Order Flow

## Bibliographic Details

Fu, Guanxing, Ulrich Horst, and Xiaonyu Xia. 2022. "Portfolio liquidation games with self-exciting
order flow." *Mathematical Finance* 32(4): 1020–1065. doi 10.1111/mafi.12359. Preprint
arXiv:2011.05589v1 [math.OC], 11 November 2020, 33 pp.

**Read: arXiv 2011.05589v1 (preprint); page and equation numbers follow that version.** (Non-core
work; preprint accepted under the project's preprint policy. The published version exists, hence
`based_on: preprint`.) Printed page numbers equal PDF page numbers.

### Notation map (source → project, CLAUDE.md § Notation)

⚠ The source's Greek letters collide with project notation almost everywhere.

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $X_t$ | shares still to sell (inventory), $X_T=0$ | $q_t$ |
| $\xi_t$ | trading (selling) rate, the control | no project symbol |
| $\zeta^\pm_t=\mu_t+\alpha\int_0^te^{-\beta(t-s)}dN^\pm_s$ | Hawkes intensity of market sell/buy orders | $\lambda_t$ (project); $\mu$ = baseline $\mu$ ✓; $\alpha$ = jump size, so branching ratio $\alpha/\beta=\rho(K)$; $\beta$ = decay $\beta$ ✓ |
| $\mu+\xi^\pm$ | base intensity shifted by the investor's trading | control enters the **baseline** linearly |
| $\bar Z_t$, $C_t$ | expected net sell orders; expected net sell *child* orders (eqs. 2.4–2.5) | $C$ ≈ integrated excess of the intensity forecast $m_t$ [I] |
| $Y_t$ | transient (persistent) price impact, resilience $\rho$, impact factor $\gamma$ | ⚠ $\rho$ is **not** a spectral radius; $\gamma$ is **not** risk aversion |
| $\eta$ | instantaneous impact | — |
| $\lambda_t$ | running inventory penalty ("market risk", $\lambda X^2$) | ⚠ **not** an intensity; ≈ $\tfrac12\gamma\sigma^2$ in project terms |
| $n$ | terminal penalty $n X_T^2$ (Section 5, §3.4) | — |
| $P,Q,R$; $M:=P-Y$ | adjoint processes of $(X,Y,C)$ | — |
| $\mathscr A$ (3.12), $A_t$ (p. 26) | coefficient of the affine ansatz $M=\mathscr AX+\mathscr B$ | ↔ inventory-quadratic coefficient $A$ (scalar) |
| $D$, $\mathscr D$, $\mathcal D$ (5.2, 5.6, 5.8) | matrix coefficient of $\mathbb B=D\mathbb F+D^0$ in the deterministic case | matrix Riccati in $(X,Y,C)$ |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (feedback of trading on future order arrivals; overselling; method) | 1–4 |
| — | Notation (spaces $L^2_{\mathscr F}$, $\mathbb S^2$, $\mathcal H_{a}$) | 4 |
| ✓ F1 | 2.1 Single player benchmark: Graewe–Horst model (2.1)–(2.3); Hawkes child flow (2.4)–(2.6); mean-field-type problem (2.7)–(2.8) | 4–6 |
| ✓ F1 | 2.2 Many-player models: $N$-player problem (2.9)–(2.10), homogeneity (2.11)–(2.12), MFG (2.13)–(2.15) | 6–7 |
| ✓ F1 | 3.1 Characterisation of open-loop equilibria: Hamiltonians, adjoint systems (3.1)–(3.7) | 7–9 |
| ✓ F1 | 3.2 The mean-field FBSDE: unified system (3.8), Assumption 3.2 (weak interaction), Remark 3.3, Thm. 3.4; affine ansatz and singular Riccati BSDE (3.12)–(3.14); continuation method | 10–17 |
| ✓ F1 | 3.3 Verification: Thm. 3.5, cost decomposition into equilibrium + round-trip cost (3.23), Lemmas 3.7–3.8 | 17–20 |
| — | 3.4 Approximation by terminal penalisation (3.29), Prop. 3.9 | 21 |
| — | 4 From many-player games to MFG: Lemma 4.1, Thm. 4.2 | 21–25 |
| ✓ F1 | 5.1 Deterministic MFG: linear ODE (5.1), matrix Riccati (5.2), explicit solution (5.3)–(5.4), coth formula; Fig. 1 | 25–27 |
| ✓ F1 | 5.2 Single player: (5.5)–(5.6), $\det(\mathscr G)\neq0$; Fig. 2 | 27–29 |
| ✓ F1 | 5.3 Two-player game: 6-dim system (5.7)–(5.8); Fig. 3 | 28–30 |
| — | References | 30–33 |

## Kernthesen

### 1. ⭐⭐ Market orders are self-exciting Hawkes processes whose base intensity is shifted by the large investors' own trading — the intensities are controlled, not exogenous (pp. 2, 5)

Sell and buy market orders arrive as independent counting processes $N^\pm$ with exponential-kernel
intensities $\zeta^\pm_t=\mu_t+\alpha\int_0^te^{-\beta(t-s)}dN^\pm_s$ (p. 5). «In the presence of the large
trader the base intensities change to $\mu+\xi^\pm$ where $\xi^\pm$ denotes the positive/negative part
of the large investor's liquidation strategy» (p. 5). Selling thus generates "child orders" in the
same direction, which the authors motivate by a shrinking counterparty pool, herding and predatory
front-running (p. 2). The contrast with earlier Hawkes execution models is explicit: «In all three
models the intensities of the Hawkes processes were exogenous; in our model they are endogenously
controlled by the large investors» (p. 2). There is self-excitation per side but no cross-side
excitation ($N^+$, $N^-$ independent).

### 2. ⭐⭐ Only the *expected* child order flow enters the problem, and it follows a linear mean-reverting ODE (p. 5)

The expected net number of sell orders satisfies the renewal-type equation
$\bar Z_t=\int_0^t\mathbb E[\xi_s]ds+\alpha\int_0^te^{-\beta(t-s)}\bar Z_sds$ (2.4); the expected net child
flow is $C_t=\alpha\int_0^te^{-\beta(t-s)}\bar Z_sds$ (2.5), and differentiating gives
$dC_t=(-(\beta-\alpha)C_t+\alpha(x_0-\mathbb EX_t))dt$, $C_0=0$ (2.6). «The child order flow rate
increases linearly in the investor's expected traded volume $x_0-\mathbb EX$. The child order flow
is mean-reverting if $\frac\alpha\beta<1$» (p. 5). The realised Hawkes intensity never becomes a state
variable; the Hawkes structure collapses to one deterministic linear ODE with decay rate $\beta-\alpha$.

### 3. ⭐ The child flow feeds the transient impact, turning each player's best response into a mean-field-type control problem (pp. 5–6)

Base model (Graewe–Horst): minimise $\mathbb E\int_0^T\{\eta\xi_s^2+\xi_sY_s+\lambda_sX_s^2\}ds$ with
$dX=-\xi dt$, $X_T=0$, and transient impact $dY=(-\rho Y+\gamma\xi)dt$ (2.1)–(2.2); execution price
$\tilde S=S-\eta\xi-Y$ (2.3). Adding the child flow gives
$dY_t=(-\rho_tY_t+\gamma_t(\xi_t-(\beta-\alpha)C_t+\alpha(x_0-\mathbb EX_t)))dt$ (2.8). Because $\mathbb EX$
appears in the dynamics, the single player already faces a control problem of mean-field type
(p. 5); with $N$ players both $Y^i$ and $C^i$ are driven by the *average* trading rate (2.10, p. 6). All
cost and impact coefficients may be bounded progressively measurable processes; permanent impact is
left out on purpose «as it does not alter the mathematical analysis» (p. 2).

### 4. The $N$-player game and the MFG share one FBSDE framework (pp. 6–10)

The MFG replaces the averages $\bar\xi,\bar X$ by deterministic processes and imposes the fixed point
$\mathbb E[\xi_t]=\bar\mu_t$, $\mathbb E[X_t]=\nu_t$ (2.13)–(2.15, p. 7). The stochastic maximum principle
gives candidate best responses $\xi^{*,i}=(P^{i,i}-Y^i-\frac{\gamma^i}NQ^{i,i})/(2\eta^i)$ (3.1, p. 8)
with adjoints $(P,Q,R)$ for $(X,Y,C)$ (3.2). Writing $\mathcal S=(Y,C)^\top$ yields the compact
systems (3.4) ($N$ players) and (3.7) (MFG), both special cases of the general linear mean-field
FBSDE (3.8) (Remark 3.1, p. 10). The terminal value of $P$ is unknown because of the liquidation
constraint.

### 5. ⭐⭐ An affine ansatz turns the unknown terminal condition into a singular Riccati BSDE plus a linear BSDE (pp. 11–12)

With $\widetilde M^i=\mathscr A^i\widetilde X^i+\mathscr B^i$, integration by parts gives
$d\mathscr A^i_t=\big(2\lambda^i_t-\frac{(\mathscr A^i_t)^2}{2\eta^i_t}\big)dt-Z^{\mathscr A^i}_tdW_t$,
$\lim_{t\uparrow T}\mathscr A^i_t=+\infty$ (3.12), and a linear BSDE for $\mathscr B^i$ (3.13). The
Riccati coefficient $\mathscr A$ involves only $\lambda,\eta$ — the Hawkes parameters $\alpha,\beta$
and impact $\gamma,\rho$ enter only $\mathscr B$ and the forward/backward coupling. The singular
equation (3.12) has a unique solution with
$\exp(-\int_r^s\frac{\mathscr A_u}{2\eta_u}du)\le(\frac{T-s}{T-r})^b$ (3.14), quoted from earlier
work [4, 27].

### 6. ⭐ Existence and uniqueness hold under a weak-interaction condition, proved by a continuation method for singular FBSDEs (pp. 10–17)

Assumption 3.2: bounded coefficients; $A^i+(A^i)^\top$ uniformly positive definite (3.9); and (3.10),
which «requires either the cost functions to be dominated by the terms $\eta^i(\xi^i)^2$ and
$\lambda^i(X^i)^2$ that are unaffected by the choices of other players … or the impact of other
players … to be weak enough» (p. 11). Thm. 3.4: unique solution in weighted spaces
$\mathcal H_{a}\times\mathbb S^2\times\dots$ (p. 11). The proof extends the continuation method of Fu
et al. [22] to the higher-dimensional system (pp. 11–17). The authors note that «Without some form of
weak interaction uniqueness of equilibria usually cannot be expected» (p. 3).

### 7. For identical constant coefficients the condition reduces to a bound linking impact, resilience and the Hawkes decay gap (p. 11)

Remark 3.3: for large $N$ and identical constant $\alpha,\beta,\gamma,\rho$, (3.9) reduces to
$4\rho>\gamma^2(\beta-\alpha)$ and $\beta>\alpha$, with $\hat\rho$ the minimum eigenvalue of
$\frac{A+A^\top}2$:
$\hat\rho=\frac{\rho+\beta-\alpha-\sqrt{(\rho+\beta-\alpha)^2-4\rho(\beta-\alpha)+\gamma^2(\beta-\alpha)^2}}2$.
Subcriticality $\alpha<\beta$ is thus part of the well-posedness condition, and the Hawkes gap
$\beta-\alpha$ plays the role of a second resilience rate alongside $\rho$.

### 8. ⭐ Verification works without convexity: deviation cost = equilibrium cost + a round-trip cost that is non-negative (pp. 3, 17–20)

«in our model the players' optimization problems are not convex and hence standard verification
arguments do not apply. Instead, we establish a novel maximum principle that strongly relies on the
liquidation constraint» (p. 3). Thm. 3.5 (p. 17) shows that the FBSDE solution is the unique
open-loop Nash equilibrium under a slightly stronger condition (3.22). The key identity (3.23, p. 18)
writes $J^i(\xi^i,\xi^{*,-i})$ as the equilibrium cost plus
$\mathbb E\int_0^T[\eta(\xi-\xi^*)^2+\lambda(X-X^*)^2+(X-X^*)\langle\Theta,\dots\rangle]dt$, i.e. the cost of a
round trip; «As a byproduct of our verification result we thus obtain that round-trips are costly in
equilibrium» (p. 18). Remark 3.6(2): in the MFG the impact process is exogenous to the
representative player, so standard convexity holds there (p. 17).

### 9. The liquidation constraint can be approximated by an increasing terminal penalty (p. 21)

Replacing $X_T=0$ by a penalty $n(X^i_T)^2$ changes (3.8) to (3.29) with $M^i_T=2nX^i_T-\mathcal S^{i,(1)}_T$;
Prop. 3.9: the penalised solutions converge to the constrained one as $n\to\infty$ (p. 21). This
justifies using the penalised model in the numerics of Section 5.

### 10. $N$-player equilibria converge to the MFG equilibrium under homogeneity (pp. 21–25)

Under (2.11)–(2.12) (coefficients as functions of the player's own initial position and Brownian
path; i.i.d. initial positions) and conditions (3.9)–(3.10) for large $N$, Thm. 4.2 gives
$\mathbb E\int_0^T|\xi^{*,i,N}_t-\xi^{*,i}_t|^2dt\to0$ (p. 22). This complements Fu et al. [22], «where no
such convergence result was established» (p. 3).

### 11. ⭐⭐ With deterministic coefficients everything reduces to a linear ODE system solved by a matrix Riccati ODE and a matrix exponential (pp. 25–27)

«If all model parameters except the initial positions are constant, then the stochastic integral
terms drop out of the FBSDE system» (p. 25). Taking expectations, $\mathbb F=(\mathbb EX,\mathbb EY,\mathbb EC)^\top$
and $\mathbb B=(\mathbb EP,\mathbb EQ,\mathbb ER)^\top$ solve the linear system (5.1) with $3\times3$ blocks
$\varphi_{00},\varphi_{01},\varphi_{10},\varphi_{11}$. The ansatz $\mathbb B=D\mathbb F+D^0$ gives the matrix
Riccati ODE $D'=-D\varphi_{01}D-D\varphi_{00}+\varphi_{11}D+\varphi_{10}$, $D_T=\mathrm{diag}(2n,0,0)$, and a
linear ODE for $D^0$ (5.2). Its solution is explicit through the fundamental solution
$\Phi(T,t)=e^{\mathscr P(T-t)}$ of the $6\times6$ linear system (5.3)–(5.4), provided a $3\times3$ block is
invertible, «which will be the case in the our simulations» (p. 26). The deviation from the mean has
the classical scalar closed form $A_t=2\sqrt{\eta\lambda}\coth(\sqrt{\lambda/\eta}(T-t))$ and
$X_t-\mathbb E[X_t]=(\mathcal X-\mathbb E[\mathcal X])\frac{\sinh(\sqrt{\lambda/\eta}(T-t))}{\sinh(\sqrt{\lambda/\eta}T)}$
(pp. 26–27).

### 12. ⭐ Anticipating one's impact on future order flow makes players oversell and take short positions near criticality (pp. 2–3, 27–28)

«Anticipating their impact on future order arrivals, the players typically trade more aggressively
initially and may alternately take long and short positions» (p. 2). In the MFG, short positions do
not occur for small $\alpha,\gamma$; «For near critical values of $\alpha$ it is optimal for the
representative player to unwind his position before the terminal time, and then to take a negative
position that he closes at the end» (Fig. 1, p. 27). In the single-player model «the initial
trading rate increases in $\alpha$ and … it is optimal to oversell for near-critical values of
$\alpha$» (Fig. 2, p. 28). The mechanism: the player «benefits from the inertia in market order flow
when closing a short position» (p. 27).

### 13. Oscillations come from anticipated impact on order flow, not from a "hot potato" effect, and need strong interaction (pp. 3, 28)

Unlike Schied et al. [42, 43], «oscillations in our model do not arise from "a hot potato effect" but
rather from the players' anticipated impact on future order flow. More importantly, in our model
strong oscillations require extremely large choices of impact parameters» (p. 3). Fig. 2 (right)
shows large fluctuations only for $\gamma=10$; «We emphasize that this behavior only occurs for very
large values of $\gamma$» (p. 28).

### 14. ⭐ Single-player models admit no arbitrage from self-excitation, but two-player models admit beneficial round trips (pp. 3, 30)

«anticipating one's own impact on future order flow does not generate arbitrage opportunities in
single player models. In multi-player models there may indeed exist beneficial round-trips as we
show by means of an explicit example» (p. 3). In the two-player game (state dimension 6, (5.7)–(5.8))
a player starting from $x_2=0$ trades in equilibrium: «Player 2 benefits from the presence of
Player 1; there is a beneficial round-trip for this player in equilibrium», stronger for larger
transient impact (Fig. 3, p. 30). Here $\det(\mathcal G)\equiv0$, so the integral of the fundamental
solution has no explicit expression (p. 30); in the single-player case
$\det(\mathscr G)=-\rho\lambda(\beta-\alpha)^2(\frac\gamma{\eta^2}+\frac\rho\eta)\neq0$ because $\beta>\alpha$
(p. 28).

## Figures and tables

- Fig. 1 (p. 27): MFG equilibrium position vs. $\alpha\in\{0,0.5,1\}$, for $\gamma=0.1$ and $\gamma=1$.
- Fig. 2 (p. 29): single-player optimal position vs. $\alpha$ and vs. $\gamma\in\{0.1,1,10\}$.
- Fig. 3 (p. 30): two-player equilibrium positions, $\gamma=1$ and $\gamma=0.1$.
- Parameters throughout: $\eta=0.1$, $\rho=0.2$, $\lambda=0.3$, $\beta=1.1$, $T=5$ (Figs. 1–3 captions).

## What this source does not address

- **Market making / quote control.** The players liquidate with absolutely continuous trading rates;
  there are no quotes, no fill probability $f(\delta)$ and no Hamiltonian. For quote-controlled
  Hawkes flow see [[cartea-2014-buy-low-sell]], [[jusselin-2021-persistent-order-flow]],
  [[barzykin-2026-hawkes-driven-otc]].
- **Realised (pathwise) intensities as state.** Only expected child flow enters (eqs. 2.4–2.6); the
  Hawkes intensity's own randomness and its feedback on inventory risk are averaged out.
- **Several assets or cross-asset excitation.** One stock; $N^+$ and $N^-$ are independent (no
  cross-side excitation). Multi-dimensional impact with stochastic resilience is in Horst–Xia [30]
  (not in the library).
- **Non-exponential kernels, CARA utility, permanent impact.** None (permanent impact excluded on
  purpose, p. 2). Power-law propagators in LQ execution: [[abijaber-2025-optimal-liquidation-signals]].
- **Calibration, regret or benchmark numbers.** Figures are qualitative illustrations only.

## Model card

| Field | Value |
|---|---|
| Assets | 1 stock; $N$ players (and MFG) trading it |
| Kernel | exponential Hawkes, $\zeta^\pm=\mu+\alpha\int e^{-\beta(t-s)}dN^\pm$ (p. 5); $\alpha,\beta$ may be player-specific processes in §2.2 |
| Excitation | self (per side); no cross-side ($N^\pm$ independent); no cross-asset |
| Who excites the flow | all market orders self-excite **and** the investors' trading rates shift the base intensity ($\mu+\xi^\pm$) — control-driven baseline, neither flow- nor fill-driven in the [[who-excites-the-flow]] sense |
| Objective | minimise expected LQ execution cost $\mathbb E\int(\eta\xi^2+\xi Y+\lambda X^2)$ under strict liquidation $X_T=0$ (risk-adjusted; not CARA) |
| Solution method | stochastic maximum principle → linear mean-field FBSDE with unknown terminal value; affine ansatz → singular Riccati BSDE (3.12) + linear BSDE; continuation method (Thm. 3.4); non-convex verification (Thm. 3.5). Deterministic case: linear ODE, matrix Riccati (5.2), explicit via matrix exponential |
| Benchmark | single-player and $\alpha=0$ (no child flow) curves in Figs. 1–2 |
| Reported regret / gap numbers | n/a — no quantitative comparison |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 1, 2, 3, 5, 7, 11, 14.**

### What this focus needs beyond the Kernthesen

1. **Why the closure holds [I from eqs. 2.4–2.8].** Three choices keep the problem exactly LQ
   despite Hawkes flow. (a) The control enters the intensity *linearly*, through the baseline
   $\mu+\xi^\pm$, not through a nonlinear fill probability. (b) Only the *expected* child flow drives
   the impact state, so the stochastic intensity is replaced by a deterministic linear ODE (2.6) — the
   same "expected-value collapse" as freezing the [[intensity-forecast]]. (c) Costs are quadratic in
   $(\xi,X)$ and bilinear in $\xi Y$. The Riccati coefficient $\mathscr A$ then depends on $\lambda,\eta$
   only (3.12); Hawkes parameters reach the strategy through the linear part.
2. **Where it would break [I].** If impact were driven by *realised* child orders, $\zeta_t$ would
   become a state and the jump terms would multiply the value function's increments; with the
   control in the baseline these stay affine-times-intensity, so an exact quadratic closure in
   $(X,Y,\zeta)$ is still plausible (same mechanism as [[zarezade-2018-steering-social-activity]]).
   What breaks it in market making is the control acting through $f(\delta)$ times $\lambda$, which
   this paper never has. This supports the [[problem-anatomy]] diagnosis that the Hamiltonian, not
   memory, is the obstruction.
3. **Correction to the wiki [I].** [[chen-2026-optimal-trade-execution]] (focus item 2) says that with
   risk aversion and stochastic strategies the problem «returns to a controlled-intensity HJB as in»
   this paper. That is not what this paper does: it keeps risk aversion ($\lambda X^2$) and stochastic
   coefficients, yet only $\mathbb E X$ enters the child flow (2.8). It is a mean-field-type FBSDE,
   not an HJB in the realised intensity.
4. **Carry-over to several assets with cross-asset excitation [I].** Replacing the scalar
   $C$ by a vector and $\beta-\alpha$ by a matrix $D(I-K)$ keeps (2.6) linear:
   $dC=(-D(I-K)C+\dots)dt$. The deterministic system (5.1) would grow to blocks of size $3d$, and the
   matrix Riccati (5.2) would remain explicit via a matrix exponential. Subcriticality $\rho(K)<1$
   would replace $\beta>\alpha$ in the weak-interaction condition (Remark 3.3). None of this is in the
   source. The $N$-player game (Kernthese 14) is the nearest thing to multi-dimensionality: a
   $6\times6$ system for two players in one stock.
5. **Bearing on Stage 2a.** Little direct bearing: no quotes, no perturbative expansion. It is a
   clean precedent that *control-driven* Hawkes excitation (the investor raises the baseline) can sit
   inside an exact LQ closure, provided only the mean flow matters.

### Direct quotes (for the draft)

> "In all three models the intensities of the Hawkes processes were exogenous; in our model they are endogenously controlled by the large investors." (p. 2)

> "The child order flow rate increases linearly in the investor's expected traded volume x0 − EX. The child order flow is mean-reverting if α/β < 1; it is well known that the Hawkes process is stable in the long term if α/β < 1." (p. 5)

> "Making a standard affine ansatz the system with unknown terminal condition can be replaced by an FBSDE with known initial and terminal condition, yet singular driver." (p. 3)

> "In the presence of the large trader the base intensities change to μ + ξ± where ξ± denotes the positive/negative part of the large investor's liquidation strategy" (p. 5)

### Examples & illustrations (for later drafting)

- Eqs. (2.4)–(2.6) (p. 5): a three-line derivation of how a controlled Hawkes baseline becomes one
  linear ODE for expected child flow. A compact illustration of the expected-value collapse.
- Fig. 1 right (p. 27): near-critical $\alpha=1$ ($\alpha/\beta\approx0.91$) drives the representative
  player short, a vivid case of anticipated self-excitation changing the optimal path.
- Single-player determinant $\det(\mathscr G)=-\rho\lambda(\beta-\alpha)^2(\dots)$ (p. 28): solvability
  hinges on $\beta>\alpha$, i.e. subcriticality.

### Boundary of this focus

This is a liquidation game, not market making; all statements about quote control, realised
intensities and multi-asset excitation (items 2–5) are the project's inferences. The paper offers no
numbers that could enter the closed-form / exact / RL comparison.

## Mentioned entities

- Concepts: [[hawkes-process]], [[who-excites-the-flow]], [[intensity-forecast]], [[matrix-riccati-equation]], [[markov-lift]] (not needed here: no realised-intensity state).
- Synthesis: [[problem-anatomy]].
- Other works (bibkeys / not in library): Graewe & Horst 2017 [25] (base model); Horst & Xia 2019 [30] (multi-dimensional execution, stochastic resilience); Fu, Graewe, Horst & Popier 2020/21 [22] (MFG of liquidation, continuation method); Alfonsi & Blanc 2016 [1]; Amaral & Papanicolaou [3]; Cayé & Muhle-Karbe 2016 [17]; Schied et al. [42, 43]; Obizhaeva & Wang [38].

## Connections

- Builds on: [[hawkes-process]] (exponential kernel, controlled baseline).
- Cites: [[cartea-2018-algorithmic-trading-stochastic]] as an exogenous-intensity Hawkes execution model (p. 2).
- Same exact-LQ mechanism (control does not multiply the intensity nonlinearly): [[zarezade-2018-steering-social-activity]]; contrast with the Hamiltonian obstruction in [[barzykin-2026-hawkes-driven-otc]] Kernthese 11.
- Later work in the same line: [[chen-2026-optimal-trade-execution]] (deterministic, risk-neutral, permanent impact; see focus item 3 on how it describes this paper).
- Contrast: [[abijaber-2025-optimal-liquidation-signals]] (general Volterra propagator in impact, no order-flow excitation).
