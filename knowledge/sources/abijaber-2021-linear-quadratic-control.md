---
title: "Abi Jaber, Miller & Pham 2021 — Linear–quadratic control for a class of stochastic Volterra equations: solvability and approximation"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: abijaber-2021-linear-quadratic-control
depth: standard
based_on: preprint
tags: [stochastic-volterra, linear-quadratic-control, markov-lift, banach-space-riccati, integral-operator-riccati, sum-of-exponentials, kernel-approximation, fractional-brownian-motion, value-convergence]
relations:
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "Rigorous lift of a controlled Volterra SDE with completely-monotone-type kernel K(t)=∫e^{-θt}μ(dθ) into mean-reverting factors Y_t(θ) in L¹(μ): «we establish the correspondence of the initial problem with a lifted Markovian controlled system ... taking its values in the possibly infinite-dimensional Banach space L1(µ)» (p. 3); Thm 2.3 (p. 9). Brownian noise only."
  - target: matrix-riccati-equation
    type: supports
    confidence: extracted
    because: "For a sum-of-n-exponentials kernel «the problem reduces to a conventional linear-quadratic control for the finite-dimensional controlled system ... the standard n × n–matrix Riccati equation» (p. 18), eq. (3.18)."
  - target: volterra-riccati
    type: mentions
    confidence: inferred
    because: "Same words, different object: here the 'Riccati' is an exact integral-operator Riccati equation for the kernel Γ_t(θ,τ) of an LQ problem (eq. 3.2, p. 13), not Barzykin's certainty-equivalent forecast-frozen ODE. Only the shared idea — Volterra memory enters a Riccati system through a kernel/forecast — connects them."
  - target: abijaber-2021-integral-operator-riccati
    type: builds-on
    confidence: extracted
    because: "«The existence and uniqueness of a solution to the Riccati system follows from [5]» (p. 15), [5] = Abi Jaber–Miller–Pham, Integral operator Riccati equations, arXiv:1911.01903."
---

# Linear–quadratic control for a class of stochastic Volterra equations: solvability and approximation

## Bibliographic Details

Abi Jaber, Eduardo; Miller, Enzo; Pham, Huyên. 2021. "Linear–quadratic control for a class of
stochastic Volterra equations: Solvability and approximation." *The Annals of Applied Probability*
31(5): 2244–2274. DOI 10.1214/20-AAP1645.

**Read:** arXiv 1911.01900v3 (preprint, dated 26/30 Nov 2020); page/equation numbers on this page
follow it (41 pp.). The published AAP version was not read. Non-core work; preprint accepted under
the project's preprint policy.

### Notation map (source → project)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $X^\alpha_t$ | controlled $d$-dim. Volterra state (eq. 2.1) | no MM analogue; ⚠ not cash $X_t$ |
| $\alpha_t\in\mathbb R^m$ | control | ⚠ not a Hawkes jump size |
| $K(t)=\int e^{-\theta t}\mu(d\theta)$ | convolution kernel, Laplace transform of a signed matrix measure $\mu$ (eq. 2.2) | kernel; ⚠ project $K$ = branching matrix |
| $\theta$ | mean-reversion speed of one factor | decay $\beta$ |
| $Y_t(\theta)$ | lifted factor (eq. 2.13) | lifted Hawkes memory factor ([[markov-lift]]) |
| $\Gamma_t(\theta,\tau),\Lambda_t(\theta),\chi_t$ | quadratic kernel, linear kernel, constant of the value (eq. 3.1) | analogue of $A,B,C$ |
| $Q,N,L$ | running-cost matrices (eq. 2.7) | ⚠ project $Q$ = inventory bound |
| $B,C,D,F$; $\beta,\gamma$ | linear drift / diffusion coefficients; affine terms | ⚠ project $\gamma$ = risk aversion |
| $\mu^n$, $K^n$ | discretised measure / $n$-factor kernel (eqs. 3.15, 3.19, 3.25) | $p$-factor truncation (E0) |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (LQ regulator with memory, lifts, related literature) | 2–5 |
| ✓ F1 | 2 Formulation (eq. 2.1, admissible set, kernel conditions 2.3–2.4, Example 2.2) | 5–8 |
| ✓ F1 | 2.1 Markovian representation (Thm 2.3, Remarks 2.4–2.5) | 8–11 |
| ✓ F1 | 2.2 Formal derivation (operator Riccati in $L^1(\mu)$) | 11–13 |
| ✓ F1 | 3.1 Solvability (Riccati system 3.2, Thm 3.4, Thm 3.7, Example 3.9, Remark 3.10, Example 3.11) | 13–19 |
| ✓ F1 | 3.2 Stability and approximation by conventional LQ problems (Thm 3.13, eq. 3.25) | 19–21 |
| ✓ F1 (skim) | 4 Infinite-dimensional SDE with Lipschitz coefficients (Thm 4.1, Lemma 4.3, Thm 4.4) | 21–26 |
| ✓ F1 (skim) | 5 Martingale verification (Lemma 5.1, Thm 5.2, Remark 5.3) | 26–31 |
| ✓ F1 (skim) | 6 Proof of solvability | 32–33 |
| ✓ F1 | 7 Stability and approximation (Lemmas 7.1–7.4, proof of Thm 3.13) | 33–39 |
| — | Appendix A (Lemma A.1), References | 39–41 |

