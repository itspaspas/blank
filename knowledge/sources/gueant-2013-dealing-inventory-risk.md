---
title: "Guéant–Lehalle–Fernandez-Tapia 2013 — Dealing with the Inventory Risk: A Solution to the Market Making Problem"
type: source
created: 2026-10-25
updated: 2026-10-25
status: review
author: llm
bibkey: gueant-2013-dealing-inventory-risk
depth: deep
tags: [market-making, closed-form, linear-ode, cara, poisson, single-asset, inventory-bounds, spectral-approximation, avellaneda-stoikov, benchmark]
relations:
  - target: glft-2013-model
    type: supports
    confidence: extracted
    because: "This is the original of the model: «the Hamilton–Jacobi–Bellman equations associated to the problem boil down to a system of linear ordinary differential equations» (p. 478); Prop. 1–2, Thm. 1 (pp. 481–482)."
  - target: avellaneda-stoikov-model
    type: builds-on
    confidence: extracted
    because: "«We consider the same model as in [3]—adding inventory limits» (p. 478); the AS approximations are «nothing but the Taylor expansions of the optimal quotes for t close to T» (fn. 8, p. 482)."
  - target: cartea-jaimungal-ricci-model
    type: cites
    confidence: extracted
    because: "«Cartea et al. [8] consider a more sophisticated model inspired from the Avellaneda–Stoikov one, including richer dynamics of market orders ... adverse selection effects» (p. 479); [8] is the 2011 working-paper version of CJR 2014."
  - target: matrix-riccati-equation
    type: mentions
    confidence: inferred
    because: "Not in the source. GLFT closes exactly with a LINEAR ODE v' = Mv (Prop. 2, p. 482), no Riccati step; the later quadratic/Riccati closure (BEGV) is the approximate counterpart once the exact linear system becomes too large."
  - target: hamiltonian-quadratic-approximation
    type: mentions
    confidence: inferred
    because: "Not in the source. GLFT's own closed form comes from a spectral/Gaussian approximation of the ground-state eigenvector (Prop. 3, p. 485), not from expanding the Hamiltonian; the two routes are alternatives."
  - target: hawkes-process
    type: mentions
    confidence: inferred
    because: "Not in the source: fills are Poisson with intensity A e^{-k delta} (p. 480). The page records, as inference, which Hawkes-type intensities would keep the linear structure (focus block)."
  - target: markov-lift
    type: mentions
    confidence: inferred
    because: "Not in the source. Inference on this page: if an exponential-kernel intensity is lifted to a state that jumps ONLY at the maker's own fills, the GLFT power transform still linearises the lifted HJB; uncontrolled jumps or intensity diffusion break it."
  - target: intensity-forecast
    type: mentions
    confidence: inferred
    because: "Not in the source. Inference: with a deterministic time-varying amplitude A(t) the GLFT system stays linear (time-inhomogeneous), so a frozen intensity forecast plugs in exactly at this level."
---

# Dealing with the Inventory Risk: A Solution to the Market Making Problem

## Bibliographic Details

Guéant, Olivier, Charles-Albert Lehalle, and Joaquin Fernandez-Tapia. 2013. "Dealing with the
inventory risk: a solution to the market making problem." *Mathematics and Financial Economics*
7 (4): 477–507. DOI 10.1007/s11579-012-0087-0. Received 31 March 2012, accepted 14 August 2012,
published online 4 September 2012 (p. 477). Affiliations: Université Paris-Diderot (Guéant),
Crédit Agricole Cheuvreux (Lehalle), Université Pierre et Marie Curie (Fernandez-Tapia).

**Read:** the **published journal version** (`library/pdf/gueant-2013-dealing-inventory-risk.pdf`),
in line with the project's preprint policy for B1 core works. All page numbers on this page are
the **journal's printed page numbers (477–507)**. All 31 pages were read, including the appendix of
proofs (pp. 496–506).

**Equation numbering.** The journal version has **no numbered equations**. Results are cited by
the paper's own labels: "(HJB)" (p. 481), Proposition 1–5, Theorem 1–2, Figs. 1–13. Where this
page needs a handle for an unlabelled display, it gives the page and the label in brackets (e.g.
"[spread, Thm. 1]").

### Notation map (source → project, CLAUDE.md § Notation)

