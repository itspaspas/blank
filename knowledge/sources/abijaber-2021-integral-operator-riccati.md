---
title: "Abi Jaber, Miller & Pham 2021 — Integral operator Riccati equations arising in stochastic Volterra control problems"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: abijaber-2021-integral-operator-riccati
depth: standard
based_on: preprint
tags: [integral-operator-riccati, infinite-dimensional-riccati, stochastic-volterra, linear-quadratic-control, lyapunov-equation, markov-lift, completely-monotone-kernel, existence-uniqueness, non-market-making]
relations:
  - target: matrix-riccati-equation
    type: builds-on
    confidence: extracted
    because: "The kernel equation (1.1) is «the infinite dimensional analogue of matrix Riccati equations» (abstract, p. 1); for a finite atomic measure it «reduces to a n × n-matrix Riccati equation» (p. 2). Existence proof adapts the finite-dimensional LQ technique of Yong–Zhou Thm 6.7.2 (p. 4)."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "«our motivation for studying the Riccati equation (1.1) comes from infinite dimensional lifts of LQ control theory of non-Markovian stochastic Volterra equations» (p. 2), with kernel K(t)=∫e^{-θt}μ(dθ), which covers the fractional kernel (pp. 2–3). Brownian noise only; no point processes."
  - target: abijaber-2021-linear-quadratic-control
    type: cites
    confidence: extracted
    because: "The Volterra LQ problem «can be explicitly solved using the Riccati equation (1.1), see [2]» (p. 3), [2] = Abi Jaber–Miller–Pham, Linear–Quadratic control for a class of stochastic Volterra equations (companion paper)."
  - target: volterra-riccati
    type: mentions
    confidence: inferred
    because: "Same words, different object: here an exact kernel Riccati Γ_t(θ,τ) for a Brownian LQ problem (eq. 1.1, p. 2), not Barzykin's certainty-equivalent Riccati along a frozen Hawkes forecast. Connected only by the idea that Volterra memory enters a Riccati system through a kernel."
---

# Integral operator Riccati equations arising in stochastic Volterra control problems

## Bibliographic Details

Abi Jaber, Eduardo; Miller, Enzo; Pham, Huyên. 2021. "Integral Operator Riccati Equations Arising
in Stochastic Volterra Control Problems." *SIAM Journal on Control and Optimization* 59 (2):
1581–1603. doi:10.1137/19M1298287.

**Read: arXiv 1911.01903v1 (preprint, dated 5/6 November 2019, 28 pp.); page and equation numbers
on this page follow that version.** The published SICON version (23 pp.) was not read and may differ
in numbering and content. Non-core work; preprint accepted under the project's preprint policy.
The v1 still carries an author's note in French inside Remark 2.2 («On utilise cette notation dans
le lemme 4.1(ii)», p. 5), which marks it as an early draft.

