---
title: "Bielecki, Mastrolia & Yan 2026 — Continuous-time reinforcement learning for controlled Hawkes jump-diffusions"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: bielecki-2026-continuous-time-reinforcement
depth: standard
tags: [hawkes, markov-lift, sum-of-exponentials, reinforcement-learning, ct-ddpg, controlled-intensity, value-convergence, cyber-risk]
relations:
  - target: khabou-2025-markov-approximation-hawkes
    type: builds-on
    confidence: extracted
    because: "«To the best of our knowledge, the main recent breakthrough is due to [41], who approximate the value of a stochastic control problem driven by a general-kernel Hawkes process by that of a regularized version driven by a mixture of exponentials» (p. 2); [41] = Khabou & Talbi."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "Thm 3.10 (p. 19): process, objective and value convergence of the signed exponential-mixture lift, uniformly in the control, «V0K − V0 → 0»; lift state (t, X, Z^1,…,Z^K), Def. 3.4 (p. 11)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Multivariate controlled Hawkes intensity λ^i = µ^i(t,X,a_t) + Σ_j ∫ Φ_ij(t−s, a_t) dN^j, eq. (1)–(2) (pp. 4–5), with «Φ is a mutual excitation matrix» (p. 2)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "The controlled events themselves feed the memory and the current action rescales the memory readout (Remark 2.2, p. 5); the numerics use a Hill attenuation Q(a) of the excitation gain (p. 35) — a controlled-excitation convention, not a market-making one."
  - target: jusselin-2021-persistent-order-flow
    type: cites
    confidence: extracted
    because: "Jusselin [37] cited under «market order flow modeling [38, 37, 26, 25]» (p. 2); not discussed further."
---

# Continuous-Time Reinforcement Learning for Controlled Hawkes Jump-Diffusions

## Bibliographic Details

Bielecki, Tomasz R., Thibaut Mastrolia and Haoze Yan. 2026. *Continuous-Time Reinforcement Learning
for Controlled Hawkes Jump-Diffusions*. arXiv:2608.19151v1 [cs.LG], 19 August 2026 (title page dated
20 August 2026). 43 pp. Affiliations: Hinsdale, Illinois (Bielecki); UC Berkeley IEOR (Mastrolia,
Yan).

**Read: arXiv 2608.19151v1 (preprint); page/equation numbers follow it.** Not a core (B1) work; the
preprint is accepted under the preprint policy. The algorithm is named both "Hawkes-CT DDPG"
(abstract) and "Hawkes CT-DDPG" (body); the body form is used here.

### Notation map (source → project)

