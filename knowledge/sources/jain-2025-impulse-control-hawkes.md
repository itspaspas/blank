---
title: "Jain–Firoozye–Kochems–Treleaven 2025 — An Impulse Control Approach to Market Making in a Hawkes LOB Market"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: jain-2025-impulse-control-hawkes
depth: standard
tags: [market-making, hawkes, limit-order-book, impulse-control, hjb-qvi, deep-galerkin, reinforcement-learning, ppo, single-asset, markov-lift]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "LOB modelled «using a d-dimensional mutually-exciting Hawkes process» (p. 4), exponential kernels eqs. (2.9)–(2.11) (p. 7)."
  - target: markov-lift
    type: supports
    confidence: extracted
    because: "Exponential kernels give an SDE representation (2.9); «there is no SDE representation for general kernels» and a power-law sum-of-exponentials approximation «leads to an infinite dimensional Markov process» (p. 7); full 12-D model needs «a 144 dimensional Markovian representation» (p. 9)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Intensities (2.11) are driven by all LOB events; the impulse operator Γ (App. B, pp. 26–27) updates queues, prices, cash and inventory but not λ, so the agent's own orders do not feed the intensities as written (flow-driven, exogenous). Not discussed by the authors."
  - target: gasperov-2022-deep-reinforcement-learning
    type: cites
    confidence: extracted
    because: "«[22] use an 8-dimensional Hawkes-based simulator … their Soft Actor-Critic agent outperforms a stochastic control baseline, while DQN and TD3 fail to converge» (p. 2)."
  - target: jusselin-2021-persistent-order-flow
    type: cites
    confidence: extracted
    because: "[30] «derive HJB solutions in the exponential kernel case and extend to more realistic power-law kernels via approximations» (p. 2); cited again for the sum-of-exponentials approximation of power laws (pp. 7, 11)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«The seminal work of [5] established the theoretical foundation for modern market making models» (p. 2)."
---

# An Impulse Control Approach to Market Making in a Hawkes LOB Market

## Bibliographic Details

Jain, Konark; Firoozye, Nick; Kochems, Jonathan; Treleaven, Philip. 2025. *An Impulse Control
Approach to Market Making in a Hawkes LOB Market*. arXiv:2510.26438v2 [q-fin.TR], 31 Oct 2025.
27 pp. (22 pp. text, references pp. 22–25, Appendices A–B pp. 25–27). UCL Computer Science and
J.P. Morgan Quantitative Research, London; funded by JPMorganChase (p. 1).

**Read:** arXiv 2510.26438v2 (preprint); page and equation numbers follow it. No published
version is recorded in `library/references.bib`. Non-core work, preprint accepted under the
project's preprint policy.

### Notation map (source → project)