## Kernthesen

### 1. The object is a controlled linear Volterra SDE with a Laplace-transform kernel, possibly singular at zero (pp. 5–8)

State (eq. 2.1): $X^\alpha_t=g_0(t)+\int_0^tK(t-s)b(s,X_s,\alpha_s)ds+\int_0^tK(t-s)\sigma(s,X_s,\alpha_s)dW_s$,
with affine $b=\beta(t)+BX+C\alpha$, $\sigma=\gamma(t)+DX+F\alpha$ (p. 6). The kernel is
$K(t)=\int_{\mathbb R_+}e^{-\theta t}\mu(d\theta)$ (eq. 2.2) for a signed $d\times d'$ measure with
$\int(1\wedge\theta^{-1/2})|\mu|(d\theta)<\infty$ (eq. 2.3) and a Hölder-type condition (eq. 2.4).
This admits $\mu_{ij}(\mathbb R_+)=\pm\infty$, i.e. a kernel singular at 0, and covers the fractional
kernel $t^{H-1/2}/\Gamma(H+1/2)$, $H<1/2$ (Example 2.2, p. 8). Note that **the control sits inside the
convolution**: memory acts on controlled drift and diffusion alike.

### 2. Completely monotone kernels, sums of exponentials, and fractional kernels are all inside the class (p. 8)

Example 2.2: (i) $\mu=\sum_i c_i^n\delta_{\theta_i^n}$ gives $K(t)=\sum_ic_i^ne^{-\theta_i^nt}$, smooth;
(ii) fractional and Gamma kernels; (iii) sums and products of admissible kernels; (iv) every
completely monotone kernel by Bernstein's theorem (p. 8). Signed measures allow non-monotone
kernels of this Laplace form.

### 3. ⭐⭐ The Volterra state is exactly a linear functional of an $L^1(\mu)$-valued Markov lift (Thm 2.3, pp. 9–10)

$X_t=g_0(t)+\int\mu(d\theta)Y_t(\theta)$ (eq. 2.12) with
$Y_t(\theta)=\int_0^te^{-\theta(t-s)}b\,ds+\int_0^te^{-\theta(t-s)}\sigma\,dW_s$ (eq. 2.13), i.e. each
factor solves $dY_t(\theta)=[-\theta Y_t(\theta)+\tilde b(\cdot)]dt+\tilde\sigma(\cdot)dW_t$ (eq. 2.11).
Proof by stochastic Fubini (p. 10). The converse also holds. Original problem and lifted problem
therefore coincide; the lift is not an approximation.

### 4. The lift must live in $L^1(\mu)$, a non-reflexive Banach space, not in a Hilbert space (pp. 11, 13)

