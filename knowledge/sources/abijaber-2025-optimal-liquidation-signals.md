---
title: "Abi Jaber & Neuman 2025 — Optimal Liquidation with Signals: the General Propagator Case"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: abijaber-2025-optimal-liquidation-signals
depth: standard
based_on: preprint
read: arXiv 2211.00447v2
tags: [optimal-execution, portfolio-liquidation, transient-impact, propagator, volterra, power-law-kernel, operator-riccati, lq-control, signals, infinite-dimensional-control]
relations:
  - target: abijaber-2021-linear-quadratic-control
    type: builds-on
    confidence: extracted
    because: "«Our methodology complements and extends the growing literature on linear-quadratic stochastic Volterra problems [5, 43, 31, 20, 3, 29, 1]» (p. 3); [5] = Abi Jaber, Miller & Pham 2021, AAP. Remark 4.9 relates its operator Riccati to the Riccati equations of [4, 5] (p. 14)."
  - target: markov-lift
    type: mentions
    confidence: extracted
    because: "For completely monotone kernels, «introducing the Markovian auxiliary variables Z̃_t(x) := ∫e^{−x(t−s)}u_s ds» re-expresses the value as linear-quadratic in (Z̃, Q) with an infinite-dimensional Riccati (Remark 4.9, pp. 14–15); the main result needs no lift."
  - target: volterra-riccati
    type: mentions
    confidence: inferred
    because: "Different object with the same name-space: here an exact operator Riccati Ψ̇ = 2ΨΣ̇Ψ for an LQ Volterra problem (6.9, p. 25), not Barzykin's certainty-equivalent Riccati along a forecast path. Barzykin cites this paper as proof that memory alone does not block tractability."
  - target: barzykin-2026-hawkes-driven-otc
    type: mentions
    confidence: inferred
    because: "Barzykin 2026 (pp. 3, 8) cites this work as the LQ-execution case where memory leads to Fredholm/Volterra/Riccati equations without a lift; stated there, not here."
---

# Optimal Liquidation with Signals: the General Propagator Case

## Bibliographic Details

Abi Jaber, Eduardo, and Eyal Neuman. 2025. "Optimal Liquidation With Signals: The General Propagator
Case." *Mathematical Finance* 35(4): 841–866. doi 10.1111/mafi.12465. Preprint arXiv:2211.00447v2
[q-fin.TR], 15 September 2025, 55 pp. Code: Colab notebook linked in fn. 1 (p. 4).