| Source symbol | Meaning in source | Project symbol / remark |
|---|---|---|
| $S_t$, $\sigma$, $W_t$ | reference price, $dS_t=\sigma\,dW_t$ (p. 479) | $S_t$, $\sigma$ (here one asset, no $\Sigma$) |
| $q_t=N^b_t-N^a_t$, $Q$ | inventory, inventory bound (pp. 479–480) | $q_t$, $Q$ |
| $X_t$ | cash (p. 480) | $X_t$ |
| $\delta^b,\delta^a$ | quote distances $S_t-S^b_t$, $S^a_t-S_t$ (p. 480) | $\delta^b,\delta^a$ |
| $A$, $k$ | intensity amplitude and decay, $\lambda(\delta)=Ae^{-k\delta}$ (p. 480) | $\Lambda$, $k$ — ⚠ the source's $A$ is the project's $\Lambda$, **not** the project's quadratic coefficient $A$ |
| $\lambda^b(\delta^b),\lambda^a(\delta^a)$ | fill intensities (p. 480) | $\Lambda e^{-k\delta}$ — ⚠ not the Hawkes intensity $\lambda_t$ |
| $\gamma$ | CARA absolute risk aversion (p. 480) | $\gamma$ |
| $u(t,x,q,s)$ | value function (p. 481) | $u=-\exp(-\gamma(x+qs+\theta(t,q)))$ with $\theta=\tfrac1k\ln v_q$ (derived, not the source's notation) |
| $v_q(t)$, $v(t)$ | transformed value, $u=-e^{-\gamma(x+qs)}v_q^{-\gamma/k}$ (Prop. 1) | no project symbol; $\theta=\tfrac1k\ln v_q$ |
| $\alpha=\tfrac k2\gamma\sigma^2$, $\eta=A(1+\tfrac\gamma k)^{-(1+k/\gamma)}$ | ODE coefficients (Prop. 1) | — |
| $M$ | $(2Q+1)\times(2Q+1)$ tridiagonal matrix (Prop. 2) | — |
| $f^0$, $\tilde f^0$ | ground-state eigenvector of $M$; its continuous Gaussian surrogate (Thm. 2, Prop. 3) | — |
| $\psi^*$, $\delta^{b*}_\infty,\delta^{a*}_\infty,\psi^*_\infty$ | spread; asymptotic ($T\to\infty$) quotes and spread | — |
| $\mu$, $\beta=k\mu$ | price drift and its ODE coefficient (Prop. 4) | ⚠ clash with Hawkes baseline $\mu$ and decay $\beta$ |
| $\xi$ | permanent impact per fill / adverse selection (Prop. 5) | — |
| $\lambda$, $\lambda^i$, $g^i$ | eigenvalues / eigenvectors of $M$ (proof of Thm. 2, pp. 502–503) | ⚠ clash with Hawkes $\lambda_t$ |
| $\Delta$ | order size (fn. 5) | — |

<!-- ═══ ERSCHLIESSUNG ═══ -->

## Section map

| Covered | Section | pp. |
|---|---|---|
| ✓ F1 | Abstract, keywords | 477 |
| ✓ F1 | 1 Introduction (Ho–Stoll, Avellaneda–Stoikov, contributions, related work) | 478–479 |
| ✓ F1 | 2 Setup of the model (Brownian reference price, $Ae^{-k\delta}$ fills, cash, bound $Q$, CARA objective) | 479–480 |
| ✓ F1 | 3 Characterization of the optimal quotes ((HJB), Prop. 1, Prop. 2, Thm. 1) | 480–482 |
| ✓ F1 | 4 Asymptotic behavior and approximation of the optimal quotes (Figs. 1–3, Thm. 2, Prop. 3, Figs. 4–5) | 482–485 |
| ✓ F1 | 5 Extensions of the model — 5.1 The case of a trend in the price dynamics (Prop. 4) | 485–487 |
| ✓ F1 | 5.2 The case of market impact (Prop. 5) | 487–489 |
| ✓ F1 | 6 Comparative statics — 6.1 $\sigma^2$, 6.2 $\mu$, 6.3 $A$, 6.4 $\gamma$, 6.5 $k$, 6.6 market impact $\xi$ (Figs. 6–8) | 489–493 |
| ✓ F1 | 7 Backtests (France Telecom, 15 March 2012; Figs. 9–13) | 493–495 |
| ✓ F1 | 8 Conclusion (AS PDE, future work: general intensities, passive impact) | 495–496 |
| ✓ F1 | Appendix: proofs of Props. 1–2 and Thm. 1 (positivity, verification) | 496–501 |
| ✓ F1 | Appendix: proof of Thm. 2 (Perron-type argument, spectral decomposition) | 502–503 |
| ✓ F1 | Appendix: proof of Prop. 3 (compact operator, Gaussian ground state) | 503–506 |
| — | References | 506–507 |

## Kernthesen

### 1. ⭐⭐ Under exponential fill intensities, CARA utility and an inventory bound, the HJB system of the Avellaneda–Stoikov problem reduces exactly to a linear ODE system (pp. 478, 480–481, Prop. 1)

The model is the Avellaneda–Stoikov one plus inventory bounds: «We consider the same model as in
[3]—adding inventory limits—and we show, using a new change of variables, that the
Hamilton–Jacobi–Bellman equations associated to the problem boil down to a system of linear
ordinary differential equations» (p. 478). The (HJB) is a system of $2Q+1$ PDEs in $(t,x,s)$ indexed
by $q$ (p. 481), with terminal condition $u(T,x,q,s)=-\exp(-\gamma(x+qs))$. Proposition 1 (p. 481):
if $(v_q)_{|q|\le Q}$ are **positive** functions solving
$\dot v_q=\alpha q^2v_q-\eta(v_{q-1}+v_{q+1})$ for $|q|<Q$, $\dot v_{\pm Q}=\alpha Q^2v_{\pm Q}-\eta v_{\pm(Q-1)}$,
$v_q(T)=1$, with $\alpha=\tfrac k2\gamma\sigma^2$ and $\eta=A(1+\tfrac\gamma k)^{-(1+k/\gamma)}$, then
$u(t,x,q,s)=-\exp(-\gamma(x+qs))\,v_q(t)^{-\gamma/k}$ solves (HJB). The contribution is framed as
practical as well as theoretical: «This new change of variables (i) simplifies the computation of a
solution since numerical approximation of partial differential equations is now unnecessary, and
(ii) allows to study the asymptotic behavior of the optimal quotes» (p. 478).

### 2. ⭐⭐ The change of variables rests on exactly two ingredients: CARA factors out the mark-to-market, and the exponential intensity turns the Hamiltonian into a power that a power transform linearises (p. 481)

«To solve these equations we will use a change of variables based on two different ideas. First,
the choice of a CARA utility function allows to factor out the Mark-to-Market value of the
portfolio $(x+qs)$. Then, the exponential decay for the intensity functions $\lambda^b$ and
$\lambda^a$ allows to reduce the Hamilton–Jacobi–Bellman (HJB) equations associated to our control
problem to a linear system of ordinary differential equations» (p. 481). The proof (pp. 496–498)
makes the mechanism visible: with $u=-e^{-\gamma(x+qs)}v_q^{-\gamma/k}$ the bid Hamiltonian equals
$-\tfrac{\gamma A}{k+\gamma}(1+\tfrac\gamma k)^{-k/\gamma}\tfrac{v_{q+1}(t)}{v_q(t)}\,u$ (p. 497) — i.e.
**linear in $v_{q+1}$ after division by the common factor**. The same exponent $-\gamma/k$ must work
for both sides, so $k$ is common to bid and ask.

### 3. ⭐⭐ The linear system is solved by a matrix exponential of a symmetric tridiagonal matrix (p. 482, Prop. 2)

$M$ has diagonal $\alpha q^2$ for $q=Q,\dots,-Q$ (i.e. $\alpha Q^2,\alpha(Q-1)^2,\dots,\alpha Q^2$) and
$-\eta$ on both off-diagonals (p. 482). With
$v(t)=(v_{-Q}(t),\dots,v_Q(t))'=\exp(-M(T-t))\times(1,\dots,1)'$, «$(v_q)_{|q|\le Q}$ is a family of
positive functions solution of the equations of Proposition 1» (Prop. 2, p. 482). The whole optimal
control problem therefore costs one $(2Q+1)$-dimensional matrix exponential per time point.

### 4. ⭐ Positivity of $v$ is the load-bearing technical step, shown by an explicit lower bound (pp. 498–499)

«The positivity of the functions $(v_q)_{|q|\le Q}$ was essential in the definition of $u$» (p. 498),
since $v_q^{-\gamma/k}$ must exist. The appendix proves
$v_q(t)\ge e^{-(\alpha Q^2-\eta)(T-t)}>0$ for all $t,q$ by a minimum-principle contradiction argument
on $e^{-2\eta(T-t)}(v_q(t)-e^{-(\alpha Q^2-\eta)(T-t)})+\epsilon(T-t)$, treating $|q|<Q$, $q=Q$ and
$q=-Q$ separately (pp. 498–499). (Structurally, positivity follows because $-M$ has non-negative
off-diagonal entries — our remark, not the paper's argument.)

### 5. ⭐⭐ The optimal quotes are explicit in the ratios of neighbouring $v_q$ (Thm. 1, p. 482)

Theorem 1: $u$ is the value function and
$\delta^{b*}(t,q)=\tfrac1k\ln\tfrac{v_q(t)}{v_{q+1}(t)}+\tfrac1\gamma\ln(1+\tfrac\gamma k)$ for $q\ne Q$,
$\delta^{a*}(t,q)=\tfrac1k\ln\tfrac{v_q(t)}{v_{q-1}(t)}+\tfrac1\gamma\ln(1+\tfrac\gamma k)$ for $q\ne-Q$,
with spread
$\psi^*(t,q)=-\tfrac1k\ln\tfrac{v_{q+1}(t)v_{q-1}(t)}{v_q(t)^2}+\tfrac2\gamma\ln(1+\tfrac\gamma k)$, $|q|\ne Q$
(p. 482). Each quote is a static term $\tfrac1\gamma\ln(1+\tfrac\gamma k)$ plus an inventory term that
is a finite difference of $\theta=\tfrac1k\ln v$. The first-order condition
$(k+\gamma)\exp(-\gamma\delta^{b*})(v_{q+1}/v_q)^{-\gamma/k}=k$ «corresponds to a maximum (because $u$ is
negative)» (p. 496).

### 6. ⭐ The inventory bound is what makes the problem rigorously solvable; at the bound one side is not quoted (p. 480)

«we assume that a market maker with inventory $Q$ ... will never set a bid quote and symmetrically
that a market maker with inventory $-Q$ ... will never set an ask quote. This realistic restriction
may be read as a risk limit and allows to solve rigorously the problem» (p. 480). It enters (HJB) as
the two boundary equations and $M$ as the truncation of an infinite tridiagonal operator. It is also
what bounds $\int q\,dW$ in the verification proof (Kernthese 8).

### 7. ⭐⭐ The paper supplies the verification theorem missing from Avellaneda–Stoikov; without inventory limits optimality of the AS quotes is open (pp. 478, 496)

«Finally, we provide in the case of our model with inventory limits a verification theorem that was
absent from the original article (the admissibility of the quotes obtained in the original
Avellaneda–Stoikov model appears in fact to be an open problem!)» (p. 478). The conclusion repeats:
the change of variables also solves the original AS equations ([12], Guéant–Lehalle working paper),
«However, in the absence of inventory limits, no proof of optimality is available for the quotes
claimed to be optimal in [3] and their admissibility appears to be an open problem» (p. 496).

### 8. The verification argument uses bounded-below quotes, bounded intensities, a localisation and Girsanov via $|q|\le Q$ (pp. 499–501)

Admissible controls $\mathcal A$ are «predictable processes bounded from below» (p. 480), so
intensities $Ae^{-k\delta}\mathbf 1_{q<Q}$ are bounded: «These intensities are bounded since
$\delta^b$ and $\delta^a$ are bounded from below» (fn. 13, p. 499). Itô's formula is applied up to a
stopping time $t_n$; local martingales are true martingales because $v_q$ has a positive lower bound
on a compact set (p. 500). Uniform integrability is obtained by an $L^2$ bound on
$\exp(-\gamma(X+qS))$, split by Hölder into two point-process Laplace transforms and
$\mathbb E[\exp(-6\gamma\int q\,dW)]^{1/3}\le\exp(3\gamma^2\sigma^2Q^2T)$, «because $|q_t|$ is bounded by
$Q$, we know (for instance applying Girsanov's theorem)» (p. 501). The optimal quotes are admissible
«because $v$ is bounded and has a positive lower bound» (p. 500).

### 9. ⭐ Far from the horizon the optimal quotes are almost time-independent; the AS approximations are only Taylor expansions near $T$ (pp. 482–484, fn. 8, Figs. 1–3)

«We clearly see that the optimal quotes are almost independent of $t$, as soon as $t$ is far from the
terminal time $T$. This observation is at odds with the approximations proposed in Avellaneda and
Stoikov [3] using an expansion in $q$» (pp. 482–483). The AS approximations
$\delta^{b*}_t\simeq\tfrac1\gamma\ln(1+\tfrac\gamma k)+\tfrac{1+2q}2\gamma\sigma^2(T-t)$ (and ask
analogue) are «nothing but the Taylor expansions of the optimal quotes for $t$ close to $T$» (fn. 8,
p. 482). Figs. 1–3 (σ = 0.3 Tick s⁻¹ᐟ², A = 0.9 s⁻¹, k = 0.3 Tick⁻¹, γ = 0.01 Tick⁻¹, T = 600 s) show
bid/ask quotes between roughly 1 and 5.5 ticks and a spread between ≈6.55 and ≈6.64 ticks
(pp. 483–484).

### 10. ⭐⭐ The $T\to\infty$ quotes are given by the ground-state eigenvector of $M$ (Thm. 2, pp. 483–484)

Theorem 2: $\lim_{T\to+\infty}\delta^{b*}(0,q)=\delta^{b*}_\infty(q)=\tfrac1\gamma\ln(1+\tfrac\gamma k)+\tfrac1k\ln\tfrac{f^0_q}{f^0_{q+1}}$,
$\delta^{a*}_\infty(q)=\tfrac1\gamma\ln(1+\tfrac\gamma k)+\tfrac1k\ln\tfrac{f^0_q}{f^0_{q-1}}$, where
«$f^0\in\mathbb R^{2Q+1}$ is an eigenvector corresponding to the smallest eigenvalue of the matrix $M$
introduced in Proposition 2 and characterized (up to a multiplicative constant) by»
$f^0\in\arg\min_{\|f\|_2=1}\sum_{q=-Q}^{Q}\alpha q^2f_q^2+\eta\sum_{q=-Q}^{Q-1}(f_{q+1}-f_q)^2+\eta f_Q^2+\eta f_{-Q}^2$
(p. 484). The asymptotic spread is
$\psi^*_\infty(q)=-\tfrac1k\ln\tfrac{f^0_{q+1}f^0_{q-1}}{(f^0_q)^2}+\tfrac2\gamma\ln(1+\tfrac\gamma k)$ (p. 484).
The Rayleigh form is $x'(M+2\eta I)x$: a discrete Schrödinger operator with potential $\alpha q^2$
(pp. 484, 502).

### 11. The ground state is positive and simple, and dominates $v(0)$ as $T\to\infty$ (pp. 502–503)

Because $M+2\eta I$ is symmetric, $|x|$ is an eigenvector whenever $x$ is; a zero coordinate
propagates to $x=0$ through the tridiagonal recursion; hence every non-negative ground-state
eigenvector is strictly positive and the eigenvalue is simple (p. 502). Expanding
$v_q(0)=\sum_i\exp(-\lambda^iT)\langle g^i,(1,\dots,1)\rangle g^i_q$ with $g^0=f^0$ gives
$v_q(0)\sim\exp(-\lambda^0T)\langle f^0,(1,\dots,1)\rangle f^0_q$ (pp. 502–503), so the ratios
$v_q/v_{q\pm1}$ converge to $f^0_q/f^0_{q\pm1}$. The rate is set by the spectral gap
$\lambda^1-\lambda^0$, which the paper does not compute (see focus block).

### 12. ⭐ Replacing the discrete eigenproblem by a continuous harmonic-oscillator problem gives a Gaussian ground state in closed form (Prop. 3, pp. 484–485)

The criterion is replaced by $\tilde f^0\in\arg\min_{\|\tilde f\|_{L^2}=1}\int_{\mathbb R}(\alpha x^2\tilde f(x)^2+\eta\tilde f'(x)^2)\,dx$
(p. 484). Proposition 3: $\tilde f^0(x)=\pm\pi^{-1/4}(\alpha/\eta)^{1/8}\exp(-\tfrac12\sqrt{\alpha/\eta}\,x^2)$
(p. 485). «From the above proposition, we expect $f^0_q$ to behave, up to a multiplicative constant,
as $\exp(-\tfrac12\sqrt{\alpha/\eta}\,q^2)$» (p. 485). The proof (pp. 503–506) builds the Hilbert space
$H=\{u: xu\in L^2, u'\in L^2\}$, shows the compact injection $H\hookrightarrow L^2$, a compact positive
self-adjoint solution operator $L$ of $-u''+x^2u=f$ (with weights), and that the Gaussian spans the
top eigenspace of $L$.

### 13. ⭐⭐ The resulting closed-form quotes are affine in inventory with slope $\sqrt{\sigma^2\gamma/(2kA)\,(1+\gamma/k)^{1+k/\gamma}}$ (p. 485)

Plugging the Gaussian into Thm. 2 (p. 485):
$\delta^{b*}_\infty(q)\simeq\tfrac1\gamma\ln(1+\tfrac\gamma k)+\tfrac{2q+1}2\sqrt{\tfrac{\sigma^2\gamma}{2kA}(1+\tfrac\gamma k)^{1+k/\gamma}}$,
$\delta^{a*}_\infty(q)\simeq\tfrac1\gamma\ln(1+\tfrac\gamma k)-\tfrac{2q-1}2\sqrt{\tfrac{\sigma^2\gamma}{2kA}(1+\tfrac\gamma k)^{1+k/\gamma}}$,
$\psi^*_\infty(q)\simeq\tfrac2\gamma\ln(1+\tfrac\gamma k)+\sqrt{\tfrac{\sigma^2\gamma}{2kA}(1+\tfrac\gamma k)^{1+k/\gamma}}$
— the spread is inventory-independent, the skew linear in $q$. Equivalent form:
$\tfrac1{2k}\sqrt{\alpha/\eta}\,(2q\pm1)$. «Empirically, these approximations for the quotes are
satisfactory in most cases and are always very good for small values of the inventory $q$» (p. 485).
This is the formula the later literature calls "the GLFT closed form".

### 14. The approximation degrades at large $|q|$ because it approximates ratios of eigenvector entries (p. 485, Figs. 4–5)

«even though $f^0$ appears to be well approximated by the gaussian approximation, we cannot expect a
very good fit for the quotes when $q$ is large because we are approximating expressions that depend
on ratios of the form $f^0_q/f^0_{q+1}$ or $f^0_q/f^0_{q-1}$» (p. 485). Figs. 4–5 (p. 486): with
σ = 0.4, A = 0.9, k = 0.3, γ = 0.01, T = 600 the exact and approximate bid curves separate visibly
near $|q|=30$; with σ = 1.0, A = 0.2 they are almost indistinguishable over $[-30,30]$. The
boundary $\pm Q$ — absent from the Gaussian on $\mathbb R$ — is the obvious source of the edge error
(our reading).

### 15. ⭐ A price drift keeps the linear structure; it only adds a term linear in $q$ to the diagonal (Prop. 4, pp. 485–487)

With $dS_t=\mu\,dt+\sigma\,dW_t$, Proposition 4 (p. 486, «the proof is not repeated», p. 485):
$\dot v_q=(\alpha q^2-\beta q)v_q-\eta(v_{q-1}+v_{q+1})$, $\beta=k\mu$, same terminal condition, same
quote formulas; asymptotics use the smallest eigenvalue of the matrix with diagonal
$\alpha q^2-\beta q$ (p. 487). Approximation (p. 487):
$\delta^{b*}_\infty(q)\simeq\tfrac1\gamma\ln(1+\tfrac\gamma k)+[-\tfrac{\mu}{\gamma\sigma^2}+\tfrac{2q+1}2]\sqrt{\cdot}$,
$\delta^{a*}_\infty(q)\simeq\tfrac1\gamma\ln(1+\tfrac\gamma k)+[\tfrac{\mu}{\gamma\sigma^2}-\tfrac{2q-1}2]\sqrt{\cdot}$:
the drift shifts the inventory "target" by $\mu/(\gamma\sigma^2)$ (our interpretation). The spread
approximation is unchanged.

### 16. ⭐ Permanent market impact / adverse selection on fills also keeps the linear structure, via a slightly modified transform (Prop. 5, pp. 487–489)

With $dS_t=\sigma\,dW_t+\xi\,dN^a_t-\xi\,dN^b_t$, $\xi>0$ (p. 487) — «Adverse selection is another way
to interpret the interaction we consider between the price process and the point processes modeling
execution» (p. 487) — «the problem can be solved using a change of variables that is slightly more
involved than the one presented above but the method is exactly the same» (p. 488). Proposition 5:
$u=-\exp(-\gamma(x+qs+\tfrac12\xi q^2))v_q(t)^{-\gamma/k}$, $\dot v_q=\alpha q^2v_q-\eta e^{-\frac k2\xi}(v_{q-1}+v_{q+1})$,
terminal $v_q(T)=\exp(-\tfrac12k\xi q^2)$; quotes gain $+\xi/2$ on each side and the spread $+\xi$
(p. 488). Note that the price here **jumps at the maker's own fills** — the one place in the paper
where a fill feeds back into a state variable, and linearity survives.

### 17. Adverse selection has a direct ($\xi/2$) and an inventory side-effect ($e^{\frac k4\xi}$) on the quotes (pp. 489, 492–493)

Approximation (p. 489): $\delta^{b*}_\infty(q)\simeq\tfrac1\gamma\ln(1+\tfrac\gamma k)+\tfrac\xi2+\tfrac{2q+1}2e^{\frac k4\xi}\sqrt{\cdot}$,
spread $\simeq\tfrac2\gamma\ln(1+\tfrac\gamma k)+\xi+e^{\frac k4\xi}\sqrt{\cdot}$. Interpretation (p. 492):
the direct effect «approximately [adds] $\xi/2$ to each optimal quote: the market maker approximately
maintains his profit per round trip on the market but the probability of occurrence of a trade is
reduced», and «since adverse selection gives the market maker an incentive to post orders deeper in
the book, it increases the risk of being stuck with a large inventory» (p. 492), labelled
"adverse selection" and "side-effect" in the display on p. 493.

### 18. Volatility raises the spread and steepens the inventory skew (§6.1, pp. 489–490)

Observed numerically «in accordance with the approximations»: $\partial\delta^{b*}_\infty/\partial\sigma^2<0$
and $\partial\delta^{a*}_\infty/\partial\sigma^2>0$ for $q<0$; both $>0$ at $q=0$; signs reversed for
$q>0$; $\partial\psi^*_\infty/\partial\sigma^2>0$ (p. 489). «The rationale behind this is that an
increase in $\sigma^2$ increases inventory risk» (p. 490). §6.2: drift moves both quotes in the
intuitive direction, $\partial\delta^b/\partial\mu<0$, $\partial\delta^a/\partial\mu>0$ (p. 490).

### 19. The intensity amplitude $A$ acts exactly opposite to $\sigma^2$ (§6.3, p. 490)

«Because of the form of the system of equations that defines $v$, the dependence on $A$ must be the
exact opposite of the dependence on $\sigma^2$» (p. 490); $\partial\psi^*_\infty/\partial A<0$. «An
increase in $A$ indeed increases the frequency of trades and hence reduces the risk of being stuck
with a large inventory ... an increase in $A$ should have the same effect as a decrease in
$\sigma^2$» (p. 490). (In the closed form, $\sigma^2$ and $A$ enter only through $\sigma^2/A$ in the
inventory term.)

### 20. Risk aversion has an ambiguous effect because it penalises two different risks (§6.4, pp. 490–491, Figs. 6–7)

«The market maker faces indeed two different risks that contribute to inventory risk: (i) trades
occur at random times and (ii) the reference price is stochastic. But if risk aversion increases,
the market maker will mitigate the two risks: (i) he may set his quotes closer to one another to
reduce the randomness in execution and (ii) he may widen his spread to reduce price risk» (p. 490).
Fig. 6 (σ = 0.3, A = 0.9, k = 0.3, T = 600, γ ∈ [0, 0.5]) shows the spread varying between ≈4.5
and ≈7 ticks; Fig. 7 (σ = 0.6, A = 0.9, k = 0.9) between ≈1.9 and ≈2.5 ticks, with different shapes
(p. 491).

### 21. A larger $k$ narrows the spread: the "no-volatility" effect dominates the execution-risk effect (§6.5, pp. 491–492, Fig. 8)

The closed forms imply $\partial\psi^*_\infty/\partial k<0$ (p. 492). Two effects interact: when $k$
rises, «trades occur closer to the reference price ... the optimal bid-ask spread has to shrink»,
but «an increase in $k$ also affects the inventory risk since it decreases the probability to be
executed ... an increase in $k$ is also, in some aspects, similar to a decrease in $A$» (p. 492).
«Numerically, we observed that the "no-volatility" effect dominated for the values of the inventory
under consideration» (p. 492; Fig. 8: σ = 0.3, A = 0.9, γ = 0.01, T = 600, k ∈ [0.5, 2]).

### 22. ⭐ Practical use requires discretising price and time, and $A,k$ should depend on the market spread (§7, p. 493)

«the model is continuous in both time and space while the real control problem is intrinsically
discrete in space, because of the tick size, and in time» (p. 493). Quotes are rounded to the nearest
tick; an order of one ATS (average trade size) is left for a period $\Delta t$ unless filled, then
re-quoted (p. 493). «it is well known by practitioners that $A$ and $k$ have to depend at least on
the actual market bid-ask spread. Since we do not explicitly take into account the underlying market,
there is no market bid-ask spread in the model» (p. 493). γ is not calibrated: «we decided in our
backtests to assign $\gamma$ an arbitrary value for which the inventory stayed between −10 and 10
during the day we considered (the unit being the ATS)» (p. 493).

### 23. The backtest is a one-day illustration, deliberately under-specified (§7, pp. 493–495, Figs. 9–13)

France Telecom, 15 March 2012, 10:00–16:00, ATS = 1105 shares (fn. 12); fills assumed whenever a
trade prints at or through the quote (p. 493). «Our goal here is just to exemplify the use of the
model» and «We, voluntarily, do not give full details about the algorithm based on the model»
(p. 493, fn. 11). Read off the plots: inventory stays within about ±7 ATS (Fig. 10), the strategy's
P&L rises to ≈1,200 EUR (Fig. 11), a naive best-quote market maker ends near +400 EUR after swings
between ≈−550 and ≈+650 EUR (Fig. 12) (pp. 494–495). No statistics, no other days. «Adaptations of
our results are in use at Cheuvreux» (p. 479).

### 24. Two directions are named as future research: general intensity functions and passive market impact (p. 496)

«An important topic for future research consists in generalizing the model to any intensity
function. This is particularly important because the exponential form of the intensity is only
suited to liquid stocks with a small bid-ask spread. Another important topic consists in introducing
"passive market impact" (i.e. the perturbations of the price formation process by liquidity
provision). This is a real modeling challenge since no quantitative model for this type of impact has
been proposed in the literature» (p. 496). Fn. 6 notes that «Some authors also used a linear form for
the intensity functions—see [18] for instance» (p. 480).

### 25. Modelling conventions: one stock, exogenous price, unit order size, terminal liquidation at the reference price (pp. 479–480, fns. 2–5, 7)

«We consider a high-frequency market maker operating on a single stock» (p. 479); «we assume that
the size of his orders is small enough to consider price dynamics exogenous» (fn. 2, p. 479); the
Brownian assumption is «almost equivalent to the usual Black-Scholes one» on short horizons (fn. 4);
«The only important hypothesis is the constant size of orders since we can easily replace 1 by any
positive size $\Delta$» (fn. 5, p. 480). Fills $N^b,N^a$ are point processes independent of $W$
(p. 480). Terminal inventory is liquidated at $S_T$; «Our results would be mutatis mutandis the same
if we added a penalization term $-b(|q_T|)$ for the shares remaining at time $T$» (fn. 7, p. 480).

### 26. The same controlled-intensity model is shared with optimal execution with limit orders (p. 479)

«the model we use to find the orders a market maker should optimally send to the market has been
used in a totally different domain of algorithmic trading: optimal execution. Bayraktar and Ludkovski
[4] and Guéant et al. [13] used indeed a similar model to optimally liquidate a portfolio» (p. 479).
Related market-making work cited: Cartea–Jaimungal–Ricci [8] (richer market-order dynamics, impact,
adverse selection, closed-form approximations by first-order Taylor expansion; «The objective function
is different», fn. 1), Cartea–Jaimungal [6,7], Guilbaud–Pham [14,15] (p. 479).

## Figures and tables

- Fig. 1, Fig. 2 (p. 483): optimal bid / ask quote surfaces over time (0–600 s) and inventory (−30…30); σ = 0.3, A = 0.9, k = 0.3, γ = 0.01, T = 600.
- Fig. 3 (p. 484): spread surface, ≈6.55–6.64 ticks, same parameters.
- Figs. 4, 5 (p. 486): asymptotic bid / ask quotes vs Gaussian approximation; left σ = 0.4, A = 0.9; right σ = 1.0, A = 0.2 (k = 0.3, γ = 0.01, T = 600).
- Fig. 6 (p. 491): asymptotic spread vs inventory and γ ∈ [0, 0.5] (σ = 0.3, A = 0.9, k = 0.3).
- Fig. 7 (p. 491): same with σ = 0.6, A = 0.9, k = 0.9.
- Fig. 8 (p. 492): asymptotic bid quote vs inventory and k ∈ [0.5, 2] (σ = 0.3, A = 0.9, γ = 0.01).
- Figs. 9–13 (pp. 494–495): France Telecom price, inventory, model P&L, naive P&L, one-hour quote detail.
- No tables. No figures extracted to `knowledge/assets/` (write scope limited to this page).

## What this source does not address

- **Self- or cross-exciting order flow.** Fill intensities are Poisson with constant amplitude $A$;
  no Hawkes, no stochastic or time-varying intensity anywhere. For Hawkes market making see
  [[barzykin-2026-hawkes-driven-otc]] (Volterra–Riccati, one asset), [[martin-2026-market-making-hawkes]]
  (lifted HJB + PINN), [[acero-2026-hawkes-structured-networks]] (multi-asset network Hawkes) and
  [[jusselin-2021-persistent-order-flow]] (general kernels, path-dependent HJB).
- **Several assets.** «a single stock» (p. 479). The multi-asset version with correlated prices and
  the quadratic/Riccati approximation is [[begv-2021-model]] / [[bergault-2021-closed-form-approximations]].
- **General intensity shapes.** Only $Ae^{-k\delta}$; generalisation is named future work (p. 496).
- **Risk-adjusted (non-CARA) objective.** Only CARA utility; the linear structure is tied to it.
- **Limit-order-book state, market orders, queue position.** Only a reference price and two
  fill intensities; CJR [8] and Guilbaud–Pham [14,15] are cited for richer microstructure (p. 479); see
  [[cartea-2014-buy-low-sell]].
- **Calibration and statistical evaluation.** σ, A, k are said to be calibratable on trade data but
  no estimation is shown; γ is chosen ad hoc; the backtest is one day without statistics (p. 493).
- **Error bounds for the closed-form approximation.** Assessed only visually (Figs. 4–5).

## Model card

| Field | Value |
|---|---|
| Assets | 1 («a single stock», p. 479) |
| Kernel | n/a — Poisson fills, intensity $Ae^{-k\delta}$ with constant $A,k$ (p. 480) |
| Excitation | none (no self, cross-side or cross-asset excitation) |
| Who excites the flow | n/a — no excitation; the only fill feedback is the permanent price impact $\pm\xi$ at the maker's own fills in the §5.2 extension (p. 487) |
| Objective | CARA expected utility $\mathbb E[-\exp(-\gamma(X_T+q_TS_T))]$ (p. 480) |
| Solution method | exact closed form up to a matrix exponential: linear ODE $v(t)=e^{-M(T-t)}\mathbf 1$ (Prop. 2) + verification theorem (Thm. 1); $T\to\infty$ spectral limit (Thm. 2); Gaussian closed-form approximation (Prop. 3) |
| Benchmark | exact quotes vs closed-form approximation (Figs. 4–5, visual); AS approximations shown to be near-$T$ Taylor expansions (fn. 8); backtest vs a naive best-quote maker on one day (Figs. 11–12) |
| Reported regret / gap numbers | none — no regret, no error metric; backtest P&L only read off plots (≈1,200 vs ≈400 EUR) |
| Benchmark parameters | σ = 0.3 Tick s⁻¹ᐟ², A = 0.9 s⁻¹, k = 0.3 Tick⁻¹, γ = 0.01 Tick⁻¹, T = 600 s; $Q$ not stated (plots −30…30) (Figs. 1–3, pp. 483–484) |

<!-- ═══ FOKUS ═══ -->

## Focus: How the source models self-/cross-exciting order flow inside a market-making control problem, where its value-function closure (linear ODE / quadratic-Riccati / lift) holds or breaks, and what of it carries over to several assets with cross-asset excitation. — 2026-10-25

**Carries Kernthesen 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 24, 25.**

The source models **no** exciting flow: it is the Poisson baseline whose exact closure the project
wants to extend. What it supplies is the exact linear closure and the precise list of ingredients it
needs. The reconstruction below follows the paper's steps; everything marked **[inference]** is this
page's analysis, not a claim of the source.

### What this focus needs beyond the Kernthesen

1. **Step-by-step reconstruction of the closure (pp. 481–482, 496–503).**
   (i) *HJB* (p. 481), $|q|<Q$:
   $\partial_tu+\tfrac12\sigma^2\partial^2_{ss}u+\sup_{\delta^b}Ae^{-k\delta^b}[u(t,x-s+\delta^b,q+1,s)-u]+\sup_{\delta^a}Ae^{-k\delta^a}[u(t,x+s+\delta^a,q-1,s)-u]=0$,
   one sup dropped at $q=\pm Q$, $u(T)=-e^{-\gamma(x+qs)}$.
   (ii) *Change of variables* (Prop. 1): $u=-\exp(-\gamma(x+qs))\,v_q(t)^{-\gamma/k}$. CARA removes $x$ and,
   with Brownian $S$, turns $\tfrac12\sigma^2\partial_{ss}$ into the multiplicative term
   $\tfrac{\gamma^2\sigma^2}2q^2u$ (p. 496). The bid sup becomes
   $\sup_\delta Ae^{-k\delta}u[\exp(-\gamma\delta)(v_{q+1}/v_q)^{-\gamma/k}-1]$ (p. 496); FOC gives
   Kernthese 5; the sup's value is $-\tfrac{\gamma A}{k+\gamma}(1+\tfrac\gamma k)^{-k/\gamma}\tfrac{v_{q+1}}{v_q}u$
   (p. 497). Dividing everything by $-\tfrac\gamma k\tfrac{u}{v_q}$ yields
   $\dot v_q-\tfrac{k\gamma\sigma^2}2q^2v_q+A(1+\tfrac\gamma k)^{-(1+k/\gamma)}(v_{q+1}+v_{q-1})=0$ (p. 497).
   (iii) *Why it is linear.* The optimised Hamiltonian is a **power** $w_q^{1+k/\gamma}w_{q+1}^{-k/\gamma}$ of
   $w=v^{-\gamma/k}$; the power transform turns it into $v_q^{-\gamma/k-1}\cdot v_{q+1}$, and the common
   factor $v_q^{-\gamma/k-1}$ also multiplies $\partial_tv_q$ and $q^2v_q$. Required: exponential
   $\delta$-dependence (so the sup is a power), the **same $k$** on both sides (one exponent $-\gamma/k$),
   CARA with an **additive Brownian** price (so $s$ and $x$ factor out and the price risk becomes
   $\alpha q^2$), constant order size, and **every jump of the state is a jump of $q$ produced by
   the controlled fill**. The bound $Q$ is not needed for linearity but for finiteness, positivity
   and verification (Kernthesen 4, 6, 8).
   (iv) *Linear system* (Prop. 2): $\dot v=Mv$, $v(T)=\mathbf 1$, $M=\mathrm{diag}(\alpha q^2)-\eta(\text{shift}_{+1}+\text{shift}_{-1})$
   truncated at $\pm Q$, $\alpha=\tfrac k2\gamma\sigma^2$, $\eta=A(1+\tfrac\gamma k)^{-(1+k/\gamma)}$;
   $v(t)=e^{-M(T-t)}\mathbf 1$.
   (v) *Verification* (Thm. 1, pp. 499–501): Kernthese 8.
   (vi) *Asymptotics* (Thm. 2): ground state $f^0$ of the symmetric $M$; quotes →
   $\tfrac1\gamma\ln(1+\tfrac\gamma k)+\tfrac1k\ln(f^0_q/f^0_{q\pm1})$.
   (vii) *Closed form* (Prop. 3, p. 485): Gaussian $f^0_q\propto e^{-\frac12\sqrt{\alpha/\eta}q^2}$ ⇒
   affine quotes, slope $\tfrac1k\sqrt{\alpha/\eta}$.
2. **[inference] (a) Known deterministic $A(t)$ (and $A^b(t)\ne A^a(t)$): the linear structure
   survives exactly.** Every step in (ii) is pointwise in $t$, so
   $\dot v=M(t)v$ with $\eta(t)=A(t)(1+\tfrac\gamma k)^{-(1+k/\gamma)}$ (side-specific
   $\eta^b(t),\eta^a(t)$ on the upper/lower off-diagonal). What is lost: the plain matrix exponential
   (since $M(t)$ and $M(t')$ do not commute, $v$ is a time-ordered exponential / numerical ODE solve),
   symmetry of $M$ when $A^b\ne A^a$, and the stationary spectral asymptotics of Thm. 2. Positivity
   survives ($-M(t)$ stays off-diagonally non-negative). A time-varying $\sigma(t)$ is equally harmless;
   a time-varying $k(t)$ is **not**, because the exponent $-\gamma/k$ would depend on $t$ and
   $\partial_t(v^{-\gamma/k(t)})$ produces a $v\ln v$ term. This is the basis of the proposal's
   "stage 1" (the [[glft-2013-model]] entity page: «the linear system stays exact along a deterministic
   intensity path (proposal eq. 3)») and is
   why a frozen [[intensity-forecast]] $m_t(u)$ can be inserted as $A(t)$ without approximation at
   this step.
3. **[inference] (b) Random / state-dependent amplitude that jumps after trades: it depends on what
   drives the jumps.** Let $A$ be replaced by $\lambda_t$ with Markov state (e.g. exponential Hawkes,
   $d\lambda=\beta(\mu-\lambda)dt+\text{jumps}$) and take $u=-e^{-\gamma(x+qs)}v(t,q,\lambda)^{-\gamma/k}$.
   - *First-order (deterministic-flow) dynamics of $\lambda$* — the drift $\beta(\mu-\lambda)\partial_\lambda$ is a
     first-order operator, which commutes with the power transform (chain rule): **linear**.
   - *Jumps of $\lambda$ that occur exactly at the maker's own fills* (fill-driven self- or cross-side
     excitation, $(q,\lambda)\to(q\pm1,\lambda+\alpha^{\pm})$): the optimised jump term becomes
     $\eta(\lambda)\,v(t,q\pm1,\lambda+\alpha^{\pm})$ after division by the common factor — **linear**,
     but now a linear transport-jump PDE in $(t,\lambda)$ on the $(2Q+1)$ inventory lattice, not a finite
     ODE system with a constant matrix. This is the same structural reason Prop. 5 (price jumping at
     fills) stays linear (Kernthese 16).
   - *Jumps of $\lambda$ caused by events that do not move $q$* (market-wide orders that miss the quote,
     other assets' trades, exogenous news) add $\lambda'[u(\cdot,\lambda+\alpha)-u(\cdot,\lambda)]$, which in
     $v$ reads $v(\lambda)^{\gamma/k+1}v(\lambda+\alpha)^{-\gamma/k}-v(\lambda)$: **nonlinear**.
   - *Diffusive intensity* (CIR-type): $\partial^2_{\lambda\lambda}(v^{-\gamma/k})$ produces
     $(\partial_\lambda v)^2/v$: **nonlinear**.
   So the GLFT linearisation is compatible with a [[markov-lift]] of an exponential kernel **only** if
   excitation is driven by the maker's fills; flow excited by all orders — the case in
   [[barzykin-2026-hawkes-driven-otc]] (requests drive memory) — breaks it, which is consistent with that
   paper's observation that lifted problems give «transport-jump equations» rather than small closed
   systems.
4. **What the source itself says about extensions (all quoted with pages).** Drift: Prop. 4, «the proof
   is not repeated» (p. 485). Impact / adverse selection: «slightly more involved ... but the method is
   exactly the same» (p. 488). General intensities: future research, exponential form «only suited to
   liquid stocks with a small bid-ask spread» (p. 496). Several assets: **nothing** — the model is «a
   single stock» (p. 479); multi-asset, cross-asset excitation and stochastic intensities are never
   mentioned (checked across all 31 pages).
5. **[inference] Carry-over to several assets with cross-asset excitation.** With $d$ assets, CARA and
   correlated Brownian prices, the price-risk term becomes $\tfrac{k\gamma}2q'\Sigma q\,v_q$, still
   multiplicative, so with a **common $k$** across all assets and sides the same transform gives a
   linear system on the lattice $\{-Q,\dots,Q\}^d$ — size $(2Q+1)^d$, i.e. exact but cursed by
   dimension (this is the gap that [[begv-2021-model]] closes with the quadratic/[[matrix-riccati-equation]]
   approximation; to be checked against [[bergault-2021-closed-form-approximations]]). Adding cross-asset
   Hawkes excitation preserves linearity only in the fill-driven case of point 3, where the state
   becomes $(q,\lambda)\in\{-Q..Q\}^d\times\mathbb R_+^{2d\times\#\text{factors}}$ — a linear but
   high-dimensional PDE; with excitation by all market orders (the economically natural case for
   cross-asset contagion, governed by a [[branching-matrix]] $K$) the exact closure breaks and only
   approximate closures (forecast freezing + quadratic expansion, [[volterra-riccati]]; or neural /
   grid solutions of the lift) remain.

### Direct quotes (for the draft)

> "To solve these equations we will use a change of variables based on two different ideas. First, the choice of a CARA utility function allows to factor out the Mark-to-Market value of the portfolio (x + qs). Then, the exponential decay for the intensity functions λ^b and λ^a allows to reduce the Hamilton–Jacobi–Bellman (HJB) equations associated to our control problem to a linear system of ordinary differential equations" (p. 481)

> "We consider the same model as in [3]—adding inventory limits—and we show, using a new change of variables, that the Hamilton–Jacobi–Bellman equations associated to the problem boil down to a system of linear ordinary differential equations. This new change of variables (i) simplifies the computation of a solution since numerical approximation of partial differential equations is now unnecessary, and (ii) allows to study the asymptotic behavior of the optimal quotes." (p. 478)

> "In this modified framework, the problem can be solved using a change of variables that is slightly more involved than the one presented above but the method is exactly the same" (p. 488)

> "An important topic for future research consists in generalizing the model to any intensity function. This is particularly important because the exponential form of the intensity is only suited to liquid stocks with a small bid-ask spread." (p. 496)

> "Empirically, these approximations for the quotes are satisfactory in most cases and are always very good for small values of the inventory q. In fact, even though f^0 appears to be well approximated by the gaussian approximation, we cannot expect a very good fit for the quotes when q is large because we are approximating expressions that depend on ratios of the form f^0_q/f^0_{q+1} or f^0_q/f^0_{q−1}." (p. 485)

### Examples & illustrations (for later drafting)

- **Benchmark parameters (Figs. 1–3, pp. 483–484):** σ = 0.3 Tick·s⁻¹ᐟ², A = 0.9 s⁻¹, k = 0.3 Tick⁻¹,
  γ = 0.01 Tick⁻¹, T = 600 s. **$Q$ is not stated**; the plots span inventory −30…30. These match
  the proposal's benchmark (σ = 0.3, Λ = 0.9, k = 0.3, γ = 0.01, T = 600) exactly, with source $A$ =
  project $\Lambda$. Reproduction (this ingest, numpy/scipy, $Q=30$; not in the paper): $\alpha=1.35\cdot10^{-4}$,
  $\eta=0.3257$; at $q=0$, $t=0$: $\delta^b=\delta^a=3.313$ ticks, spread 6.626 (closed form 6.626;
  at $t=T$: 3.279 / 6.558), matching the 6.55–6.64 range of Fig. 3; spectral gap
  $\lambda^1-\lambda^0\approx0.0132\,\mathrm s^{-1}$, i.e. convergence time scale ≈ 76 s ≪ 600 s, which
  explains the flat-in-$t$ surfaces. Closed form vs exact bid at $t=0$: $q=0$: 3.313 vs 3.313;
  $q=\pm10$: error ≤ 0.002; $q=\pm20$: ≤ 0.005; $q=-29$: 1.345 vs 1.134 and $q=29$: 5.281 vs 6.131
  with $Q=30$ — the edge error comes from the boundary. With $Q\ge35$ the exact edge values become
  1.364 / 5.259 and the Fig. 1 surface (≈1–5.5 ticks, no edge kink) is better matched, so **the figures
  were probably computed with $Q>30$** (inference).
- **Prop. 5 as the model of "state jumps at own fills that keep linearity"** (pp. 487–489): price jumps
  ±ξ at the maker's fills, transform absorbs $\tfrac12\xi q^2$, ODE stays linear with $\eta e^{-k\xi/2}$.
- **Backtest** (pp. 493–495): France Telecom, 15 Mar 2012; model P&L ≈ +1,200 EUR vs naive ≈ +400 EUR
  (read off Figs. 11–12), inventory within ±7 ATS.

### Boundary of this focus

The source contains no excitation, no intensity state and no multi-asset structure; every statement
on this page about Hawkes intensities, lifts and several assets is the project's derivation from the
paper's mechanism (marked [inference]) and should be checked against
[[bergault-2021-closed-form-approximations]] (multi-asset, common-$k$ linear case) and
[[jusselin-2021-persistent-order-flow]] / [[martin-2026-market-making-hawkes]] (lifted Hawkes HJBs). The
paper gives no error bound for its closed form and no regret numbers.

## Mentioned entities

- Models: [[glft-2013-model]] (this paper), [[avellaneda-stoikov-model]], [[cartea-jaimungal-ricci-model]] (cited as the 2011 working paper [8]), [[begv-2021-model]] (later multi-asset extension; not cited — postdates the paper)
- Concepts: [[matrix-riccati-equation]], [[hamiltonian-quadratic-approximation]], [[hawkes-process]], [[markov-lift]], [[intensity-forecast]], [[branching-matrix]], [[volterra-riccati]] (all used only in this page's inference, not in the source)
- Other works (bibkeys): `avellaneda-2008-high-frequency-trading`, `ho-1981-optimal-dealer-pricing`, `cartea-2014-buy-low-sell` ([8], cited as 2011 WP), `bergault-2021-closed-form-approximations`, `jusselin-2021-persistent-order-flow`; not in the library: Guéant–Lehalle 2012 "Existence and uniqueness for the Avellaneda–Stoikov PDE" [12], Guéant–Lehalle–Fernandez-Tapia "Optimal execution with limit orders" [13], Bayraktar–Ludkovski 2011 [4], Guilbaud–Pham [14,15], Cartea–Jaimungal [6,7], Menkveld 2010 [22].

## Connections

- Builds on: [[avellaneda-stoikov-model]] (same model plus inventory bounds; AS approximations = Taylor expansion near $T$, fn. 8, p. 482).
- Defines / supports: [[glft-2013-model]].
- Cites: [[cartea-jaimungal-ricci-model]] (p. 479) — see [[cartea-2014-buy-low-sell]].
- Cited as lineage by: [[barzykin-2026-hawkes-driven-otc]] (p. 1), [[martin-2026-market-making-hawkes]], [[acero-2026-hawkes-structured-networks]], [[bergault-2024-price-aware-automated]].
- Extended by (not cited, later): [[begv-2021-model]] / [[bergault-2021-closed-form-approximations]] — multi-asset, quadratic/Riccati closure.
- Compare (inference): [[markov-lift]], [[intensity-forecast]], [[hawkes-process]] — which Hawkes extensions preserve the linear closure (focus block, points 2–5).
