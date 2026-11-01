---
title: "Ceci & Cretarola 2025 — Optimal reinsurance in a dynamic contagion model: comparing self-exciting and externally-exciting risks"
type: source
created: 2026-10-26
updated: 2026-10-26
status: review
author: llm
bibkey: ceci-2025-optimal-reinsurance-dynamic
depth: standard
based_on: preprint
tags: [hawkes, dynamic-contagion, cox-shot-noise, cara, exponential-utility, hjb, bsde, stochastic-lipschitz, reinsurance, exponential-affine, markov-lift, single-intensity]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Claim intensity (2.1) combines self-exciting jumps $\\ell(Z^{(1)}_j)$ at claims with externally-excited jumps $Z^{(2)}_j$ at Poisson times, exponential decay $\\alpha$ (p. 4) — the Dassios–Zhao dynamic contagion process."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "«The process Λ is an (F,P)-Markov process with generator …» (Prop. 2.4, p. 6); under Markovian premiums «the pair $(X^u,\\Lambda)$ … is a Markov process» (p. 10), value $v(t,x,\\lambda)$ (4.2)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Every claim excites the intensity and the control (retention) does not change arrivals, only the wealth jump at the same event (Lemma 4.4, p. 11). Externally-excited jumps do not hit wealth; they drop out of the Cox-case control (Remark 6.4, p. 24). Analogy to flow- vs fill-driven conventions is the project's."
  - target: shen-2022-mean-variance-portfolio
    type: mentions
    confidence: inferred
    because: "Both obtain an exponential-affine-in-intensity representation only for a fixed control (here Lemma 7.5 / eq. 7.5 under Q, p. 30); the optimised value does not inherit it. Not cited."
---

# Optimal reinsurance in a dynamic contagion model: comparing self-exciting and externally-exciting risks

## Bibliographic Details

Ceci, Claudia, and Alessandra Cretarola. 2025. "Optimal reinsurance in a dynamic contagion model:
comparing self-exciting and externally-exciting risks." *Quantitative Finance* 26(8): 1199–1219.
doi:10.1080/14697688.2025.2488450. Preprint arXiv:2404.11482. Affiliations: Sapienza University of
Rome (MEMOTEF); University "G. D'Annunzio" of Chieti-Pescara.

**Read: arXiv 2404.11482v2 (20 September 2024, preprint, 38 pp.); page/equation numbers follow it.**
Non-core work; preprint accepted under the project's preprint policy. A published version exists,
hence `based_on: preprint`.

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $\lambda_t$ ($\Lambda$) | claim-arrival intensity (2.1) | $\lambda_t$ (scalar) |
| $\beta$ | reversion level of $\lambda$ | $\mu$ (baseline) — ⚠ **not** a decay |
| $\alpha$ | exponential decay rate | $\beta$ |
| $\ell(z)$ | self-exciting jump per claim of size $z$ (e.g. $az$) | $K$ (scalar, mark-dependent) |
| $N^{(2)}$, $\rho$, $Z^{(2)}$ | external Poisson shocks, their rate, their jump in $\lambda$ | no project symbol (exogenous cross-excitation into $\lambda$) |
| $N^{(1)}$, $Z^{(1)}$, $F^{(1)}$ | claims, claim sizes, size distribution | — |
| $\eta$ | CARA risk aversion | $\gamma$ |
| $\Phi(z,u)$ | retained part of a claim under control $u$ | — |
| $q(t,\lambda,u)$, $c(t,\lambda)$ | reinsurance / insurance premium rates | ⚠ $q$ is **not** inventory |
| $\theta_R,\theta_I$ | safety loadings | ⚠ not the reduced value function |
| $\varphi(t,\lambda)$ | reduced value, $v=e^{-\eta xe^{r(T-t)}}\varphi(t,\lambda)$ | ≈ $e^{-\gamma\theta}$ in the GLFT sense; one state variable only |
| $W^N$, $V_t$ | Snell envelope under null reinsurance; value process | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract; 1 Introduction (literature: Dassios–Zhao 2011, Cao et al. 2020, Brachetta et al. 2024, Wu et al. 2024) | 1–3 |
| ✓ F1 | 2 Framework: intensity (2.1), change of measure (2.4), compensators (2.5), Markov generator (Prop. 2.4) | 4–6 |
| ✓ | 3 Problem: surplus with reinsurance, contracts (Ex. 3.1), premiums (Ass. 3.2, Ex. 3.8), CARA objective (3.1) | 6–10 |
| ✓ F1 | 4 HJB: generator (Lemma 4.4), CARA factorisation, reduced HJB (4.5)–(4.7), Verification Thm. 4.6, Prop. 4.7; 4.1 Cox case (4.11)–(4.13) | 10–15 |
| ✓ F1 | 5 BSDE approach: Snell envelope (5.1)–(5.6), martingale representation (Prop. 5.2), Thm. 5.4, Thm. 5.5, Cor. 5.6, Prop. 5.8 | 15–22 |
| ✓ F1 | 6 Optimal strategy: Prop. 6.1, Cox Prop. 6.3 / Remark 6.4; 6.1 EVP cases (Props. 6.5, 6.7) | 22–27 |
| ✓ F1 | 7 Comparison (Props. 7.1–7.2), Lemma 7.5 (representation under Q), monotonicity Prop. 7.6 | 28–30 |
| — | Acknowledgements, references | 31–32 |
| ✓ | Appendix A: proofs (Thm. 4.6, Thm. 5.5 via Papapantoleon et al. 2018, Lemma 7.5, Lemmas A.1–A.2) | 32–38 |

