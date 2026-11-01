---
title: "Aït-Sahalia & Hurd 2016 — Portfolio Choice in Markets with Contagion"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: aitsahalia-2016-portfolio-choice-markets
depth: standard
tags: [portfolio-choice, merton-problem, hawkes, mutual-excitation, cara, log-utility, distorted-intensity, multi-asset, non-market-making]
relations:
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "Asset shocks are an m-dimensional exponential Hawkes process (2.2)–(2.3): «a jump dN_{j,s} … in asset class j … raises each of the jump intensities λ_{l,t}, l = 1, …, m, by a constant amount d_{lj}» (p. 6)."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Stationarity Assumption: Γ = (Γ_lj), Γ_lj = α_j δ_lj − d_lj, «a positive (hence invertible) matrix», then «the intensities λ are stationary processes with bounded moments» (p. 9)."
  - target: markov-lift
    type: mentions
    confidence: extracted
    because: "«Equation 2.3 also reveals that (N, λ) is a 2m-dimensional Markov process, while (λ) alone is an m-dimensional Markov process» (p. 6) — the exponential kernel is its own lift."
  - target: problem-anatomy
    type: supports
    confidence: inferred
    because: "§3b's flow-driven obstruction is a post-/pre-event value ratio that enters the HJB nonlinearly; AH's CARA ansatz L = −exp[−κx]g(λ) produces exactly such a ratio, the distorted intensity h_l(λ) = λ_l g(λ+d_l)/g(λ) (7.12, p. 27), and leaves g as the solution of an implicit nonlinear equation (7.13)–(7.14) (p. 28)."
  - target: who-excites-the-flow
    type: mentions
    confidence: inferred
    because: "Excitation is exogenous: intensity dynamics (3.3) contain no control; the portfolio only scales the wealth jump at each event, eq. (3.5) (pp. 10–11)."
  - target: matrix-riccati-equation
    type: mentions
    confidence: extracted
    because: "The Riccati equations in this paper are those of the affine characteristic function, not of a value function: «the deterministic functions A, B_l satisfy the Riccati equations» (2.6)–(2.7) (p. 9)."
based_on: preprint
---

# Aït-Sahalia & Hurd 2016 — Portfolio Choice in Markets with Contagion

## Bibliographic Details

Aït-Sahalia, Yacine and Thomas Robert Hurd. 2016. "Portfolio Choice in Markets with Contagion."
*Journal of Financial Econometrics* 14(1): 1–28. DOI 10.1093/jjfinec/nbv024.