| Source | Meaning | Project symbol / remark |
|---|---|---|
| $X$, $d_x$ | controlled physical state | ⚠ not cash |
| $N=(N^1,\dots,N^m)$, $\lambda$ | $m$-variate counting process, intensity | $\lambda_t$ |
| $\mu(t,x,a)$ | baseline, depends on state **and current action** | $\mu$ |
| $\Phi(\tau,a)\in\mathbb R^{m\times m}_+$ | kernel matrix read with the current action | kernel; masses ↔ $K$ |
| $Q_k(a)$, $\beta k$ | signed coefficient matrices, decays on a lattice | $\beta$, $D=\mathrm{diag}(\beta)$ |
| $Z^{K,k}\in\mathbb R^m$ | exponential memory filter $k$ | lift state |
| $K$ | number of filters | ⚠ clashes with project $K$ (branching matrix); "$p$" in Acero, "$n$" in Khabou |
| $\delta_K(T)$ | $\int_0^T\sup_a\|\Phi_K-\Phi\|_{1\to1}$ — kernel error | E0 input |
| $\rho$ | reward discount rate | ⚠ not $\rho(K)$ |
| $\gamma_i$, $b$, $\sigma$ | jump size, drift, vol | ⚠ $\gamma$ is not risk aversion |
| $a$, $A$ compact | action, action space | quotes $\delta$ in MM |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (cyber-risk motivation) | 1 |
| ✓ F1 | 1.1 Hawkes processes: theory, applications, control (literature) | 2 |
| ✓ F1 | 1.2 Hawkes CT-DDPG: the big picture | 3–4 |
| ✓ F1 | 2 Framework: controlled system (1)–(4), Remarks 2.1–2.5, Assumption 2.1 | 4–6 |
| ✓ F1 | 3.1 Signed exponential approximation: Assumption 3.1, Lemma 3.1, Remark 3.2 | 7–9 |
| ✓ F1 | 3.2 Markovianization: (8)–(9), (Hawkes–SDE)$_K$, Remark 3.3, Def. 3.4, Remark 3.5, Assumption 3.2, Prop. 3.6, Remark 3.7 | 9–14 |
| ✓ F1 | 3.3 Objective and value convergence: Assumption 3.3, generator, Lemmas 3.8–3.9, **Thm 3.10** and proof | 14–25 |
| ✓ F1 | 3.4 Online Markov-state update: Algorithm 1, Remark 3.11 | 25–26 |
| ✓ F1 | 4.1 Hawkes-MDP and value function: Def. 4.1, Thm 4.2 | 26–29 |
| (✓) | 4.2 Advantage rate: Def. 4.4, Thm 4.5 | 29–31 |
| (✓) | 4.3 Policy loss: Lemma 4.6, Assumption 4.1, Thm 4.7 | 31–33 |
| ✓ F1 | 4.4 Full algorithm (Algorithm 2) | 33–34 |
| ✓ F1 | 5 Numerical illustrations: model, three kernels, benchmarks, Figs. 1–3 | 34–38 |
| — | References | 38–41 |
| ✓ F1 | A Numerical setup: Tables 1–3, subcriticality check | 42–43 |

(✓) = read for statements, proofs skimmed.

## Kernthesen

### 1. ⭐⭐ The control enters the intensity twice: in the baseline and in how the *current* action reads the whole memory (pp. 2, 4–5)

$\lambda^{a,i}_t=\mu^i(t,X^a_{t-},a_t)+\sum_j\int_{(0,t)}\Phi_{ij}(t-s,a_t)\,dN^{a,j}_s$ (eq. 1–2,
pp. 4–5). «The control inside the kernel Φ is given by the current action $a_t$, not the
historical action $(a_s)_{s\le t}$. The coefficient $\Phi_{ij}(\tau,a)$ represents the lag-τ
excitation of component i caused by a past jump in component j, as read under the current action
$a_t$» (Remark 2.2, p. 5). The events $N$ are themselves the controlled process; there is no
separate "uncontrolled flow" layer.

### 2. Standing assumptions: nonnegative kernels with an action-uniform $L^1$ envelope; well-posedness assumed, not proved (pp. 6)

Assumption 2.1: Lipschitz/linear-growth $b,\sigma,\gamma$ (S1) and baseline (S2); (S3) $\Phi$
**entrywise nonnegative** with $\phi_T=\sup_a\|\Phi(\cdot,u)\|_{1\to1}\in L^1([0,T])$; (S4) strong
existence and moments uniform in $a$. Remark 2.5: this «isolates strong existence, pathwise
uniqueness, nonexplosion, and uniform moment control from the Markov-approximation argument»,
referring to Khabou–Talbi Prop. 1.4 for sufficient conditions (p. 6).

### 3. ⭐ The approximation must hold uniformly in the action, on a fixed decay lattice (pp. 7–9)

«In our model however, we face a technical challenge since the Markovianized kernel is itself
controlled and must approximated the general one unformly with respect to the control» (p. 7).
Assumption 3.1: fix $\beta>0$; $\Phi_K(\tau,a)=\sum_{k=1}^KQ_k(a)e^{-\beta k\tau}$ with continuous
$Q_k:A\to\mathbb R^{m\times m}$ and $\delta_K(T)=\int_0^T\sup_a\|\Phi_K(\tau,a)-\Phi(\tau,a)\|_{1\to1}d\tau\to0$
(p. 7). It is an **assumption**, verified for separable kernels $\Phi(\tau,a)=\hat\Phi(\tau)Q(a)$ on
compact $A$ with $m=1$ (Remark 3.2, p. 9). Lemma 3.1 bounds the resolvents of the envelopes
uniformly in $K$ (pp. 7–9).