**Read: arXiv 2211.00447v2 (preprint); page and equation numbers follow that version.** (Non-core
work; preprint accepted under the project's preprint policy. The published version exists, hence
`based_on: preprint`.) Printed page numbers equal PDF page numbers.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $Q^u_t=q-\int_0^tu_sds$ | inventory | $q_t$ |
| $u_t$ | selling speed (control) | no project symbol |
| $P_t$ | unaffected price, progressively measurable; carries the signal $\mathbb E[P_s-P_T\mid\mathcal F_t]$ | ≈ $S_t$ with drift |
| $\lambda$ | temporary impact | ⚠ **not** an intensity |
| $G(t,s)$ | Volterra propagator (transient-impact kernel) | ⚠ an *impact* kernel, not a Hawkes kernel |
| $Z^u_t=h_0(t)+\int_0^tG(t,s)u_sds$ | transient impact | — |
| $\phi$, $\varrho$ | running and terminal inventory penalties | $\phi\approx\tfrac12\gamma\sigma^2$ |
| $g^u_t(s)$ | "controlled adjusted forward process" $=1_{s\ge t}\mathbb E[X_s-\int_t^sK(s,r)u_rdr\mid\mathcal F_t]$ (3.7) | infinite-dimensional state (role of $\lambda$-memory in a lift) |
| $\Gamma^{-1}_t$, $\Psi_t$ | operator coefficient of the quadratic term; its Riccati representation (6.6) | ↔ $A$ (operator-valued) |
| $\Theta_t(s)$, $\chi_t$ | linear coefficient (L²-valued BSDE) and constant term | ↔ $B$, $C$ |
| $\rho$ (Section 5) | decay of the exponential kernel | ⚠ not a spectral radius |
| $\alpha$ (Section 5) | fractional kernel $(t-s)^{\alpha-1}$, $\alpha\in(1/2,1)$ | ⚠ not a Hawkes jump size |
| $\gamma,\sigma$ (Section 5) | Ornstein–Uhlenbeck signal parameters | ⚠ $\gamma$ not risk aversion |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (propagators; signals; exponential vs. general kernels; relation to Gatheral et al., Alfonsi–Schied, Neuman–Vo, Forde et al.) | 1–5 |
| ✓ F1 | 2 Model setup: price (2.4)–(2.5), objective (2.6)–(2.7), nonnegative-definite kernels (2.8)–(2.11), class $\mathcal G$ (Def. 2.3), Example 2.5 | 5–8 |
| ✓ F1 | 3 Transformation of the performance functional: (3.1)–(3.8) | 9–10 |
| ✓ F1 | 4 Main results: operators $D_t$, $\Gamma^{-1}_t$ (4.2)–(4.5); processes $\Theta$, $\chi$ (4.7)–(4.12); value ansatz (4.13); Thm. 4.4; Prop. 4.5; Remarks 4.6–4.9 | 10–15 |
| ✓ F1 | 5 Numerical illustration: Nyström scheme (5.1)–(5.10); examples with exponential and fractional kernels and OU signal; Table 1, Figs. 1–5 | 15–24 |
| ✓ F1 | 6 Derivation: covariance operator (6.1)–(6.4); Riccati operator (6.5)–(6.10), Lemmas 6.1–6.2; L²-valued BSDE (Prop. 6.3); verification (Lemmas 6.4–6.6, Prop. 6.7) | 20–37 |
| — | 7 Proof of Prop. 4.5 (Lemmas 7.1–7.4) | 37–41 |
| — | 8–11 Proofs of Lemma 6.8, Prop. 6.3, Lemma 6.2(ii), Lemmas 2.2, 4.1, 6.1 | 41–51 |
| — | References | 51–55 |

## Kernthesen

### 1. ⭐ Liquidation with temporary impact, a general Volterra propagator and a progressively measurable signal is a well-posed LQ problem (pp. 5–6)

Execution price $S^u_t=P_t-\lambda u_t-Z^u_t$ (2.4) with transient impact
$Z^u_t=h_0(t)+\int_0^tG(t,s)u_sds$ (2.5). The trader maximises
$J(u)=\mathbb E[\int_0^T(P_t-Z^u_t)u_tdt-\lambda\int_0^Tu_t^2dt+Q^u_TP_T-\phi\int_0^T(Q^u_t)^2dt-\varrho(Q^u_T)^2]$
(2.6) over progressively measurable speeds with $\mathbb E\sup u_t^2<\infty$ (2.3). The price $P$ need
not be a semimartingale; only (2.1) is required, which covers an integrated OU drift plus a
martingale (p. 5). The objective is risk-adjusted (inventory penalties), not CARA.

### 2. ⭐ The admissible kernels are the nonnegative-definite Volterra kernels — including singular power laws and non-convolution kernels (pp. 7–8)

$G$ is admissible if $\int\!\!\int(G(t,s)+G(s,t))f(s)f(t)\ge0$ (2.8) and two $L^2$ regularity conditions
hold (Def. 2.3). Lemma 2.2: a convolution kernel $H(t)=\int e^{-xt}\mu(dx)$ (completely monotone) is
nonnegative definite. Example 2.5 lists a shifted power law in $(\ell_0+t)^{-\beta}$, the singular power law
$H(t)=t^{-\gamma}$ with $0<\gamma<1/2$, exponentials and their combinations, and a non-convolution bond
kernel $f(t-T)H(t-s)$ (p. 8). Remark 2.1: with a martingale price, (2.10) rules out price manipulation;
«once the price process is no longer a martingale, as in the setting of this paper, round trips are
possible» (p. 7).

