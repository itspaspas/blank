# memory-regret — Tier 0 analytic screen (Task 3)

Task 3 of `input/ideas/lai2023-gaps-and-memory-plan.md` (status **pre-registered 2026-11-01**,
`pre-registered: true`). **There is no control problem in this tier.** The screen measures how far
a *p*-factor exponential lift of a shifted power-law Hawkes kernel moves the conditional intensity
forecast.
- It does **not** measure regret, and it does **not** test H1 or H2.
- Every H2-related number here is an **informational screen proxy**.
- Revision 2 (after the two-stage review) **adds** supplementary, labelled material. It changes no
  pre-registered element.

## Files

| Path | What |
|---|---|
| `screen.py` | Library + CLI. `python screen.py` writes `results/screen.json` |
| `tests/test_screen.py` | pytest suite: kernel, Volterra, lifts, simulation, pipeline, Lai Table 2 |
| `data/lai2023_table2.csv` | Lai, Gao & Li (2023) Table 2 (p. 782; PDF physical page 7), 16 rows |
| `results/screen.json` | All results (compact JSON, floats to 8 significant digits) |

## How to run

```bash
cd output/data-analysis/memory-regret
python -m pytest -q tests            # ~20 s
python screen.py                     # ~17 min on 4 cores (1001 s measured); writes results/screen.json
python screen.py --quick --out /tmp/quick.json   # 4-cell smoke run (~40 s)
```

- **Environment:** Python 3.13, numpy 2.5, scipy 1.18. The run is deterministic.
- **Seeds:** every random stream is a numpy `SeedSequence` built from `BASE_SEED = 20261101` (see
  `screen.json → seeds`).
- **Provenance:** `screen.json` records `git_commit`, the dirty flag, and `code_sha256` for
  `screen.py`, the tests and the CSV.

## Model and conventions (project notation)

- **Kernel:** g(t) = ρ(b−1)t₀^{b−1}(t+t₀)^{−b}, with ‖g‖₁ = ρ, T = 1 and t₀ = 0.01 T. Its
  representation is g = ∫e^{−xt}ϑ(dx) with ϑ(dx) = ρ(b−1)t₀^{b−1}/Γ(b)·x^{b−1}e^{−t₀x}dx.
- **Cells (frozen):** b ∈ {1.15, 1.25, 1.4, 1.8} × ρ ∈ {0.5, 0.8, 0.95} × {common-mode,
  directional}; p ∈ {0, 1, 2, 3, 4, 6, 8}.
- **Forecast** (Barzykin 2026b eqs. 19–22): m_t = ζ_t + ψ*ζ_t, where ψ = g + g*ψ and
  ζ_t(u) = μ + Σ_{r≤t} g(t+u−r).
  - The lifted forecast m̂_t uses the same equations with ĝ_p = Σc_j e^{−x_j t}, the same history and
    the same μ.
  - Δm_t = m̂_t − m_t on [0, T−t], evaluated at t_k = k/20 for k = 1..19.
- **Regimes:** ρ is the spectral radius of the 2×2 side branching matrix.
  - Directional: Φ = diag(g, 0).
  - Common-mode: Φ = (g/2)[[1,1],[1,1]], so the total process is Hawkes(2μ, g) and each side's
    forecast is half the total.
- **Baseline:** μ∫₀^T(1+Ψ) = 400 per side at B = 0, which operationalises the plan's "μ̄T ≈ 400".
- **History:** the primary convention is B = 0 (fresh start).
  - Same-μ sensitivity runs (as specified) use B = 1 and B = 10.
  - Recalibrated runs (supplementary, review Q4) use μ_B = 400/∫₀^T(1+Ψ(s+B))ds, so the expected
    in-day count per side stays 400.

## Lifts