### 4. Signed weights are allowed; a componentwise positive part keeps the intensity valid (pp. 3, 10–11)

$\lambda^K_t=\mu(t,X^K_{t-},a_t)+\big(\sum_kQ_k(a_t)Z^{K,k}_{t-}\big)_+$ ((Hawkes–SDE)$_K$, p. 10).
«mixtures of exponentials with possibly negative weights are dense in $L^p$» (Kammler, p. 3);
«Since signed approximants may create negative raw memory values, the approximating intensity
applies a componentwise positive part only to the approximated memory term» (Remark 3.3, p. 11).
So the true kernel is nonnegative (S3), but the approximant may be signed.

### 5. The lift: $K$ vector filters, i.e. $K\cdot m$ memory variables, all updated from event times (pp. 10–11)

$dZ^{K,k}_t=-\beta_kZ^{K,k}_tdt+dN^K_t$ (9); state $S^K_t=(t,X^{K,a}_t,Z^{K,1}_t,\dots,Z^{K,K}_t)\in[0,T]\times\mathbb R^{d_x}\times(\mathbb R^m)^K$
(Def. 3.4, p. 11). An event of type $i$ shifts every filter by $e_i$. The filters are shared across
all target components: cross-excitation lives in the matrices $Q_k(a)$, not in extra state.

### 6. ⭐ The lifted state is model-free: kernel, baseline and coefficients are not needed to build it (pp. 11, 25–26)

«The matrices $Q_k(a)$, the baseline µ, and the intensity λ are used only in the theoretical Markov
approximation. They are not needed to construct the state $S^K_t$» (Remark 3.5, p. 11). Algorithm 1
updates the filters from observed time stamps and labels (p. 26); with binned counts only, an
endpoint approximation $Z^k_{t_{n+1}}\approx e^{-\beta_k\Delta_n}Z^k_{t_n}+\Delta N_n$ is offered
(Remark 3.11, p. 26).

### 7. Uniform moments from bounded baseline, bounded jumps and a subcritical envelope (pp. 11–14)

Prop. 3.6: bounded $\mu$ and $\gamma$, and $\rho_T=\sup_K\int_0^T\sup_u\|\Phi_K(s,u)\|_{1\to1}ds<1$
imply Assumption 3.2. Proof: dominate the total count by a scalar linear Hawkes process with the
envelope kernel, then a Galton–Watson / Borel-distribution cluster bound (pp. 12–13).

### 8. ⭐⭐ Convergence theorem: state, intensity, counts, objective and value converge, uniformly in the control — without a rate (pp. 19–25)

Thm 3.10 (p. 19), under Assumptions 2.1, 3.1, 3.2, with the same Brownian motion, Poisson measures
and control process in both systems:
$\lim_K\sup_a\big\{\mathbb E\sup_t\|X^{K,a}_t-X^a_t\|+\mathbb E\int_0^T\|\lambda^{K,a}_t-\lambda^a_t\|_1dt\big\}=0$ (21),
the same for $N$ (22); if moreover Assumption 3.3 holds (costs with polynomial growth $q+1$ and
locally Lipschitz) and $p^\star>q+1$, then $\sup_a|J_K(a)-J(a)|\to0$ and $|V^K_0-V_0|\to0$.
Rate status: inside the proof, the **localised** errors satisfy $D_{\lambda,R}(T)\le C_{T,R}\delta_K(T)$
and $D_{X,R}(T)\le C_{T,R}\delta_K(T)$ (pp. 20–21); the localisation level $R$ is then removed by
uniform integrability and Hölder (pp. 22–25), which gives convergence but **no explicit rate** in
$\delta_K$ or $K$.