Field: infinite-dimensional linear-quadratic (LQ) control theory. Not a market-making or finance
paper; no numerics. Companion of [[abijaber-2021-linear-quadratic-control]], which states the
control problem this Riccati equation solves.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\mu$ | $d\times d'$ signed matrix measure on $\mathbb R_+$, possibly infinite (1.2) | ⚠ **not** the Hawkes baseline $\mu$ |
| $K(t)=\int e^{-\theta t}\mu(d\theta)$ | Volterra kernel (Laplace transform of $\mu$) | ⚠ **not** the branching matrix $K$; plays the role of a Hawkes kernel $g$ |
| $\theta,\tau\in\mathbb R_+$ | mean-reversion speeds indexing the lift factors | ⚠ **not** the reduced value $\theta$; ≈ decays $\beta$ |
| $\Gamma_t(\theta,\tau)$ | kernel solution of the Riccati equation, in $L^1(\mu\otimes\mu)$ | plays the role of the quadratic coefficient $A(t)$, but indexed by $(\theta,\tau)$ |
| $X_t$, $\alpha_t$ | controlled $d$-dim Volterra state, $m$-dim control | — |
| $B,C,D,F$ | drift/diffusion coefficients of state and control | ⚠ source $B,C$ ≠ project $B,C$ |
| $Q$, $N$ | running state cost, control cost ($N\ge\lambda I_m$) | ⚠ $\lambda$ here is a constant, **not** an intensity |
| $A^{mr}$ | mean-reverting operator $(A^{mr}\varphi)(\theta)=-\theta\varphi(\theta)$ | ≈ $-D$ in the lifted Hawkes dynamics |
| $W$ | one-dimensional Brownian motion | no point process anywhere |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract, keywords | 1 |
| ✓ F1 | 1 Introduction: kernel Riccati (1.1); finite-atom reduction; Volterra LQ motivation; operator form (1.4); why existing theory fails; proof plan | 2–4 |
| ✓ F1 | 2 Preliminaries and main result: spaces $L^1(\mu\otimes\mu)$, Def. 2.1 (symmetric, nonnegative), compact form (2.2)–(2.4), mild solution Def. 2.3 (2.5), Thm 2.4 | 5–6 |
| ✓ F1 | 3 Infinite-dimensional Lyapunov equation: Thm 3.1, Lemmas 3.3–3.5 (contraction, Gronwall bounds, continuity) | 7–12 |
| ✓ F1 | 4.1 Step 1: sequence of Lyapunov solutions (Lemma 4.1 monotonicity via the lifted SDE; induction (4.5)–(4.9)) | 12–15 |
| ✓ | 4.2 Step 2: convergence in $L^1(\mu\otimes\mu)$ (Lemmas 4.2–4.5) | 15–21 |
| ✓ | 4.3 Step 3: limit solves the Riccati equation (Lemma 4.6) | 21–22 |
| ✓ | 4.4 Step 4: continuity and uniqueness (Lemmas 4.7–4.8) | 22–25 |
| — | Appendix A: Cauchy–Schwarz for nonnegative kernels; difference equations (Lemma A.2) | 25–27 |
| — | References | 27–28 |

## Kernthesen

### 1. ⭐⭐ The object is a Riccati equation for a kernel $\Gamma_t(\theta,\tau)$, the infinite-dimensional analogue of the matrix Riccati equation (pp. 1–2)

Backward equation (1.1): $\Gamma_T=0$,
$\dot\Gamma_t(\theta,\tau)=(\theta+\tau)\Gamma_t(\theta,\tau)-Q-D^\top\!\int\!\!\int\mu(d\theta')^\top\Gamma_t(\theta',\tau')\mu(d\tau')D-B^\top\!\int\mu(d\theta')^\top\Gamma_t(\theta',\tau)-\int\Gamma_t(\theta,\tau')\mu(d\tau')B+S_t(\theta)^\top\hat N_t^{-1}S_t(\tau)$,
with $S_t$ and $\hat N_t=N+F^\top\!\int\!\!\int\mu^\top\Gamma_t\mu\,F$ (p. 2). Solutions are sought in
$L^1(\mu\otimes\mu)$; $\mu$ need not be finite but must satisfy $\int(1\wedge\theta^{-1/2})|\mu|(d\theta)<\infty$
(1.2). The abstract calls these equations «the infinite dimensional analogue of matrix Riccati
equations» (p. 1). The term $(\theta+\tau)\Gamma$ is the mean reversion of the lifted factors.

### 2. ⭐⭐ A finite atomic measure gives back an ordinary $n\times n$ matrix Riccati equation (p. 2)

«In particular, if $d=d'=1$ and $\mu(d\theta)=\sum_{i=1}^n\delta_{\theta_i^n}(d\theta)$, (1.1) reduces to a $n\times n$-matrix
Riccati equation for $\Gamma^n=(\Gamma(\theta_i^n,\theta_j^n))_{1\le i,j\le n}$, only written componentwise» (p. 2).
Setting $\mu=I_d\delta_0$ recovers the $d\times d$ matrix Riccati equation of classical LQ control
(p. 2). A sum of $n$ exponentials therefore lifts to an $n$-dimensional Markov state and an
$n\times n$ Riccati system. This is the same reduction the project relies on when it lifts an
exponential Hawkes kernel.

### 3. ⭐⭐ The motivation is the LQ control of a stochastic Volterra equation through its Markov lift (pp. 2–3)

