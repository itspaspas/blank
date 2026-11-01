---
title: "Where and why does closed-form market making (GLFT 2013 → BEGV 2021) fail to extend to multivariate Hawkes order flow with cross-asset excitation — and is the gap real?"
type: design
created: 2026-10-25
updated: 2026-10-25
tags: [market-making, hawkes-processes, stochastic-control, multi-asset, literature-synthesis]
status: approved
author: mixed
methodology: hermeneutic   # this phase only; the project is `mixed` — quantitative sub-studies (H1–H4 of the proposal) get their own pre-registered plans later
---

# Phase 1 — Problem anatomy: multi-asset market making under Hawkes order flow

Framing document: `proposal/proposal.pdf` (October 2026), "Market Making under
Cross-Asset Hawkes Order Flow: Closed-Form Approximations, Exact Solutions and
Reinforcement Learning in One Study". This design covers **only the first phase**:
understanding the problem and verifying the gap before any derivation, code or data work.

## Research Question

**Where exactly, and why, does the closed-form theory of market making — the
single-asset linear-ODE solution of Guéant, Lehalle & Fernandez-Tapia (2013) and the
multi-asset quadratic/matrix-Riccati approximation of Bergault, Evangelista, Guéant &
Vieira (2021) — fail to extend to multivariate Hawkes order flow with cross-asset
excitation, and does the literature confirm that no one has closed this gap?**

Falsifiable in two ways: (a) the gap search may find a paper (journal, preprint, thesis,
or adjacent field) that already gives such a closed form; (b) the analysis may show the
obstruction is technical rather than structural (e.g. a frozen-forecast Riccati system
closes trivially and the open problem is only its accuracy).

### Sub-questions

- **Q1 — Why the Poisson case closes.** What exactly makes BEGV's quadratic ansatz
  `θ ≈ −qᵀA q − qᵀB − C` close under Poisson flow? (Hamiltonian quadratic expansion
  `H(p) ≈ h₀ + h₁p + ½h₂p²` → matrix Riccati `A' = 2AΓA − (γ/2)Σ`.)
- **Q2 — What Hawkes adds to the state.** With exponential kernels the intensities λ
  become Markov state; what does the lifted HJB look like (transport term
  `−Σβ_j(λ_j−μ_j)∂_{λ_j}θ`, jump term at post-order intensities `λ + DKe_j`), how does
  the state dimension scale with d assets and with sums-of-exponentials kernels, and
  why does Barzykin (2026b) say the lift + quadratic ansatz yields transport-jump
  equations rather than a small Riccati system?
- **Q3 — When the ansatz fails, and what the workarounds cost.** Bergault, Bertucci,
  Bouba, Guéant & Guilbert (2024): inventory and intensity jump together and the ansatz
  does not close. Under which modelling convention (all orders excite vs. only the
  maker's fills excite) does "freeze the intensity forecast" remain valid, and what
  error sources does it introduce (forecast freezing vs. Hamiltonian expansion)?
- **Q4 — What has actually been solved.** For every Hawkes market-making paper:
  number of assets, kernel type, self/cross/side excitation, objective (utility vs.
  risk-adjusted), solution method (closed form / grid / neural PDE / RL), and the
  benchmark it is checked against. → comparison matrix.
- **Q5 — How large is cross-asset excitation empirically,** and how sensitive are
  estimates of the cross-asset block of the branching matrix K to tie handling,
  binning and common-shock components?
- **Q6 — Is the gap real?** Has anyone, since or outside the proposal's 75-paper
  search, extended the multi-asset closed form to Hawkes (or other self-exciting /
  state-dependent intensity) flow — including adjacent problems (optimal execution,
  RFQ/OTC dealing, insurance/credit with mutually exciting jumps)?

## Relevance / State of the Field (brief)

The closed-form branch of market-making theory (Avellaneda–Stoikov 2008 → GLFT 2013 →
Guéant 2017 → BEGV 2021) rests on Poisson arrivals, while order flow is empirically
clustered (Bacry, Mastromatteo & Muzy 2015). The proposal's search found 21 Hawkes
market-making papers: two keep a closed form (Cartea, Jaimungal & Ricci 2014; Barzykin
2026b), both single-asset; multi-asset Hawkes studies (Lai, Gao & Li 2023; Kumar 2024;
Acero, Plank & Zhang 2026) use learned policies only. This phase turns that claim into
a source-anchored, independently re-checked map.

## Method

Systematic hermeneutic synthesis in three strands:

1. **Uniform full ingest** of every PDF in `./library` (~70) via `ingest-source`,
   with structured extraction (section map, Kernthesen, model/solution-method fields
   needed for the Q4 matrix). Duplicates resolved at bibkey assignment.
   Ingest depth `deep` for the works the question rests on (GLFT 2013, BEGV 2021,
   Cartea–Jaimungal–Ricci 2014, Barzykin 2026b, Bergault et al. 2024, Martin & Tse
   2026, Jusselin 2021, Acero–Plank–Zhang 2026); `standard` for the rest.
2. **Supplementary literature search** (`literature-review` → `acquire-sources`):
   forward/backward citation chasing from the core papers plus OpenAlex / arXiv /
   Crossref queries targeted at Q6, including adjacent fields. Newly found sources
   are acquired and ingested the same way.
3. **Critical synthesis** (`critical-thinking`): reconstruct the Q1–Q3 argument chain
   from the sources' own equations; treat contested claims explicitly — e.g. the
   proposal's non-reproduction of Barzykin's 0.17 % state-feedback regret, the weak
   Poisson comparator, the Acero et al. constant-quote baseline concern.

Why not a question-driven partial read: risk of confirming the proposal's own framing.
Why not derivation now: Phase 1's job is to locate the obstruction precisely; deriving
around it belongs to the pre-registered quantitative sub-studies.

## Data Sources / Material Basis

- `./library/` — ~70 PDFs (arXiv preprints and published versions), designated as the
  project's research library (`.research-library` → `./library`; bibkey-named copies
  in `library/pdf/`, originals untouched).