## Kernthesen

### 1. ⭐ The claim intensity is a dynamic contagion process: self-excited by claims, externally excited by Poisson shocks (pp. 4–6)

$\lambda_t=\beta+(\lambda_0-\beta)e^{-\alpha t}+\sum_{j\le N^{(1)}_t}e^{-\alpha(t-T^{(1)}_j)}\ell(Z^{(1)}_j)+\sum_{j\le N^{(2)}_t}e^{-\alpha(t-T^{(2)}_j)}Z^{(2)}_j$
(2.1), p. 4, i.e. $d\lambda=\alpha(\beta-\lambda)dt+\int\ell(z)m^{(1)}(dt,dz)+\int z\,m^{(2)}(dt,dz)$ (2.6),
p. 5. $N^{(2)}$ is Poisson with rate $\rho$; $N^{(1)},N^{(2)}$ have no common jumps (p. 4). The
self-exciting jump may depend on claim size, e.g. $\ell(z)=az$ (p. 4). $\lambda$ is Markov with an
explicit generator (Prop. 2.4, p. 6).

### 2. The model is built by a change of measure from unit-rate Poisson processes (p. 5)

Under $\mathbf Q$, $N^{(1)},N^{(2)}$ are Poisson with rate 1; $\mathbf P$ is defined by
$L_t=\exp(-\int_0^t(\lambda_s-1)ds+\int_0^t\ln\lambda_{s-}dN^{(1)}_s)$ (2.4), giving the
$\mathbf P$-compensators $\lambda_{t-}F^{(1)}(dz)dt$ and $\rho F^{(2)}(dz)dt$ (2.5), p. 5. This
resolves the «apparent logical loop» of an intensity defined through its own history (p. 4).

### 3. Objective: CARA utility of terminal wealth under general reinsurance contracts and premiums (pp. 6–10)

Wealth $dX^u=[c-q^u+rX^u]dt-\int\Phi(z,u)m^{(1)}(dt,dz)$; the insurer solves
$\inf_u\mathbb E[e^{-\eta X^u_T}]$ (3.1), p. 8. Contracts: proportional, excess-of-loss, limited
excess-of-loss (Ex. 3.1, p. 7). Premiums: expected-value, variance and mean-variance principles
(Ex. 3.8, pp. 9–10).

### 4. ⭐⭐ CARA removes wealth exactly: $v=e^{-\eta xe^{r(T-t)}}\varphi(t,\lambda)$, and the HJB reduces to a PIDE in $\lambda$ alone (pp. 11–12)

