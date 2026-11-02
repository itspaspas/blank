"""Tests for screen.py (Task 3, Tier 0 analytic screen).  Run:
    python -m pytest -q output/data-analysis/memory-regret/tests
"""
import os
import sys

import numpy as np
import pytest
from scipy import integrate

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import screen as s  # noqa: E402

LAI_CSV = os.path.join(os.path.dirname(HERE), "data", "lai2023_table2.csv")


@pytest.fixture(scope="module")
def templates():
    return {b: s.build_lift_templates(b, log=lambda *a: None) for b in s.B_GRID}


# ---------------------------------------------------------------- kernel ------------------------

def _int_g_numeric(k, a=0.0):
    """int_a^inf g dt numerically: quad on [a, a+1] plus the tail t = a + 1/v on (0, 1] (algebraic weight)."""
    head = integrate.quad(k.g, a, a + 1.0, limit=200, epsabs=0, epsrel=1e-12, points=[a + k.t0])[0]
    # t = a + 1/v: g(t) dt = K (a + 1/v + t0)^(-b) v^(-2) dv = K v^(b-2) (1 + (a + t0) v)^(-b) dv
    f = lambda v: k.K * (1.0 + (a + k.t0) * v) ** (-k.b)
    tail = integrate.quad(f, 0.0, 1.0, weight="alg", wvar=(k.b - 2.0, 0.0), epsabs=0, epsrel=1e-12)[0]
    return head + tail


@pytest.mark.parametrize("b", s.B_GRID)
@pytest.mark.parametrize("rho", [0.5, 0.95])
def test_kernel_normalisation(b, rho):
    k = s.PowerLawKernel(b, rho)
    assert _int_g_numeric(k) == pytest.approx(rho, rel=1e-8)
    tq, wq = s.NODES
    assert np.sum(wq * k.g(tq)) == pytest.approx(k.mass_on(s.T), rel=1e-10)
    assert np.sum(wq * k.g(tq) ** 2) == pytest.approx(k.l2sq_on(s.T), rel=1e-10)
    # completely monotone representation: int_0^inf theta = g(0)
    tot = integrate.quad(k.theta_density, 0, np.inf, limit=400)[0]
    assert tot == pytest.approx(k.g0(), rel=1e-6)


@pytest.mark.parametrize("b", s.B_GRID)
@pytest.mark.parametrize("D", list(s.DELTAS.values()) + [s.T])
def test_tail_mass_formula(b, D):
    k = s.PowerLawKernel(b, 0.8)
    assert _int_g_numeric(k, D) / k.rho == pytest.approx(k.tail_fraction(D), rel=1e-8)


# ---------------------------------------------------------------- Volterra ----------------------

ALPHA, BETA = 50.0, 100.0   # time scale t0, rho = 0.5


def test_resolvent_exponential_closed_form():
    gfun = lambda t: ALPHA * np.exp(-BETA * np.asarray(t))
    res = s.make_resolvent(gfun, s.H)
    u = np.arange(len(res.psi_R)) * s.H
    exact = ALPHA * np.exp(-(BETA - ALPHA) * u)
    for psi in (res.psi_R, res.psi_c):      # production (Richardson) and plain trapezoid
        l2rel = s.l2_trap(psi - exact, s.H) / s.l2_trap(exact, s.H)
        suprel = np.max(np.abs(psi - exact)) / exact[0]
        assert l2rel < 1e-3 and suprel < 1e-3
    # Richardson is much better than plain
    assert s.l2_trap(res.psi_R - exact, s.H) < 0.01 * s.l2_trap(res.psi_c - exact, s.H)
    # Psi closed form
    Psi_exact = ALPHA / (BETA - ALPHA) * (1 - np.exp(-(BETA - ALPHA) * u))
    assert np.max(np.abs(res.Psi_R - Psi_exact)) < 1e-6


def _truth_forecast_single(gfun, hist, t, mu, h):
    """Production generic route for one history: zeta exact on the fine grid, Richardson (h, h/2)."""
    res = s.make_resolvent(gfun, h)
    L = int(round((s.T - t) / h)) + 1
    uf = np.arange(2 * L - 1) * (h / 2)
    zf = mu + gfun(t + uf[None, :] - hist[:, None]).sum(0)
    m_c = s.volterra_forecast(zf[None, ::2], res.psi_c, h)[0]
    m_f = s.volterra_forecast(zf[None, :], res.psi_f, h / 2)[0]
    return (4 * m_f[::2] - m_c) / 3, m_c, np.arange(L) * h