### 9. Fixed-policy value solves a linear Feynman–Kac PDE on the lifted state (pp. 26–29)

Thm 4.2: for a smooth Markov policy $\pi_\zeta$ with polynomial-growth derivatives, $J^K_\zeta$
solves $\mathcal L^K_{\pi_\zeta}J-\rho J+c=0$, $J(T)=g$ (40)–(41), with generator
$\ldots-\sum_k\beta_kz_k\cdot\nabla_{z_k}f+\sum_i\lambda^K_i(t,x,z,a)[f(t,x+\gamma_i,z_1+e_i,\dots,z_K+e_i)-f]$
(p. 14). This is the transport-jump structure in the memory variables.

### 10. The RL layer: advantage rate, martingale characterisation, deterministic policy gradient (pp. 29–33)

Def. 4.4 / Thm 4.5: the advantage rate $\mathcal A=\mathcal L^K_aJ-\rho J+c$ is identified by a
martingale condition (45), which is the training signal (p. 29). Thm 4.7:
$\nabla_\zeta J^K_\zeta=\mathbb E\int_0^Te^{-\rho t}D_\zeta\pi_\zeta^\top\nabla_a\mathcal A^K_\zeta\,dt$
(p. 32). Algorithm 2 (p. 33) = CT-DDPG of Cheng–Guo–Zhang on the lifted state, with value critic,
raw advantage critic, replay buffer and target networks.

### 11. ⭐ The error budget has two parts, and only the first is analysed (p. 3)

«the convergence of our algorithm rests on two main contributions: the Markovianization
approximation and the error incurred when training the actor and critic networks … The former can
be analyzed theoretically, whereas the latter remains poorly understood within current
reinforcement learning theory and can only be assessed numerically» (p. 3).

### 12. Numerical model: one event type, a Hill-type attenuation of the excitation gain, quadratic costs (pp. 34–35; App. A)

$m=d_x=d_W=1$; $dX=(b_0-\kappa X-b_aa)dt+[\sigma_0+\sigma_xX+\sigma_aa]_+dW+\mathrm{clip}(\gamma_0+\gamma_xX+\gamma_aa)dN$;
$\lambda_t=\mu(t,X,a)+\alpha Q(a_t)\int\phi(t-s)dN_s$ with $Q(a)=1-c_{\rm eff}a/(a_{\rm half}+a)$;
costs $c=c_xX^2+c_aa^2$, $g=\tilde cX_T^2$ (pp. 34–35). Kernels: exponential $e^{-1.30u}$,
Erlang $1.15ue^{-1.15u}$, power law $0.8(0.12)^{0.8}(u+0.12)^{-1.8}$; masses on $[0,T]$ 0.960, 0.893,
0.956 (pp. 42–43). Filter banks: $K=8,12,20$ with decays $0.325k$, $0.23k$, $1.00k$ (Table 2, p. 42).

### 13. ⭐ Benchmarks: exact DGM/HJB oracle for exponential and Erlang, a mixture oracle for the power law (p. 35)

