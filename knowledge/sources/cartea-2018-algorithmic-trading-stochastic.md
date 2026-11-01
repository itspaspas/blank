---
title: "Cartea, Jaimungal & Ricci 2018 — Algorithmic Trading, Stochastic Control, and Mutually Exciting Processes (SIAM Review SIGEST)"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: cartea-2018-algorithmic-trading-stochastic
depth: standard
tags: [market-making, hawkes, mutually-exciting, single-asset, limit-order-book, short-term-alpha, adverse-selection, asymptotic-expansion, sigest-reprint, mean-field-games]
relations:
  - target: cartea-2014-buy-low-sell
    type: builds-on
    confidence: extracted
    because: "Reprint with revisions: «This paper originally appeared in SIAM Journal on Financial Mathematics, Volume 5, Number 1, 2014, pp. 415--444, as ``Buy Low, Sell High: A High Frequency Trading Perspective.''» (fn. *, p. 673). Model, HJB, Proposition 5.1, Theorem 5.2 and Corollary 5.3 are unchanged."
  - target: cartea-jaimungal-ricci-model
    type: supports
    confidence: extracted
    because: "Restates the model unchanged: «By introducing a multifactor mutually exciting process, we allow for feedback effects in market buy and sell orders and the shape of the limit order book (LOB)» (abstract, p. 673); (2.2), (3.1), (4.1), (5.2), pp. 680-685."
  - target: hawkes-process
    type: builds-on
    confidence: extracted
    because: "«Multivariate Hawkes processes have recently been used in the financial econometrics literature to model clustering in trade arrival ... However, this paper is the first to incorporate such effects into optimal control problems related to AT.» (p. 677); key words include «Hawkes processes» (p. 673)."
  - target: branching-matrix
    type: builds-on
    confidence: extracted
    because: "Lemma 2.1: «The mean future rate m_t(u) remains bounded for all u >= t if and only if beta > rho(eta + nu)» (p. 681); eigenvalues of A are beta - (eta +/- nu) rho (B.1, p. 695)."
  - target: intensity-forecast
    type: builds-on
    confidence: extracted
    because: "(B.2), p. 695: the mean future rate (m^-_t(u), m^+_t(u))' = e^{-A(u-t)}[(lambda^-_t, lambda^+_t)' - A^{-1}zeta] + A^{-1}zeta; it enters b_phi in (5.11c), p. 687, and (5.13b), p. 689."
  - target: who-excites-the-flow
    type: supports
    confidence: extracted
    because: "Flow-driven: «MOs are mutually exciting since their arrival rates lambda^+- jump upon the arrival of influential orders (note that the arrival of noninfluential orders does not affect lambda^+-)» (p. 680); the agent's fills are thinnings with probability h(delta; kappa), HJB (5.3), p. 685."
  - target: glft-2013-model
    type: cites
    confidence: extracted
    because: "Ref. [28] (Gueant-Lehalle-Fernandez-Tapia 2013) among algorithms «designed to manage inventory risk [14], [28]» (p. 677) and among reduced-form fill models «see [32], [3], [6], [14], and [28]» (p. 681)."
  - target: avellaneda-stoikov-model
    type: cites
    confidence: extracted
    because: "«more recently Avellaneda and Stoikov [3] studied the optimal HF submission strategies of bid and ask LOs» (p. 675)."
  - target: barzykin-2026-hawkes-driven-otc
    type: mentions
    confidence: inferred
    because: "Barzykin cites this 2018 SIAM Review version (see the 2014 page); same flow-driven convention, with RFQs instead of MOs and general kernels instead of one exponential."
  - target: martin-2026-market-making-hawkes
    type: mentions
    confidence: inferred
    because: "Martin-Tse (Remark 2.2, per the 2014 page) cite this 2018 version as the exponential CJR model they generalise to arbitrary memory kernels."
  - target: choi-2021-synchronised-order-arrivals
    type: mentions
    confidence: inferred
    because: "Choi et al. 2021 build on the 2014 version of the same model (their eqs. (3)-(4) add a synchronising drift term) and benchmark against the CJR asymptotic formula; they do not cite this 2018 reprint."
---