def test_volterra_forecast_exponential_closed_form():
    gfun = lambda t: ALPHA * np.exp(-BETA * np.asarray(t))
    rng = np.random.default_rng(1)
    hist = np.sort(rng.uniform(0, 0.4, 120))
    hist[-1] = 0.399  # a very recent event
    t, mu = 0.4, 200.0
    m, m_plain, u = _truth_forecast_single(gfun, hist, t, mu, s.H)
    lam_t = mu + ALPHA * np.exp(-BETA * (t - hist)).sum()
    Linf = mu * BETA / (BETA - ALPHA)
    exact = Linf + (lam_t - Linf) * np.exp(-(BETA - ALPHA) * u)
    assert np.max(np.abs(m - exact)) / np.max(exact) < 1e-3
    assert s.l2_trap(m - exact, s.H) / s.l2_trap(exact, s.H) < 1e-5
    assert np.max(np.abs(m_plain - exact)) / np.max(exact) < 1e-3
    # the exact filter route reproduces the closed form to round-off
    es = s.ExpSum([ALPHA], [BETA])
    ex2 = es.forecast(mu, s.filters_at(hist, t, np.array([BETA])), u)
    assert np.max(np.abs(ex2 - exact)) / np.max(exact) < 1e-12


def test_filter_route_vs_generic_volterra_route():
    """Second, independent implementation: exponential filters (exact ODE) vs the generic Volterra
    route (trapezoid resolvent + trapezoid convolution, Richardson) at the production h.
    Moderate rates {1, 5, 20}/T (see operationalisation)."""
    c, x = np.array([0.3, 1.0, 4.0]), np.array([1.0, 5.0, 20.0])
    es = s.ExpSum(c, x)
    rng = np.random.default_rng(2)
    hist = np.sort(rng.uniform(0, 0.4, 150))
    t, mu = 0.4, 50.0
    m_gen, _, u = _truth_forecast_single(es.kernel, hist, t, mu, s.H)
    m_fil = es.forecast(mu, s.filters_at(hist, t, x), u)
    assert s.l2_trap(m_gen - m_fil, s.H) / s.l2_trap(m_fil, s.H) < 1e-6
    assert np.max(np.abs(m_gen - m_fil)) / np.max(np.abs(m_fil)) < 1e-6
    # resolvent: eigen-decomposition vs Volterra
    res = s.make_resolvent(es.kernel, s.H)
    uu = np.arange(len(res.psi_R)) * s.H
    assert np.max(np.abs(res.psi_R - es.resolvent(uu))) / es.resolvent(np.zeros(1))[0] < 1e-6
    assert np.max(np.abs(res.Psi_R - es.Psi(uu))) < 1e-6
    # product-integration L2 distance helper: distance of psi_R to its own exact form is ~0
    assert s.l2_grid_vs_expsum(res.psi_R, s.H, es.a ** 2, es.lam) < 1e-5 * s.l2_trap(res.psi_R, s.H)


def test_decision_filters_vectorised_matches_direct():
    rng = np.random.default_rng(3)
    paths = [np.sort(rng.uniform(-0.5, 1.0, n)) for n in (0, 5, 40, 300)]
    rates = [0.7, 13.0, 450.0]
    X = s.decision_filters(paths, rates)
    for i, r in enumerate(paths):
        for kk, k in enumerate(s.DEC_K):
            direct = s.filters_at(r, k * s.DT_DEC, np.array(rates))
            got = np.array([X[x][i, kk] for x in rates])
            assert np.allclose(got, direct, rtol=1e-12, atol=1e-12)


# ---------------------------------------------------------------- lifts -------------------------

@pytest.mark.parametrize("b", s.B_GRID)
@pytest.mark.parametrize("p", s.P_LIFTS)
def test_gauss_lift_moments(b, p):
    k = s.PowerLawKernel(b, 0.8)
    L = s.lift_gauss(k, p)
    assert np.sum(L["c"]) == pytest.approx(k.g0(), rel=1e-10)            # moment 0: g(0)
    assert np.sum(L["c"] * L["x"]) == pytest.approx(k.minus_dg0(), rel=1e-10)  # moment 1: -g'(0)
    if p >= 2:  # 2p moments: also check moment 2p-1
        m = 2 * p - 1
        from scipy.special import gamma
        exact = k.rho * (k.b - 1) * k.t0 ** (k.b - 1) / gamma(k.b) * gamma(k.b + m) / k.t0 ** (k.b + m)
        assert np.sum(L["c"] * L["x"] ** m) == pytest.approx(exact, rel=1e-8)


