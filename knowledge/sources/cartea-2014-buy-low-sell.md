---
title: "Cartea, Jaimungal & Ricci 2014 — Buy Low, Sell High: A High Frequency Trading Perspective"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: cartea-2014-buy-low-sell
depth: deep
tags: [market-making, hawkes, mutually-exciting, single-asset, limit-order-book, short-term-alpha, adverse-selection, asymptotic-expansion, feynman-kac, high-frequency-trading]
relations:
  - target: cartea-jaimungal-ricci-model
    type: supports
    confidence: extracted
    because: "This is the defining paper of the model: «this paper is the first to incorporate such effects into optimal control problems related to AT» (p. 418); MO intensities (2.2), LOB shape (3.1), short-term alpha (4.1), objective (5.2)."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«Multivariate Hawkes processes have recently been used in the financial econometrics literature to model clustering in trade arrival» (p. 418); bivariate exponential mutually exciting intensities, eq. (2.2a)-(2.2b), p. 421."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Lemma 2.1 (p. 421): the mean future rate «remains bounded for all u >= t if and only if beta > rho(eta + nu)»; the 2x2 matrix A has eigenvalues beta - (eta +/- nu) rho (p. 437)."
  - target: intensity-forecast
    type: builds-on
    confidence: extracted
    because: "«define the mean future activity rate m_t(u) = E[lambda_u | F_t]» (p. 421), solved in closed form by a matrix exponential (B.2), p. 436, and integrated against (T - u) to give the inventory term b_phi, (C.8), p. 441."
  - target: markov-lift
    type: mentions
    confidence: inferred
    because: "No lift is discussed: the single exponential decay makes (lambda, kappa, alpha) themselves Markov states of the HJB (5.3)-(5.4), p. 426-427 - the trivial one-factor case of a lift."
  - target: matrix-riccati-equation
    type: mentions
    confidence: inferred
    because: "Contrast: the first-order expansion in varsigma = max(phi, alpha, E[eps]) yields linear Feynman-Kac PIDEs (B.5a)-(B.5d), p. 438, and linear affine ODEs (C.6), p. 441; the quadratic (Riccati) term in inventory is of second order and is dropped."
  - target: hamiltonian-quadratic-approximation
    type: mentions
    confidence: inferred
    because: "Alternative closure route: CJR expand the value function and quotes around the risk-neutral quote delta_0 in small parameters (5.6)-(5.7), p. 427, rather than expanding the Hamiltonian in the shadow price as BEGV/Barzykin do."
  - target: shadow-price
    type: mentions
    confidence: inferred
    because: "The control enters through the post-MO finite difference S_qlambda g - S_lambda g in (5.8) and (C.1a), pp. 427, 439 - a shadow price evaluated after the intensity jump; the source does not use the term."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Ref. [20] (Gueant-Lehalle-Fernandez-Tapia 2013): algorithms «designed to manage inventory risk [11], [20]» (p. 419); also among reduced-form fill models «[23], [3], [5], [11], and [20]» (p. 422)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«more recently Avellaneda and Stoikov [3] studied the optimal HF submission strategies of bid and ask LOs» (pp. 416-417)."
  - target: barzykin-2026-hawkes-driven-otc
    type: mentions
    confidence: inferred
    because: "Same structural convention: market events (here MOs, there RFQs) move the flow state whether or not the maker trades, fills are thinnings (HJB (5.3), p. 426); quotes use the post-event forecast via S_lambda. Barzykin cites the 2018 SIAM Review CJR paper, not this one."
  - target: martin-2026-market-making-hawkes
    type: mentions
    confidence: inferred
    because: "Martin-Tse replace the CJR mean-reverting (single-exponential) activity and LOB shape by general memory kernels (their Remark 2.2 cites the 2018 version); this paper is the exponential original."
  - target: acero-2026-hawkes-structured-networks
    type: mentions
    confidence: inferred
    because: "Acero et al. cite this paper as [15] for the fill function exp(-10 delta); here fills are exp(-kappa delta) with stochastic kappa of long-run level 50 in the simulations (p. 432), so the value 10 does not come from this paper's experiments."
  - target: bergault-2024-price-aware-automated
    type: mentions
    confidence: inferred
    because: "Bergault et al. 2024 cite CJR as ref. [15]; both let a flow state jump together with market events, here with an exponential-kernel Markov state and a first-order expansion instead of a full grid solution."
---

# Buy Low, Sell High: A High Frequency Trading Perspective

## Bibliographic Details

Cartea, Álvaro; Jaimungal, Sebastian; Ricci, Jason. 2014. "Buy Low, Sell High: A High Frequency
Trading Perspective." *SIAM Journal on Financial Mathematics* 5(1): 415–444.
DOI 10.1137/130911196. Received 26 Feb 2013; accepted 15 Apr 2014; published electronically
22 Jul 2014 (p. 415). Affiliations: UCL London (Cartea), University of Toronto (Jaimungal, Ricci).