Controlled state: $X_t=\int_0^tK(t-s)(BX_s+C\alpha_s)ds+\int_0^tK(t-s)(DX_s+F\alpha_s)dW_s$ with
$K(t)=\int e^{-\theta t}\mu(d\theta)$ (p. 2). Cost $J(\alpha)=\mathbb E\int_0^T(X_t^\top QX_t+\alpha_t^\top N\alpha_t)dt$,
which «can be explicitly solved using the Riccati equation (1.1), see [2]» (p. 3). Condition (1.2)
«allows singularity of the kernel $K$ at 0, and includes the case of a fractional kernel
$K_H(t)=t^{H-1/2}$ with Hurst parameter $H\in(0,1/2)$», with $\mu(d\theta)=c_H\theta^{-H-1/2}d\theta$ (p. 3). The
lift itself, and the value function, are in the companion paper.

### 4. The same equation computes Laplace transforms of integrated Gaussian Volterra processes (p. 3)

When $D=F=0$, (1.1) «also enters in the computation of the Laplace transform of
$\mathrm{tr}(\int_0^TZ_s^\top QZ_sds)$» for a matrix Gaussian Volterra process $Z$ (p. 3), with a reference
to a Volterra Wishart paper in preparation. The Riccati equation is thus also a tool for exponential
moments, not only for control.

### 5. ⭐ An equivalent operator Riccati equation exists, with the mean-reverting operator as generator (pp. 3–4)

The integral operator $\boldsymbol\Gamma_t$ with kernel $\Gamma_t$ solves (1.4):
$\dot{\boldsymbol\Gamma}_t=-\boldsymbol\Gamma_tA^{mr}-(\boldsymbol\Gamma_tA^{mr})^*-Q-D^*\boldsymbol\Gamma_tD-B^*\boldsymbol\Gamma_t-(B^*\boldsymbol\Gamma_t)^*+(C^*\boldsymbol\Gamma_t+F^*\boldsymbol\Gamma_tD)^*(N+F^*\boldsymbol\Gamma_tF)^{-1}(C^*\boldsymbol\Gamma_t+F^*\boldsymbol\Gamma_tD)$,
where $(A^{mr}\varphi)(\theta)=-\theta\varphi(\theta)$ (p. 3). This is the standard form of Riccati equations in
Hilbert- or Banach-space LQ theory (p. 4).

### 6. ⭐ Existing operator-Riccati theory does not apply, for two reasons (p. 4)

«First, they are valid for Hilbert and reflexive Banach spaces, while $L^1(\mu)$ is in general not
reflexive, unless $\mu$ has finite support, and mostly apply to the cases without multiplicative
noise, i.e., $D=0$, and without control on the diffusion coefficient, i.e. $F=0$ … Second, they
concern the operator Riccati equation (1.4), which is not enough for our purposes, as we still need
to argue that $\boldsymbol\Gamma$ is an integral operator induced by some bounded symmetric kernel» (p. 4). The
authors therefore work on the kernel equation directly.

### 7. ⭐⭐ Main result: a unique nonnegative symmetric kernel solution exists under definite costs (p. 6)

Theorem 2.4: if $Q\in\mathbb S^d_+$ and $N-\lambda I_m\in\mathbb S^m_+$ for some $\lambda>0$ (2.6), there is a unique
$\Gamma\in C([0,T],L^1(\mu\otimes\mu))$ solving the kernel Riccati equation (2.2) with $\Gamma_t\in\mathbb S^d_+(\mu\otimes\mu)$,
and $\int|\mu|(d\tau)|\Gamma_t(\theta,\tau)|\le M$ $\mu$-a.e. (2.7) (p. 6). Solutions are understood in mild form
(2.5): $\Gamma_t(\theta,\tau)=\int_t^Te^{-(\theta+\tau)(s-t)}\mathcal R(\Gamma_s)(\theta,\tau)ds$ (p. 6). The cost is definite
($Q\ge0$, $N$ uniformly positive): the indefinite case is not treated.

### 8. ⭐ The linear (Lyapunov) kernel equation is solved by a contraction argument and Gronwall bounds (pp. 7–12)

Theorem 3.1: the Lyapunov equation (3.2)–(3.3),
$\Gamma_t=\int_t^Te^{-(\theta+\tau)(s-t)}F(s,\Gamma_s)ds$, with bounded coefficients $\tilde Q,\tilde B^i,\tilde D^i$ (3.4),
has a unique solution in $C([0,T],L^1(\mu_1\otimes\mu_2))$ with uniform bounds (3.5)–(3.7) (p. 7).
Existence follows from the contraction mapping principle in a weighted sup norm (Lemma 3.3,
pp. 8–9), using only $K_i\in L^2(0,T)$. The bounds come from «the generalized Gronwall inequality for
convolution equations» (Lemma 3.4, p. 10), and continuity in $t$ from the $L^2$-continuity of
translations of $K$ (Lemma 3.5, pp. 10–12).