| Source | Meaning | Project |
|---|---|---|
| $X_t$, $Y_t$ | cash, inventory | $X_t$, $q_t$ ⚠ inventory is $Y$ |
| $\lambda^{(i)}_t$, $\mu_i$ | Hawkes intensity, baseline of event type $i$ | $\lambda_t$, $\mu$ |
| $\alpha_{ij}$, $\gamma_{ij}$ | jump size and decay of the $(i,j)$ kernel (eq. 2.11) | entries of $K$ (as $\alpha_{ij}/\gamma_{ij}$), $\beta$ ⚠ source $\gamma$ is a **decay**, not risk aversion |
| $\eta$, $\kappa$ | running and terminal quadratic inventory penalty (eq. 2.1) | no project symbol (risk-adjusted objective) |
| $K(S,\psi)$ | instantaneous cost/profit of an impulse (0 for LO/CO; $z p^{(\zeta)}_t$ for MOs) | ⚠ clashes with branching matrix $K$ |
| $\Gamma(S,\psi)$ | state-intervention operator | — |
| $\mathcal M$ | value-intervention operator (eq. 2.6) | — |
| $d_t\in\{0,1\}$ | intervene-or-not control (eq. 2.7) | — |
| $n^{(\zeta)}_t, q^{(\zeta)}_t, q^{(\zeta,D)}_t$ | queue priority, top queue size, second-level queue size | — |
| $\phi_\theta, d_\chi, u_\xi$ | value, decision and action networks | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (stochastic control vs RL for LOB MM; jump decision processes vs impulse control) | 1–4 |
| ✓ F1 | 2.1 Limit Order Book model (12-event mutually exciting Hawkes, exponential kernels) | 4 |
| ✓ F1 | 2.2 Optimal market making: objective (2.1), state (2.3) | 4–5 |
| ✓ F1 | 2.3 State-intervention operator $\Gamma$ | 5 |
| ✓ F1 | 2.4 HJB-QVI (2.4)–(2.7) | 6 |
| ✓ F1 | 2.5 Generator (2.8)–(2.12): Poisson vs exponential Hawkes, no SDE for general kernels | 6–7 |
| ✓ F1 | 2.6 Solution approaches and challenges (closed form infeasible; grids impractical; DGM fails) | 7–8 |
| ✓ F1 | 3 Deep Galerkin Method for the HJB-QVI (eqs. 3.1–3.6) | 8–9 |
| ✓ F1 | 3.1 DGM results (Fig. 1, Table 1, Fig. 2 "pump and dump") | 9–11 |
| ✓ F1 | 4.1 Decomposition into decision + action networks | 11–12 |
| ✓ F1 | 4.2 State space (4.1) | 12–13 |
| ✓ F1 | 4.3 Reward (4.2) | 13–14 |
| ✓ F1 | 4.4 PPO training, simulator, action-space restriction, transaction costs (4.3)–(4.5) | 14–15 |
| ✓ F1 | 4.5 Self-imitation learning (4.6)–(4.7) | 15–17 |
| ✓ F1 | 4.6 RL results (Sharpe 31.54) | 17–18 |
| ✓ F1 | 4.7 Sensitivity and ablation (Tables 2–3), probabilistic-agent baseline (Fig. 4) | 18–20 |
| ✓ F1 | 5 Conclusion | 21 |
| ✓ F1 | 6 Future work (SMP, FBSDE, SPDE, delay, Volterra control) | 21–22 |
| — | Disclaimer, acknowledgements, references | 22–25 |
| ✓ F1 | App. A State dynamics (A.1)–(A.9) | 25–26 |
| ✓ F1 | App. B State-intervention operator (B.1)–(B.19) | 26–27 |

## Kernthesen

### 1. Market making in an LOB is a pure-jump problem, and latency makes impulse control the realistic control class (pp. 1, 3)

The authors argue that «the true microstructure of the LOB is inherently discrete and driven by a
pure jump process» (p. 1) and that jump-decision / piecewise-deterministic formulations, which let
controls react «instantaneously in response to jumps», become «increasingly unrealistic as trading
speeds approach the physical limits of electronic order processing» (p. 3). Impulse control, with
discrete intervention times, is presented as the better representation (p. 3).

### 2. ⭐ The market is a d-dimensional mutually exciting Hawkes LOB with 12 event types and exponential kernels (pp. 4, 7)

The LOB is the authors' own compound-Hawkes simulator (`jain-2024` works [27, 29], not in this
project's library). Event types are limit orders at the top (T), deeper (D) and in-spread (IS),
cancellations and market orders, per side (p. 4). The displayed event set lists **ten** symbols
($LO^{ask}_D, LO^{ask}_T, CO^{ask}_T, MO^{ask}, LO^{ask}_{IS}$ and their bid mirrors), while the
text says impulses are «one of the 12 events in E» (p. 4) and Appendix A uses deep cancellations
$CO^D_\zeta$ (eq. A.7, p. 25): the two missing types are evidently $CO^{ask}_D, CO^{bid}_D$. Kernels:
«We allow for general kernel types … but restrict to exponential kernels for mathematically
tractability» (p. 4). Intensities (eq. 2.11, p. 7):
$\lambda^{(i)}_t=\mu_i+\sum_{j=1}^M\alpha_{ij}\int_0^te^{-\gamma_{ij}(t-u)}dN^{(j)}_u$, i.e. **full
cross-excitation across all 12 types, with a separate decay per pair $(i,j)$**. «The model
implicitly includes a concave price impact due to self-excitation» (p. 4). One asset.

