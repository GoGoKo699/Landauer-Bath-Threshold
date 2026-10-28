# Reproducible numerical artifacts

Run `python scripts/run_checks.py` from the repository root to regenerate these tables and the two SVG figures in `science/figures/`. Run `python -m unittest discover -s tests -v` for the small independent channel, unitary, LP, and integer-count checks. The tested dependency versions are in `requirements.txt` and `summary.json`. All random cases use fixed, recorded seeds.

The normalization is **memory dimension d = 2, physical gap Delta = 1, inverse temperature beta = ln(4)** unless a row explicitly specifies a three-level memory. All logarithms are natural. Quantities named `beta_heat` are dimensionless. The collective detuning is `c = N (delta/Delta)^2`, where N counts **pairs**, not individual physical bath qubits.

## What each table establishes

| File | Quantity and contract |
|---|---|
| `unitary_checks.csv` | Actual small-bath outputs of 42 prescribed unitaries: identity, maximal-cooling permutations, coherent perturbations of those permutations, and Haar samples. It compares the spectral witness with entropy production and independently evaluates the relative-entropy identity. These samples check implementation and expose nontrivial positive-witness cases; they do not prove an all-unitary theorem. |
| `finite_lp_frontier.csv` | Numerical minimum mean heat at a target-population error, starting from the maximally mixed memory. Schur–Horn makes the doubly stochastic diagonal optimization exact as a mathematical all-unitary optimization problem: every majorized output diagonal is realizable by a unitary, even though a particular transport matrix need not be unistochastic. The reported solver values are floating-point results with residuals, not formal exact certificates. This is not a diamond-error or universal-channel optimization. Finite sorting/majorization optimization is inherited methodology. |
| `cutoff_permutations.csv` | Enumerated, explicitly completed cutoff permutations. The actual maximally mixed input heat/error and worst-input heat are separate from the probability and energy bounds. These modest cases check indexing, coherence handling, and the energy-decreasing overflow completion; they are not asymptotic demonstrations. |
| `binomial_certificates.csv` | Exact integer checks of the cumulative shell inequalities at every shell below each selected cutoff. Separate `explicit_gamma_selector` rows check the conservative analytic selector with small gaps and large bath sizes, without enumerating those large baths. `verified_shell_count=0` identifies selector-only rows. |
| `threshold_curves.csv` | The zero-error intercept `W_N(0)` of the spectral entropy-production lower bound, along fixed collective-detuning curves and three shrinking-gap power laws. A finite full-rank bath cannot reset exactly. These intercepts display the asymptotic obstruction, not attained finite-bath heat or an optimal heat curve. |
| `construction_curves.csv` | Analytic heat and full-channel reset-error upper bounds for explicitly specified cutoff protocols. Every accepted rank-expansion condition is checked in integer arithmetic. `certified=false` means this selected cutoff/search did not produce a certificate; it is not an impossibility result. No many-body state enumeration is used here. |
| `summary.json` | Model normalization, software versions, seeds, check counts, numerical residuals, selected finite certificates, and the separately attributed homogeneous-bath comparison. |

## Finite construction choices

The primary plotted construction takes `delta = 0.35 N^(-1/4)` and `m = floor(N a_delta/2)` active virtual qubits. For `z = m (2 beta delta)^2`, it chooses the cutoff `k = floor(m p_b + t sqrt(m))` with `t = 0.5 sqrt(log(1+z))`. This grows more slowly than the convenient proof choice `t = z^(1/4)`, which is also tabulated. Both meet the asymptotic cutoff requirements; their finite validity is checked directly through the same rank-expansion criterion. The integer shift search is capped at 100,000; the recorded accepted shifts are much smaller.

The probability and energy formulas are analytic bounds evaluated with floating-point arithmetic, not an interval-arithmetic computation. Log probability bounds and underflow flags are retained. Positive ordinary-space probability bounds are floored at the smallest positive float on numerical underflow; sums are evaluated in the logarithmic domain. The recorded cutoff is an explicit integer k, and its tail bound uses the event `X >= k+1`. Since the finite lemma allows any such k, it does not require the floating selector to reproduce a symbolic floor exactly. Evaluating the thermal excitation probability and the probability formula still uses binary64 arithmetic.

The error formula is an upper bound on **half the diamond norm** to the pure replacement channel, including reference-entangled inputs. Large-bath heat columns are protocol upper bounds rather than actual optimized costs.

## Figures and non-tightness control

`spectral_obstruction.svg` plots the witness and its collective-detuning limit. Its separate point at c = 0 is the known homogeneous **maximal-cooling asymptotic excess** `(ln 2)/3` for this normalization, attributed to Allahverdyan et al., *Physical Review E* **84**, 041109 (2011), Sec. VI.B. This is not asserted to be the arbitrary-vanishing-error optimum. The witness at c = 0 is smaller; the plot does not claim a tight lower bound.

`certified_construction.svg` plots heat/error upper bounds from one explicit construction, with the more conservative proof cutoff shown separately for heat. It does not represent the optimal finite-bath heat-versus-error frontier.