### 3. ⭐⭐ Exponential propagators make the problem Markovian; general propagators make it path-dependent (pp. 3–4)

«The special case where the propagator is exponential simplifies the liquidation problem, as the
transient price impact can be written as a state variable and the problem becomes Markovian» (p. 3).
A general Volterra kernel «turns the stochastic control problem to become non-Markovian as the state
variables (e.g. the execution price) depend on the entire trading trajectory» (p. 4). Results for
general kernels were «scarce as the associated stochastic control problem is non-Markovian and often
singular» (p. 3).

### 4. The problem is recast with an infinite-dimensional state: the conditional forward curve of (impact, inventory) (pp. 9–10)

The terminal penalty is folded into the running cost via $Y^u:=Z^u-2\varrho Q^u$ (3.2), giving a
modified kernel $\tilde G=2\varrho1_{s<t}+G$ (3.4). With $X^u=(Y^u,Q^u)$ and
$K(t,s)=(\tilde G(t,s),-1_{s\le t})^\top$, the state is the "controlled adjusted forward process"
$g^u_t(s)=1_{s\ge t}(g_0(s)+\int_0^tK(s,r)u_rdr)$ (3.7), an $L^2([0,T],\mathbb R^2)$-valued process with
$g^u_t(t)=X^u_t$ (3.8). Its second component is just $Q^u_t$, «since Q is Markovian» (p. 10).

### 5. ⭐⭐ The value function is quadratic in the forward curve with an operator coefficient, linear through an L²-valued BSDE and linear in the signal (pp. 12–13)

Candidate (4.13):
$V^u_t=\frac12(\langle g^u_t,\Gamma^{-1}_tg^u_t\rangle_{L^2}+2\langle\Theta_t,g^u_t\rangle_{L^2}+2\mathbb E[P_T\mid\mathcal F_t]Q^u_t+\chi_t)$,
«the infinite dimensional analogue of standard liquidation problems with signals» (p. 12). Thm. 4.4
(p. 13): for $\lambda>0$, $\varrho,\phi\ge0$ there is a unique optimum
$u^*_t=\frac1{2\lambda}(\mathbb E[P_t-P_T\mid\mathcal F_t]-Y^{u^*}_t+\langle\Theta_t,K_t\rangle+\langle\Gamma^{-1}_tK_t,g^{u^*}_t\rangle)$
(4.15), and the value is (4.13) along $u^*$. $\Theta$ solves a free-boundary L²-valued BSDE (6.11)–(6.12,
Prop. 6.3, p. 26); $\chi$ solves the scalar BSDE (4.11).

### 6. ⭐ The optimal speed is the solution of a linear Volterra equation, given in closed form (pp. 13–14)

Because $g^u$ is linear in $u$, (4.15) is equivalent to $u^*_t=a_t+\int_0^tB(t,s)u^*_sds$ (4.16) with
explicit $a$ (linear in the signal) and deterministic kernel $B$ (4.17). Prop. 4.5:
$u^*=(\mathrm{id}-\boldsymbol B)^{-1}a$ (p. 14). Remark 4.6: with a martingale price and $G\equiv0$
this is the continuous-time Almgren–Chriss solution. Remark 4.7: it generalises Neuman–Vo [38]
(exponential kernel, semimartingale signal).

### 7. ⭐⭐ The operator coefficient solves an operator Riccati equation that is solved explicitly (pp. 22, 25)

