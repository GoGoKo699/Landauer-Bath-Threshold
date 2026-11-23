"""Independent finite-basis comparisons for the critical-window diagnostics."""

from math import log, sqrt
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "scripts")]

import numpy as np

from landauer_bath.optimization import maximum_cooling_permutation
from landauer_bath.spectral import paired_gaps, thermal_bath
from check_critical_heat import beta_heat_curve, finite_rank_sort


class CriticalHeatChecks(unittest.TestCase):
    def test_grouped_sort_matches_explicit_bath_basis(self):
        pairs, alpha, scale = 2, 0.91, 0.17
        detuning = sqrt(scale / pairs)
        energies, probabilities = thermal_bath(paired_gaps(pairs, detuning), alpha)
        bath_size = len(energies)
        for dimension in (2, 3):
            weights = np.tile(probabilities / dimension, dimension)
            output_energy = np.tile(energies, dimension)
            output_error = np.arange(dimension * bath_size) >= bath_size
            for penalty in (None, 0.4):
                with self.subTest(dimension=dimension, penalty=penalty):
                    if penalty is None:
                        permutation = maximum_cooling_permutation(energies, probabilities, dimension)
                    else:
                        inputs = np.argsort(-weights, kind="stable")
                        outputs = np.argsort(output_energy + penalty * output_error, kind="stable")
                        permutation = np.empty_like(inputs)
                        permutation[inputs] = outputs
                    expected_heat = alpha * (weights @ output_energy[permutation] - probabilities @ energies)
                    expected_error = weights @ output_error[permutation]
                    heat, error = finite_rank_sort(pairs, alpha, dimension, scale, penalty)
                    self.assertAlmostEqual(heat, expected_heat, places=12)
                    self.assertAlmostEqual(error, expected_error, places=12)

    def test_resonant_and_nonresonant_limits_against_rank_sorting(self):
        dimension = 2
        penalty = 8
        cases = [
            (log(2), 0.05, log(2), 0.689294147, 0.011),
            (1.0, 0.05, 0.723139421, 0.722830115, 0.004),
            (1.0, 0.10, 0.707088725, 0.706767663, 0.004),
        ]
        for alpha, scale, expected_limit, expected_penalty_limit, tolerance in cases:
            with self.subTest(alpha=alpha, scale=scale):
                limit = beta_heat_curve(alpha, dimension, scale)
                self.assertAlmostEqual(limit, expected_limit, places=8)
                penalty_limit = beta_heat_curve(alpha, dimension, scale, penalty)
                self.assertAlmostEqual(penalty_limit, expected_penalty_limit, places=8)
                self.assertLess(penalty_limit, limit)
                heat, error = finite_rank_sort(256, alpha, dimension, scale)
                penalized_heat, penalized_error = finite_rank_sort(256, alpha, dimension, scale, penalty)
                objective = penalized_heat + alpha * penalty * penalized_error
                self.assertLess(error, 1e-12)
                self.assertLess(abs(heat - limit), tolerance)
                self.assertLess(abs(objective - penalty_limit), tolerance)
                self.assertLessEqual(objective, heat + alpha * penalty * error + 1e-12)


if __name__ == "__main__":
    unittest.main()
