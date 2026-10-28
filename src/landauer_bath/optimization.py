"""Small-bath optimizers with explicit optimization contracts.

The LP optimizes mean heat on the maximally mixed memory for a target
population constraint. It is NOT a diamond-norm erasure optimizer.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix


def maximum_cooling_permutation(energies: np.ndarray,
                                 probabilities: np.ndarray, d: int = 2
                                 ) -> np.ndarray:
    """Permutation maximizing target population, then minimizing heat.

    Ky Fan selects the largest D eigenvalues for the target subspace. Sorting
    them by output energy, and separately sorting the remainder, minimizes
    heat among permutations with that maximal target population.
    """
    D = len(probabilities)
    eigenvalues = np.tile(probabilities / d, d)
    incoming = np.argsort(-eigenvalues, kind="stable")
    target = np.argsort(energies, kind="stable")
    other = np.arange(D, d * D)
    other = other[np.argsort(np.tile(energies, d - 1), kind="stable")]
    outgoing = np.concatenate((target, other))
    permutation = np.empty(d * D, dtype=np.int64)
    permutation[incoming] = outgoing
    return permutation


def permutation_matrix(permutation: np.ndarray) -> np.ndarray:
    n = len(permutation)
    if not np.array_equal(np.sort(permutation), np.arange(n)):
        raise ValueError("Not a permutation.")
    matrix = np.zeros((n, n), dtype=complex)
    matrix[permutation, np.arange(n)] = 1
    return matrix


def heat_population_optimum(energies: np.ndarray, probabilities: np.ndarray,
                            epsilon: float, d: int = 2) -> dict[str, float]:
    """All-unitary mean-heat optimum for one diagonal population constraint.

    Schur-Horn: attainable diagonals are precisely vectors majorized by the
    input spectrum. A doubly stochastic matrix parametrizes that polytope;
    not every such matrix is unistochastic, but every resulting diagonal is
    attainable by a unitary. Both cost and population are diagonal observables.
    This finite LP is intentionally capped at joint dimension 64.
    """
    D = len(probabilities)
    n = d * D
    if n > 64 or not 0 <= epsilon <= 1:
        raise ValueError("LP cap is joint dimension 64; epsilon must be in [0,1].")
    lam = np.tile(probabilities / d, d)
    out_energies = np.tile(energies, d)
    cost = (out_energies[:, None] * lam[None, :]).ravel()
    # Variables are B[output,input]. Rows and columns each sum to one.
    indices = np.arange(n * n).reshape(n, n)
    row_indices = np.concatenate((np.repeat(np.arange(n), n),
                                  np.tile(np.arange(n, 2 * n), n)))
    col_indices = np.concatenate((indices.ravel(), indices.ravel()))
    constraints = coo_matrix((np.ones(2 * n * n),
                              (row_indices, col_indices)),
                             shape=(2 * n, n * n)).tocsr()
    target = np.zeros((n, n))
    target[:D, :] = -lam
    result = linprog(cost, A_ub=target.reshape(1, -1),
                     b_ub=[-(1 - epsilon)], A_eq=constraints,
                     b_eq=np.ones(2 * n), bounds=(0, None), method="highs",
                     options={"dual_feasibility_tolerance": 1e-9,
                              "primal_feasibility_tolerance": 1e-9})
    if not result.success:
        raise RuntimeError(f"Population-constrained LP failed: {result.message}")
    B = result.x.reshape(n, n)
    diagonal = B @ lam
    actual_error = float(1 - diagonal[:D].sum())
    heat = float(out_energies @ diagonal - energies @ probabilities)
    return {"heat": heat, "actual_error": actual_error,
            "stochastic_residual": float(max(
                np.max(np.abs(B.sum(axis=0) - 1)),
                np.max(np.abs(B.sum(axis=1) - 1)))),
            "population_constraint_residual": max(0.0, actual_error - epsilon),
            "solver_iterations": int(result.nit)}