def test_mass_preserving_mass_exact(templates):
    for b in s.B_GRID:
        for rho in s.RHO_GRID:
            for p in s.P_LIFTS:
                x, c = s.scale_lift(templates[b]["mass_preserving"][p], rho)
                assert abs(np.sum(c / x) - rho) < 1e-8
                assert templates[b]["mass_preserving"][p]["info"]["feasible"]


def test_all_lift_weights_nonnegative(templates):
    for b in s.B_GRID:
        for ln in s.LIFT_NAMES:
            for p in s.P_LIFTS:
                x, c = s.scale_lift(templates[b][ln][p], 0.95)
                assert np.all(c >= 0) and np.all(x > 0) and len(c) == p
                s.ExpSum(c, x)  # constructor rejects negative weights


def test_nnls_improves_with_p(templates):
    for b in s.B_GRID:
        k = s.PowerLawKernel(b, 1.0)
        e = [s._rel_l2(k, *s.scale_lift(templates[b]["nnls_L2"][p], 1.0)) for p in s.P_LIFTS]
        assert e[-1] < e[0]
        assert all(e[i + 1] <= e[i] * (1 + 1e-6) for i in range(len(e) - 1))  # monotone (warm starts)
        # the NNLS lift is the best L2 lift at every p
        for p in s.P_LIFTS:
            en = s._rel_l2(k, *s.scale_lift(templates[b]["nnls_L2"][p], 1.0))
            for ln in ("gauss", "gauss_composite", "acero_eq3", "mass_preserving"):
                assert en <= s._rel_l2(k, *s.scale_lift(templates[b][ln][p], 1.0)) * (1 + 1e-9)


def test_acero_weights_are_theta_masses():
    k = s.PowerLawKernel(1.4, 0.8)
    beta, c = s.acero_weights(k, 4, 500.0)
    assert np.allclose(beta, [62.5, 187.5, 312.5, 437.5])
    assert np.sum(c) == pytest.approx(k.theta_cdf(500.0), rel=1e-12)
    num = integrate.quad(k.theta_density, 0, 125.0)[0]
    assert c[0] == pytest.approx(num, rel=1e-8)


# ---------------------------------------------------------------- simulation & p0 ---------------

@pytest.mark.parametrize("b,rho", [(1.8, 0.5), (1.8, 0.95)])
def test_simulated_expected_count_matches_400(b, rho):
    k = s.PowerLawKernel(b, rho)
    mu = s.calibrate_mu(s.make_resolvent(k.g, s.H))
    rng = np.random.default_rng([s.BASE_SEED, 12345])
    paths = s.simulate_cluster(mu, k, 0.0, 3000, rng)
    n = np.array([len(r) for r in paths], float)
    se = n.std(ddof=1) / np.sqrt(len(n))
    assert abs(n.mean() - 400.0) < 3 * se
    assert all(np.all(np.diff(r) >= 0) and (r.size == 0 or (r[0] >= 0 and r[-1] <= s.T)) for r in paths)


def test_p0_nhpp_equals_analytic_mean_curve():
    # exponential kernel: Psi closed form
    gfun = lambda t: ALPHA * np.exp(-BETA * np.asarray(t))
    res = s.make_resolvent(gfun, s.H, Tend=2.0)
    for B in (0.0, 1.0):
        t, mu = 0.35, 120.0
        L = int(round((s.T - t) / s.H)) + 1
        u = np.arange(L) * s.H
        got = s.nhpp_curve(mu, res.Psi_R, t, B, s.H, L)
        exact = mu * (1 + ALPHA / (BETA - ALPHA) * (1 - np.exp(-(BETA - ALPHA) * (t + u + B))))
        assert np.max(np.abs(got - exact)) / np.max(exact) < 1e-6


