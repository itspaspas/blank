---
title: "Khabou & Talbi 2025 — Markov approximation for controlled Hawkes jump-diffusions with general kernels"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: khabou-2025-markov-approximation-hawkes
depth: standard
tags: [hawkes, markov-lift, sum-of-exponentials, stochastic-control, value-convergence, non-monotone-kernel, portfolio-choice, nonlinear-hawkes]
relations:
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "Proves that sums of exponentials lift general L1 kernels, incl. non-monotone ones: «Under minimal integrability conditions, the kernel can be approximated by a linear combination of exponential functions» (abstract, p. 1); Thm 3.1 (p. 7), value convergence Thm 4.1 (p. 11)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Nonlinear, multivariate, marked Hawkes jump-diffusion (1.2) with signed matrix kernel: «We call such phenomenon cross-excitation (respectively cross-inhibition)» (p. 4)."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Stability Assumption 1.2 (p. 4) requires L·E[b(Y)]·sp(‖ϕ‖₁) < 1, the spectral radius of the matrix of kernel L1 masses — the source's version of ρ(K) < 1."
  - target: jusselin-2021-persistent-order-flow
    type: cites
    confidence: extracted
    because: "Jusselin [38] cited among lifting approaches (p. 2) and for exponential approximation of completely monotone kernels via Bernstein's theorem (p. 3)."
  - target: bergault-2024-price-aware-automated
    type: cites
    confidence: extracted
    because: "Reference [14] cited as an exponential-kernel controlled Hawkes application «in market making» (p. 2); the in-text author list wrongly starts with Bensoussan."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Control enters the intensity only through the weight ν(s, X_{s−}, α_{s−}) attached to each past event in (4.1) (p. 10) — the control at event time scales that event's future excitation; no current-control modulation of the jump rate."
---

# Markov approximation for controlled Hawkes jump-diffusions with general kernels

## Bibliographic Details

Khabou, Mahmoud and Mehdi Talbi. 2025. *Markov approximation for controlled Hawkes
Jump-Diffusions with general kernels*. arXiv:2507.11294v1 [math.PR], 15 July 2025 (title page dated
16 July 2025). 30 pp. Affiliations: Imperial College London (NeST); LPSM, Université Paris-Cité.
MSC 60G55, 93E20, 45D05, 60H10.

**Read: arXiv 2507.11294v1 (preprint); page/equation numbers follow it.** No published version is
recorded in the library entry. Not a core (B1) work, so the preprint is accepted under the preprint
policy.

### Notation map (source → project)

| Source | Meaning | Project symbol / remark |
|---|---|---|
| $X_t$ | controlled state (jump-diffusion) | ⚠ not cash; in §4.3 it is wealth |
| $\lambda_\infty(t,x)$ | baseline intensity, state-dependent | $\mu$ (baseline) |
| $\mu,\sigma,\gamma$ | drift, volatility, jump size of $X$ | ⚠ $\mu$ is drift, $\gamma$ jump size (not baseline / risk aversion) |
| $\phi$ (matrix $\phi_{ij}$) | kernel, possibly signed | kernel; $\|\phi\|_1$ masses ↔ $K$ |
| $\psi$ | non-decreasing, Lipschitz jump-rate (link) function | no project symbol; ⚠ re-used in §4.3 for a Hamiltonian-type term |
| $\nu(s,x,a)$ | weight of a past event in the intensity; control-dependent in (4.1) | no project symbol |
| $b(y)$, $m(dy)$ | mark effect, mark law | — |
| $\eta_k,\beta_k$; $\xi^k_t$ | weights/decays of the exponential sum (3.1); lift variables (3.2) | $\beta$, $D=\mathrm{diag}(\beta)$; lift state |
| $n$ | number of exponentials | lift size ("$p$" in Acero) |
| $\alpha$, $A$ | control, action space | quotes $\delta$ in MM |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1.1 Introduction (Hawkes jump-diffusions, why Volterra control is hard, lifting literature) | 1–3 |
| ✓ F1 | 1.2 Preliminary results: setting (1.2), Assumptions 1.1–1.3, Prop. 1.4 (existence, moments) | 3–5 |
| ✓ F1 | 2.1 Continuity w.r.t. the kernel, state-independent intensity (Prop. 2.1, Thm 2.2) | 5 |
| ✓ F1 | 2.2 Continuity, state-dependent intensity (Prop. 2.3, Thm 2.4) | 6 |
| ✓ F1 | 3 Markov approximation: sums of exponentials (3.1)–(3.4), Thm 3.1, fitting recipe, Remark 3.2, example (3.5), Figs. 1–2 | 6–10 |
| ✓ F1 | 4.1 The control problem (4.1)–(4.3) | 10–11 |
| ✓ F1 | 4.2 The Markov approximation: lifted HJB, Thm 4.1 | 11 |
| ✓ F1 | 4.3 Example: portfolio optimisation with contagion (Aït-Sahalia–Hurd), log utility (4.5)–(4.14) | 11–14 |
| ✓ F1 | 4.4 Numerical approach (discretise + DP + HybridNow) | 14–15 |
| (✓) | 5 Proofs: 5.1 Prop. 1.4, 5.2 Thm 2.2, 5.3 Thm 2.4, 5.4 Thm 4.1 | 15–22 |
| (✓) | A Technical lemmata (A.1 Volterra-resolvent inequality, A.2, A.3) | 22–24 |
| — | B Proofs of Prop. 2.1, 2.3; References | 24–30 |