| key | rule |
|---|---|
| `gauss` (i) | One global p-point generalised Gauss–Laguerre rule for ϑ (α = b−1). It matches 2p moments, i.e. short-lag behaviour only. |
| `gauss_composite` (i-b) | **Added in rev 2.** Composite 1-point Gauss rule for ϑ on [0, ξ₁), geometric interior breakpoints up to ξ_{p−1} = b/t₀ (top factor 1, fixed a priori), and [ξ_{p−1}, ∞). Each interval gets weight ϑ(I_j) and its node at the ϑ-mean; this preserves ϑ-moments 0 and 1 exactly. ξ₁ is the single scalar, chosen to minimise the L²[0,T] error. It operationalises the plan's "Gauss-type quadrature (Alfonsi–Kebaier)"; AK 2024 is not on disk. |
| `acero_eq3` (supplementary) | Acero–Plank–Zhang 2026 eq. (3), with K₁ = 0 and K₂ minimising their Prop. 1 bound. The bound is ≈ ‖g‖ for every p ≤ 8 (vacuous), so this minimiser is degenerate. |
| `nnls_L2` (ii) | Best L²[0,T] fit: multi-start L-BFGS-B over the log-rates (analytic variable-projection gradient) with an inner NNLS. |
| `mass_preserving` (iii) | Geometric rates on [1/T, b/t₀], with weights from the exact QP min ‖g−ĝ‖ subject to Σc/x = ρ and c ≥ 0. Some weights end at zero, so p_effective < p (p = 8 → 4–5 nonzero factors). |
| `p0_nhpp` / `p0_baseline` | p = 0 forecasts. `p0_nhpp`, m̂ = μ(1+Ψ(t+u)), is THE p = 0 entry. `p0_baseline` (m̂ = μ) is supplementary. Their `kernel` block holds the formal metrics of ĝ = 0. |
| `<lift>_mean_matched` | **Supplementary (rev 2).** Same lifted kernel and history, with baseline μ̂ set so that μ̂∫₀^T(1+Ψ̂(s+B_cal))ds = 400. The lifted model then reproduces the expected daily count. |

## Numerics

- **u-grid h = t₀/10.**
  - Truth: trapezoid Volterra for ψ plus trapezoid convolution (FFT), Richardson-extrapolated
    from (h, h/2) and evaluated on the h-grid. ζ is exact at the grid points.
  - Lifts: exact closed form, through the exponential filters X_j(t) and an eigen-decomposition.
- **Why Richardson.** With the plain trapezoid, the mean ‖Δm‖ of these entries changed by more
  than the dispatch's 2% target between h and h/2:
  - nnls_L2 p = 4: 11.0% (hard cell) and 15.6% (b = 1.8, ρ = 0.5);
  - nnls_L2 p = 8: about 75% in both cells;
  - mass_preserving p = 8: 23.6% at b = 1.8, ρ = 0.5.

  Every other checked entry moved by ≤ 1.2%, including mass_preserving p = 4 at b = 1.8 (5.6%,
  which is above 2% but was not counted in the p ∈ {1, 4} summary of rev 1). With Richardson
  the largest change is 1.6e-4 over p ∈ {1, 4} and 0.9% over p ∈ {1, 4, 8}. The p = 8 change is
  NNLS p = 8, which sits at the numerical floor.
- **Target source.** The 2% target comes from the Task 3 dispatch. The plan's own criterion (Stop
  Criterion) is a < 10% change of the exact anchor's *regret* under 2× refinement.
- **Numerical floor (rev 2).** For each cell, the floor is E‖m_R(h) − m_R(h/2)‖. It is computed
  on independent histories: 100 paths at B = 0 and 50 for the recalibrated burn-in runs. Entries
  with mean ‖Δm‖ below 10× the floor are flagged `below_numerical_resolution`; at B = 0 this
  catches only NNLS p = 8, as-specified and mean-matched.
- **Statistics.** Equal weight on the 19 decision times, averaged within each path first. SEs are
  across paths. The bias part is ‖EΔm_t‖ and the fluctuation part is √(E‖Δm_t − EΔm_t‖²).

## Metrics and H2-proxy normalisations