# Algorithmic Trading, Stochastic Control, and Mutually Exciting Processes (SIAM Review, 2018)

## Bibliographic Details

Cartea, Álvaro; Jaimungal, Sebastian; Ricci, Jason. 2018. "Algorithmic Trading, Stochastic
Control, and Mutually Exciting Processes." *SIAM Review* 60(3): 673–703. DOI 10.1137/18M1176968.
Published electronically 8 August 2018 (p. 673). SIGEST section: a revised reprint of
[[cartea-2014-buy-low-sell]] (*SIAM J. Financial Math.* 5(1): 415–444, 2014), as the first-page
footnote states (p. 673). Affiliations now Oxford (Cartea), Toronto (Jaimungal, Ricci).

**Read:** the published SIAM Review original, `library/pdf/cartea-2018-algorithmic-trading-stochastic.pdf`,
all 31 pages including Appendices A–D and the references [1]–[44]. Page numbers are the journal's
(673–703). Equation, lemma, proposition and appendix numbering is **identical to the 2014 paper**,
so equation references carry over one to one; page references do not.

**How this page is scoped.** The 2014 paper has a `deep` page with 30 Kernthesen
([[cartea-2014-buy-low-sell]]). This page does not repeat that work. It (i) checks that the model and
the closure are unchanged, (ii) records what is new or removed in 2018, and (iii) lists the
differences in one table. For the derivation, read the 2014 page. Notation is the same as there
(see its notation map: "+" = buy MO = ask-side fill; $\rho$ = probability that an MO is influential,
not the spectral radius; $\phi$ = running inventory penalty).

## Section map

| Covered | Section | pp. | vs. 2014 |
|---|---|---|---|
| ✓ F1 | Abstract, key words, AMS classes, **table of contents** (new: SIAM Review format) | 673–674 | abstract identical; ToC new |
| ✓ F1 | 1 Introduction | 674–677 | copy-edited; references renumbered |
| ✓ F1 | 2 Arrival of MOs and price dynamics; 2.1 Price dynamics (2.1); **Fig. 1 now INTC, 29 Jan 2018** | 677–679 | data example replaced (was IBM, 1 Feb 2008) |
| ✓ F1 | 2.2 Mutually exciting MO dynamics, Assumption 1, (2.2), Lemma 2.1, Fig. 2 | 679–681 | unchanged |
| ✓ F1 | 3 Limit-quote arrival and fill rates, Assumptions 2–3, (3.1), Fig. 3 | 681–683 | unchanged |
| ✓ F1 | 4 Short-term-alpha, Assumption 4, (4.1) | 683–684 | unchanged |
| ✓ F1 | 5 The HFT's optimisation problem (5.1); 5.1 value function (5.2), HJB (5.3)–(5.5) | 684–685 | unchanged |
| ✓ F1 | 5.2 Feedback control, Proposition 5.1, (5.6)–(5.9) | 686–687 | unchanged |
| ✓ F1 | 5.3 Asymptotic solution, Theorem 5.2 (5.10)–(5.11), Corollary 5.3 (5.12), symmetric case (5.13) | 687–689 | unchanged |
| ✓ F1 | 6 HF market making, short-term-alpha and directional strategies: six HFT types, **Table 1 only** | 689–692 | **Tables 2 and 3 removed** |
| ✓ F1 | **7 New Developments** (stochastic games / MFG, VWAP and tracking, latent factors + ML, partial-information MFG) | 692–693 | **new section** |
| ✓ F1 | 8 Conclusions (no MOs by the HFT; manipulation) | 693–694 | was Section 7; unchanged in substance |
| ✓ F1 | Appendix A Fitting the model ($\rho=1$ MLE), (A.1)–(A.2); **INTC 2018 estimates** | 694 | estimates replaced |
| ✓ F1 | Appendix B Proofs (B.1 Lemma 2.1, B.2 Prop. 5.1, B.3 Thm. 5.2, B.4 Cor. 5.3, B.5 Feynman–Kac) | 695–697 | unchanged |
| ✓ F1 | Appendix C Explicit formulae (C.1 exact feedback for exp./power FPs; C.2 $b_\varepsilon$; C.3 $b_\phi$; C.4 Lemma C.6) | 697–700 | unchanged |
| ✓ F1 | Appendix D Simulation procedure (exact event simulation) | 700–701 | unchanged |
| — | Acknowledgments, References [1]–[44] (with "Cited on p." back-references) | 701–703 | was [1]–[32]; 2014–2018 works added |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Kernthesen