- `proposal/proposal.pdf` — framing document and claims to verify.
- OpenAlex, arXiv, Crossref, Semantic Scholar for the supplementary search.

## Wiki structure (target)

- `knowledge/sources/` — one page per paper.
- `knowledge/entities/` — models as named objects (GLFT 2013, BEGV 2021,
  Avellaneda–Stoikov, Cartea–Jaimungal–Ricci, Barzykin Volterra–Riccati), datasets
  (Binance, Tardis, Databento, LOBSTER, TRACE).
- `knowledge/concepts/` — Hawkes process, branching matrix & spectral radius, Markov
  lift, Volterra–Riccati, Hamiltonian quadratic approximation, shadow price, matrix
  Riccati equation, intensity forecast, semi-Lagrangian scheme, deep Galerkin,
  model-based actor-critic, PPO, generalised policy iteration, regret.
- `knowledge/synthesis/`
  - `problem-anatomy` — the core page; answers Q1–Q3 as one argument chain.
  - `hawkes-mm-comparison-matrix` — Q4.
  - `cross-asset-excitation-evidence` — Q5.
  - `gap-verification` — Q6, with search log and disconfirming candidates.
  - `open-questions` — what Phase 2 must decide.

## Output Target

☐ Book chapter  ☐ Journal article  ☐ Grant proposal  ☐ Talk
☑ Other: internal knowledge base + `problem-anatomy` synthesis; later feeds §3
(Literature Review) of the proposal and the related-work section of the eventual paper.

## Expected Results

- **Positive:** a precise statement of the obstruction (which term of the lifted HJB
  breaks the quadratic closure, under which convention), a complete comparison matrix,
  and a gap confirmed against an extended search — giving Stage 2 of the proposal a
  sharply defined target.
- **Null / disconfirming:** a prior multi-asset Hawkes closed form is found, or the
  obstruction turns out trivial → the proposal's contribution claim is revised toward
  the accuracy/benchmark comparison, which is then the real gap.

## Ethical / Methodological Risks

- **Version drift:** many 2025–26 sources are arXiv preprints; each source page records
  the version read. No silent preprint↔published substitution (ingest hard-stop).
- **Duplicates / misattribution** among loosely named PDFs — resolved via verified
  metadata before bibkeys are assigned.
- **Framing bias:** the proposal was written by the same researcher; the gap search
  actively seeks disconfirming work.
- **Secondary-hand claims:** the proposal reads some works only at abstract level
  (Tarditi 2026; Bielecki, Mastrolia & Yan 2026) — flagged until read in full.
- **Copyright:** PDFs and figures stay internal; not redistributed.

## Feasibility

Single researcher with LLM support. ~70 ingests run as batched subagent dispatches
with `wiki-lint` between batches; supplementary search adds an estimated 10–30
sources. No data purchase, compute or collaborators needed in this phase.

## Scope Boundaries (what is NOT investigated)

**Not investigated in this phase:** new derivations, numerical solutions, RL training,
data fitting, or any test of hypotheses H1–H4. Queue-position models, power-law
kernels beyond sums of exponentials, and the self-fill-excitation case are recorded
where sources discuss them but not pursued.

## Next Step

Hand off to `writing-research-plan` to produce `input/ideas/hawkes-multi-asset-mm-plan.md`.