**Read:** the published journal original, `library/pdf/cartea-2014-buy-low-sell.pdf`, every page
including Appendices A–D (pp. 435–443) and the references (pp. 443–444). **All page numbers on
this page are the journal's printed page numbers (415–444)**; equation, lemma and table
numbers are the journal's. (An SSRN preprint, 1964781, also sits in `library/preprints/`; it
was not used.)

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $S_t$, $\sigma$, $q_t$, $X_t$ | midprice (2.1), its volatility, inventory $q=N^--N^+$, cash (5.1) | $S_t,\sigma,q_t,X_t$ |
| $\delta^+_t$, $\delta^-_t$ | depth of sell LO at $S+\delta^+$, buy LO at $S-\delta^-$ | $\delta^a$, $\delta^b$ |
| $\lambda^+_t$, $\lambda^-_t$ | arrival rate of market **buy** (+) / **sell** (−) orders, eq. (2.2); a buy MO lifts the agent's sell LO | $\lambda_t$ (Hawkes intensity); ⚠ "+" = buy MO = ask-side fill |
| $\theta$, $\beta$ | long-run level, mean-reversion (decay) rate of $\lambda^\pm$ | $\mu$, $\beta$ ($D=\beta I$, one decay for both sides) |
| $\eta$, $\nu$ | jump of same-side / opposite-side intensity per influential MO | entries of the kernel jump matrix |
| $\rho\in[0,1]$ | probability that an MO is influential (p. 421) | ⚠ clashes with spectral radius $\rho(K)$ |
| $\frac{\rho}{\beta}\begin{pmatrix}\eta&\nu\\\nu&\eta\end{pmatrix}$ | (not written in the source) | branching matrix $K$; $\rho(K)=\rho(\eta+\nu)/\beta$ (reader's mapping) |
| $\mathbf A=\begin{pmatrix}\beta-\eta\rho&-\nu\rho\\-\nu\rho&\beta-\eta\rho\end{pmatrix}$ | drift matrix of $m_t(u)$ (Lemma 2.1, (B.1)) | $=D(I-K)$; ⚠ clashes with project $A$ (quadratic coefficient) |
| $\boldsymbol\zeta=(\beta\theta,\beta\theta)'$ vs $\zeta$ | baseline vector in Lemma 2.1 vs mean-reversion rate of $\alpha_t$ (4.1) | ⚠ symbol overloaded in source |
| $m^\pm_t(u)$, $\tilde m^\pm_t(u)$ | $\mathbb E[\lambda^\pm_u\mid\mathcal F_t]$ (p. 421), $\mathbb E[\kappa^\pm_u\mid\mathcal F_t]$ (C.9) | $m_t(u)$ (intensity forecast) |
| $h_\pm(\delta;\boldsymbol\kappa_t)$ | fill probability given an MO arrives (Assumption 2) | $f(\delta)$ |
| $\Lambda^\pm_t=\lambda^\pm_th_\pm(\delta;\boldsymbol\kappa_t)$ | fill rate | ⚠ not the GLFT amplitude $\Lambda$ |
| $\kappa^\pm_t$; $\vartheta,\xi,\eta_\kappa,\nu_\kappa$ | stochastic LOB-shape (depth) parameter, eq. (3.1); its long-run level, rate, jumps | GLFT $k$ made stochastic; no project symbols for the rest |
| $\alpha_t$; $\zeta,\sigma_\alpha,\epsilon^\pm$, $\varepsilon\mathfrak a^\pm=\mathbb E[\epsilon^\pm]$ | short-term alpha (predictable drift), eq. (4.1) | no project symbol; ⚠ $\alpha^\pm$ also the power-law FP exponent (C.1b, C.5) |
| $\phi$ | running inventory penalty in (5.2) | plays the role of $\tfrac12\gamma\sigma^2$ in risk-adjusted objectives (no $\gamma$ in source) |
| $\Phi$, $g$; $g_0,g_\alpha,g_\varepsilon,g_\phi$; $a_\cdot,b_\cdot,c_\phi$ | value function, $\Phi=x+qs+g$; expansion terms (5.6), (5.10) | $g\approx\theta(t,q,\lambda)$; $c_\phi,b_\phi$ ↔ quadratic/linear coefficients $A,B$ |
| $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon^\pm])$ | expansion parameter (p. 427) | — |
| $\mathbb S^\pm_\lambda$, $\mathbb S^\pm_{q\lambda}$, $\mathcal S^\pm_q$, $\mathcal S^\pm_\lambda$ | shift operators (5.5) | post-event finite differences ↔ shadow price $p^j$ |
| $B(\delta_0;\boldsymbol\kappa)$ | $h'/(2h'+\delta_0h'')$ (p. 427) | ⚠ not project $B$ |
| $\overline M^\pm_t$, $\widetilde M^\pm_t$, $N^\pm_t$ | influential / non-influential MO counts; agent's filled sell/buy LOs | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract, key words | 415 |
| ✓ F1 | 1 Introduction (HF market making, adverse selection, influential vs non-influential MOs, simulation preview) | 415–418 |
| ✓ F1 | 2 Arrival of MOs and price dynamics (Poisson/independence in prior work) | 418–419 |
| ✓ F1 | 2.1 Price dynamics, eq. (2.1); Fig. 1 (IBM intensities) | 419–420 |
| ✓ F1 | 2.2 Mutually exciting incoming MO dynamics, Assumption 1, eq. (2.2), Lemma 2.1, Fig. 2 | 420–422 |
| ✓ F1 | 3 Limit quote arrival dynamics and fill rates, Assumptions 2–3, eq. (3.1), Fig. 3 | 422–425 |
| ✓ F1 | 4 Short-term-alpha dynamics, Assumption 4, eq. (4.1) | 424–426 |
| ✓ F1 | 5 The HFT's optimization problem, eq. (5.1) | 426 |
| ✓ F1 | 5.1 Formulation: value function (5.2), HJB (5.3), generator (5.4), shift operators (5.5) | 426–427 |
| ✓ F1 | 5.2 Feedback control: Proposition 5.1, eqs. (5.6)–(5.9) | 427–428 |
| ✓ F1 | 5.3 Asymptotic solution: Theorem 5.2 (5.10)–(5.11), Corollary 5.3 (5.12), symmetric case (5.13) | 428–430 |
| ✓ F1 | 6 HF market making, short-term-alpha, directional strategies: simulation, Tables 1–3 | 430–434 |
| ✓ F1 | 7 Conclusions | 434–435 |
| ✓ F1 | Appendix A Fitting the model (MLE with $\rho=1$, IBM), eqs. (A.1)–(A.2) | 435–436 |
| ✓ F1 | Appendix B Proofs: B.1 Lemma 2.1 (B.1)–(B.2); B.2 Prop. 5.1 (B.3); B.3 Thm. 5.2 (B.4)–(B.5); B.4 Cor. 5.3; B.5 Feynman–Kac (B.6)–(B.7) | 436–439 |
| ✓ F1 | Appendix C Explicit formulae: C.1 exact feedback (C.1a/b), (C.2); C.2 $b_\varepsilon$ (C.3)–(C.6); C.3 $b_\phi$ (C.7)–(C.8), Examples C.4–C.5; C.4 Lemma C.6 (C.9)–(C.10) | 439–442 |
| ✓ F1 | Appendix D Simulation procedure (exact event simulation) | 442–443 |
| — | Acknowledgments, References [1]–[32] | 443–444 |

## Kernthesen

### 1. ⭐ The HF trader is an ultrafast market maker maximising penalised expected wealth, not utility (pp. 416, 426)

The goal is «a particular dynamic HF trading strategy based on optimal postings and
cancellations of LOs to maximize expected terminal wealth over a fixed horizon T while
penalizing inventories» (p. 416); $T$ is at most one trading day and LOs are «canceled an
instant later if not filled» (p. 416). Value function (5.2):
$$\Phi(t,X_t,S_t,q_t,\alpha_t,\boldsymbol\lambda_t,\boldsymbol\kappa_t)=\sup_{(\delta^-_u,\delta^+_u)_{t\le u\le T}\in\mathcal A}\mathbb E\Big[X_T+q_TS_T-\phi\int_t^Tq_s^2\,ds\,\Big|\,\mathcal F_t\Big].$$
CARA utility is named only as an alternative: «An alternative specification is to assume that the
HFT is risk averse so that she maximizes expected utility of terminal wealth» (fn. 8, p. 426); the
running penalty is «more akin to [1], where quadratic variation, rather than variance, is
penalized» and can be read as ambiguity aversion via [12] (p. 426). LOs have unit size (fn. 9,
p. 426). There is no terminal liquidation penalty in (5.2); terminal inventory is liquidated at
$S_T$ with a per-share cost only in the simulation (p. 431).

### 2. ⭐⭐ Market orders come in two unobservable types: influential orders excite, non-influential ones do not (pp. 418, 421)

«The first type of orders are influential orders, which excite the market and induce other
traders to increase the number of MOs they submit» (p. 418); «when noninfluential orders arrive,
the intensity of the arrival of MOs does not change» (p. 418). The type is a latent mark: «Note
that the type indicator of an order is not an observable. Rather, all one can observe is whether
the market became more active after that trade. Therefore, we assume that, conditional on the
arrival of an MO, the probability that the trade is influential is a constant $\rho\in[0,1]$»
(p. 421). The motivation is that bursts are hard to link to news: «it is very difficult to link
news arrival or other classical ways of explaining motives for trade to the activity one observes
in electronic markets» (p. 417).

### 3. ⭐⭐ MO intensities are a bivariate exponential Hawkes system with self- and cross-side excitation (p. 421)

Assumption 1, eq. (2.2):
$$d\lambda^-_t=\beta(\theta-\lambda^-_t)dt+\eta\,d\overline M^-_t+\nu\,d\overline M^+_t,\qquad d\lambda^+_t=\beta(\theta-\lambda^+_t)dt+\eta\,d\overline M^+_t+\nu\,d\overline M^-_t,$$
with $\beta,\theta,\eta,\nu\ge0$ and $\beta>\rho(\eta+\nu)$. «MOs are mutually exciting since their
arrival rates $\lambda^\pm$ jump upon the arrival of influential orders (note that the arrival of
noninfluential orders does not affect $\lambda^\pm$)» (p. 421). Same-side jump $\eta$,
opposite-side jump $\nu$: «Typically one would expect $\nu<\eta$ so that jumps on the opposite side
of the book are smaller than jumps on the same side of the book» (p. 421). One decay rate $\beta$
serves both sides; the kernel is a single exponential, symmetric between sides. This captures
«trade clustering which can be one-sided or two-sided» (p. 418). News could be added as an
exogenous jump process but is excluded (p. 422).

