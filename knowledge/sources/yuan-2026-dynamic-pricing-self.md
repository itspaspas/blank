---
title: "Yuan, Du & Hu 2026 — Dynamic Pricing Under Self-Exciting Arrival Processes"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: yuan-2026-dynamic-pricing-self
depth: standard
tags: [dynamic-pricing, revenue-management, hawkes, nonlinear-hawkes, fill-driven, risk-neutral, hjb, affine-closure, fluid-approximation]
relations:
  - target: who-excites-the-flow
    type: supports
    confidence: extracted
    because: "Base model is fill-driven: «the stochastic arrival intensity is stimulated with an immediate boost after any purchase» (p. 1); the extension where non-buyers also excite (α_O = α) makes the price constant: «If αO = α, the optimal intensity is constant» (Lemma 3, p. 21)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Arrivals follow a «generalized self-exciting process (see, e.g., Brémaud and Massoulié 1996 and Zhu 2015)», Definition 1, intensity ϕ + h(Σ α e^{-β(t-t_i)}) (p. 10)."
  - target: markov-lift
    type: builds-on
    confidence: extracted
    because: "Exponential kernel gives a one-dimensional Markov state, the excitement level x_t with dx_t = -βx_t dt + α dN_t (Lemma 1, p. 11), «shown to be the only sufficient statistic for our problem» (p. 1)."
  - target: problem-anatomy
    type: supports
    confidence: inferred
    because: "Reconstruction (not stated by the authors): with exponential demand the fill-driven HJB (3) is linearised by w = e^{V}, while the non-buyer-excitation HJB (5) is not — the risk-neutral pricing mirror of problem-anatomy §3b."
based_on: preprint
---

# Dynamic Pricing Under Self-Exciting Arrival Processes

## Bibliographic Details

Yuan, Quan; Du, Longyuan; Hu, Ming. 2026. "Dynamic Pricing Under Self-Exciting Arrival
Processes." *Operations Research* 74(3): 1408–1424. doi:10.1287/opre.2024.1172.

**Read:** author preprint (49 pp., no date or version stamp), not the Operations Research
version; page and equation numbers on this page follow the preprint. PDF page = printed page.
Main text pp. 1–31, online appendix with proofs pp. 34–49. Accepted under the preprint policy
(non-core work).

### Notation map (source → project)

| Source | Meaning in source | Project symbol / remark |
|---|---|---|
| $\varphi$ | organic (baseline) arrival rate | $\mu$ |
| $\alpha$, $\beta$ | jump of the excitement level per purchase, decay | $\alpha$ (kernel amplitude), $\beta$ |
| $x_t=\sum_{t_i<t}\alpha e^{-\beta(t-t_i)}$ | "excitement level", Hawkes memory driven by **purchases** only | lifted state, cf. $\lambda_t-\mu$ |
| $h(\cdot)$ | strictly increasing self-exciting (link) function: nonlinear Hawkes | none |
| $\lambda$, $\lambda(p)$ | **purchase probability** = decision variable | ⚠ the project's $\lambda_t$ is an intensity; here $\lambda$ plays the role of the fill probability $f(\delta)$ |
| $\Lambda_t=\lambda_t(\varphi+h(x_t))$ | purchase (fill) rate | fill intensity; ⚠ not the GLFT amplitude $\Lambda$ |
| $r(\lambda)=\lambda(p(\lambda)-c)$ | profit rate per arriving customer | analogue of $H$ (before adding the continuation term) |
| $V_t(x)$ | value function (expected profit-to-go) | $\theta(t,\lambda)$ without inventory |
| $\mu_t,\omega_t$ | slope and intercept of the affine value function (Cor. 1) | ⚠ $\mu_t$ is not a baseline intensity |
| $n$ | scale of the arrival rate in Section 4 | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract | 1 |
| ✓ F1 | 1 Introduction (JD.com motivation, Fig. 1; summary of results) | 1–5 |
| — | 2 Literature review (Hawkes in OM, correlated arrivals in RM, network-effect pricing, asymptotic RM) | 6–9 |
| ✓ F1 | 3.1 The model (Definition 1, eq. 1, Assumption R, objective eq. 2) | 9–11 |
| ✓ F1 | 3.2 Structure of optimal policy (Lemma 1, Prop. 1 HJB eq. 3, Example 1, Lemma 2, Props. 2–3, Theorems 1–2, Corollary 1 eq. 4) | 11–15 |
| ✓ F1 | 3.3 Optimal price trend (Theorem 3, submartingale) | 16 |
| ✓ F1 | 4 Asymptotic analysis: scaling by $n$, Props. 4–5, deterministic heuristic, Theorem 4 | 16–20 |
| ✓ F1 | 5.1 General information spreading (non-buyers excite; eq. 5, Lemma 3, Prop. 6, Fig. 4) | 20–23 |
| ✓ F1 | 5.2 Discrete prices (Theorems 5–6) | 23–24 |
| ✓ F1 | 5.3 Multiple products (eq. 6) | 24–25 |
| ✓ F1 | 6 Numerical study (JD.com calibration; myopic, static, deterministic heuristics; Figs. 5–7, Algorithm 1) | 25–30 |
| ✓ F1 | Conclusion, future research | 30–31 |
| ✓ F1 (Prop. 1, Thm. 2, Cor. 1 proofs) | Online appendix A, proofs | 34–49 |