«One might be tempted to look for solutions in the Hilbert space $L^2(\mu)$, but since $\mu$ is not
always a finite measure ... $L^2(\mu)$ is not necessarily included in $L^1(\mu)$» (Remark 2.4, p. 11).
Hence existing Hilbert-space LQ/Riccati theory «cannot be directly applied» (p. 13).

### 5. ⭐ Formally, the value is quadratic in the lifted state and the control is linear feedback, via an operator Riccati equation (pp. 11–13)

In $L^1(\mu)$ the dynamics read $dY_t=(A^{mr}Y_t+BY_t+C\alpha_t)dt+(DY_t+F\alpha_t)dW_t$ with
$(A^{mr}\varphi)(\theta)=-\theta\varphi(\theta)$ (eq. 2.18); the formal candidate is
$V_t=\langle Y_t,\Gamma_tY_t\rangle_\mu$ with an operator Riccati equation, and, when $\Gamma$ is an
integral operator, a **kernel** Riccati equation for $\Gamma_t(\theta,\tau)$ in which the free term
$(\theta+\tau)\Gamma_t(\theta,\tau)$ comes from the mean reversion of the two factors (p. 12).

### 6. ⭐⭐ The Riccati system has three equations (quadratic kernel, linear kernel, constant) in mild form (eqs. 3.1–3.9, pp. 13–15)

Value candidate (3.1): $V^\alpha_t=\int Y_t(\theta)^\top\mu(d\theta)^\top\Gamma_t(\theta,\tau)\mu(d\tau)Y_t(\tau)+2\int\Lambda_t(\theta)^\top\mu(d\theta)Y_t(\theta)+\chi_t$,
with (3.2): $\dot\Gamma_t(\theta,\tau)=(\theta+\tau)\Gamma_t(\theta,\tau)-\mathcal R_1(\Gamma_t)(\theta,\tau)$,
$\dot\Lambda_t(\theta)=\theta\Lambda_t(\theta)-\mathcal R_2(t,\Gamma_t,\Lambda_t)(\theta)$,
$\dot\chi_t=-\mathcal R_3(t,\Gamma_t,\Lambda_t)$, all zero at $T$ (p. 13). Solutions are understood
in the mild/variation-of-constants sense (3.7)–(3.9), e.g.
$\Gamma_t(\theta,\tau)=\int_t^Te^{-(\theta+\tau)(s-t)}\mathcal R_1(\Gamma_s)(\theta,\tau)ds$ (p. 15).
The $\Gamma$-equation is decoupled; $\Lambda$ is a linear (Lyapunov) equation given $\Gamma$; $\chi$ is
a quadrature (Section 6, p. 32).

### 7. Existence and uniqueness of the Riccati solution under $Q\ge0$, $N\ge\lambda I$ (Thm 3.4, p. 15)

Under (2.3) and $Q\in S^d_+$, $N-\lambda I_m\in S^m_+$ for some $\lambda>0$ (eq. 3.10), there is a unique
triplet $(\Gamma,\Lambda,\chi)\in C([0,T],L^1(\mu\otimes\mu))\times C([0,T],L^1(\mu))\times C([0,T],\mathbb R)$
with $\Gamma_t$ symmetric nonnegative and the bound $\int|\mu|(d\tau)|\Gamma_t(\theta,\tau)|\le M$
(eq. 3.11). The $\Gamma$-part is imported from the companion paper
[[abijaber-2021-integral-operator-riccati]] (Thm 2.3 there = Thm 2.4 in the arXiv version read).

### 8. ⭐⭐ Main solvability theorem: linear optimal feedback in the lifted state, quadratic value (Thm 3.7, p. 16)