### 4. ⭐⭐ Stability: the mean forecast is bounded iff $\beta>\rho(\eta+\nu)$, with a closed-form matrix-exponential forecast (pp. 421, 436–437)

Lemma 2.1: «The mean future rate $m^\pm_t(u)$ remains bounded for all $u\ge t$ if and only if
$\beta>\rho(\eta+\nu)$. Furthermore, $\lim_{u\to\infty}m^\pm_t(u)=\mathbf A^{-1}\boldsymbol\zeta$»
(p. 421), $\mathbf A=\begin{pmatrix}\beta-\eta\rho&-\nu\rho\\-\nu\rho&\beta-\eta\rho\end{pmatrix}$,
$\boldsymbol\zeta=(\beta\theta,\beta\theta)'$. Proof (B.1)–(B.2), p. 436: $\tfrac{d}{du}m_t+\mathbf Am_t-\boldsymbol\zeta=0$,
$m_t(u)=e^{-\mathbf A(u-t)}\big[\boldsymbol\lambda_t-\mathbf A^{-1}\boldsymbol\zeta\big]+\mathbf A^{-1}\boldsymbol\zeta$.
«Since $\mathbf A$ is symmetric ... its eigenvalues are $\beta-(\eta\pm\nu)\rho$» (p. 437). The
binding eigenvalue is the symmetric (common-mode) one $\beta-(\eta+\nu)\rho$; the antisymmetric
(imbalance) mode decays at $\hat\beta=\beta-\rho(\eta-\nu)$ (reader's reading of (5.13), p. 430).
Intuition: «the decay rate $\beta$ must be strong enough to compensate for both jumps» (p. 422).

### 5. The midprice carries a predictable short-term drift ("short-term-alpha") (pp. 419–420)

Eq. (2.1): $dS_t=(\upsilon+\alpha_t)\,dt+\sigma\,dW_t$, with long-term drift $\upsilon$ set to 0
«because the HF strategies we develop are for very short-term intervals» (p. 420), and
$\alpha_t$ «a predictable zero-mean reverting process» (p. 419). The predictors are «based on order
flow information where we allow for feedback between MO events and short-term-alpha»
(pp. 419–420). Prior work differs: «In previous works on algorithmic trading in LOBs, the
midprice is assumed to be independent of MOs, and MOs arrive at Poisson times» (p. 419).

### 6. ⭐ Fill probabilities are stochastic through a LOB-shape process $\boldsymbol\kappa_t$ (p. 423)

Assumption 2: fill rates $\Lambda^\pm_t\triangleq\lambda^\pm_th_\pm(\delta;\boldsymbol\kappa_t)$,
$h_\pm$ nonincreasing, $C^2$ in $\delta$, $\lim_{\delta\to\infty}\delta h_\pm=0$, and $h_\pm=1$ for
$\delta\le0$, $\boldsymbol\kappa_t\in\mathbb R^n$ (p. 423). Prime examples: exponential
$h=e^{-\kappa^\pm_t\delta^\pm}$ and power law $h=(1+(\kappa^\pm_t\delta^\pm)^\alpha)^{-1}$ (p. 423).
$h=1$ for $\delta\le0$ makes crossing the midprice suboptimal and removes the boundary condition
at $\delta=0$ (p. 423). If MO volumes are i.i.d. exponential and the book flat, $\kappa^\pm_t$ «can
be interpreted as depth of the LOB at each price level» (p. 423). The exponential must be smoothed
at 0 to be $C^2$ (p. 423). In prior reduced-form approaches «the probability that the HFT's limit
order is filled is a (static) function of the posted depth» (p. 423).

### 7. ⭐⭐ Influential MOs also excite the LOB shape $\kappa$ — one-way, slower, and side-asymmetric (pp. 423–425)

Assumption 3, eq. (3.1):
$$d\kappa^-_t=\xi(\vartheta-\kappa^-_t)dt+\eta_\kappa d\overline M^-_t+\nu_\kappa d\overline M^+_t,\qquad d\kappa^+_t=\xi(\vartheta-\kappa^+_t)dt+\nu_\kappa d\overline M^-_t+\eta_\kappa d\overline M^+_t.$$
«This is a one-way effect because influential MOs cause jumps in the $\kappa_t$ process, but jumps
in the FP do not induce jumps in MO arrivals» (p. 424), justified by [27] (Large 2007). «Typically,
we expect the rate of mean-reversion $\xi$ for the LOB to be slower than the rate of mean-reversion
$\beta$ of the MO activity» (p. 424). An upward jump in $\kappa$ lowers the fill probability at a
given depth: market participants «decide to send LOs to the book» after an influential MO (p. 424).
Adverse selection is encoded by $\eta_\kappa<\nu_\kappa$, which «will induce more arrivals of limit
buy (sell) quotes when an influential market buy (sell) order arrives» (p. 425). The net effect on
$\Lambda=\lambda h$ is ambiguous since $\lambda$ rises and $h$ falls (fn. 7, p. 424).

### 8. ⭐ Adverse selection enters through jumps in the drift, not in the price (pp. 425–426)

Assumption 4, eq. (4.1): $d\alpha_t=-\zeta\alpha_tdt+\sigma_\alpha dB_t+\epsilon^+d\overline M^+_t-\epsilon^-d\overline M^-_t$,
$\epsilon^\pm$ random jump sizes (p. 425). «Slower traders will be adversely selected by better
informed and quicker traders» (p. 425). Contrast with [11] (Cartea–Jaimungal 2013), «whereby MOs may
induce an immediate jump in the midprice» so the agent widens by the expected jump; here «the
agent adjusts her posting to protect herself against the potential change in the midprice drift»
(pp. 425–426).

### 9. ⭐⭐ Who excites: all influential MOs — the agent's fills are thinnings and do not drive the flow state (pp. 426–427)

The agent's fills $N^\pm$ arrive at rate $\Lambda^\pm_t=\lambda^\pm_th_\pm(\delta;\boldsymbol\kappa_t)$
(p. 426). In the HJB (5.3) every MO arrival applies the shift $\mathbb S^\pm_\lambda$ to
$(\alpha,\boldsymbol\lambda,\boldsymbol\kappa)$ whether or not the agent's LO is hit: with probability
$h$ the inventory and cash also jump ($\mathbb S^\pm_{q\lambda}$), with probability $1-h$ only the
state shifts ($\mathbb S^\pm_\lambda$). The influential mark is independent of whether the agent was
filled (5.5a). Hence the agent cannot steer $\lambda,\kappa,\alpha$ through her quotes; the
forecasts $m_t,\tilde m_t$ are quote-independent (reader's reading of (5.3)–(5.5)).

### 10. ⭐⭐ The exact problem is a Markov HJB in $(t,x,s,q,\alpha,\boldsymbol\lambda,\boldsymbol\kappa)$, asserted to have a unique viscosity solution (pp. 426–427)

«The above control problem can be cast into a discrete-time controlled Markov chain as carried out
in [4]. Classical results from [6] imply that a dynamic programming principle holds and that the
value function is the unique viscosity solution of the HJB equation» (p. 426). HJB (5.3):
$$(\partial_t+\mathcal L)\Phi+\alpha\Phi_s+\tfrac12\sigma^2\Phi_{ss}+\lambda^-\sup_{\delta^-}\Big\{h_-(\delta^-;\boldsymbol\kappa)\big[\mathbb S^-_{q\lambda}\Phi(t,x-s+\delta^-)-\Phi\big]+(1-h_-)\big[\mathbb S^-_\lambda\Phi-\Phi\big]\Big\}+\lambda^+\sup_{\delta^+}\{\ldots\}=\phi q^2,$$
$\Phi(T,\cdot)=x+qs$; generator (5.4)
$\mathcal L=\beta(\theta-\lambda^-)\partial_{\lambda^-}+\beta(\theta-\lambda^+)\partial_{\lambda^+}+\xi(\vartheta-\kappa^-)\partial_{\kappa^-}+\xi(\vartheta-\kappa^+)\partial_{\kappa^+}-\zeta\alpha\partial_\alpha+\tfrac12\sigma_\alpha^2\partial_{\alpha\alpha}$;
shift operators (5.5a)–(5.5d), e.g. $\mathbb S^\pm_\lambda\Phi=\rho\,\mathbb E[\mathcal S^\pm_\lambda\Phi]+(1-\rho)\Phi$ and
$\mathcal S^+_\lambda\Phi=\Phi(\ldots,\alpha+\epsilon^+,\boldsymbol\lambda+(\nu,\eta)',\boldsymbol\kappa+(\nu_\kappa,\eta_\kappa)')$ (p. 427).
No proof is given; the claim rests on the cited references. Because the kernel is a single
exponential, no history or lift is needed.

### 11. ⭐ An exact optimal control is not tractable in general; for exponential and power FPs only its feedback *form* is explicit (pp. 427, 439–440)

«In general, an exact optimal control is not analytically tractable; two exceptions are the cases
of an exponential and power FPs where the optimal control admits exact analytical solutions, as
presented in section C.1» (p. 427). Proposition C.1 (p. 439–440): for $h=e^{-\kappa^\pm\delta}$,
$\delta^\pm_t=\max\{\tfrac1{\kappa^\pm}-\{\mathbb S^\pm_{q\lambda}g-\mathbb S^\pm_\lambda g\},0\}$ (C.1a);
for the power FP, $\delta^\pm_t=\max\{\tfrac{\alpha}{\alpha-1}(\tfrac1{\kappa^\pm}-\{\mathbb S^\pm_{q\lambda}g-\mathbb S^\pm_\lambda g\}),0\}$ (C.1b).
These are the GLFT-type first-order conditions; they still contain the unknown $g$, so they are a
feedback representation, not a solution of the HJB (reader's assessment; the source calls them
«exact analytical solutions»).

### 12. ⭐⭐ The approximation is a first-order asymptotic expansion in $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon^\pm])$ (p. 427)

«For the general case, we provide an approximate optimal control via an asymptotic expansion which
is correct to $o(\varsigma)$ where $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon^\pm])$. In
principle, the expansion can be carried to higher orders if so desired» (p. 427). Proposition 5.1
*assumes* the decomposition $\Phi=x+qs+g$ and the expansion (5.6)
$$g=g_0(t,q,\boldsymbol\lambda,\boldsymbol\kappa)+\alpha g_\alpha+\varepsilon g_\varepsilon+\phi g_\phi+o(\varsigma),$$
with $\mathbb E[\epsilon^\pm]=\varepsilon\mathfrak a^\pm$ (p. 427). The small parameters are
therefore the inventory penalty, the *current state* of the drift $\alpha_t$, and the mean drift
jump — not the inventory penalty alone. Validity of the ansatz is not proved.