## Kernthesen

### 1. ⭐ Arrivals self-excite through purchases only, with a nonlinear link and exponential decay (pp. 9–10)

Organic customers arrive at rate $\varphi$; each purchase at $t_i$ informs further customers at rate
$\alpha e^{-\beta(t-t_i)}$; informed customers bring influenced customers at rate
$h(\sum_{t_i<t}\alpha e^{-\beta(t-t_i)})$. Definition 1 (p. 10): potential customers arrive with
$\Phi_t(H_t)=\varphi+h\big(\sum_{t_i<t}\alpha e^{-\beta(t-t_i)}\big)$, $h$ strictly increasing — a
nonlinear Hawkes process in the sense of Brémaud–Massoulié. Only **purchase** times $t_i$ enter;
an arriving customer who does not buy leaves no trace. Each arrival buys with probability
$\lambda(p)$, so the purchase rate is $\Lambda_t(p)=\lambda(p)(\varphi+h(\cdot))$ (eq. 1, p. 10).

### 2. The decision variable is the purchase probability; the profit rate must be strictly concave in it (pp. 10–11)

Following Gallego–van Ryzin, the seller chooses $\lambda\in[\underline\lambda,\bar\lambda]$ and
the price is $p(\lambda)$. Assumption (R): $\lambda(p)$ differentiable and invertible; the profit
rate $r(\lambda)=\lambda(p(\lambda)-c)$ «is differentiable, bounded and strictly concave in λ»
(p. 11). The objective is **risk-neutral** expected profit,
$V_t=\max_u\mathbb E_u\int_t^T(p(\lambda_s)-c)\,dN_s$ (eq. 2, p. 11). No inventory, no capacity,
no risk penalty.

### 3. ⭐⭐ The excitement level is a one-dimensional Markov state and the HJB is a first-order transport-jump PDE (p. 11)

$x_t:=\sum_{t_i<t}\alpha e^{-\beta(t-t_i)}$ satisfies $dx_t=-\beta x_tdt+\alpha dN_t$ (Lemma 1),
$N$ with intensity $\lambda_t(\varphi+h(x_t))$. Proposition 1 (eq. 3):
$$-\partial_tV_t(x)+x\beta\,\partial_xV_t(x)=(h(x)+\varphi)\max_\lambda\{r(\lambda)+\lambda(V_t(x+\alpha)-V_t(x))\},\qquad V_T(x)=0.$$
$V_t(x+\alpha)-V_t(x)$ «can be viewed as the future impact of one additional purchase» (p. 12). The
excitation jump sits **inside** the Hamiltonian's argument: it is a fill-driven equation.