### 9. ⭐⭐ The Riccati solution is built as the limit of successive Lyapunov solutions (pp. 4, 12–15)

Four steps, «adapting the technique used in classical linear-quadratic control theory [14,
Theorem 6.7.2]»: «(i) Construct a sequence of Lyapunov solutions $(\Gamma^i)_{i\ge0}$ by successive
iterations, (ii) Establish the convergence of $(\Gamma^i)_{i\ge0}$ in $L^1(\mu\otimes\mu)$, (iii) Prove that the
limiting point is a solution to the Riccati equation (2.5), (iv) Derive the estimate (2.7), the
continuity and the uniqueness» (p. 12). At step $i$ the feedback gain $\Theta^i_t(\tau)$ is computed from
$\Gamma^i$, the coefficients are frozen as $\tilde Q^i=Q+\Theta^{i\top}N\Theta^i$, $\tilde B^i=B+C\Theta^i$, $\tilde D^i=D+F\Theta^i$ (4.8),
and $\Gamma^{i+1}$ solves a Lyapunov equation (4.9) (pp. 14–15). This is policy iteration on the Riccati
equation.

### 10. ⭐ Monotonicity comes from a probabilistic representation through the lifted SDE (pp. 12–16)

Lemma 4.1: the Lyapunov solution is nonnegative and non-increasing in $t$. The proof applies Itô's
formula to $\langle Y_s,\boldsymbol\Gamma_sY_s\rangle$ for the $L^1(\mu)$-valued lifted process
$dY_s(\theta)=(-\theta Y_s(\theta)+\int\tilde B_s\mu Y_s)ds+(\int\tilde D_s\mu Y_s)dW_s$, giving
$\langle\varphi,\boldsymbol\Gamma_t\varphi\rangle=\mathbb E\int_t^T\langle Y_s,\tilde Q_sY_s\rangle ds$ (pp. 13). Lemma 4.2: the iterates decrease,
$0\le U^{i+1}_t\le U^i_t$ for $U^i=\int\!\!\int\mu^\top\Gamma^i\mu$ (p. 16). The quadratic form of the Riccati kernel is
therefore a value function of the lifted Markov system.

### 11. Convergence of kernels, not just of operators, is the hard part (pp. 4, 17–21)

«The reason is that we need to establish the convergence of the kernels $(\Gamma^i)_{i\ge0}$ which is a
stronger requirement than the usual convergence of the operators $(\boldsymbol\Gamma^i)_{i\ge0}$» (p. 4). The
argument uses a uniform bound on $\int\Gamma^i\mu$ (Lemma 4.3), Dini's theorem for uniform convergence
of $U^i$ (Lemma 4.4), and a Cauchy estimate in $L^1(\mu\otimes\mu)$ via two Gronwall steps (Lemma 4.5,
pp. 19–21).

### 12. Uniqueness: the difference of two solutions solves a homogeneous linear Lyapunov equation (pp. 24–25)

For two solutions $\Gamma^a,\Gamma^b$ with the bounds (2.7), (4.27), $\Delta=\Gamma^a-\Gamma^b$ solves a Lyapunov equation
«with bounded coefficients, and no affine term» (4.30). The generalized Gronwall inequality gives
$\|\Delta_t\|_{L^1(\mu\otimes\mu)}=0$ (p. 25). The nonlinear feedback term is rewritten as linear in $\Delta$
using $A^{-1}-B^{-1}=B^{-1}(B-A)A^{-1}$ (pp. 24–25).

### 13. Multiplicative noise and control in the diffusion are covered; jumps are not (pp. 2, 4)

$D$ and $F$ may be nonzero, which is the case the cited Hilbert-space works «mostly» exclude (p. 4).
The noise is a single Brownian motion $W$ (p. 3). Point processes, jump measures and
state-dependent intensities do not appear anywhere in the paper.

## What this source does not address