(✓) = skimmed for structure and for what the constants depend on; not checked line by line.

## Kernthesen

### 1. The object: a multivariate, marked, *nonlinear* Hawkes jump-diffusion with signed matrix kernel (pp. 3–4)

Eq. (1.2): $X$ is a jump-diffusion whose $i$-th component jumps by $y\gamma_i(s,X_{s-})$ when the
Poisson-embedded point is accepted; the intensity is
$\lambda^i_t=\lambda^i_\infty(t,X_{t-})+\psi\big(\int_0^{t-}\sum_j\phi_{ij}(t-s)b(y)\nu(s,X_{s-})\mathbf 1_{\theta\le\lambda^j_s}\Pi^j(ds,d\theta,dy)\big)$.
$\phi_{ij}$ «encodes the effect of the jumps of node j on node i … We call such phenomenon
cross-excitation (respectively cross-inhibition)» (p. 4). The state $X$ feeds back into the
intensity through $\lambda_\infty$ and $\nu$. However, «Even though the SDE (1.2) is multivariate,
in the remainder of this paper all the results are written in the univariate case to reduce
clutter» (p. 4).

### 2. Stability is a spectral-radius condition on kernel masses, scaled by the link's Lipschitz constant (p. 4)

Assumption 1.2: $\psi$ positive, $L$-Lipschitz; $\phi\in L^1([0,T])$; $\nu$ bounded by 1;
$L\,\mathbb E[b(Y)]\,\mathrm{sp}(\|\phi\|_1)<1$ with $\|\phi\|_p$ the matrix of $L^p$ norms of
$\phi_{ij}$. Assumption 1.1 adds Lipschitz coefficients and a baseline whose Lipschitz constant in
$x$ is **strictly less than one**; Assumption 1.3 asks either a bounded $\psi$ or $\gamma,\nu$
independent of $x$. Prop. 1.4: unique solution with $\mathbb E\sup|X_t|<\infty$ (p. 4–5).

### 3. Why the problem is hard: path dependence, and the intensity is not a semimartingale (p. 2)

«due to the presence of the kernel φ in the dynamics (1.1), this problem is in general
path-dependent, and therefore cannot be analyzed through the standard dynamic programming approach
for Markov processes. Additionally, the intensity of the Hawkes process is not even a
semimartingale» (p. 2), so path-dependent PDE theory (Ekren–Keller–Touzi–Zhang) does not apply
either. Alternatives surveyed: maximum principle, relaxed controls, infinite-dimensional lifts
(Abi Jaber–Miller–Pham, Jusselin, Viens–Zhang, Possamaï–Talbi) (p. 2).

### 4. ⭐ Continuity in the kernel: intensities differ by a $T$-independent constant, states by $e^{CT}$ (pp. 5–6)