### 4. ⭐ No closed form in general; closed form for exponential demand, linear $h$, no decay (p. 12)

«While Equation (3) in general does not have close-form solutions, we illustrate the optimal
solution through the following special case» (p. 12). Example 1: $\beta=0$, $c=0$, $h(x)=x$,
$\lambda(p)=ae^{-p}$ gives $\lambda^*_t(x)=a/(\alpha a(t-T)+e)$,
$p^*_t(x)=\ln(\alpha a(t-T)+e)$ and
$V_t(x)=\tfrac1\alpha(1-\ln(\alpha a(t-T)+e))x-\tfrac\varphi\alpha\ln(\alpha a(t-T)+e)$ (p. 12):
price depends on time only. No derivation is given for the example.

### 5. Without excitation the optimal price is constant (p. 12)

Lemma 2: if $\alpha=0$ or $\beta\to\infty$ the optimal purchase probability is
$\lambda^*=\arg\max r(\lambda)$, constant — the Poisson benchmark.

### 6. Value increases in $x$ and $\alpha$, decreases in $t$ and $\beta$; the optimal purchase rate increases in $x$ (p. 13)

Proposition 2 (monotonicity of $V$) and Proposition 3: the optimal purchase **rate**
$\Lambda^*_t(x)=\lambda^*_t(x)(\varphi+h(x))$ increases in $x$ «without any specific assumptions about
the self-exciting function» (p. 13), even when the price rises with $x$.

### 7. ⭐ Low prices early, higher later (p. 13); a submartingale price path when there is no decay (p. 16)

Theorem 1: $\lambda^*_t(x)$ decreases and $p^*_t(x)$ increases in $t$ for every $x$. Theorem 3:
if $1/g(p)$ (Mills ratio) is convex and $\beta=0$, $\mathbb E[p^*_s(x_s)\mid\mathcal F_t]\ge p^*_t(x_t)$
(p. 16). Interpretation: early sales buy future arrivals.

### 8. ⭐⭐ The shape of $h$ decides the curvature of $V$ and the sign of the price response to excitement (p. 14)

Theorem 2: convex $h$ → $V$ strictly convex in $x$, $\lambda^*$ increases and $p^*$ **decreases** in
$x$ ("growth" market); concave $h$ → $V$ strictly concave, $p^*$ increases in $x$ ("maturity");
linear $h$ → «$V_t(x)$ is linear in x, and $\lambda^*_t(x)$ (hence, $p^*_t(x)$) is independent of x»
(p. 14).

### 9. ⭐⭐ Linear $h$: an affine ansatz in the excitement level closes the HJB into two ODEs (p. 15; proof pp. 40–41)

Corollary 1: for $h(x)=h_1x+h_0$, $V_t(x)=\mu_tx+\omega_t$ with
$\tfrac{d\mu_t}{dt}=\beta\mu_t-h_1\max_\lambda\{r(\lambda)+\lambda\alpha\mu_t\}$ and
$-\tfrac{d\omega_t}{dt}=(h_0+\varphi)\max_\lambda\{r(\lambda)+\lambda\alpha\mu_t\}$ (eq. 4 as derived in the
proof, p. 40), $\mu_T=\omega_T=0$; the optimal purchase probability
$\lambda^*_t=\arg\max\{r(\lambda)+\lambda\alpha\mu_t\}$ «is independent of x» (p. 15). Proof: the
coefficients of $x$ and of the constant are matched (p. 40). The closure works because the jump
$V(x+\alpha)-V(x)=\alpha\mu_t$ does not depend on $x$ and the intensity is affine in $x$. No change
of variables is used.

### 10. Scaling: with Lipschitz $h$ the excitement level is $O(n)$ and the optimal control concentrates (p. 17)

