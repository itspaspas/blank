# Stage 2a — fixed prior-art search protocol (F-novelty)

Plan: `input/ideas/hawkes-perturbative-closed-form-plan.md`, Task 1. Fixed on 2026-10-26, before
any derivation. **Cut-off: 2026-11-30.** Runs after the cut-off are logged as exploratory.

## Question
Has anyone published a perturbative / asymptotic closed form (finite matrix-ODE system) for
**multi-asset (d > 1)** market making or dealing under **self-/mutually exciting (Hawkes) or
state-dependent stochastic order-arrival intensities**?

## Databases
OpenAlex · arXiv (q-fin.TR, q-fin.MF, math.OC, math.PR) · Crossref · Semantic Scholar.
Plus the local library: `python scripts/bib-search.py` with one alias per `--q`.

## Fixed queries (verbatim, all databases)
1. "multi-asset market making" Hawkes
2. "market making" "mutually exciting" closed form
3. "market making" Hawkes perturbation OR asymptotic OR expansion Riccati
4. "stochastic intensity" "market making" "matrix Riccati"
5. "optimal market making" "stochastic liquidity" multi-asset approximation
6. "self-exciting" "optimal quotes" multi-asset OR multivariate

## Forward citations (all citing works up to the cut-off)
- Fujii 2015 (`fujii-2015-optimal-position-management`)
- BEGV 2021 (`bergault-2021-closed-form-approximations`)
- Barzykin 2026b (`barzykin-2026-hawkes-driven-otc`)

## Grading and verdict
A = could pre-empt one of the four novelty items (design § Relevance): (i) Hawkes jump factor
with error order; (ii) intensities through Hamiltonian curvature $h_2$; (iii) explicit matrix
order-1 system, d > 1; (iv) accuracy map against exact solutions. B = adjacent (single-asset,
or no expansion). C = off-topic. Every A gets an explicit verdict per item; A candidates are
acquired and ingested.

## Runs
| Date | Run | New A | New B | Verdict |
|---|---|---|---|---|
| 2026-10-26 | 1 (provisional) | 0 | 7 | No new work pre-empts (i)–(iv). Known A re-confirmed: Barzykin 2026b (d=1 only, conceded), Acero et al. 2026 (RL, no closed form). Gaps: Semantic Scholar keyword search HTTP 429 on all queries (citation endpoint worked); Park & Malinova 2026 (SSRN 10.2139/ssrn.7432398, multi-asset FX AMM) abstract unreadable — check manually. Re-run S2 keyword queries before cut-off. |

### Run 1 — B list (new)
1. Park & Malinova 2026, "Dethroning the Dollar? Optimal Multi-Asset Market Making", SSRN 10.2139/ssrn.7432398 — **open: check for stochastic intensity**.
2. Yu 2026, "Explicit Signal-Adaptive Sequential Optimal Execution Quotes", arXiv 2605.24242 — triangular finite-dim structure, single asset, execution.
3. Roldan-Contreras & Swishchuk 2022, Risks 10(8):160, 10.3390/risks10080160 — single-asset MM, compound Hawkes, no expansion.
4. Tiwari 2025, SSRN 10.2139/ssrn.5775204 — multivariate Hawkes LQ execution, no quotes.
5. Baldacci, Derchu & Manziuk 2020, arXiv 2009.00907 — high-dim options MM approximation, constant intensities.
6. Fujii & Takahashi 2015, "Asymptotic Expansion for FBSDEs with Jumps", 10.2139/ssrn.2672890 — method precedent (jump expansion).
7. Boyce & Neuman 2026, arXiv 2606.06413 — closed-form dealer equilibrium, single asset, no Hawkes.
Forward citations: Fujii 2015 → 3; BEGV 2021 → ~48 unique; Barzykin 2026b → 0. C: ~72. Scout scratch: session scratchpad s2a/.