State-independent intensity: Prop. 2.1 gives $\mathbb E|\tilde\lambda_t-\lambda_t|\le C\|\tilde\phi-\phi\|_1$
and an $L^2$ analogue with $C$ independent of $T$; Thm 2.2 gives
$\mathbb E\sup|\tilde X_t-X_t|^2\le C(\|\tilde\phi-\phi\|_1+\|\tilde\phi-\phi\|_2^2)e^{CT^2}$ (p. 5).
State-dependent intensity: Prop. 2.3 and **Thm 2.4**,
$\mathbb E\sup_{s\le T}|\tilde X_s-X_s|\le C_1\|\tilde\phi-\phi\|_1e^{C_2T}$ (p. 6). The stability
assumption is what keeps the intensity error $T$-uniform; without it Grönwall would give
$O(e^{CT})$ for the intensity and $O(\exp(Ce^{CT^2}))$ for the state (p. 5).

### 5. Sums of exponentials give an exact finite-dimensional Markov lift (pp. 6–7)

For $\phi(t)=\sum_{k=1}^n\eta_ke^{-\beta_kt}$ (3.1) the intensity is
$\lambda_t=\lambda_\infty(t,X_{t-})+\psi(\sum_k\eta_k\xi^k_t)$ with
$d\xi^j_t+\beta_j\xi^j_tdt=\int b(y)\nu(t,X_{t-})\mathbf 1\,\Pi(dt,d\theta,dy)$, so
$(X,\xi^1,\dots,\xi^n)$ is Markov with generator (3.4) (pp. 6–7). Every factor jumps by the
same amount $b(y)\nu$ at an event. Note the weights $\eta_k$ are **real** (signed), not positive.

### 6. ⭐⭐ Main approximation theorem: Markov jump-diffusions are universal approximators of Hawkes jump-diffusions (p. 7)

Thm 3.1: under Assumptions 1.1–1.3, «For any ε > 0, there exists an n ∈ ℕ and a n + 1-dimensional
Markov process $(\tilde X,\tilde\xi^1,\dots,\tilde\xi^n)$ that follows the dynamics (3.3) such that
$\mathbb E\sup_{s\in[0,T]}|X_s-\tilde X_s|\le\varepsilon$» (p. 7). Proof = Thm 2.4 + density of
$\{e^{-k\beta t}\}_{k\ge1}$ in $L^p(\mathbb R_+)$ (Kammler; Müntz–Szász type results). **No rate in
$n$** is given: the error is controlled by $\|\phi_n-\phi\|_1$, and how fast that falls with $n$
depends on the kernel and is not analysed.

### 7. ⭐ Non-monotone (signed) kernels are covered — the point of departure from Bernstein-based lifts (pp. 3, 7)

«completely monotone kernels are subject to such approximations» via Bernstein's theorem
(Coutin–Carmona, Alfonsi–Kebaier, Jusselin, Bayer–Breneis), but «In the present paper, we use the
fact that the exponential approximation holds for a larger class of non-exponential kernels, under
mere integrability conditions» (p. 3). Two facts carry the result: sums of exponentials are dense
in integrable functions, «and not only of completely monotonous ones», and Hawkes jump-diffusions
are continuous in their kernel (p. 7).

### 8. Practical fitting: fix the decay scale, solve a modified-Hilbert linear system, increase $n$ (p. 8)

Fix $\beta$ (a memory time scale), take exponents $k\beta$, choose $n$; minimise the $L^1$ error
$J(\eta)$ numerically, or the $L^2$ error $I(\eta)$ in closed form by solving $M_H\eta=v$ with
$M_H=(1/(\beta(i+j)))$ a modified Hilbert matrix and $J\le I^{1/2}$ (p. 8, on a finite window).
Exponentials are not orthogonal, so coefficients change when $n$ grows; $\beta$ is not optimised
«because of the lack of convexity» (p. 8). Simulation cost of the lifted SDE is $O(nT)$ against
$O(T^2)$ for the original (p. 8). Remark 3.2: $\{x^ke^{-\beta x}\}$ (Erlang-type) bases are also
dense and Markov via $f_k'=kf_{k-1}-\beta f_k$; Beylkin–Monzón would also optimise the decays (pp.
8–9).

