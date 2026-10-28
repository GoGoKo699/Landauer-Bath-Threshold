#!/usr/bin/env python3
"""Regenerate finite-instance checks, CSV tables, and two SVG figures.

Run from the repository root: python scripts/run_checks.py
The fixed seed, model normalization, software versions, numerical residuals,
and optimization contracts are recorded in results/summary.json.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("MPLCONFIGDIR", "/tmp/landauer-bath-matplotlib")

import numpy as np
import scipy
from scipy.linalg import expm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from landauer_bath.compression import (
    binomial_cumulative_integers, cutoff_certificate, cutoff_permutation, explicit_proof_selector,
    paired_certificate, permutation_statistics, rank_bath, selected_cutoff,
)
from landauer_bath.optimization import (
    heat_population_optimum, maximum_cooling_permutation, permutation_matrix,
)
from landauer_bath.spectral import (
    paired_gaps, paired_log_characteristic_sq, paired_witness,
    reset_entropy_bound, spectral_witness, thermal_bath, unitary_statistics,
)

SEED = 20261028
BETA = math.log(4.0)
DELTA = 1.0
D_MEMORY = 2
T0 = 2 * math.pi / (BETA * DELTA)
AMPLITUDE = 0.35


def write_csv(path: Path, rows: list[dict]) -> None:
    keys = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=keys, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def coherent_checks() -> list[dict]:
    rows = []
    for n in [1, 2, 3]:
        for delta in [0.0, 0.2]:
            energies, probabilities = thermal_bath(paired_gaps(n, delta), BETA)
            perm = maximum_cooling_permutation(energies, probabilities)
            P = permutation_matrix(perm)
            dim = len(P)
            cases = [("identity", 0, 0.0, np.eye(dim)),
                     ("max_cooling_permutation", 0, 0.0, P)]
            for index, theta in enumerate([0.04, 0.12, 0.25]):
                seed = SEED + 1000 * n + round(100 * delta) + index
                rng = np.random.default_rng(seed)
                X = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
                H = (X + X.conj().T) / 2
                H /= np.linalg.norm(H, ord=2)
                cases.append(("coherent_near_cooling", seed, theta,
                              expm(1j * theta * H) @ P))
            for index in range(2):
                seed = SEED + 2000 * n + round(100 * delta) + index
                rng = np.random.default_rng(seed)
                X = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
                Q, R = np.linalg.qr(X)
                phases = np.diag(R) / np.abs(np.diag(R))
                cases.append(("haar_unitary", seed, math.nan, Q * phases))
            for family, seed, theta, U in cases:
                stats = unitary_statistics(U, energies, probabilities,
                                          BETA, D_MEMORY, T0)
                if stats["witness_slack"] < -2e-9:
                    raise AssertionError("Spectral witness violated numerically.")
                if stats["pinsker_slack"] < -2e-9:
                    raise AssertionError("Pinsker check failed.")
                rows.append({"N_pairs": n, "delta": delta, "Delta": DELTA,
                             "beta": BETA, "d": D_MEMORY,
                             "joint_dimension": dim, "family": family,
                             "seed": seed, "rotation_angle": theta, **stats})
    return rows


def lp_frontiers() -> list[dict]:
    rows = []
    for n in [1, 2]:
        for delta in [0.0, 0.2]:
            energies, probabilities = thermal_bath(paired_gaps(n, delta), BETA)
            perm = maximum_cooling_permutation(energies, probabilities)
            weights = np.tile(probabilities / D_MEMORY, D_MEMORY)
            min_error = float(weights[perm // len(probabilities) != 0].sum())
            for epsilon in np.linspace(min_error + 1e-8, 0.45, 8):
                optimum = heat_population_optimum(energies, probabilities,
                                                  float(epsilon), D_MEMORY)
                w = spectral_witness(probabilities, D_MEMORY, T0, float(epsilon))
                heat_lower = math.log(D_MEMORY) - reset_entropy_bound(
                    float(epsilon), D_MEMORY) + w
                optimum_beta_heat = BETA * optimum["heat"]
                slack = optimum_beta_heat - heat_lower
                if slack < -2e-8:
                    raise AssertionError("LP optimum below the finite spectral lower bound.")
                rows.append({"N_pairs": n, "delta": delta, "Delta": DELTA,
                             "beta": BETA, "d": D_MEMORY,
                             "joint_dimension": D_MEMORY * len(probabilities),
                             "epsilon_target": float(epsilon),
                             "minimum_feasible_population_error": min_error,
                             "beta_heat_optimum_numerical": optimum_beta_heat,
                             "beta_heat_witness_lower": heat_lower,
                             "spectral_sigma_correction": w,
                             "optimum_minus_lower": slack, **optimum})
    return rows


def enumerated_cutoffs() -> list[dict]:
    rows = []
    cases = [(6, 1.8, 1, 2), (8, 1.8, 2, 2), (10, 1.4, 2, 2),
             (12, 1.6, 3, 2), (14, 1.5, 4, 2),
             (10, 1.3, 2, 3), (12, 1.5, 2, 3)]
    for m, b, k, d in cases:
        cert = cutoff_certificate(m, b, k, d)
        if cert is None:
            raise AssertionError("Selected exact cutoff case has no rank certificate.")
        excitation, probabilities = rank_bath(m, b)
        perm = cutoff_permutation(m, k, d)
        stats = permutation_statistics(perm, excitation, probabilities, b, d)
        R = sum(math.comb(m, ell) for ell in range(k + 1))
        tail = float(probabilities[R:].sum())
        actual_bound = cert.beta_heat_upper * (1 - tail)
        if stats["worst_input_beta_heat"] > actual_bound + 2e-10:
            raise AssertionError("Pointwise energy inequality failed.")
        if stats["actual_reset_error_maxmixed"] > tail + 2e-10:
            raise AssertionError("Reset error exceeds the bath-tail bound.")
        rows.append({**cert.to_dict(), "bath_dimension": len(probabilities),
                     "cutoff_rank_R": R, "enumerated_bath_tail": tail,
                     "beta_heat_upper_with_good_weight": actual_bound,
                     "half_diamond_error_upper": tail, **stats})
    return rows


def cumulative_checks() -> list[dict]:
    rows = []
    for m in [16, 32, 64, 128, 256, 512, 1024]:
        cumulative = binomial_cumulative_integers(m)
        for b in [0.2, 0.3, 0.45, 0.7, 1.0, 1.5]:
            for d in [2, 3]:
                k = selected_cutoff(m, b, "logarithmic")
                cert = cutoff_certificate(m, b, k, d)
                row = {"check_family": "all_cumulative_shells", "m": m, "b": b, "z": m * b * b,
                       "d": d, "k": k, "certified": cert is not None}
                if cert is not None:
                    ratios = []
                    for ell in range(k + 1):
                        if cumulative[ell + cert.r] < d * cumulative[ell]:
                            raise AssertionError("Exact cumulative count inequality failed.")
                        ratios.append(cumulative[ell + cert.r] / cumulative[ell])
                    row.update({"r": cert.r,
                                "minimum_cumulative_rank_ratio": min(ratios),
                                "shell_of_minimum_ratio": int(np.argmin(ratios)),
                                "log_termwise_rank_lower": cert.log_rank_ratio_lower,
                                "verified_shell_count": k + 1,
                                "binomial_tail": cert.binomial_tail,
                                "hoeffding_tail_upper": cert.hoeffding_tail_upper})
                rows.append(row)
    for b in [1.0, 0.3, 0.1, 0.01, 0.001]:
        for z_target in [25_000, 50_000, 1_000_000]:
            m = math.ceil(z_target / (b * b))
            selected = explicit_proof_selector(m, b)
            if selected is None:
                raise AssertionError("Expected gamma-selector case is outside its domain.")
            cert, gamma = selected
            rows.append({"check_family": "explicit_gamma_selector", "m": m,
                         "b": b, "z": m * b * b, "d": 2, "k": cert.k,
                         "r": cert.r, "certified": True, "gamma": gamma,
                         "log_termwise_rank_lower": cert.log_rank_ratio_lower,
                         "verified_shell_count": 0,
                         "beta_heat_upper": cert.beta_heat_upper,
                         "selector_heat_upper": math.log(2) / (1 - gamma) + b,
                         "hoeffding_tail_upper": cert.hoeffding_tail_upper})
    return rows


def threshold_curves() -> list[dict]:
    rows = []
    p = 1 / 5
    v = p * (1 - p)
    coefficient = 8 * math.pi ** 2 * v
    intercept = paired_witness(1, 0.0, BETA)
    for n in [8, 32, 128, 512]:
        for collective in np.linspace(0, 1, 101):
            delta = math.sqrt(float(collective) / n)
            rows.append({"curve_family": "collective_detuning", "N_pairs": n,
                         "delta": delta, "collective_detuning_c": float(collective),
                         "alpha": None, "amplitude": None,
                         "W_zero_error_intercept": paired_witness(n, delta, BETA),
                         "log_characteristic_squared": paired_log_characteristic_sq(
                             n, delta, BETA),
                         "bounded_c_limit_W": intercept * math.exp(-coefficient * collective)})
    sizes = np.unique(np.rint(np.logspace(1, 12, 89)).astype(np.int64))
    for alpha in [0.25, 0.5, 0.75]:
        for n0 in sizes:
            n = int(n0)
            delta = AMPLITUDE * n ** (-alpha)
            collective = n * delta * delta
            rows.append({"curve_family": "power_law", "N_pairs": n,
                         "delta": delta, "collective_detuning_c": collective,
                         "alpha": alpha, "amplitude": AMPLITUDE,
                         "W_zero_error_intercept": paired_witness(n, delta, BETA),
                         "log_characteristic_squared": paired_log_characteristic_sq(
                             n, delta, BETA),
                         "bounded_c_limit_W": intercept * math.exp(-coefficient * collective)})
    return rows


def construction_curves() -> list[dict]:
    rows = []
    sizes = np.unique(np.rint(np.logspace(3, 12, 91)).astype(np.int64))
    for rule in ["logarithmic", "proof"]:
        for n0 in sizes:
            n = int(n0)
            delta = AMPLITUDE * n ** (-0.25)
            result = paired_certificate(n, delta, BETA, cutoff_rule=rule)
            result.update({"alpha": 0.25, "amplitude": AMPLITUDE,
                           "collective_detuning_c": n * delta * delta,
                           "landauer_beta_heat": math.log(D_MEMORY)})
            rows.append(result)
    return rows


def homogeneous_control() -> list[dict]:
    rows = []
    for m in [2, 4, 8, 12, 16]:
        excitation, probabilities = rank_bath(m, BETA)
        perm = maximum_cooling_permutation(excitation.astype(float), probabilities)
        stats = permutation_statistics(perm, excitation, probabilities, BETA)
        rows.append({"bath_qubits": m, **stats})
    return rows


def make_figures(threshold: list[dict], construction: list[dict], destination: Path) -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.alpha": 0.2,
                         "svg.fonttype": "none", "svg.hashsalt": "landauer-bath-threshold-v1"})
    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.5), constrained_layout=True)
    ax = axes[0]
    colors = ["#9bc4e2", "#5b9dcc", "#2c6da4", "#153f67"]
    for n, color in zip([8, 32, 128, 512], colors):
        selected = [r for r in threshold if r["curve_family"] == "collective_detuning"
                    and r["N_pairs"] == n]
        ax.semilogy([r["collective_detuning_c"] for r in selected],
                    [r["W_zero_error_intercept"] for r in selected],
                    color=color, lw=1.6, label=f"finite N = {n}")
    selected = [r for r in threshold if r["curve_family"] == "collective_detuning"
                and r["N_pairs"] == 512]
    ax.semilogy([r["collective_detuning_c"] for r in selected],
                [r["bounded_c_limit_W"] for r in selected],
                "--", color="black", lw=1.4, label="bounded-c limit")
    inherited_excess = math.log(2) / 3
    ax.scatter([0], [inherited_excess], marker="D", s=32, color="#a44339", zorder=6)
    ax.annotate("homogeneous maximal-cooling\nasymptote (AHJM11; not the witness)",
                xy=(0, inherited_excess), xytext=(0.17, 0.045),
                fontsize=8.1, color="#89372f",
                arrowprops={"arrowstyle": "-", "color": "#a44339", "lw": 0.8})
    ax.set(xlabel=r"collective detuning $c=N(\delta/\Delta)^2$",
           ylabel=r"zero-error witness intercept $W_N(0)$",
           title="A. Finite spectral witness and its limit",
           xlim=(-0.015, 1), ylim=(1e-7, 0.35))
    ax.legend(frameon=False, fontsize=8, loc="lower left")
    ax = axes[1]
    for alpha, color in [(0.25, "#247f61"), (0.5, "#bd7c20"), (0.75, "#7654a3")]:
        selected = [r for r in threshold if r["curve_family"] == "power_law"
                    and r["alpha"] == alpha]
        ax.loglog([r["N_pairs"] for r in selected],
                  [max(r["W_zero_error_intercept"], 1e-300) for r in selected],
                  lw=2, color=color, label=fr"$\alpha={alpha:g}$")
    ax.set(xlabel="number of physical qubit pairs N", ylabel=r"$W_N(0)$",
           title=r"B. Shrinking detuning $\delta/\Delta=0.35N^{-\alpha}$",
           ylim=(1e-7, 0.2))
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    fig.suptitle(r"Spectral lower bound: $d=2$, $\Delta=1$, $\beta=\ln4$", fontsize=13)
    fig.savefig(destination / "spectral_obstruction.svg", metadata={"Date": None})
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.3), constrained_layout=True)
    selected = [r for r in construction if r["certified"]
                and r["cutoff_rule"] == "logarithmic"]
    proof = [r for r in construction if r["certified"]
             and r["cutoff_rule"] == "proof"]
    ax = axes[0]
    ax.semilogx([r["N_pairs"] for r in selected],
                 [r["beta_heat_upper"] for r in selected],
                 color="#206aa1", lw=2, label="certified cutoff upper bound")
    ax.semilogx([r["N_pairs"] for r in proof],
                 [r["beta_heat_upper"] for r in proof],
                 color="#7898ae", lw=1.5, linestyle="--",
                 label=r"more conservative $t=z^{1/4}$ cutoff")
    ax.axhline(math.log(2), color="black", lw=1.2, linestyle=":", label=r"Landauer limit $\ln2$")
    ax.set(xlabel="number of physical qubit pairs N", ylabel=r"certified upper bound on $\beta Q$",
           title="A. Explicit protocol cost; no optimality claim")
    ax.legend(frameon=False, fontsize=8.3, loc="upper right")
    ax = axes[1]
    ax.loglog([r["N_pairs"] for r in selected],
               [r["reset_error_upper"] for r in selected],
               color="#206aa1", lw=2, label="channel error upper bound")
    ax.set(xlabel="number of physical qubit pairs N",
           ylabel="upper bound on half-diamond reset error",
           title="B. Same certified cutoff protocol", ylim=(1e-3, 1))
    ax.legend(frameon=False, fontsize=8.3)
    fig.suptitle(r"Constructive upper bounds: $\delta/\Delta=0.35N^{-1/4}$, $\beta\Delta=\ln4$", fontsize=13)
    fig.savefig(destination / "certified_construction.svg", metadata={"Date": None})
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "results")
    parser.add_argument("--figures-dir", type=Path, default=ROOT / "science" / "figures")
    parser.add_argument("--skip-figures", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figures_dir.mkdir(parents=True, exist_ok=True)

    unitary = coherent_checks()
    lp = lp_frontiers()
    cutoffs = enumerated_cutoffs()
    cumulative = cumulative_checks()
    threshold = threshold_curves()
    construction = construction_curves()
    tables = {"unitary_checks.csv": unitary, "finite_lp_frontier.csv": lp,
              "cutoff_permutations.csv": cutoffs,
              "binomial_certificates.csv": cumulative,
              "threshold_curves.csv": threshold,
              "construction_curves.csv": construction}
    for filename, rows in tables.items():
        write_csv(args.output_dir / filename, rows)
    if not args.skip_figures:
        make_figures(threshold, construction, args.figures_dir)
    positive = [r for r in unitary if r["witness"] > 1e-10]
    certified = [r for r in construction if r["certified"]
                 and r["cutoff_rule"] == "logarithmic"]
    summary = {
        "normalization": {"d": D_MEMORY, "Delta": DELTA, "beta": BETA,
                          "beta_Delta": BETA * DELTA, "t0": T0,
                          "logs": "natural", "heat_units": "Delta=1"},
        "reproducibility": {"seed": SEED, "python": platform.python_version(),
                            "numpy": np.__version__, "scipy": scipy.__version__,
                            "matplotlib": matplotlib.__version__,
                            "command": "python scripts/run_checks.py"},
        "table_row_counts": {name: len(rows) for name, rows in tables.items()},
        "unitary_checks": {"sample_count": len(unitary),
                           "positive_witness_count": len(positive),
                           "largest_joint_dimension": max(r["joint_dimension"] for r in unitary),
                           "minimum_witness_slack": min(r["witness_slack"] for r in unitary),
                           "minimum_positive_witness_slack": min(r["witness_slack"] for r in positive),
                           "maximum_entropy_identity_residual": max(
                               r["relative_entropy_identity_error"] for r in unitary),
                           "maximum_unitarity_residual": max(r["unitarity_error"] for r in unitary)},
        "population_LP": {"instances": len(lp),
                          "largest_joint_dimension": max(r["joint_dimension"] for r in lp),
                          "minimum_optimum_minus_witness_lower": min(r["optimum_minus_lower"] for r in lp),
                          "maximum_stochastic_residual": max(r["stochastic_residual"] for r in lp),
                          "maximum_population_residual": max(r["population_constraint_residual"] for r in lp)},
        "cumulative_count_checks": {"parameter_choices": len(cumulative),
                                    "certified_choices": sum(r["certified"] for r in cumulative),
                                    "exact_shell_inequalities_checked": sum(
                                        r.get("verified_shell_count", 0) for r in cumulative)},
        "construction_logarithmic_cutoff": {"certified_points": len(certified),
                                             "first_certified": certified[0],
                                             "largest_N": certified[-1]},
        "homogeneous_control": {
            "attribution": "Allahverdyan et al., Phys. Rev. E 84, 041109 (2011), Sec. VI.B",
            "known_maximal_cooling_asymptotic_beta_Q": (2 / 3) * math.log(4),
            "known_maximal_cooling_asymptotic_excess_over_ln2": math.log(2) / 3,
            "zero_error_spectral_witness_intercept": paired_witness(1, 0, BETA),
            "finite_max_cooling_permutations": homogeneous_control()},
        "contracts": {
            "unitary_sampling": "Finite numerical checks, not a proof of the universal bound; coherent near-cooling samples keep the spectral correction nonzero.",
            "LP": "Numerical all-unitary optimum of mean heat at a target-population error for I_d/d input, by Schur-Horn. Not a diamond-error or universal-channel optimum. Solver tolerances are not formal exact arithmetic certification.",
            "cutoff_permutations": "Actual enumerated permutation costs and population errors. The full-channel error column is a proved upper bound, checked on full small-bath channels in the unittest suite.",
            "large_construction": "Analytic heat/error upper bounds from explicit cutoff permutations; every accepted rank expansion uses exact integer arithmetic. No large Hilbert-space enumeration or optimization.",
            "probability_arithmetic": "Probability formulas are analytic bounds evaluated in binary64, not interval-certified values. Log bounds and underflow flags are retained; positive ordinary-space bounds are floored at the smallest positive float. The recorded integer k is used with event X>=k+1, so the flexible finite lemma does not rely on the selector reproducing a symbolic floor exactly.",
            "missing_certificates": "certified=false means the selected cutoff/search returned no certificate; it is not an impossibility statement.",
            "witness_curves": "W_N(0) is the zero-error intercept of the entropy-production lower bound. Finite full-rank baths cannot reset exactly; these curves are not an attained finite-bath heat or an optimal heat curve.",
            "cutoff_rule": "Main finite curve uses t=.5 sqrt(log(1+z)); the proof cutoff t=z^(1/4) is also recorded. Both satisfy the asymptotic requirements, and the finite rank condition is independently checked.",
        },
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(f"Generated {len(tables)} CSV tables and summary.json.")
    print(f"Unitary checks: {len(unitary)} samples; {len(positive)} positive spectral corrections.")
    print(f"Maximum entropy-identity residual: {summary['unitary_checks']['maximum_entropy_identity_residual']:.3g}")
    print(f"LP checks: {len(lp)} instances; minimum lower-bound slack {summary['population_LP']['minimum_optimum_minus_witness_lower']:.6g}.")
    print(f"Exact cumulative inequalities: {summary['cumulative_count_checks']['exact_shell_inequalities_checked']}.")
    last = certified[-1]
    print(f"Largest construction N={last['N_pairs']}: beta Q <= {last['beta_heat_upper']:.9g}, channel error <= {last['reset_error_upper']:.6g}.")
    if not args.skip_figures:
        print("Figures: spectral_obstruction.svg; certified_construction.svg.")


if __name__ == "__main__":
    main()