There exists an admissible optimal control
$\alpha^*_t=-\hat N(\Gamma_t)^{-1}\big(h(t,\Gamma_t,\Lambda_t)+\int S(\Gamma_t)(\theta)\mu(d\theta)Y^{\alpha^*}_t(\theta)\big)$ (eq. 3.12),
and $V^{\alpha}_t$ of (3.1) is the optimal value process (eq. 3.13). Proof by a «refined martingale
verification argument combined with a squares completion technique» (abstract, p. 1; Thm 5.2,
pp. 28–31): $J_t(\alpha)-V_t=\mathbb E[\int_t^T(\alpha_s-\mathcal T_s(\alpha))^\top\hat N(\alpha_s-\mathcal T_s(\alpha))ds\mid\mathcal F_t]\ge0$ (eq. 5.11).
Admissibility requires $\sup_t\mathbb E|\alpha_t|^4<\infty$ because the solution of a singular-kernel
Volterra SDE need not satisfy $\mathbb E[\sup|X_t|^2]<\infty$ (Remark 2.1, p. 7).

### 9. ⭐ The value is LQ in the lifted state but not in the original state after time 0 (Remark 3.8, p. 16)

For constant $g_0\equiv X_0$, $V_0$ is LQ in $X_0$; «However, because of the possible
non-Markovianity of the problem, for t > 0, the optimal value $V_t$ is not necessarily
linear–quadratic in $X_t$ as in the standard case» (p. 16). The Markovian state is the whole curve
$Y_t(\cdot)$.

### 10. ⭐ Worked example: the optimal control = standard feedback in $X$ + a memory correction (Example 3.9, p. 17)

For $X_t=\int_0^t\alpha_sds+\int_0^t\tilde K(t-s)dW_s$ (LQ regulator with Volterra noise),
$\alpha^*_t=-\frac1N\big(\Gamma_t(0,0)X_t+\int(\Gamma_t(\theta,0)-\Gamma_t(0,0))Y^2_t(\theta)\tilde\mu(d\theta)\big)$:
«the sum of a feedback form in X, and a second term capturing the non Markovianity of X» (p. 17).
$\Gamma(0,0)$ solves the standard scalar Riccati equation; with $\tilde K\equiv1$ the memory term
disappears (p. 17).

### 11. Conventional LQ is nested: $\mu=\delta_0$ recovers matrix Riccati; a sum of $n$ exponentials gives an $n\times n$ matrix Riccati (Remark 3.10, Example 3.11, pp. 18–19)

With $\mu(d\theta)=\sum_ic^n_i\delta_{\theta^n_i}$, $X^n_t=g^n_0(t)+\sum_ic^n_iY^{n,i}_t$ (eq. 3.16) and
the factors (3.17) form a finite-dimensional linear SDE: «the problem reduces to a conventional
linear-quadratic control for the finite-dimensional controlled system» (p. 18), with the standard
$n\times n$ matrix Riccati equation (3.18) and $B^n_{ij}=Bc^n_j-\theta^n_i\delta_{ij}$ etc. (p. 19).

### 12. ⭐⭐ Stability: the optimal value is Lipschitz in the kernel's $L^2(0,T)$ distance (Thm 3.13, pp. 19–20)

For kernels $K^n$ of the form (3.19) with measures satisfying (2.3)–(2.4), under (3.10) **and $Q$
invertible**, if $\|K^n-K\|_{L^2(0,T)}\to0$ and $\|g^n_0-g_0\|_{L^2(0,T)}\to0$ then $V^{n*}_0\to V^*_0$ «with a
rate of convergence given by»
$$|V^*_0-V^{n*}_0|\le c\big(\|g^n_0-g_0\|_{L^2(0,T)}+\|K^n-K\|_{L^2(0,T)}\big)\quad(3.24)$$
«for some positive constant c independent of n» (p. 20). The rate is **in the kernel error, not in
$n$**; $c$ is not explicit (it depends on $T$, the coefficients, the resolvents of $c|K^n|^2$, and a
uniform $L^2$ bound on optimal controls, Lemmas 7.1–7.4). The statement concerns the value at
time 0 only; no convergence of the optimal controls or of $\Gamma^n\to\Gamma$ is stated.