def test_p0_nhpp_is_unbiased_in_mc():
    """E[m_t(u)] = E[lambda_{t+u}] = p0_nhpp: the MC bias of p0_nhpp is at the noise floor."""
    k = s.PowerLawKernel(1.4, 0.8)
    mu = s.calibrate_mu(s.make_resolvent(k.g, s.H))
    G1 = s.lift_gauss(k, 1)
    L = {"gauss": {1: s.ExpSum(G1["c"], G1["x"])}}
    out = s.run_cell_mc(k, "directional", mu, 0.0, 300, [s.BASE_SEED, 4242, 0], L)
    f = out["forecast"][("p0_nhpp", 0)]
    for lab, pr in f["profile"].items():
        assert pr["bias_abs"] < 4 * pr["bias_noise_floor_abs"]
    assert abs(out["sim"]["z_count_vs_expected"]) < 4


# ---------------------------------------------------------------- Lai Table 2 -------------------

def test_lai_table2_rows_and_norms():
    rows = s.load_lai(LAI_CSV)
    assert len(rows) == 16
    get = lambda u, ks, ttm, ty: next(r for r in rows if (r["underlying"], r["K_S"], r["TTM_days"], r["type"]) == (u, ks, ttm, ty))
    r = get("AAPL", "(1.01,1.02]", "6-10", "Buy")
    assert s.lai_rho(r["alpha"], r["beta"], r["delta"]) == pytest.approx(1.0002, abs=2e-4)
    assert s.lai_tail(r["beta"], r["delta"]) == pytest.approx(0.119, abs=1e-3)
    r = get("AAPL", "(1.01,1.02]", "6-10", "Sell")
    assert s.lai_rho(r["alpha"], r["beta"], r["delta"]) == pytest.approx(7.67, abs=5e-3)
    n_super = sum(s.lai_rho(r["alpha"], r["beta"], r["delta"]) > 1 for r in rows)
    assert n_super == 8
    chk = s.lai_table2_check(LAI_CSV)
    assert chk["n_supercritical_L1_gt_1"] == 8 and chk["n_rows"] == 16
    # internal consistency of the Lai mapping with the kernel class
    k = s.PowerLawKernel(r["beta"], s.lai_rho(r["alpha"], r["beta"], r["delta"]), t0=r["delta"])
    assert k.g(0.3) == pytest.approx(r["alpha"] / (0.3 + r["delta"]) ** r["beta"], rel=1e-12)


def test_far_excitation_spline_is_exact_enough():
    k = s.PowerLawKernel(1.15, 0.95)
    rng = np.random.default_rng(5)
    far = np.sort(rng.uniform(-10.0, -s.FAR_LAG, 3000))
    s_tail = np.arange(100, 2001) * (s.H / 2)
    direct = k.g(s_tail[None, :] - far[:, None]).sum(0)
    approx = s.far_excitation(k, far, s_tail)
    assert np.max(np.abs(approx - direct) / direct) < 1e-9



# ---------------------------------------------------------------- review rev 2 ------------------

@pytest.mark.parametrize("b", s.B_GRID)
@pytest.mark.parametrize("p", s.P_LIFTS)
def test_gauss_composite_moments(b, p):
    k = s.PowerLawKernel(b, 0.8)
    L = s.lift_gauss_composite(k, p)
    assert len(L["c"]) == p and np.all(L["c"] >= 0)
    assert np.sum(L["c"]) == pytest.approx(k.g0(), rel=1e-10)               # theta mass preserved
    assert np.sum(L["c"] * L["x"]) == pytest.approx(k.minus_dg0(), rel=1e-10)  # first moment preserved
    e = L["info"].get("edges")
    if p >= 3:
        assert e[-2] == pytest.approx(s.GC_TOP_FACTOR * b / k.t0)
    if p == 1:
        G = s.lift_gauss(k, 1)
        assert np.allclose(L["x"], G["x"]) and np.allclose(L["c"], G["c"])


def test_filter_route_vs_volterra_route_production_nnls(templates):
    """S6: production NNLS p = 4 lift of the hard cell (b = 1.15, rho = 0.95)."""
    x, c = s.scale_lift(templates[1.15]["nnls_L2"][4], 0.95)
    es = s.ExpSum(c, x)
    rng = np.random.default_rng(6)
    hist = np.sort(rng.uniform(0, 0.5, 250))
    t, mu = 0.5, 244.0
    m_gen, _, u = _truth_forecast_single(es.kernel, hist, t, mu, s.H)
    m_fil = es.forecast(mu, s.filters_at(hist, t, x), u)
    assert s.l2_trap(m_gen - m_fil, s.H) / s.l2_trap(m_fil, s.H) < 1e-6