Arrival rate scaled by $n$: $\Lambda^{(n)}_t=n\lambda_t[\varphi+h(x_t/n)]$ (p. 16). Proposition 4:
Lipschitz $h$ ⇒ $\mathbb E[x_t]=O(n)$ for any Markov policy. Proposition 5: under the optimal policy
$\mathrm{Var}[\lambda^*_t]=O(1/n)$, $\mathrm{Var}[x^*_t]=O(n)$ (p. 17).

### 11. ⭐ The open-loop fluid policy loses only $O(1)$ — unlike capacitated RM (pp. 18–20)

The deterministic problem $\max\int_0^Tn\lambda_t[\varphi+h(x_t/n)](p(\lambda_t)-c)dt$, $\dot x_t=\alpha n\lambda_t[\varphi+h(x_t/n)]-\beta x_t$
(p. 19) is solved by forward–backward sweep (Algorithm 1, p. 29). Theorem 4: constants
$K_1,K_2$ independent of $n$ with $|V^{DH}(n)-V^d(n)|\le K_1$ and $|V^*(n)-V^d(n)|\le K_2$ (p. 19),
versus $O(\sqrt n)$ / $\Theta(\ln n)$ in the capacitated problem (p. 20). The key is that no
capacity constraint makes the variance of the control blow up near $T$.

### 12. ⭐⭐ If non-buyers excite as well, the HJB gains a jump term outside the maximisation; if they excite equally, the control decouples (pp. 20–21)

With non-purchasers exciting at $\alpha_O\le\alpha$ (p. 20), eq. (5):
$-\partial_tV+x\beta\partial_xV=(h(x)+\varphi)\big[\max_\lambda\{r(\lambda)+\lambda(V(x+\alpha)-V(x+\alpha_O))\}+V(x+\alpha_O)-V(x)\big]$
(p. 21). Lemma 3: «If αO = α, the optimal intensity is constant … If αO = 0, the optimal intensity
is the one from the base model» (p. 21). Proposition 6: $V$ increases in $\alpha_O$ (p. 22); the
optimal intensity can be non-monotone in $\alpha_O$ (Fig. 4, p. 22–23).

### 13. Finite price menus are not asymptotically optimal (pp. 23–24)

Theorem 5 gives threshold structures (in $x$ for convex $h$, in $t$ for linear $h$); Theorem 6: any
finite-price heuristic has $V^*(n)-V^u(n)=\Theta(n)$ (p. 24), because the fluid optimum is
non-stationary in time.

### 14. ⭐ Multiple products share one excitement level; no cross-product excitation matrix (pp. 24–25)

With $M$ products, purchases of any product feed one $x=\sum_n\sum_{t^n_i<t}\alpha e^{-\beta(t-t^n_i)}$,
so (eq. 6, p. 24) is still a scalar-state HJB with a vector control; FOC equalises marginal profit
rates across products («loss leader», p. 25). Separate organic streams with cross-product
excitation are listed as future research (p. 31).

### 15. Ignoring excitation costs up to ~13–20% of profit; the fluid heuristic loses < 0.02% (pp. 25–30)

JD.com sunscreen calibration: $\varphi=0.392$, $\tilde\alpha=0.09$, $\beta=0.11$, normalised
$\alpha\approx0.23$, $T=600$ min, $h(x)=x+0.001x^2$, uniform valuations, semi-Lagrangian HJB solver,
$\Delta x=0.01$, $\Delta t=0.1$ (p. 25). Myopic (Poisson) pricing loses «up to roughly 13%» (p. 26),
up to 20% at $\beta=0.1$, below 1% at $\beta=0.3$, up to 18% at $\alpha=0.25$ (pp. 26–27). Static
pricing ≈ 5% (p. 27). The deterministic heuristic loses < 0.02%, 0.012%, 0.009% for $x=0,20,40$
(p. 29).

## What this source does not address