Because wealth is linear and utility exponential, «we can write (4.2) as follows
$v(t,x,\lambda)=e^{-\eta xe^{r(T-t)}}\varphi(t,\lambda)$» (p. 11). The reduced HJB (4.5) is
$\partial_t\varphi+\alpha(\beta-\lambda)\partial_\lambda\varphi+\int[\varphi(t,\lambda+z)-\varphi]\rho F^{(2)}(dz)-\eta e^{r(T-t)}\varphi c+\inf_u\Psi^u=0$,
$\varphi(T,\lambda)=1$ (4.6), with
$\Psi^u=\eta e^{r(T-t)}\varphi q(t,\lambda,u)+\int[e^{\eta\Phi(z,u)e^{r(T-t)}}\varphi(t,\lambda+\ell(z))-\varphi(t,\lambda)]\lambda F^{(1)}(dz)$
(4.7), p. 12. For each fixed $u$ every term is **linear** in $\varphi$; the nonlinearity is only the
$\inf_u$.

### 5. ⭐ The optimal retention depends on the value-function ratio $\varphi(t,\lambda+\ell(z))/\varphi(t,\lambda)$ (pp. 13–14)

Verification Thm. 4.6 (classical $C^1$ solution, uniform integrability), p. 13. Prop. 4.7: under
strict convexity the optimum is $u_M$, $u_N$ or the root $\bar u$ of
$-\varphi\,\partial_uq=\int\varphi(t,\lambda+\ell(z))e^{\eta e^{r(T-t)}\Phi}\partial_u\Phi\,F^{(1)}(dz)$
(4.8)–(4.10), p. 13. The self-exciting jump $\ell$ makes the feedback depend on how much the value
changes when a claim raises the intensity.

### 6. ⭐ Classical solvability of the reduced HJB is open, even without self-excitation (pp. 2, 14–15)

«proving the existence of a classical solution to the HJB equation … is challenging» because it is
«a partial integro-differential equation, compounded by an optimization component embedded within
the associated integro-differential operator» (p. 2). Even in the Cox case, «due to the fact that the
claim intensity is an unbounded process, there are no results that we can apply directly to prove
existence of classical solutions» (p. 15).

### 7. ⭐⭐ Without self-excitation ($\ell=0$) the control decouples and the reduced equation is linear with a Feynman–Kac solution (pp. 14–15)

With $\ell=0$, $\varphi(t,\lambda+\ell)=\varphi(t,\lambda)$ factors out of (4.7): (4.11)–(4.12) read
$\partial_t\varphi+\alpha(\beta-\lambda)\partial_\lambda\varphi+\int[\varphi(t,\lambda+z)-\varphi]\rho F^{(2)}(dz)-\varphi(\eta e^{r(T-t)}c-\lambda H)=0$
with $H(t,\lambda)=\inf_u\{\dots\}$ independent of $\varphi$, so
$\varphi(t,\lambda)=\mathbb E_{t,\lambda}[e^{-\int_t^T(\eta e^{r(T-s)}c(s,\lambda_s)-H(s,\lambda_s))ds}]$ (4.13),
p. 15. The optimal strategy then «do[es] not depend explicitly on the function $\varphi$» (p. 15).

### 8. ⭐ BSDE route: the value process solves a BSDE driven by a two-dimensional marked point process (pp. 15–21)

Snell envelope $W^u_t$ (5.1), value process $V_t$ (5.3) with $W^u_t=e^{-\bar X^u_te^{rT}}V_t$ (5.4),
$V_t=\varphi(t,\lambda_t)$ in the Markov case (5.6), p. 16. Thm. 5.4: any solution of the BSDE
(5.9) with generator (5.10) and terminal value $e^{-\eta X^N_T}$ equals $W^N$, and the pointwise
maximiser of the generator is optimal (pp. 18–21). This «enables us to solve the problem without
imposing any requirements for regularity on the associated value function» (abstract, p. 1).

### 9. Existence needs a stochastic-Lipschitz BSDE theory because the intensity is unbounded (pp. 3, 21, 33–36)

