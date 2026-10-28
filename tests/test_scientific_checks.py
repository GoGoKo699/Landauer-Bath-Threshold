"""Small independent checks of the scientific constructions and inequalities.

Run from the repository root with:
    python -m unittest discover -s tests -v
"""

from pathlib import Path
import itertools
import math
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
from scipy.linalg import expm

from landauer_bath.compression import (
    apply_channel_with_reference, binomial_cumulative_integers,
    channel_tensor, channel_tensor_for_bath_rank, cutoff_certificate,
    cutoff_permutation, explicit_proof_selector, paired_certificate, permutation_statistics, rank_bath, rank_condition,
    selected_cutoff,
)
from landauer_bath.optimization import (
    heat_population_optimum, maximum_cooling_permutation, permutation_matrix,
)
from landauer_bath.spectral import (
    characteristic, hermitian_trace_norm, paired_gaps,
    paired_log_characteristic_sq, thermal_bath, unitary_statistics,
)


class ScientificChecks(unittest.TestCase):
    def test_lp_interior_point_is_attained_by_coherent_rotation(self):
        """A non-permutation LP point is reproduced by a genuine unitary."""
        beta = math.log(4)
        energy, p = thermal_bath(np.array([1.0]), beta)
        theta = math.pi / 4
        U = np.eye(4, dtype=complex)
        i, j = 1, 2  # |target,excited> and |non-target,ground>
        U[np.ix_([i, j], [i, j])] = [[math.cos(theta), -math.sin(theta)],
                                    [math.sin(theta), math.cos(theta)]]
        stats = unitary_statistics(U, energy, p, beta, 2, 2 * math.pi / beta)
        lp = heat_population_optimum(energy, p, stats["epsilon"], 2)
        self.assertAlmostEqual(lp["heat"], stats["heat"], places=10)
        self.assertAlmostEqual(stats["epsilon"], 0.35, places=12)
        self.assertLess(lp["stochastic_residual"], 1e-9)

    def test_maximal_cooling_permutation_against_all_four_dimensional_permutations(self):
        beta = math.log(4)
        energy, p = thermal_bath(np.array([1.0]), beta)
        weights = np.tile(p / 2, 2)
        points = []
        for perm in itertools.permutations(range(4)):
            perm = np.asarray(perm)
            error = weights[perm // 2 != 0].sum()
            heat = weights @ energy[perm % 2] - p @ energy
            points.append((float(error), float(heat)))
        minimum_error = min(v[0] for v in points)
        minimum_heat_at_error = min(v[1] for v in points
                                    if abs(v[0] - minimum_error) < 1e-12)
        perm = maximum_cooling_permutation(energy, p)
        error = weights[perm // 2 != 0].sum()
        heat = weights @ energy[perm % 2] - p @ energy
        self.assertAlmostEqual(error, minimum_error, places=12)
        self.assertAlmostEqual(heat, minimum_heat_at_error, places=12)

    def test_nonzero_witness_on_coherent_near_erasure_outputs(self):
        rng = np.random.default_rng(20261028)
        beta = math.log(4)
        t0 = 2 * math.pi / beta
        positive_count = 0
        for delta in [0.0, 0.2]:
            energy, p = thermal_bath(paired_gaps(2, delta), beta)
            P = permutation_matrix(maximum_cooling_permutation(energy, p))
            for theta in [0.0, 0.07, 0.2]:
                X = rng.normal(size=P.shape) + 1j * rng.normal(size=P.shape)
                H = (X + X.conj().T) / 2
                H /= np.linalg.norm(H, ord=2)
                U = expm(1j * theta * H) @ P
                s = unitary_statistics(U, energy, p, beta, 2, t0)
                positive_count += s["witness"] > 1e-8
                self.assertGreaterEqual(s["witness_slack"], -2e-11)
                self.assertGreaterEqual(s["pinsker_slack"], -2e-11)
                self.assertLess(s["relative_entropy_identity_error"], 2e-11)
        self.assertEqual(positive_count, 6)

    def test_paired_spectral_product_against_full_spectrum(self):
        beta = math.log(4)
        t0 = 2 * math.pi / beta
        for n in [1, 2, 3, 4]:
            for delta in [0.0, 0.03, 0.2, 0.45]:
                _, p = thermal_bath(paired_gaps(n, delta), beta)
                actual = abs(characteristic(p, t0)) ** 2
                product = math.exp(paired_log_characteristic_sq(n, delta, beta))
                self.assertAlmostEqual(actual, product, places=12)

    def test_integer_binomial_expansion_at_every_lower_shell(self):
        valid = 0
        for m in [32, 64, 128, 256, 512]:
            for b in [0.3, 0.6, 1.0, 1.5]:
                k = selected_cutoff(m, b, "logarithmic")
                cert = cutoff_certificate(m, b, k)
                if cert is None:
                    continue
                counts = binomial_cumulative_integers(m)
                self.assertTrue(rank_condition(m, k, cert.r))
                for ell in range(k + 1):
                    self.assertGreaterEqual(counts[ell + cert.r], 2 * counts[ell])
                self.assertLessEqual(cert.binomial_tail,
                                     cert.hoeffding_tail_upper + 1e-12)
                valid += 1
        self.assertGreaterEqual(valid, 10)

    def test_cutoff_unitary_transfers_coherences_and_controls_reference_error(self):
        m, b, k, d = 6, 1.8, 1, 2
        cert = cutoff_certificate(m, b, k, d)
        self.assertIsNotNone(cert)
        perm = cutoff_permutation(m, k, d)
        excitation, p = rank_bath(m, b)
        D = len(p)
        R = sum(math.comb(m, ell) for ell in range(k + 1))
        reset_tensor = np.zeros((d, d, d, d), dtype=complex)
        for s in range(d):
            reset_tensor[0, 0, s, s] = 1
        # Verify the whole channel on each good bath input, not only populations.
        for j in range(R):
            np.testing.assert_array_equal(
                channel_tensor_for_bath_rank(perm, j, D, d), reset_tensor)
        tensor = channel_tensor(perm, p, d)
        tail = p[R:].sum()
        rng = np.random.default_rng(719231)
        for _ in range(24):
            psi = rng.normal(size=4) + 1j * rng.normal(size=4)
            psi /= np.linalg.norm(psi)
            rho = np.outer(psi, psi.conj())
            output = apply_channel_with_reference(tensor, rho, 2)
            target = apply_channel_with_reference(reset_tensor, rho, 2)
            distance = 0.5 * hermitian_trace_norm(output - target)
            self.assertLessEqual(distance, tail + 1e-12)
        stats = permutation_statistics(perm, excitation, p, b, d)
        self.assertLessEqual(stats["worst_input_beta_heat"], cert.beta_heat_upper + 1e-12)
        self.assertLessEqual(stats["actual_reset_error_maxmixed"], tail + 1e-12)

    def test_overflow_paths_never_raise_energy_for_three_level_memory(self):
        m, k, d = 10, 2, 3
        perm = cutoff_permutation(m, k, d)
        excitation, _ = rank_bath(m, 1.3)
        D = len(excitation)
        R = sum(math.comb(m, ell) for ell in range(k + 1))
        overflow = np.arange(R, d * R)
        self.assertTrue(np.all(excitation[perm[overflow] % D] <= excitation[overflow]))
        self.assertTrue(np.all(perm[overflow] // D > 0))
        self.assertTrue(np.all(perm[overflow] % D < R))

    def test_uniform_gamma_selector_with_tiny_gaps_and_large_m(self):
        for b in [1.0, 0.1, 0.01, 0.001]:
            for z_target in [25_000, 1_000_000]:
                m = math.ceil(z_target / (b * b))
                selected = explicit_proof_selector(m, b)
                self.assertIsNotNone(selected)
                cert, gamma = selected
                self.assertLessEqual(gamma, 0.5)
                self.assertTrue(rank_condition(m, cert.k, cert.r))
                self.assertLessEqual(cert.beta_heat_upper,
                                     math.log(2) / (1 - gamma) + b + 1e-12)

    def test_large_finite_bath_probability_bound_does_not_become_zero(self):
        cert = paired_certificate(10**12, 0.00035, math.log(4))
        self.assertTrue(cert["certified"])
        self.assertTrue(cert["inactive_pattern_upper_underflowed"])
        self.assertGreater(cert["inactive_pattern_probability_upper"], 0.0)
        self.assertLess(cert["inactive_pattern_log_probability_upper"], -1e9)
        self.assertGreater(cert["reset_error_upper"], 0.0)
        self.assertAlmostEqual(math.log(cert["reset_error_upper"]),
                               cert["reset_log_error_upper"], places=12)


if __name__ == "__main__":
    unittest.main()