- **Point-process or Hawkes noise.** Only Brownian motion (p. 3). No intensity, no compensator.
- **Nonlinear Hamiltonians.** The problem is LQ: dynamics linear in state and control, quadratic
  cost. No supremum over quotes, no fill probability.
- **Indefinite costs.** $Q\ge0$ and $N\ge\lambda I$ are assumed (2.6, p. 6).
- **The control problem and the lift.** Only cited from the companion paper ([2], p. 3).
- **Approximation by finite atoms and its error.** Not treated here; that is the companion paper's
  topic.
- **Numerics, finance, market making.** None.

## Model card

n/a — not a market-making model. For the record: assets n/a (state dimension $d$, control dimension
$m$) · kernel: Volterra kernel $K(t)=\int e^{-\theta t}\mu(d\theta)$ (completely-monotone type, possibly singular,
e.g. fractional) acting on Brownian-driven linear dynamics, not on a point process · excitation:
none · who excites the flow: n/a · objective: quadratic LQ cost $\mathbb E\int(X^\top QX+\alpha^\top N\alpha)dt$ (definite) ·
solution method: existence/uniqueness of the kernel Riccati equation by successive Lyapunov
iterations, contraction and Gronwall · benchmark: none · reported numbers: none.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 1, 2, 3, 7, 9, 10, 13.**

*Read as lift-and-Riccati theory:* there is no order flow in this paper. What it offers is the
closure mechanism for the quadratic value of a lifted Volterra system, and its limits.

### What this focus needs beyond the Kernthesen

1. **Verdict: no self- or cross-exciting flow; the paper supplies the Riccati side of the lift.**
   The memory kernel acts on a Brownian-driven linear state (p. 2). Closure is exact because the
   problem is LQ. With a finite sum of exponentials the closure is an ordinary $n\times n$ matrix
   Riccati (Kernthese 2). For a general completely-monotone kernel, the fractional one included, it
   is a kernel Riccati in $L^1(\mu\otimes\mu)$ (Kernthesen 1, 7). Cite it as the existence theory for
   "Riccati of a lifted Volterra system", not as a market-making precedent.
2. **Where the closure holds and where it breaks [I from the structure of (1.1)].** It holds
   because all three LQ conditions are met: state dynamics linear in $(X,\alpha)$, quadratic cost, and
   noise coefficients linear in $(X,\alpha)$. Flow-driven Hawkes market making violates the first
   one in the relevant sense: the control (quote) enters through a nonlinear fill probability that
   multiplies the intensity, $\lambda_jH(p^j)$. So the quadratic ansatz no longer closes exactly
   (cf. [[hamiltonian-quadratic-approximation]], [[fujii-2015-optimal-position-management]] focus 1,
   item 3). The paper says nothing about point-process noise either (Kernthese 13).
