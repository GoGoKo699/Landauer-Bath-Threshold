#!/usr/bin/env python3
"""Compare the critical-window heat curve with finite grouped rank sorting."""

from __future__ import annotations

from math import ceil, comb, exp, floor, fsum, log, log1p, pi, sqrt

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import expit, log_ndtr, logsumexp


def beta_heat_curve(alpha: float, dimension: int, scale: float,
                    integer_penalty: int | None = None) -> float:
    """Evaluate the limiting heat or fixed integer-penalty objective."""
    p = expit(-alpha)
    variance = 2 * p * (1 - p) * scale
    sigma = sqrt(variance)
    shells = np.arange(-ceil(36 / alpha), ceil(1 + alpha * variance + 12 * sigma) + 1)
    log_weights = alpha * shells
    log_rank_ratio = log(dimension)
    max_shift = ceil(log_rank_ratio / alpha) + 1
    if integer_penalty is not None:
        # The shifted non-target count is (dimension - 1) exp(-alpha L) A(u).
        log_rank_ratio -= log1p((dimension - 1) * exp(-alpha * integer_penalty))

    def log_count(u: float) -> float:
        # Reduce the argument to [0, 1) using A(u+1) = exp(alpha) A(u).
        period = floor(u)
        return alpha * period + logsumexp(log_weights + log_ndtr((u - period - shells) / sigma))

    def integrand(z: float) -> float:
        u = sigma * z - alpha * variance
        target = log_count(u) + log_rank_ratio
        shift = brentq(lambda step: log_count(u + step) - target, 0, max_shift, xtol=1e-12)
        return shift * exp(-z**2 / 2) / sqrt(2 * pi)

    mean_shift, _ = quad(integrand, -9, 9, epsabs=2e-11, epsrel=2e-11)
    return alpha * mean_shift


def finite_rank_sort(pairs: int, alpha: float, dimension: int, scale: float,
                     penalty: float | None = None) -> tuple[float, float]:
    """Return beta Q and error for maximally mixed memory at c_N = scale.

    Omit penalty for maximal cooling followed by heat minimization. Otherwise
    minimize beta Q + alpha * penalty * error, with penalty in units of Delta.
    Both use exact integer multiplicities and floating-point energies and weights.
    """
    detuning = sqrt(scale / pairs)
    multiplicities = [comb(pairs, k) for k in range(pairs + 1)]
    groups = sorted(
        (plus + minus + detuning * (plus - minus), multiplicities[plus] * multiplicities[minus])
        for plus in range(pairs + 1)
        for minus in range(pairs + 1)
    )
    target = [(energy, count, False) for energy, count in groups]
    other = [(energy, (dimension - 1) * count, True) for energy, count in groups]
    outputs = target + other
    if penalty is not None:
        outputs.sort(key=lambda group: group[0] + penalty * group[2])

    log_partition = pairs * (
        np.logaddexp(0, -alpha * (1 + detuning))
        + np.logaddexp(0, -alpha * (1 - detuning))
    )
    log_normalizer = log_partition + log(dimension)
    output_groups = iter(outputs)
    output_energy, output_count, is_error = next(output_groups)
    heat_terms = []
    error_terms = []
    for energy, count in groups:
        input_count = dimension * count
        while input_count:
            if output_count == 0:
                output_energy, output_count, is_error = next(output_groups)
            matched = min(input_count, output_count)
            mass = exp(log(matched) - alpha * energy - log_normalizer)
            heat_terms.append(mass * (output_energy - energy))
            if is_error:
                error_terms.append(mass)
            input_count -= matched
            output_count -= matched
    return alpha * fsum(heat_terms), fsum(error_terms)


def main() -> None:
    dimension = 2
    penalty = 8
    print("alpha        c       N    limit beta Q  rank beta Q   reset error   penalty limit  finite penalty")
    for alpha, scale in [(1.0, 0.05), (1.0, 0.10), (log(2), 0.05)]:
        limit = beta_heat_curve(alpha, dimension, scale)
        penalty_limit = beta_heat_curve(alpha, dimension, scale, penalty)
        for pairs in [24, 96, 256]:
            heat, error = finite_rank_sort(pairs, alpha, dimension, scale)
            penalized_heat, penalized_error = finite_rank_sort(pairs, alpha, dimension, scale, penalty)
            objective = penalized_heat + alpha * penalty * penalized_error
            print(f"{alpha:.9f}  {scale:.2f}  {pairs:4d}  {limit:.9f}   {heat:.9f}   {error:.3e}     "
                  f"{penalty_limit:.9f}    {objective:.9f}")


if __name__ == "__main__":
    main()