### 13. ⭐ Constructive discretisation of $\mu$: moment-matched atoms; for the fractional kernel a geometric partition (eq. 3.25, pp. 20–21)

$c^n_i=\int_{\eta_{i-1}^n}^{\eta_i^n}\mu(dx)$, $\theta^n_i=\frac1{c^n_i}\int_{\eta_{i-1}^n}^{\eta_i^n}\theta\mu(d\theta)$
(eq. 3.25). For $K_H$ with $\eta^n_i=r_n^{i-n/2}$, explicit $c^n_i,x^n_i$ are given, and
$\|K^n-K_H\|_{L^2}\to0$ if $r_n\downarrow1$, $n\ln r_n\to\infty$ (p. 20; citing Abi Jaber 2019, Lemma A.3).
«In practice ... if n = 20, setting $r_{20}$ = 2.5 yields very good approximations for the
un-controlled stochastic Volterra equation» (p. 21). No explicit rate in $n$ is derived here; it
must be imported from the multifactor-approximation literature (`[3]` = Abi Jaber & El Euch 2019).

### 14. Proof machinery: a priori $L^2$ bounds via the resolvent of $c|K|^2$ and a convolution Gronwall (Lemmas 7.1–7.2, pp. 34–37)

$\mathbb E\|X^n-X\|^2_{L^2}\le c\,m_n(1+\|R^n\|_{L^1})$ with $m_n=\|g^n_0-g_0\|^2+\|K^n-K\|^2_{L^2}(\mathbb E\|X\|^2_{L^2}+\mathbb E\|\alpha\|^2_{L^2})$ (eq. 7.2);
$R^n\to R$ in $L^1$ by continuity of the resolvent in the kernel (p. 37). Lemma 7.3 bounds
$|J(\alpha)-J^n(\alpha)|^2$ uniformly over controls with bounded $L^2$ norm (p. 37); Lemma 7.4 needs
$Q$ invertible to bound optimal controls uniformly in $n$ (p. 38).

### 15. Infinite-dimensional SDE existence by contraction in $L^1(\mu)$ (Thm 4.1, pp. 21–24)

Mild solutions of $dY=A^{mr}Y+b(s,Y)ds+\sigma(s,Y)dW$ in $L^1(\mu)$ exist uniquely under Lipschitz/linear
growth; continuity in $L^1(\mu)$ uses condition (2.4) and Kolmogorov–Chentsov (Lemma 4.3, p. 25).
Driving noise is an $n$-dimensional **Brownian** motion throughout.

### 16. Singular kernels make the Riccati solution singular too (Remark 5.3, p. 31)

A linear-quadratic terminal cost can be added by changing terminal conditions (p. 31). «If K has no
singularities at 0, then one can still construct continuous solutions to (3.2). However, in the
presence of a singularity, the solution $t\mapsto\Gamma_t$ inherits the singularity of the kernel and
is no longer continuous but only lies in $L^1([0,T],L^1(\mu\otimes\mu))$» (p. 31). (This sits awkwardly
with Thm 3.4, which asserts $\Gamma\in C([0,T],L^1(\mu\otimes\mu))$; see "Contested" below.)

## What this source does not address

- **Jumps, point processes, Hawkes intensities.** The noise is Brownian only (p. 5; Remark 3.12
  allows multi-dimensional Brownian motion). No jump term, no counting process, no
  state-dependent intensity appears anywhere.
- **Non-LQ objectives.** No exponential (CARA) utility, no nonlinear Hamiltonian, no control that
  enters through a nonlinear response function (fill probability).
- **Bilinear state–control or state–state coupling.** Dynamics are affine in $(X,\alpha)$; the
  structure that a Hawkes intensity multiplies an inventory jump is outside the class.
- **Rates in the number of factors** $n$ and explicit constants; convergence of optimal controls.
- **Market making** in any form; finance appears only as motivation (transient impact, hedging,
  p. 5).

## Model card