### 13. ⭐⭐ Optimal quotes split into risk-neutral, adverse-selection/directional and inventory terms (pp. 427–428)

(5.7): $\delta^{\pm*}_t=\delta^\pm_0+\alpha\delta^\pm_\alpha+\varepsilon\delta^\pm_\varepsilon+\phi\delta^\pm_\phi+o(\varsigma)$, with
(5.8a–c) $\delta^\pm_\alpha=-B(\delta^\pm_0;\boldsymbol\kappa)(\mathbb S^\pm_{q\lambda}g_\alpha-\mathbb S^\pm_\lambda g_\alpha)$ etc.,
$B(\delta_0;\boldsymbol\kappa)=\frac{h'_\pm(\delta_0)}{2h'_\pm(\delta_0)+\delta_0h''_\pm(\delta_0)}$, and $\delta_0^\pm>0$
solving (5.9) $\delta_0h'_\pm(\delta_0;\boldsymbol\kappa)+h_\pm(\delta_0;\boldsymbol\kappa)=0$. The terms are
«risk-neutral (first term), adverse selection and directional (second and third), and
inventory-management (fourth term)» (p. 428). The risk-neutral quote maximises $\delta h(\delta)$
and «$\lambda^\pm$ plays no role in how the LOs are calculated» (p. 428). Exact controls are
nonnegative (p. 428; proof p. 437).

### 14. ⭐⭐ Theorem 5.2: each first-order coefficient is a polynomial in $q$ of degree ≤ 2, given by Feynman–Kac expectations (pp. 428–429)

(5.10): $g_\alpha=a_\alpha+q\,b_\alpha(t)$, $g_\varepsilon=a_\varepsilon+q\,b_\varepsilon(t,\boldsymbol\lambda)$,
$g_\phi=a_\phi+q\,b_\phi(t,\boldsymbol\lambda,\boldsymbol\kappa)+q^2c_\phi(t)$, with (5.11)
$$b_\alpha=\tfrac1\zeta\big(1-e^{-\zeta(T-t)}\big),\quad b_\varepsilon=\rho\,\mathbb E\Big[\int_t^T(\mathfrak a^+\lambda^+_u-\mathfrak a^-\lambda^-_u)b_\alpha(u)du\,\Big|\,\boldsymbol\lambda_t\Big],$$
$$b_\phi=2\,\mathbb E\Big[\int_t^T\{h^+_{0,u}\lambda^+_u-h^-_{0,u}\lambda^-_u\}(T-u)\,du\,\Big|\,\boldsymbol\lambda_t,\boldsymbol\kappa_t\Big],\quad c_\phi(t)=-(T-t).$$
«the functions $g_0$, $a_\alpha$, $a_\varepsilon$, and $a_\phi$ do not affect the optimal strategy»
(p. 429). The PIDEs are (B.5a)–(B.5d), p. 438, solved by the Feynman–Kac formula (B.6)–(B.7),
p. 439. Crucially, the $q$-polynomial is not itself an approximation: «Note that this step is not
an asymptotic expansion in q; rather it is exact given the prescribed expansion in the other
parameters» (fn. 17, p. 438).

### 15. ⭐⭐ Corollary 5.3: closed-form first-order quotes, truncated at zero (p. 429)

(5.12): $$\delta^{\pm*}=\delta^\pm_0+B(\delta^\pm_0;\kappa^\pm)\Big\{\pm\mathbb S^\pm_\lambda\Big(\mathbb E\Big[\int_t^T\alpha_udu\Big]\Big)+\phi\big(\pm\mathbb S^\pm_\lambda b_\phi+(1\mp2q)(T-t)\big)\Big\},$$
with $|\delta^\pm_{opt}-\delta^{*\pm}|=o(\varsigma)$ and $\max\{\delta^{\pm*},0\}$ also $o(\varsigma)$-accurate.
«the exact solution of the optimal control is nonnegative ... but this is not necessarily the case
in the asymptotic solution; thus we write the optimal control as $\max\{\delta^{\pm*},0\}$»
(fn. 11, p. 429). Both correction terms are evaluated *after* the MO-induced shift
$\mathbb S^\pm_\lambda$, i.e. on the post-event forecast.

### 16. ⭐ Interpretation: the alpha term both protects and speculates; the $\phi$ term targets a nonzero inventory (p. 429)