def test_int_Psi_and_mean_matched_mu():
    k = s.PowerLawKernel(1.4, 0.8)
    for ln, L in (("gauss", s.lift_gauss(k, 3)), ("gc", s.lift_gauss_composite(k, 4))):
        es = s.ExpSum(L["c"], L["x"])
        u = np.linspace(0, 1, 400001)
        for B in (0.0, 1.0, 10.0):
            num = np.trapezoid(es.Psi(u + B), u)
            assert es.int_Psi(B) == pytest.approx(num, rel=1e-8)
            assert es.mean_matched_mu(B) * (1 + num) == pytest.approx(400.0, rel=1e-8)


def test_calibrate_mu_B_matches_expected_count():
    k = s.PowerLawKernel(1.8, 0.8)
    res = s.make_resolvent(k.g, s.H, Tend=2.0)
    mu1 = s.calibrate_mu_B(res, 1.0)
    assert s.expected_day_count(mu1, res, 1.0) == pytest.approx(400.0, rel=1e-12)
    assert mu1 < s.calibrate_mu(s.make_resolvent(k.g, s.H))   # pre-day memory -> smaller baseline


def test_run_cell_mc_matches_direct_per_path_computation():
    """Pipeline check: per-path truth (generic route) and exact lifted forecasts, base and mean-matched."""
    k = s.PowerLawKernel(1.25, 0.8)
    mu = s.calibrate_mu(s.make_resolvent(k.g, s.H))
    G = s.lift_gauss_composite(k, 3)
    es = s.ExpSum(G["c"], G["x"])
    mu_hat = es.mean_matched_mu(0.0)
    seed = [s.BASE_SEED, 777, 0]
    out = s.run_cell_mc(k, "directional", mu, 0.0, 2, seed, {"gc": {3: es}}, mm_mu={("gc", 3): mu_hat})
    paths, *_ = s._simulate_with_counts(k, "directional", mu, 0.0, 2, seed)
    kk = 9
    t = s.DEC_K[kk] * s.DT_DEC
    vals, vals_mm, cnt = [], [], []
    for r in paths:
        hist = r[r <= t]
        m, _, u = _truth_forecast_single(k.g, hist, t, mu, s.H)
        X = s.filters_at(r, t, es.x_all)
        dm = es.forecast(mu, X, u) - m
        dmm = es.forecast(mu_hat, X, u) - m
        vals.append(s.l2_trap(dm, s.H))
        vals_mm.append(s.l2_trap(dmm, s.H))
        w = s.trap_weights(len(u), s.H)
        cnt.append(abs(dm @ w) / (m @ w))
    f, fm = out["forecast"][("gc", 3)], out["forecast"][("gc_mm", 3)]
    assert f["profile_all_t"]["abs_mean"][kk] == pytest.approx(np.mean(vals), rel=1e-6)
    assert fm["profile_all_t"]["abs_mean"][kk] == pytest.approx(np.mean(vals_mm), rel=1e-6)
    assert f["profile_all_t"]["count_rel_mean"][kk] == pytest.approx(np.mean(cnt), rel=1e-6)
    # N3 of the NHPP forecast is 1 by construction; N2 of p0_nhpp is 1
    n = out["forecast"][("p0_nhpp", 0)]
    assert n["N2_ratio_to_nhpp"] == pytest.approx(1.0) and n["N3_fluct_over_truth_fluct_tavg"] == pytest.approx(1.0, rel=1e-6)


def test_h2_classification():
    assert s._classify(4, [2, 2, 3, 2]) == "consistent_strict"
    assert s._classify(">8", [2, ">8", 3, 2]) == "consistent_weak"
    assert s._classify(0, [1, 3, 4, 1]) == "reversed_strict"
    assert s._classify(0, [0, 3, 4, 0]) == "reversed_weak"
    assert s._classify(3, [3, 3, 3, 3]) == "flat"
    assert s._classify(">8", [">8"] * 4) == "flat_unresolved_all_gt8"
    assert s._classify(3, [2, 4, 3, 3]) == "mixed"


def test_numerical_floor_small():
    k = s.PowerLawKernel(1.8, 0.95)
    mu = s.calibrate_mu(s.make_resolvent(k.g, s.H))
    fl = s.numerical_floor(k, "directional", mu, 0.0, 8, [s.BASE_SEED, 31, 0, 2])
    assert 0 < fl["floor_rel_to_mean_norm"] < 1e-4
    assert fl["plain_trapezoid_error_abs"] > 10 * fl["floor_abs"]
