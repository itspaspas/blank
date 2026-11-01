---
title: "Sakhanda & Ricalde-Guerrero 2026 — Stochastic Optimal Control of Hawkes Jump-Diffusion Systems"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: sakhanda-2026-hawkes-jump-diffusion
depth: standard
tags: [hawkes, stochastic-control, hjb, markov-lift, small-excitation, poisson-approximation, value-convergence, error-bound, jump-diffusion, growth-environment, single-intensity]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Disasters are «a marked Hawkes process» with intensity $\\lambda^H_t=\\mu(P^H_{t-})+Y_{t-}$ (eq. 2.4, p. 3), exponential excitation $dY=-bY\\,dt+\\int a(\\zeta)N(dt,d\\zeta)$ (2.3), subcritical $\\bar a_1<b$ (4.7, p. 6)."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "«a subcritical Markovian Hawkes specification, in which the state space is augmented by the self-excitation component of disaster risk» (abstract, p. 1); state $(K,P,Y)$ on $\\mathcal S_H=\\mathcal S_P\\times\\mathbb R_{\\ge0}$ (p. 4); Hawkes generator (5.86), p. 26."
  - target: intensity-forecast
    type: mentions
    confidence: extracted
    because: "Mean excitation solves the linear ODE $m'(t)=-(b-\\bar a)m(t)+\\bar a\\,\\mathbb E[\\mu(P_t)]$ (5.37, p. 15) — the scalar analogue of the deterministic forecast ODE; used only to show $\\mathbb E[Y_t]\\to0$, not inside the control problem."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Every disaster excites (2.3); the controls (consumption, abatement) act only on the baseline $\\mu(P)$ through pollution, never on the excitation (4.8)–(4.11), pp. 6–7. Neither market-making convention applies; closest to 'all events excite, control does not touch the jump'."
---

# Stochastic Optimal Control of Hawkes Jump-Diffusion Systems

## Bibliographic Details

Sakhanda, Daria, and Joshué Helí Ricalde-Guerrero. 2026. *Stochastic Optimal Control of Hawkes
Jump-Diffusion Systems*. arXiv:2608.29473v1 [math.OC], 30 August 2026. 30 pp. ETH Zürich,
Department of Mathematics. Sequel to the authors' Poisson paper (arXiv:2511.13568, ref. [12]).

**Read: arXiv 2608.29473v1; page/equation numbers follow it.** No published version known — the
preprint is its own original (non-core work; preprint policy).

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $K_t$ | aggregate capital stock | ⚠ **not** the branching matrix $K$ |
| $P_t$ | pollution stock (geometric diffusion, $\sigma P\,dW$) | ⚠ not a price |
| $Y_t$ | self-exciting part of the intensity | $\lambda_t-\mu$ (excitation component of a lifted exponential Hawkes intensity) |
| $\mu(P)$ | pollution-dependent baseline intensity | $\mu$, but state-dependent and control-influenced |
| $b$ | decay rate of excitation | $\beta$ (scalar) |
| $a(\zeta)$, $\bar a_1=\int a\,d\nu$ | jump of $Y$ per disaster of mark $\zeta$; mean jump | $K$ (scalar, marked); branching ratio $\bar a_1/b$ ↔ $\rho(K)$ |
| $\eta$, $a_\eta=\eta a$ | small-excitation parameter | ≈ Stage 2a's $\varepsilon$, but here it scales the **jump size with baseline fixed** (Hawkes → Poisson), not the baseline |
| $\omega(k,p,\zeta)\in(0,1]$ | fraction of capital surviving a disaster | — |
| $\alpha=(C,\theta)$ | control: consumption, abatement | ⚠ $\theta$ is **not** the reduced value function |
| $\rho$ | discount rate | — |
| $\varepsilon$, $\beta$, $\psi$, $x$ | utility/Poisson-value exponents and weights in $v=\frac{\psi^{-\varepsilon}}{1-\varepsilon}k^{1-\varepsilon}-\frac{x}{1+\beta}p^{1+\beta}$ | ⚠ $\varepsilon$ is not a small parameter; $\beta$ is not a decay |
| $V_H^\eta$, $V_P=v$ | Hawkes / Poisson value functions (maximised) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (contributions 1–3) | 1–2 |
| ✓ F1 | 2 Modelling framework: dynamics (2.1)–(2.3), intensities (2.4)–(2.5), scaling $a_\eta=\eta a$ | 2–3 |
| — | 3.1 Basic notation | 3–4 |
| ✓ | 3.2 Marked Hawkes processes (3.1)–(3.2); 3.3 subcriticality, branching ratio (Def. 3.1) | 4–5 |
| ✓ F1 | 4 Controlled model: admissible controls (Def. 4.1), Assumptions 4.2, Thm. 4.3 (main result, eq. 4.15) | 5–8 |
| ✓ | 5.1 Well-posedness: Prop. 5.1 (Poisson embedding, localisation, nonexplosion), Remark 5.2 | 8–14 |
| ✓ F1 | 5.2 Asymptotic Poisson approximation: Thm. 5.3 (mean-excitation ODE 5.37), Cors. 5.4–5.5, Prop. 5.6, Cor. 5.7 | 14–19 |
| ✓ F1 | 5.3 Small-excitation approximation: Prop. 5.8 (uniform weighted estimate), Lemma 5.9, Thm. 5.10 (verification bound 5.83) | 19–29 |
| — | References | 29–30 |