- **Market making, inventory, two-sided quotes.** The state has no inventory; a sale is pure revenue.
- **Risk aversion / CARA.** Risk-neutral throughout; no exponential utility.
- **Mutual excitation across streams.** Multi-product excitation is pooled into one scalar $x$
  (eq. 6); a matrix kernel is future research (p. 31).
- **Non-exponential kernels.** Only exponential decay (one-dimensional lift).
- **Any exponential change of variables.** The paper never transforms $V$; see focus item 1 for
  what such a transform would do here.
- **Exact numbers for the HJB error.** The numerical HJB solution is the benchmark; no regret
  against an independent solver.

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

Read as an outside-MM source: what its control machinery says about exponential transforms, affine
closures, lifts, and whether the control feeds the intensity.

**Carries Kernthesen 1, 3, 4, 8, 9, 12, 14.**

### What this focus needs beyond the Kernthesen

1. **D1 analogue (fill-driven exponential linearisation): absent from the paper, but implicit in
   its exponential-demand case [D].** The authors use no transform; their closures are (i) the
   affine-in-$x$ ansatz for linear $h$ (Cor. 1) and (ii) a numerical semi-Lagrangian scheme. However,
   with exponential demand $\lambda(p)=ae^{-p}$ (their Example 1) the Hamiltonian is
   $\max_\lambda\{\lambda\ln(a/\lambda)-c\lambda+\lambda\Delta\}=ae^{-1-c}e^{\Delta}$ with
   $\Delta=V(x+\alpha)-V(x)$ (unconstrained optimum $\lambda^*=ae^{\Delta-1-c}$). So (3) becomes
   $-\partial_tV+\beta x\partial_xV=(h(x)+\varphi)\,ae^{-1-c}\,e^{V(x+\alpha)-V(x)}$, and with
   $w=e^{V}$ (multiply by $w$):
   $$-\partial_tw+\beta x\,\partial_xw=ae^{-1-c}\,(h(x)+\varphi)\,w(t,x+\alpha),\qquad w(T,x)=1,$$
   a **linear** transport-jump equation in $(t,x)$ **for any increasing $h$** — the risk-neutral
   pricing counterpart of the GLFT substitution under fill-driven excitation (problem-anatomy §3b,
   right column). Example 1 is consistent with it: for $h=x$, $\beta=0$, $c=0$, the ansatz
   $w=e^{\mu_tx+\omega_t}$ gives $\dot\mu=-(a/e)e^{\alpha\mu}$, solved by $e^{-\alpha\mu}$ linear in $t$,
   which reproduces $p^*_t=\ln(\alpha a(t-T)+e)$. Caveat: this holds only while the cap
   $\lambda\le\bar\lambda$ (purchase probability ≤ 1) does not bind; $\Delta$ grows with the horizon.
2. **The flow-driven obstruction appears in the paper's own extension [D].** In eq. (5) (Kernthese
   12), non-buying arrivals also move $x$, and the term $V(x+\alpha_O)-V(x)$ sits outside the
   maximisation. With $w=e^V$ and exponential demand the right-hand side becomes
   $ae^{-1-c}\,w(x)w(x+\alpha)/w(x+\alpha_O)+w(x)\ln\!\big(w(x+\alpha_O)/w(x)\big)$, nonlinear. This is
   the same mechanism as the proposal's statement that «the value of an order that does not fill
   the market maker enters nonlinearly» (problem-anatomy §3b, left column). At $\alpha_O=\alpha$
   (pure flow-driven) the control decouples from the intensity and the optimal price is myopic
   and constant (Lemma 3, p. 21); this matches Barzykin's observation that flow-driven forecasts
   are quote-independent ([[barzykin-2026-hawkes-driven-otc]], p. 9).
3. **Affine-in-excitation closure ↔ D2.** Corollary 1 is the scalar, risk-neutral version of an
   ansatz whose coefficients are functions of time only, because intensity is affine in $x$ and
   the value jump is $x$-independent. With an inventory and a quadratic-in-$q$ ansatz
   (BEGV), the coefficients would have to depend on $x$ (D2), and fill-driven jumps in $x$ and $q$
   together would break the closure ([[bergault-2024-price-aware-automated]], p. 17). The paper
   says nothing about this; it is the project's reading.