For the power law «we first approximate the true kernel by a finite exponential mixture …
Since this benchmark contains both kernel-approximation error and numerical HJB error, it is
referred to below as the mixture DGM/HJB benchmark, rather than an exact oracle» (p. 35). The
mixture size $M$ of that oracle is not reported (Table 1 says only "exponential-mixture
approximation with positive memory link", p. 42).

### 14. ⭐ Results: filtered CT-DDPG is the best learned policy, 1–2% above the oracle on non-exponential kernels (pp. 36–38, Table 3 p. 43)

Mean discounted cost (Table 3, p. 43; 90% MC intervals ≈ ±4–7%):

| Policy | Exponential | Erlang | Power law |
|---|---|---|---|
| DGM/HJB oracle | 0.1658 | 0.1037 | 1.5696 (mixture) |
| CT-DDPG filtered | 0.1744 (text p. 36) | 0.1056 | 1.5870 |
| CT-DDPG current state | – | 0.1219 | 1.6647 |
| SAC filtered / DDPG filtered | – | 0.1065 / 0.1103 | 1.7056 / 1.7410 |
| static | 0.3247 | 0.1314 | 1.9242 |

Computed here (not in the paper): filtered CT-DDPG is +5.2% (exp.), +1.8% (Erlang), +1.1% (power
law, vs the mixture oracle) above the oracle. Paper: filtering cuts CT-DDPG cost by 13.4% (Erlang)
and 4.67% (power law) (pp. 36, 38). The intervals of oracle and filtered CT-DDPG overlap in all
three cases.

### 15. Conclusion drawn: memory filters help every RL method, and CT-DDPG is best among them (p. 38)

«augmenting the physical state with observable exponential filters improves the performance of
CT-DDPG, SAC, and DDPG relative to their state-only counterparts. Moreover, when all model-free
methods are supplied with the same preselected filter bank and filter-update rule, Hawkes CT-DDPG
achieves the lowest mean cost in both experiments» (p. 38).

## Figures and tables

- Fig. 1 (p. 36): exponential kernel, oracle vs CT-DDPG vs static.
- Figs. 2–3 (pp. 37–38): Erlang and power-law cost comparisons, current vs filtered.
- Tables 1–3 (pp. 42–43): experiment definitions, parameters, mean discounted costs.

No figures extracted (write scope limited to this page).

## What this source does not address

- **Market making.** The application is cyber-risk defence; MM papers (Jusselin, Gennaro–Mastrolia–
  Primavera, Graf–Mastrolia) are only cited as Hawkes applications (p. 2).
- **A rate for the lift error.** Thm 3.10 is qualitative; no dependence on $K$ or on the kernel
  class is given.
- **Multivariate experiments.** The theory is $m$-variate; all numerics have $m=1$.
- **Closed forms / Riccati.** None; the fixed-policy value is characterised by a PDE (Thm 4.2) and
  learned.
- **Non-monotone true kernels.** (S3) requires $\Phi\ge0$; only the approximant may be signed.
- **Regret against an exact optimum for non-Markov kernels.** The power-law oracle is itself
  approximate, so the E0 error of the benchmark is not separated.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 3, 4, 5, 8, 9, 11, 13, 14.** Read as a non-MM source: what its machinery
says about the lift closure (E0 of [[problem-anatomy]] §4) and about controls that feed the
intensity.

### What this focus needs beyond the Kernthesen

1. **E0 under a controlled kernel.** This is the first lift-convergence result in the wiki where
   the **current action multiplies the memory readout** and enters the baseline, and convergence is
   uniform over all admissible controls (Thm 3.10, p. 19). *Inference for MM:* a fill intensity
   $f(\delta_t)\big(\mu+\int\phi(t-s)dN_s\big)$ with $N$ = the maker's fills has the separable form
   $\mu(a)+Q(a)\int\phi\,dN$ of Remark 3.2 with $Q(a)=f(\delta)$. So the fill-driven convention
   (the maker's own fills excite, the quote thins) falls inside the theorem for $m=1$ and bounded
   quotes. The flow-driven convention (all orders excite, fills are a controlled thinning of them)
   does **not** fit as written: the fills would have to be a component driven by the same Poisson
   points as the orders, while (1) uses independent Poisson measures per component.
2. **Objective class.** Costs with polynomial growth and local Lipschitz continuity (Assumption
   3.3, p. 14) cover the risk-adjusted MM objective (quadratic inventory penalty, linear spread
   gains) given enough moments ($p^\star>q+1$). CARA utility is not covered (*inference*).
3. **No rate.** Unlike [[acero-2026-hawkes-structured-networks]] ($p^{-1/2}$) and
   [[khabou-2025-markov-approximation-hawkes]] (linear in $\|\phi_n-\phi\|_1$ for Lipschitz
   rewards), this paper gives only $V^K_0\to V_0$; the explicit $C_{T,R}\,\delta_K(T)$ bound holds
   only for the localised processes (pp. 20–21).
4. **Lift + closure.** The fixed-policy equation (Thm 4.2) is linear in $J$ but has the
   transport-jump form in $(z_1,\dots,z_K)$, shifted by $e_i$ at every event: the structure
   [[barzykin-2026-hawkes-driven-otc]] p. 8 says does not reduce to a small Riccati system. The
   paper does not look for any closed form; it learns the value and advantage rate with networks.
5. **Multi-asset / cross-excitation.** Theory: an $m\times m$ kernel with cross-excitation and a
   lift of $K\cdot m$ filters (Def. 3.4). For $d$ assets × 2 sides, $m=2d$ and the lift has $2dK$
   variables (*inference*). Numerics: only $m=1$, so nothing is shown about cross-excitation.
6. **For the gap claim (three-way comparison).** This is a working instance of the "exact
   (DGM/HJB on the lift) vs RL" comparison on a non-Markov Hawkes kernel, with the oracle–RL gaps
   of Kernthese 14. There is no closed-form leg, no MM, and the power-law oracle confounds E0 with
   solver error. It is a methodological precedent for the project's comparison design, not a
   competitor on the gap.

### Direct quotes (for the draft)

> "The control inside the kernel Φ is given by the current action $a_t$, not the historical action $(a_s)_{s\le t}$." (Remark 2.2, p. 5)

> "In our model however, we face a technical challenge since the Markovianized kernel is itself controlled and must approximated the general one unformly with respect to the control." (p. 7)

> "Since this benchmark contains both kernel-approximation error and numerical HJB error, it is referred to below as the mixture DGM/HJB benchmark, rather than an exact oracle for the original power-law problem." (p. 35)

> "The former can be analyzed theoretically, whereas the latter remains poorly understood within current reinforcement learning theory and can only be assessed numerically, by benchmarking our algorithm against an oracle and against analytical solutions, where these exist, as a sanity check." (p. 3)

### Examples & illustrations

- Erlang kernel (p. 35): exact two-state lift $(L^1,L^2)$ used by the oracle, against a 12-filter
  generic bank used by the learner. A clean case where the exact lift is known and the generic
  bank is a deliberate misspecification of the lift basis.
- Filtering ablation (Table 3): CT-DDPG with memory filters vs current state only, 0.1056 vs
  0.1219 (Erlang). This is the RL analogue of Barzykin's memory-free Poisson policy.

### Boundary of this focus

Not a market-making paper. Statements about quotes, fills and assets are the project's inference
from the general model. The numerics are one-dimensional with one control-attenuated
self-exciting stream.

## Mentioned entities

- Concepts: [[markov-lift]], [[hawkes-process]], [[who-excites-the-flow]]
- Sources in this wiki: [[khabou-2025-markov-approximation-hawkes]], [[jusselin-2021-persistent-order-flow]]
- Other works (not in library unless noted): Cheng–Guo–Zhang 2026 (CT-DDPG), Bensoussan &
  Chevalier-Roignant 2024 (`bensoussan-2024-stochastic-control-diffusions`), Callegaro–Fontana–Hillairet–Ongarato 2025, Duarte–Löcherbach–Ost 2019,
  Kammler 1976, Abi Jaber & El Euch 2019, Gennaro–Mastrolia–Primavera 2026 (`gennaro-2026-signature-methods-optimal`), Graf–Mastrolia (market
  making with closing auctions), Sirignano–Spiliopoulos (DGM), SAC, DDPG.

## Connections

- Builds on: [[khabou-2025-markov-approximation-hawkes]] (the general-kernel lift; here extended to
  action-dependent kernels, uniformly in the control, and paired with RL).
- Supports: [[markov-lift]].
- Compare: [[acero-2026-hawkes-structured-networks]] (lift with regret rate in MM),
  [[martin-2026-market-making-hawkes]] (neural PDE on a lifted MM state),
  [[barzykin-2026-hawkes-driven-otc]] (memory-free vs memory-aware policies; transport-jump
  obstruction).
- Feeds: [[problem-anatomy]] §4 (E0) and the three-way-comparison design.