«due to the unboundedness of the claim arrival intensity, our BSDE satisfies only a stochastic
Lipschitz condition» (p. 3). Thm. 5.5 (existence and uniqueness) uses Papapantoleon–Possamaï–
Saplaouras 2018, Thm. 3.5, with Lipschitz processes $r_t=3\eta^2e^{2r(T-t)}(q^{u_M}_t)^2+3\lambda^2_{t-}$,
$\theta_t=3\lambda_{t-}$ (p. 35), plus the martingale representation of Prop. 5.2 (p. 17).

### 10. In the Markov case the BSDE integrands are jumps of $\varphi$, and the strategy is recovered without regularity (pp. 22–23)

Prop. 5.8: $\Gamma^{(1)}_t(z)=e^{-\bar X^N_{t-}e^{rT}}[e^{\eta ze^{r(T-t)}}\varphi(t,\lambda_{t-}+\ell(z))-\varphi(t,\lambda_{t-})]$
(5.15) and the analogue (5.16) for external shocks, p. 22. Prop. 6.1 recovers the strategy (4.8) of
Prop. 4.7 under concavity, «but without any regularity assumption on the value function» (p. 23).

### 11. ⭐⭐ Externally-excited risk is managed by premium alone; self-excited risk also changes the reinsurance strategy (p. 24)

Remark 6.4 (Cox, deterministic premium loadings): the strategy is a deterministic function of time.
«It is noteworthy that the optimal strategy remains independent of the claim arrival intensity or
its dynamics, thus aligning with the optimal strategy under a constant claim arrival intensity. …
However, addressing the self-exciting effect requires adjustments in both the premium rate and
reinsurance strategy» (p. 24).

### 12. Explicit threshold strategies under the expected-value principle (pp. 24–27)

Proportional reinsurance: two stochastic thresholds $\theta^F(t,\lambda)<\theta^N(t,\lambda)$ built
from $\varphi(t,\lambda+\ell(z))/\varphi(t,\lambda)$ decide full / partial / no reinsurance (Prop. 6.5,
p. 25). Limited excess-of-loss: a threshold $\theta^L$ (6.3); null reinsurance never optimal
(Prop. 6.7, p. 26). Cox limits: $u^{*,cox}(t)=\frac{\log(1+\theta_R)}{\eta}e^{-r(T-t)}$ for the
limited XL case (Remark 6.8, p. 27).

### 13. With an increasing value in $\lambda$, the contagion insurer cedes more risk than the Cox insurer (pp. 28–29)

Props. 7.1–7.2: if $\varphi(t,\cdot)$ is increasing, then $u^*_t\le u^{*,cox}(t)$ — «in the contagion
model the insurer transfers more risk to the reinsurer than in the case without the self-exciting
component» (p. 28).

### 14. ⭐ For a fixed control path, the reduced value is exponential-affine in $\lambda$ under $\mathbf Q$ (pp. 29–30)

Lemma 7.5 (premiums proportional to $\lambda$, Ass. 7.3): $\varphi(t,\lambda)=\inf_u\mathbb E^{\mathbf Q}_{t,\lambda}[\exp\{\dots\}]$ (7.1)
with $a(t,u)=1+\eta e^{r(T-t)}(c(t)-d(t,u))$, $A(t,u.)=\int_t^Ta(s,u_s)e^{-\alpha(s-t)}ds$,
$B=e^{\eta e^{r(T-t)}\Phi-A\ell}$ (7.2)–(7.3), p. 29. In the proof,
$\tilde\varphi(t,\lambda,u)=\mathbb E^{\mathbf Q}[H(t,T,u.)\,e^{\lambda\int_t^Te^{-\alpha(s-t)}\{\int BF^{(1)}-a\}ds}]$
(7.5) with $H$ «not depend[ing] on $\lambda$» (p. 30). Prop. 7.6 gives monotonicity in $\lambda$
under condition (7.4). The $\inf_u$ is taken **after** this representation, so the optimised
$\varphi$ is not itself exponential-affine [I from (7.1)].

### 15. No numerical illustration (whole paper)

All results are qualitative or quasi-explicit; no simulation, no calibration, no figures.