## Kernthesen

### 1. ⭐ Rare disasters with clustering are modelled as a marked Hawkes process with a state-dependent baseline (pp. 1–3)

The growth–environment model of [12] (capital $K$, pollution $P$, Poisson disasters) is extended
so that «past disasters [can] temporarily increase the likelihood of subsequent shocks»
(abstract, p. 1). Intensity $\lambda^H_t=\mu(P^H_{t-})+Y_{t-}$ (2.4) with
$dY_t=-bY_t\,dt+\int_{\mathcal Z}a(\zeta)N(dt,d\zeta)$ (2.3), p. 3. A disaster destroys the fraction
$1-\omega$ of capital (2.1). The Poisson benchmark has $\lambda^P_t=\mu(P^P_{t-})$ (2.5).

### 2. ⭐⭐ Markov lift: the exponential kernel augments the state by the excitation $Y$ (pp. 1, 4, 26)

«Our work focuses on a subcritical Markovian Hawkes specification, in which the state space is
augmented by the self-excitation component of disaster risk» (p. 1). State spaces
$\mathcal S_P=\mathbb R_{>0}^2$ and $\mathcal S_H=\mathcal S_P\times\mathbb R_{\ge0}$ (p. 4). The Hawkes
generator (5.86, p. 26) carries the transport term $-by\,\partial_y\varphi$ and the jump term
$(\mu(p)+y)\int[\varphi(\omega k,p,y+\eta a(\zeta))-\varphi(k,p,y)]\nu(d\zeta)$ — one scalar intensity
state, one event type.

### 3. Controls act on the baseline, not on the excitation (pp. 5–7)

Admissible controls $\alpha=(C,\theta)$ (consumption, abatement) are predictable with
$\mathbb E\int|\alpha|^2<\infty$ (Def. 4.1, p. 5). They enter the drifts $b^{\rm cap},b^{\rm pol}$
(4.8)–(4.9); the excitation kernel $a(\zeta)$ is deterministic and the baseline is $\mu(P^H_t)$
(4.11), p. 7. So the decision-maker influences disaster risk only through the pollution stock.

### 4. Subcriticality is the branching-ratio condition $\bar a_1<b$ (pp. 5–6)

Def. 3.1: branching ratio $m_h=\int_0^\infty\!\int h(s,\zeta)\nu(d\zeta)ds$, subcritical if $m_h<1$
(3.3)–(3.4), p. 5. For the exponential kernel this reads $\bar a_1:=\int a(\zeta)\nu(d\zeta)<b$
(Assumption 4.2(3), (4.7), p. 6).

### 5. Well-posedness and nonexplosion via Poisson embedding plus localisation (pp. 8–14)

Prop. 5.1: on every $[0,T]$ a pathwise unique strong solution exists and
$N((0,T]\times\mathcal Z)<\infty$ a.s. (p. 8). Proof: thinning
$N(dt,d\zeta)=\int\mathbf 1_{\{r\le\lambda_t\}}M(dt,d\zeta,dr)$ (5.4), truncation of the intensity at
$n$ (5.7), the integrated Lipschitz estimate for the thinning indicator (5.12), moment bounds
(5.15)–(5.23), exit-time argument (pp. 9–13). «The main difficulty relative to the Poisson model is
that the jump intensity is itself stochastic and depends on the endogenous excitation process $Y$»
(p. 8).

### 6. ⭐ The mean excitation solves a closed linear ODE and is integrable over time (pp. 14–16)

Thm. 5.3: with $\int_0^\infty\mathbb E[\mu(P_t)]dt<\infty$ (5.34),
$m(t)=\mathbb E[Y_t]$ satisfies $m'(t)=-(b-\bar a)m(t)+\bar a\,\mathbb E[\mu(P_t)]$, $m(0)=y$ (5.37),
hence $\mathbb E[Y_t]\to0$ and $\int_0^\infty\mathbb E[Y_t]dt=\frac{y+\bar a\int_0^\infty\mathbb E[\mu(P_t)]dt}{b-\bar a}$
(5.36), p. 15. This is the scalar Hawkes mean equation; the integrability of the *baseline*
(5.34) is a strong assumption (disaster risk must die out in mean) [I].