### 1. ⭐ The SIGEST paper is the 2014 paper, revised: the model and its mathematics are unchanged (p. 673)

«This paper originally appeared in SIAM Journal on Financial Mathematics, Volume 5, Number 1, 2014,
pp. 415--444, as "Buy Low, Sell High: A High Frequency Trading Perspective."» (fn. *, p. 673). The
abstract is the 2014 abstract almost word for word (p. 673). Assumptions 1–4, the value function
(5.2), HJB (5.3), Proposition 5.1, Theorem 5.2, Corollary 5.3, (5.13) and Appendices B–D keep their
numbers and content (reader's sentence-by-sentence comparison of the two PDFs; the differences are
copy-editing and reference renumbering). Every claim of [[cartea-2014-buy-low-sell]] Kernthesen 1–21
and 28 therefore holds for this version at the new page numbers.

### 2. ⭐⭐ Market orders form a bivariate exponential Hawkes system gated by an unobservable "influential" mark (pp. 679–681)

Influential orders «excite the state of the market and induce other traders to increase their
trading activity» (p. 679); noninfluential ones do not. Assumption 1, (2.2): $d\lambda^\mp_t=\beta(\theta-\lambda^\mp_t)dt+\eta\,dM^\mp_t+\nu\,dM^\pm_t$,
with $\beta>\rho(\eta+\nu)$ (p. 680). Lemma 2.1 (p. 681): the mean future rate is bounded iff
$\beta>\rho(\eta+\nu)$, and tends to $A^{-1}\zeta$. Same as 2014 (Kernthesen 2–4 there).

### 3. ⭐⭐ The flow is market-driven; the agent's fills are thinnings and never move the intensities (pp. 680, 684–685)

The intensities jump only at influential MOs, «note that the arrival of noninfluential orders does
not affect $\lambda^\pm$» (p. 680). The agent's fills $N^\pm$ have rate $\Lambda^\pm_t=\lambda^\pm_th_\pm(\delta;\boldsymbol\kappa_t)$
(p. 684), so in HJB (5.3) the intensity jump $\mathbb S_\lambda$ happens with or without the fill
(p. 685). In the vocabulary of [[who-excites-the-flow]]: flow-driven.

### 4. ⭐⭐ The closure is a first-order asymptotic expansion: affine in $q$ for $g_\alpha,g_\varepsilon$, quadratic for $g_\phi$, solved by linear ODEs (pp. 686–689, 695–699)

«In general, an exact optimal control is not analytically tractable ... For the general case, we
provide an approximate optimal control via an asymptotic expansion which is correct to $o(\varsigma)$,
where $\varsigma=\max(\phi,\alpha,\mathbb E[\epsilon^\pm])$» (p. 686). Theorem 5.2 (p. 687):
$g_\phi=a_\phi+q\,b_\phi(t,\boldsymbol\lambda,\boldsymbol\kappa)+q^2c_\phi(t)$ with $c_\phi=-(T-t)$, and
$b_\phi$ an expectation of the integrated fill-rate imbalance. Unchanged from 2014 (Kernthesen
12–19 there): a linear closure, not a Riccati one.

### 5. ⭐⭐ In the symmetric case the corrections are linear in the intensity imbalance, relaxing at $\hat\beta=\beta-\rho(\eta-\nu)$ (p. 689)

(5.13b): $b_\phi=2h(\lambda^+_t-\lambda^-_t)\{\tfrac1{\hat\beta}(T-t)-\tfrac{1-e^{-\hat\beta(T-t)}}{\hat\beta^2}\}$.
«Both expressions contain terms proportional to the difference in the MO activity on the buy and
sell sides. If there are no influential orders, these will be equal to their long-run levels and
will therefore be zero.» (p. 689). The intensity enters the quote linearly, through the
antisymmetric eigenmode of $A$.

