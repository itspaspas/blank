---
title: "Phase 1 — Problem anatomy: multi-asset market making under Hawkes order flow"
type: plan
created: 2026-10-25
updated: 2026-10-25
status: ready
author: mixed
design: "[[hawkes-multi-asset-mm-design]]"
methodology: hermeneutic   # sub-study of a `mixed` project; no task in this plan is pre-registered
---

# Phase 1 — Problem anatomy — Research Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `research-superpowers:executing-research-plan` to run this plan task by task.

**Research Question:** Where exactly, and why, does the closed-form theory of market
making (GLFT 2013 → BEGV 2021) fail to extend to multivariate Hawkes order flow with
cross-asset excitation, and does the literature confirm that no one has closed this gap?
(Sub-questions Q1–Q6 as in the design.)

**Method sketch:** Uniform full ingest of the existing library (~72 PDFs), a
supplementary literature search aimed at Q6 (including disconfirming and
adjacent-field work), then critical synthesis that reconstructs the Q1–Q3 argument
chain from the sources' own equations and builds the Q4 comparison matrix.

**Expected source corpus:**
- **Closed-form market making:** Ho–Stoll 1981, Avellaneda–Stoikov 2008, GLFT 2013,
  Guéant 2017, Cartea–Jaimungal–Penalva 2015, BEGV 2021, Bergault–Guéant 2023,
  Barzykin–Bergault–Guéant 2023.
- **Hawkes market making:** Cartea–Jaimungal–Ricci 2014, Barzykin 2026a/b/c,
  Bergault–Bertucci–Bouba–Guéant–Guilbert 2024, Jusselin 2021, Martin–Tse 2026,
  Choi–Jang–Lee–Zheng 2021, Jain et al. 2025, Acero–Plank–Zhang 2026, Gašperov–Kostanjčar
  2022, Lai–Gao–Li 2023, Kumar 2024, Yang–Xu 2026.
- **Hawkes theory and Markov lift:** Hawkes 1971, Bacry–Mastromatteo–Muzy 2015,
  Bacry–Jaisson–Muzy 2016, Khabou–Talbi 2025, Bielecki–Mastrolia–Yan 2026.
- **Learning and numerical methods:** Guéant–Manziuk 2019, Cheridito–Dupret–Hainaut 2025,
  Boyce–Herdegen–Sánchez-Betancourt 2025.
- **Plus** whatever the Q6 search adds.

**Iteration expectation:** Ingest and synthesis alternate. The `problem-anatomy` page is
started after the core batch (Task 4) and revised after every later batch. A new source
that changes the Q1–Q3 chain is logged in `knowledge/_meta/log.md`. If Q6 turns up a
prior multi-asset Hawkes closed form, the design's contribution claim is revised
(back-edge to `brainstorming-research`).

**Output target:** other — internal knowledge base + synthesis pages (they later feed §3 of the proposal)
**Language:** en

---

## Data Sources

- **Library:** `./library/` (~72 PDFs on disk; exact count fixed in Task 1), designated via `.research-library`.
  Status: *on disk, unidentified*. About 50 are named only `arXiv_<id>.pdf`; at least
  two duplicate pairs are suspected:
  - `Dealing with the Inventory Risk.pdf` ↔ `arXiv_1105.3115.pdf`
  - `Closed-form approximations in multi-asset market making__.pdf` ↔ `arXiv_2106.06974.pdf`
- **Proposal reference list:** `proposal/proposal.pdf` §8 (pp. 29 ff.). Each reference
  is either *on disk* (matched in Task 2) or *acquire pending* (Task 3).
- **Supplementary search:** OpenAlex, arXiv, Crossref, Semantic Scholar (Task 6).

## Tasks

### Task 0: Finish the project scaffold
**Files:** `CLAUDE.md`, `scripts/*`, `schema/*`, `knowledge/_meta/*`, `output/bibtex/*`, `.gitignore`

- [ ] Copy the `research-project-template` into the project root without overwriting
  (`cp -rn <template>/. .`). The existing `library/`, `proposal/` and `input/` files stay untouched.
- [ ] Patch the `CLAUDE.md` frontmatter: `methodology: mixed`, `discipline: "Quantitative Finance / Market Microstructure"`, `languages: [en]`, `plugin_version: "0.41.1"`
- [ ] Fill the **Ingest depth** block in `CLAUDE.md`: `deep` for the 8 core works named in the design, `standard` otherwise
- [ ] Add project conventions to `CLAUDE.md`: notation follows the proposal's "List of Main Symbols", equations keep their source numbering, and the coordinates section is deleted
- [ ] Delete the 4 `_example-*` pages (Megiddo domain) and the example asset
- [ ] Run `python scripts/library.py` and confirm it resolves to `./library`
- [ ] Register the project in `~/.config/research-superpowers/projects`