assets · n/a — generic $d$-dimensional controlled state, no assets · kernel · Laplace transform of a
signed matrix measure (completely monotone, sums of exponentials, fractional/Gamma; singular at 0
allowed) · excitation · n/a — Brownian-driven Volterra memory, no point process · who excites the
flow · n/a — no flow; the control itself is convolved with the kernel (it shapes the state's
memory) · objective · quadratic cost $\mathbb E\int(X^\top QX+\alpha^\top N\alpha+2L^\top X)dt$ (eq. 2.6–2.7)
· solution method · closed form up to an integral-operator Riccati equation in $L^1(\mu\otimes\mu)$;
numerically via $n$-factor discretisation → $n\times n$ matrix Riccati · benchmark · n/a — no
numerics reported · reported numbers · none (only the qualitative remark $n=20$, $r_{20}=2.5$, p. 21).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

Read for this project as: what its control machinery says about Riccati closure on a lifted
Volterra state, and what rigorous approximation theory it offers for the lift-truncation step (E0).

**Carries Kernthesen 1, 3, 5, 6, 8, 9, 10, 11, 12, 13, 16.**

### What this focus needs beyond the Kernthesen

1. **Closure holds because the problem is LQ in the lifted state.** The lift (Thm 2.3) turns the
   Volterra state into a linear SDE in $L^1(\mu)$; the cost is quadratic; hence the value is
   quadratic in $Y$ with deterministic coefficients $(\Gamma,\Lambda,\chi)$ that do **not** depend on the
   state. This is the structural reason the Riccati closes exactly here and the reason it does not
   in Hawkes market making: there the intensity (a lifted state) *multiplies* the jump term
   $\lambda\,[\theta(q\pm1)-\theta(q)+H(\cdot)]$, a bilinear coupling, so a quadratic-in-$q$ ansatz has
   coefficients that depend on the lifted memory (Barzykin's "transport-jump" objection, recorded on
   [[barzykin-2026-hawkes-driven-otc]] Kernthese 10). *Inference, not the authors'.*
2. **E0 (lift truncation): what is proven and what is not.**
   (a) Proven: $|V^*_0-V^{n*}_0|\le c(\|g^n_0-g_0\|_{L^2}+\|K^n-K\|_{L^2})$, linear in the kernel's
   $L^2(0,T)$ error (eq. 3.24, p. 20) — for **Brownian LQ** only, value at $t=0$ only, $c$ not explicit,
   $Q$ invertible required. (b) Not proven: a rate in $n$, convergence of controls, any statement
   with jumps. (c) The analogy to Hawkes: the Hawkes intensity is a Volterra equation driven by
   $dN$ instead of $dW$, and the same Laplace-measure lift applies (see [[markov-lift]]); but the
   stability proof (Lemmas 7.1–7.2) uses Itô isometry for $dW$ and LQ cost structure, so it does not
   transfer verbatim. For a controlled-Hawkes value-convergence result with jumps see
   [[khabou-2025-markov-approximation-hawkes]] (no rate for polynomial costs); for a regret rate
   $p^{-1/2}$ see [[acero-2026-hawkes-structured-networks]].
3. **Multi-dimensionality is native.** $X\in\mathbb R^d$, $K\in\mathbb R^{d\times d'}$, $\mu$ a matrix
   measure (pp. 5–6): cross-component memory (the LQ analogue of cross-asset kernels) is covered by
   the solvability theorem. Only the explicit discretisation (3.25) is written for $d=d'=m=1$ («for
   higher dimension matrices need to be replaced by tensors», p. 20).
4. **The "Volterra–Riccati" name.** Here it denotes an *exact* integral-operator Riccati equation
   for the value kernel; in [[volterra-riccati]] (Barzykin) it denotes a certainty-equivalent ODE
   driven by a forecast. The papers share the idea that memory enters via a kernel in the Riccati
   coefficients (e.g. the $(\theta+\tau)\Gamma$ term), not the approximation logic.
5. **Who excites / control feeds memory.** The control is convolved with $K$ (eq. 2.1): today's
   action shapes the future state's memory — the LQ counterpart of fill-driven excitation in the
   sense of [[who-excites-the-flow]]. That this case still closes is because the coupling is linear.
   *Inference.*

