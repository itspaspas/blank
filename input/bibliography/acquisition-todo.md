# Source acquisition — manual downloads needed

These sources could not be downloaded automatically (paywalled, bot-blocked, damaged, or no
open-access copy). Download each **original** PDF through your university VPN or library proxy (or
an ordinary browser for SSRN) and save it **into `library/pdf/`** under the **exact** "Save as"
filename below. Then re-run acquire-sources to reconcile.

Last updated: 2026-11-01 (run 3, plan `lai2023-gaps-and-memory` Task 2) · 25 items open (14 from
run 2 + 9 memory-plan keys + 2 novelty follow-ups). None blocks Tier 0 (Task 3): it needs only the
kernel and Lai Table 2, both on disk. Jusselin is ingested from the preprint with consent.

**Run 3: nothing could be auto-downloaded.** This cloud container's network policy blocks the
scholarly hosts (`arxiv.org`, `export.arxiv.org`, `api.openalex.org`, `api.crossref.org`,
`api.unpaywall.org`, `projecteuclid.org`: the proxy refuses the CONNECT). The arXiv copies below
are open access and, under the project's **preprint policy** (CLAUDE.md), acceptable originals for
these non-core works. Either allow `arxiv.org` (plus `projecteuclid.org`) in the environment's
network settings and re-run acquire-sources, or download them in a browser and commit them to
`library/pdf/` under the exact filename.

Resolved in run 2:
- User-added files renamed to their bibkeys: Avellaneda–Stoikov 2008, Ho–Stoll 1981, Hawkes 1971,
  Lai–Gao–Li 2023, Tarditi 2026, Cartea–Jaimungal–Ricci 2018, Bathini 2026, Yuan–Du–Hu 2026
  (author preprint).
- 15 open-access copies downloaded: Fujii, Shen, Aït-Sahalia, Zarezade, Alfonsi ×2, Fu, Ceci,
  Abi Jaber ×3, Zhang, Gennaro, Zimmer, Chen.

## Priority 1: damaged file

| ☐ | Citekey | Author Year | Short title | Grade | DOI / landing | Note | Save as (exact filename) |
|---|---------|-------------|-------------|-------|---------------|------|--------------------------|
| [ ] | cartea-2015-algorithmic-high-frequency | Cartea, Jaimungal & Penalva 2015 | Algorithmic and High-Frequency Trading (book) | A | ISBN 9781107091146 | The copy you added is **damaged** (invalid XRef and /Pages object; no page renders). Moved to `library/damaged/`. Please download it again. | `cartea-2015-algorithmic-high-frequency.pdf` |

## Priority 2: core original