### Task 1: Identify every PDF in the library
**Files:** `input/bibliography/library-inventory.md`

- [ ] For each PDF, resolve the metadata: arXiv API for `arXiv_<id>.pdf`, Crossref/OpenAlex by title for the others. Record authors, year, title, venue, DOI, arXiv ID and version.
- [ ] Mark each one: preprint vs. published version, and whether a published version exists elsewhere
- [ ] Flag duplicates (same work, two files). Keep one canonical file per work and note which version it is.
- [ ] Assign the canonical bibkey `author-year-shorttitle` per the CLAUDE.md rule
- [ ] Assign an ingest batch to each unique work. Batch B1 holds the 8 core works; B2–B7 hold ≤ 10 works each, grouped by theme (closed-form MM / Hawkes MM exact & neural / Hawkes MM RL / Hawkes theory & lift / execution & other / empirical)
- [ ] Mark works that are off-topic (not market making, Hawkes, or control). They get `map` depth, not `standard`.

### Task 2: Build the bibkey library
**Files:** `library/pdf/<bibkey>.pdf`, `library/references.bib`

- [ ] Copy each canonical PDF to `library/pdf/<bibkey>.pdf`. The originals in `library/` stay unchanged.
- [ ] Write verified BibTeX entries to `library/references.bib`
- [ ] Run `python scripts/bib-search.py index` and record scans with no text layer in the inventory
- [ ] Match the proposal's §8 reference list against the inventory and list unmatched references in `input/bibliography/library-inventory.md` § "Missing from library"

### Task 3: Acquire missing proposal references
**Files:** `library/pdf/*.pdf`, `input/bibliography/acquisition-todo.md`

- [ ] Run `acquire-sources` on § "Missing from library" (open-access copies are downloaded automatically)
- [ ] The user fetches paywalled originals manually into `library/pdf/<bibkey>.pdf`
- [ ] Re-run `acquire-sources` to reconcile. Every remaining gap is explicitly deferred, with its reason recorded in `acquisition-todo.md`.

### Task 4: Ingest batch B1 — core works (deep)
**Files:** `knowledge/sources/*.md`, `knowledge/concepts/*.md`, `knowledge/entities/*.md`, `output/bibtex/references.bib`, `knowledge/_meta/{index,log}.md`

- [ ] Ingest the 8 B1 works via `ingest-source` at depth `deep`. The ingest focus follows `input/description/project-description.md` § "Guidance for ingest". Each source page gets a structured **Model card**: assets, kernel, excitation structure, who excites the flow, objective, solution method, benchmark, reported regrets, key equation numbers.
- [ ] Create concept pages as they arise: `hawkes-process`, `branching-matrix`, `markov-lift`, `hamiltonian-quadratic-approximation`, `matrix-riccati-equation`, `volterra-riccati`, `intensity-forecast`, `shadow-price`, `regret`
- [ ] Create entity pages for the models: `glft-2013-model`, `begv-2021-model`, `avellaneda-stoikov-model`, `cartea-jaimungal-ricci-model`, `barzykin-volterra-riccati`
- [ ] Run `wiki-lint` and fix the findings

### Task 5: Start the problem-anatomy synthesis (first pass)
**Files:** `knowledge/synthesis/problem-anatomy.md`

- [ ] Q1: rebuild the closure argument of BEGV 2021 (quadratic Hamiltonian → Riccati) from the source page's equations, citing equation numbers
- [ ] Q2: write out the lifted HJB with Hawkes intensities, show the transport and jump terms, and tabulate how the state dimension scales with d and the number of exponentials
- [ ] Q3: state why the ansatz fails when fills excite (Bergault et al. 2024), and what freezing the forecast does (Barzykin 2026b); separate the two error sources
- [ ] Add the `## Evidence base` and `## What stays open` sections. Set `status: draft`.

### Task 6: Supplementary literature search (Q6)
**Files:** `input/bibliography/literaturguide.md`, `input/bibliography/audit-log-*.json`, `output/bibtex/references.bib`

- [ ] Run `literature-review`. Chase forward citations of GLFT 2013, BEGV 2021, CJR 2014, Barzykin 2026b and Bergault et al. 2024, and backward citations of the 2025–26 Hawkes MM papers.
- [ ] Run keyword queries: "multi-asset market making Hawkes", "mutually exciting order flow market making", "Riccati Hawkes optimal control", "multivariate Hawkes optimal execution closed form", "self-exciting intensity stochastic control quadratic approximation"
- [ ] Search adjacent fields: optimal execution with Hawkes flow, RFQ/OTC dealing, insurance and credit with mutually exciting jumps, theses (ProQuest, HAL, arXiv)
- [ ] Grade the candidates A/B/C. Every A-graded candidate that could disconfirm the gap gets an explicit note.

