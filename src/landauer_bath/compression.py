"""Finite cutoff compression and paired-bath certificates.

Large baths use an exactly checked integer rank-expansion condition and
analytic probability/heat bounds. Actual heat is evaluated only for the
explicit, enumerated small-bath permutations.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
import numpy as np
from scipy.special import expit
from scipy.stats import binom


def _exp_bound(log_value: float) -> float:
    """Keep positive analytic probability bounds positive on underflow.

    The formulas are analytic bounds; floating-point reporting is not an
    interval-arithmetic certification. One upward float step also avoids
    displaying a rounded-down zero as an exact finite-bath probability.
    """
    value = math.exp(min(0.0, log_value))
    return min(1.0, math.nextafter(value, math.inf))


@dataclass(frozen=True)
class CutoffCertificate:
    m: int
    b: float
    d: int
    k: int
    r: int
    log_rank_ratio_lower: float
    exact_integer_condition: bool
    beta_heat_upper: float
    binomial_tail: float
    hoeffding_tail_upper: float
    hoeffding_log_tail_upper: float
    hoeffding_upper_underflowed: bool

    def to_dict(self) -> dict:
        return asdict(self)


def rank_condition(m: int, k: int, r: int, d: int = 2) -> bool:
    """Exact integer check of ((m-k-r+1)/(k+r))**r >= d."""
    if d < 2 or m < 1 or k < 0 or r < 1 or k + r > m:
        return False
    return pow(m - k - r + 1, r) >= d * pow(k + r, r)


def log_rank_lower(m: int, k: int, r: int) -> float:
    if r < 1 or k < 0 or k + r > m:
        return -math.inf
    # Integer subtraction before float conversion avoids cancellation when
    # m is large and the two binomial fractions are both near one half.
    contrast = (m - 2 * k - 2 * r + 1) / (k + r)
    if contrast <= -1:
        return -math.inf
    return r * math.log1p(contrast)


def smallest_rank_shift(m: int, k: int, d: int = 2,
                        max_shift: int = 100_000) -> int | None:
    """Find the first certified r, or None within the explicit search cap.

    The function r log((m-k-r+1)/(k+r)) is strictly concave. Once it decreases
    below log(d), it cannot reach the threshold at a later r. A floating-point
    value only selects candidates; every accepted candidate is checked with
    integer arithmetic. The recorded benchmarks stay far below max_shift.
    """
    if m < 1 or k < 0 or k >= m or d < 2:
        return None
    previous = -math.inf
    for r in range(1, min(m - k, max_shift) + 1):
        value = log_rank_lower(m, k, r)
        if value >= math.log(d) - 1e-10 and rank_condition(m, k, r, d):
            return r
        if value <= 0 or value < previous - 1e-12:
            return None
        previous = value
    return None


def cutoff_certificate(m: int, b: float, k: int, d: int = 2,
                        r: int | None = None,
                        evaluate_binomial_tail: bool = True
                        ) -> CutoffCertificate | None:
    """A certificate for any chosen cutoff, not an optimal protocol search."""
    if m < 1 or b <= 0 or not 0 <= k < m or d < 2:
        return None
    if r is None:
        r = smallest_rank_shift(m, k, d)
    if r is None or not rank_condition(m, k, r, d):
        return None
    p = float(expit(-b))
    threshold_displacement = max(0.0, k + 1 - m * p)
    log_hoeffding = -2 * threshold_displacement ** 2 / m
    hoeffding = _exp_bound(log_hoeffding)
    tail = float(binom.sf(k, m, p)) if evaluate_binomial_tail else math.nan
    return CutoffCertificate(m=m, b=float(b), d=d, k=k, r=r,
                             log_rank_ratio_lower=log_rank_lower(m, k, r),
                             exact_integer_condition=True,
                             beta_heat_upper=r * b,
                             binomial_tail=tail,
                             hoeffding_tail_upper=hoeffding,
                             hoeffding_log_tail_upper=log_hoeffding,
                             hoeffding_upper_underflowed=math.exp(log_hoeffding) == 0)


def selected_cutoff(m: int, b: float, rule: str = "logarithmic") -> int:
    """Two valid asymptotic cutoffs with different finite conservatism.

    'proof' uses t=z**(1/4). 'logarithmic' uses t=.5 sqrt(log(1+z));
    both have t->infinity and t/sqrt(z)->0 when z=m b**2->infinity.
    The finite rank criterion is still checked, not presumed from this rule.
    """
    z = m * b * b
    if rule == "proof":
        t = z ** 0.25
    elif rule == "logarithmic":
        t = 0.5 * math.sqrt(math.log1p(z))
    else:
        raise ValueError("Unknown cutoff rule.")
    return math.floor(m * float(expit(-b)) + t * math.sqrt(m))


def explicit_proof_selector(m: int, b: float, d: int = 2
                             ) -> tuple[CutoffCertificate, float] | None:
    """Check the conservative finite gamma selector from compression.md.

    The return value contains the certificate and gamma. This checks the
    analytic selector; it does not replace its uniform proof.
    """
    if m < 1 or not 0 < b <= 1 or d < 2:
        return None
    z = m * b * b
    gamma = 6 * (z ** (-0.25) + (2 * math.log(d) + 1) / z)
    if gamma > 0.5:
        return None
    k = selected_cutoff(m, b, "proof")
    r = math.ceil(math.log(d) / (b * (1 - gamma)))
    cert = cutoff_certificate(m, b, k, d, r,
                              evaluate_binomial_tail=m <= 1_000_000)
    if cert is None:
        raise AssertionError("Explicit gamma selector failed its integer certificate.")
    return cert, gamma


def paired_certificate(n_pairs: int, delta: float, beta: float,
                       Delta: float = 1.0, d: int = 2,
                       cutoff_rule: str = "logarithmic") -> dict:
    if n_pairs < 1 or not 0 < delta < Delta or beta <= 0:
        raise ValueError("Invalid paired-bath parameters.")
    p_plus, p_minus = expit(-beta * np.array([Delta + delta, Delta - delta]))
    activity = float(p_plus * (1 - p_minus) + (1 - p_plus) * p_minus)
    m = math.floor(n_pairs * activity / 2)
    b = 2 * beta * delta
    z = m * b * b
    log_outer_tail = -n_pairs * activity * activity / 2
    outer_tail = _exp_bound(log_outer_tail)
    result = {"N_pairs": n_pairs, "delta": delta, "Delta": Delta,
              "beta": beta, "d": d, "activity_probability": activity,
              "m_virtual": m, "b_virtual": b, "z_virtual": z,
              "cutoff_rule": cutoff_rule,
              "inactive_pattern_probability_upper": outer_tail,
              "inactive_pattern_log_probability_upper": log_outer_tail,
              "inactive_pattern_upper_underflowed": math.exp(log_outer_tail) == 0,
              "certified": False, "k": None, "r": None,
              "beta_heat_upper": None, "reset_error_upper": None,
              "reset_log_error_upper": None,
              "log_rank_ratio_lower": None}
    if m < 1:
        return result
    k = selected_cutoff(m, b, cutoff_rule)
    cert = cutoff_certificate(m, b, k, d, evaluate_binomial_tail=False)
    if cert is None:
        return result
    log_total = min(0.0, float(np.logaddexp(log_outer_tail,
                                          cert.hoeffding_log_tail_upper)))
    result.update({"certified": True, "k": cert.k, "r": cert.r,
                   "beta_heat_upper": cert.beta_heat_upper,
                   "reset_error_upper": _exp_bound(log_total),
                   "reset_log_error_upper": log_total,
                   "virtual_log_probability_upper": cert.hoeffding_log_tail_upper,
                   "virtual_probability_upper_underflowed": cert.hoeffding_upper_underflowed,
                   "log_rank_ratio_lower": cert.log_rank_ratio_lower})
    return result


def binomial_cumulative_integers(m: int) -> list[int]:
    if m < 0 or m > 4096:
        raise ValueError("Exact cumulative-count checks are capped at m=4096.")
    counts = []
    total = 0
    for k in range(m + 1):
        total += math.comb(m, k)
        counts.append(total)
    return counts


def rank_bath(m: int, b: float) -> tuple[np.ndarray, np.ndarray]:
    """Rank-ordered bath excitation numbers and probabilities, m<=18."""
    if not 1 <= m <= 18 or b <= 0:
        raise ValueError("Require 1<=m<=18 and b>0 for enumeration.")
    excitation = np.concatenate([np.full(math.comb(m, k), k, dtype=np.int16)
                                 for k in range(m + 1)])
    logp = -b * excitation - m * np.logaddexp(0.0, -b)
    return excitation, np.exp(logp)


def cutoff_permutation(m: int, k: int, d: int = 2) -> np.ndarray:
    """Explicit input-to-output permutation, with the energy-safe overflow.

    Memory-major indexing: input index is s*D+j (zero-based bath rank j).
    The map exists when d*R<=D; a heat certificate requires rank_condition too.
    """
    if not 1 <= m <= 18 or not 0 <= k <= m or d < 2:
        raise ValueError("Invalid enumerated cutoff parameters.")
    D = 1 << m
    R = sum(math.comb(m, ell) for ell in range(k + 1))
    if d * R > D:
        raise ValueError("Target subspace too small for the selected cutoff.")
    perm = np.arange(d * D, dtype=np.int64)
    j = np.arange(R, dtype=np.int64)
    for s in range(d):
        perm[s * D + j] = d * j + s
    # Input (target, rank R+u) fills non-target vacancies in blocks of R.
    for s in range(1, d):
        perm[s * R + j] = s * D + j
    if len(np.unique(perm)) != d * D:
        raise AssertionError("Cutoff completion is not a permutation.")
    return perm


def permutation_statistics(perm: np.ndarray, excitation: np.ndarray,
                            bath_probabilities: np.ndarray, b: float,
                            d: int = 2) -> dict[str, float]:
    """Actual cost/error, not an upper-bound surrogate, for I_d/d input."""
    D = len(excitation)
    if len(perm) != d * D:
        raise ValueError("Dimension mismatch.")
    output_excitation = excitation[perm % D]
    input_excitation = np.tile(excitation, d)
    weights = np.tile(bath_probabilities / d, d)
    beta_heat = float(b * weights @ (output_excitation - input_excitation))
    error = float(weights[perm // D != 0].sum())
    input_specific_heat = [float(b * bath_probabilities @ (
        output_excitation[s * D:(s + 1) * D] - excitation))
                           for s in range(d)]
    return {"actual_beta_heat_maxmixed": beta_heat,
            "actual_reset_error_maxmixed": error,
            "worst_input_beta_heat": max(input_specific_heat),
            "minimum_input_beta_heat": min(input_specific_heat),
            "largest_pointwise_energy_increase_in_gap_units": int(
                np.max(output_excitation - input_excitation))}


def channel_tensor_for_bath_rank(perm: np.ndarray, bath_rank: int,
                                bath_dim: int, d: int = 2) -> np.ndarray:
    """Tensor M[a,b,s,t] such that Phi(|s><t|)[a,b]=M[a,b,s,t]."""
    result = np.zeros((d, d, d, d), dtype=complex)
    destinations = perm[np.arange(d) * bath_dim + bath_rank]
    for s in range(d):
        for t in range(d):
            if destinations[s] % bath_dim == destinations[t] % bath_dim:
                result[destinations[s] // bath_dim,
                       destinations[t] // bath_dim, s, t] += 1
    return result


def channel_tensor(perm: np.ndarray, bath_probabilities: np.ndarray,
                   d: int = 2) -> np.ndarray:
    D = len(bath_probabilities)
    result = np.zeros((d, d, d, d), dtype=complex)
    for j, probability in enumerate(bath_probabilities):
        result += probability * channel_tensor_for_bath_rank(perm, j, D, d)
    return result


def apply_channel_with_reference(tensor: np.ndarray, state: np.ndarray,
                                  reference_dim: int) -> np.ndarray:
    """Input/output order is memory tensor reference."""
    d = tensor.shape[0]
    rho = state.reshape(d, reference_dim, d, reference_dim)
    return np.einsum("abst,sutv->aubv", tensor, rho).reshape(
        d * reference_dim, d * reference_dim)