### 6. ⭐ New empirical motivation: INTC trades on 29 January 2018 replace IBM on 1 February 2008 (p. 679)

Fig. 1: «INTC market orders. Historical running intensity versus smoothed fitted intensity
(restricted to $\rho=1$) using a two-second sliding window for INTC for the period between 9:30 am and
9:33 am, January 29, 2018.» (p. 679). The text reads the figure the same way as in 2014: clusters,
one-sided periods «(for instance, the period around 100 seconds)», bursts that «die out rather
quickly and revert to around two events per second» (p. 679).

### 7. ⭐⭐ New calibration: on INTC 2018 cross-side excitation almost vanishes and decay is extremely fast (p. 694)

With $\rho=1$ MLE (A.1)–(A.2): «For the time window 9:30 am to 9:33 am on January 29, 2018, for INTC
the estimated parameters are $\hat\beta=3{,}774$, $\hat\theta=0.22$, $\hat\eta=2{,}766$, and $\hat\nu=54$.»
(p. 694). Reader's calculations: branching ratio $(\hat\eta+\hat\nu)/\hat\beta\approx0.75$, of which
self-side $\approx0.73$ and cross-side $\approx0.014$; mean decay time $1/\hat\beta\approx0.26$ ms; long-run rate
$\hat\theta\hat\beta/(\hat\beta-\hat\eta-\hat\nu)\approx0.87$ per side per second, consistent with «around
two events per second» in total. The 2014 IBM fit had $\hat\beta=180.05$, $\hat\eta=64.16$,
$\hat\nu=55.73$ (cross nearly equal to self, ratio ≈ 0.67). The statement «Typically, one would expect
$\nu<\eta$ ... (this bears out in the calibration ...)» (p. 680) is now true by a factor of about 50.

### 8. ⭐ The simulation study is cut to Table 1: strong alpha impact, $\rho=0.7$ (pp. 689–692)

Same six HFT types, same parameters ($\beta=60$, $\theta=1$, $\eta=40$, $\nu=10$, $\rho=0.7$,
$\varepsilon=0.04$, ...; p. 690), same numbers: benchmark 14.09 (6.98) vs alpha-ignorer −3.81 (2.83)
at $\phi=10^{-5}$, 1 bp (Table 1, p. 691). The 2014 Table 2 ($\varepsilon=0.02$, where
alpha-ignorers «subsist») and Table 3 ($\rho=0.3$), with their paragraphs and footnote, are gone.
The retained conclusion: «HFTs who omit short-term-alpha face negative, or at best close to zero,
mean PnLs» (p. 691).

### 9. A higher inventory penalty still helps alpha-ignorers by pushing quotes deeper (pp. 691–692)

«by increasing $\phi$, the HFT reduces her exposure to adverse selection, which explains why the mean
PnL increases in $\phi$» (p. 692); unchanged from 2014.

### 10. ⭐⭐ New Section 7: the field has moved to stochastic games and mean-field games, where closed forms are lost (p. 692)

«The problem setup here, and in all other works at the time, ignores the optimization of other
agents.» Multi-agent trading «becomes a multiplayer stochastic game, and, in general, such problems
cannot be solved in closed form. Instead, the authors make use of the theory of mean-field games
(MFGs) ... to obtain Nash equilibria for the infinite-player game, and demonstrate that the MFG
solution leads to $\epsilon$-Nash equilibria for the finite-player version of the game.» (p. 692).
Works named: Cartea–Jaimungal 2016 on order flow [16], Huang–Jaimungal–Nourian [34],
Cardaliaguet–Lehalle [10], Huang–Caines–Malhamé [33], Lasry–Lions [39].

### 11. ⭐ New Section 7: tracking problems and latent factors; machine learning as a complement to control (p. 692)

VWAP and rate-tracking problems [29, 26, 15, 4]. Latent factors: Casgrain–Jaimungal [20] derive
«closed-form optimal strategies under a general class of Markov-modulated diffusion and counting
process models ... while the mathematical results are in closed form, estimation and implementation
of the strategy require use of machine-learning tools ... This integration of machine learning and
stochastic control is a very exciting and promising direction of research.» (p. 692).