- **Kernel metrics:**
  - L² error (absolute and relative), L¹ error, sup error on [0,T];
  - total mass, mass in [0,T], subcriticality;
  - resolvent error ‖ψ̂ − ψ‖;
  - tail mass beyond Δ ∈ {T/800, T/400 (reference, provisional until Task 4), T/100, T/10} and
    beyond T.
- **Forecast metrics:**
  - ‖Δm‖ (absolute and relative);
  - count error |∫₀^{T−t}Δm| / ∫m (rev 2, review Q8);
  - bias and fluctuation parts;
  - profile over all 19 t (B = 0).
- **H2 screen proxy** p\*_screen(τ) = min{p : metric ≤ τ}, for τ ∈ {0.10, 0.05, 0.02}. Metrics:
  - **N1:** ‖Δm‖/‖m‖. This is the pre-registered dispatch proxy; p = 0 counts via `p0_nhpp`.
  - **N1 lifts-only:** as N1, with p = 0 excluded.
  - **N2:** ‖Δm_p‖/‖Δm_{p0_nhpp}‖, the share of the history's information that the lift loses.
  - **N3:** the fluctuation part only (bias removed), divided by the truth's own fluctuation
    √(E‖m−Em‖²).
  - **C:** the count error.
- **Runs and lifts:** the proxy is computed for B = 0, B = 1 and B = 10 (same-μ and recalibrated),
  for all lifts and their mean-matched variants, in both regimes.
- **Classes** compare the hard cell (1.15, 0.95) with the four easy cells
  {1.4, 1.8} × {0.5, 0.8}:
  - consistent_strict / consistent_weak (hard ≥ every easy, ties allowed in the weak case);
  - reversed_strict / reversed_weak;
  - flat (and flat (>8));
  - mixed.

## Lai Table 2 check: it contradicts the design doc and the plan anchor

- **Transcription:** all 16 rows match the PDF (journal p. 782 = physical page 7).
- **Plan's test row:** AAPL (1.01,1.02] 6–10 Buy gives ‖g‖₁ = 1.0002 with tail mass beyond 1 Lai
  time unit 0.119.
- **Supercritical rows:** **8 of the 16 averaged-parameter rows are supercritical** (‖g‖₁ > 1, up
  to 7.67 for AAPL (1.01,1.02] 6–10 Sell).
- **Design-doc claim (a) is false.** The claim is "tail mass 0.4–3% for β ≥ 1.45 and 12–55% for
  β ≈ 1.07–1.2".
  - β ≥ 1.45 rows: tail masses span 0.37–18.3%, and 7 of 8 rows lie outside 0.4–3% (11.9%; BAC
    8.3%, 3.0%, 18.3%, 4.4%; 3.1%; 0.37%).
  - β ∈ [1.07, 1.2] rows: tail masses span 26.7–55.9%; one row is above 55%.
- **Plan anchor (b) is false.** The anchor is "AAPL (1.01,1.02] 0–5 buy: b ≈ 1.12, ρ ≈ 0.59 → cell
  b = 1.15, ρ = 0.5". The computed value is **ρ = 0.746**, so the nearest cell is **b = 1.15,
  ρ = 0.8**, not ρ = 0.5.
- Lai's time unit is unstated, so the tail masses are in Lai's units.

## Results at a glance