### 3. Objective: risk-adjusted terminal wealth with quadratic running and terminal inventory penalty, impulse costs for market orders (pp. 4–5)

Eq. (2.1): $J=\sup_u\mathbb E[\int_t^T-\eta Y_t^2dt+X_T+Y_TP^{mid}_T-\kappa Y_T^2+\sum K(S(\tau_i),\psi_i)]$,
with $K=0$ for limit/cancel orders and $zp^{(\zeta)}_t$ for market orders (p. 5). Not CARA. Order
sizes of the Hawkes events and of the agent are «uniformly constant», so only impulse time and type
are controlled; optimal size «is out of scope» (p. 5). The agent has full level-2 observation (p. 4).

### 4. The state is high-dimensional: cash, inventory, best prices, queue sizes and priority on two levels, mid-price, and all Hawkes intensities (pp. 5, 8)

Eq. (2.3): $S_t=\{X_t,Y_t,p^{(\zeta)}_t,q^{(\zeta)}_t,q^{(\zeta,D)}_t,n^{(\zeta)}_t,P^{mid}_t,(\lambda^{(i)}_t)_{i=1..d}\}$.
The DGM implementation works on «23 dimensions representing market microstructure variables»
(p. 8). Inventory moves only when an incoming market order hits the agent's resting order (eq.
A.4) or when the agent sends a market order (eq. B.19).

### 5. ⭐ The control problem is an HJB quasi-variational inequality, rewritten with a binary intervene/continue control (pp. 6)

Eq. (2.4): $\min\{-\partial_tV-\mathcal LV,\;V-\sup_\psi V(t,\Gamma(S,\psi))\}=0$, terminal condition
(2.5). With $\mathcal M\Phi=\sup_\psi\{\Phi(t,\Gamma(S,\psi))+K(S,\psi)\}$ (2.6) and $d\in\{0,1\}$:
$\sup_d\{(1-d)(\mathcal L\Phi+f)+d(\mathcal M\Phi-\Phi)\}=0$ (2.7). Well-posedness is asserted by
reference only: «We see that the conditions and assumptions for this HJB-QVI's wellposedness and
the solutions' existence have been met (Ch. 2 [42])» (p. 6, citing Øksendal–Sulem); no proof or
verification is given.

### 6. ⭐⭐ The generator is Markov only for exponential kernels; the lift dimension is the number of kernel pairs (pp. 6–7, 9)

For exponential kernels $d\lambda^{(i)}=\gamma_i(\mu_i-\lambda^{(i)})dt+\alpha_idN^{(i)}$ (2.9); for the
mutually exciting case «we have $M^2$ such equations which when added gives us the final
intensity» (p. 7), because each pair $(i,j)$ has its own decay $\gamma_{ij}$. Generator (2.12):
$\mathcal L\Phi=\Phi_t+\sum_i[\lambda^{(i)}(\Phi(t,\lambda+\alpha_{\cdot i},T_i(s))-\Phi(t,s))+\Phi_{\lambda_i}\,d\lambda_i/dt]$
(the second argument is printed as $\Phi(t,s)$, a typo for $\Phi(t,\lambda,s)$). «We note that there
is no SDE representation for general kernels of the Hawkes process» (p. 7); power laws approximated
by sums of exponentials give «an infinite dimensional Markov process» (p. 7). The full 12-type model
therefore «require[s] a 144 dimensional Markovian representation» (p. 9).