The alpha term «plays a dual role in the optimal strategy: it corrects for the adverse selection
effect and positions the quotes to execute directional strategies. If the drift is positive, the
agent posts further away from the midprice on the sell side (adverse selection correction) and
closer to the midprice on the buy side in anticipation of upward price movements (directional
strategy)» (p. 429). The $\phi$ term has two parts, flow asymmetry ($b_\phi$) and inventory
($(1\mp2q)(T-t)$): «Both terms together help to induce mean reversion to an optimal inventory level
which is not necessarily zero» (p. 429).

### 17. ⭐⭐ In the symmetric case, both corrections are linear in the intensity imbalance $\lambda^+_t-\lambda^-_t$ (p. 430)

Under (i) $\varepsilon^+=\varepsilon^-$, (ii) $h^+$ and $h^-$ of the same class, (iii)
$h_\pm(\delta_0^\pm,\boldsymbol\kappa)=$ const (p. 430):
$$\text{(5.13a)}\quad\mathbb E\Big[\int_t^T\alpha_udu\Big]=\varepsilon\frac\rho\zeta(\lambda^+_t-\lambda^-_t)\Big\{\frac{1-e^{-\hat\beta(T-t)}}{\hat\beta}-\frac{e^{-\zeta(T-t)}-e^{-\hat\beta(T-t)}}{\hat\beta-\zeta}\Big\}+\alpha_t\frac{1-e^{-\zeta(T-t)}}{\zeta},$$
$$\text{(5.13b)}\quad b_\phi=2h(\lambda^+_t-\lambda^-_t)\Big\{\frac1{\hat\beta}(T-t)-\frac{1-e^{-\hat\beta(T-t)}}{\hat\beta^2}\Big\},\qquad\hat\beta=\beta-\rho(\eta-\nu).$$
«Both expressions contain terms proportional to the difference in the MO activity on the buy and
sell sides. If there are no influential orders, these will be equal to their long-run levels and
will therefore be zero» (p. 430). The imbalance relaxes at $\hat\beta$, which is slower than
$\beta$ when $\eta>\nu$.

### 18. ⭐⭐ The closure is linear: affine ansatz → linear matrix ODEs solved by $e^{-\mathbf A(T-t)}$ (pp. 440–441)

Proposition C.2 (p. 440): $\mathbb E[\int_t^T\alpha_sds\mid\boldsymbol\lambda,\alpha]=\varepsilon b_\varepsilon+\alpha b_\alpha$,
$\varepsilon b_\varepsilon=A(t)+\boldsymbol\lambda\cdot\mathbf C(t)$ with (C.4a–c) in terms of
$\mathbf A^{-1}$, $(\mathbf A-\zeta\mathbf I)^{-1}$ and $e^{-\mathbf A(T-t)}$. The affine ansatz
$f=A(t)+\boldsymbol\lambda\mathbf C(t)+\alpha b_\alpha(t)$ gives the **linear** system (C.6):
$\partial_tA+\boldsymbol\zeta'\cdot\mathbf C=0$, $\partial_t\mathbf C-\mathbf A\mathbf C+\rho b_\alpha(t)\varepsilon\mathfrak a=0$
(p. 441). Nothing quadratic in the unknowns appears anywhere: no Riccati equation arises at this
order.

### 19. ⭐⭐ $b_\phi$ has a closed form, independent of $\kappa$, whenever the risk-neutral fill probability is constant (p. 441)

Proposition C.3: if $h_\pm(\delta^\pm_0;\boldsymbol\kappa)=h_\pm$ constant, then
$$\text{(C.7)}\quad b_\phi(t,\boldsymbol\lambda)=2\boldsymbol\xi'\Big\{\big(\mathbf A^{-1}(T-t)-\mathbf A^{-2}(\mathbf I-e^{-\mathbf A(T-t)})\big)\big[\boldsymbol\lambda-\mathbf A^{-1}\boldsymbol\zeta\big]+\tfrac12(T-t)^2\mathbf A^{-1}\boldsymbol\zeta\Big\},\quad\boldsymbol\xi=(-h_-,h_+)',$$
from $\int_t^T\mathbf m_t(u)(T-u)du$ (C.8). «This result is valid under the restriction that
$\mathbf A$ is invertible, which is implied by the arrival rate of MOs (2.2) and Lemma 2.1» (p. 441).
Examples C.4–C.5: exponential FPs give $h(\delta_0)=e^{-1}$ (so $\delta_0=1/\kappa$); power FPs
$[1+(\kappa\delta)^{\alpha}]^{-1}$, $\alpha>1$, give $\delta_0=(\alpha-1)^{-1/\alpha}\kappa^{-1}$ and
$h=(\alpha-1)/\alpha$ (p. 441). So in both standard classes the LOB-shape process $\kappa$ affects
the quotes only through $\delta_0=1/\kappa$-type terms and $B$, not through $b_\phi$.

### 20. Poisson is the special case $\rho=0$; symmetric initial states kill the flow term (p. 441)

«Notice that the Poisson model of trade arrivals can be recovered by setting $\rho=0$. Furthermore,
if the initial states $\lambda_0^\pm$ are equal and $\kappa^\pm$ are equal, then $b_\phi\equiv0$»
(p. 441).

### 21. The conditional mean of the LOB-shape process is explicit and driven by the MO forecast (p. 442)

Lemma C.6, (C.9): $\tilde m^\pm_t(u)=\vartheta+\frac\rho\xi[\eta_\kappa m^\pm_t(u)+\nu_\kappa m^\mp_t(u)]+\big[\kappa^\pm_t-\vartheta-\frac\rho\xi(\eta_\kappa\lambda^\pm_t+\nu_\kappa\lambda^\mp_t)\big]e^{-\xi(u-t)}$,
from the uncoupled ODE (C.10), consistent with (3.1) ($\kappa^\pm$ takes $\eta_\kappa$ from
same-side MOs, whose rate is $\lambda^\pm$). $\tilde m_t(\infty)$ is used to set the misspecified agents' constant $\kappa$ (p. 431).

### 22. ⭐ Simulation design: six information types of HFT against one data-generating process (pp. 430–432)

MOs are generated over five minutes; quotes from Corollary 5.3 with $b_\phi$ from Proposition C.2
[sic; C.3 gives $b_\phi$]; terminal inventory liquidated at $S_T$ with 1 bp or 10 bp per share
(p. 431; fn. 15: $S_0=\$100$); 5,000 repetitions (p. 431); exponential FPs (fn. 14: power FPs
«very similar», p. 430). Agents differ in $\rho$ used: (1) correct $\rho$ with (a) correct alpha
dynamics — the **benchmark** — or (b) $\alpha\equiv0$; (2) $\rho=1$ with jump sizes rescaled to
match long-run means, (a) misspecified alpha or (b) $\alpha\equiv0$; (3) $\rho=0$, constant
$\lambda,\kappa$ at their long-run means, (a) diffusion-only alpha or (b) $\alpha\equiv0$
(pp. 431–432). Data-generating parameters (p. 432): $\beta=60$, $\theta=1$, $\eta=40$, $\nu=10$,
$\xi=10$, $\vartheta=50$, $\eta_\kappa=10$, $\nu_\kappa=25$, $\upsilon=0$, $\sigma=0.01$,
$\zeta=2$, $\sigma_\alpha=0.01$, $\rho=0.7$, $\epsilon^\pm$ exponential with mean $\varepsilon\in\{0.04,0.02\}$;
$\phi\in\{1,2,4\}\times10^{-5}$. Implied branching ratio $\rho(\eta+\nu)/\beta=0.58$ (reader's
calculation).

### 23. ⭐⭐ With strong alpha impact ($\varepsilon=0.04$) only alpha-aware HFTs make money (Table 1, pp. 432–433)