## What this source does not address

- **Market making, quotes, inventory.** The control is a claim-retention level; wealth is linear in
  the claim jumps, there is no inventory state.
- **Control of arrival rates.** The insurer cannot change claim arrivals; the control acts only on
  the size of the wealth jump at an event.
- **Several intensities / mutual excitation.** One intensity; external shocks excite it one-way, but
  there is no second excited process and no branching matrix.
- **An explicit value function in the contagion case.** $\varphi$ is characterised (BSDE, PIDE), not
  computed; only the Cox strategy is explicit.
- **Approximation or expansion.** None; no small-parameter analysis.
- **Numerics.** None.

## Model card

| Field | Value |
|---|---|
| Assets | n/a — not market making; one insurance line, wealth + one intensity |
| Kernel | exponential (dynamic contagion: Hawkes + Cox shot noise), decay $\alpha$, mean reversion to $\beta$ (2.1), p. 4 |
| Excitation | self (claims, size-dependent $\ell(z)$) + external one-way (Poisson shocks $Z^{(2)}$); no cross-asset |
| Who excites the flow | all claims; the control does not change arrivals, only the retained loss at the same event (Lemma 4.4, p. 11) |
| Objective | CARA utility of terminal wealth, $\inf_u\mathbb E[e^{-\eta X^u_T}]$ (3.1) |
| Solution method | CARA factorisation → PIDE in $\lambda$ (4.5); verification for classical solutions (Thm. 4.6); BSDE with stochastic-Lipschitz generator for existence (Thms. 5.4–5.5); Feynman–Kac in the Cox case (4.13); quasi-explicit threshold strategies (Props. 6.5, 6.7) |
| Benchmark | Cox shot-noise model ($\ell=0$) and constant intensity |
| Reported regret / gap numbers | none — no numerics |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-26

**Carries Kernthesen 1, 4, 5, 6, 7, 11, 14.**

### What this focus needs beyond the Kernthesen

1. **Verdict: off-domain, but a clean instance of the closure mechanism.** Not market making, one
   intensity, no closed form for the self-exciting case. Its value for the project is structural:
   it shows *exactly* where a CARA closure survives Hawkes excitation and where it does not.
2. **Where the closure holds [S+D].** CARA plus linear wealth removes wealth exactly (Kernthese 4).
   What is left is linear in $\varphi$ for each control. If the event that jumps wealth does **not**
   jump the intensity ($\ell=0$), the $\inf_u$ factors out of $\varphi$ and the equation is linear,
   solved by Feynman–Kac (Kernthese 7). Excitation by events that do not move wealth (the Cox
   shocks $N^{(2)}$) only adds a linear jump term in $\lambda$ and leaves the control unchanged
   (Kernthese 11).
3. **Where it breaks [S+D].** If the wealth-jumping event also jumps the intensity ($\ell\ne0$), the
   optimised term contains $\varphi(t,\lambda+\ell(z))/\varphi(t,\lambda)$ (4.10). The equation is
   then a nonlinear Bellman PIDE with no known classical solution (Kernthese 6). The authors switch
   to a BSDE to get existence. This is the same obstruction the project finds for the flow-driven
   GLFT substitution: the value after the excitation jump enters the optimiser nonlinearly
   ([[problem-anatomy]] §3b) [I: analogy].
4. **Lift.** One-dimensional Markov lift of an exponential kernel with marks (Prop. 2.4); value
   $v(t,x,\lambda)$. Nothing beyond the standard lift ([[markov-lift]]).
5. **Exponential-affine structure only for fixed controls (Kernthese 14) [I].** Under $\mathbf Q$
   and premiums proportional to $\lambda$, the cost of a *fixed* control path is exponential-affine
   in $\lambda$, with a Volterra-type coefficient $\int_t^Te^{-\alpha(s-t)}\{\dots\}ds$. Optimising
   breaks it. This matches the Stage 2a finding that an exponential-affine ansatz does not close for
   the optimised problem ([[shen-2022-mean-variance-portfolio]] analogue).