### Direct quotes

> "Using a refined martingale verification argument combined with a squares completion technique, we prove that the value function is of linear quadratic form in these state variables with a linear optimal feedback control, depending on non-standard Banach space valued Riccati equations." (abstract, p. 1)

> "Furthermore, we show that the value function of the stochastic Volterra optimization problem can be approximated by that of conventional finite dimensional Markovian Linear–Quadratic problems, which is of crucial importance for numerical implementation." (abstract, p. 1)

> "then, $V_0^{n*}\to V_0^*$, as $n\to\infty$, with a rate of convergence given by $|V_0^*-V_0^{n*}|\le c(\|g_0^n-g_0\|_{L^2(0,T)}+\|K^n-K\|_{L^2(0,T)})$, for some positive constant c independent of n." (Thm 3.13, p. 20)

> "However, because of the possible non-Markovianity of the problem, for t > 0, the optimal value $V_t$ is not necessarily linear–quadratic in $X_t$ as in the standard case." (Remark 3.8, p. 16)

### Examples & illustrations

- Example 3.9 (p. 17): LQ regulator with Volterra noise — optimal control = standard Riccati
  feedback $-\Gamma_t(0,0)X_t/N$ plus a memory term $\int(\Gamma_t(\theta,0)-\Gamma_t(0,0))Y^2_t(\theta)\tilde\mu(d\theta)$;
  a clean template for "Poisson-like feedback + Hawkes-memory correction" in quote rules.
- Example 3.11 (pp. 18–19): sum-of-exponentials kernel → $n\times n$ matrix Riccati (3.18) with
  $B^n_{ij}=Bc^n_j-\theta^n_i\delta_{ij}$ — the lift's mean-reversion speeds sit on the diagonal.
- Fractional kernel, geometric partition, $n=20$, $r_{20}=2.5$ (pp. 20–21).

### Boundary of this focus

The source is Brownian LQ. Everything said here about Hawkes flow, jumps, inventory-jump closures
and market making is the project's inference from structural analogy. The approximation theorem
is a *value* bound in the *kernel* norm; it gives no rate in the number of factors.

## Mentioned entities

- Concepts: [[markov-lift]], [[matrix-riccati-equation]], [[volterra-riccati]], [[who-excites-the-flow]]
- Companion: [[abijaber-2021-integral-operator-riccati]]
- Comparison pages (not cited by the source): [[khabou-2025-markov-approximation-hawkes]], [[acero-2026-hawkes-structured-networks]], [[barzykin-2026-hawkes-driven-otc]]
- Other works (not in this wiki): Abi Jaber 2019 (Lifting the Heston model), Abi Jaber & El Euch 2019 (Markovian structure of Volterra Heston; Multifactor approximation of rough volatility), Abi Jaber–Larsson–Pulido 2019 (Affine Volterra), Alfonsi & Schied 2013, Bank–Soner–Voß 2017, Carmona & Coutin 1998, Cuchiero & Teichmann 2018, Duncan & Pasik-Duncan 2013, Gripenberg–Londen–Staffans 1990, Han & Wong 2019, Kleptsyna et al. 2003, Wang 2018, Yong 2006, Yong & Zhou 1999.

## Connections

- Builds on: [[abijaber-2021-integral-operator-riccati]] (existence/uniqueness of $\Gamma$, p. 15).
- Supports: [[markov-lift]] (rigorous Laplace-measure lift; Brownian case); [[matrix-riccati-equation]] (finite-factor reduction).
- Compare: [[khabou-2025-markov-approximation-hawkes]] (jump/Hawkes analogue of the stability theorem); [[acero-2026-hawkes-structured-networks]] (E0 rate $p^{-1/2}$ in regret); [[barzykin-2026-hawkes-driven-otc]] (cites the LQ-Volterra precedent via Abi Jaber & Neuman 2025, not this paper).
- Name clash: [[volterra-riccati]].