### Task 7: Acquire the new sources
**Files:** `library/pdf/*.pdf`, `input/bibliography/acquisition-todo.md`

- [ ] Run `acquire-sources` on the A+B set from `literaturguide.md`
- [ ] Manual fetches, then re-run `acquire-sources` to reconcile

### Task 8: Ingest batches B2–B7 plus the new sources
**Files:** as in Task 4

- [ ] Ingest B2 (`standard`), then run `wiki-lint`
- [ ] Ingest B3 (`standard`), then run `wiki-lint`
- [ ] Ingest B4 (`standard`), then run `wiki-lint`
- [ ] Ingest B5 (`standard`), then run `wiki-lint`
- [ ] Ingest B6 (`standard`), then run `wiki-lint`
- [ ] Ingest B7 (`standard`; off-topic works at `map`), then run `wiki-lint`
- [ ] Ingest the A+B sources from Task 7 in batches of ≤ 10, running `wiki-lint` after each
- [ ] Add method and dataset pages as they arise: `semi-lagrangian-scheme`, `deep-galerkin-method`, `model-based-actor-critic`, `ppo`, `generalised-policy-iteration`; datasets `binance-futures-archive`, `tardis-dev`, `databento-cme`, `lobster`, `trace`
- [ ] After each batch, revise `problem-anatomy` if a source changes Q1–Q3, and log the change in `log.md`

### Task 9: Comparison matrix (Q4)
**Files:** `knowledge/synthesis/hawkes-mm-comparison-matrix.md`

- [ ] Build one table row per Hawkes MM paper from the source pages' Model cards. Columns: assets, kernel, self / cross-side / cross-asset excitation, exciter (all orders vs. maker's fills), objective, solution method, benchmark, best reported regret.
- [ ] Re-count the proposal's §3.3 tallies (21 Hawkes papers: 2 closed form, 5 lifted numerical, 12 learned, 2 lift theory) and record agreements and differences

### Task 10: Cross-asset excitation evidence (Q5)
**Files:** `knowledge/synthesis/cross-asset-excitation-evidence.md`

- [ ] Collect every reported estimate of cross-asset or cross-side excitation (branching ratios, cross-block size, decay rates), with market, period and estimation method
- [ ] Record what each source says about ties, binning and common shocks, and how sensitive its estimates are to them

### Task 11: Gap verification (Q6)
**Files:** `knowledge/synthesis/gap-verification.md`

- [ ] For each candidate that could disconfirm the gap: what it solves, why it does or does not close the gap (cited)
- [ ] State a verdict on the proposal's two gap claims (no multi-asset Hawkes closed form; no three-way comparison): **confirmed / refuted / qualified**, with the search scope stated

### Task 12: Finish the problem anatomy and open questions
**Files:** `knowledge/synthesis/problem-anatomy.md`, `knowledge/synthesis/open-questions.md`

- [ ] Final pass on `problem-anatomy`: state the obstruction precisely (which term, which convention, which dimension) and the candidate routes around it, each with the sources that support it
- [ ] Write `open-questions`: the decisions Stage 2 of the proposal must make, and the proposal claims that Phase 1 revised
- [ ] Run a `critical-thinking` pass on the contested claims (Barzykin's 0.17 %, the Poisson comparator, the Acero et al. baselines) and record the outcome in the relevant source pages' `Contested` sections

### Task 13: Quality pass
**Files:** `knowledge/_meta/*`, `knowledge/_meta/graph/*`

- [ ] Run `wiki-lint`; it must exit 0
- [ ] Run `semantic-wiki-review` over the synthesis pages and fix contradictions and stale claims
- [ ] Run `wiki-graph`. Check that the `problem-anatomy` neighbourhood reaches every core source, and list orphaned clusters.
- [ ] The user reviews the 5 synthesis pages. Approved pages get `status: stable`.

## Verification

Phase 1 is complete when:
- [ ] `input/bibliography/library-inventory.md` lists every PDF in `./library` with a verified bibkey, and every duplicate is resolved
- [ ] Every unique on-topic work in the library, plus every A+B source from Task 6 that was acquired, has a source page. Each deferred source is listed with its reason in `acquisition-todo.md`.
- [ ] Every Hawkes MM source page has a complete Model card (no empty fields; "n/a" allowed with a reason)
- [ ] `python scripts/lint-wiki.py` exits 0
- [ ] The 5 synthesis pages (`problem-anatomy`, `hawkes-mm-comparison-matrix`, `cross-asset-excitation-evidence`, `gap-verification`, `open-questions`) exist with `status: stable`
- [ ] `gap-verification` gives an explicit verdict on both gap claims
- [ ] Q1–Q6 are each answered on a synthesis page, or explicitly marked "open" with a reason

## Deviations Log

Append to `knowledge/_meta/log.md` whenever the scope, method or sources change. Reference the slug `hawkes-multi-asset-mm`.
