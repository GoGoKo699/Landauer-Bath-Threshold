"""Spectral witness and small-Hilbert-space unitary checks.

Logarithms are natural. Heat is in the same energy units as the input gaps.
The witness bounds Sigma = beta Q - log(d) + S(output memory), not Q alone.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.special import expit, logsumexp


def paired_gaps(n_pairs: int, delta: float, Delta: float = 1.0) -> np.ndarray:
    if n_pairs < 1 or not 0 <= delta < Delta:
        raise ValueError("Require n_pairs >= 1 and 0 <= delta < Delta.")
    return np.tile([Delta + delta, Delta - delta], n_pairs)


def thermal_bath(gaps: np.ndarray, beta: float) -> tuple[np.ndarray, np.ndarray]:
    """Enumerate at most 20 qubits; return energies and Gibbs probabilities.

    Basis order is a tensor-product bit order. No sorting is implicit.
    """
    gaps = np.asarray(gaps, dtype=float)
    if beta <= 0 or np.any(gaps < 0) or len(gaps) > 20:
        raise ValueError("Positive beta, nonnegative gaps, at most 20 qubits.")
    energies = np.array([0.0])
    for gap in gaps:
        energies = np.concatenate((energies, energies + gap))
    logp = -beta * energies
    probabilities = np.exp(logp - logsumexp(logp))
    return energies, probabilities


def characteristic(probabilities: np.ndarray, t: float) -> complex:
    p = np.asarray(probabilities, dtype=float)
    p = p[p > 0]
    return complex(np.sum(p * np.exp(1j * t * np.log(p))))


def entropy(probabilities: np.ndarray) -> float:
    p = np.asarray(probabilities, dtype=float)
    p = p[p > 0]
    return float(-np.sum(p * np.log(p)))


def reset_entropy_bound(epsilon: float, d: int) -> float:
    """Maximum memory entropy under target-population error <= epsilon."""
    if d < 2 or not 0 <= epsilon <= 1:
        raise ValueError("Require d >= 2 and epsilon in [0,1].")
    e = min(float(epsilon), 1 - 1 / d)
    return entropy(np.array([1 - e, e])) + e * math.log(d - 1)


def spectral_witness(probabilities: np.ndarray, d: int, t: float,
                     epsilon: float) -> float:
    if d < 2 or not 0 <= epsilon <= 1:
        raise ValueError("Require d >= 2 and epsilon in [0,1].")
    phase = abs(1 - np.exp(-1j * t * math.log(d)))
    bracket = max(0.0, phase / math.hypot(1.0, t) - 2 * epsilon)
    return 0.5 * abs(characteristic(probabilities, t)) ** 2 * bracket ** 2


def paired_log_characteristic_sq(n_pairs: int, delta: float, beta: float,
                                  Delta: float = 1.0) -> float:
    """Log |F_t0(tau)|^2 without constructing the many-body spectrum."""
    if n_pairs < 1 or not 0 <= delta < Delta or beta <= 0:
        raise ValueError("Invalid paired bath parameters.")
    p = expit(-beta * np.array([Delta + delta, Delta - delta]))
    loss = 4 * p * (1 - p) * math.sin(math.pi * delta / Delta) ** 2
    return float(n_pairs * np.log1p(-loss).sum())


def paired_witness(n_pairs: int, delta: float, beta: float, d: int = 2,
                   Delta: float = 1.0, epsilon: float = 0.0) -> float:
    t0 = 2 * math.pi / (beta * Delta)
    phase = abs(1 - np.exp(-1j * t0 * math.log(d)))
    bracket = max(0.0, phase / math.hypot(1.0, t0) - 2 * epsilon)
    return 0.5 * math.exp(paired_log_characteristic_sq(
        n_pairs, delta, beta, Delta)) * bracket ** 2


def partial_trace_memory(rho: np.ndarray, d: int, bath_dim: int) -> np.ndarray:
    return np.trace(rho.reshape(d, bath_dim, d, bath_dim), axis1=1, axis2=3)


def hermitian_trace_norm(matrix: np.ndarray) -> float:
    h = (matrix + matrix.conj().T) / 2
    return float(np.abs(np.linalg.eigvalsh(h)).sum())


def unitary_statistics(unitary: np.ndarray, energies: np.ndarray,
                       probabilities: np.ndarray, beta: float, d: int,
                       t: float) -> dict[str, float]:
    """Check a coherent unitary on I_d/d tensor tau, including direct D.

    The reference product is output_memory tensor initial_bath. Direct relative
    entropy uses its logarithm, independently of the heat-entropy identity.
    """
    D = len(probabilities)
    if unitary.shape != (d * D, d * D):
        raise ValueError("Unitary dimension does not match memory and bath.")
    initial = np.tile(probabilities / d, d)
    sigma = (unitary * initial[np.newaxis, :]) @ unitary.conj().T
    sigma_s = partial_trace_memory(sigma, d, D)
    ev_s, vec_s = np.linalg.eigh((sigma_s + sigma_s.conj().T) / 2)
    if np.min(ev_s) <= 0:
        raise ValueError("Finite full-rank input should yield full-rank marginal.")
    log_s = (vec_s * np.log(ev_s)[np.newaxis, :]) @ vec_s.conj().T
    log_omega = np.kron(log_s, np.eye(D)) + np.kron(
        np.eye(d), np.diag(np.log(probabilities)))
    direct_D = float(np.dot(initial, np.log(initial))
                     - np.trace(sigma @ log_omega).real)
    heat = float(np.dot(np.diag(sigma).real, np.tile(energies, d))
                 - np.dot(probabilities, energies))
    S_s = entropy(ev_s)
    epsilon = float(1 - sigma_s[0, 0].real)
    sigma_production = beta * heat - math.log(d) + S_s
    omega = np.kron(sigma_s, np.diag(probabilities))
    trace_distance_norm = hermitian_trace_norm(sigma - omega)
    w = spectral_witness(probabilities, d, t, epsilon)
    return {
        "epsilon": epsilon, "heat": heat, "beta_heat": beta * heat,
        "memory_entropy": S_s, "sigma": sigma_production,
        "direct_relative_entropy": direct_D,
        "relative_entropy_identity_error": abs(direct_D - sigma_production),
        "trace_norm_to_product": trace_distance_norm,
        "pinsker_slack": direct_D - 0.5 * trace_distance_norm ** 2,
        "witness": w, "witness_slack": sigma_production - w,
        "unitarity_error": float(np.linalg.norm(
            unitary.conj().T @ unitary - np.eye(d * D), ord=2)),
    }