With the covariance operator $\Sigma_t(s,u)=\frac1{4\lambda}\int_t^{s\wedge u}K(s,z)K(u,z)^\top dz$ (6.1), its
adjusted version $\tilde\Sigma_t=(\mathrm{id}-\frac1{2\lambda}\hat K)^{-1}\Sigma_t(\mathrm{id}-\frac1{2\lambda}\hat K^*)^{-1}$
(6.4) and $A=\mathrm{diag}(\frac1{2\lambda},-2\phi)$ (6.5), the operator
$\Psi_t=(\mathrm{id}-\frac1{2\lambda}\hat K^*)^{-1}A(\mathrm{id}-2\tilde\Sigma_tA)^{-1}(\mathrm{id}-\frac1{2\lambda}\hat K)^{-1}$
(6.6) coincides with $\Gamma^{-1}_t$ on the relevant test functions (Lemma 6.1) and satisfies
$\dot\Psi_t=2\Psi_t\dot\Sigma_t\Psi_t$, $\Psi_T=(\mathrm{id}-\frac1{2\lambda}\hat K^*)^{-1}A(\mathrm{id}-\frac1{2\lambda}\hat K)^{-1}$
(6.9), with $\dot\Sigma_t(s,u)=-\frac1{4\lambda}K(s,t)K(u,t)^\top$ (6.10). The Riccati is driven only by the
kernel's "covariance"; its proof follows Abi Jaber–Miller–Pham [3, Lemma 5.6] (p. 26).

### 8. ⭐ This extends Alfonsi–Schied, whose function-valued Riccati was solvable only for finite sums of exponentials (pp. 4, 14–15)

Alfonsi–Schied [7] needed completely monotone convolution kernels with $G(+0)<\infty$ (excluding
fractional kernels) and a deterministic problem; «their Riccati equation in general cannot be solved
explicitly, and the only tractable example provided is when G is a finite sum of exponential
kernels. In this work we solve explicitly the operator Riccati equation» (p. 4). The present setting
adds a non-martingale price (so the problem becomes stochastic), risk aversion $\phi$, and singular
and non-convolution kernels (Remark 4.8, p. 14).

### 9. ⭐⭐ For completely monotone kernels the operator solution is equivalent to a Markov lift with an infinite-dimensional Riccati (pp. 14–15)

Remark 4.9: if $G$ is a convolution with a completely monotone $H=\int e^{-x\cdot}\mu(dx)$, then
«introducing the Markovian auxiliary variables $\tilde Z^u_t(x):=\int_0^te^{-x(t-s)}u_sds$» lets the value
function «be re-expressed as linear-quadratic in $(\tilde Z,Q)$», with a quadratic term
$\int\!\!\int\tilde Z_t(x)^\top\Gamma_t(x,y)\tilde Z_t(y)\mu(dx)\mu(dy)$, and $\Gamma$ «solves an
infinite-dimensional Riccati equation, in line with the equations in [6]» (pp. 14–15). The operator
route therefore contains the lift as a special case, and does not need it.

### 10. ⭐ The explicit formulas are implemented by a Nyström discretisation: a few matrices and one linear solve (pp. 15–18)

On a grid $0=t_0<\dots<t_n=T$, $u^{(n)}=(I_{n+1}-B^{(n)})^{-1}a^{(n)}$ (5.1). Only three matrices depend
on the inputs: $N$ (signal conditional expectations, 5.3) and the lower/upper triangular kernel
integrals $L,U$ (5.4)–(5.5). For $\phi=0$, $D_t$ is approximated by $D^{(n)}_{t_i}=2\lambda I_n+d^{(n)}_{t_i}$
(5.6)–(5.7), and $a^{(n)},B^{(n)}$ follow by (5.9)–(5.10). Summary of the four-step implementation on
p. 18; $L,U$ are explicit for no-transient, exponential and fractional kernels (Table 1, p. 19).

### 11. Power-law impact makes trading more restrained and impact more persistent than exponential impact (pp. 19–24)