### 7. The excess intensity, and its effect on the compensator, vanish in $L^1$ — on windows and on the tail (pp. 16–19)

Cor. 5.5: $\mathbb E|\lambda_t-\mu(P_{t-})|=\mathbb E[Y_t]\to0$ (p. 16). Prop. 5.6: for bounded
continuous test functions the expected Hawkes integral differs from the Poisson-compensator integral
by at most $\int_T^{T+H}\mathbb E[Y_t]dt$ (5.40), p. 17; Cor. 5.7 extends this to $(T,\infty)$
(5.41), p. 18. This is an «asymptotic approximation in time» that «alone, however, does not yield a
uniform estimate for the difference between the corresponding infinite-horizon value functions»
(p. 19).

### 8. ⭐⭐ Small-excitation scaling: discounted excitation is $O(\eta)$ uniformly over controls (pp. 19–23)

With $a_\eta=\eta a$, initial excitation $0\le y_\eta\le c_y\eta$, uniform subcriticality
$\eta_0\bar a_1<b$ (5.46) and discounted moment bounds (5.47)–(5.48), Prop. 5.8 gives
$\mathbb E\int_0^\infty e^{-\rho t}(Y^\eta_t)^2dt\le A_Y\eta^2$ (p. 22) and the weighted estimate
$\sup_\alpha\mathbb E\int_0^\infty e^{-\rho t}Y^\eta_t(1+(K_t)^q+(P_t)^q)dt\le A_*\eta$ (5.49), p. 20.
Proof: Itô on $e^{-\rho t}(Y^\eta)^2$, compensation, Young's inequality to absorb the
self-exciting term into $2b+\rho-2\eta_0\bar a_1>0$ (5.51)–(5.60), Cauchy–Schwarz (5.68)–(5.71).

### 9. The Poisson value function is explicit and its disaster increment is bounded independently of pollution (pp. 23–25)

From [12]: $v(k,p)=\frac{\psi^{-\varepsilon}}{1-\varepsilon}k^{1-\varepsilon}-\frac{x}{1+\beta}p^{1+\beta}$
solves the Poisson HJB $\rho v=\sup_\alpha\{U+\mathcal L^\alpha_Pv\}$ (5.78)–(5.79), p. 25. Lemma 5.9:
«The pollution terms cancel», so $\Delta_\zeta v=\frac{\psi^{-\varepsilon}}{1-\varepsilon}k^{1-\varepsilon}(\omega^{1-\varepsilon}-1)$
(5.76) and $\int|\Delta_\zeta v|\nu(d\zeta)\le\frac{\psi^{-\varepsilon}}{1-\varepsilon}k^{1-\varepsilon}$
(5.73), p. 24.

### 10. ⭐⭐ Plugging the $y$-independent Poisson value into the Hawkes generator leaves a residual linear in $y$ (p. 26)

Define $\tilde v(k,p,y):=v(k,p)$, so $\partial_y\tilde v=0$. Then
$\mathcal L^\alpha_{H,\eta}\tilde v(k,p,y)=\mathcal L^\alpha_Pv(k,p)+y\int\Delta_\zeta v(k,p)\nu(d\zeta)$
(5.87), and $|\mathcal L^\alpha_{H,\eta}\tilde v-\mathcal L^\alpha_Pv|\le A_vy(1+k^q+p^q)$ (5.88), p. 26.
«when the Poisson value function is extended trivially to the enlarged Hawkes state space, the
difference between the Hawkes and Poisson generators is entirely generated by the additional
intensity $Y^\eta$» (p. 24). The transport term vanishes because $\partial_y\tilde v=0$, and the
excitation jump $y\to y+\eta a$ is invisible to $\tilde v$.

### 11. ⭐⭐ Two-sided verification bound: $|V^\eta_H-V_P|\le\frac{\psi^{-\varepsilon}}{1-\varepsilon}A_*\eta$ (pp. 8, 25–29)