3. **What would carry over to a power-law Hawkes lift [I, not the authors'].** A Hawkes kernel of
   completely-monotone form $g(t)=\int e^{-\theta t}\mu(d\theta)$ lifts to factors $U_t(\theta)$, each mean-reverting
   at rate $\theta$ and jumping at every event. If the reduced value were expanded with coefficients
   affine in the lifted intensity, those coefficients would be functions of $\theta$. The order-1
   equations would then be linear kernel equations with the transport term $(\theta+\tau)\Gamma$, of the
   Lyapunov type covered by Theorem 3.1. Existence for such linear equations with bounded
   coefficients is therefore available off the shelf. Point-process noise would add jump terms
   that Theorem 3.1 does not contain.
4. **Multi-asset content [I].** $\mu$ is a $d\times d'$ *matrix* measure, so $K$ is a matrix kernel
   whose entries can have different decay spectra (p. 2). The formalism already hosts cross-component
   memory $K_{ij}(t)=\int e^{-\theta t}\mu_{ij}(d\theta)$. That is the shape a cross-asset Hawkes kernel with
   distinct cross-decays would take. The paper proves nothing about cross-excitation itself, since
   its state is a Brownian Volterra process.
5. **Bearing on D2 ($\lambda$-dependent Riccati coefficients).** Indirect. In this paper the
   Riccati unknown is indexed by the lift variables $(\theta,\tau)$, not by the current value of the
   factor. The state-dependence of the value is entirely carried by the quadratic form
   $\langle Y,\boldsymbol\Gamma Y\rangle$ in the lifted state (Kernthese 10). That is the LQ analogue of a value that is
   quadratic jointly in inventory and lifted intensity. It is the structure a Hawkes problem would
   need for an exact closure, and the market-making Hamiltonian prevents it.

### Bearing on Stage 2a (`input/ideas/hawkes-perturbative-closed-form-design.md`) [I]

- **S1 global existence: a usable technique.** Stage 2a must check global existence of the order-0
  Riccati with a time-dependent deterministic forecast $m(t)$, and of the coupled order-1 system.
  Successive Lyapunov iteration with monotone convergence (Kernthesen 9–10) is the classical route
  (Yong–Zhou Thm 6.7.2, which the paper adapts). In finite dimension it applies directly to a
  definite Riccati with continuous time-dependent coefficients.
- **Order-1 as a Lyapunov equation.** Stage 2a expects the order-1 system to be linear
  (Lyapunov/Sylvester) given $A^0$. Theorem 3.1 is the infinite-dimensional version of exactly that
  step. It becomes relevant only if Stage 2a moves beyond one exponential per asset-side.
- **Scope note.** Stage 2a fixes one exponential per asset-side, so the finite-atom case
  (Kernthese 2) is all it needs. This paper matters for a later power-law extension, not for Stage 2a.

### Direct quotes (for the draft)

> "Such equations can be seen as the infinite dimensional analogue of matrix Riccati equations and they appear in the Linear–Quadratic control theory of stochastic Volterra equations." (p. 1)

> "In particular, if d = d′ = 1 and µ(dθ) = Σ_{i=1}^n δ_{θ_i^n}(dθ), (1.1) reduces to a n × n-matrix Riccati equation for Γ^n = (Γ(θ_i^n, θ_j^n))_{1≤i,j≤n}, only written componentwise." (p. 2)

> "This is indeed the case, and our motivation for studying the Riccati equation (1.1) comes from infinite dimensional lifts of LQ control theory of non-Markovian stochastic Volterra equations." (p. 2)

> "The reason is that we need to establish the convergence of the kernels (Γ^i)_{i≥0} which is a stronger requirement than the usual convergence of the operators (**Γ**^i)_{i≥0}." (p. 4)

### Examples & illustrations (for later drafting)

- The fractional kernel $K_H(t)=t^{H-1/2}$ with $\mu(d\theta)=c_H\theta^{-H-1/2}d\theta$ (p. 3) is a ready example of a
  memory kernel that needs infinitely many lift factors. Use it to show why exponential kernels give
  finite Riccati systems and power-law ones do not.
- The four-step proof plan (p. 12) is a compact template for a policy-iteration existence proof.

### Boundary of this focus

Everything said here about Hawkes flow, market-making Hamiltonians and Stage 2a is the project's
inference. The paper has no point process, no market making and no numbers, so it cannot inform the
regret comparison.

## Mentioned entities

- Concepts: [[matrix-riccati-equation]], [[markov-lift]], [[volterra-riccati]] (contrast only), [[hamiltonian-quadratic-approximation]] (contrast, focus inference), [[hawkes-process]] (absent from the source; used only in the focus inference)
- Sources: [[abijaber-2021-linear-quadratic-control]] (companion; states the control problem), [[fujii-2015-optimal-position-management]] (contrast, focus inference)
- Works cited by the source, not in the library: Yong & Zhou 1999 (Thm 6.7.2); Gripenberg, Londen & Staffans 1990 (Volterra integral equations, generalized Gronwall); Curtain & Pritchard 1974; Da Prato 1984; Flandoli 1986; Guatteri & Tessitore 2005; Hu & Tang 2018; Koshkin 2016; Lasiecka 2005; Artamonov 2019; Alfonsi & Schied 2013; Abi Jaber (Volterra Wishart, in preparation).

## Connections

- Builds on: [[matrix-riccati-equation]], of which (1.1) is the kernel-valued generalisation.
- Supports: [[markov-lift]], by supplying the Riccati existence theory that makes the lifted LQ
  problem solvable.
- Companion: [[abijaber-2021-linear-quadratic-control]] (control problem, lift, finite-atom
  approximation).
- Contrast: [[volterra-riccati]] (Barzykin's certainty-equivalent object with the same name).