### 7. ⭐ Closed form is declared infeasible and grids impractical; the paper does not attempt any reduction (p. 7)

«obtaining a closed-form solution to the resulting quasi-variational inequality (QVI) … is
generally infeasible due to the high dimensionality and nonlinearity of the system» (p. 7). The
state includes inventory, cash, queue positions, prices, spread, imbalance, «time since last
event, and a multi-dimensional Hawkes kernel history», which «renders traditional grid-based
numerical techniques … impractical» (p. 7). No ansatz (linear, quadratic, exponential) is tried.

### 8. ⭐⭐ The Deep Galerkin Method failed; the authors locate the failure in the non-local, discontinuous impulse operator and in dimension (pp. 7–9, 21)

DGM (Sirignano–Spiliopoulos) fits LSTM networks $\phi_\theta$ (value), $d_\chi$ (decision),
$u_\xi$ (impulse) by minimising the squared QVI residual on sampled states plus a terminal loss
(3.3)–(3.6), with the control networks *maximising* the same loss — «a minimax optimization problem
similar to an actor-critic setup» (p. 9). Samples come from ad-hoc «stationary distributions»,
e.g. $Y\sim N(0,4)$ rounded, $P^{mid}\sim N(200,100)$, spreads $\sim$ Geometric(0.8)×0.01 (p. 8);
ADAM, ReLU, fixed learning rate $10^{-3}$ (p. 9). The failure modes recorded, in the authors' words:

- **Cause 1 — operator structure:** DGM «struggled to converge in our setting. The primary
  bottleneck lies in the non-local and discontinuous structure of the impulse control operator in
  the QVI, which poses significant challenges for sampling-based learning methods» (pp. 7–8). The
  Al-Aradi et al. extensions for discontinuities «were also tested, but their effectiveness was
  limited by the irregular jump structure induced by the impulse control» (p. 8).
- **Cause 2 — oscillation:** «convergence is oscillatory due to the opposing updates of value and
  policy function» (p. 9).
- **Cause 3 — degenerate decision network:** «the d network was quickly converging to a local
  optima where it always decided not to act»; the authors froze $d_\chi$ for the first 50 epochs
  (p. 9).
- **Cause 4 — dimension:** in the full model «the model did not converge. This is primarily due to
  the extremely high dimensional nature of the problem since 12 mutually exciting Hawkes process
  require a 144 dimensional Markovian representation» (p. 9).

DGM only "worked" in reduced settings: Poisson LOB (net 3×20) and a Hawkes LOB in which **only
market orders are Hawkes** and all other events Poisson (net 10×50), architectures chosen by
comparing losses after 200 epochs (p. 9).

### 9. ⭐⭐ Where DGM converged, it learned a "pump and dump" strategy, which the authors attribute to dynamic arbitrage under exponential kernels (pp. 10–11)

Table 1 (p. 10), out-of-sample, 5-minute episodes, annualised Sharpe and mean |inventory|:

| LOB model | Sharpe | Mean abs. inventory |
|---|---|---|
| Poisson | 4.54 | 0.891 |
| Hawkes — market orders only | 0.78 | 21.56 |
| Full 12-D Hawkes | did not converge | did not converge |

In the MO-only Hawkes case the policy is identical across tests and «rel[ies] on pumping the
market by sending aggressive orders initially and liquidating the inventory on a slow scale»; the
profit is «near zero with a quite high variance» (p. 10). The authors connect it to the dynamic
arbitrage of exponential-kernel Hawkes impact models (Alfonsi–Blanc, arXiv 2015; in the library as
`alfonsi-2016-extension-calibration-hawkes`) and note that no-arbitrage
implies power-law kernels (Jusselin–Rosenbaum 2020), which have no finite Markov representation;
finitely many exponentials bring back «the same curse of dimensionality as the full 12D Hawkes
setting» (p. 11).

### 10. RL approximation: split the QVI into a timing network and an impulse network, trained with PPO (pp. 11–12, 14)