6. **Multi-asset carry-over [I].** Not addressed. The structural lesson does carry over. Under CARA,
   excitation that arrives through events the agent does not trade on (here $N^{(2)}$) enters
   linearly and is harmless to the closure. Excitation through the agent's own wealth-moving events
   is what makes it nonlinear. In multi-asset flow-driven market making, a market order in asset $j$
   both may fill the maker (jumping $q_j$ and cash) and excites all $\lambda_k$ through column $j$ of
   $K$. So the cross-asset terms sit in the nonlinear class, not the harmless one, unless the jump is
   separated from the fill.

### Bearing on Stage 2a (`input/ideas/hawkes-perturbative-closed-form-design.md`)

- No perturbative closed form, no multi-asset Hawkes; does not overlap Stage 2a's claims.
- Indirect support for the design's diagnosis that a truncation is needed: here, too, the
  exponential-affine form holds only for a fixed control (Kernthese 14), and the full problem is
  handled by existence theory, not by a closed form.
- The Cox result (Kernthese 11) gives a clean $K\to0$-type limit check in miniature: when no
  excitation is tied to the controlled event, the optimal control equals the constant-intensity one.
  The analogue in Stage 2a is the S2 limit check "$K\to0$ → Poisson BEGV" [I].

### Direct quotes (for the draft)

> "It is important to stress that proving the existence of a classical solution to the HJB equation corresponding to the optimal stochastic control problem under investigation is challenging due to its inherent complexity. This difficulty stems from the equation's nature as a partial integro-differential equation, compounded by an optimization component embedded within the associated integro-differential operator." (p. 2)

> "It is noteworthy that the optimal strategy remains independent of the claim arrival intensity or its dynamics, thus aligning with the optimal strategy under a constant claim arrival intensity." (p. 24)

> "However, addressing the self-exciting effect requires adjustments in both the premium rate and reinsurance strategy, as outlined in Proposition 6.1. In essence, the self-exciting effect poses a greater challenge, necessitating a more comprehensive array of risk management tools." (p. 24)

> "Note that, due to the fact that the claim intensity is an unbounded process, there are no results that we can apply directly to prove existence of classical solutions to (4.12)" (p. 15)

### Examples & illustrations (for later drafting)

- Eq. (4.7) vs (4.11), pp. 12, 14: the same HJB term with $\ell\neq0$ and $\ell=0$. A compact
  illustration of "excitation tied to the controlled event makes the optimiser nonlinear".
- Remark 6.8, p. 27: $u^{*,cox}(t)=\frac{\log(1+\theta_R)}{\eta}e^{-r(T-t)}$, a closed-form control
  that ignores the (Cox) intensity entirely.

### Boundary of this focus

The market-making analogies (items 3, 6 and the Stage 2a bullets) are the project's inferences. The
source has one intensity, no quote-controlled arrivals, no multi-asset structure and no numbers.

## Mentioned entities

- Concepts: [[hawkes-process]], [[markov-lift]], [[who-excites-the-flow]], [[volterra-riccati]] (only as analogy for the $\int e^{-\alpha(s-t)}\dots ds$ coefficient in (7.5)).
- Other works (not in library): Dassios & Zhao 2011 (dynamic contagion process); Brachetta, Callegaro, Ceci & Sgarra 2024 (same model under partial information); Cao, Landriault & Li 2020 (mean–variance reinsurance under dynamic contagion, same qualitative finding); Wu, Shen, Zhang & Ding 2024 (closed-form value with self-excitation only, HJB approach, p. 2); Papapantoleon, Possamaï & Saplaouras 2018 (stochastic-Lipschitz BSDEs).

## Connections

- Same closure obstruction as the flow-driven GLFT substitution: [[problem-anatomy]] §3b; [[gueant-2013-dealing-inventory-risk]] (CARA linearisation).
- Exponential-affine only for fixed controls: [[shen-2022-mean-variance-portfolio]].
- Contrast with: [[sakhanda-2026-hawkes-jump-diffusion]] — also a lifted scalar Hawkes control problem, but approximated by its Poisson limit with an $O(\eta)$ value bound instead of characterised exactly.
