# Scientific account

[Home](../README.md)

This project asks when a bath made of increasingly similar thermal qubits can erase a memory reversibly. The main result identifies the collective detuning scale that separates Landauer attainability from a positive heat excess.

## Connected reading route

1. [Model and conventions](model.md) defines the apparatus, heat, population error, half-diamond error and fixed parameters.
2. [Threshold theorem](theorem.md) states the exact equivalence and the finite certificates used in its proof.
3. [Spectral obstruction](spectral_obstruction.md) derives a bound that applies to every global unitary.
4. [Small-gap compression](compression.md) constructs a complete permutation, including its heat-controlled overflow, and proves the uniform joint limit.
5. [Paired bath](paired_bath.md) embeds the compression into the thermally occupied one-excitation sectors without measurement or auxiliary memory.
6. [Physical interpretation](interpretation.md) explains why formal spectral density and thermodynamic reversibility are different requirements.

Each proof has one authoritative home. The theorem page collects its consequences without replacing the detailed arguments.

## Proof dependencies

| Claim | Main input | Authoritative proof |
|---|---|---|
| Finite all-unitary heat obstruction S1 | Unitary spectral invariance, eigenvalue trace-norm inequality, exact Landauer identity, Pinsker | [Spectral obstruction](spectral_obstruction.md) |
| Finite complete-channel compression C1 | Cumulative binomial dimensions and a completed basis permutation | [Compression](compression.md) |
| Uniform small-gap attainability | Exact thermal log-odds and a moderate-deviation cutoff | [Compression](compression.md) |
| Physical paired-bath realization P1 | Orthogonal activity sectors and a binomial occupation tail | [Paired bath](paired_bath.md) |
| Necessary-and-sufficient threshold T1 | S1, C1 and P1 | [Theorem](theorem.md) |
| Dense available gaps with finite heat excess | Virtual energy-difference grid and S1 | [Theorem](theorem.md#a-dense-gap-regime-that-still-has-excess-heat) |

For attribution and comparison, use [Related work](../references/RELATED_WORK.md) and the [source register](../references/LITERATURE.md). For numerical evidence, use [Verification](../verification/README.md). Finite computations inspect the stated formulas and constructions; the asymptotic and all-unitary quantifiers are supplied by the written proofs.