Following Mguni et al.'s auxiliary-control idea, a decision network $d_\chi$ approximates $d_t$
and an action network $u_\xi$ approximates $\sup_\psi V(t,\Gamma(S,\psi))$; «This architectural
separation preserves the natural structure of the quasi variational inequality» while learning the
policy «implicitly through interaction», «bypassing the non-local operator evaluation challenges
that hindered DGM convergence» (p. 12). PPO clipped objective (4.3), $\epsilon\approx0.2$ (p. 14).
Decisions every $\Delta\tau=0.1$ s, episodes $T=300$ s (p. 14).

### 11. The RL state augments the intensities with a truncated event history to compensate for non-exponential kernels (pp. 12–13)

Eq. (4.1): $S_t=(X_t,Y_t,s_t,(n^{(\zeta)}_t/q^{(\zeta)}_t)_\zeta,\lambda^{(i)}_t,H_{t-\tau_H:t})$. The
history window is meant to capture what «the exponential kernel parameterization» does not, since
«power-law kernels do not admit finite-dimensional Markovian representations» (p. 13). How
$\lambda^{(i)}_t$ is computed under the power-law kernel is not stated.

### 12. The RL action set excludes market orders; reward is the discretised objective with a 1 bp terminal-inventory fee (pp. 13–15)

Restricted action set (4.4): $\{LO^a_T,LO^b_T,CO^a_T,CO^b_T\}$ — top-of-book limit orders and
cancellations only; market orders are excluded «to focus policy learning on queue management and
symmetric liquidity provision», explicitly in contrast to the DGM pump-and-dump (p. 15). Reward
(4.2) adds $-\eta Y^2\Delta t$, cash and mark-to-market increments, and impulse cost; transaction
cost (4.5) $0.0001\,|Y_T|P^{mid}_T$ (p. 15). The DGM and RL agents therefore solve **different
control problems** (DGM may send MOs; RL cannot).

### 13. Self-imitation learning is necessary for stable RL; without it RL also pumps and dumps (pp. 15–16, 18)

SIL loss (4.6) imitates replayed actions whose return exceeds the critic's estimate; total loss
(4.7) $=L^{PPO}+\beta_{SIL}L^{SIL}-\beta_{entropy}H$ (p. 16). In Table 2, «Self-Imitation Off» gives
«Pump & Dump» (p. 18); «Stable convergence further requires the inclusion of Self-Imitation, whose
removal induces pathological "Pump & Dump" dynamics» (p. 20).

### 14. ⭐ Headline: PPO+SIL reaches an annualised Sharpe of 31.54 within 60 episodes and behaves like a market maker (pp. 17–18)

With initial cash 2000, $\eta=10$, $T=300$ s: «the trained agent achieves an annualized Sharpe ratio
of 31.54 within only 60 training episodes», with a policy that «symmetrically provides liquidity at
the top of the book and dynamically balances inventory» (p. 17). Versus DGM: RL converges in ~60
episodes while DGM «requires orders of magnitude more iterations without escaping local minima»
(p. 17). Conclusion: the QVI «admits mathematically feasible but economically unrealistic
solutions», the RL formulation with inventory penalty gives «economically meaningful and stable»
ones (p. 18).

### 15. ⭐ Sensitivity and ablation: inventory penalty, costs and intensity features decide profitability (pp. 18–20)

Table 2 (p. 18), OOS annualised Sharpe:

| Setting | Exponential | Power-law |
|---|---|---|
| Standard (η = 10, 1 bp, SIL on) | 31.54 | 28.81 |
| SIL off | Pump & Dump | — |
| Probabilistic agent (baseline) | 7.73 | 20.12 |
| η = 0.1 / 1.0 / 10 / 100 | P&D / P&D / 31.54 / 21.32 | — |
| Cost 1 / 2 / 4 / 8 bp | 31.54 / 3.02 / −5.67 / −19.48 | 28.81 / 2.40 / −25.22 / −107.08 |