Table 1, Case I (1 bp), mean PnL (std) — alpha used / not used:
$\phi=10^{-5}$: benchmark 14.09 (6.98) / −3.81 (2.83); $\rho=1$: 12.77 (6.44) / −3.88 (2.83); $\rho=0$:
−4.34 (3.00) / −4.32 (2.94). $\phi=4\cdot10^{-5}$: benchmark 12.49 (4.28) / 0.24 (1.48); $\rho=1$:
11.08 (3.94) / 0.06 (1.48); $\rho=0$: −1.24 (1.60) / −1.25 (1.58). Case II (10 bp) is similar
(e.g. benchmark 13.32 vs $\rho=0$ −4.81 at $\phi=10^{-5}$). «The tables clearly show that market
making is more profitable if the HFTs incorporate in their optimal strategies predictions of
short-term-alpha; this is true even if the HFTs incorrectly specify the short-term-alpha
parameters» (pp. 432–433); «HFTs who omit short-term-alpha face negative, or at best close to zero,
mean PnLs» (p. 433).

### 24. With weaker alpha impact ($\varepsilon=0.02$) alpha-ignorers survive (Table 2, p. 433)

Case III (1 bp): $\phi=10^{-5}$: benchmark 8.81 (2.84) / 1.66 (1.46); $\rho=1$: 8.16 / 1.61;
$\rho=0$: 1.25 / 1.23. $\phi=4\cdot10^{-5}$: benchmark 7.41 (1.75) / 3.08 (0.81). «Table 2 shows that
if the mean impact of influential orders decreases to $\varepsilon=0.02$, HFTs are able to subsist even
if they do not use predictors of short-term-alpha» (p. 433), though the authors «believe that in
practice HFTs will not survive» without it (p. 433).

### 25. ⭐ A higher inventory penalty helps alpha-ignorers by pushing quotes deeper (pp. 433–434)

For alpha-aware HFTs, raising $\phi$ lowers both mean and std (a mean–risk trade-off). For
alpha-ignorers it raises the mean and lowers the std: «by increasing $\phi$, the HFT reduces her
exposure to adverse selection, and this explains why the mean PnL increases in $\phi$» (p. 434).
Conclusions restate: HFTs who are «systematically being picked off can stay in business if they
exert tight controls on their inventories» (p. 435).

### 26. With fewer influential orders ($\rho=0.3$) the gaps shrink but the ranking holds (Table 3, p. 434)

$\varepsilon=0.04$, $\phi=10^{-5}$: benchmark 4.97 (1.43), $\rho=1$ 4.16, $\rho=0$ 2.60; alpha
not used ≈ 2.57–2.59. $\varepsilon=0.02$, $\phi=10^{-5}$: 4.69 / 4.34 / 3.86. «the $\rho=0$ agent
performs significantly better relative to the other agents (although still is the worst of the
three strategies). ... the benchmark HFT always performs better than the other HFTs» (p. 434). No
optimality gap to an exact solution is reported anywhere; comparisons are between misspecified
agents.

### 27. ⭐ Calibration is a $\rho=1$ maximum-likelihood fit on IBM trades (pp. 420, 435–436)

Appendix A fits only the all-influential case: «Calibrating and estimating the current state of
activity in the general model in an online manner are beyond the scope of this work and will be
reported on elsewhere» (p. 435). With $\rho=1$ the intensity path is explicit (A.1) and the
log-likelihood is (A.2). IBM, 1 Feb 2008, 3:30–4:00 p.m.: $\hat\beta=180.05$, $\hat\theta=2.16$,
$\hat\eta=64.16$, $\hat\nu=55.73$ (p. 436) — branching ratio $(\hat\eta+\hat\nu)/\hat\beta\approx0.67$,
and cross-side jump almost as large as same-side (reader's calculation). «Notice that the spikes in
the historical intensity are often above the fitted intensities» because with $\rho=1$ «the size of
the jump in intensities must be smaller than the true jump size» (p. 436). Fig. 1 (p. 420) compares
1-second historical and fitted intensities over 3 minutes.

### 28. The simulation is an exact event-by-event scheme (pp. 442–443)

«Note that this produces an exact simulation; specifically, there are no discretization errors»
(p. 442). Interarrival times are drawn by inverting the compensator of the total rate
$2\theta+(\lambda^+_{t_n}+\lambda^-_{t_n}-2\theta)e^{-\beta(t-t_n)}$ via a Lambert-W root (p. 442,
fn. 18); side by $p_{buy}$; fill if $u<e^{-\kappa\delta}$; correlated Gaussian update of $(S,\alpha)$;
influential with probability $\rho$ (pp. 442–443).

### 29. Limitations and extensions named by the authors (pp. 422, 426, 435)

No market orders by the HFT: «In our stochastic optimal control problem the HFT does not execute
MOs; the best she can do is send LOs at the midprice» (p. 435). Fixed LO size (fn. 9, p. 426). News
excluded (p. 422). Online filtering of $\rho$/state left open (p. 435). Manipulation: «algorithms
could be designed to send MOs, in the hope of being perceived as influential, to trigger other
algorithms into action» — beyond scope (p. 435).

### 30. Internal inconsistencies in the printed text (pp. 423, 440–443)

(i) Power FP written $(1+(\kappa\delta)^\alpha)^{-1}$ (p. 423) and $[1+(\kappa\delta)^{\alpha}]^{-1}$
(Example C.5, p. 441) but $(1+\kappa\delta)^{\alpha}$ in Proposition C.1(2) (p. 440). (ii) $\alpha$
denotes both short-term alpha and the FP exponent; $\zeta$ both the alpha mean-reversion rate and the
baseline vector. (iii) Appendix D codes $B_{n}\in\{1,-1\}$ (p. 442) but Appendix A uses $\{0,1\}$
(p. 436), and the step-6 update $\lambda^\pm\mathrel{+}=\tfrac12(1\pm B)\nu+\tfrac12(1\mp B)\eta$
(p. 443) gives a buy MO a jump $\nu$ on the buy side, the reverse of (2.2b) — read literally it
swaps self and cross excitation. (iv) Section 6 cites Proposition C.2 for $b_\phi$ (p. 430); it is
C.3. (v) Footnote 18 refers to an undefined $A_0$ (p. 442). Points (iii)–(v) are the reader's
observations; whether the simulation code had the same swap cannot be checked.

## Figures and tables

- Fig. 1 (p. 420): IBM historical (1-s window) vs fitted ($\rho=1$) intensities, buy and sell MOs, 3 min.
- Fig. 2 (p. 422): sample path of buy/sell activity with influential (circles) and non-influential (squares) MOs.
- Fig. 3 (p. 425): fill-rate curves $\Lambda^\pm$ vs depth with $\kappa^+=2,\kappa^-=1,\lambda^+=0.75,\lambda^-=1$.
- Table 1 (p. 432): PnL mean/std, $\varepsilon=0.04$, $\rho=0.7$, liquidation 1 bp and 10 bp.
- Table 2 (p. 433): same, $\varepsilon=0.02$.
- Table 3 (p. 434): $\rho=0.3$, $\varepsilon\in\{0.04,0.02\}$, 1 bp.

No figures extracted to `knowledge/assets/` (write scope limited to this page).

## What this source does not address

- **More than one asset.** One stock, two sides. Nothing on several assets, cross-asset
  excitation or portfolio inventory risk (verified page by page). The multi-asset closed form is
  [[begv-2021-model]]; multi-asset Hawkes with network structure is in
  [[acero-2026-hawkes-structured-networks]].
- **Non-exponential kernels.** Single exponential decay per process; no sums of exponentials,
  power laws or general Volterra kernels. For general kernels see
  [[martin-2026-market-making-hawkes]], [[barzykin-2026-hawkes-driven-otc]] and
  [[jusselin-2021-persistent-order-flow]].
- **Fill-driven (self-inflicted) excitation.** Excitation comes from market-wide influential MOs;
  the agent's own fills play no special role.
- **An exact numerical benchmark or regret.** No grid solution of HJB (5.3); the accuracy of the
  $o(\varsigma)$ quotes is never measured against the optimum. PnL comparisons are between
  misspecified agents, not against an optimum.
- **A proof that the expansion is valid.** The ansatz (5.6) is assumed (Proposition 5.1); the
  DPP and viscosity uniqueness are asserted by citation (p. 426).
- **CARA utility and terminal liquidation penalty.** Risk-neutral wealth with running penalty
  only (5.2); CARA mentioned as an alternative (fn. 8).
- **Online estimation of the latent influential mark.** Out of scope (p. 435).
- **Market orders by the maker, variable order size.** Excluded (p. 435; fn. 9).

## Model card

- **Assets:** 1 (one stock; buy and sell sides).
- **Kernel:** single exponential (mean-reverting jump intensity), decay $\beta$ for MO activity,
  $\xi$ for LOB shape, $\zeta$ for short-term alpha; equivalently a bivariate exponential Hawkes
  process with marks.
- **Excitation:** self-side ($\eta$) and cross-side ($\nu$), triggered only by **influential** MOs
  (probability $\rho$, unobservable mark); non-influential MOs do not excite. Influential MOs also
  excite the LOB depth $\kappa^\pm$ ((3.1), one-way: book does not excite flow) and the drift
  $\alpha$ (4.1). No cross-asset excitation (one asset).
- **Who excites:** all (influential) market orders in the market, whether or not they fill the
  agent; fills are thinnings with probability $h(\delta;\kappa)$.
- **Objective:** risk-neutral expected terminal wealth minus running quadratic inventory penalty
  $\phi\int q^2$ (5.2); no CARA, no terminal penalty.
- **Solution method:** Markov HJB (5.3) in $(t,x,s,q,\alpha,\lambda^\pm,\kappa^\pm)$; first-order
  asymptotic expansion in $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon])$ → linear PIDEs solved by
  Feynman–Kac → closed-form quotes (5.12)–(5.13) via matrix exponentials (C.4), (C.7). Exact
  feedback form only for exponential/power FPs (C.1).
