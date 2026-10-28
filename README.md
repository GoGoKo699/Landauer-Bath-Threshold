# A Collective Threshold for Landauer Erasure

**How much variation between thermal bath qubits is needed to erase a memory reversibly?**

A bath can grow without bound while its microscopic spectrum continues to impose an excess heat cost. This project determines when vanishing differences between bath-qubit gaps remove that obstruction.

The bath contains $`N`$ pairs of independent thermal qubits. Each pair has gaps $`\Delta+\delta_N`$ and $`\Delta-\delta_N`$, with fixed $`\Delta>0`$ and $`\delta_N\to0`$. At a fixed positive temperature, a fixed $`d`$-level memory is reset by an arbitrary global unitary on the memory and the complete bath.

## Main result

Away from the explicitly stated resonances $`\ln d/(\beta\Delta)\in\mathbb Z`$, erasure with vanishing error and heat approaching $`k_{\mathrm B}T\ln d`$ is possible exactly when

```math
\boxed{N\left(\frac{\delta_N}{\Delta}\right)^2\longrightarrow\infty.}
```

Thus the collective scale $`\sqrt N\,\delta_N`$ determines attainability in this paired architecture. Here $`\beta=1/(k_{\mathrm B}T)`$, and $`N`$ counts pairs, not individual qubits.

| Local variation | Collective behavior | Consequence at nonresonance |
|---|---|---|
| $`\delta_N/\Delta\gg N^{-1/2}`$, with $`\delta_N\to0`$ | Accumulated squared detuning diverges | A complete reset channel reaches the Landauer heat in the limit. |
| $`\delta_N/\Delta\sim aN^{-1/2}`$, fixed $`a>0`$ | Finite collective detuning | A strictly positive excess heat persists. |
| $`\delta_N/\Delta\ll N^{-1/2}`$ | Accumulated squared detuning vanishes | A strictly positive excess heat persists. |

The [theorem](science/theorem.md) gives the exact quantifiers. Its converse applies to every allowed unitary, including coherent operations and protocols whose reset error vanishes arbitrarily slowly. Its construction resets arbitrary memory inputs, including reference-entangled inputs, and has a uniform heat upper bound. The limiting maximum-input heat is $`k_{\mathrm B}T\ln d`$.

## What establishes the threshold

**A spectral obstruction.** The unitary-invariant quantity $`\operatorname{Tr}\rho^{1+it}`$ detects residual spectral structure weighted by Gibbs probability. Combined with the exact Landauer identity and a dimension-independent continuity bound, it gives an explicit finite lower bound on excess heat. A bounded total squared detuning leaves a nonzero obstruction.

**A matching compression.** Each pair's one-excitation sector is a virtual thermal qubit with gap $`2\delta_N`$. A positive fraction of the pairs occupy these sectors. A single block-diagonal permutation uses them to reset the memory. Its overflow completion moves displaced states to lower bath energy, controlling heat even on the small tail that is not reset.

The [fixed-gap maximal-cooling asymptote and its resonances](references/RELATED_WORK.md), and thermal spectral rearrangement methods, are established prior work. The contribution here is the sharp collective threshold under shrinking local inhomogeneity, with a converse for arbitrary global unitaries and a matching joint-limit construction.

## Dense energy differences can still be insufficient

For $`\delta_N=\Delta N^{-\alpha}`$ with $`1/2<\alpha<1`$, available bath energy differences become dense on every fixed bounded interval: their spacing vanishes and their range diverges. Yet the excess heat remains positive. The distinction is between possible transitions and the thermally occupied spectral structure needed for reversible erasure. See the [physical interpretation](science/interpretation.md).

## Read the science

Start with the [scientific route](science/README.md) or go directly to the [model](science/model.md) and [exact statements](science/theorem.md).

| Question | Authoritative account |
|---|---|
| What apparatus and heat objective are allowed? | [Model and conventions](science/model.md) |
| What is the precise necessary-and-sufficient result? | [Threshold theorem](science/theorem.md) |
| Why does the obstruction cover every unitary? | [Spectral obstruction](science/spectral_obstruction.md) |
| How is the permutation completed, and why is its heat bounded? | [Small-gap compression](science/compression.md) |
| How does the physical bath supply the virtual qubits? | [Paired-bath construction](science/paired_bath.md) |
| Why does spectral density alone not suffice? | [Physical interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) and [source register](references/LITERATURE.md) |
| What can be reproduced numerically? | [Verification](verification/README.md) and [claim map](verification/CLAIMS.md) |

The [LLM reading guide](llms.txt) maps questions to these authoritative files.

## Reproduce the finite checks

From the repository root, with Python 3.11 or later:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/run_checks.py
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. The [verification guide](verification/README.md) explains the finite-unitary checks, optimization comparisons, exact permutation tests, binomial certificates, generated figures and committed reference outputs. The general theorem is established by the analytical proofs.

## Scope

The matching threshold concerns a paired, noninteracting bath at fixed positive temperature, with fixed memory dimension and baseline gap. The necessity statement excludes the stated resonances. A broader converse covers bounded squared perturbations of product baths; sufficiency for arbitrary unpaired spectra is not asserted.

Predetermined global driving is allowed. There is no additional entropy sink, catalyst, refreshed reservoir or measurement record. Circuit complexity, locality and operation time are separate resources. The finite critical-window bound is a lower bound, not an exact optimal heat curve.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The repository retains its [MIT License](LICENSE), copyright 2026 Ruge Lin. See [citation metadata](CITATION.cff) and the [source and assistance record](provenance/README.md).
