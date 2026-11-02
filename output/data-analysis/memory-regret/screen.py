#!/usr/bin/env python3
"""
screen.py -- Tier 0 analytic screen (no control problem).

Task 3 of input/ideas/lai2023-gaps-and-memory-plan.md (status: pre-registered 2026-11-01,
`pre-registered: true`).  Library + CLI:  `python screen.py`  writes results/screen.json.

What it does
------------
For the shifted power-law Hawkes kernel  g(t) = rho (b-1) t0^(b-1) (t+t0)^(-b)  (||g||_1 = rho)
on the frozen 24-cell grid  b in {1.15,1.25,1.4,1.8} x rho in {0.5,0.8,0.95} x regime in
{common-mode, directional}, and for p in {0,1,2,3,4,6,8}:
  * builds p-factor exponential lifts  g_p(t) = sum_j c_j exp(-x_j t), c_j >= 0, by
      (i)  Gauss quadrature in the decay rate (generalised Gauss-Laguerre for theta),
      (i-acero) Acero-Plank-Zhang 2026 eq. (3) [supplementary],
      (ii) NNLS best L2[0,T] fit (outer optimisation over the rates),
      (iii) mass-preserving log-spaced fit (sum_j c_j/x_j = rho exactly);
  * computes kernel-level errors and kernel tail masses (truth and lift);
  * computes the exact conditional intensity forecast  m_t(u) = E[lambda_{t+u} | F_t]
    (Barzykin 2026b eqs. 19-22: m = zeta + psi*zeta, psi = g + g*psi) and the p-factor
    forecast  m^_t(u)  (same equations, lifted kernel, same history, same mu) on simulated
    histories, and reports the forecast error  Dm_t = m^_t - m_t  in L2[0, T-t].

ASSUMPTIONS (stated explicitly; mandatory)
------------------------------------------
A1  Kernel: shifted power law, T = 1 (activity-time day), t0 = 0.01 T, completely monotone with
    theta(dx) = rho(b-1)t0^(b-1)/Gamma(b) x^(b-1) e^(-t0 x) dx.  Truth is subcritical (rho < 1).
A2  Flow-driven: requests excite, fills do not; Tier 0 has NO control layer, so ||Dm|| is a
    forecast error, NOT a regret.  Nothing here tests H1 or H2.
A3  History convention (primary, B = 0): fresh start, no events before t = 0 (Barzykin eq. 21
    integrates from 0).  This ignores pre-day memory; the B = 1 T (and, if run, B = 10 T)
    burn-in sensitivity quantifies the effect.
A4  Baseline mu is constant and is the same for truth and lift; calibrated so that
    E[N^side_T] = 400 under the B = 0 convention (operationalisation of "mu_bar T ~ 400 events
    per side").
A5  Regimes: rho is the spectral radius of the 2x2 side branching matrix.  directional:
    Phi = diag(g, 0) (excited side univariate Hawkes(mu, g); Dm measured on it).
    common-mode: Phi = (g/2)[[1,1],[1,1]]: N_tot is univariate Hawkes(2 mu, g); each side's
    forecast is half the total forecast; Dm is reported per side.  Because Phi is symmetric the
    side labels do not enter the per-side forecast.  In Tier 0 the two regimes therefore differ
    only through the count scale (2 mu vs mu).
A6  Monte Carlo paths are independent (independent cluster simulations); all lifts and p of a
    cell use the same histories (common random numbers).  SEs are across-path SEs of per-path
    averages (the 19 decision times within a path are correlated, so they are averaged first).
A7  Numerical: u-grid step h = t0/10; trapezoid Volterra for psi and trapezoid convolution for
    psi*zeta, with Richardson extrapolation (h, h/2) of the TRUE forecast (see
    OPERATIONALISATION / DEVIATIONS; the plain trapezoid has an O(h^2) bias of 0.5-1.8 % in psi
    at b = 1.8, rho = 0.95 and is reported alongside in the convergence check).  Per-cell numerical
    floors (Richardson(h) vs Richardson(h/2)) flag entries below resolution.
A8  Review revision 2 (2026-11-01): lift (i-b), mean-matched lift variants, count-error proxy,
    normalisations N2/N3/C of the H2 screen proxy, recalibrated burn-in.  All are SUPPLEMENTARY
    and labelled; the pre-registered elements are unchanged.  Lifted forecasts are evaluated exactly (closed-form linear ODE of the
    exponential filters); their generic Volterra-route evaluation is used only as a test.

Seeds: BASE_SEED below; every random stream is a numpy SeedSequence derived from it and is
recorded in screen.json.
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import platform
import subprocess
import sys
import time
from dataclasses import dataclass, field

import numpy as np
import scipy
from scipy import fft as sfft
from scipy import linalg, optimize, special

# ----------------------------------------------------------------------------------------------
# Constants (frozen by the plan unless flagged as operationalisation)
# ----------------------------------------------------------------------------------------------
T = 1.0
T0 = 0.01 * T
H = T0 / 10.0
B_GRID = [1.15, 1.25, 1.4, 1.8]
RHO_GRID = [0.5, 0.8, 0.95]
REGIMES = ["common-mode", "directional"]
P_GRID = [0, 1, 2, 3, 4, 6, 8]
P_LIFTS = [1, 2, 3, 4, 6, 8]
P_MAX = 8
DELTAS = {"T/800": T / 800, "T/400": T / 400, "T/100": T / 100, "T/10": T / 10}
REF_DELTA = "T/400"
DT_DEC = T / 20
DEC_K = list(range(1, 20))  # t_k = k/20, k = 1..19
PROFILE_K = {"0.25": 5, "0.5": 10, "0.75": 15}
TARGET_SIDE_COUNT = 400.0
LIFT_NAMES = ["gauss", "gauss_composite", "acero_eq3", "nnls_L2", "mass_preserving"]
GC_TOP_FACTOR = 1.0   # lift (i-b): top finite breakpoint = GC_TOP_FACTOR * b/t0 (the theta-mean), fixed a priori
BASE_SEED = 20261101
NNLS_SEED = 7
NNLS_N_JITTER = 8
NNLS_JITTER_SD = 0.5
NNLS_LOGRATE_BOUNDS = (np.log(0.01 / T), np.log(50.0 / T0))
ACERO_K2_SEARCH = (1e-2 / T, 1e3 / T0)
TAU_GRID = [0.10, 0.05, 0.02]

# ----------------------------------------------------------------------------------------------
# Small numerical helpers
# ----------------------------------------------------------------------------------------------


def phi1(lam, u):
    """int_0^u e^{lam v} dv = expm1(lam u)/lam, stable for lam -> 0 (broadcasting)."""
    lam = np.asarray(lam, dtype=float)
    u = np.asarray(u, dtype=float)
    z = lam * u
    small = np.abs(z) < 1e-10
    lam_safe = np.where(lam == 0.0, 1.0, lam)
    return np.where(small, u * (1.0 + 0.5 * z), np.expm1(z) / lam_safe)


def hat_integrals(z):
    """I0(z)=int_0^1 (1-s)e^{zs}ds, I1(z)=int_0^1 s e^{zs}ds, stable for small |z|."""
    z = np.asarray(z, dtype=float)
    small = np.abs(z) < 1e-3
    zs = np.where(small, 1.0, z)
    I0 = np.where(small, 0.5 + z / 6 + z * z / 24 + z**3 / 120, (np.expm1(zs) - zs) / zs**2)
    I1 = np.where(small, 0.5 + z / 3 + z * z / 8 + z**3 / 30, (zs * np.exp(zs) - np.expm1(zs)) / zs**2)
    return I0, I1


def trap_weights(L, h):
    w = np.full(L, h)
    if L == 1:
        return np.zeros(1)
    w[0] = w[-1] = 0.5 * h
    return w


def l2_trap(F, h):
    """L2 norm along the last axis by the trapezoid rule on a uniform grid of step h."""
    w = trap_weights(F.shape[-1], h)
    return np.sqrt(np.sum(w * F * F, axis=-1))


def quad_nodes(Tend=T, t_first=1e-9, ratio=1.06, order=16):
    """Composite Gauss-Legendre on a geometric mesh of [0, Tend] (resolves t0 and fast exps)."""
    n = int(np.ceil(np.log(Tend / t_first) / np.log(ratio)))
    e = np.concatenate([[0.0], np.geomspace(t_first, Tend, n + 1)])
    xg, wg = np.polynomial.legendre.leggauss(order)
    a, b = e[:-1], e[1:]
    m, hh = 0.5 * (a + b), 0.5 * (b - a)
    return (m[:, None] + hh[:, None] * xg).ravel(), (hh[:, None] * wg).ravel()


NODES = quad_nodes()  # ~5.7k nodes, used for all kernel integrals on [0,T]
NODES_FIT = quad_nodes(ratio=1.12, order=12)  # cheaper set for the NNLS outer loop
DENSE_SUP = np.unique(np.concatenate([NODES[0], np.linspace(0, T, 100001)]))

# ----------------------------------------------------------------------------------------------
# Kernel
# ----------------------------------------------------------------------------------------------


@dataclass
class PowerLawKernel:
    b: float
    rho: float
    t0: float = T0

    @property
    def K(self):
        return self.rho * (self.b - 1) * self.t0 ** (self.b - 1)

    def g(self, t):
        t = np.asarray(t, dtype=float)
        return self.K * np.exp(-self.b * np.log(t + self.t0))

    def g0(self):
        return self.rho * (self.b - 1) / self.t0

    def minus_dg0(self):
        return self.rho * self.b * (self.b - 1) / self.t0**2

    def tail_fraction(self, D):
        """(t0/(D+t0))^(b-1): kernel mass beyond lag D as a fraction of rho."""
        return (self.t0 / (D + self.t0)) ** (self.b - 1)

    def mass_on(self, Tend=T):
        return self.rho * (1.0 - self.tail_fraction(Tend))

    def l2sq_on(self, Tend=T):
        b = self.b
        return self.K**2 * (self.t0 ** (1 - 2 * b) - (Tend + self.t0) ** (1 - 2 * b)) / (2 * b - 1)

    def theta_density(self, x):
        b = self.b
        return self.rho * (b - 1) * self.t0 ** (b - 1) / special.gamma(b) * x ** (b - 1) * np.exp(-self.t0 * x)

    def theta_cdf(self, X):
        """theta([0, X])."""
        return self.rho * (self.b - 1) / self.t0 * special.gammainc(self.b, self.t0 * np.asarray(X))

    def upper_tail_kernel(self, t, K2):
        """g_u^{K2}(t) = int_{K2}^inf e^{-xt} theta(dx) = g(t) Q(b, K2 (t+t0))."""
        return self.g(t) * special.gammaincc(self.b, K2 * (np.asarray(t) + self.t0))

    def lag_sample(self, U):
        """Inverse-CDF sample from the density g/rho: lag = t0 (U^{-1/(b-1)} - 1)."""
        with np.errstate(over="ignore", divide="ignore"):
            return self.t0 * (U ** (-1.0 / (self.b - 1)) - 1.0)


# ----------------------------------------------------------------------------------------------
# Exponential-sum (lifted) model: kernel, exact resolvent, exact forecast via filters
# ----------------------------------------------------------------------------------------------


class ExpSum:
    """g^(t) = sum_j c_j exp(-x_j t), c_j >= 0.

    Lifted state Y_j(t) = sum_{r<=t} exp(-x_j (t-r)) (the exponential filters X_j).  Given F_t,
    y_j(u) = E[Y_j(t+u)|F_t] solves y' = (-D + 1 c^T) y + mu 1, y(0) = X(t), and
    m^(u) = mu + c^T y(u).  With s = sqrt(c), M = -D + s s^T (symmetric, S A = M S), eigh(M) =
    (lam, V), a = V^T s:
        psi^(u) = sum_k a_k^2 e^{lam_k u}                 (resolvent, Barzykin eq. 22 response)
        m^(u)   = mu (1 + Psi^(u)) + sum_k a_k e^{lam_k u} (V^T (s * X))_k .
    """

    def __init__(self, c, x):
        c = np.asarray(c, dtype=float)
        x = np.asarray(x, dtype=float)
        if np.any(c < -1e-14):
            raise ValueError("negative lift weight")
        self.c_all, self.x_all = c.copy(), x.copy()
        keep = c > 0
        self.c, self.x = c[keep], x[keep]
        self.p_nominal = len(c)
        self.p_eff = int(keep.sum())
        s = np.sqrt(self.c)
        M = -np.diag(self.x) + np.outer(s, s)
        lam, V = np.linalg.eigh(M)
        self.s, self.lam, self.V = s, lam, V
        self.a = V.T @ s

    def kernel(self, t):
        t = np.asarray(t, dtype=float)
        return (self.c[:, None] * np.exp(-np.outer(self.x, t.ravel()))).sum(0).reshape(t.shape)

    def mass(self):
        return float(np.sum(self.c / self.x))

    def mass_on(self, Tend=T):
        return float(np.sum(self.c * (-np.expm1(-self.x * Tend)) / self.x))

    def mass_beyond(self, D):
        return float(np.sum(self.c * np.exp(-self.x * D) / self.x))

    def resolvent(self, u):
        return (self.a**2) @ np.exp(np.outer(self.lam, u))

    def Psi(self, u):
        return (self.a**2) @ phi1(self.lam[:, None], np.asarray(u)[None, :])

    def int_Psi(self, B=0.0, Tend=T):
        """int_B^{B+Tend} Psi^(s) ds, exact."""
        lam, a2 = self.lam, self.a**2
        hi, lo = B + Tend, B
        out = np.empty_like(lam)
        small = np.abs(lam) * hi < 1e-7
        ls = np.where(small, 1.0, lam)
        out = np.where(small, 0.5 * (hi * hi - lo * lo),
                       (np.expm1(ls * hi) - np.expm1(ls * lo)) / ls**2 - Tend / ls)
        return float(a2 @ out)

    def mean_matched_mu(self, B=0.0):
        """mu^ such that the lifted model reproduces E[N^side over the day] = 400 (fresh start at -B)."""
        return TARGET_SIDE_COUNT / (T + self.int_Psi(B, T))

    def coeffs(self, X):
        """X: (..., p_nominal) filter values for ALL nominal rates -> (..., p_eff) coefficients."""
        Xe = X[..., self.c_all > 0]
        return self.a * ((self.s * Xe) @ self.V)

    def forecast(self, mu, X, u):
        """Exact lifted forecast m^(u) for filter state(s) X (shape (..., p_nominal))."""
        d = self.coeffs(np.asarray(X, dtype=float))
        return mu * (1.0 + self.Psi(u)) + d @ np.exp(np.outer(self.lam, u))


def decision_filters(paths, rates, dec_k=DEC_K, dt=DT_DEC):
    """X_j(t_k) for all paths and decision times, vectorised: each event contributes
    e^{-x (t_{k(i)} - r_i)} to its block k(i) = first k with t_k >= r_i, then
    X(t_k) = e^{-x dt} X(t_{k-1}) + block_k.  Returns {rate: (P, K) array}."""
    P, K = len(paths), len(dec_k)
    tk_arr = np.array(dec_k) * dt
    all_r = np.concatenate(paths) if P else np.zeros(0)
    all_pid = np.concatenate([np.full(len(r), i) for i, r in enumerate(paths)])
    kidx = np.searchsorted(tk_arr, all_r, side="left") + 1   # block k: t_{k-1} < r <= t_k (k=1 incl. pre-day)
    m_in = kidx <= K
    r_in, p_in, k_in = all_r[m_in], all_pid[m_in], kidx[m_in]
    lag_to_dec = tk_arr[k_in - 1] - r_in
    flat = p_in * K + (k_in - 1)
    out = {}
    for x in rates:
        bins = np.bincount(flat, weights=np.exp(-x * lag_to_dec), minlength=P * K).reshape(P, K)
        dec = np.exp(-x * dt)
        for k in range(1, K):
            bins[:, k] += dec * bins[:, k - 1]
        out[float(x)] = bins
    return out


FAR_LAG = 0.5 * T   # pre-day events older than this: smooth contribution, sub-grid + cubic spline
FAR_SUB = 10


def far_excitation(kern, r_far, s_tail, sub=FAR_SUB):
    """sum_{r in r_far} g(s - r) on s_tail for events with s - r >= FAR_LAG: evaluated on every
    `sub`-th grid point and interpolated by a cubic spline (error ~ (sub*h)^4 g''''/384, < 1e-9 rel)."""
    from scipy.interpolate import CubicSpline
    idx = np.arange(0, len(s_tail), sub)
    if idx[-1] != len(s_tail) - 1:
        idx = np.append(idx, len(s_tail) - 1)
    acc = np.zeros(len(idx))
    for c0 in range(0, r_far.size, 1024):
        acc += kern.g(s_tail[idx][None, :] - r_far[c0:c0 + 1024, None]).sum(0)
    if len(idx) < 4:
        return kern.g(s_tail[None, :] - r_far[:, None]).sum(0)
    return CubicSpline(s_tail[idx], acc)(s_tail)


def nhpp_curve(mu_proc, Psi_R, t, B, h, L):
    """p0_nhpp forecast m^_t(u) = mu (1 + Psi(t + u + B)) on u = 0..(L-1)h (fresh start at -B)."""
    i0 = int(round((t + B) / h))
    return mu_proc * (1.0 + Psi_R[i0:i0 + L])


def filters_at(events, t, rates):
    """X_j(t) = sum_{r<=t} exp(-x_j (t-r)) for a single history (direct; used in tests)."""
    r = np.asarray(events)
    r = r[r <= t]
    return np.exp(-np.outer(rates, t - r)).sum(1)


# ----------------------------------------------------------------------------------------------
# Volterra machinery (generic route; used for the truth)
# ----------------------------------------------------------------------------------------------


def volterra_resolvent(gv, h):
    """Trapezoid solution of psi = g + g*psi on the grid u_n = n h (gv = g(u_n))."""
    N = len(gv)
    psi = np.empty(N)
    psi[0] = gv[0]
    den = 1.0 - 0.5 * h * gv[0]
    for n in range(1, N):
        s = 0.5 * gv[n] * psi[0] + np.dot(gv[n - 1:0:-1], psi[1:n])
        psi[n] = (gv[n] + h * s) / den
    return psi


def cumtrap(f, h):
    out = np.zeros_like(f)
    out[1:] = np.cumsum(0.5 * h * (f[1:] + f[:-1]))
    return out


def volterra_forecast(Z, psi, h):
    """m = zeta + psi*zeta with trapezoid convolution; Z: (P, L) zeta on the grid, psi len >= L."""
    Z = np.atleast_2d(Z)
    P, L = Z.shape
    if L == 1:
        return Z.copy()
    ps = psi[:L]
    n = sfft.next_fast_len(2 * L - 1, real=True)
    c = sfft.irfft(sfft.rfft(Z, n, axis=1, workers=-1) * sfft.rfft(ps, n)[None, :], n, axis=1, workers=-1)[:, :L]
    return Z + h * (c - 0.5 * ps[None, :] * Z[:, :1] - 0.5 * ps[0] * Z)


@dataclass
class Resolvent:
    """psi and Psi on the evaluation grid (step h_eval) for a kernel; Richardson (h, h/2)."""
    h_eval: float
    psi_c: np.ndarray        # trapezoid at h_eval on [0, Tend]
    psi_f: np.ndarray        # trapezoid at h_eval/2 on [0, Tend]
    psi_R: np.ndarray        # Richardson on the h_eval grid
    Psi_c: np.ndarray
    Psi_R: np.ndarray
    int1Psi_c: float         # int_0^T (1+Psi) dt, plain trapezoid
    int1Psi_R: float         # Richardson


def make_resolvent(gfun, h_eval, Tend=T):
    Nc = int(round(Tend / h_eval))
    uc = np.arange(Nc + 1) * h_eval
    uf = np.arange(2 * Nc + 1) * (h_eval / 2)
    psi_c = volterra_resolvent(gfun(uc), h_eval)
    psi_f = volterra_resolvent(gfun(uf), h_eval / 2)
    Psi_c, Psi_f = cumtrap(psi_c, h_eval), cumtrap(psi_f, h_eval / 2)
    psi_R = (4 * psi_f[::2] - psi_c) / 3
    Psi_R = (4 * Psi_f[::2] - Psi_c) / 3
    nT = int(round(T / h_eval))
    Ic = float(np.sum(trap_weights(nT + 1, h_eval) * (1 + Psi_c[: nT + 1])))
    If = float(np.sum(trap_weights(2 * nT + 1, h_eval / 2) * (1 + Psi_f[: 2 * nT + 1])))
    return Resolvent(h_eval, psi_c, psi_f, psi_R, Psi_c, Psi_R, Ic, (4 * If - Ic) / 3)


def l2_grid_vs_expsum(psi, h, A, lam):
    """|| psi_lin - sum_k A_k e^{lam_k u} ||_{L2[0, N h]}: psi piecewise linear on the grid,
    exponentials integrated exactly against the hat functions (product integration)."""
    N = len(psi) - 1
    Tend = N * h
    a, b = psi[:-1], psi[1:]
    n_lin = h / 3 * np.sum(a * a + a * b + b * b)
    S = lam[:, None] + lam[None, :]
    n_hat = A @ phi1(S, Tend) @ A
    I0, I1 = hat_integrals(lam * h)
    un = np.arange(N) * h
    E = np.exp(np.outer(lam, un))
    cross = np.sum(A * h * (E @ a * I0 + E @ b * I1))
    return float(np.sqrt(max(n_lin - 2 * cross + n_hat, 0.0)))


# ----------------------------------------------------------------------------------------------
# Lifts.  All lifts are fitted for the unit kernel (rho = 1): the optimal rates do not depend on
# rho and the weights scale linearly in rho (every objective/constraint is homogeneous in rho).
# ----------------------------------------------------------------------------------------------


def gram(x, Tend=T):
    S = x[:, None] + x[None, :]
    return -np.expm1(-S * Tend) / S


def gram_deriv(s, Tend=T):
    """d/ds (1-e^{-sT})/s."""
    e = np.exp(-s * Tend)
    return (Tend * e * s - (1 - e)) / s**2


def lift_gauss(kern, p):
    y, W = special.roots_genlaguerre(p, kern.b - 1)
    x = y / kern.t0
    c = kern.rho * (kern.b - 1) / (kern.t0 * special.gamma(kern.b)) * W
    return {"x": x, "c": c, "info": {"rule": "generalised Gauss-Laguerre, alpha=b-1, y=t0 x"}}


def _theta_interval_moments(kern, lo, hi):
    """theta mass and first moment on [lo, hi) (hi may be inf), via regularised incomplete gammas."""
    b, t0 = kern.b, kern.t0
    def dP(a):
        hfin = np.where(np.isinf(hi), 1.0, hi)
        Ph = np.where(np.isinf(hi), 1.0, special.gammainc(a, t0 * hfin))
        Qh = np.where(np.isinf(hi), 0.0, special.gammaincc(a, t0 * hfin))
        useP = np.where(np.isinf(hi), False, t0 * hfin < a)
        return np.where(useP, Ph - special.gammainc(a, t0 * lo), special.gammaincc(a, t0 * lo) - Qh)
    m0 = kern.rho * (b - 1) / t0 * dP(b)
    m1 = kern.rho * (b - 1) * b / t0**2 * dP(b + 1)
    return m0, m1


def gauss_composite_edges(kern, p, xi1, top_factor=GC_TOP_FACTOR):
    if p == 1:
        return np.array([0.0, np.inf])
    if p == 2:
        return np.array([0.0, xi1, np.inf])
    top = top_factor * kern.b / kern.t0
    return np.concatenate([[0.0], np.geomspace(xi1, top, p - 1), [np.inf]])


def gauss_composite_weights(kern, edges):
    """1-point Gauss rule for theta restricted to each interval: weight theta(I_j), node = theta-mean."""
    m0, m1 = _theta_interval_moments(kern, edges[:-1], edges[1:])
    lo = edges[:-1]
    x = np.where(m0 > 0, m1 / np.where(m0 > 0, m0, 1.0), np.maximum(lo, 1e-12))
    return x, np.maximum(m0, 0.0)


def lift_gauss_composite(kern, p):
    """(i-b): composite 1-point Gauss quadrature in the decay rate on a geometric partition
    I_1 = [0, xi_1), I_j = [xi_{j-1}, xi_j) geometric, I_p = [xi_{p-1}, inf), xi_{p-1} = b/t0 (p >= 3);
    the single scalar xi_1 minimises the L2[0,T] error (p = 2: xi_1 is the only breakpoint)."""
    if p == 1:
        x, c = gauss_composite_weights(kern, gauss_composite_edges(kern, 1, None))
        return {"x": x, "c": c, "info": {"rule": "p = 1: single interval [0, inf) = lift (i) at p = 1"}}
    hi = np.log(1e3 / kern.t0) if p == 2 else np.log(GC_TOP_FACTOR * kern.b / kern.t0 * 0.999)
    grid = np.linspace(np.log(1e-3 / T), hi, 240)

    def f(z):
        v = _rel_l2(kern, *gauss_composite_weights(kern, gauss_composite_edges(kern, p, np.exp(z))))
        return v if np.isfinite(v) else 1e9
    vals = np.array([f(z) for z in grid])
    i = int(np.argmin(vals))
    o = optimize.minimize_scalar(f, bounds=(grid[max(i - 1, 0)], grid[min(i + 1, len(grid) - 1)]), method="bounded",
                                 options={"xatol": 1e-9})
    z = o.x if o.fun <= vals[i] else grid[i]
    edges = gauss_composite_edges(kern, p, np.exp(z))
    x, c = gauss_composite_weights(kern, edges)
    return {"x": x, "c": c, "info": {
        "rule": "composite 1-point Gauss for theta on [0,xi_1),[xi_1,xi_2),...,[xi_{p-1},inf); interior breakpoints "
                "geometric from xi_1 to xi_{p-1} = GC_TOP_FACTOR*b/t0 (p >= 3); xi_1 minimises the L2[0,T] error "
                "(240-point log grid on [1e-3/T, upper] + bounded refinement)",
        "label": "(i-b) operationalisation of the plan's 'Gauss-type quadrature (Alfonsi-Kebaier)', AK 2024 not on disk",
        "xi_1": float(np.exp(z)), "top_breakpoint": float(edges[-2]), "top_factor": GC_TOP_FACTOR,
        "edges": [float(e) for e in edges[:-1]] + ["inf"], "rel_L2_err": float(min(o.fun, vals[i])),
        "xi_1_at_search_edge": bool(i in (0, len(grid) - 1))}}


def acero_bound(kern, p, K2, nodes=NODES):
    tq, wq = nodes
    gu = kern.upper_tail_kernel(tq, K2)
    eps_u = np.sqrt(np.sum(wq * gu * gu))
    return float(eps_u + T**1.5 * K2 * kern.theta_cdf(K2) / (np.sqrt(3) * p)), float(eps_u)


def acero_weights(kern, p, K2, K1=0.0):
    e = np.linspace(K1, K2, p + 1)
    beta = 0.5 * (e[1:] + e[:-1])
    c = kern.theta_cdf(e[1:]) - kern.theta_cdf(e[:-1])
    return beta, np.maximum(c, 0.0)


def _rel_l2(kern, x, c, nodes=NODES):
    tq, wq = nodes
    d = kern.g(tq) - (c[:, None] * np.exp(-np.outer(x, tq))).sum(0)
    return float(np.sqrt(np.sum(wq * d * d) / kern.l2sq_on(T)))


def lift_acero(kern, p):
    logK = np.linspace(np.log(ACERO_K2_SEARCH[0]), np.log(ACERO_K2_SEARCH[1]), 400)
    vals = np.array([acero_bound(kern, p, np.exp(k))[0] for k in logK])
    i = int(np.argmin(vals))
    lo, hi = logK[max(i - 1, 0)], logK[min(i + 1, len(logK) - 1)]
    o = optimize.minimize_scalar(lambda k: acero_bound(kern, p, np.exp(k))[0], bounds=(lo, hi), method="bounded",
                                 options={"xatol": 1e-10})
    K2 = float(np.exp(o.x)) if o.fun <= vals[i] else float(np.exp(logK[i]))
    bnd, eps_u = acero_bound(kern, p, K2)
    beta, c = acero_weights(kern, p, K2)
    # information only: K2 that minimises the ACTUAL L2 error of eq. (3) (not used as the lift)
    errs = np.array([_rel_l2(kern, *acero_weights(kern, p, np.exp(k))) for k in logK[::4]])
    j = int(np.argmin(errs))
    return {"x": beta, "c": c, "info": {
        "K1": 0.0, "K2_bound_minimiser": K2, "prop1_bound_at_K2": bnd, "eps_u_at_K2": eps_u,
        "g_L2_norm": float(np.sqrt(kern.l2sq_on(T))),
        "bound_over_g_L2_norm": bnd / float(np.sqrt(kern.l2sq_on(T))),
        "K2_search_range": list(ACERO_K2_SEARCH), "K2_at_search_edge": bool(i in (0, len(logK) - 1)),
        "info_only_K2_minimising_actual_L2_error": float(np.exp(logK[::4][j])),
        "info_only_min_actual_rel_L2_error": float(errs[j])}}


class L2Fitter:
    """min_{c>=0} ||g - sum c_j e^{-x_j t}||^2_{L2[0,T]} for given rates (exact Gram, quadrature r)."""

    def __init__(self, kern, nodes=NODES_FIT):
        self.kern = kern
        self.tq, self.wq = nodes
        self.wg = self.wq * kern.g(self.tq)
        self.wgt = self.wg * self.tq
        self.g2 = kern.l2sq_on(T)
        self.nevals = 0

    def solve(self, x):
        self.nevals += 1
        G = gram(x)
        Ex = np.exp(-np.outer(x, self.tq))
        r = Ex @ self.wg
        jit = 1e-14 * np.trace(G)
        for _ in range(8):
            try:
                Lc = np.linalg.cholesky(G + jit * np.eye(len(x)))
                break
            except np.linalg.LinAlgError:
                jit *= 100
        bb = linalg.solve_triangular(Lc, r, lower=True)
        c, _ = optimize.nnls(Lc.T, bb)
        F = self.g2 - 2 * c @ r + c @ G @ c
        return max(F, 1e-300), c, G, r, Ex

    def obj_grad(self, z):
        """log(F/g2) and its gradient in z = log x (envelope theorem through the NNLS optimum)."""
        x = np.exp(z)
        F, c, G, r, Ex = self.solve(x)
        dr = -(Ex @ self.wgt)                                   # d r_j / d x_j
        dG = gram_deriv(x[:, None] + x[None, :])
        dF = -2 * c * dr + 2 * c * (dG @ c)
        return np.log(F / self.g2), x * dF / F


def lift_nnls(kern_unit, p, prev_z=None):
    fit = L2Fitter(kern_unit)
    lo, hi = NNLS_LOGRATE_BOUNDS
    b = kern_unit.b
    base = np.log(np.geomspace(1 / T, b / T0, p)) if p > 1 else np.array([0.5 * np.log(b / (T0 * T))])
    rng = np.random.default_rng([NNLS_SEED, int(round(b * 100)), p])
    starts = [("logspaced", base)]
    starts += [(f"jitter{i}", base + rng.normal(0, NNLS_JITTER_SD, p)) for i in range(NNLS_N_JITTER)]
    y, _ = special.roots_genlaguerre(p, b - 1)
    starts.append(("gauss_nodes", np.log(y / T0)))
    if prev_z is not None and p > len(prev_z):
        k = p - len(prev_z)
        extra = np.log(np.geomspace(1 / T, b / T0, k + 2))[1:-1]
        starts.append(("warm_prev_p", np.concatenate([prev_z, extra])))
    results = []
    for name, z0 in starts:
        z0 = np.clip(np.sort(z0), lo + 1e-9, hi - 1e-9)
        o = optimize.minimize(fit.obj_grad, z0, jac=True, method="L-BFGS-B", bounds=[(lo, hi)] * p,
                              options={"maxiter": 3000, "ftol": 1e-13, "gtol": 1e-9})
        results.append((float(o.fun), name, o.x))
    results.sort(key=lambda t: t[0])
    best_f, best_name, zb = results[0]
    # polish from the best start
    o = optimize.minimize(fit.obj_grad, zb, jac=True, method="L-BFGS-B", bounds=[(lo, hi)] * p,
                          options={"maxiter": 3000, "ftol": 1e-15, "gtol": 1e-11})
    if o.fun < best_f:
        best_f, zb = float(o.fun), o.x
    order = np.argsort(zb)
    zb = zb[order]
    x = np.exp(zb)
    _, c, *_ = fit.solve(x)
    rel_errs = np.sqrt(np.exp([r[0] for r in results]))
    return {"x": x, "c": c, "z": zb, "info": {
        "n_starts": len(starts), "start_names": [s[0] for s in starts], "best_start": best_name,
        "rel_L2_err_best_fit_quadrature": float(np.sqrt(np.exp(best_f))),
        "rel_L2_err_by_start_sorted": [float(v) for v in rel_errs],
        "rel_L2_err_median_over_starts": float(np.median(rel_errs)),
        "n_objective_evals": fit.nevals, "active_components": int(np.sum(c > 0)),
        "lograte_bounds": [float(lo), float(hi)],
        "rates_at_bound": bool(np.any(np.isclose(zb, lo, atol=1e-6)) or np.any(np.isclose(zb, hi, atol=1e-6)))}}


def lift_mass_preserving(kern, p, nodes=NODES):
    x = np.geomspace(1 / T, kern.b / kern.t0, p) if p > 1 else np.array([np.sqrt(kern.b / (kern.t0 * T))])
    tq, wq = nodes
    G = gram(x)
    r = np.exp(-np.outer(x, tq)) @ (wq * kern.g(tq))
    a = 1.0 / x
    best = None
    n_feasible = 0
    for k in range(1, p + 1):
        for S in itertools.combinations(range(p), k):
            S = list(S)
            KKT = np.zeros((k + 1, k + 1))
            KKT[:k, :k] = 2 * G[np.ix_(S, S)]
            KKT[:k, k] = a[S]
            KKT[k, :k] = a[S]
            rhs = np.concatenate([2 * r[S], [kern.rho]])
            sol = np.linalg.lstsq(KKT, rhs, rcond=None)[0][:k]
            if np.all(sol >= -1e-13):
                n_feasible += 1
                cS = np.maximum(sol, 0.0)
                cS *= kern.rho / (a[S] @ cS)
                c = np.zeros(p)
                c[S] = cS
                F = kern.l2sq_on(T) - 2 * c @ r + c @ G @ c
                if best is None or F < best[0]:
                    best = (F, c, S)
    if best is None:
        return {"x": x, "c": None, "info": {"feasible": False}}
    F, c, S = best
    return {"x": x, "c": c, "info": {"feasible": True, "support": [int(s) for s in S],
                                     "n_feasible_supports": n_feasible,
                                     "rate_grid": "geometric on [1/T, b/t0]" if p > 1 else "sqrt(b/(t0 T))",
                                     "mass_constraint_residual": float(np.sum(c / x) - kern.rho)}}


def build_lift_templates(b, log=print):
    """Unit-rho lifts for one exponent b (weights scale with rho)."""
    ku = PowerLawKernel(b, 1.0)
    out = {name: {} for name in LIFT_NAMES}
    prev_z = None
    for p in P_LIFTS:
        out["gauss"][p] = lift_gauss(ku, p)
        out["gauss_composite"][p] = lift_gauss_composite(ku, p)
        out["acero_eq3"][p] = lift_acero(ku, p)
        t = time.time()
        out["nnls_L2"][p] = lift_nnls(ku, p, prev_z)
        prev_z = out["nnls_L2"][p]["z"]
        out["mass_preserving"][p] = lift_mass_preserving(ku, p)
        log(f"  lifts b={b} p={p}: nnls relL2={out['nnls_L2'][p]['info']['rel_L2_err_best_fit_quadrature']:.3e} "
            f"({time.time() - t:.1f}s)")
    return out


def scale_lift(tmpl, rho):
    return np.asarray(tmpl["x"], float), rho * np.asarray(tmpl["c"], float)


# ----------------------------------------------------------------------------------------------
# Kernel metrics
# ----------------------------------------------------------------------------------------------


def kernel_metrics(kern, lift: ExpSum, res: Resolvent):
    tq, wq = NODES
    d = kern.g(tq) - lift.kernel(tq)
    l2 = float(np.sqrt(np.sum(wq * d * d)))
    gl2 = float(np.sqrt(kern.l2sq_on(T)))
    dsup = np.abs(kern.g(DENSE_SUP) - lift.kernel(DENSE_SUP))
    nT = int(round(T / res.h_eval))
    psiR = res.psi_R[: nT + 1]
    psi_l2 = float(np.sqrt(res.h_eval / 3 * np.sum(psiR[:-1] ** 2 + psiR[:-1] * psiR[1:] + psiR[1:] ** 2)))
    res_err = l2_grid_vs_expsum(psiR, res.h_eval, lift.a**2, lift.lam)
    tail = {}
    for name, D in DELTAS.items():
        tm = lift.mass_beyond(D)
        tail[name] = {"lift_abs": tm, "lift_fraction_of_lift_mass": tm / lift.mass() if lift.mass() > 0 else None,
                      "truth_abs": kern.rho * kern.tail_fraction(D), "truth_fraction": kern.tail_fraction(D),
                      "reference_Delta": name == REF_DELTA}
    mT = lift.mass_beyond(T)
    return {
        "rates": [float(v) for v in lift.x_all], "weights": [float(v) for v in lift.c_all],
        "p_effective": lift.p_eff,
        "L2_abs": l2, "L2_rel": l2 / gl2, "L1_abs": float(np.sum(wq * np.abs(d))),
        "L1_rel_to_mass_in_T": float(np.sum(wq * np.abs(d))) / kern.mass_on(T),
        "sup_abs": float(dsup.max()), "sup_rel_to_g0": float(dsup.max() / kern.g0()),
        "mass_total": lift.mass(), "mass_total_minus_rho": lift.mass() - kern.rho,
        "mass_in_T": lift.mass_on(T), "mass_in_T_truth": kern.mass_on(T),
        "subcritical": bool(lift.mass() < 1.0),
        "resolvent_L2_err_abs": res_err, "resolvent_L2_err_rel": res_err / psi_l2,
        "tail_mass_by_Delta": tail,
        "mass_beyond_T": {"lift_abs": mT, "lift_fraction_of_lift_mass": mT / lift.mass() if lift.mass() > 0 else None,
                          "truth_abs": kern.rho * kern.tail_fraction(T), "truth_fraction": kern.tail_fraction(T)},
    }


def kernel_metrics_zero(kern, res: Resolvent):
    """Kernel metrics of g^ = 0 (formal p = 0 entry; p0_nhpp itself uses the exact mean curve)."""
    nT = int(round(T / res.h_eval))
    psiR = res.psi_R[: nT + 1]
    psi_l2 = float(np.sqrt(res.h_eval / 3 * np.sum(psiR[:-1] ** 2 + psiR[:-1] * psiR[1:] + psiR[1:] ** 2)))
    gl2 = float(np.sqrt(kern.l2sq_on(T)))
    return {"note": "formal metrics of g^ = 0; p0_nhpp forecasts with the exact mean curve mu(1+Psi), p0_baseline "
                    "with mu", "rates": [], "weights": [], "p_effective": 0,
            "L2_abs": gl2, "L2_rel": 1.0, "L1_abs": kern.mass_on(T), "L1_rel_to_mass_in_T": 1.0,
            "sup_abs": kern.g0(), "sup_rel_to_g0": 1.0, "mass_total": 0.0, "mass_total_minus_rho": -kern.rho,
            "mass_in_T": 0.0, "mass_in_T_truth": kern.mass_on(T), "subcritical": True,
            "resolvent_L2_err_abs": psi_l2, "resolvent_L2_err_rel": 1.0,
            "tail_mass_by_Delta": {k: {"lift_abs": 0.0, "truth_abs": kern.rho * kern.tail_fraction(D),
                                       "truth_fraction": kern.tail_fraction(D), "reference_Delta": k == REF_DELTA}
                                   for k, D in DELTAS.items()}}


# ----------------------------------------------------------------------------------------------
# Simulation (exact cluster / branching representation)
# ----------------------------------------------------------------------------------------------


def simulate_cluster(mu_proc, kern, B, n_paths, rng, Tend=T):
    """Hawkes(mu_proc, g) on [-B, Tend], fresh start at -B. Returns list of sorted arrays."""
    n_imm = rng.poisson(mu_proc * (Tend + B), n_paths)
    t = rng.uniform(-B, Tend, n_imm.sum())
    pid = np.repeat(np.arange(n_paths), n_imm)
    all_t, all_p = [t], [pid]
    cur_t, cur_p = t, pid
    while cur_t.size:
        nch = rng.poisson(kern.rho, cur_t.size)
        pt, pp = np.repeat(cur_t, nch), np.repeat(cur_p, nch)
        ct = pt + kern.lag_sample(rng.random(pt.size))
        keep = ct <= Tend
        cur_t, cur_p = ct[keep], pp[keep]
        all_t.append(cur_t)
        all_p.append(cur_p)
    t = np.concatenate(all_t)
    pid = np.concatenate(all_p)
    order = np.lexsort((t, pid))
    t, pid = t[order], pid[order]
    splits = np.searchsorted(pid, np.arange(1, n_paths))
    return np.split(t, splits)


def calibrate_mu(res: Resolvent):
    """mu such that mu * int_0^T (1 + Psi) = 400 (expected requests per side, B = 0)."""
    return TARGET_SIDE_COUNT / res.int1Psi_R


# ----------------------------------------------------------------------------------------------
# Forecast-error Monte Carlo for one cell
# ----------------------------------------------------------------------------------------------


@dataclass
class Acc:
    """Accumulates per-(path, t) quantities plus per-t mean curves for one forecast."""
    P: int
    K: int

    def __post_init__(self):
        self.abs_ = np.zeros((self.P, self.K))      # side * ||Dm_t||_L2[0,T-t]
        self.rel = np.zeros((self.P, self.K))       # ||Dm_t|| / ||m_t||
        self.cnt_abs = np.zeros((self.P, self.K))   # side * |int_0^{T-t} Dm_t du|
        self.cnt_rel = np.zeros((self.P, self.K))   # |int Dm_t| / int m_t
        self.bias_abs = np.zeros(self.K)            # side * ||mean_paths Dm_t||
        self.ms_abs = np.zeros(self.K)              # side^2 * mean_paths ||Dm_t||^2

    def record(self, kk, side, n2, integ, mean_curve, w, truth_n, truth_int):
        n = np.sqrt(np.maximum(n2, 0.0))
        self.abs_[:, kk] = side * n
        self.rel[:, kk] = n / truth_n
        self.cnt_abs[:, kk] = side * np.abs(integ)
        self.cnt_rel[:, kk] = np.abs(integ) / truth_int
        self.bias_abs[kk] = side * np.sqrt(max(float((mean_curve * mean_curve) @ w), 0.0))
        self.ms_abs[kk] = side**2 * float(np.mean(n2))


def _summ(A, P):
    pm = A.mean(1)
    return float(pm.mean()), float(pm.std(ddof=1) / np.sqrt(P))


def accumulate_excitation(E, kern, paths, split_idx, prev, kk, nf, s_tail):
    """Add the block-kk events of every path to the running excitation E[:, nf:] (exact kernel sums
    at grid points; pre-day events older than FAR_LAG through far_excitation)."""
    for i, r in enumerate(paths):
        j1 = split_idx[i][kk]
        rb = r[prev[i]:j1]
        prev[i] = j1
        if kk == 0 and rb.size and rb[0] < -FAR_LAG:
            jfar = np.searchsorted(rb, -FAR_LAG)
            E[i, nf:] += far_excitation(kern, rb[:jfar], s_tail)
            rb = rb[jfar:]
        for c0 in range(0, rb.size, 1024):
            E[i, nf:] += kern.g(s_tail[None, :] - rb[c0:c0 + 1024, None]).sum(0)


def _simulate_with_counts(kern, regime, mu, B, n_paths, seed_entropy):
    mu_proc = mu if regime == "directional" else 2.0 * mu
    ss = np.random.SeedSequence(seed_entropy)
    rng = np.random.default_rng(ss)
    paths = simulate_cluster(mu_proc, kern, B, n_paths, rng)
    # side labels (common-mode): drawn 50/50 AFTER the cluster simulation; they do not enter the
    # per-side forecast (Phi symmetric) and are used only for the per-side count check.
    rng_side = np.random.default_rng(ss.spawn(1)[0])
    if regime == "common-mode":
        counts_side = np.array([np.sum(rng_side.random(np.sum(r >= 0)) < 0.5) for r in paths], float)
    else:
        counts_side = np.array([np.sum(r >= 0) for r in paths], float)
    counts_proc = np.array([np.sum(r >= 0) for r in paths], float)
    n_pre = np.array([np.sum(r < 0) for r in paths], float)
    return paths, mu_proc, counts_side, counts_proc, n_pre


def expected_day_count(mu, res, B, h_eval=H):
    """mu * int_0^T (1 + Psi(s + B)) ds (expected in-day requests per side, fresh start at -B)."""
    if B == 0:
        return float(mu * res.int1Psi_R)
    nB, nT = int(round(B / h_eval)), int(round(T / h_eval))
    return float(mu * np.sum(trap_weights(nT + 1, h_eval) * (1 + res.Psi_R[nB: nB + nT + 1])))


def calibrate_mu_B(res, B, h_eval=H):
    """mu_B = 400 / int_0^T (1 + Psi(s + B)) ds: expected in-day count per side = 400 at burn-in B."""
    return TARGET_SIDE_COUNT / expected_day_count(1.0, res, B, h_eval)


def run_cell_mc(kern, regime, mu, B, n_paths, seed_entropy, lifts: dict, mm_mu=None, h_eval=H,
                extra_plain=False, full_profile=True):
    """Monte Carlo of the forecast error for one cell.

    lifts: {lift_name: {p: ExpSum}}.  mm_mu: {(lift_name, p): mu_hat (per side)} -> adds the
    supplementary MEAN-MATCHED variant '<lift>_mm' (same lifted kernel and history, baseline mu_hat):
    Dm_mm = Dm + (mu_hat_proc - mu_proc)(1 + Psi^(u)), evaluated exactly from the same Dm.
    The true forecast is Richardson-extrapolated from steps (h_eval, h_eval/2); if extra_plain,
    the plain-trapezoid truth at h_eval is evaluated as well (base lifts and p0 only).
    """
    side = 1.0 if regime == "directional" else 0.5
    t_sim = time.time()
    paths, mu_proc, counts_side, counts_proc, n_pre = _simulate_with_counts(kern, regime, mu, B, n_paths, seed_entropy)
    t_sim = time.time() - t_sim
    mm_mu = mm_mu or {}

    P, K = n_paths, len(DEC_K)
    hf = h_eval / 2
    Nf = int(round(T / hf))
    s_f = np.arange(Nf + 1) * hf
    res = make_resolvent(kern.g, h_eval, Tend=T + B)
    psi_c, psi_f, Psi_R = res.psi_c, res.psi_f, res.Psi_R
    step_f = int(round(DT_DEC / hf))
    step_c = int(round(DT_DEC / h_eval))

    tk_arr = np.array(DEC_K) * DT_DEC
    rate_set = sorted({float(x) for L in lifts.values() for es in L.values() for x in es.x_all})
    Xcache = decision_filters(paths, rate_set)
    Xl = {ln: {p: np.stack([Xcache[float(x)] for x in es.x_all], axis=-1) for p, es in L.items()}
          for ln, L in lifts.items()}

    Nc = int(round(T / h_eval))
    u_full = np.arange(Nc + 1) * h_eval
    curves = {}
    for ln, L in lifts.items():
        curves[ln] = {}
        for p, es in L.items():
            one_psi = 1.0 + es.Psi(u_full)
            curves[ln][p] = (mu_proc * one_psi, np.exp(np.outer(es.lam, u_full)), one_psi)

    base_names = [(ln, p) for ln, L in lifts.items() for p in L]
    mm_names = [(ln + "_mm", p) for (ln, p) in base_names if (ln, p) in mm_mu]
    names = base_names + mm_names + [("p0_nhpp", 0), ("p0_baseline", 0)]
    acc = {nm: Acc(P, K) for nm in names}
    acc_plain = {nm: Acc(P, K) for nm in base_names + [("p0_nhpp", 0), ("p0_baseline", 0)]} if extra_plain else None
    truth_norm = np.zeros((P, K))
    truth_mean_norm = np.zeros(K)
    truth_fluct = np.zeros(K)

    E = np.zeros((P, Nf + 1))
    split_idx = [np.searchsorted(r, tk_arr, side="right") for r in paths]
    prev = [0] * P
    t_fc = time.time()
    for kk, k in enumerate(DEC_K):
        nf = k * step_f
        accumulate_excitation(E, kern, paths, split_idx, prev, kk, nf, s_f[nf:])
        Zf = mu_proc + E[:, nf:]
        m_c = volterra_forecast(Zf[:, ::2], psi_c, h_eval)
        m_f = volterra_forecast(Zf, psi_f, hf)
        m = (4.0 * m_f[:, ::2] - m_c) / 3.0
        L = m.shape[1]
        w = trap_weights(L, h_eval)
        m2 = (m * m) @ w
        tn = np.sqrt(m2)
        tint = m @ w
        mmean = m.mean(0)
        truth_norm[:, kk] = side * tn
        truth_mean_norm[kk] = side * np.sqrt((mmean * mmean) @ w)
        truth_fluct[kk] = side * np.sqrt(max(float(m2.mean() - (mmean * mmean) @ w), 0.0))
        if extra_plain:
            m2c = (m_c * m_c) @ w
            tn_c, tint_c = np.sqrt(m2c), m_c @ w
        nc = k * step_c
        for nm in base_names + [("p0_nhpp", 0), ("p0_baseline", 0)]:
            ln, p = nm
            if ln == "p0_nhpp":
                mh = np.broadcast_to(nhpp_curve(mu_proc, Psi_R, k * DT_DEC, B, h_eval, L), m.shape)
            elif ln == "p0_baseline":
                mh = np.full(m.shape, mu_proc)
            else:
                es = lifts[ln][p]
                base, Em, one_psi = curves[ln][p]
                D = es.coeffs(Xl[ln][p][:, kk, :])
                mh = D @ Em[:, :L]
                mh += base[None, :L]
            dm = mh - m
            n2 = (dm * dm) @ w
            integ = dm @ w
            mean_dm = dm.mean(0)
            acc[nm].record(kk, side, n2, integ, mean_dm, w, tn, tint)
            if (ln, p) in mm_mu:
                phi = one_psi[:L]
                delta = mm_mu[(ln, p)] * (1.0 if regime == "directional" else 2.0) - mu_proc
                wphi = w * phi
                n2mm = n2 + 2 * delta * (dm @ wphi) + delta**2 * float(phi @ wphi)
                acc[(ln + "_mm", p)].record(kk, side, n2mm, integ + delta * float(phi @ w), mean_dm + delta * phi,
                                            w, tn, tint)
            if extra_plain:
                dmc = mh - m_c
                acc_plain[nm].record(kk, side, (dmc * dmc) @ w, dmc @ w, dmc.mean(0), w, tn_c, tint_c)
    t_fc = time.time() - t_fc

    def summarise(accd):
        out = {}
        for nm, a in accd.items():
            ma, sa = _summ(a.abs_, P)
            mr, sr = _summ(a.rel, P)
            ca, csa = _summ(a.cnt_abs, P)
            cr, csr = _summ(a.cnt_rel, P)
            fluct = np.sqrt(np.maximum(a.ms_abs - a.bias_abs**2, 0.0))
            prof = {}
            for lab, k in PROFILE_K.items():
                kk = DEC_K.index(k)
                prof[lab] = {
                    "abs_mean": float(a.abs_[:, kk].mean()), "abs_se": float(a.abs_[:, kk].std(ddof=1) / np.sqrt(P)),
                    "rel_mean": float(a.rel[:, kk].mean()), "rel_se": float(a.rel[:, kk].std(ddof=1) / np.sqrt(P)),
                    "bias_abs": float(a.bias_abs[kk]), "fluct_abs": float(fluct[kk]),
                    "bias_rel": float(a.bias_abs[kk] / truth_mean_norm[kk]),
                    "fluct_rel": float(fluct[kk] / truth_mean_norm[kk]),
                    "bias_noise_floor_abs": float(fluct[kk] / np.sqrt(P)),
                    "count_rel_mean": float(a.cnt_rel[:, kk].mean())}
            o = {"mean_abs": ma, "se_abs": sa, "mean_rel": mr, "se_rel": sr,
                 "count_abs_mean": ca, "count_abs_se": csa, "count_rel_mean": cr, "count_rel_se": csr,
                 "bias_rel_tavg": float(np.mean(a.bias_abs / truth_mean_norm)),
                 "fluct_rel_tavg": float(np.mean(fluct / truth_mean_norm)),
                 "rms_rel_tavg": float(np.mean(np.sqrt(a.ms_abs) / truth_mean_norm)),
                 "N3_fluct_over_truth_fluct_tavg": float(np.mean(fluct / truth_fluct)),
                 "profile": prof,
                 "_pm_abs": a.abs_.mean(1), "_fluct": fluct}
            if full_profile:
                o["profile_all_t"] = {
                    "t": [k * DT_DEC for k in DEC_K],
                    "abs_mean": a.abs_.mean(0), "abs_se": a.abs_.std(0, ddof=1) / np.sqrt(P),
                    "rel_mean": a.rel.mean(0), "rel_se": a.rel.std(0, ddof=1) / np.sqrt(P),
                    "bias_abs": a.bias_abs, "fluct_abs": fluct,
                    "bias_rel": a.bias_abs / truth_mean_norm, "fluct_rel": fluct / truth_mean_norm,
                    "count_rel_mean": a.cnt_rel.mean(0)}
            out[nm] = o
        # N2: ||Dm_p|| relative to ||Dm_{p0_nhpp}|| (ratio of means; paired delta-method SE)
        ref = out[("p0_nhpp", 0)]
        for nm, o in out.items():
            r = o["mean_abs"] / ref["mean_abs"]
            o["N2_ratio_to_nhpp"] = r
            o["N2_se"] = float(np.std(o["_pm_abs"] - r * ref["_pm_abs"], ddof=1) / np.sqrt(P) / ref["mean_abs"])
        return out

    sim = {"paths": P, "seed_entropy": list(seed_entropy), "mu": mu, "mu_process": mu_proc,
           "mean_count_side": float(counts_side.mean()),
           "se_count_side": float(counts_side.std(ddof=1) / np.sqrt(P)),
           "mean_count_process": float(counts_proc.mean()),
           "expected_count_side": expected_day_count(mu, res, B, h_eval),
           "mean_pre_day_events": float(n_pre.mean()),
           "truth_norm_mean": float(truth_norm.mean()),
           "truth_fluct_tavg": float(truth_fluct.mean()), "truth_mean_norm_tavg": float(truth_mean_norm.mean()),
           "runtime_sim_s": t_sim, "runtime_forecast_s": t_fc}
    sim["z_count_vs_expected"] = float((sim["mean_count_side"] - sim["expected_count_side"]) / sim["se_count_side"])
    out = {"sim": sim, "forecast": summarise(acc), "resolvent": res}
    if extra_plain:
        out["forecast_plain_trapezoid"] = summarise(acc_plain)
    return out


def numerical_floor(kern, regime, mu, B, n_paths, seed_entropy, h_eval=H):
    """Per-cell numerical floor of the TRUE forecast: E||m_R(h) - m_R(h/2)|| on the h-grid, where
    m_R(h) = Richardson(h, h/2) (production) and m_R(h/2) = Richardson(h/2, h/4) (16x more accurate),
    on independent histories (n_paths).  Lifts are exact, so this bounds the numerical error of Dm."""
    side = 1.0 if regime == "directional" else 0.5
    paths, mu_proc, *_ = _simulate_with_counts(kern, regime, mu, B, n_paths, seed_entropy)
    h4 = h_eval / 4
    N4 = int(round(T / h4))
    s4 = np.arange(N4 + 1) * h4
    res = make_resolvent(kern.g, h_eval, Tend=T)
    psi1, psi2 = res.psi_c, res.psi_f
    psi4 = volterra_resolvent(kern.g(s4), h4)
    P, K = n_paths, len(DEC_K)
    tk_arr = np.array(DEC_K) * DT_DEC
    E = np.zeros((P, N4 + 1))
    split_idx = [np.searchsorted(r, tk_arr, side="right") for r in paths]
    prev = [0] * P
    d_R, d_plain, nrm = np.zeros((P, K)), np.zeros((P, K)), np.zeros((P, K))
    step4 = int(round(DT_DEC / h4))
    for kk, k in enumerate(DEC_K):
        n4 = k * step4
        accumulate_excitation(E, kern, paths, split_idx, prev, kk, n4, s4[n4:])
        Z4 = mu_proc + E[:, n4:]
        m4 = volterra_forecast(Z4, psi4, h4)
        m2 = volterra_forecast(Z4[:, ::2], psi2, h_eval / 2)
        m1 = volterra_forecast(Z4[:, ::4], psi1, h_eval)
        R1 = (4 * m2[:, ::2] - m1) / 3
        R2 = ((4 * m4[:, ::2] - m2) / 3)[:, ::2]
        d_R[:, kk] = side * l2_trap(R1 - R2, h_eval)
        d_plain[:, kk] = side * l2_trap(m1 - R2, h_eval)
        nrm[:, kk] = side * l2_trap(R2, h_eval)
    fr, fse = _summ(d_R, P)
    return {"paths": P, "seed_entropy": list(seed_entropy),
            "floor_abs": fr, "floor_abs_se": fse, "floor_rel_to_mean_norm": fr / float(nrm.mean()),
            "plain_trapezoid_error_abs": _summ(d_plain, P)[0],
            "definition": "mean over (paths, t) of side*||m_R(h) - m_R(h/2)||_L2[0,T-t] (truth only)"}


# ----------------------------------------------------------------------------------------------
# Lai, Gao & Li (2023) Table 2
# ----------------------------------------------------------------------------------------------


def lai_rho(alpha, beta, delta):
    return alpha * delta ** (1 - beta) / (beta - 1)


def lai_tail(beta, delta, D=1.0):
    return (delta / (D + delta)) ** (beta - 1)


def load_lai(path):
    import csv
    with open(path, newline="") as f:
        rows = [r for r in csv.DictReader(line for line in f if not line.startswith("#"))]
    for r in rows:
        for k in ("alpha", "beta", "delta"):
            r[k] = float(r[k])
    return rows


def lai_table2_check(path):
    rows = load_lai(path)
    out_rows = []
    for r in rows:
        rho = lai_rho(r["alpha"], r["beta"], r["delta"])
        out_rows.append({"underlying": r["underlying"], "K_S": r["K_S"], "TTM_days": r["TTM_days"], "type": r["type"],
                         "alpha": r["alpha"], "beta": r["beta"], "delta": r["delta"],
                         "b": r["beta"], "t0": r["delta"], "L1_norm_rho": rho,
                         "tail_mass_beyond_1": lai_tail(r["beta"], r["delta"]),
                         "supercritical": bool(rho > 1)})
    hi = [o for o in out_rows if o["beta"] >= 1.45]
    lo = [o for o in out_rows if 1.07 <= o["beta"] <= 1.2]
    mid = [o for o in out_rows if 1.2 < o["beta"] < 1.45]
    a1 = all(0.004 <= o["tail_mass_beyond_1"] <= 0.03 for o in hi)
    a2 = all(0.12 <= o["tail_mass_beyond_1"] <= 0.55 for o in lo)
    def rng_(L):
        v = [o["tail_mass_beyond_1"] for o in L]
        return [min(v), max(v)] if v else None
    anchor = next(o for o in out_rows if o["underlying"] == "AAPL" and o["K_S"] == "(1.01,1.02]"
                  and o["TTM_days"] == "0-5" and o["type"] == "Buy")
    nearest_rho = min(RHO_GRID, key=lambda v: abs(v - anchor["L1_norm_rho"]))
    nearest_b = min(B_GRID, key=lambda v: abs(v - anchor["b"]))
    return {
        "source": "Lai, Gao & Li 2023, Quant. Finance 23(5), Table 2, p. 782 (PDF physical page 7); averages of daily estimates",
        "mapping": "Lai g(t)=alpha/(t+delta)^beta -> b=beta, t0=delta, rho=alpha*delta^(1-beta)/(beta-1); tail mass beyond "
                   "Delta=1 Lai time unit = (delta/(1+delta))^(beta-1); Lai's time unit is unstated (plan risk list)",
        "rows": out_rows,
        "n_rows": len(out_rows), "n_supercritical_L1_gt_1": int(sum(o["supercritical"] for o in out_rows)),
        "claim_a": {
            "text": "tail mass is 0.4-3% for beta >= 1.45 and 12-55% for beta ~ 1.07-1.2 (design doc)",
            "part1_beta_ge_1.45": {"n_rows": len(hi), "tail_range": rng_(hi), "all_within_0.4_3pct": a1,
                                    "rows_outside": [f'{o["underlying"]} {o["K_S"]} {o["TTM_days"]} {o["type"]}: '
                                                     f'{o["tail_mass_beyond_1"]:.4f}' for o in hi
                                                     if not (0.004 <= o["tail_mass_beyond_1"] <= 0.03)]},
            "part2_beta_1.07_1.2": {"n_rows": len(lo), "tail_range": rng_(lo), "all_within_12_55pct": a2,
                                     "rows_outside": [f'{o["underlying"]} {o["K_S"]} {o["TTM_days"]} {o["type"]}: '
                                                      f'{o["tail_mass_beyond_1"]:.4f}' for o in lo
                                                      if not (0.12 <= o["tail_mass_beyond_1"] <= 0.55)]},
            "rows_with_1.2_lt_beta_lt_1.45_not_covered": {"n_rows": len(mid), "tail_range": rng_(mid)},
            "verdict": bool(a1 and a2)},
        "claim_b": {
            "text": "AAPL (1.01,1.02] 0-5 buy: b ~ 1.12, rho ~ 0.59 -> cell b = 1.15, rho = 0.5 (plan Data Sources)",
            "b": anchor["b"], "rho_computed": anchor["L1_norm_rho"], "rho_claimed": 0.59,
            "rho_claim_true_within_0.01": bool(abs(anchor["L1_norm_rho"] - 0.59) < 0.01),
            "nearest_cell_b": nearest_b, "nearest_cell_rho": nearest_rho,
            "cell_claim_true": bool(nearest_b == 1.15 and nearest_rho == 0.5),
            "verdict": bool(abs(anchor["L1_norm_rho"] - 0.59) < 0.01 and nearest_rho == 0.5)},
        "informational_only": True}


# ----------------------------------------------------------------------------------------------
# H2 direction check (informational screen proxy)
# ----------------------------------------------------------------------------------------------


NORMALISATIONS = {
    # name: (summary key, include p0_nhpp as the p = 0 entry, description)
    "N1_rel_to_norm_m": ("mean_rel", True, "mean over (paths,t) of ||Dm_t|| / ||m_t||  [pre-registered dispatch proxy]"),
    "N1_lifts_only": ("mean_rel", False, "as N1, p = 0 excluded"),
    "N2_ratio_to_nhpp_error": ("N2_ratio_to_nhpp", True,
                               "mean ||Dm_p|| / mean ||Dm_{p0_nhpp}||: share of the history's information the lift "
                               "loses (p0 = 1 by definition)"),
    "N3_fluct_only": ("N3_fluct_over_truth_fluct_tavg", True,
                      "t-average of fluct part sqrt(E||Dm_t - E Dm_t||^2) / sqrt(E||m_t - E m_t||^2) (bias removed; "
                      "the denominator equals the fluctuation part of p0_nhpp, so p0 = 1)"),
    "C_count_error_rel": ("count_rel_mean", True, "mean over (paths,t) of |int_0^{T-t} Dm_t du| / int_0^{T-t} m_t du"),
}


def _num(v):
    return 9 if v == ">8" else v


def _classify(hard, easy_vals):
    h, e = _num(hard), [_num(v) for v in easy_vals]
    if all(v == h for v in e):
        return "flat_unresolved_all_gt8" if h == 9 else "flat"
    if h > max(e):
        return "consistent_strict"
    if h >= max(e):
        return "consistent_weak"
    if h < min(e):
        return "reversed_strict"
    if h <= min(e):
        return "reversed_weak"
    return "mixed"


def _is_easy(b, rho):
    return b >= 1.4 and rho <= 0.8


def h2_proxy_run(run_forecasts, lift_names):
    """run_forecasts: {(b, rho, regime): forecast dict keyed by (lift, p)}."""
    out = {}
    for nname, (key, incl0, _) in NORMALISATIONS.items():
        out[nname] = {}
        for ln in lift_names:
            out[nname][ln] = {}
            for regime in REGIMES:
                out[nname][ln][regime] = {}
                for tau in TAU_GRID:
                    table = {}
                    for (b, rho, rg), f in run_forecasts.items():
                        if rg != regime:
                            continue
                        vals = {p: f[(ln, p)][key] for p in P_LIFTS}
                        if incl0:
                            vals[0] = f[("p0_nhpp", 0)][key]
                        ps = [p for p in sorted(vals) if vals[p] <= tau]
                        table[f"b={b},rho={rho}"] = ps[0] if ps else ">8"
                    easy = [v for k, v in table.items()
                            if _is_easy(float(k.split(",")[0][2:]), float(k.split(",")[1][4:]))]
                    hard = table["b=1.15,rho=0.95"]
                    out[nname][ln][regime][f"tau={tau}"] = {
                        "p_star_screen": table, "class": _classify(hard, easy),
                        "direction_consistent_hard_ge_all_easy": bool(_num(hard) >= max(_num(v) for v in easy)),
                        "pattern_easy_le2_and_hard_ge4": bool(all(_num(v) <= 2 for v in easy) and _num(hard) >= 4)}
    return out


def h2_direction_check(runs, lift_names):
    """runs: {run_name: {(b, rho, regime): forecast}}."""
    res = {rn: h2_proxy_run(rf, lift_names) for rn, rf in runs.items()}
    matrix = {}
    for ln in lift_names:
        matrix[ln] = {}
        for rg in REGIMES:
            matrix[ln][rg] = {}
            for tau in TAU_GRID:
                matrix[ln][rg][f"tau={tau}"] = {nn: {rn: res[rn][nn][ln][rg][f"tau={tau}"]["class"] for rn in runs}
                                               for nn in NORMALISATIONS}
    counts = {}
    for rn in runs:
        for nn in NORMALISATIONS:
            cl = [res[rn][nn][ln][rg][f"tau={tau}"]["class"] for ln in lift_names for rg in REGIMES for tau in TAU_GRID]
            counts[f"{rn} | {nn}"] = {c: cl.count(c) for c in sorted(set(cl))}
    pattern_any = {rn: {nn: any(res[rn][nn][ln][rg][f"tau={tau}"]["pattern_easy_le2_and_hard_ge4"]
                                for ln in lift_names for rg in REGIMES for tau in TAU_GRID) for nn in NORMALISATIONS}
                   for rn in runs}
    statements = []
    for ln in ("nnls_L2", "gauss_composite"):
        for rg in REGIMES:
            m = matrix[ln][rg]["tau=0.05"]
            for cls in ("consistent_strict", "consistent_weak", "reversed_strict", "reversed_weak", "flat", "mixed",
                        "flat_unresolved_all_gt8"):
                where = [f"{nn} @ {rn}" for nn in NORMALISATIONS for rn in runs if m[nn][rn] == cls]
                if where:
                    statements.append(f"{ln}, {rg}, tau=0.05: {cls} under " + "; ".join(where))
    return {"label": "informational, screen proxy, not a test of H2",
            "definition": "p*_screen(tau) = min{p in {0,1,2,3,4,6,8}: metric <= tau}; '>8' if never reached; "
                          "classes (hard cell vs the four easy cells): flat = equal to every easy cell "
                          "(flat_unresolved_all_gt8 if all are '>8'); consistent_strict = hard > every easy; "
                          "consistent_weak = hard >= every easy with a tie; reversed_strict = hard < every easy; "
                          "reversed_weak = hard <= every easy with a tie; mixed = otherwise; '>8' counted as 9",
            "pattern_hits": [f"{rn} | {nn} | {ln} | {rg} | tau={tau}" for rn in runs for nn in NORMALISATIONS
                             for ln in lift_names for rg in REGIMES for tau in TAU_GRID
                             if res[rn][nn][ln][rg][f"tau={tau}"]["pattern_easy_le2_and_hard_ge4"]],
            "easy_cells": "b in {1.4, 1.8} x rho in {0.5, 0.8}", "hard_cell": "b = 1.15, rho = 0.95",
            "normalisations": {k: v[2] for k, v in NORMALISATIONS.items()},
            "runs": list(runs), "lifts": lift_names,
            "conditional_summary": statements, "class_counts_by_run_and_normalisation": counts,
            "pattern_easy_le2_and_hard_ge4_appears": pattern_any,
            "matrix_lift_regime_tau_normalisation_run": matrix, "results_by_run": res}


def _r(x):
    x = float(x)
    if not np.isfinite(x):
        return str(x)
    return float(f"{x:.8g}")


def _jsonable(o):
    if isinstance(o, dict):
        return {str(k): _jsonable(v) for k, v in o.items() if not str(k).startswith("_")}
    if isinstance(o, (list, tuple)):
        return [_jsonable(v) for v in o]
    if isinstance(o, (np.floating, float)) and not isinstance(o, bool):
        return _r(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.ndarray):
        return _jsonable(o.tolist())
    return o


def git_commit():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=here, text=True).strip()
        dirty = subprocess.check_output(["git", "status", "--porcelain", "--", "."], cwd=here, text=True).strip()
        return head, bool(dirty)
    except Exception:  # pragma: no cover
        return "unknown", None


def cell_seed(ci, B):
    return [BASE_SEED, ci, int(B)]


def lifts_for_cell(templates, kern):
    L = {}
    for ln in LIFT_NAMES:
        L[ln] = {}
        for p in P_LIFTS:
            x, c = scale_lift(templates[kern.b][ln][p], kern.rho)
            L[ln][p] = ExpSum(c, x)
    return L


def _sha256(path):
    import hashlib
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def mm_mus(L, B_cal):
    return {(ln, p): es.mean_matched_mu(B_cal) for ln, d in L.items() for p, es in d.items()}


COMPACT_KEYS = ["mean_abs", "se_abs", "mean_rel", "se_rel", "N2_ratio_to_nhpp", "N2_se",
                "N3_fluct_over_truth_fluct_tavg", "count_rel_mean", "count_rel_se", "bias_rel_tavg", "fluct_rel_tavg",
                "profile"]


def _flag(f, floor):
    return None if floor is None else bool(f["mean_abs"] < 10.0 * floor["floor_abs"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--paths", type=int, default=1000, help="MC paths per cell, B = 0")
    ap.add_argument("--paths-b1", type=int, default=400, help="MC paths per cell, B = 1T sensitivity")
    ap.add_argument("--paths-b10", type=int, default=100, help="MC paths per cell, B = 10T sensitivity (same mu)")
    ap.add_argument("--paths-b10-recal", type=int, default=200, help="MC paths per cell, B = 10T recalibrated mu")
    ap.add_argument("--paths-conv", type=int, default=1000, help="MC paths for the convergence check")
    ap.add_argument("--paths-floor", type=int, default=100, help="MC paths for the per-cell numerical floor (B = 0)")
    ap.add_argument("--paths-floor-burn", type=int, default=50, help="MC paths for the floor (recalibrated burn-in)")
    ap.add_argument("--budget-s", type=float, default=1500.0, help="runtime guard for the B = 10T runs")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "screen.json"))
    ap.add_argument("--quick", action="store_true", help="smoke run (few paths, 2 cells)")
    args = ap.parse_args(argv)
    t_start = time.time()
    log = lambda *a: print(*a, flush=True)
    here = os.path.dirname(os.path.abspath(__file__))
    deviations, timings = [], {}

    log("building lift templates ...")
    templates = {b: build_lift_templates(b, log) for b in B_GRID}
    timings["lifts"] = time.time() - t_start

    cell_list = [(b, rho, rg) for b in B_GRID for rho in RHO_GRID for rg in REGIMES]
    if args.quick:
        cell_list = [(1.15, 0.95, "directional"), (1.8, 0.5, "directional"), (1.4, 0.5, "directional"),
                     (1.15, 0.95, "common-mode")]
        args.paths, args.paths_b1, args.paths_b10, args.paths_b10_recal = 60, 30, 20, 20
        args.paths_conv, args.paths_floor, args.paths_floor_burn = 40, 20, 10
    runs = {}

    # ---------------- primary: B = 0 ----------------
    t0 = time.time()
    cells, runs["B=0"] = [], {}
    for ci, (b, rho, rg) in enumerate(cell_list):
        tc = time.time()
        kern = PowerLawKernel(b, rho)
        res0 = make_resolvent(kern.g, H)
        mu = calibrate_mu(res0)
        L = lifts_for_cell(templates, kern)
        mm = mm_mus(L, 0.0)
        mc = run_cell_mc(kern, rg, mu, 0.0, args.paths, cell_seed(ci, 0), L, mm_mu=mm)
        floor = numerical_floor(kern, rg, mu, 0.0, args.paths_floor, [BASE_SEED, ci, 0, 2])
        runs["B=0"][(b, rho, rg)] = mc["forecast"]
        res = mc["resolvent"]
        entry = {"b": b, "rho": rho, "regime": rg, "mu": mu, "mu_process": mu if rg == "directional" else 2 * mu,
                 "expected_count": TARGET_SIDE_COUNT, "expected_count_side": TARGET_SIDE_COUNT,
                 "expected_count_check_plain_trapezoid": float(mu * res0.int1Psi_c),
                 "int_0^T(1+Psi)_richardson": res0.int1Psi_R, "int_0^T(1+Psi)_plain_trapezoid": res0.int1Psi_c,
                 "mass_in_T": kern.mass_on(T), "mass_beyond_T": kern.tail_fraction(T),
                 "mass_beyond_T_abs": kern.rho * kern.tail_fraction(T),
                 "tail_mass_by_Delta": {k: {"fraction": kern.tail_fraction(D), "abs": kern.rho * kern.tail_fraction(D),
                                            "reference_Delta": k == REF_DELTA,
                                            "note": "T/400 = mean inter-request time per side; provisional until Task 4"
                                            if k == REF_DELTA else ""} for k, D in DELTAS.items()},
                 "simulation": mc["sim"], "numerical_floor": floor,
                 "numerical_floor_upper_bound_nnls_p8_mean_abs": mc["forecast"][("nnls_L2", 8)]["mean_abs"],
                 "lifts": {}}
        for ln in LIFT_NAMES:
            entry["lifts"][ln] = {}
            entry["lifts"][ln + "_mean_matched"] = {}
            for p in P_LIFTS:
                km = kernel_metrics(kern, L[ln][p], res)
                f = mc["forecast"][(ln, p)]
                fm = mc["forecast"][(ln + "_mm", p)]
                entry["lifts"][ln][f"p={p}"] = {"kernel": km, "lift_info": templates[b][ln][p]["info"], "forecast": f,
                                                "below_numerical_resolution": _flag(f, floor)}
                entry["lifts"][ln + "_mean_matched"][f"p={p}"] = {
                    "label": "supplementary mean-matched variant: same lifted kernel and history, baseline mu_hat with "
                             "mu_hat (T + int_0^T Psi^) = 400",
                    "mu_hat": mm[(ln, p)], "mu_hat_over_mu": mm[(ln, p)] / mu, "kernel": f"same as {ln} p={p}",
                    "forecast": fm, "below_numerical_resolution": _flag(fm, floor)}
        kz = kernel_metrics_zero(kern, res)
        entry["lifts"]["p0_nhpp"] = {"kernel": kz, "description": "m^_t(u) = E[lambda_{t+u}] = mu(1+Psi(t+u)) "
                                     "(unconditional mean curve, NHPP-matched forecast; THE p = 0 entry)",
                                     "forecast": mc["forecast"][("p0_nhpp", 0)]}
        entry["lifts"]["p0_baseline"] = {"kernel": kz, "description": "m^ = mu (supplementary)",
                                         "forecast": mc["forecast"][("p0_baseline", 0)]}
        cells.append(entry)
        log(f"cell {ci + 1}/{len(cell_list)} b={b} rho={rho} {rg}: mu={mu:.3f} count={mc['sim']['mean_count_side']:.1f}"
            f"+-{mc['sim']['se_count_side']:.1f} floor={floor['floor_rel_to_mean_norm']:.1e} ({time.time() - tc:.1f}s)")
    timings["B0_cells_incl_floors"] = time.time() - t0

    # ---------------- convergence check ----------------
    t0 = time.time()
    log("convergence check ...")
    conv = {"design": "same histories (same seed, same mu) re-evaluated with h_eval = h/2 (Richardson from h/2, h/4) "
                      "vs production h_eval = h (Richardson from h, h/2); plain trapezoid at h vs h/2 also reported",
            "target_rel_change": 0.02,
            "target_source": "the 2% target comes from the Task 3 dispatch, NOT from the plan; the plan's own criterion "
                             "(Stop Criterion) is a < 10% change of the exact anchor's regret under 2x grid refinement",
            "p_checked": [1, 4, 8], "cells": []}
    for (b, rho, rg) in [(1.15, 0.95, "directional"), (1.8, 0.5, "directional")]:
        kern = PowerLawKernel(b, rho)
        mu = calibrate_mu(make_resolvent(kern.g, H))
        Lall = lifts_for_cell(templates, kern)
        L = {ln: {p: Lall[ln][p] for p in (1, 4, 8)} for ln in LIFT_NAMES}
        ci = cell_list.index((b, rho, rg)) if (b, rho, rg) in cell_list else 999
        r1 = run_cell_mc(kern, rg, mu, 0.0, args.paths_conv, cell_seed(ci, 0), L, h_eval=H, extra_plain=True,
                         full_profile=False)
        r2 = run_cell_mc(kern, rg, mu, 0.0, args.paths_conv, cell_seed(ci, 0), L, h_eval=H / 2, extra_plain=True,
                         full_profile=False)
        ent = {"b": b, "rho": rho, "regime": rg, "paths": args.paths_conv, "entries": {}}
        for ln in LIFT_NAMES + ["p0_nhpp"]:
            for p in ((1, 4, 8) if ln != "p0_nhpp" else (0,)):
                a1, a2 = r1["forecast"][(ln, p)], r2["forecast"][(ln, p)]
                q1, q2 = r1["forecast_plain_trapezoid"][(ln, p)], r2["forecast_plain_trapezoid"][(ln, p)]
                ent["entries"][f"{ln} p={p}"] = {
                    "richardson_h": a1["mean_abs"], "richardson_h/2": a2["mean_abs"],
                    "rel_change_richardson": abs(a2["mean_abs"] - a1["mean_abs"]) / a1["mean_abs"],
                    "plain_h": q1["mean_abs"], "plain_h/2": q2["mean_abs"],
                    "rel_change_plain": abs(q2["mean_abs"] - q1["mean_abs"]) / q1["mean_abs"],
                    "mean_rel_richardson_h": a1["mean_rel"], "mean_rel_richardson_h/2": a2["mean_rel"]}
        for pp in ((1, 4), (1, 4, 8)):
            tag = "p1_p4" if pp == (1, 4) else "p1_p4_p8"
            ks = [k for k in ent["entries"] if not k.startswith("p0") and int(k.split("p=")[1]) in pp]
            ent[f"max_rel_change_richardson_{tag}"] = max(ent["entries"][k]["rel_change_richardson"] for k in ks)
            ent[f"max_rel_change_plain_{tag}"] = max(ent["entries"][k]["rel_change_plain"] for k in ks)
        ent["plain_entries_over_target"] = {k: v["rel_change_plain"] for k, v in ent["entries"].items()
                                            if v["rel_change_plain"] >= 0.02}
        ent["pass_richardson"] = bool(ent["max_rel_change_richardson_p1_p4_p8"] < 0.02)
        ent["pass_plain"] = bool(ent["max_rel_change_plain_p1_p4"] < 0.02)
        conv["cells"].append(ent)
        log(f"  conv b={b} rho={rho}: richardson max change (p1,4,8) {ent['max_rel_change_richardson_p1_p4_p8']:.2e}, "
            f"plain (p1,4) {ent['max_rel_change_plain_p1_p4']:.4f}")
    conv["pass"] = all(c["pass_richardson"] for c in conv["cells"])
    timings["convergence"] = time.time() - t0

    # ---------------- burn-in sensitivity ----------------
    burn = {"design": "immigrants on [-B, T] (fresh start at -B); truth conditions on the full history since -B; "
                      "p0_nhpp uses mu(1+Psi(t+u+B)); independent histories (not CRN with B = 0). 'same_mu' runs keep "
                      "the B = 0 mu (as specified); 'recalibrated' runs (supplementary, review Q4) use "
                      "mu_B = 400 / int_0^T (1 + Psi(s + B)) ds so that the expected in-day count per side is 400.",
            "profile_storage": "burn-in runs store the profile at t = 0.25, 0.5, 0.75 only (B = 0 stores all 19 t)"}
    specs = [("B=1_same_mu", 1.0, False, args.paths_b1), ("B=1_recalibrated", 1.0, True, args.paths_b1),
             ("B=10_same_mu", 10.0, False, args.paths_b10), ("B=10_recalibrated", 10.0, True, args.paths_b10_recal)]
    for rn, B, recal, npaths in specs:
        t0 = time.time()
        log(f"burn-in {rn} ...")
        blk = {"B": B, "mu_convention": "recalibrated" if recal else "same_mu (B = 0 mu)", "paths": npaths,
               "cells": [], "skipped_cells": []}
        runs[rn] = {}
        t_last = None
        for ci, (b, rho, rg) in enumerate(cell_list):
            if B >= 10 and t_last is not None and time.time() - t_start + 1.5 * t_last > args.budget_s:
                blk["skipped_cells"].append(f"b={b}, rho={rho}, {rg}")
                continue
            tc = time.time()
            kern = PowerLawKernel(b, rho)
            resB = make_resolvent(kern.g, H, Tend=T + B)
            mu = calibrate_mu_B(resB, B) if recal else cells[ci]["mu"]
            L = lifts_for_cell(templates, kern)
            mm = mm_mus(L, B if recal else 0.0)
            seed = [BASE_SEED, ci, int(B), 1] if recal else cell_seed(ci, int(B))
            mc = run_cell_mc(kern, rg, mu, B, npaths, seed, L, mm_mu=mm, full_profile=False)
            floor = numerical_floor(kern, rg, mu, B, args.paths_floor_burn, [BASE_SEED, ci, int(B), 3]) if recal else None
            runs[rn][(b, rho, rg)] = mc["forecast"]
            ent = {"b": b, "rho": rho, "regime": rg, "mu": mu, "mu_over_mu_B0": mu / cells[ci]["mu"],
                   "simulation": mc["sim"], "numerical_floor": floor, "lifts": {}}
            for (ln, p), f in mc["forecast"].items():
                key = ln[:-3] + "_mean_matched" if ln.endswith("_mm") else ln
                e = {k: f[k] for k in COMPACT_KEYS}
                e["below_numerical_resolution"] = _flag(f, floor)
                ref = cells[ci]["lifts"][key][f"p={p}"]["forecast"] if key not in ("p0_nhpp", "p0_baseline") \
                    else cells[ci]["lifts"][key]["forecast"]
                e["delta_mean_rel_vs_B0"] = f["mean_rel"] - ref["mean_rel"]
                e["delta_se"] = float(np.hypot(f["se_rel"], ref["se_rel"]))
                if ln.endswith("_mm"):
                    e["mu_hat"] = mm[(ln[:-3], p)]
                ent["lifts"].setdefault(key, {})[f"p={p}"] = e
            blk["cells"].append(ent)
            t_last = time.time() - tc
            log(f"  {rn} cell {ci + 1}: mu={mu:.2f} pre-day {mc['sim']['mean_pre_day_events']:.0f}, "
                f"count {mc['sim']['mean_count_side']:.0f} (exp {mc['sim']['expected_count_side']:.0f}) ({t_last:.1f}s)")
        if blk["skipped_cells"]:
            deviations.append(f"{rn}: {len(blk['skipped_cells'])} of {len(cell_list)} cells skipped by the runtime "
                              f"guard ({args.budget_s:.0f}s)")
        burn[rn] = blk
        timings[rn] = time.time() - t0
    # keep the pre-registered keys
    burn["B=1"] = {"alias_of": "B=1_same_mu"}
    burn["B=10"] = {"alias_of": "B=10_same_mu"}

    # ---------------- Lai, H2 proxy, route comparison ----------------
    lai = lai_table2_check(os.path.join(here, "data", "lai2023_table2.csv"))
    lift_variants = LIFT_NAMES + [ln + "_mm" for ln in LIFT_NAMES]
    complete_runs = {rn: rf for rn, rf in runs.items() if len(rf) == len(cell_list)}
    h2 = h2_direction_check(complete_runs, lift_variants) if not args.quick else {"skipped": "quick run"}
    if not args.quick:
        # pre-registered dispatch proxy (N1, B = 0, p0 included) kept under its original keys
        h2["results"] = {ln: {rg: h2["results_by_run"]["B=0"]["N1_rel_to_norm_m"][ln][rg] for rg in REGIMES}
                         for ln in LIFT_NAMES}
    route = _route_comparison(templates)

    # ---------------- deviations / bookkeeping ----------------
    plain_pass = all(c["pass_plain"] for c in conv["cells"])
    if plain_pass:
        deviations.append("Discretisation: Richardson (h, h/2) kept for the TRUE forecast although the plain trapezoid "
                          "also met the dispatch's 2% target.")
    else:
        over = {f"b={c['b']},rho={c['rho']}": c["plain_entries_over_target"] for c in conv["cells"]}
        deviations.append("Discretisation: the plain trapezoid scheme at h = t0/10 FAILED the dispatch's 2% convergence "
                          "target (the plan's own criterion is < 10% on regret, Stop Criterion) for these entries: "
                          f"{json.dumps(_jsonable(over))}; the TRUE forecast is therefore Richardson-extrapolated from "
                          "(h, h/2) -- the 'refine' branch the dispatch allowed. The evaluation grid is still h = t0/10.")
    deviations.append(
        "Lifted forecasts m^ are computed by the exact exponential-filter route (closed-form linear ODE) instead of "
        "trapezoid on the grid. Check at production h on a fixed history (route_comparison_production_h): the "
        f"Richardson grid route differs from the exact route by at most {route['max_rel_L2_diff_richardson_route']:.1e} "
        f"(relative L2) and the plain trapezoid route by up to {route['max_rel_L2_diff_plain_route']:.1e}.")
    n_peff = sum(1 for c in cells for p in P_LIFTS if c["lifts"]["mass_preserving"][f"p={p}"]["kernel"]["p_effective"] < p)
    peff8 = sorted({c["lifts"]["mass_preserving"]["p=8"]["kernel"]["p_effective"] for c in cells})
    deviations.append(f"Lift (iii) mass_preserving: the exact QP leaves some weights at zero, so p_effective < p in "
                      f"{n_peff} of {len(cells) * len(P_LIFTS)} cell x p entries (p = 8 -> p_effective in {peff8}); "
                      "the lift is reported at its nominal p.")
    deviations += DEVIATIONS
    if not conv["pass"]:
        deviations.append("convergence check failed even with Richardson extrapolation (see convergence_check)")
    head, dirty = git_commit()
    timings["total"] = time.time() - t_start
    out = {
        "task": "lai2023-gaps-and-memory Task 3 (Tier 0)", "pre_registered": True,
        "plan": "input/ideas/lai2023-gaps-and-memory-plan.md", "plan_status_at_run": "pre-registered 2026-11-01",
        "revision": "rev 2 (2026-11-01): review revisions Q1-Q8, S1-S6 added as supplementary/labelled; "
                    "pre-registered elements unchanged",
        "run_date": time.strftime("%Y-%m-%d"), "git_commit": head, "git_worktree_dirty_for_this_dir": dirty,
        "code_sha256": {"screen.py": _sha256(os.path.join(here, "screen.py")),
                        "tests/test_screen.py": _sha256(os.path.join(here, "tests", "test_screen.py")),
                        "data/lai2023_table2.csv": _sha256(os.path.join(here, "data", "lai2023_table2.csv"))},
        "software": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
                     "platform": platform.platform()},
        "seeds": {"BASE_SEED": BASE_SEED,
                  "cell_seed_entropy": "B = 0 and same-mu burn-in: [BASE_SEED, cell_index, B]; recalibrated burn-in: "
                                       "[BASE_SEED, cell_index, B, 1]; floors: [BASE_SEED, cell_index, B, 2 (B=0) or 3]; "
                                       "-> numpy SeedSequence; side labels from SeedSequence.spawn(1)[0]",
                  "NNLS_SEED": NNLS_SEED, "nnls_start_rng": "default_rng([NNLS_SEED, round(100 b), p])",
                  "cell_index_order": [f"{i}: b={b}, rho={r}, {g}" for i, (b, r, g) in enumerate(cell_list)]},
        "constants": {"T": T, "t0": T0, "h": H, "h_fine_for_richardson": H / 2, "b_grid": B_GRID, "rho_grid": RHO_GRID,
                      "regimes": REGIMES, "p_grid": P_GRID, "p_max": P_MAX, "Delta_grid": DELTAS,
                      "reference_Delta": REF_DELTA, "decision_times": [k * DT_DEC for k in DEC_K],
                      "profile_times": list(PROFILE_K), "paths_B0": args.paths, "paths_B1": args.paths_b1,
                      "paths_B10_same_mu": args.paths_b10, "paths_B10_recalibrated": args.paths_b10_recal,
                      "paths_convergence": args.paths_conv, "paths_floor_B0": args.paths_floor,
                      "paths_floor_burn_in": args.paths_floor_burn, "B_values": [0, 1, 10],
                      "target_side_count": TARGET_SIDE_COUNT, "tau_grid_h2_proxy": TAU_GRID,
                      "lifts": LIFT_NAMES, "gauss_composite_top_factor": GC_TOP_FACTOR},
        "operationalisation": OPERATIONALISATION, "deviations": deviations,
        "lai_table2": lai, "cells": cells, "burn_in_sensitivity": burn, "convergence_check": conv,
        "route_comparison_production_h": route, "h2_direction_check": h2,
        "runtime_seconds": timings, "limitations": LIMITATIONS,
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(_jsonable(out), f, indent=None, separators=(",", ":"))
    log(f"wrote {args.out}  total runtime {time.time() - t_start:.0f}s")
    return out


def _route_comparison(templates):
    """Generic Volterra route (trapezoid psi^, trapezoid conv, Richardson) vs exact filter route for
    production lifts at production h, on one fixed synthetic history (informational)."""
    rng = np.random.default_rng([BASE_SEED, 999])
    hist = np.sort(rng.uniform(0, 0.5, 200))
    t = 0.5
    out = {}
    for b in (1.15, 1.8):
        kern = PowerLawKernel(b, 0.8)
        for ln, p in itertools.product(LIFT_NAMES, (1, 4, 8)):
            x, c = scale_lift(templates[b][ln][p], 0.8)
            es = ExpSum(c, x)
            mu = 100.0
            L = int(round((T - t) / H)) + 1
            u = np.arange(L) * H
            exact = es.forecast(mu, filters_at(hist, t, x), u)
            uf = np.arange(2 * L - 1) * (H / 2)
            zf = mu + es.kernel(t + uf[None, :] - hist[:, None]).sum(0)
            psi_c = volterra_resolvent(es.kernel(u), H)
            psi_f = volterra_resolvent(es.kernel(uf), H / 2)
            gen = (4 * volterra_forecast(zf[None, :], psi_f, H / 2)[0, ::2] - volterra_forecast(zf[None, ::2], psi_c, H)[0]) / 3
            plain = volterra_forecast(zf[None, ::2], psi_c, H)[0]
            out[f"b={b} {ln} p={p}"] = {
                "max_rate": float(x.max()), "max_rate_times_h": float(x.max() * H),
                "rel_L2_diff_richardson_route": float(l2_trap(gen - exact, H) / l2_trap(exact, H)),
                "rel_L2_diff_plain_trapezoid_route": float(l2_trap(plain - exact, H) / l2_trap(exact, H))}
    return {"note": "generic grid route (Richardson, as used for the truth; and plain trapezoid) vs the exact "
                    "filter route used in production for the lifts", "history": "200 uniform events on [0, 0.5], "
                    "t = 0.5, mu = 100, rho = 0.8", "results": out,
            "max_rel_L2_diff_richardson_route": max(v["rel_L2_diff_richardson_route"] for v in out.values()),
            "max_rel_L2_diff_plain_route": max(v["rel_L2_diff_plain_trapezoid_route"] for v in out.values())}


OPERATIONALISATION = [
    "[flag] 'mu_bar T ~ 400 events per side' read as E[N^side_T] = 400 under the fresh-start (B = 0) convention: "
    "mu * int_0^T (1 + Psi(t)) dt = 400 (directional: excited side; common-mode: total baseline 2 mu, E[N_tot,T] = 800); "
    "the same mu results in both regimes; int(1+Psi) Richardson-extrapolated.",
    "[flag] rho = spectral radius of the 2x2 side branching matrix; common-mode Phi = (g/2)[[1,1],[1,1]], directional "
    "Phi = diag(g, 0).",
    "[flag] Lift (i) 'gauss': p-point generalised Gauss-Laguerre rule (alpha = b-1) for theta in y = t0 x; "
    "x_j = y_j/t0, c_j = rho(b-1)/(t0 Gamma(b)) W_j. Matches the first 2p moments of theta (short-lag behaviour). "
    "Alfonsi-Kebaier 2024 is not on disk, so the exact AK construction is UNVERIFIED.",
    "[flag] Lift (i-b) 'gauss_composite' (added in review rev 2; operationalisation of the plan's 'Gauss-type "
    "quadrature (Alfonsi-Kebaier)', AK 2024 not on disk; Abi Jaber-El Euch 2019 / Bayer-Breneis style): composite "
    "1-point Gauss rule for theta on I_1 = [0, xi_1), geometric interior breakpoints xi_1 < ... < xi_{p-1} = b/t0 "
    "(top factor 1, the theta-mean, fixed a priori), I_p = [xi_{p-1}, inf); weight theta(I_j), node = theta-mean of x "
    "on I_j (preserves moments 0 and 1 of theta exactly); the single scalar xi_1 minimises the L2[0,T] error "
    "(240-point log grid on [1e-3/T, upper] + bounded refinement; p = 2: xi_1 is the only breakpoint, upper 1e3/t0; "
    "p = 1 coincides with lift (i)).",
    "[flag] Lift (i-acero, supplementary): Acero-Plank-Zhang 2026 eq. (3) with K1 = 0, beta_j = midpoints, "
    "theta(I_j) via the regularised incomplete gamma; K2 minimises the Prop. 1 bound eps_u(K2) + "
    "T^(3/2) K2 theta([0,K2])/(sqrt(3) p) by a 400-point log grid on [1e-2/T, 1e3/t0] plus bounded refinement; "
    "eps_u(K2) = ||g(t) Q(b, K2(t+t0))||_L2[0,T] (closed form of the upper-tail kernel).",
    "[flag] Lift (ii): outer L-BFGS-B over log-rates with bounds [log(0.01/T), log(50/t0)], analytic variable-projection "
    "gradient (envelope theorem through the NNLS optimum); starts = log-spaced on [1/T, b/t0] (p = 1: geometric mean), "
    "8 jittered copies (sd 0.5 in log-rate, seeded), the Gauss nodes, and a warm start from the previous p; polish "
    "from the best start; inner scipy.optimize.nnls on the Cholesky factor of the exact Gram matrix (jitter 1e-14 tr G); "
    "<g, e^{-xt}> by composite Gauss-Legendre (geometric mesh). Fitted for rho = 1, weights scaled by rho.",
    "[flag] Lift (iii): rates geometric on [1/T, b/t0] (p = 1: sqrt(b/(t0 T))); exact convex QP min ||g - g^||_L2[0,T] "
    "s.t. sum c_j/x_j = rho, c >= 0 solved by enumerating supports (KKT on each support; 2^p - 1 <= 255 candidates).",
    "[flag] p = 0: 'p0_nhpp' m^_t(u) = mu(1 + Psi(t+u)) (THE p = 0 entry; with burn-in B: mu(1 + Psi(t+u+B))); "
    "'p0_baseline' m^ = mu (supplementary). Their 'kernel' block holds the formal metrics of g^ = 0.",
    "[flag] Supplementary MEAN-MATCHED variant '<lift>_mean_matched' (review Q2): same lifted kernel and history, "
    "baseline mu^ with mu^ int_0^T (1 + Psi^(s + B_cal)) ds = 400 per side (B_cal = the calibration convention of the "
    "run: 0 for B = 0 and same-mu runs, B for recalibrated runs), i.e. the lifted model reproduces the expected daily "
    "count; Dm_mm = Dm + (mu^_proc - mu_proc)(1 + Psi^(u)) evaluated exactly.",
    "[flag] Forecast-error norm ||Dm_t||_L2[0,T-t] by the trapezoid rule on the h-grid; relative error divides by "
    "||m_t|| in the same norm, per path and t. 'Mean over (paths, t)': equal weight on the 19 decision times, "
    "averaged within each path first; SE = across-path SD of the per-path means / sqrt(paths).",
    "[flag] Count-error proxy (review Q8): |int_0^{T-t} Dm_t(u) du| per path and t (trapezoid), absolute (per side) and "
    "relative to int_0^{T-t} m_t(u) du; mean over (paths, t).",
    "[flag] Bias part = ||mean_paths Dm_t||; fluctuation part = sqrt(mean_paths ||Dm_t - mean Dm_t||^2); relative "
    "versions divide by ||mean_paths m_t||; 'bias_noise_floor_abs' = fluct/sqrt(paths). N3 divides the fluctuation "
    "part by sqrt(E||m_t - E m_t||^2), the truth's own fluctuation (= the fluctuation part of p0_nhpp).",
    "[flag] N2 = mean ||Dm_p|| / mean ||Dm_{p0_nhpp}|| (ratio of means over (paths, t)); SE by the paired delta "
    "method on per-path means.",
    "[flag] H2 screen proxy: easy cells = b in {1.4, 1.8} x rho in {0.5, 0.8}; hard cell = (1.15, 0.95); "
    "p*_screen(tau) = min p with metric <= tau, tau in {0.10, 0.05, 0.02} for every normalisation; p = 0 entry = "
    "p0_nhpp (N2 = N3 = 1 there); '>8' counted as 9; classes flat / consistent / reversed / mixed as defined in "
    "h2_direction_check.definition. Evaluated for runs B=0, B=1 and B=10, same-mu and recalibrated.",
    "[flag] Recalibrated burn-in (review Q4, supplementary): mu_B = 400 / int_0^T (1 + Psi(s + B)) ds (expected in-day "
    "count per side 400; common-mode total 800 with baseline 2 mu_B). The pre-registered same-mu burn-in runs are kept.",
    "[flag] Numerical floor (review Q7): per cell, mean over (paths, t) of side*||m_R(h) - m_R(h/2)||_L2[0,T-t] where "
    "m_R(h) = Richardson(h, h/2) (production) and m_R(h/2) = Richardson(h/2, h/4), on independent histories (100 paths "
    "at B = 0, 50 for recalibrated burn-in); entries with mean ||Dm|| < 10 x floor are flagged "
    "'below_numerical_resolution'. Upper-bound indicator: the NNLS p = 8 mean ||Dm|| per cell.",
    "[flag] Common-mode: Dm per side = Dm_tot/2 (absolute norms halved; relative norms equal to the total's).",
    "[flag] Lift kernel tail mass beyond Delta: sum_j c_j e^{-x_j Delta}/x_j (absolute) and as a fraction of the "
    "lift's total mass; truth: rho (t0/(Delta+t0))^(b-1) and the fraction (t0/(Delta+t0))^(b-1).",
    "[flag] sup|g - g^| on [0,T]: maximum over the quadrature nodes plus a uniform grid of step 1e-5 T.",
    "[flag] Resolvent error ||psi^ - psi||_L2[0,T]: psi^ exact (eigen-decomposition), psi = Richardson trapezoid "
    "solution on the h-grid, taken piecewise linear; cross terms by exact product integration. Floor ~ discretisation "
    "error of psi.",
    "[flag] Lifted forecasts m^ are evaluated EXACTLY via the exponential filters X_j (closed-form solution of the "
    "linear ODE for E[Y_j(t+u)|F_t]); the generic Volterra route (trapezoid psi^ + trapezoid convolution) is used for "
    "the truth and, for lifts, only as a cross-check (tests; route_comparison_production_h).",
    "[flag] True forecast: Richardson extrapolation (4 m_{h/2} - m_h)/3 of the trapezoid scheme, evaluated on the "
    "h = t0/10 grid (zeta exact at grid points).",
    "[flag] Burn-in: immigrants Poisson on [-B, T] (fresh start at -B). Pre-day events older than 0.5T enter the true "
    "forecast through a sub-grid (every 10th fine point) + cubic-spline evaluation of their smooth excitation (error "
    "< 1e-9 relative, tested); all other kernel sums are evaluated exactly at grid points.",
    "[flag] Common-mode side labels are drawn 50/50 after the cluster simulation; they are irrelevant to the per-side "
    "forecast because Phi is symmetric and are used only for the per-side count check.",
    "[flag] Convergence check: same histories (same seed and mu), h_eval = h/2 (Richardson from h/2, h/4) vs h; "
    "relative change of the mean ||Dm|| (absolute) for p in {1, 4, 8}, all five lifts; target 2% from the dispatch.",
    "[flag] Exponential-kernel resolvent test: alpha = 50, beta = 100 (time scale t0, rho = 0.5); 'rel. err' = "
    "L2[0,T]-relative and sup-relative to psi(0).",
    "[flag] Filter-route vs generic-route tests (1e-6 relative): a moderate-rate exponential sum {1, 5, 20}/T and the "
    "production NNLS p = 4 lift of the hard cell, both at production h with the production (Richardson) generic route.",
    "[flag] Lai claim (a) evaluated literally: part 1 = rows with beta >= 1.45 in [0.4%, 3%]; part 2 = rows with "
    "1.07 <= beta <= 1.2 in [12%, 55%]; rows with 1.2 < beta < 1.45 are not covered by the claim and listed separately.",
    "[flag] Storage: B = 0 cells store the per-t profile at all 19 decision times (profile_all_t) plus the 3 labelled "
    "times; burn-in runs store the 3 labelled times only. Floats in screen.json are rounded to 8 significant digits.",
]

DEVIATIONS = [
    "Lai Table 2 is on PDF physical page 7 (journal p. 782), not physical page 6 as in the dispatch's pdftotext "
    "command; all 16 rows were verified against page 7 with no value mismatch.",
    "Review rev 2 additions (all supplementary and labelled; no pre-registered element changed): lift (i-b) "
    "gauss_composite; mean-matched variants of every lift; count-error proxy; normalisations N2/N3/C of the H2 screen "
    "proxy; recalibrated-mu burn-in runs (B = 1, 10) next to the specified same-mu runs; per-cell numerical floors; "
    "p = 8 in the convergence check; all-19-t profiles; code hashes.",
    "The H2 screen-proxy summary is stated conditionally (which normalisation / burn-in convention points which way); "
    "the earlier 'mostly reversed' headline held only for N1 at B = 0 with p = 0 counted.",
]

LIMITATIONS = [
    "Tier 0 has no control layer: ||Dm|| is a forecast error, not regret. Regret depends on how the Riccati value map "
    "weights Dm (H1's curvature kernel K), which Tier 0 does not compute; the p*_screen proxy is NOT p* of H2, and its "
    "direction depends on the normalisation and on the burn-in convention (see h2_direction_check).",
    "In Tier 0 the two flow regimes differ only through the count scale (common-mode total baseline 2 mu): relative "
    "errors of the bias part coincide in expectation, the fluctuation part shrinks with the count.",
    "The B = 0 convention ignores pre-day memory; with heavy tails (b = 1.15: about half the kernel mass lies beyond T) "
    "this convention is optimistic for long-memory cells; lifts fitted on [0,T] lags are wrong at lags > T, which the "
    "burn-in runs expose.",
    "Lift (i) is a single global Gauss rule for theta (short-lag moments only; mass captured 0.13-0.32 rho at b = 1.15); "
    "lift (i-b) fixes the top breakpoint at b/t0 a priori and optimises one scalar; neither is the verified "
    "Alfonsi-Kebaier construction (source not on disk).",
    "The Acero eq. (3) lift uses the K2 that minimises their Proposition 1 bound; for p <= 8 that bound is ~||g|| "
    "(vacuous), so the minimiser is degenerate (small K2) and the lift is supplementary only.",
    "The NNLS L2[0,T] fit does not see kernel mass beyond T; its total mass is not controlled (subcriticality flag "
    "reported per lift).",
    "Lift (iii) mass_preserving: the exact QP leaves weights at zero, so its effective number of factors is below the "
    "nominal p in many entries (p = 8 -> 4 nonzero factors); the lift is reported at nominal p.",
    "The mean-matched variant fixes the expected daily count, not the conditional mean curve; it removes the gross "
    "level bias of wrong-mass lifts but not the shape error of Psi^.",
    "Lai Table 2 time units are unstated, so the Lai tail masses beyond Delta = 1 are in Lai's (unknown) unit.",
    "MC SEs rest on the CLT across independent paths; at rho = 0.95 counts are strongly over-dispersed.",
    "The burn-in runs use fewer paths and independent (non-CRN) histories; differences carry both SEs. Numerical floors "
    "use 100 (B = 0) or 50 (recalibrated burn-in) paths and are not computed for the same-mu burn-in runs.",
]


if __name__ == "__main__":
    main()