4. **Multi-asset / cross-excitation.** Not carried: eq. (6) pools all products into one scalar
   excitation, so there is no matrix kernel and no cross-product asymmetry. *Inference:* with a
   vector state $x\in\mathbb R^M$ (product-specific kernels) and exponential demands per product,
   the transform $w=e^V$ still linearises the fill-driven HJB, because each product's Hamiltonian is
   $a_me^{-1-c_m}e^{V(x+\alpha_m)-V(x)}$ — the cross-excitation enters only through the shift
   vector $\alpha_m$ and the intensity $\varphi_m+h_m(x)$. The linear equation then lives on an
   $M$-dimensional lifted grid; linearity does not give a closed form.

### Direct quotes (for the draft)

> "We show that the optimal pricing policy depends on the current time and excitement level, which measures the currently accumulated influence that previously informed customers exert and is shown to be the only sufficient statistic for our problem." (p. 1)

> "While Equation (3) in general does not have close-form solutions, we illustrate the optimal solution through the following special case." (p. 12)

> "If h(x) is linear, Vt(x) is linear in x, and λ∗t(x) (hence, p∗t(x)) is independent of x." (Theorem 2(iii), p. 14)

> "Lemma 3. If αO = α, the optimal intensity is constant, λO∗(x) = arg max0≤λ≤λ(0){r(λ)}. If αO = 0, the optimal intensity is the one from the base model, λO∗(x) = λ∗(x)." (p. 21)

> "Even with multiple products that contribute to exciting customers, the system dynamics are similar to those of a single product, as we can capture the system state by a single-dimensional exciting level x." (p. 25)

### Examples & illustrations (for later drafting)

- Example 1 (p. 12, Fig. 3): with exponential demand the price path $\ln(\alpha a(t-T)+e)$ rises in
  time and is flat in $x$ — a one-line closed form that the $w=e^V$ reading reproduces.
- Lemma 3 (p. 21) as a two-line illustration of "who excites the flow": buyers-only excitation →
  price trades off current margin against future arrivals; everyone excites equally → myopic price.
- Myopic loss up to ~13% (p. 26) vs fluid-heuristic loss < 0.02% (p. 29): ignoring excitation is
  costly, ignoring its randomness is nearly free in this scaling.

### Boundary of this focus

The source is a risk-neutral pricing problem without inventory; the linearisation in focus items 1–2
is the project's derivation from eqs. (3) and (5), not a claim of the authors, and it is not checked
against the published OR version. Nothing here speaks to CARA utility or to a quadratic
inventory closure.

## Mentioned entities

- Concepts: [[hawkes-process]], [[markov-lift]], [[who-excites-the-flow]]
- Synthesis: [[problem-anatomy]] (§3b)
- Other works (bibkeys): `hawkes-1971-spectra-self-exciting`; not in the library: Brémaud & Massoulié
  1996, Gallego & van Ryzin 1994, Wang & Wang 2022, Jasin 2014, Ajorlou et al. 2018, Daw & Pender 2018,
  Zhu 2015.

## Connections

- Supports (fill-driven case, inferred): [[problem-anatomy]] §3b — exponential linearisation survives
  when only fills excite and breaks when non-fills excite too.
- Compare: [[gueant-2013-dealing-inventory-risk]] (GLFT transform; here the risk-neutral analogue
  $w=e^V$ is implicit), [[barzykin-2026-hawkes-driven-otc]] (flow-driven convention, forecast
  independent of quotes), [[bergault-2024-price-aware-automated]] (fill-driven excitation breaks the
  quadratic closure).
- Sibling ingest of this task: [[chen-2026-optimal-trade-execution]] (control feeds the intensity,
  closure via deterministic risk-neutral expectations instead of an HJB).