### 9. Worked example: a non-monotone, excite-then-inhibit kernel needs only three exponentials on a finite horizon (pp. 9–10)

Hawkes–OU SDE (3.5) with $\phi(t)=(1-t)/(1+t^{2.5})$, «not monotonous (a fortiori not completely
monotonous)», excitation then inhibition; $\beta=0.5$; fits
$\phi^{(2)}=-1.16e^{-0.5t}+2.17e^{-t}$ and $\phi^{(3)}=-0.82e^{-0.5t}+0.58e^{-t}+1.39e^{1.5t}$ (p. 9;
the last exponent is printed positive, evidently a typo for $e^{-1.5t}$). «Both approximations fail
at capturing the heavy polynomial tail, but this is not a problem given that we are interested in
approximation on finite horizons» (Fig. 1, p. 9). With common randomness, $X^{(3)}$ «remains
confounded with the original process X» because it accepts and rejects the same Poisson points;
$X^{(2)}$ does not (Fig. 2, p. 10). This is an illustration on one path, not an error study.

### 10. ⭐⭐ The control can enter drift, volatility, jump size and the *event weight* $\nu$ — so the control feeds future intensity (p. 10)

Controlled dynamics (4.1): $\mu,\sigma,\gamma,\nu$ all take $(s,X_s,\alpha_s)$; the intensity is
$\lambda_t=\lambda_\infty(t,X_{t-})+\psi\big(\int_0^{t-}\phi(t-s)b(y)\nu(s,X_{s-},\alpha_{s-})\mathbf 1_{\theta\le\lambda_s}\Pi(ds,d\theta,dy)\big)$.
The control therefore acts on the intensity (i) through the weight $\nu(\cdot,\alpha_{s-})$ chosen
**at the time of each past event**, scaling that event's future excitation, and (ii) indirectly
through the controlled state $X$ in $\lambda_\infty$ and $\nu$. It does **not** enter
$\lambda_\infty$ directly, so the current control cannot thin the current jump rate. Admissible
controls must keep Assumptions 1.1–1.3 and give moments uniform in $\alpha$ (4.2).

### 11. ⭐⭐ Value convergence, with a Lipschitz-case bound linear in the kernel $L^1$ error (p. 11)

The lifted problem $V^n_0$ (4.4) has a standard HJB in $(t,x,\xi)$ whose nonlocal term shifts all
$\xi^k$ by $\nu(t,x,a)b(y)$ (p. 11). **Thm 4.1**: if $f,g$ are continuous with polynomial growth of
order $m\ge1$ uniformly in $(t,a)$, then $V^n_0\to V_0$; «In particular, if f is
Lipschitz-continuous in x, uniformly in the other variables, and g is Lipschitz-continuous, we
have: $|V^n_0-V_0|\le\|\phi_n-\phi\|_1C_1e^{C_2T}$» (p. 11). The general case is proved by
truncation and a modulus of continuity (pp. 21–22): **no rate** for polynomial-growth costs.

### 12. Example: log-utility portfolio choice with contagion separates into wealth × memory, with the memory part given by Feynman–Kac (pp. 11–14)

Aït-Sahalia–Hurd: $dS/S=\mu dt+\sigma dW+\gamma dN$, $\lambda_t=\lambda_0+\int\phi(t-s)dN_s$ (4.5);
wealth (4.6) with proportion $\omega$ and consumption rate $c$; infinite-horizon discounted
utility (4.7). Lifted HJB (4.10) in $(x,\xi)\in\mathbb R^{n+1}$. For $U=\log$, the ansatz
$v=f(\xi)+K\log x$ with $K=1/\rho$ removes $x$; $f$ solves a **linear** equation
$-\rho f-\beta\xi\cdot\nabla f+(\lambda_0+\eta\cdot\xi)(f(\xi+1)-f(\xi))=\text{source}(\eta\cdot\xi)$,
the generator of $\xi$, hence a Feynman–Kac representation (p. 13). Result:
$V_0=\frac1\rho[\log X_0+1-\frac r\rho-\log\rho]-\int_0^\infty e^{-\rho t}\mathbb E\psi(\lambda_t-\lambda_0)dt$,
$c^*=\rho$, and $\omega^*_t$ a pointwise argmax depending on the current intensity $\lambda_t$
(p. 14). The infinite horizon needs an extra truncation argument, since Thm 4.1 is finite-horizon
(p. 14). Here the control does **not** affect the intensity (exogenous contagion).