- **Benchmark:** simulation (5 min, 5,000 paths, exact event simulation) of six HFTs differing in
  assumed $\rho$ and alpha model; the correctly specified first-order strategy is the "benchmark".
  No exact optimum, no Poisson-optimal comparator other than the $\rho=0$ agent.
- **Reported numbers:** PnL mean (std) in $ per 5 min, Tables 1–3; e.g. benchmark 14.09 (6.98) vs
  alpha-ignorer −3.81 (2.83) at $\varepsilon=0.04,\phi=10^{-5}$, 1 bp (p. 432). **No regret or gap
  numbers** (n/a — no exact solution computed).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 26, 30.**

### What this focus needs beyond the Kernthesen

1. **The multi-factor mutually exciting process, precisely.** One latent mark (influential with
   probability $\rho$) gates three excitation channels at once: an influential buy MO raises
   $\lambda^+$ by $\eta$ and $\lambda^-$ by $\nu$ (2.2), raises $\kappa^+$ by $\eta_\kappa$ and
   $\kappa^-$ by $\nu_\kappa$ (3.1), and raises $\alpha$ by $\epsilon^+$ (4.1); a sell MO acts
   symmetrically. Every channel is a single exponential with its own rate ($\beta,\xi,\zeta$). The
   LOB depth $\kappa$ is *excited but not exciting* (one-way, p. 424). In branching-matrix terms
   (reader's mapping) $K=\tfrac\rho\beta\begin{pmatrix}\eta&\nu\\\nu&\eta\end{pmatrix}$ and
   $\mathbf A=\beta(I-K)$; Lemma 2.1 is the condition $\rho(K)<1$.
2. **State of the HJB.** $(t,x,s,q,\alpha,\lambda^+,\lambda^-,\kappa^+,\kappa^-)$; $x$ and $s$
   are removed by $\Phi=x+qs+g$, leaving $g(t,q,\alpha,\boldsymbol\lambda,\boldsymbol\kappa)$
   (Proposition 5.1, p. 427). Because each channel is one exponential, the intensities themselves
   are the Markov state, so no lift is needed and the dimension is fixed (2 + 2 + 1 flow-type
   variables plus $q$).
3. **The "first-order expansion" — in what, giving what, exact where.**
   - *Small parameter:* $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon^\pm])$ (p. 427) — the
     inventory penalty **and** the current alpha **and** the mean alpha jump. The wiki entity page
     describes it as "a first-order expansion in the inventory penalty"; that is incomplete.
   - *What it yields:* quotes (5.12) = risk-neutral $\delta_0$ (from $\delta h'+h=0$; $=1/\kappa$
     for exponential FPs) + an alpha correction + a $\phi$ correction. In the symmetric case both
     corrections are **linear in $\lambda^+_t-\lambda^-_t$** with deterministic time weights
     (5.13), plus $\alpha_t$ and $(1\mp2q)(T-t)$ terms. So the entity page's "quotes linear in the
     buy–sell intensity difference" is right, but only for the symmetric case (5.13) and to first
     order.
   - *Closure type:* **linear ODE / linear PIDE.** The coefficient PIDEs (B.5a)–(B.5d) are linear;
     with exponential kernels their Feynman–Kac solutions reduce to the linear matrix ODE (C.6) and
     matrix exponentials $e^{-\mathbf A(T-t)}$ (C.4), (C.7). **No Riccati equation appears.**
   - *Where it is exact:* given the truncation in $\varsigma$, the quadratic-in-$q$ form is exact
     (fn. 17, p. 438) and the formulas (C.4)/(C.7) are exact solutions of the first-order PIDEs.
     The approximation lives entirely in the truncation at $o(\varsigma)$, whose validity is assumed
     (5.6), not proved.
   - *Why no Riccati (reader's inference):* the inventory coefficient is $c_\phi=-(T-t)$, i.e.
     the $q^2$-coefficient of $g$ is $-\phi(T-t)+o(\phi)$. In GLFT/BEGV-type models the
     $q^2$-coefficient solves a Riccati ODE whose quadratic term is $O(\phi^2)$; truncating at
     first order linearises it away. Consequence: the inventory skew $\phi(1\mp2q)(T-t)$ grows
     linearly in time-to-go and never saturates to the GLFT/BEGV stationary skew, so the
     approximation needs $\phi(T-t)$ (times intensity and $\kappa$ scales) small. In the paper's
     simulation $T=5$ min and $\phi\le4\cdot10^{-5}$, which keeps it in that regime.
   - *A useful simplification (reader's calculation):* for exponential FPs
     $B(\delta_0;\kappa)=h'/(2h'+\delta_0h'')=(-\kappa)/(-2\kappa+\kappa)=1$ at $\delta_0=1/\kappa$, so
     (5.12) becomes $\delta^{\pm*}=1/\kappa^\pm\pm\mathbb S^\pm_\lambda\mathbb E[\int\alpha]+\phi(\pm\mathbb S^\pm_\lambda b_\phi+(1\mp2q)(T-t))$.
4. **Short-term-alpha / adverse-selection component.** It enters as
   $\pm\mathbb S^\pm_\lambda\mathbb E[\int_t^T\alpha_u du]$: the expected integrated drift *after* the
   MO that would fill the quote (p. 429). In the symmetric case it is linear in the intensity
   imbalance with relaxation $\hat\beta=\beta-\rho(\eta-\nu)$ and in $\alpha_t$ with relaxation
   $\zeta$ (5.13a). The same term both widens the side at risk of being picked off and narrows the
   side that profits from the trend (p. 429). The simulation shows it is the economically dominant
   term: dropping it flips PnL from ≈ +14 to ≈ −4 at $\varepsilon=0.04$ (Table 1, p. 432).
5. **Post-event evaluation as a closure feature.** Every correction is evaluated through
   $\mathbb S^\pm_\lambda$, i.e. on the state after the triggering MO has (possibly) excited the
   flow. Because the excitation is applied regardless of fill and the shifts are linear operators
   on functions affine in $\boldsymbol\lambda$, this costs nothing in the linear closure. This is the
   exponential, first-order analogue of the "post-request forecast" in
   [[barzykin-2026-hawkes-driven-otc]] (Kernthese 18 there) — reader's comparison; neither paper
   draws it.
6. **How strategies are tested.** Simulation only (Kernthesen 22–26): exact event simulation, 5 min,
   5,000 runs, six agents differing in assumed $\rho\in\{0.7\text{ (true)},1,0\}$ and in alpha
   modelling. Comparator for "ignoring excitation" is the $\rho=0$ agent with constant long-run
   $\lambda,\kappa$ — Poisson-like but still quoting with the first-order formula. There is no exact
   HJB solution, so nothing measures the accuracy of the expansion itself; the reported gains
   measure the value of *information* (modelling $\rho$ and $\alpha$), not the closeness to the
   optimum.
7. **Several assets: not discussed.** Verified page by page. *Inference (not the authors'):* the
   ingredients are already matrix-valued and carry over formally. (a) With $2d$ MO types
   (asset × side) and cross-asset blocks, $\mathbf A=D(I-K)$ becomes $2d\times2d$; $m_t(u)$ (B.2) and
   $\int m_t(u)(T-u)du$ (C.8) keep their matrix-exponential form, valid iff $\rho(K)<1$. (b) A
   multi-asset running penalty $\phi\,q'\Gamma q$ would at first order give $c_\phi=-\Gamma(T-t)$
   and a vector $b_\phi$ linear in $\boldsymbol\lambda$ through $e^{-\mathbf A(T-t)}$, so quotes on
   asset $i$ would respond linearly to intensity imbalances on asset $j$ through the off-diagonal
   blocks of $e^{-\mathbf A(T-t)}$ — a linear "cross-asset response" closed form. (c) What does not
   carry over: the inventory coupling across assets stays linear-in-time; the BEGV matrix Riccati
   (the source of cross-asset hedging saturation in [[begv-2021-model]]) is second-order in $\phi$ and
   absent. So CJR's route gives a cheap first-order multi-asset closure but cannot reproduce
   BEGV's inventory nonlinearity; combining them (BEGV Riccati for inventory, CJR-type affine
   forecast terms for flow) is the open construction. (d) Cross-asset alpha (a burst in $j$ moving
   the drift of $i$) would need a vector $\alpha$ and a matrix $\zeta$; the affine structure (C.6)
   survives.

### Direct quotes (for the draft)

> "However, this paper is the first to incorporate such effects into optimal control problems related to AT." (p. 418)

> "MOs are mutually exciting since their arrival rates $\lambda^\pm$ jump upon the arrival of influential orders (note that the arrival of noninfluential orders does not affect $\lambda^\pm$)." (p. 421)

> "For the general case, we provide an approximate optimal control via an asymptotic expansion which is correct to $o(\varsigma)$ where $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon^\pm])$. In principle, the expansion can be carried to higher orders if so desired." (p. 427)

> "Note that this step is not an asymptotic expansion in q; rather it is exact given the prescribed expansion in the other parameters." (fn. 17, p. 438)

> "Both expressions contain terms proportional to the difference in the MO activity on the buy and sell sides. If there are no influential orders, these will be equal to their long-run levels and will therefore be zero." (p. 430)

> "This is a one-way effect because influential MOs cause jumps in the $\kappa_t$ process, but jumps in the FP do not induce jumps in MO arrivals." (p. 424)

### Examples & illustrations (for later drafting)

- Table 1, Case I, $\phi=10^{-5}$ (p. 432): benchmark 14.09 vs $\rho=1$ 12.77 vs $\rho=0$ −4.34;
  without alpha all three ≈ −3.8 to −4.3 — the value of modelling the alpha channel dwarfs the
  value of getting $\rho$ right.
- IBM fit (p. 436): $\hat\eta=64.16$, $\hat\nu=55.73$, $\hat\beta=180.05$ — cross-side excitation
  nearly as strong as self-excitation, branching ratio ≈ 0.67; a concrete number for a two-type
  $K$.
- Fig. 3 (p. 425): asymmetric fill-rate curves showing how $\kappa^\pm$ change shape and
  $\lambda^\pm$ the vertical scale.

### Boundary of this focus

Single asset; the multi-asset statements in item 7 are the project's inference from the
matrix structure of (B.2), (C.4), (C.7), not claims of the source. The paper never solves
the exact HJB, so whether the first-order closure is accurate (rather than just profitable relative
to misspecified agents) is not known from this source. Kernels are single exponentials throughout.

## Mentioned entities

- Models: [[cartea-jaimungal-ricci-model]] (this paper defines it), [[glft-2013-model]] (ref. [20]),
  [[avellaneda-stoikov-model]] (ref. [3]); [[begv-2021-model]] is later and not cited.
- Concepts: [[hawkes-process]], [[branching-matrix]], [[intensity-forecast]], [[markov-lift]],
  [[shadow-price]], [[matrix-riccati-equation]], [[hamiltonian-quadratic-approximation]].
- Library works cited: `gueant-2013-dealing-inventory-risk` ([20]; see
  [[gueant-2013-dealing-inventory-risk]]), `avellaneda-2008-high-frequency-trading` ([3]),
  `ho-1981-optimal-dealer-pricing` ([23]), `guilbaud-2011-optimal-high-frequency` ([22] is the
  2013 Quant. Finance version of this Guilbaud–Pham preprint).
- Not in the library: Almgren 2003; Almgren–Chriss 2000; Bäuerle–Rieder 2009; Bayraktar–Ludkovski
  2012; Bertsekas–Shreve 1978; Bouchard–Dang–Lehalle 2011; Bowsher 2007; Cartea–Jaimungal 2013a,b
  (Appl. Math. Finance; Math. Finance); Cartea–Jaimungal–Donnelly 2013; Cartea–Jaimungal–Kinzebulatov
  2013; Cartea–Penalva 2012; Cont–Talreja–Stoikov 2010; Easley–O'Hara 1992; Large 2007; O'Hara 1998;
  Roşu 2009; Sarkar–Schwartz 2009; Toke 2011; Guilbaud–Pham 2013 (pro rata).

## Connections

- Defines: [[cartea-jaimungal-ricci-model]].
- Cites: [[glft-2013-model]] / [[gueant-2013-dealing-inventory-risk]], [[avellaneda-stoikov-model]].
- Later generalisations (not cited here): [[martin-2026-market-making-hawkes]] (general kernels,
  Mercer lift + PINN), [[barzykin-2026-hawkes-driven-otc]] (general kernels, Volterra–Riccati,
  post-request forecast), [[jusselin-2021-persistent-order-flow]] (general Hawkes, path-dependent
  HJB).
- Contrast on closure: [[begv-2021-model]] and [[bergault-2021-closed-form-approximations]]
  (Hamiltonian quadratic approximation → matrix Riccati, multi-asset, Poisson flow) vs this paper
  (first-order expansion → linear ODEs, one asset, Hawkes flow). Together they bracket the
  project's gap.
- Cited by: [[acero-2026-hawkes-structured-networks]] (ref. [15], fill function),
  [[bergault-2024-price-aware-automated]] (ref. [15]).