Thm. 5.10 / Thm. 4.3(3): (4.15) = (5.83). Upper bound: Itô on $e^{-\rho t}v(K^H,P^H)$ for any
control, the residual bound (5.90) and Prop. 5.8 give $J_H\le v+A_vA_*\eta$ (5.97)–(5.98). Lower
bound: run the **Poisson-optimal feedback** $\hat\alpha_P(K^H_t,P^H_t)$ in the Hawkes system;
the residual is exactly $y\int\Delta_\zeta v\,d\nu$ (5.100), so
$J_H(\hat\alpha_P)\ge v-A_vA_*\eta$ (5.101)–(5.103), pp. 28–29. Hence the Poisson feedback is
$O(\eta)$-optimal for the Hawkes problem [D from (5.98), (5.103)]. Needs: $v\in C^2$, integrability
(5.80), transversality (5.81), uniform integrability (5.82), admissibility of $\hat\alpha_P$ (p. 26).

### 12. ⭐ What is not shown: no Hawkes HJB solution, no first-order correction, no numerics (whole paper)

The Hawkes value function is never characterised by its own HJB; it is only bracketed by the
Poisson one. The «explicit first-order bound for the approximation error» (p. 2) is an $O(\eta)$
error bound on the order-0 (Poisson) approximation, not a computed $O(\eta)$ correction term. There
is no numerical section, and the result concerns value functions, not policies (beyond the
$O(\eta)$-optimality of the Poisson feedback in Kernthese 11). Infinite horizon, discounted.

## What this source does not address

- **Market making, quotes, fills, inventory.** None; the model is macro growth with disasters.
- **Several intensities / cross-excitation.** One scalar intensity, one event type; marks scale the
  jump, but there is no branching matrix and no cross-excitation.
- **The exact Hawkes control problem.** No HJB for $V_H$ is solved, no regularity of $V_H$ is shown.
- **A correction beyond order 0.** No first-order term in $\eta$, no expansion around a forecast;
  the expansion point is the Poisson ($\eta=0$) model.
- **Large or near-critical excitation.** The bound needs $\eta\to0$ and $y_\eta=O(\eta)$.
- **Numerics, benchmarks, regret.** None.

## Model card

| Field | Value |
|---|---|
| Assets | n/a — not market making; one capital stock, one pollution stock, one disaster intensity |
| Kernel | exponential Hawkes (marked), decay $b$, jump $a(\zeta)$ (2.3), p. 3 |
| Excitation | self only (disasters excite disasters); no cross-side / cross-asset |
| Who excites the flow | all events (every disaster); controls act on the baseline $\mu(P)$ via pollution, not on the excitation (4.11), p. 7 |
| Objective | discounted infinite-horizon utility $\mathbb E\int e^{-\rho t}U(K,P,\alpha)dt$ (Thm. 5.10, p. 25); power-type Poisson value |
| Solution method | Poisson value function explicit (from [12]); Hawkes value bracketed by verification with a residual bound, $\lvert V^\eta_H-V_P\rvert\le\frac{\psi^{-\varepsilon}}{1-\varepsilon}A_*\eta$ (5.83) |
| Benchmark | the Poisson model ($\eta=0$) |
| Reported regret / gap numbers | none numerical; analytic gap $O(\eta)$ with constant $A_*$ from Prop. 5.8 |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 2, 3, 6, 8, 10, 11, 12.**

### What this focus needs beyond the Kernthesen

1. **Verdict: off-domain, but a reusable proof device.** Not market making. There is no flow, no
   quote, no inventory and no closed form for the Hawkes problem. The lift (Kernthese 2) is the
   standard scalar one. What carries over is the **error-bound technique**: take the explicit value
   function of a simpler problem, plug it into the exact (lifted) generator, and bound the residual
   uniformly over controls. That gives a two-sided value bound and the near-optimality of the simple
   feedback (Kernthesen 10–11).
2. **Where the closure "holds".** No closure is attempted for $V_H$. The order-0 object is closed
   because it does not depend on $y$ at all, so the transport term $-by\partial_y$ and the excitation
   jump drop out exactly and only $y\int\Delta_\zeta v\,d\nu$ survives (5.87). In project terms
   [I]: this is the **frozen-baseline / Poisson approximation** evaluated in the lifted state, the
   analogue of plugging the Poisson-BEGV $\theta(t,q)$ into the Hawkes HJB in $(q,\lambda)$. The
   residual there would be $\sum_j(\lambda_j-\mu_j)\,\breve H(p^j)$-type terms, linear in the
   excitation, as here.
3. **What breaks for market making [I].** Three properties make the bound easy here and fail in
   the project's problem. (a) $\Delta_\zeta v$ is bounded independently of $p$ and of the control
   (Lemma 5.9). In market making the analogous increment is the optimised Hamiltonian at $p^j$, which
   grows quadratically in inventory. (b) The infinite discounted horizon with $y_\eta=O(\eta)$ makes
   the excitation small for all $t$. Stage 2a works on $[0,T]$ with $O(1)$ excitation and a large
   baseline instead. (c) Controls do not touch the intensity at all, so the generator difference is
   control-independent. In flow-driven market making that also holds, which is favourable.