Table 3 (p. 20), state ablation:

| Removed | Exponential | Power-law |
|---|---|---|
| none | 31.54 | 28.81 |
| history $H$ | Pump & Dump | 30.85 |
| intensities $\lambda$ | −20.23 | −51.21 |
| spread $s_t$ | Pump & Dump | 17.66 |
| relative queue position | Pump & Dump | Pump & Dump (unprofitable) |

«The strategy remains viable up to transaction costs of 2bps but collapses beyond that threshold»
(p. 20). Removing the intensities makes the agent lose money under both kernels: the Hawkes state
is load-bearing.

### 16. The only non-neural benchmark is a heuristic "probabilistic agent" (pp. 19–20)

It normalises the Hawkes intensities into a distribution over event types, predicts the most
likely next market order side, adjusts quotes or takes liquidity accordingly, and enforces
corrective market orders above an inventory threshold (pp. 19–20, Fig. 4). «the RL agent
consistently outperforms this baseline» (p. 20). No Avellaneda–Stoikov, GLFT or other control
benchmark is run, and no exact optimum exists, so no regret is reported.

### 17. The authors read the exponential kernel itself as a source of the degenerate strategy (p. 21)

«Notably, the Exponential kernel often leads to profitable "Pump & Dump" patterns, whereas this is
rarely observed under the Power-Law kernel, providing some evidence that the DGM's convergence to
such behaviour may be driven by the Exponential kernel specification» (p. 21).

### 18. Future work names SMP, FBSDE, SPDE, delay equations and Volterra control as routes to semi-analytic policies (pp. 21–22)

SMP «potentially yielding closed-form or semi-analytical feedback policies»; FBSDE for scalable
HJB-QVI approximation; «Volterra control [2] methods appear promising to address the seemingly
non-Markovian dynamics induced by Power-Law kernels» (p. 22).

## What this source does not address

- **Several assets.** One asset; "multi-dimensional" means 12 event types.
- **Any closed-form or semi-closed-form reduction.** No linear-ODE, quadratic/Riccati or
  exponential-transform attempt; closed form is dismissed in one sentence (p. 7). For those routes
  see [[glft-2013-model]], [[begv-2021-model]], [[barzykin-2026-hawkes-driven-otc]].
- **Quote-depth control.** Only top-of-book orders; no continuous $\delta$, no fill-probability
  curve $f(\delta)$, so no Hamiltonian $H$ in the GLFT sense.
- **CARA utility.** Risk-adjusted objective only.
- **Regret against an optimum, or a stochastic-control benchmark.** None computed.
- **Hawkes parameter values.** Neither $\mu$, $\alpha_{ij}$ nor $\gamma_{ij}$ are reported; the
  simulator is referenced to [27].
- **Whether the agent's impulses excite the intensities.** Not discussed (see focus item 1).
- **Statistical uncertainty of Sharpe ratios.** No confidence intervals, number of test episodes
  not stated ("several episodes", p. 9).

## Model card

| Field | DGM part (Sec. 3) | RL part (Sec. 4) |
|---|---|---|
| Assets | 1 | 1 |
| Kernel | single exponential per pair $(i,j)$ (eq. 2.11); converged runs: Poisson, or Hawkes for MOs only | exponential and power-law (power-law parameters not given) |
| Excitation | full self + cross across 12 event types (both sides, all order kinds) in the model; MO-only Hawkes in the converged run (self/cross between the two MO types not specified) | full 12-type mutual excitation |
| Who excites the flow | all market events (exogenous); agent impulses update the book via $\Gamma$ but not $\lambda$ as written (inferred, App. B) | same (inferred) |
| Objective | risk-adjusted: $\mathbb E[X_T+Y_TP_T-\kappa Y_T^2-\eta\int Y^2+\sum K]$ (2.1) | same, discretised (4.2), + 1 bp terminal fee (4.5), η = 10 |
| Solution method | HJB-QVI by Deep Galerkin (3 LSTM nets, minimax) | model-free RL: two-network PPO + self-imitation |
| Benchmark | n/a — no reference solution | DGM agent; heuristic "probabilistic agent" |
| Reported numbers | Sharpe 4.54 (Poisson), 0.78 (MO-only Hawkes; |inv| 21.56), full 12-D did not converge | Sharpe 31.54 (exp), 28.81 (PL); probabilistic agent 7.73 / 20.12; annualised from 5-min episodes; no regret |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16.**