**Read: arXiv 1210.1598v1 (preprint, submitted 4 Oct 2012; PDF compiled with the date "November 27,
2024"); page/equation numbers follow it.** 31 printed pages + title page. **Printed page = PDF page
− 1** (the title page is unnumbered); all page numbers below are printed numbers. Non-core work;
preprint accepted under the project's preprint policy. The 2012 preprint predates the 2016 journal
version by four years; whether the verification gap for power/exponential utility (Kernthese 14)
was closed in print is **not** known from this copy.

### Notation map (source → project)

| Source | Meaning | Project symbol / remark |
|---|---|---|
| $N_t$, $\lambda_t$ ($m$-dim) | Hawkes shock counts, intensities | $\lambda_t$ |
| $\alpha_l$, $\lambda_{l,\infty}$ | mean-reversion speed, long-run level | $D=\mathrm{diag}(\beta)$, $\mu$ ⚠ source $\beta$ is the impatience rate |
| $d_{lj}$, $d_l$ | jump of $\lambda_l$ from an $N_j$ event; $l$-th column | jump sizes of $K$ (kernel $d_{lj}e^{-\alpha_l u}$) |
| $\Gamma=(\alpha_j\delta_{lj}-d_{lj})$ | stationarity matrix | $D-K$-type matrix ⚠ not BEGV's $\Gamma$ |
| $\omega$, $\pi=\omega X$ | portfolio weights; dollar amounts (CARA section) | no MM analogue (quotes $\delta$) |
| $J_{i,l}\in[-1,0]$, $Z_l\in[0,1]$ | loading of asset $i$ on shock $l$; shock size | — |
| $\Sigma=\sigma\sigma'$, $R$ | diffusive covariance, excess returns | $\Sigma$ |
| $\beta$ | subjective discount ("impatience") | ⚠ clashes with project decay $\beta$ |
| $\gamma$; $\kappa=r\gamma$ | CARA coefficient of $U(x)=-e^{-\gamma x}/\gamma$; wealth coefficient in the value function | $\gamma$ |
| $L(x,\lambda)$, $f$, $g$ | reduced value function; log-case additive part; power/CARA multiplicative part | $\theta(t,q,\lambda)$ (analogue only) |
| $h_l(\lambda)=\lambda_lg(\lambda+d_l)/g(\lambda)$ | distorted intensity | post-/pre-event value ratio × intensity |
| $\mathcal A$ | Markov generator of $\lambda$ (4.6) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract (title page); 1 Introduction (crisis motivation, Fig. 1 filtered US jump intensity, related literature, summary of results) | [i], 1–5 |
| ✓ F1 | 2 Mutually Exciting Jumps (eqs. 2.1–2.3, Figs. 2–3; properties: generator, Dynkin 2.4, stationarity, ergodic 2.5, affine Riccati 2.6–2.7) | 5–9 |
| ✓ F1 | 3 Optimal portfolio selection: 3.1 asset dynamics (3.1–3.3); 3.2 wealth and HJB (3.4–3.11) | 10–13 |
| ✓ F1 | 4 Log-utility investors: 4.1 solution (4.1–4.7, Lemma 1); 4.2 verification (Theorem 1, 4.9–4.15); 4.3 properties | 13–17 |
| ✓ F1 | 5 Additional structure: factor structure (5.1–5.11); 5.1 closed-form solution (5.12–5.23) | 17–21 |
| ✓ F1 | 6 Consequences: Merton/Poisson limits (6.1–6.2), two-asset case (6.3), flight to quality (Fig. 4), home bias, correlations | 22–25 |
| ✓ F1 | 7 Other HARA investors: 7.1 power (7.1–7.9, Remark 1); 7.2 exponential (7.10–7.14) | 25–28 |
| ✓ F1 | 8 Conclusions | 28 |
| — | References | 29–31 |

## Kernthesen

### 1. ⭐ A "Hawkes jump-diffusion" adds drift and Brownian volatility to mutually exciting jumps; the jump part is no longer Lévy (pp. 1–2)

«Unlike models typically employed in finance, the jump part of this model is no longer a Lévy
process since excitation introduces a departure from independence of the increments of the jumps»
(p. 2). Jumps are clustered (self-excitation), systematic (cross-excitation), «but neither exactly
simultaneous nor certain» (p. 2), unlike the simultaneous Poisson jumps of Aït-Sahalia–Cacho-Diaz–
Hurd 2009 (p. 4).

### 2. Empirical motivation: filtered jump intensities of financial-sector indices in 2008–09 (pp. 2–3)

Fig. 1 (p. 3) shows US jump intensity filtered from US, UK, Eurozone and Asian financial-sector
indices, with jumps identified as 3σ-and-above events; the intensity rises with each jump in Fall
2008 and «contain[s] information that is different from other measures of market stress, VIX and
the CDS rate» (p. 2). No estimation procedure is reported in this paper.

### 3. ⭐ Intensities: exponential Hawkes with a full excitation matrix, Markov in $\lambda$ alone (pp. 5–7)

$\lambda_{l,t}=e^{-\alpha_lt}\lambda_{l,0}+(1-e^{-\alpha_lt})\lambda_{l,\infty}+\sum_j\int_0^td_{lj}e^{-\alpha_l(t-s)}dN_{j,s}$ (2.2), i.e.
$d\lambda_l=\alpha_l(\lambda_{l,\infty}-\lambda_l)dt+\sum_jd_{lj}dN_j$ (2.3). «(N, λ) is a 2m-dimensional Markov
process, while (λ) alone is an m-dimensional Markov process» (p. 6). Asymmetric contagion
(e.g. US → rest of world stronger than the reverse) is allowed (p. 4).

### 4. Stationarity, ergodicity and an affine Riccati transform (pp. 7–9)

Generator $[\mathcal Ag](n,\lambda)=\sum_l[\alpha_l(\lambda_{l,\infty}-\lambda_l)\partial_{\lambda_l}g+\lambda_l(g(n+e_l,\lambda+d_l)-g(n,\lambda))]$ (p. 9).
If $\Gamma_{lj}=\alpha_j\delta_{lj}-d_{lj}$ is «a positive (hence invertible) matrix», the intensities are
stationary with bounded moments and an ergodic theorem (2.5) holds (p. 9). The joint characteristic
function is affine, with $A,B_l$ solving Riccati ODEs (2.6)–(2.7) (p. 9).

### 5. Assets: n risky assets loaded on m ≤ n shocks, negative jumps only (pp. 10–11)

$dS_i/S_{i,t-}=(r+R_i)dt+\sum_j\sigma_{ij}dW_j+\sum_lJ_{i,l}Z_{l,t}dN_{l,t}$ (3.2) with $J_{i,l}\in[-1,0]$,
$Z_l\in[0,1]$: «we chose to include only negative asset jumps … since those are the more relevant
ones from both a portfolio risk management perspective and their contribution to mutual
excitation» (p. 10). $W$, $N$, $Z$ are mutually independent (p. 10).

### 6. ⭐ The control does not feed the intensities; each Hawkes event moves wealth and intensity together (pp. 10–13)

Wealth (3.5): $dX=(rX+\omega'RX-C)dt+X\omega'\sigma dW+X\sum_l(\omega'J)_lZ_ldN_l$; the intensity
dynamics (3.3) have constant parameters and no control. The HJB (3.7)/(3.8) contains the joint jump
$\lambda_l\int[L(x+(\omega'J)_lzx,\lambda+d_l)-L(x,\lambda)]\nu_l(dz)$ (p. 12): the event's arrival rate is
exogenous; the control sets only the wealth jump size. The problem is Merton's: infinite-horizon
discounted utility of consumption, $V=e^{-\beta t}L(x,\lambda)$ (pp. 11–12).

### 7. ⭐⭐ Log utility separates additively and is myopic: the policy is the constant-intensity policy evaluated at the current $\lambda_t$ (pp. 13–14, 17)

Ansatz $L=f(\lambda)+\beta^{-1}\log x$ (4.1) gives $C^*=\beta X$ (4.4) and
$\omega^*(\lambda)=\arg\min_\omega\{-\omega'R+\tfrac12\omega'\Sigma\omega-\sum_l\lambda_l\int\log(1+(\omega'J)_lz)\nu_l(dz)\}$ (4.3).
«at any time t, the policy … is precisely the same as the policy when the jump frequency is
treated as a constant λ = λ_t, although that "constant" is changed at each instant» (p. 17). The
policy «does not require knowledge of the function f(λ)» (p. 17).

### 8. ⭐ In the log case the λ-part solves a *linear* nonlocal equation with a Feynman–Kac solution (pp. 14–15)

$[\mathcal Af](\lambda)-\beta f(\lambda)=F(\lambda)$ (4.5), with $F$ depending on $\lambda$ only through the
optimised $K_l(\omega^*(\lambda),\lambda)$; Lemma 1: $f(\lambda)=\int_0^\infty e^{-\beta s}E_{0,\lambda}[F(\lambda_s)]ds$ (4.7),
absolutely convergent by the ergodic property and the growth bound (4.8) (pp. 14–15).

### 9. A verification theorem exists for the log investor only (pp. 15–17)

Theorem 1 (Fleming–Soner III.9 logic): the candidate is a classical HJB solution, the policy is
admissible, and it is optimal in the class satisfying the transversality condition (4.9), under the
stationarity assumption (pp. 15–17).

### 10. Factor structure gives closed-form weights: quadratic first-order conditions for deterministic jumps, cubic for binomial jumps (pp. 17–21)

Block-equicorrelated $\Sigma$ (5.1)–(5.3), loadings $J_l=j_l1_l$ per asset class (5.10). The problem
separates into an alpha part $\omega^\perp_l=R^\perp_l/\kappa_{2l}$ (5.16) and $m$ scalar problems (5.18).
Deterministic jumps → $m$ independent quadratics with explicit root (5.21); binomial jumps → cubics
(5.23) (pp. 20–21).

### 11. ⭐ Flight to quality: one jump in asset 1 cuts the position in every risky asset immediately (pp. 22–23)

The weights are time-varying because they depend on $\lambda_{l,t}$ (p. 22). After a shock to asset 1,
self-excitation lowers the allocation to asset 1 and cross-excitation lowers it for asset 2, «without
waiting for future jumps»; «we believe that this is the first portfolio choice model to actually
capture it in a theoretical setting» (p. 23). Poisson or unconditional-mean intensities give
constant weights (p. 22).

### 12. Partial equilibrium caveats; home bias and crisis correlations (pp. 23–25)

The analysis «assumes among other things that expected returns do not change as jump intensities
change» (p. 23). Cross-sectional excitation lowers the value of international diversification (home
bias, pp. 23–25) and pushes measured correlations toward 1 during excitation episodes (p. 25).

### 13. ⭐ Power utility: multiplicative separation and a distorted intensity (pp. 25–27)

$L=x^\gamma g(\lambda)/\gamma$; the policy is $\omega^*(h(\lambda_t))$ with
$h_l(\lambda)=\lambda_lg(\lambda+d_l)/g(\lambda)$ (7.4), and $g$ solves the implicit nonlinear equation
$[\mathcal Ag]-(\beta-r\gamma)g=G(\lambda;g)$ (7.6)–(7.7), written as a fixed point (7.8)–(7.9). Remark 1
(p. 26): the $\lambda$-dependence of $K$ «is distorted in a g dependent fashion through the mapping h»,
and a second consumption term $(1-\gamma)(\gamma g)^{\gamma/(\gamma-1)}$ «introduces complications». A
contraction argument à la Delong–Klüppelberg 2008 is suggested, not carried out (p. 27).

### 14. ⭐⭐ Exponential (CARA) utility: $L=-\exp[-\kappa x]\,g(\lambda)$ with $\kappa=r\gamma$, the same distortion, an implicit equation, and no verification (pp. 25, 27–28)

For $U(x)=-e^{-\gamma x}/\gamma$ the candidate is $L(x,\lambda)=-\exp[-\kappa x]g(\lambda)$ (p. 27). The HJB
(7.10) contains $L\,g^{-1}[\mathcal Ag]$ and the jump term $L\sum_l\lambda_l\frac{g(\lambda+d_l)}{g(\lambda)}\int(\exp[-\kappa(\pi'J)_lz]-1)\nu_l(dz)$.
Optimal dollar holdings $\pi^*=\pi^*(h(\lambda))$ with the same $h_l=\lambda_lg(\lambda+d_l)/g(\lambda)$ (7.11)–(7.12);
consumption $C^*=\gamma^{-1}(\kappa x-\log g-\log\kappa)$; substitution forces $\kappa=r\gamma$ and leaves
$[\mathcal Ag]-(\beta-r\gamma+r\log(r\gamma))g=g\,[r\log g+K(\pi^*(\lambda),h(\lambda))]$ (7.13)–(7.14) (p. 28).
«Due to the complexity of the underlying HJB conditions, the relevant verification result requires
a lengthy, and perhaps uninformative, analysis that we have not yet completed» (p. 25).

### 15. Claimed: contagion makes power and CARA investors *more aggressive* than non-contagion investors (pp. 5, 28)

«This distortion of intensities has the effect of magnifying the investment in the risky assets: the
contagion investor will go "longer" when the non-contagion investor is long» (p. 5); «power and
exponential investors both adopt more aggressive strategies, characterized by a distortion function
h» (p. 28). No computation in the paper supports the claim (see "Contested" below).

## What this source does not address

- **Market making, fills, quotes.** The control scales jump sizes, not arrival probabilities.
- **Control-dependent intensities.** Intensities are exogenous (3.3).
- **Verification and numerics for power and CARA utility.** Candidates only (p. 25); no solution of
  (7.6) or (7.13) is computed.
- **Finite horizon and terminal inventory penalties.** Infinite-horizon consumption problem only.
- **Non-exponential kernels.** Only the Markov exponential case.
- **Estimation.** The filtered intensities of Fig. 1 come "from the model"; no estimator or
  parameter table is given.

### Contested / inconsistent in the source

- **"More aggressive" (Kernthese 15) [I].** For CARA, $L=-e^{-\kappa x}g<0$; if more intensity of
  negative jumps lowers the value, then $g(\lambda+d_l)>g(\lambda)$ and $h_l>\lambda_l$, i.e. the contagion
  investor acts like a non-contagion investor facing *more* negative jumps, which should shrink a
  long risky position, not magnify it. The same reasoning gives the opposite sign for power utility
  with $\gamma\in(0,1)$ (where $L>0$). The paper asserts the magnification for both without proof or
  numbers; treat it as unverified.
- **Sign of $K$ in (7.11).** As printed, $K(\pi,\lambda)=\kappa\pi'R-\tfrac{\kappa^2}2\pi'\Sigma\pi-\sum_l\lambda_l\int(e^{-\kappa(\pi'J)_lz}-1)\nu_l$
  is concave in $\pi$ and is paired with an argmin; an argmax (or a flipped sign) is presumably meant.
- Minor: index typo $\partial V/\partial\lambda_i$ in (3.7); "$\lambda\in\mathbb R^n_+$" where $\mathbb R^m_+$ is meant
  (pp. 12, 14).

## Model card

- **Assets:** $n$ risky + 1 riskless, $m\le n$ Hawkes shocks; explicit two-asset example (6.3).
- **Kernel:** exponential Hawkes (Markov in $\lambda$).
- **Excitation:** self and cross between shock components, asymmetric allowed; cross-asset via $d$
  and the loading matrix $J$.
- **Who excites the flow:** exogenous price shocks; the control never affects an intensity. n/a in the
  fill-/flow-driven sense — no orders.
- **Objective:** infinite-horizon expected utility of consumption — log (solved, verified), power and
  CARA (candidates).
- **Solution method:** HJB; closed form (log, with factor structure); fixed-point characterisation
  (power, CARA).
- **Benchmark:** Merton (pure diffusion), Poisson jumps, the "non-contagion investor" with constant
  intensities.
- **Reported numbers:** none (illustrative sample-path figures only).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

*Read as a non-market-making source: what its control machinery says about the closures.*

**Carries Kernthesen 3, 4, 6, 7, 8, 13, 14, 15.**

### What this focus needs beyond the Kernthesen

1. **Does the control affect the intensities? No.** (3.3) has constant parameters; the control
   $\omega$ (or $\pi$) appears only in the wealth jump $X(\omega'J)_lZ_l$ (3.5). Every Hawkes event
   jumps wealth *and* intensity at the same instant (HJB 3.7). There is no "unfilled" event: the
   jump probability is exogenous, its size is controlled.
2. **The CARA separation and where the ratio comes from [D].** Insert $L=-e^{-\kappa x}g(\lambda)$ into
   the jump term of (3.8): $L(x+\pi'J_lz,\lambda+d_l)-L(x,\lambda)=L(x,\lambda)\big[\frac{g(\lambda+d_l)}{g(\lambda)}e^{-\kappa(\pi'J)_lz}-1\big]$.
   Splitting $-1=-\frac{g(\lambda+d_l)}{g(\lambda)}+(\frac{g(\lambda+d_l)}{g(\lambda)}-1)$ gives the two pieces of
   (7.10): the generator part $\lambda_l(g(\lambda+d_l)-g(\lambda))/g$ (inside $L g^{-1}\mathcal Ag$) and the
   control part weighted by $h_l(\lambda)=\lambda_lg(\lambda+d_l)/g(\lambda)$. Because the wealth jump and the
   intensity jump are **simultaneous**, the post-event value enters as the *ratio*
   $g(\lambda+d_l)/g(\lambda)$, which multiplies the control-dependent term.
3. **Why it stays nonlinear [I].** After multiplying by $g$, for a *fixed* $\pi$ the equation is linear
   in the values $(g(\lambda),g(\lambda+d_1),\dots,g(\lambda+d_m))$. The nonlinearity enters only through
   (a) the optimiser $\pi^*(h(\lambda))$, which depends on the ratio, and (b) the consumption term
   $r g\log g$. The optimised term $\sup_\pi\{\cdot\}$ is a degree-one homogeneous but non-linear
   function of $(g(\lambda),g(\lambda+d))$, so no power substitution $g=w^p$ linearises it in general —
   unlike GLFT, where the optimiser's dependence on the ratio is a pure power. In the project's §3b
   ([[problem-anatomy]]) the flow-driven obstruction is the same object: the ratio
   $v(q,\lambda)/v(q,\lambda^{+j})$ inside the optimised Hamiltonian. AH show this ratio structure is
   generic for CARA/power problems with Hawkes jumps; they do not claim, and do not show, a
   linearising transform. Relevance for D1 (fill-driven CARA linearisation): AH is **not** a
   counterexample — its nonlinearity comes from a continuously controlled jump *size*, which a
   GLFT fill (fixed size, controlled probability $\Lambda e^{-k\delta}$) does not have. It does show
   that the "distorted intensity" $h$ is where any exact linearisation must succeed or fail.
4. **The exact linear closure exists here, but only for log utility.** Log utility separates
   additively; then $\lambda$ enters a **linear** nonlocal equation (4.5) whose solution is a Feynman–Kac
   integral (4.7), and the policy is myopic (Kernthesen 7–8). This is the portfolio analogue of an
   exact linear closure: the value's $\lambda$-part is linear because the log investor's control
   problem decouples from the future dynamics of $\lambda$.
5. **Riccati content.** The only Riccati equations are the affine transform (2.6)–(2.7) of the
   Hawkes process itself, not a value-function closure. No quadratic-in-state ansatz appears (CARA
   in wealth gives an exponential, not quadratic, value).
6. **What carries over to several assets with cross-asset excitation [I].** The distortion is
   per-shock: $h_l$ involves $g$ at $\lambda+d_l$, the column $d_l$ spreading one shock's excitation
   over all intensities. With cross-excitation ($d_{jl}\ne0$, $j\ne l$), a shock in class $l$ changes
   the distorted intensity of every class through $g(\lambda+d_l)$. The factor structure (Sec. 5)
   makes the log policy separate across asset classes; it does not make $g$ separate, since $g$ lives
   on all of $\mathbb R^m_+$. The flight-to-quality mechanism (Kernthese 11) is the portfolio image of a
   cross-asset quote reaction to a burst in another asset.

### Direct quotes (for the draft)

> "In other words, a jump dN_{j,s}, occurring at time s ∈ [0, t) in asset class j = 1, . . . , m, raises each of the jump intensities λ_{l,t}, l = 1, . . . , m, by a constant amount d_{lj}." (p. 6)

> "We can however, search for candidate optimal strategies that solve the reduced HJB equation (3.8) in the form L(x, λ) = −exp[−κx]g(λ) for some positive function g, and then attempt to interpret the result." (p. 27)

> "Due to the complexity of the underlying HJB conditions, the relevant verification result requires a lengthy, and perhaps uninformative, analysis that we have not yet completed." (p. 25)

> "In particular, at any time t, the policy (ω∗t, C∗t, t) is precisely the same as the policy when the jump frequency is treated as a constant λ = λt, although that "constant" is changed at each instant." (p. 17)

> "We find that under the contagion conditions of the model, the investor will choose a portfolio that is optimal for a non-contagion investor who has a specific distorted value of the intensities, which we characterize." (p. 5)

### Examples & illustrations (for later drafting)

- Figs. 3–4 (pp. 8, 24): two asset classes, a jump in $S_1$ at $T_1$ raises $\lambda_1$ and $\lambda_2$; both
  weights $\omega_1,\omega_2$ drop at once — a visual for cross-asset excitation driving a cross-asset
  control response.
- (5.21)/(6.3) (pp. 21–22): the explicit root of a quadratic as the log-optimal weight, with $\lambda_{l,t}$
  under the square root — an example of a closed form that is time-varying only through the current
  intensity.

### Boundary of this focus

AH is a consumption–portfolio problem with exogenous Hawkes shocks. The comparisons with GLFT,
BEGV, §3b and D1 are the project's analogy ([I]/[D]), not claims of the source. The CARA and power
results are formal candidates without verification (p. 25).

## Mentioned entities

- Concepts: [[hawkes-process]], [[branching-matrix]], [[markov-lift]], [[matrix-riccati-equation]], [[who-excites-the-flow]]
- Models: [[glft-2013-model]] (comparison in the focus block only; not cited by the source)
- Synthesis: [[problem-anatomy]]
- Other works (bibkeys): `hawkes-1971-spectra-self-exciting`, `errais-2010-affine-point-processes`. Cited but not in the library: Aït-Sahalia–Cacho-Diaz–Hurd 2009 (Poisson systematic jumps), Merton 1971/1976, Delong–Klüppelberg 2008 (fixed-point method), Fleming–Soner 2006, Goll–Kallsen 2000, Bowsher 2007.

## Connections

- Built on by: [[shen-2022-mean-variance-portfolio]] (same market model, MV objective, SMP/BSDE; LQ quadratic value with λ-dependent coefficient).
- Supports (by analogy, not cited): [[problem-anatomy]] §3b — the post-/pre-event ratio as the source of nonlinearity in a CARA HJB with Hawkes jumps.
- Compare: [[glft-2013-model]] (CARA closure made exact by a power substitution, Poisson flow).