4. **Multi-asset carry-over [I].** The residual argument is dimension-free in form. With $Y\in\mathbb
   R^{2d}$, $dY=-DY\,dt+DK\,dN$, the generator difference would be $\sum_j Y_j\int\Delta_jv$. The
   uniform discounted $L^2$ estimate (Prop. 5.8) would need the matrix subcriticality $\rho(K)<1$ in
   place of $\eta_0\bar a_1<b$, via a Lyapunov weight rather than the scalar Young inequality. Not in
   the paper.

### Bearing on Stage 2a (`input/ideas/hawkes-perturbative-closed-form-design.md`)

- **Fallback scaling, not the main one.** The paper's $\eta$ scales the excitation jump with the
  baseline fixed, so the limit is Poisson. That is Stage 2a's **small-$\|K\|$** fallback
  (Disconfirmation 1), not the large-baseline scaling $\mu\to\mu/\varepsilon^2$. For the fallback it
  is a direct precedent: order 0 = Poisson value, error $O(\eta)$ in value, proved by residual +
  verification (Thm. 5.10). It gives no order-1 term.
- **Error-order proof template for S1 [I].** The verification-with-residual route (5.86)–(5.103)
  is a candidate way to prove a value-gap order for the truncated Riccati solution: plug
  $\theta^{\rm approx}=-q^\top(A^0+\varepsilon\sum\tilde\Delta_kA^1_k)q-\dots$ into the exact lifted
  HJB, bound the residual, and run the two-sided Itô argument with the approximate feedback. The
  residual of an order-1 truncation would be $O(\varepsilon^2)$ times polynomial weights in $q$; the
  moment bounds in $q$ (inventory bounded by $Q$ in the project) replace their $(1+k^q+p^q)$ weights.
- **Order-0 bound is first order in $\eta$ [I].** For the fallback this sets expectations. The frozen
  (Poisson) policy has value gap $O(\|K\|)$. An order-1 correction would have to be shown to reach
  $O(\|K\|^2)$.

### Direct quotes (for the draft)

> "Our work focuses on a subcritical Markovian Hawkes specification, in which the state space is augmented by the self-excitation component of disaster risk." (p. 1)

> "The main difficulty relative to the Poisson model is that the jump intensity is itself stochastic and depends on the endogenous excitation process Y." (p. 8)

> "The key observation is that, when the Poisson value function is extended trivially to the enlarged Hawkes state space, the difference between the Hawkes and Poisson generators is entirely generated by the additional intensity $Y^\eta$." (p. 24)

> "The uniform weighted estimate over admissible controls leads to an O(η) bound for the difference between the Hawkes and Poisson value functions." (p. 29)

### Examples & illustrations (for later drafting)

- Eqs. (5.86)–(5.88), p. 26: a three-line illustration of why a $\lambda$-independent value function
  turns the Hawkes generator into "Poisson generator + excitation × jump increment".
- Eq. (5.37), p. 15: the scalar mean-excitation ODE, a one-dimensional instance of the project's
  deterministic forecast $\dot m=D\mu-D(I-K)m$.

### Boundary of this focus

Everything said about market making, the multi-asset residual and Stage 2a's error proof is the
project's inference. The source has one scalar intensity, no flow-controlled fills, no closed form
for the Hawkes problem and no numbers.

## Mentioned entities

- Concepts: [[hawkes-process]], [[markov-lift]], [[intensity-forecast]], [[who-excites-the-flow]], [[branching-matrix]] (scalar branching ratio only).
- Other works (not in library): Sakhanda & Ricalde-Guerrero 2025 (arXiv:2511.13568, Poisson predecessor, source of the explicit $v$); Brémaud & Massoulié 1996; Hawkes & Oakes 1974; Øksendal & Sulem 2019; Daley & Vere-Jones 2008.

## Connections

- Same order-0 idea in the project: the frozen-forecast / Poisson-BEGV policy evaluated under Hawkes flow ([[problem-anatomy]] §4; [[begv-2021-model]]).
- Contrast with: [[fujii-2015-optimal-position-management]] — Fujii expands to all orders around a deterministic path of a diffusive factor with an $\epsilon^{N+1}$ bound; here only order 0, a jump factor, and an $O(\eta)$ bound by residual + verification.
- Contrast with: [[ceci-2025-optimal-reinsurance-dynamic]] — also a Hawkes control problem with a lifted intensity, but finite horizon, CARA, and an exact BSDE characterisation instead of an approximation.