### What this focus needs beyond the Kernthesen

1. **Who excites the flow.** The paper never states it. As written, intensities (2.11) count all
   LOB events $N^{(j)}$, and the intervention operator (App. B, pp. 26–27) changes queues, prices,
   cash and inventory but has no $\lambda$ component; the agent's market orders move the mid-price
   (B.16–B.17) but are not added to $N^{(MO)}$. So the model is **flow-driven with an exogenous
   intensity**: the agent's fills (incoming MOs hitting its queue, A.4) are a thinning of the
   exciting market flow, not a separate exciting stream (inference from the equations). The
   "endogenous price impact" of the abstract is book-mechanical, not intensity feedback. This
   matters for [[who-excites-the-flow]]: the paper is a flow-driven example in which, nevertheless,
   no closure is attempted.
2. **Closure.** No linear-ODE or Riccati route is tried. The paper is the clearest case in the
   library of the **"no reduction, solve the full state"** branch: an impulse QVI on a 23-D state
   (DGM) or the full simulator (RL). Its closure obstacles are of a different kind from the
   project's: (a) impulse control makes the operator non-local *in the control* (sup over
   $\Gamma(S,\psi)$), not only in $\lambda$; (b) the state carries queue positions and discrete
   prices. Neither is present in the GLFT/BEGV quote-depth formulation, so the DGM failure is
   **not** evidence about whether a Riccati closure exists under Hawkes flow.