**Mean relative ‖Δm_t‖** (directional, B = 0; mean over 1000 paths × 19 decision times). Each entry is
`as-specified → mean-matched`, and the bracket gives the t-averaged bias / fluctuation parts (relative to
‖E m_t‖) of the as-specified lift. The mean-matched fluctuation part equals the as-specified one by construction.
`†` means below numerical resolution (< 10× the cell's floor). All SEs are < 3e-3.

| cell (b, ρ) · p0_nhpp | lift | p=1 | p=2 | p=4 | p=8 |
|---|---|---|---|---|---|
| 1.15, 0.95 · 0.0198 [0.0005/0.0241] | gauss | 0.355 → 0.086 [0.355/0.022] | 0.308 → 0.084 [0.308/0.020] | 0.249 → 0.079 [0.249/0.017] | 0.180 → 0.070 [0.180/0.013] |
|  | gauss_composite | 0.355 → 0.086 [0.355/0.022] | 0.232 → 0.073 [0.232/0.015] | 0.088 → 0.031 [0.088/0.005] | 0.024 → 0.007 [0.024/0.001] |
|  | nnls_L2 | 0.215 → 0.077 [0.215/0.016] | 0.034 → 0.026 [0.034/0.005] | 5.2e-04 → 4.7e-04 [4.9e-04/2.1e-04] | 5.1e-07 → 5.0e-07 [3.5e-07/3.8e-07] |
|  | mass_preserving | 1.709 → 0.332 [1.710/0.098] | 0.127 → 0.111 [0.127/0.019] | 0.225 → 0.114 [0.225/0.018] | 0.227 → 0.115 [0.228/0.018] |
|  | acero_eq3 | 0.426 → 0.083 [0.426/0.023] | 0.416 → 0.079 [0.417/0.023] | 0.401 → 0.073 [0.401/0.022] | 0.377 → 0.064 [0.377/0.021] |
| 1.15, 0.5 · 0.0080 [0.0003/0.0097] | gauss | 0.180 → 0.038 [0.180/0.009] | 0.152 → 0.037 [0.152/0.008] | 0.119 → 0.035 [0.119/0.006] | 0.085 → 0.031 [0.085/0.005] |
|  | gauss_composite | 0.180 → 0.038 [0.180/0.009] | 0.111 → 0.032 [0.111/0.005] | 0.041 → 0.013 [0.041/0.002] | 0.011 → 0.003 [0.011/4.6e-04] |
|  | nnls_L2 | 0.102 → 0.034 [0.102/0.006] | 0.017 → 0.013 [0.017/0.002] | 2.6e-04 → 2.3e-04 [2.5e-04/9.2e-05] | 2.7e-07 → 2.7e-07 [2.1e-07/1.8e-07] |
|  | mass_preserving | 0.417 → 0.047 [0.417/0.022] | 0.066 → 0.054 [0.066/0.008] | 0.102 → 0.049 [0.102/0.006] | 0.103 → 0.049 [0.103/0.006] |
|  | acero_eq3 | 0.227 → 0.036 [0.227/0.010] | 0.222 → 0.033 [0.222/0.009] | 0.212 → 0.030 [0.212/0.009] | 0.198 → 0.025 [0.198/0.008] |
| 1.8, 0.95 · 0.1779 [0.0067/0.2210] | gauss | 0.795 → 0.249 [0.801/0.210] | 0.714 → 0.235 [0.722/0.195] | 0.582 → 0.206 [0.589/0.166] | 0.400 → 0.160 [0.407/0.121] |
|  | gauss_composite | 0.795 → 0.249 [0.801/0.210] | 0.647 → 0.215 [0.654/0.175] | 0.397 → 0.145 [0.402/0.109] | 0.174 → 0.066 [0.176/0.045] |
|  | nnls_L2 | 0.618 → 0.218 [0.626/0.177] | 0.263 → 0.122 [0.267/0.087] | 0.003 → 0.003 [0.002/0.003] | 6.6e-06† → 4.9e-06† [4.5e-06/4.5e-06] |
|  | mass_preserving | 0.099 → 0.128 [0.051/0.113] | 0.526 → 0.139 [0.529/0.142] | 0.036 → 0.020 [0.036/0.017] | 0.009 → 0.006 [0.008/0.004] |
|  | acero_eq3 | 0.886 → 0.258 [0.890/0.221] | 0.886 → 0.258 [0.890/0.221] | 0.884 → 0.257 [0.888/0.220] | 0.880 → 0.255 [0.884/0.219] |
| 1.8, 0.5 · 0.0250 [0.0009/0.0306] | gauss | 0.331 → 0.043 [0.331/0.024] | 0.254 → 0.039 [0.254/0.020] | 0.173 → 0.034 [0.173/0.014] | 0.103 → 0.027 [0.103/0.009] |
|  | gauss_composite | 0.331 → 0.043 [0.331/0.024] | 0.211 → 0.035 [0.211/0.015] | 0.103 → 0.024 [0.103/0.007] | 0.041 → 0.011 [0.041/0.002] |
|  | nnls_L2 | 0.190 → 0.036 [0.190/0.017] | 0.065 → 0.023 [0.065/0.007] | 0.001 → 0.001 [0.001/4.7e-04] | 1.8e-06† → 1.8e-06† [1.4e-06/1.3e-06] |
|  | mass_preserving | 0.034 → 0.035 [0.026/0.024] | 0.157 → 0.036 [0.157/0.020] | 0.008 → 0.003 [0.007/0.002] | 0.002 → 0.001 [0.002/7.4e-04] |
|  | acero_eq3 | 0.481 → 0.047 [0.481/0.031] | 0.480 → 0.047 [0.480/0.031] | 0.479 → 0.047 [0.479/0.031] | 0.475 → 0.045 [0.475/0.030] |

**Kernel relative L²[0,T] error** (independent of ρ; total mass Σc/x in brackets, as a fraction of ρ)

| b | lift | p=1 | p=2 | p=4 | p=8 |
|---|---|---|---|---|---|
| 1.15 | gauss | 0.487 (0.13) | 0.352 (0.19) | 0.239 (0.26) | 0.155 (0.32) |
| 1.15 | gauss_composite | 0.487 (0.13) | 0.219 (0.27) | 0.078 (0.42) | 0.029 (0.52) |
| 1.15 | nnls_L2 | 0.262 (0.29) | 0.083 (0.45) | 0.005 (0.54) | 1.0e-05 (0.58) |
| 1.15 | mass_preserving | 1.014 (1.00) | 0.343 (1.00) | 0.180 (1.00) | 0.181 (1.00) |
| 1.15 | acero_eq3 | 0.995 (0.12) | 0.989 (0.16) | 0.980 (0.22) | 0.964 (0.27) |
| 1.8 | gauss | 0.324 (0.44) | 0.184 (0.60) | 0.093 (0.74) | 0.042 (0.84) |
| 1.8 | gauss_composite | 0.324 (0.44) | 0.130 (0.68) | 0.046 (0.84) | 0.024 (0.92) |
| 1.8 | nnls_L2 | 0.158 (0.71) | 0.038 (0.89) | 0.003 (0.97) | 1.1e-05 (0.99) |
| 1.8 | mass_preserving | 0.715 (1.00) | 0.284 (1.00) | 0.029 (1.00) | 0.020 (1.00) |
| 1.8 | acero_eq3 | 1.000 (0.01) | 1.000 (0.01) | 1.000 (0.02) | 0.999 (0.04) |

**Numerical floor per cell** (relative to ‖m‖, B = 0; floor_abs = E‖m_R(h) − m_R(h/2)‖)

| b \ ρ | 0.5 | 0.8 | 0.95 |
|---|---|---|---|
| 1.15 | 2.2e-08 | 3.8e-08 | 4.7e-08 |
| 1.25 | 4.4e-08 | 8.0e-08 | 9.9e-08 |
| 1.4 | 9.1e-08 | 1.5e-07 | 1.5e-07 |
| 1.8 | 2.7e-07 | 5.0e-07 | 4.9e-06 |

**H2 screen-proxy direction (informational, screen proxy, not a test of H2)**: directional, τ = 0.05

| lift | normalisation | B=0 | B=1_same_mu | B=1_recalibrated | B=10_same_mu | B=10_recalibrated |
|---|---|---|---|---|---|---|
| nnls_L2 | N1_rel_to_norm_m | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| nnls_L2 | N1_lifts_only | reversed_strict | reversed_weak | reversed_weak | consistent_weak | consistent_weak |
| nnls_L2 | N2_ratio_to_nhpp_error | reversed_weak | flat | flat | flat (>8) | flat (>8) |
| nnls_L2 | N3_fluct_only | reversed_strict | consistent_weak | consistent_weak | consistent_weak | consistent_weak |
| nnls_L2 | C_count_error_rel | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| gauss_composite | N1_rel_to_norm_m | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| gauss_composite | N1_lifts_only | reversed_weak | reversed_weak | reversed_weak | flat (>8) | flat (>8) |
| gauss_composite | N2_ratio_to_nhpp_error | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss_composite | N3_fluct_only | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss_composite | C_count_error_rel | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| nnls_L2_mm | N1_rel_to_norm_m | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| nnls_L2_mm | N1_lifts_only | mixed | mixed | reversed_weak | consistent_weak | reversed_weak |
| nnls_L2_mm | N2_ratio_to_nhpp_error | reversed_weak | flat | consistent_weak | flat (>8) | consistent_weak |
| nnls_L2_mm | N3_fluct_only | reversed_strict | consistent_weak | consistent_weak | consistent_weak | consistent_weak |
| nnls_L2_mm | C_count_error_rel | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| gauss_composite_mm | N1_rel_to_norm_m | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| gauss_composite_mm | N1_lifts_only | mixed | mixed | reversed_weak | consistent_weak | reversed_weak |
| gauss_composite_mm | N2_ratio_to_nhpp_error | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss_composite_mm | N3_fluct_only | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss_composite_mm | C_count_error_rel | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| mass_preserving | N1_rel_to_norm_m | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| mass_preserving | N1_lifts_only | consistent_strict | consistent_weak | consistent_weak | consistent_weak | consistent_weak |
| mass_preserving | N2_ratio_to_nhpp_error | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| mass_preserving | N3_fluct_only | consistent_weak | consistent_weak | consistent_weak | consistent_weak | consistent_weak |
| mass_preserving | C_count_error_rel | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| gauss | N1_rel_to_norm_m | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |
| gauss | N1_lifts_only | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss | N2_ratio_to_nhpp_error | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss | N3_fluct_only | flat (>8) | flat (>8) | flat (>8) | flat (>8) | flat (>8) |
| gauss | C_count_error_rel | reversed_weak | reversed_weak | reversed_weak | reversed_weak | reversed_weak |

**How to read the direction matrix (stated conditionally; there is no single headline):**

- **NNLS at B = 0 (fresh start).** No normalisation supports H2's direction. Most are flat, or
  reversed by a single grid step; only the normalisations that count p0 are clearly reversed.
  - N1 (p0 counted) and C: weakly reversed. `p0_nhpp` already meets τ in the hard cell.
  - N1 lifts-only: strictly reversed.
  - N2 is essentially flat: p\* = 4 in 11 of 12 directional cells. The only "reversal" is one
    easy cell, (1.8, 0.5), at p\* = 6.
  - N3 is one grid step reversed: the hard cell has p\* = 3, against 4 in (1.4, 0.5), (1.4, 0.8)
    and (1.8, ρ ≤ 0.8).
  - Cause: at B = 0 the heavy-tailed cells have a large μ and roughly half their kernel mass
    beyond T, so the baseline dominates the intensity.
  - Caveat: N2 and N3 reuse N1's τ grid {0.10, 0.05, 0.02}. A τ calibrated for each normalisation
    (e.g. from ε_eq relative to the Poisson-policy regret) needs Tier 1/2 regrets and is left to
    Task 6–7.
- **NNLS with pre-day history (B = 1, B = 10, either μ convention).**
  - The bias-removed N3 becomes weakly consistent: the hard cell needs ≥ as many factors as every
    easy cell.
  - N1 lifts-only becomes weakly consistent at B = 10 only.
  - N2 is flat at B = 1 and unresolved (> 8 everywhere) at B = 10.
  - N1 with p0 counted and C stay weakly reversed, because `p0_nhpp` already meets τ in the hard
    cell.
- **Mean-matched NNLS.** N2 is weakly consistent under the recalibrated burn-in (B = 1 and
  B = 10), and N3 is weakly consistent for every B ≥ 1.
- **Lift (i-b).** It never reaches τ = 0.05 under N2 or N3 (flat, > 8). It is weakly reversed under
  N1 and C.
- **Pattern "≤ 2 factors in easy cells, ≥ 4 in the hard cell".** It appears only for lift (iii),
  as-specified or mean-matched, under N1 lifts-only, mostly at τ = 0.10. Every such case is an
  artefact: lift (iii)'s error plateaus (p_effective ≤ 5), so its hard cell never reaches τ (> 8).
- **Overall.** The proxy's direction is set by the normalisation and the burn-in convention, not by
  the lifts. None of this tests H2.

**Burn-in (recalibrated μ_B, directional; mean relative ‖Δm‖ for as-specified → mean-matched).**
Lifts fitted on [0,T] lags lose accuracy once pre-day history matters. For NNLS p = 4 in the hard
cell, the error goes from 5.2e-4 at B = 0 to 0.0146 → 0.0084 at B = 1 and 0.145 → 0.0065 at
B = 10, while `p0_nhpp` stays at 0.020–0.025. Mean matching removes most of the level bias: at
B = 10, mean-matched NNLS beats `p0_nhpp` from p = 1 in the hard cell (0.019 vs 0.025).

## Assumption checks (verified in code)

| Check | Expected | Got | Pass |
|---|---|---|---|
| Simulated E[N^side_T] vs expected, 24 cells × 5 runs | \|z\| < 3 | z ∈ [−2.53, 2.51] | yes |
| `p0_nhpp` unbiased (E m_t = E λ) | bias ≈ noise floor | e.g. 5e-4 vs floor 7.6e-4 (hard cell) | yes |
| Convergence h vs h/2 (Richardson), p ∈ {1, 4} | < 2% | ≤ 1.6e-4 | yes |
| Same, p ∈ {1, 4, 8} | < 2% | ≤ 0.91% (NNLS p = 8, at the floor) | yes |
| Plain trapezoid, p ∈ {1, 4} | < 2% | 11.0% / 15.6% (nnls p = 4) | **no**: Richardson adopted |
| Generic grid route vs exact filter route (production lifts) | small | ≤ 7.7e-7 (Richardson) | yes |
| Lift weights ≥ 0; lift (iii) mass = ρ; (i-b) moments 0 and 1 | exact | yes | yes |
| All lifts subcritical (‖ĝ‖₁ < 1) | report | yes, all subcritical | yes |
| Lai Table 2 transcription vs PDF p. 782 | 16 rows | 16 rows, no mismatch | yes |

## Limitations

- **No control layer.** Tier 0 measures forecast error, not regret, and p\*_screen is not H2's p\*.
  The proxy's direction depends on the normalisation and on the burn-in convention.
- **Regimes.** In Tier 0 the two regimes differ only through the count scale.
- **B = 0 is optimistic for long memory.** Lifts fitted on [0,T] lags are wrong at lags > T, and
  the burn-in runs expose this.
- **Gauss-type lifts.** Lift (i) captures short-lag moments only. Lift (i-b) fixes its top
  breakpoint a priori. Neither is the verified Alfonsi–Kebaier construction.
- **Acero lift.** The bound-minimising K₂ is degenerate.
- **NNLS mass.** NNLS does not control mass beyond T.
- **Lift (iii)** has p_effective < p in many entries.
- **Mean matching** fixes the expected count, not the shape of Ψ̂.
- **Floors** are estimated on 50–100 paths and are not computed for the same-μ burn-in runs.
- **Burn-in statistics.** The burn-in runs use independent (non-CRN) histories and fewer paths.

## Pre-registration discipline

Every free choice the plan does not fix is listed in `screen.json → operationalisation`. Every
departure from the dispatch spec, and every rev-2 addition, is listed in `screen.json → deviations`.
The hypotheses are untouched.