Without a signal, «the optimal strategy in the power law case is more restrained than the one of the
exponential kernel, as the transient price impact resulting by trades has a slower decay» (Fig. 1,
p. 19). With an OU signal the gap grows for a negative signal and shrinks for a positive one (Fig. 2,
pp. 20–21); «the price impact induced by the power law kernel is significantly more persistent» (Fig.
3, p. 20). With a positive signal and long horizon the agent «is first buying in order to make a quick
profit and then selling» (Fig. 5, p. 20).

### 12. Small fractional exponents and slow exponential decay both slow the trader down (p. 20)

Fig. 4 (p. 23): «for small values of α, the kernel $t\mapsto t^{\alpha-1}$ induces more price impact over
small time intervals enforcing the agent to trade slower. On the other hand when ρ increases the price
impact induced by kernel $t\mapsto e^{-\rho t}$ decays faster which allows the agent to trade faster»
(p. 20). U-shaped speed profiles appear under transient impact, against a flat Almgren–Chriss speed.

## Figures and tables

- Table 1 (p. 19): explicit $L$, $U$ entries for no-transient, exponential and fractional kernels.
- Figs. 1–3 (pp. 19–22): speed, inventory and transient impact, no signal / OU signal.
- Figs. 4–5 (pp. 23–24): sensitivity in the fractional exponent $\alpha$ and exponential decay $\rho$.

## What this source does not address

- **Order flow, point processes, Hawkes.** Memory sits in the *price-impact* kernel acting on the
  trader's own speed; there is no order arrival process. Hawkes execution with controlled baseline:
  [[fu-2022-portfolio-liquidation-games]]; Hawkes market making: [[jusselin-2021-persistent-order-flow]],
  [[barzykin-2026-hawkes-driven-otc]].
- **Market making / quote control / fills.** No quotes, no $f(\delta)$, no Hamiltonian.
- **Several assets.** One asset; the state is $\mathbb R^2$-valued only because it stacks impact and
  inventory. Multivariate Volterra LQ is in Abi Jaber–Miller–Pham [3] (not in the library).
- **Error analysis of the Nyström scheme.** Convergence in $n$ is not quantified; no benchmark against
  a lifted solver.
- **CARA utility, regret numbers.** None.

## Model card

| Field | Value |
|---|---|
| Assets | 1 |
| Kernel | n/a for order flow — no point process. The impact propagator is any nonnegative-definite Volterra kernel: exponential, power law $t^{-\gamma}$ ($\gamma<1/2$), shifted power law, non-convolution (Example 2.5) |
| Excitation | n/a — no order-flow excitation; the trader's own past speed feeds transient impact |
| Who excites the flow | n/a — no flow |
| Objective | maximise expected revenue minus temporary/transient impact costs and running/terminal inventory penalties (2.6); risk-adjusted, not CARA |
| Solution method | infinite-dimensional LQ control: value quadratic in an $L^2$-valued state with operator coefficient $\Gamma^{-1}_t$ solving an explicit operator Riccati (6.6)/(6.9), linear part from an L²-valued BSDE; optimal speed from a linear Volterra equation (Prop. 4.5); Nyström discretisation |
| Benchmark | no-transient case $G\equiv0$ (Almgren–Chriss) and exponential vs. fractional kernels |
| Reported regret / gap numbers | n/a — qualitative figures only |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 3, 5, 7, 8, 9, 10.**

### What this focus needs beyond the Kernthesen

1. **No order flow at all.** The memory kernel acts on the trader's own control path, so there is
   nothing self- or cross-exciting to model. The paper bears on the focus only through its closure
   technique.
2. **Why the closure holds [I].** The state $g^u_t$ is linear in the control and the objective is
   quadratic, so the value stays exactly quadratic for *any* nonnegative-definite kernel; memory only
   makes the coefficient an operator. This is the precise sense of Barzykin's remark that «Memory
   therefore does not by itself preclude tractable control» (his p. 3, see
   [[barzykin-2026-hawkes-driven-otc]] Kernthese 11). The closure would break if the control entered
   through a nonlinear map multiplying a random intensity, i.e. the market-making Hamiltonian
   ([[hamiltonian-quadratic-approximation]]).