### 13. Computation of the lifted HJB is left open: high dimension, suggested DP + neural networks (pp. 14–15)

«the possibly high dimension of the state process of the Markov problem represents a computational
challenge. We may then combine the dynamic programming approach with neural network
approximations, similarly to the "HybridNow" algorithm» (pp. 14–15). No numerical control
experiment is reported.

## Figures and tables

- Fig. 1 (p. 9): $\phi$ vs $\phi^{(2)},\phi^{(3)}$ on $[0,20]$; excitation then inhibition.
- Fig. 2 (p. 10): one path of $(X,\lambda)$ and its order-2 and order-3 approximations.

No figures extracted (write scope limited to this page).

## What this source does not address

- **Market making.** Cited only as an application area of exponential-kernel control
  (`bergault-2024-price-aware-automated`, p. 2); no quotes, inventory or fill-probability model.
- **Controlled thinning.** The current control cannot modulate the current jump rate (Kernthese
  10), which is exactly how quotes act in GLFT/BEGV ($\Lambda e^{-k\delta}$).
- **Rates in $n$** and constants: neither $\|\phi_n-\phi\|_1$ as a function of $n$, nor $C_1,C_2$, are
  quantified; no numerical value-error study.
- **Multivariate results.** The setting is multivariate but every theorem is written and proved
  univariately (p. 4); how the constants scale with dimension is not discussed.
- **Riccati / closed forms.** No LQ or quadratic structure; the only explicit solution is the
  log-utility separation.
- **Exponential (CARA) utility or quadratic costs with a rate.** Thm 4.1 gives a rate only for
  Lipschitz $f,g$.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 2, 4, 5, 6, 7, 10, 11, 12.** Read as a non-MM source: what its control
machinery says about the lift closure (step E0 of [[problem-anatomy]] §4).

### What this focus needs beyond the Kernthesen

1. **What E0 is, in this source's terms.** E0 = replacing $\phi$ by $\phi_n$ (sum of $n$
   exponentials on a fixed lattice $k\beta$). Thm 4.1 bounds the induced value error by
   $\|\phi_n-\phi\|_1C_1e^{C_2T}$ **only for Lipschitz running and terminal rewards**; for
   polynomial growth it gives convergence without a rate (p. 11). A market-making objective with a
   running penalty $\frac12\gamma\sigma^2q^2$ and a quadratic terminal penalty is not Lipschitz in
   $q$; CARA utility $-e^{-\gamma(X+qS)}$ is not of polynomial growth at all. *Inference:* for
   either MM objective this paper gives at most bare convergence of E0, and a constant that grows
   like $e^{C_2T}$. It complements the $p^{-1/2}$ regret rate of
   [[acero-2026-hawkes-structured-networks]] (completely monotone kernels) by covering
   **non-monotone, signed** kernels, but without a rate in $n$.
2. **Does the control affect the intensity?** Yes, but in a specific way: through the event
   weight $\nu(s,X_{s-},\alpha_{s-})$ fixed at each event time (Kernthese 10). In MM terms
   (*inference*): this fits "the maker's own trades excite future flow with a size the maker
   influences", not "the quote thins today's arrivals". GLFT-type fill intensities
   $\Lambda e^{-k\delta}$ are outside (4.1) as written. Compare
   [[bielecki-2026-continuous-time-reinforcement]], where the *current* action multiplies the
   kernel readout and enters the baseline.