### 12. ⭐ New Section 7: latent factors plus heterogeneous agents, solved by FBSDEs from convex analysis (pp. 692–693)

Casgrain–Jaimungal [21]: prices adapted to a large filtration $\mathcal G$, agents to a coarser
$\mathcal F\subseteq\mathcal G$, several subpopulations with different criteria; «by using methods
of convex analysis (rather than using the dynamic programming principle, or the stochastic
Pontryagin maximum principle), in obtaining forward-backward SDEs (FBSDEs)», solved, with an
$\epsilon$-Nash result (pp. 692–693).

### 13. ⭐⭐ The new section is silent on Hawkes market making after 2014 (pp. 692–693, reader's observation)

None of the four "new developments" concerns mutually exciting order flow, non-exponential
kernels, several assets, or the accuracy of the first-order expansion. The model of this paper is
not extended; the section points away from it (games, tracking, latent factors). The authors'
own open items are the 2014 ones, repeated in the Conclusions: «We leave for future research the
optimal control problem where HFTs can submit both passive and aggressive orders» (p. 693), and
manipulation by orders sent «in the hope of being perceived as influential» (p. 694).

### 14. Exact feedback forms exist only for exponential and power fill probabilities (pp. 697–698)

Proposition C.1: for $h=e^{-\kappa\delta}$, $\delta^\pm=\max\{1/\kappa^\pm-(\mathbb S_{q\lambda}g-\mathbb S_\lambda g),0\}$ (C.1a);
for power FPs (C.1b). These are feedback forms in terms of the unknown $g$, not solutions. Unchanged.

### 15. Printed inconsistencies of 2014 survive; one is new (pp. 679, 688–689, 694, 698, 701)

