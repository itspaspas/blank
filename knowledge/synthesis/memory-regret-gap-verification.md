---
title: "Memory-regret gap: verification against the full texts and the fixed search protocol"
type: synthesis
created: 2026-11-01
updated: 2026-11-01
status: draft
author: mixed
tags: [market-making, hawkes, power-law-kernel, markov-lift, regret, novelty-check, lai2023-gaps-and-memory]
---

# Memory-regret gap: verification against the full texts and the fixed search protocol

**Question (plan `lai2023-gaps-and-memory`, Task 2):** has anyone already reported regret or reward
**versus the number p of exponential memory factors** on a power-law (or fractional) Hawkes truth,
with an exact or near-exact reference, **and** a second-order regret law? If so, the gap is closed
and the plan stops before Task 3 (stop rule).

**The gap, in three parts** (design §Re-evaluation; plan header):
1. a *predictive, second-order* regret law, $r \approx \tfrac12\,\mathbb E\iint K(u,v)\,\Delta m(u)\,\Delta m(v)\,du\,dv$;
2. a table of regret versus $p$ on a power-law truth, with the control-approximation error
   reported separately from the memory-truncation error;
3. a map of where memory is irrelevant (Acero's "tie" regime) and where it is not.

Tags: **[S]** stated in the source, with page · **[D]** derived here · **[I]** inference.

## The two closest works, re-ingested under the focus «p-sweep / error theory» (2026-11-01)

### [[barzykin-2026-hawkes-driven-otc]] — does not close the gap
- **[S] p is never swept.** §5 validates the hierarchy for **one** exponential factor. §6.2's
  "power-law-like" memory is a **fixed** 8-exponential mixture (decays $\beta_n$ log-spaced on
  $[2,2500]$, $w_n\propto\beta_n^{-0.65}$, pp. 18–20). Only the burst size varies (Fig. 7, p. 21).
- **[S] No exact long-memory reference:** «we do not solve a lifted HJB in the exponential
  factors» (p. 19); «an exact lifted benchmark is not available at comparable complexity» (p. 21).
  §6.2 compares against Poisson only and reports risk reduction, not regret.
- **[S] No regret law.** The curvature kernel $K_{ij}(t,q;u,v)$ of eq. (36) enters only the
  covariance correction, eq. (38). «a general error or convergence theory remains open» (p. 22).
- **[S] Table 3 (p. 16)** gives the control-approximation floors that the plan's Task 5 gate must
  respect. Relative regret in % (benign / near-critical / directional):
  - mean VR: 0.182 / 0.884 / 2.498
  - noise-aware: 0.151 / 0.513 / 2.159
  - state-feedback: 0.080 / 0.083 / 0.170
  - Poisson: 6.138 / 12.742 / 27.312
- **[I] Notes for later tasks** (the re-ingest agent's inferences, not the source's):
  - The common-mode side intensity is not stated. $\lambda^s=\mu^s+x$ would be supercritical at
    the Table 2 values, so $\mu^s+x/2$ is the reading that keeps $\eta$ the branching ratio.
    Tier 0 uses the equivalent convention $\Phi=(g/2)\mathbf 1\mathbf 1^\top$.
  - The kernel $K$ that the plan's H1 names is the curvature of the deterministic-intensity
    *value* map. The regret kernel of a mis-specified *policy* may differ from it: an envelope
    argument gives $K$ minus the curvature of a fixed policy's value in $m$. **To be checked in
    Task 6**; H1 is not changed (it is pre-registered).
  - The §6.2 mixture decays like $u^{-0.35}$ over its range, i.e. $b<1$, outside the plan's grid.

### [[acero-2026-hawkes-structured-networks]] — does not close the gap
- **[S] Reward is never reported as a function of p.** Reward exists only at $p=2$ (Table 1,
  p. 6). Fig. 2 (pp. 6–7) sweeps $p\in\{1,2,3,4,6,8\}$ for two quantities only: kernel $L^2$ error
  and intensity MSE. On the power law both plateau over $p\in\{4,6,8\}$.
- **[S] No exact or near-exact reference.** No HJB is solved; every baseline is neural (p. 5).
- **[S] Theorem 1 (p. 3)** is a worst-case upper bound, $\mathrm{Reg}\le C\,(\text{kernel error})^{1/2}$:
  - $C$ «depends on model parameters and $\rho^*$, but is independent of $K_1,K_2$ and $p$»;
  - it requires $\|\hat g\|_{L^1[0,T]}\le\rho^*<1$.
  It is an upper bound in the *kernel* error, not a predictive second-order law in the *forecast*
  error.
- **[S] The lift, eq. (3) (p. 3), is an equal-width rectangle rule** in the decay rate:
  $\hat g=\sum_j\vartheta(I_j)e^{-\beta_jt}$ over a uniform partition of $[K_1,K_2]$, with no values
  given for $K_1,K_2$. It is not a Gauss rule. Tier 0 therefore implements a true Gauss rule as lift
  (i) and Acero's eq. (3) as a labelled supplementary variant.
- **[S] Experimental kernel** $g(t)=n\varepsilon\tau_0^{\varepsilon}(t+\tau_0)^{-(1+\varepsilon)}$
  (p. 5) is exactly the project's shifted power law ($b=1+\varepsilon$, $\rho=n$, $t_0=\tau_0$).
  Fig. 2 uses $\varepsilon=0.15$, $n=0.85$, $t_0/T=0.01$, the plan's hardest corner.
- **[S] The "tie" regime** (exponential controls, p. 5) is the source's own null result. It is
  what the gap's part (3) proposes to map.

### Verdict on the stop rule (Task 2)
Neither core source reports regret or reward versus $p$ on a power-law kernel with an exact or
near-exact reference, and neither gives a second-order regret law. **The stop rule does not
trigger from the core sources.** The search-protocol verdict follows below.

## Re-read of the four lift papers for a value- or regret-versus-p table

One line per source, as the plan requires. All four were re-read on 2026-11-01 against the PDFs on
disk; the pages already recorded most of this (cross-checked).

| Source | What is swept over the number of factors | Reference | Second-order law? | Bearing |
|---|---|---|---|---|
| [[jusselin-2021-persistent-order-flow]] (read: arXiv 2003.05958v2) | **[S]** Figs 1–3 (pp. 11–13): value of the Poisson, 1-exponential and 2-exponential controls when the truth *is* a 2-exponential kernel — «a 10% gain … another 10% gain» (p. 12). Fig. 4 (p. 14): log relative error between $U^{K_n}$ and $U^K$ for a completely monotone, power-law-type kernel $K(t)=\frac{\lambda}{\lambda+(t+\varepsilon)^{\alpha}}(t+\varepsilon)^{-\beta}$, $n$ up to ≈1100, with a fitted regression line (log error falls from ≈ −2 to ≈ −3.2, noisy). | Fig. 4: the true-kernel value $U^K$ via a probabilistic representation (p. 12, App. H); Figs 1–3: the exact 2-exponential HJB. | No | **Narrows (2), does not close it.** Fig. 4 is the closest existing object: a value-versus-$n$ curve on a power-law-type kernel. But it measures the *value of the lifted model* $U^{K_n}$, not the regret of the lifted *policy* run on the true flow. No control-approximation floor is separated out; $n$ runs to ≈1100, not $p\le 8$; and the p-sweep in Figs 1–3 has an exponential truth. |
| [[martin-2026-market-making-hawkes]] | Nothing. **[S]** Thm 2.4 (p. 7): $V_n\to V$ for truncated Mercer expansions, with no rate in value; eigenvalue decay $\xi_n=O(n^{-2})$ for the fractional kernel (p. 8). Numerics use a learned rank-4 factorisation ($n=4$, p. 13). The only performance comparison is naive vs sophisticated on an OU kernel (Fig. 8, p. 16). | None (no exact optimum) | No | Adjacent: convergence without a rate; no p-sweep. |
| [[khabou-2025-markov-approximation-hawkes]] | Nothing. **[S]** $V_0^n\to V_0$ (§4.3, pp. 13–14) through Thm 4.1, with no rate. Fig. 1 (p. 9) shows kernel approximations $\phi^{(2)},\phi^{(3)}$ only. The application is consumption–investment, not market making. | None | No | Adjacent: convergence without a rate. |
| [[jain-2025-impulse-control-hawkes]] (arXiv 2510.26438) | Nothing. **[S]** The model is restricted to single exponentials (p. 7). A finite sum of exponentials «has the same curse of dimensionality», so it switches to RL (p. 11). Tables 2–3 (pp. 18, 20) report OOS Sharpe for an exponential vs a "power-law" kernel, not versus $p$. | None | No | Adjacent: a motivation for RL, no p-sweep. |

## Fixed search protocol, blocks A–D (run 2026-11-01, cut-off 2026-10-29)

Full log, with every query, emulated database, date and hit count:
`input/bibliography/memory-search-log.md`.

- **Protocol deviation, stated plainly:** none of the six named databases (OpenAlex, arXiv, SSRN,
  Crossref, Semantic Scholar, Google Scholar) could be queried directly. The container's network
  policy blocks their APIs, and WebFetch could not open arxiv.org. Each database was emulated with
  domain-restricted WebSearch:
  - the arXiv filter held;
  - the SSRN, Semantic Scholar and Google Scholar filters leaked;
  - OpenAlex and Crossref returned nothing.

  Every classification below rests on search titles, URLs and snippets; no abstract page was
  opened.
- **Queries:** A 21, B 4, C 4, D 9 (at least one per seed). No work cites Barzykin 2026b or
  Acero 2026 yet.

| Hit | Bearing | Verdict |
|---|---|---|
| R1 — Abi Jaber, Bondi, De Carvalho, Neuman, Tuschmann 2025, *Fredholm approach to nonlinear propagator models*, [arXiv 2503.04323](https://arxiv.org/pdf/2503.04323) (authors per a search summary; existence of the arXiv record confirmed 2026-11-01) | Optimal **execution** with a transient-impact propagator, not Hawkes market making. Reports optimal P&L against the number of exponential time scales on a power-law and a shifted power-law kernel, with a general-kernel Fredholm reference (snippet-level). | **Narrows (2)** on the execution side. It is unknown whether the p-exponential *policy* is evaluated on the true kernel (a regret) or whether optimal values are compared across models (as in Jusselin Fig. 4). There is no regret law. **Must be read in full** before any novelty claim. |
| R5 — TechRxiv preprint, Nov 2025, DOI 10.36227/techrxiv.176412729.90497182/v1 (title and authors not resolved) | Execution under self-exciting flow; a robustness section on kernel misspecification. | Adjacent to (1); **not conclusive** (full text unreachable). |
| R2 — Hey et al. 2023 (arXiv 2306.00599); R3 — arXiv 2204.08581; R4 — arXiv 2601.03799; R6 — Chatziandreou–Karbach 2026; R7–R11 (option-flow Hawkes) | Misspecification costs in price-impact or execution problems; option market making | Adjacent; none meets the inclusion criterion for market making under Hawkes flow. |

**Verdict per part of the gap:**
- **(1) Second-order regret law:** OPEN.
- **(2) Regret versus p on a power-law truth with the control floor separated:** NARROWED by R1
  (execution) and by Jusselin 2021 Fig. 4 (model value versus $n$). OPEN for market making under
  Hawkes flow.
- **(3) Map of memory relevance:** OPEN for market making. R1's rule of thumb (2, 3 or 5
  exponentials) and Acero's "tie" are point statements, not a map.

**Stop rule (Task 2): not triggered.** No source reports regret or reward versus $p$ on a power-law
kernel with an exact or near-exact reference *and* a second-order law. The plan proceeds to
Task 3.

## Evidence base

- Full-text re-reads (2026-11-01): Barzykin 2026b and Acero–Plank–Zhang 2026, focus «p-sweep / error
  theory» (focus blocks dated 2026-11-01 on their source pages); Jusselin 2021 (preprint), Martin–Tse
  2026, Khabou–Talbi 2025, Jain et al. 2025 (one line each, above).
- Search protocol blocks A–D, logged in `input/bibliography/memory-search-log.md`.
- Gap statement: design `input/ideas/lai2023-gaps-and-memory-design.md` §Re-evaluation.

## What stays open

- **R1 and R5 must be read in full** before the novelty claim is written (Task 12 related work).
  Both are on the manual worklist. R1 decides how "first" the p-sweep can be called. The likely
  framing is "first for market making under Hawkes flow, with the control floor separated and a
  second-order law" — not "first p-sweep".
- **The search ran on snippets only.** OpenAlex and Crossref were in effect not searched. The
  protocol should be re-run against the real APIs once the network allows it, before submission.
  Until then this verdict is **provisional**.
- **Nine plan sources are still not on disk** (see `input/bibliography/acquisition-todo.md`,
  "Priority 3b"):
  - Alfonsi–Kebaier 2024, which fixes what "Gauss-type quadrature" means in plan lift (i);
  - the Lai 2021 thesis (Lai's time unit);
  - the near-criticality papers by Hardiman, Filimonov–Sornette and Lallouache–Challet.
- **The regret kernel in H1 (Task 6):** whether the plan's $K$ (curvature of the value map) or
  "$K$ minus the curvature of the fixed-policy value" is the right second-order object. This is
  recorded as a question to check, not a change to H1.
- **Barzykin's common-mode convention** ($\lambda^s=\mu^s+x$ vs $\mu^s+x/2$) must be settled in
  Task 4, before his Table 3 can be reproduced.