3. **Lift + quadratic.** The lifted HJB (p. 11) has the nonlocal shift
   $\xi\mapsto\xi+\nu b(y)\mathbf 1$ (all factors jump together) and transport $-(\beta\xi)\cdot\nabla_\xi$.
   This is the structure [[barzykin-2026-hawkes-driven-otc]] p. 8 calls "transport-jump equations
   in the memory variables". The log-utility example shows the one case where it closes: the
   state variable separates ($v=f(\xi)+K\log x$) and the memory part becomes **linear** and
   solvable by Feynman–Kac (p. 13). *Inference for D2:* this is the log-utility analogue of the
   GLFT exponential transform — the separation removes the controlled variable, leaving
   $\lambda$-/$\xi$-dependent coefficients that solve a linear equation along the lift, not a
   Riccati system. It works because the control does not feed the intensity in that example.
4. **Multi-asset / cross-excitation.** The model allows a $d\times d$ signed kernel with
   cross-excitation and cross-inhibition (p. 4), and the stability condition is a spectral radius
   of kernel masses. A $d$-asset, $s$-side flow with $n$ exponentials per entry would need up to
   $n$ factors per *source* component (the lift jumps by component), i.e. $O(dsn)$ memory variables
   if each source has its own decays (*inference*; the paper writes only the univariate case).
5. **For the gap claim.** No closed form, no MM, no comparison with exact or RL solutions. The
   paper does not touch the gap; it supplies a convergence guarantee for E0 that a
   lifted-HJB "exact" benchmark for a non-exponential kernel would rely on.

### Direct quotes (for the draft)

> "In the present paper, we use the fact that the exponential approximation holds for a larger class of non-exponential kernels, under mere integrability conditions. This allows us to approximate path-dependent Hawkes jump-diffusion processes with multidimensional Markov jump diffusions, even when the kernel non-monotonous." (p. 3)

> "In particular, if f is Lipschitz-continuous in x, uniformly in the other variables, and g is Lipschitz-continuous, we have: $|V_0^n - V_0| \le \|\phi_n - \phi\|_1 C_1 e^{C_2 T}$ for some nonnegative constants $C_1, C_2$." (Thm 4.1, p. 11)

> "Both approximations fail at capturing the heavy polynomial tail, but this is not a problem given that we are interested in approximation on finite horizons." (Fig. 1 caption, p. 9)

> "the possibly high dimension of the state process of the Markov problem represents a computational challenge." (pp. 14–15)

### Examples & illustrations

- Non-monotone kernel $\phi(t)=(1-t)/(1+t^{2.5})$ fitted by 2 and 3 exponentials with negative
  weights (p. 9): a ready-made example that a signed exponential sum handles excite-then-inhibit
  flow, which Bernstein-based lifts cannot.
- Log-utility separation (p. 13): value = wealth term + Feynman–Kac functional of the memory.

### Boundary of this focus

Nothing here is market making. Every MM statement above is the project's inference from the
general framework. The rate statement holds only for Lipschitz rewards and is linear in the kernel
$L^1$ error, not in $n$.

## Mentioned entities

- Concepts: [[markov-lift]], [[hawkes-process]], [[branching-matrix]], [[who-excites-the-flow]]
- Sources in this wiki: [[jusselin-2021-persistent-order-flow]], [[bergault-2024-price-aware-automated]]
- Other works (bibkeys or not in library): `aitsahalia-2016-portfolio-choice-markets` (Aït-Sahalia & Hurd, portfolio choice with
  contagion), `bensoussan-2024-stochastic-control-diffusions`, Duarte–Löcherbach–Ost 2019, Kammler 1976,
  Abi Jaber–Miller–Pham, Viens–Zhang, Possamaï–Talbi, Hure–Pham–Bachouch–Langrené (HybridNow),
  Beylkin–Monzón.

## Connections

- Supports: [[markov-lift]] (general $L^1$ kernels, signed weights; value convergence).
- Extended by: [[bielecki-2026-continuous-time-reinforcement]], which calls this paper «the main
  recent breakthrough» (p. 2) and extends it to kernels that depend on the current action, uniformly
  in the control.
- Compare: [[acero-2026-hawkes-structured-networks]] (rate $p^{-1/2}$ for completely monotone kernels
  in an MM setting) and [[martin-2026-market-making-hawkes]] (Mercer-expansion lift, also beyond
  complete monotonicity).
- Feeds: [[problem-anatomy]] §4, step E0.