3. **Lift dimension — the transferable point.** The paper's arithmetic «12 mutually exciting Hawkes
   process require a 144 dimensional Markovian representation» (p. 9) follows from a separate decay
   $\gamma_{ij}$ for every pair. With decay depending only on the target ($\gamma_{ij}=\gamma_i$,
   the project's $D=\mathrm{diag}(\beta)$) the exponential lift is $\lambda$ itself, 12-D. For the
   project's $2d$-dimensional cross-asset flow this is the difference between a $2d$- and a
   $(2d)^2$-dimensional lifted state ([[markov-lift]], [[branching-matrix]]) — an argument for the
   common-decay-per-target parameterisation if exact lifted benchmarks are to stay computable
   (inference).
4. **RL vs. exact vs. closed form.** The paper compares a neural-PDE "exact" attempt with RL, but
   the neural PDE did not converge in the full model, and the two methods solve different action
   sets (Kernthese 12). It is therefore **not** a three-way comparison and gives no regret; it
   neither fills nor narrows the project's gap (closed form vs. exact vs. RL on the same model). It
   does document that a DGM attack on the full Hawkes HJB can fail outright, which supports the
   project's choice of a low-dimensional grid-lifted benchmark over a neural PDE.
5. **Cross-asset.** Nothing carries over directly. The full cross-excitation across 12 event types
   (both sides, LO/CO/MO) is the richest single-asset Hawkes structure in the library; the RL
   ablation shows that removing $\lambda$ from the state turns Sharpe negative (−20.23 / −51.21,
   p. 20), consistent with the project's premise that the intensity is a control-relevant state.
6. **Pump and dump as a modelling warning.** Under exponential kernels with MO-only excitation and
   MO impulses allowed, the optimiser exploited price manipulation (pp. 10–11). In the project's
   flow-driven quote-depth setting the maker sends no market orders and cannot move $\lambda$, so
   this channel is closed by construction; it would reopen if the maker's own orders excited the
   flow (fill-driven or order-driven feedback) — a caution for any D1 (fill-driven) design
   (inference).

### Direct quotes (for the draft)

> "Despite its success in solving parabolic PDEs arising in finance and physics, DGM struggled to converge in our setting. The primary bottleneck lies in the non-local and discontinuous structure of the impulse control operator in the QVI, which poses significant challenges for sampling-based learning methods." (pp. 7–8)

> "We note that in the full Hawkes LOB setting (i.e. all 12 events form a mutually exciting Hawkes Process), the model did not converge. This is primarily due to the extremely high dimensional nature of the problem since 12 mutually exciting Hawkes process require a 144 dimensional Markovian representation for the stochastic control framework." (p. 9)

> "We note that there is no SDE representation for general kernels of the Hawkes process." (p. 7)

> "Overall, the comparison suggests that while the QVI formulation admits mathematically feasible but economically unrealistic solutions, the reinforcement learning approximation with an explicit inventory penalty guides the agent towards economically meaningful and stable market making strategies." (p. 18)

### Examples & illustrations (for later drafting)

- Table 1 (p. 10): DGM Sharpe 4.54 (Poisson) → 0.78 (MO-only Hawkes, |inventory| 21.56) → no
  convergence (full Hawkes): a three-step degradation of a neural PDE solver as Hawkes structure is
  added.
- Fig. 2 (p. 11): the identical "pump and dump" inventory path across all test runs.
- Table 3 (p. 20): removing $\lambda$ from the RL state: 31.54 → −20.23 (exp), 28.81 → −51.21 (PL).

### Boundary of this focus

Single-asset LOB, impulse control, top-of-book orders, risk-adjusted objective. All numbers are
annualised Sharpe ratios from 300-second simulated episodes without dispersion statistics, against
a heuristic baseline; no optimum is computed. Statements above about who excites the flow and
about the lift dimension are inferred from the equations, not claims of the authors.

## Mentioned entities

- Models: [[avellaneda-stoikov-model]] (cited as [5]); GLFT-type closed forms only via Fernandez-Tapia–Guéant–Lasry 2016 [20], not [[glft-2013-model]] itself.
- Concepts: [[hawkes-process]], [[markov-lift]], [[branching-matrix]], [[who-excites-the-flow]]
- Sources in this wiki: [[jusselin-2021-persistent-order-flow]] (cited twice, [30] and [31]), [[gasperov-2022-deep-reinforcement-learning]] ([22]).
- Other works (bibkeys / not in library): Sirignano & Spiliopoulos 2018 (DGM); Al-Aradi et al. 2022 (DGM extensions); Alfonsi & Blanc 2015 (dynamic arbitrage); Jusselin & Rosenbaum 2020 (no-arbitrage → power law); Mguni et al. 2023 (auxiliary control); Oh et al. 2018 (SIL); Schulman et al. 2017 (PPO); Guilbaud & Pham 2013; Ricci 2014; Abergel & Jedidi 2013; Øksendal & Sulem 2005; Jain et al. 2024 (compound Hawkes LOB simulator).

## Connections

- Supports [[markov-lift]]: exponential kernels give a finite Markov state, general kernels do not; lift dimension counted as (#types)² under pair-specific decays (pp. 7, 9).
- Supplements [[gasperov-2022-deep-reinforcement-learning]]: both train deep RL on a multivariate exponential-Hawkes LOB simulator; Jain et al. add an impulse-control formulation and a failed neural-PDE comparator.
- Contrast with [[barzykin-2026-hawkes-driven-otc]] and [[martin-2026-market-making-hawkes]] (not cited by the source): low-dimensional reductions / lifted HJB solved where Jain et al. attempt the full LOB state.
- Cites [[jusselin-2021-persistent-order-flow]] for exact HJB under exponential kernels and power-law approximation.
