# Verification and reproduction

[Home](../README.md) · [Claim map](CLAIMS.md) · [Data contracts](../results/README.md) · [Machine-readable summary](../results/summary.json)

The universal and asymptotic assertions are established by the [analytical proofs](../science/README.md). The numerical work checks independent finite consequences, the explicit permutation, and the implementation of the bounds. It also compares the lower bound with a finite population-constrained optimum. These are different kinds of evidence, with the distinctions retained in the tables and figures.

## Reproduce the checks

Use Python 3.11 or later. The committed results were generated with Python 3.12.14 and the exact package versions in [requirements.txt](../requirements.txt): NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8.

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/run_checks.py
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1`. No test-runner package is required: the suite uses Python's `unittest`.

The last command rewrites the six reference CSV tables, `results/summary.json`, and the two scientific SVG figures. To reproduce into an ignored directory while preserving the committed files:

```bash
python scripts/run_checks.py --output-dir results/generated --figures-dir results/generated/figures
```

The seed is `20261028`; additional finite tests use their explicitly recorded fixed seeds. Dependency versions and the environment are recorded in the summary. Floating-point residuals can differ across numerical-library versions and platforms, so scientific comparisons should use the stated tolerances rather than assume universal byte identity.

## What is checked

| Check | Independent comparison | Scientific purpose |
|---|---|---|
| Exact Landauer identity | Direct relative entropy versus heat and output entropy | Detect sign, partial-trace, and entropy-convention mistakes. |
| Finite spectral product | Explicit bath-spectrum moment versus the paired product formula | Check that the product is already the squared witness modulus. |
| Coherent-unitary converse | Entropy production versus the bound for coherent perturbations of cooling permutations, Haar unitaries, and controls | Exercise positive witness corrections as well as cases where the correction vanishes. |
| Finite population optimization | A doubly stochastic linear program, an explicitly attainable coherent interior point, and exhaustive four-dimensional permutation comparisons | Check the finite optimization and its unitary-orbit interpretation. |
| Complete compression permutation | Full basis bijection, energy changes, and the induced channel on each good bath basis state | Check the overflow completion and that the good branch resets the entire input space. |
| Reference correlations | Apply the full small-bath channel to sampled entangled inputs and compare trace distance with the bath-tail bound | Check channel-tensor and reference conventions; the all-input diamond bound follows from the channel decomposition proof. |
| Binomial expansion | Exact integer cumulative counts at every shell below accepted cutoffs | Check the finite rank certificate independently of logarithmic approximations. |
| Uniform explicit selector | Exact rank condition for small gaps and large virtual baths | Check representative cases of the selector used in the joint-limit proof. |
| Critical-window heat | Finite grouped rank sorting and independent quadrature of the limiting rank map | Check heat normalization, resonance, and convergence in representative critical-window baths. |

The implementation is split by role: [spectral.py](../src/landauer_bath/spectral.py), [compression.py](../src/landauer_bath/compression.py), and [optimization.py](../src/landauer_bath/optimization.py). The tests are in [test_scientific_checks.py](../tests/test_scientific_checks.py); [run_checks.py](../scripts/run_checks.py) generates the committed tables and figures.

## Critical-window heat

Run the [numerical check](../scripts/check_critical_heat.py) for the [critical-window theorem](../science/critical_heat.md) from the repository root.

```bash
python scripts/check_critical_heat.py
```

For each case, the script evaluates the Gaussian-smoothed counting function, inverts its rank map, and integrates the resulting displacement against the tilted Gaussian density. It also evaluates finite baths with $`N=24,96,256`$ pairs and $`\delta_N/\Delta=\sqrt{c/N}`$. The sorter uses $`(N+1)^2`$ occupation groups with exact binomial multiplicities. Each group represents bath states with a fixed number of excitations of each gap. The sorter matches blocks of Gibbs eigenvalues to blocks of output energies and accumulates heat and error without enumerating the bath basis.

The target-first order gives maximal target population and minimizes heat among permutations with that population. A second order minimizes $`\beta Q+\alpha L\epsilon`$ by adding $`L\Delta`$ to each output energy outside the reset target before sorting. Both sorts use the maximally mixed memory. The penalty calculation exercises the [finite variational bound](../science/critical_heat.md#an-energy-penalty-for-reset-failure). At a fixed integer $`L`$, the limiting penalized count multiplies the unpenalized count by $`1+(d-1)e^{-\alpha L}`$. The proof recovers the optimal heat by taking the large-bath limit and then sending $`L`$ to infinity.

| $`\alpha=\beta\Delta`$ | $`c`$ | Limiting $`\beta Q`$ | Target-first $`\beta Q`$ at $`N=256`$ | Limit with $`L=8`$ | Penalized objective at $`N=256`$ |
|---|---:|---:|---:|---:|---:|
| $`1`$ | 0.05 | 0.723139421 | 0.724972173 | 0.722830115 | 0.724645203 |
| $`1`$ | 0.10 | 0.707088725 | 0.709420789 | 0.706767663 | 0.709078348 |
| $`\ln 2`$ | 0.05 | 0.693147181 | 0.702200021 | 0.689294147 | 0.697797946 |

All three cases have $`d=2`$. The resonant example has $`\alpha=\ln 2`$ and limiting heat $`\ln 2`$. The [regression tests](../tests/test_critical_heat.py) compare the grouped sorts with the full basis for two bath pairs and memory dimensions two and three. They also check the three quadrature fixtures and their agreement with the large finite baths. The limiting theorem and the complete-channel guarantee follow from their analytical proofs.

## Reference run

The reference numerical normalization is $`d=2`$, $`\Delta=1`$, and $`\beta=\ln4`$. It is nonresonant because $`\ln2/(\beta\Delta)=1/2`$. Some permutation and integer-count rows additionally test $`d=3`$.

| Quantity | Reference result |
|---|---:|
| Explicit unitary cases | 42 |
| Cases with a positive spectral correction | 24 |
| Largest joint dimension in the unitary table | 128 |
| Largest entropy-identity residual | $`1.78\times10^{-15}`$ |
| Finite population-constrained LP instances | 32 |
| Smallest numerical optimum minus witness heat bound | $`0.0227`$ |
| Largest doubly stochastic constraint residual | $`5.55\times10^{-16}`$ |
| Enumerated cutoff permutations | 7 |
| Exact cumulative shell inequalities checked | 6,029 |

The least witness slack over all sampled unitaries is about $`-6.7\times10^{-16}`$, consistent with floating-point roundoff at a zero-slack control. All positive-correction cases have positive slack; the smallest is approximately $`0.154`$. The summary and raw tables retain the unrounded values.

## Reading the finite optimizer correctly

The LP minimizes bath heat for the input $`I_d/d`$ subject to a target-population error. Both are diagonal observables. The [Schur–Horn theorem](../references/LITERATURE.md#schurhorn) says that the possible output diagonals are exactly the vectors majorized by the initial spectrum. Equivalently, they are the images of that spectrum under doubly stochastic matrices. This makes the mathematical optimization exact over all joint unitaries for those two observables.

The transport matrix returned by the solver need not itself be unistochastic. Schur–Horn guarantees some unitary with the same output population vector, which is sufficient for this objective. It does not turn the calculation into a diamond-norm or universal-channel optimization. The reported optimum is numerical, with solver residuals, rather than a formal exact-arithmetic certificate. Finite error–heat optimization is established prior work [MMO16](../references/LITERATURE.md#mmo16).

## Reading the figures correctly

### Spectral obstruction

![Finite spectral witness and its collective-detuning limit](../science/figures/spectral_obstruction.svg)

The plotted quantity is $`W_N(0)=A_N\kappa^2/2`$, the zero-error intercept of the finite entropy-production lower bound. No finite full-rank bath permits an exact reset. Thus a plotted intercept is neither an attained finite-bath heat nor the optimal heat. Along vanishing-error sequences, its nonzero limit supplies the positive heat floor proved in [S1](../science/theorem.md#s1-finite-spectral-heat-bound).

The separate homogeneous marker is the known maximal-cooling asymptote from [AHJM11](../references/LITERATURE.md#ahjm11). At this normalization its excess is $`(\ln2)/3`$, larger than the witness intercept. It illustrates that the present lower bound need not be tight.

### Explicit constructive bounds

![Heat and channel-error upper bounds for a certified cutoff protocol](../science/figures/certified_construction.svg)

This figure takes $`\delta_N/\Delta=0.35N^{-1/4}`$. Every plotted protocol satisfies the finite integer rank-expansion criterion. The plotted heat is an upper bound for every memory input, and the plotted error bounds half the diamond distance from the pure replacement channel. These are protocol bounds, not an optimized finite frontier.

The main curve uses a less conservative cutoff than the selector chosen for the uniform proof. Its margin is $`t=\tfrac12\sqrt{\ln(1+z)}`$ in $`k=\lfloor mp_b+t\sqrt m\rfloor`$. The proof-style cutoff $`t=z^{1/4}`$ is shown separately. The finite rank condition is checked for each accepted point. A missing certificate indicates failure of that chosen cutoff/search, not a physical impossibility.

At the largest tabulated point, $`N=10^{12}`$, the main construction gives the evaluated bounds $`\beta Q\lesssim0.706456`$ and half-diamond error $`\lesssim0.002577`$, compared with $`\ln2\approx0.693147`$. This large bath size reflects a sufficient construction and conservative concentration bounds; it is not a lower bound on the resources of every possible protocol.

## Numerical limits

The large-bath calculations never enumerate their Hilbert spaces. Rank-expansion acceptance uses exact Python integer arithmetic. Gibbs occupations, binomial-tail evaluations, heat bounds, and concentration bounds use floating-point arithmetic. Positive analytic probability bounds are kept positive on underflow, with logarithmic values recorded where needed; none is presented as an exact zero error. This is not an interval-arithmetic verification of the transcendental factors.

The analytical arguments cover arbitrary bath size, all permitted unitaries, and all memory/reference inputs within the stated assumptions. The numerical checks cover the listed cases. The critical-window quadrature uses finite Gaussian and shell truncations, and the reported agreement is a floating-point diagnostic. Efficient gate synthesis, operation time, and generic-disorder sufficiency lie outside the verification scope.