3. **Lift vs. operator route [I].** Remark 4.9 shows that for completely monotone kernels the
   operator Riccati is equivalent to an infinite [[markov-lift]] with Riccati $\Gamma_t(x,y)$. For a
   power-law Hawkes kernel in a market-making problem, the analogous choice is between a
   sum-of-exponentials lift (finite but approximate) and a Nyström-discretised operator object (exact
   up to quadrature). The paper's numerics show the latter is cheap: a few $n\times n$ matrices and one
   linear solve (Kernthese 10).
4. **Carry-over to several assets [I].** The operator framework is already $L^2([0,T],\mathbb R^2)$-valued;
   replacing $\mathbb R^2$ by $\mathbb R^{2d}$ with a matrix propagator $G(t,s)\in\mathbb R^{d\times d}$
   (cross-impact) looks formally direct, with nonnegative definiteness of the matrix kernel as the
   key condition. Not in the source.
5. **Bearing on Stage 2a.** Indirect: no perturbative expansion, no intensity factor. It is the
   reference for "exact Riccati with memory when the problem is LQ". It sharpens the claim that
   Stage 2a's difficulty is the quote-controlled Hamiltonian, not the kernel.

### Direct quotes (for the draft)

> "The special case where the propagator is exponential simplifies the liquidation problem, as the transient price impact can be written as a state variable and the problem becomes Markovian." (p. 3)

> "However, as stated in Section 1.3 of [7], their Riccati equation in general cannot be solved explicitly, and the only tractable example provided is when G is a finite sum of exponential kernels. In this work we solve explicitly the operator Riccati equation (see (6.6)) along with all the other ingredients of the value function." (p. 4)

> "Our main result summarised in Theorem 4.4 and Proposition 4.5 shows that, remarkably, the problem can be solved explicitely despite the path-dependency of the model." (p. 6)

### Examples & illustrations (for later drafting)

- Remark 4.9 (pp. 14–15): one paragraph that maps the operator solution onto a Markov lift in the
  completely monotone case. A ready illustration of "lift as a special case of an operator Riccati".
- Table 1 (p. 19): fractional-kernel matrix entries in closed form, showing a singular power law
  costs no more to discretise than an exponential.
- Fig. 1 (p. 19): power-law vs. exponential speed profiles under otherwise identical parameters.

### Boundary of this focus

The source has no order flow, no quotes and one asset; items 2–5 are the project's inferences about
transfer. It offers no numbers for the closed-form / exact / RL comparison.

## Mentioned entities

- Concepts: [[markov-lift]], [[volterra-riccati]], [[matrix-riccati-equation]] (operator-valued analogue), [[hamiltonian-quadratic-approximation]] (absent here; contrast).
- Other works (bibkeys / not in library): Alfonsi & Schied 2013 [7]; Gatheral, Schied & Slynko 2012 [24]; Neuman & Vo 2022 [38]; Forde, Sánchez-Betancourt & Smith 2022 [21]; Abi Jaber, Miller & Pham 2021 SIFIN [3] and SICON [4]; Abi Jaber 2022 [6]; Obizhaeva & Wang 2013 [40]; Almgren & Chriss [8, 9]; Bouchaud et al. [13].

## Connections

- Builds on: [[abijaber-2021-linear-quadratic-control]] (LQ stochastic Volterra control; Riccati machinery).
- Cited by: [[barzykin-2026-hawkes-driven-otc]] as the case where memory does not break tractability (Kernthese 11 there).
- Contrast: [[fu-2022-portfolio-liquidation-games]] (memory in a controlled Hawkes order flow, collapsed to its mean); [[volterra-riccati]] (certainty-equivalent, not exact).
- Lift relation: [[markov-lift]] (Remark 4.9).