Still present: Section 6 and p. 688 cite «Proposition C.2» for $b_\phi$, which is Proposition C.3
(p. 699); power FP written $[1+(\kappa\delta)^\alpha]^{-1}$ in Example C.5 (p. 700) but
$(1+\kappa\delta)^{\alpha}$ in Proposition C.1(2) (p. 698); footnote 18 refers to an undefined $A_0$
(p. 701); the Appendix D step-6 update gives a buy MO the jump $\nu$ on the buy side, the reverse of
(2.2b) (p. 701). New: Fig. 1 says «two-second sliding window» (p. 679) and Appendix A integrates
over «the last two seconds», but then compares with «the one-second historical intensity in
Figure 1» (p. 694). (Reader's observations.)

## Differences from the 2014 version

| Item | 2014 (SIFIN 5:415–444) | 2018 (SIREV 60:673–703) |
|---|---|---|
| Title | Buy Low, Sell High: A High Frequency Trading Perspective | Algorithmic Trading, Stochastic Control, and Mutually Exciting Processes |
| Model, HJB, expansion, Theorem 5.2, Cor. 5.3, App. B–D | — | identical (same numbering) |
| Data example (Fig. 1) | IBM, 1 Feb 2008, 3:30–3:33 pm, 1-s window | INTC, 29 Jan 2018, 9:30–9:33 am, 2-s window (p. 679) |
| $\rho=1$ MLE (App. A) | $\hat\beta=180.05,\hat\theta=2.16,\hat\eta=64.16,\hat\nu=55.73$ | $\hat\beta=3{,}774,\hat\theta=0.22,\hat\eta=2{,}766,\hat\nu=54$ (p. 694) |
| Implied branching ratio (reader) | ≈ 0.67, cross ≈ self | ≈ 0.75, cross ≈ 2% of self |
| Simulation tables | Tables 1–3 ($\varepsilon=0.04$; $\varepsilon=0.02$; $\rho=0.3$) | Table 1 only (pp. 691) |
| "New Developments" section | — | Section 7 (pp. 692–693): MFG/games, VWAP, latent factors + ML, partial-information MFG |
| Conclusions | Section 7 | Section 8, same content |
| References | [1]–[32] | [1]–[44], with "Cited on p." |
| Running-penalty interpretation | via [12] (ambiguity aversion) | via [11], Cartea–Donnelly–Jaimungal 2017 (p. 685) |
| Cartea's affiliation | UCL | Oxford |
| Printed slips | Prop. C.2/C.3, $A_0$, step-6 swap, power-FP form | same, plus the 1-s/2-s window mismatch |

## What this source does not address

- **Anything the 2014 page lists as absent**: several assets, cross-asset excitation, non-exponential
  kernels, fill-driven excitation, CARA utility, a terminal liquidation penalty in the objective, an
  exact numerical benchmark or regret, a validity proof of the expansion (see
  [[cartea-2014-buy-low-sell]], "What this source does not address"). Nothing of that is added.
- **Post-2014 Hawkes market-making work.** The new section cites none of it (Kernthese 13).
- **The robustness checks removed from 2014**: the weak-alpha case ($\varepsilon=0.02$) and the
  low-influence case ($\rho=0.3$) are no longer in this version; for them use the 2014 page.
- **A full calibration with $\rho<1$.** Still «beyond the scope of this work and will be reported on
  elsewhere» (p. 694).

## Model card

- **Assets:** 1 (one stock; buy and sell sides).
- **Kernel:** single exponential (decay $\beta$ for MO intensity, $\xi$ for LOB shape, $\zeta$ for
  short-term alpha); marked bivariate exponential Hawkes.
- **Excitation:** self-side ($\eta$) and cross-side ($\nu$), only by influential MOs (probability
  $\rho$); influential MOs also excite the LOB depth $\kappa^\pm$ (one-way) and the drift $\alpha$. No
  cross-asset excitation.
- **Who excites:** all influential market orders, filled or not; the agent's fills are thinnings.
- **Objective:** expected terminal wealth minus running penalty $\phi\int q^2$ (5.2); no CARA.
- **Solution method:** Markov HJB (5.3); first-order expansion in $\varsigma$ → linear PIDEs →
  Feynman–Kac → closed-form quotes (5.12)–(5.13) via matrix exponentials.
- **Benchmark:** simulation of six HFTs differing in assumed $\rho$ and alpha model (Table 1); the
  correctly specified first-order strategy is the "benchmark". No exact optimum.
- **Reported numbers:** PnL mean (std), Table 1 only, e.g. 14.09 (6.98) vs −3.81 (2.83)
  ($\phi=10^{-5}$, 1 bp, p. 691). Regret / gap: n/a — no exact solution computed. New: INTC 2018
  $\rho=1$ fit (p. 694).

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 2, 3, 4, 5, 7, 10, 13.**

### What this focus needs beyond the Kernthesen

1. **For the closure, cite either version; the content is the same.** The linear (not Riccati)
   closure, the affine-in-$\lambda$ coefficient $b_\phi$, and the flow-driven convention are
   stated identically in both. All focus material on the 2014 page ("What this focus needs beyond the
   Kernthesen", items 1–7 there) applies with 2018 page numbers: Lemma 2.1 p. 681; HJB (5.3)
   p. 685; Prop. 5.1 p. 686; Thm. 5.2 p. 687; Cor. 5.3 p. 688; (5.13) p. 689; (B.2) p. 695;
   (C.7)–(C.8) p. 699. Cite 2018 when a reader needs the accessible SIAM Review version; cite 2014
   for the robustness tables.
2. **The new calibration changes what "cross-side excitation" looks like in data.** On INTC 2018 the
   fitted $K$ (reader's mapping, $\rho=1$) is $\tfrac1{\hat\beta}\begin{pmatrix}\hat\eta&\hat\nu\\\hat\nu&\hat\eta\end{pmatrix}\approx\begin{pmatrix}0.733&0.014\\0.014&0.733\end{pmatrix}$:
   almost diagonal, so the symmetric and antisymmetric eigenvalues of $A=\hat\beta(I-K)$ are
   close ($\hat\beta-\hat\eta-\hat\nu\approx954$ and $\hat\beta-\hat\eta+\hat\nu\approx1{,}062$ per second). For the quote correction (5.13), whose
   relaxation rate is $\hat\beta-\rho(\eta-\nu)$, this means the imbalance term decays at almost the
   same speed as total activity. On IBM 2008 the two rates were very different. One three-minute
   window per stock; nothing general can be drawn from it.
3. **Time scales.** $1/\hat\beta\approx0.26$ ms on INTC: the excitation dies out far faster than any
   quoting horizon. A first-order expansion with frozen-at-$t$ forecasts then behaves almost like a
   Poisson model with a state-dependent level. This is a reader's inference; the paper draws no such
   conclusion.
4. **Section 7 is not a follow-up on the closure question.** It sets no new problem on mutually
   exciting flow and offers no multi-asset extension. For the project's gap it shows that, in the
   authors' own 2018 view, the frontier had moved to games and partial information, not to
   multi-asset Hawkes market making.

### Direct quotes (for the draft)

> "This paper originally appeared in SIAM Journal on Financial Mathematics, Volume 5, Number 1, 2014, pp. 415--444, as ``Buy Low, Sell High: A High Frequency Trading Perspective.''" (fn. *, p. 673)

> "In general, an exact optimal control is not analytically tractable; two exceptions are the cases of exponential and power FPs, where the optimal control admits exact analytical solutions, as presented in section C.1." (p. 686)

> "For the time window 9:30 am to 9:33 am on January 29, 2018, for INTC the estimated parameters are $\hat\beta = 3{,}774$, $\hat\theta = 0.22$, $\hat\eta = 2{,}766$, and $\hat\nu = 54$." (p. 694)

> "In both cases, the trading problem becomes a multiplayer stochastic game, and, in general, such problems cannot be solved in closed form." (p. 692)

> "This integration of machine learning and stochastic control is a very exciting and promising direction of research." (p. 692)

### Examples & illustrations (for later drafting)

- INTC vs IBM fits as a pair: the same model, two stocks a decade apart, give cross-to-self ratios
  of ≈ 0.02 and ≈ 0.87. A concrete warning that the off-diagonal of $K$ is an empirical quantity,
  not a structural constant.
- Fig. 1 (p. 679): fitted vs historical MO intensity, INTC buy and sell, three minutes.
- Table 1 (p. 691): numbers identical to 2014 Table 1.

### Boundary of this focus

One asset; one exponential kernel; linear closure only; no exact benchmark. The INTC numbers come
from a $\rho=1$ fit on a three-minute window and are biased in the way the authors describe (jumps
understated, p. 694). Differences to 2014 are established by the reader comparing the two PDFs.

## Mentioned entities

- Models: [[cartea-jaimungal-ricci-model]] (this paper restates it), [[glft-2013-model]] (ref. [28]),
  [[avellaneda-stoikov-model]] (ref. [3]).
- Concepts: [[hawkes-process]], [[branching-matrix]], [[intensity-forecast]], [[who-excites-the-flow]].
- Library works cited: `gueant-2013-dealing-inventory-risk` ([28]; see
  [[gueant-2013-dealing-inventory-risk]]), `avellaneda-2008-high-frequency-trading` ([3]),
  `ho-1981-optimal-dealer-pricing` ([32]), `guilbaud-2011-optimal-high-frequency` ([30] is the 2013
  Quant. Finance version).
- New in Section 7, not in the library: Cartea–Jaimungal 2016 (order flow, [16]); Huang–Jaimungal–Nourian
  2015 [34]; Cardaliaguet–Lehalle 2016 [10]; Huang–Caines–Malhamé 2007 [33]; Lasry–Lions 2007 [39];
  Guéant–Royer 2014 [29]; Frei–Westray 2015 [26]; Cartea–Jaimungal 2016 VWAP [15]; Bank–Soner–Voß 2017 [4];
  Casgrain–Jaimungal 2016 [20] and 2018 [21].

## Connections

- Revised reprint of: [[cartea-2014-buy-low-sell]] (read that page for the derivation and the
  robustness tables).
- Cited by: [[barzykin-2026-hawkes-driven-otc]], [[martin-2026-market-making-hawkes]] (both cite this
  2018 version).
- Later work on the same model (cites 2014, not 2018): [[choi-2021-synchronised-order-arrivals]]
  (adds a synchronising drift and solves by deep Galerkin).
- Contrast on closure: [[begv-2021-model]] (multi-asset Riccati, Poisson flow) vs this paper (linear
  expansion, one asset, Hawkes flow).