| ☐ | Citekey | Author Year | Short title | Grade | DOI / landing | Note | Save as (exact filename) |
|---|---------|-------------|-------------|-------|---------------|------|--------------------------|
| [ ] | jusselin-2021-persistent-order-flow | Jusselin 2021 | Optimal market making with persistent order flow | A | [10.1137/20M1376054](https://doi.org/10.1137/20M1376054) | SIAM blocked both of us. `library/pdf/` holds arXiv v2; **overwrite it** with the original when obtained, then re-ingest. | `jusselin-2021-persistent-order-flow.pdf` |

## Priority 3: literature-search A+B items without an open-access copy

| ☐ | Citekey | Author Year | Grade | DOI / landing | Note | Save as (exact filename) |
|---|---------|-------------|-------|---------------|------|--------------------------|
| [ ] | sharma-2026-structural-hawkes-ambiguity | Sharma 2026 | B | [10.2139/ssrn.6777719](https://doi.org/10.2139/ssrn.6777719) | SSRN, browser download | `sharma-2026-structural-hawkes-ambiguity.pdf` |
| [ ] | lim-2026-liquidation-aware-market | Lim 2026 | B | [10.2139/ssrn.6847019](https://doi.org/10.2139/ssrn.6847019) | SSRN | `lim-2026-liquidation-aware-market.pdf` |
| [ ] | lucic-2024-optimal-option-market | Lucic 2024 | B | [10.2139/ssrn.4729290](https://doi.org/10.2139/ssrn.4729290) | SSRN | `lucic-2024-optimal-option-market.pdf` |
| [ ] | errais-2010-affine-point-processes | Errais, Giesecke & Goldberg 2010 | B | [10.1137/090771272](https://doi.org/10.1137/090771272) | SIAM; SSRN 908045 | `errais-2010-affine-point-processes.pdf` |
| [ ] | duffie-2000-transform-analysis-asset | Duffie, Pan & Singleton 2000 | B | [10.1111/1468-0262.00164](https://doi.org/10.1111/1468-0262.00164) | Econometrica / JSTOR | `duffie-2000-transform-analysis-asset.pdf` |
| [ ] | bo-2019-credit-portfolio-selection | Bo & Capponi 2019 | B | [10.1111/mafi.12177](https://doi.org/10.1111/mafi.12177) | Wiley | `bo-2019-credit-portfolio-selection.pdf` |
| [ ] | bo-2016-optimal-investment-credit | Bo & Capponi 2016 | B | [10.1111/mafi.12074](https://doi.org/10.1111/mafi.12074) | Wiley; SSRN 2342645 | `bo-2016-optimal-investment-credit.pdf` |
| [ ] | chehrazi-2019-dynamic-credit-collections | Chehrazi et al. 2019 | B | [10.1287/mnsc.2018.3070](https://doi.org/10.1287/mnsc.2018.3070) | INFORMS | `chehrazi-2019-dynamic-credit-collections.pdf` |
| [ ] | branger-2014-partial-information-contagion | Branger et al. 2014 | B | [10.1016/j.jedc.2013.10.005](https://doi.org/10.1016/j.jedc.2013.10.005) | Elsevier; econstor 10419/88730 | `branger-2014-partial-information-contagion.pdf` |
| [ ] | bensoussan-2024-stochastic-control-diffusions | Bensoussan et al. 2024 | B | [10.3934/mcrf.2024038](https://doi.org/10.3934/mcrf.2024038) | AIMS | `bensoussan-2024-stochastic-control-diffusions.pdf` |
| [ ] | li-2002-indefinite-stochastic-lq | Li & Zhou 2002 | B | [10.4310/CIS.2002.v2.n3.a4](https://doi.org/10.4310/CIS.2002.v2.n3.a4) | International Press | `li-2002-indefinite-stochastic-lq.pdf` |

## Priority 3b: memory-regret plan (`lai2023-gaps-and-memory`, Data Sources), run 3, 2026-11-01

Metadata resolved by search (WebSearch only; see `input/bibliography/memory-acquisition-metadata.json`
for confidence and provenance). Grade B = needed for Tasks 4–8 and for the related-work section, not
for Tier 0.

| ☐ | Citekey | Author Year | Grade | DOI / landing | Best download URL(s) | Note | Save as (exact filename) |
|---|---------|-------------|-------|---------------|----------------------|------|--------------------------|
| [ ] | lai-2021-data-driven-approach | Lai 2021 | B | — | — | CUHK PhD thesis; no repository record found. Needed for Lai's time unit and same-timestamp aggregation. Proposed key `lai-2021-data-driven-approach-option` renamed (4-word short title). | `lai-2021-data-driven-approach.pdf` |
| [ ] | alfonsi-2024-approximation-stochastic-volterra | Alfonsi & Kebaier 2024 | B | [10.1090/mcom/3911](https://doi.org/10.1090/mcom/3911) | [arXiv 2102.13505](https://arxiv.org/pdf/2102.13505) (preprint, accepted per policy) |  | `alfonsi-2024-approximation-stochastic-volterra.pdf` |
| [ ] | bayer-2023-markovian-approximations-stochastic | Bayer & Breneis 2023 | B | [landing](https://ideas.repec.org/a/taf/quantf/v23y2023i1p53-70.html) | [arXiv 2108.05048](https://arxiv.org/pdf/2108.05048) (preprint, accepted per policy) |  | `bayer-2023-markovian-approximations-stochastic.pdf` |
| [ ] | abijaber-2019-multifactor-approximation-rough | Jaber & Euch 2019 | B | [10.1137/18M1170236](https://doi.org/10.1137/18M1170236) | [arXiv 1801.10359](https://arxiv.org/pdf/1801.10359) (preprint, accepted per policy) |  | `abijaber-2019-multifactor-approximation-rough.pdf` |
| [ ] | hardiman-2013-critical-reflexivity | Hardiman et al. 2013 | B | [10.1140/epjb/e2013-40107-3](https://doi.org/10.1140/epjb/e2013-40107-3) | [arXiv 1302.1405](https://arxiv.org/pdf/1302.1405) (preprint, accepted per policy) |  | `hardiman-2013-critical-reflexivity.pdf` |
| [ ] | filimonov-2015-apparent-criticality | Filimonov & Sornette 2015 | B | [10.1080/14697688.2015.1032544](https://doi.org/10.1080/14697688.2015.1032544) | [arXiv 1308.6756](https://arxiv.org/pdf/1308.6756) (preprint, accepted per policy) |  | `filimonov-2015-apparent-criticality.pdf` |
| [ ] | lallouache-2016-limits-statistical-significance | Lallouache & Challet 2016 | B | [10.1080/14697688.2015.1068442](https://doi.org/10.1080/14697688.2015.1068442) | [arXiv 1406.3967](https://arxiv.org/pdf/1406.3967) (preprint, accepted per policy) |  | `lallouache-2016-limits-statistical-significance.pdf` |
| [ ] | hillairet-2024-chaotic-expansion-counting | Hillairet & Réveillac 2024 | B | [10.1214/24-EJP1193](https://doi.org/10.1214/24-EJP1193) | [arXiv 2209.01972](https://arxiv.org/pdf/2209.01972) (preprint, accepted per policy); [OA journal](https://projecteuclid.org/journals/electronic-journal-of-probability/volume-29/issue-none/On-the-chaotic-expansion-for-counting-processes/10.1214/24-EJP1193.full) | Authors: Hillairet & Réveillac (not Rosenbaum). EJP is open access. | `hillairet-2024-chaotic-expansion-counting.pdf` |
| [ ] | leblanc-2024-exponential-moments-hawkes | Leblanc 2024 | B | [10.1214/24-ECP625](https://doi.org/10.1214/24-ECP625) | [arXiv 2505.15253](https://arxiv.org/pdf/2505.15253) (preprint, accepted per policy); [OA journal](https://projecteuclid.org/journals/electronic-communications-in-probability/volume-29/issue-none/Exponential-moments-for-Hawkes-processes-under-minimal-assumptions/10.1214/24-ECP625.full) | ECP is open access; arXiv posting (2025) postdates the journal version. | `leblanc-2024-exponential-moments-hawkes.pdf` |

### Novelty-check follow-ups (search hits from `memory-search-log.md`; must be read in full before the novelty claim is written)

| ☐ | Citekey | Author Year | Grade | DOI / landing | Best download URL(s) | Note | Save as (exact filename) |
|---|---------|-------------|-------|---------------|----------------------|------|--------------------------|
| [ ] | abijaber-2025-fredholm-approach-nonlinear | Abi Jaber et al. 2025 | A | arXiv 2503.04323 (authors per search summary, unverified) | [arXiv 2503.04323](https://arxiv.org/pdf/2503.04323) | R1: optimal P&L vs number of exponentials on a power-law propagator (execution). Closest existing p-sweep; verify authors and bibkey on the title page | `abijaber-2025-fredholm-approach-nonlinear.pdf` |
| [ ] | (key after title page is seen) | TechRxiv preprint, Nov 2025 | B | [10.36227/techrxiv.176412729.90497182/v1](https://doi.org/10.36227/techrxiv.176412729.90497182/v1) | [TechRxiv PDF](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176412729.90497182/v1) | R5: execution under self-exciting flow with a kernel-misspecification robustness section; title and authors not resolved | `<bibkey>.pdf` (derive from the title page) |

## Priority 4: methods-only

| ☐ | Citekey | Author Year | Grade | DOI / landing | Save as (exact filename) |
|---|---------|-------------|-------|---------------|--------------------------|
| [ ] | ogata-1981-lewis-simulation-method | Ogata 1981 | B | [10.1109/TIT.1981.1056305](https://doi.org/10.1109/TIT.1981.1056305) | `ogata-1981-lewis-simulation-method.pdf` |
