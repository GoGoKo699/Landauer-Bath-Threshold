# Related work and the scope of the threshold

[Home](../README.md) · [Theorem](../science/theorem.md) · [Source guide](LITERATURE.md) · [BibTeX](references.bib)

The question here is whether a **prescribed sequence of thermal baths** permits erasure at asymptotically reversible heat cost. The bath contains $`N`$ pairs with gaps $`\Delta\pm\delta_N`$, where $`\delta_N\to0`$. For a fixed maximally mixed $`d`$-level memory and a nonresonant baseline, the [threshold theorem](../science/theorem.md#t1-exact-attainability-threshold) identifies the necessary and sufficient condition

```math
N(\delta_N/\Delta)^2\longrightarrow\infty.
```

The scientific addition is the combination of a bound valid for **every allowed joint unitary** and a matching construction in this simultaneous limit. Finite-bath optimization, the Landauer identity, virtual qubits, and homogeneous-bath resonance are established ingredients.

## Foundations used by the proof

The exact entropy balance is inherited from [RW14](LITERATURE.md#rw14), with the earlier entropy-production formulation in [ELV10](LITERATURE.md#elv10):

```math
\beta Q-\ln d+S(\sigma_S)
=I(S:B)_\sigma+D(\sigma_B\Vert\tau_B)
=D(\sigma_{SB}\Vert\sigma_S\otimes\tau_B).
```

The [spectral obstruction](../science/spectral_obstruction.md) combines this identity with the ordered-eigenvalue trace-norm inequality [Mirsky60](LITERATURE.md#mirsky60) and quantum [Pinsker](LITERATURE.md#pinsker). Its additional step uses the unitary-invariant, tensor-multiplicative function $`F_t(\rho)=\mathrm{Tr}\rho^{1+it}`$ to detect a mismatch between the preserved joint spectrum and the spectrum required by reversible erasure. The scalar Lipschitz estimate is supplied in the proof; no operator-Lipschitz theorem is assumed.

The construction uses the established virtual-qubit perspective [BLPS12](LITERATURE.md#blps12) and binomial concentration [Hoeffding63](LITERATURE.md#hoeffding63). The new work is to arrange a complete permutation with a uniform heat bound in the joint small-gap, large-bath limit, and to implement it coherently inside the occupied sectors of the original paired bath.

## Homogeneous baths and finite-bath optimization

### [AHJM11]: the fixed-gap resonance is inherited

Allahverdyan, Hovhannisyan, Janzing, and Mahler analyze a reservoir of identical spins. Section VI.B, Eqs. (90), (93), and (94), gives the asymptotic work at maximal cooling and the special gap ratios at which the Landauer value is attained. Their degenerate-target specialization has no memory energy change, so its work is the bath heat. For a bit, the resonance is $`\ln2/(\beta\Delta)\in\mathbb Z`$. [AHJM11](LITERATURE.md#ahjm11)

That fixed-gap result is not a contribution of this repository. The present converse quantifies how a nonresonant obstruction survives individually vanishing detunings, without imposing maximal cooling at each finite bath size. The matching construction then identifies when those detunings suffice to remove the obstruction in the paired architecture. General fixed $`d`$ and the full two-parameter limit are included in the stated theorem.

### [MMO16]: the finite error–heat optimization is inherited

Mohammady, Mohseni, and Omar optimize over joint unitaries for finite-dimensional erasure. Section 2.4 and Theorem C.1 give the minimum-heat rule conditional on maximal reset probability. Section 2.5 and Theorem C.2 extend the analysis to the error–heat tradeoff through sequential swaps and partial swaps. Thus their result is broader than a maximum-cooling sorter. [MMO16](LITERATURE.md#mmo16)

The present contribution is not a new finite optimizer. It gives a uniform asymptotic criterion for a specified family of bath spectra, an explicit positive lower bound below its threshold, and a construction above it. Finite optimization provides useful context but does not by itself establish this simultaneous limit.

## Spectral requirements and controlled cooling

### [T23]: spectral shape and occupied weight already matter

Taranto and coauthors develop energy-gap variety, control complexity, and explicit cooling constructions. Their Appendix D4, Theorem 12, treats maximal cooling of an initially maximally mixed target. For the qubit case with even bath dimension $`D`$, its Eqs. (D23)–(D24) require the upper half of the bath spectrum to carry asymptotically all weight and

```math
\frac{\lambda_{\lfloor i/2\rfloor}
      +\lambda_{D/2+\lfloor i/2\rfloor}}
     {2\lambda_i}\longrightarrow1,
```

with the negligible-weight qualification discussed there. The end of D4 expressly distinguishes arbitrary near-perfect protocols. [T23](LITERATURE.md#t23)

This repository does not claim to discover spectral sensitivity or to refute that analysis. It supplies an explicit stability scale and a converse independent of the finite optimizer. The paired construction also explains why the thermally populated detuning width matters: dense or finely spaced formal gaps alone do not establish attainability for an arbitrary prescribed bath. A useful example is $`\delta_N=\Delta N^{-\alpha}`$ with $`1/2<\alpha<1`$: many-body gap spacing shrinks and the total detuning bandwidth grows, while the nonresonant heat floor persists.

### [T25]: optimized collision schedules use different controls

Taranto and coauthors derive finite-resource heat bounds using thermodynamic length. Their Theorem 1 assumes swaps with a fresh qudit machine, with an arbitrary machine Hamiltonian at each step; qubit optimality is developed in Appendix B1. Appendix C studies sorted and rescaled GOE-derived gap schedules. [T25](LITERATURE.md#t25)

Those controls permit engineering a sequence of machine gaps. Here the physical gaps are prescribed near one fixed value, all bath qubits are initially present, and no replacement or rethermalization is supplied during the protocol. The resulting threshold is a property of that restricted bath architecture.

### [LP25]: convergence-rate bounds do not decide attainability of a fixed bath family

Lipka-Bartosik and Perarnau-Llobet prove an inverse-size lower bound on entropy production for noninteracting reservoirs and construct interacting reservoirs with inverse-square convergence. Their framework permits engineering the reservoir Hamiltonian. [LP25](LITERATURE.md#lp25)

An inverse-size lower bound can vanish even for a particular bath family whose actual excess heat stays positive. The present theorem addresses this separate attainability question. It neither improves their optimal convergence rates nor compares interacting and noninteracting architectures.

## Recent finite-resource analyses

| Source | Established result relevant here | Distinction from this theorem |
|---|---|---|
| [X25](LITERATURE.md#x25) | Cooling with nonidentical thermal qubits; energetic criteria, reducibility, and perfect-matching descriptions of cooling operations. Appendix H includes cost optimization; Appendix I2 discusses lifting median degeneracies by small gap noise. | The threshold concerns vanishing error **and** vanishing excess heat for a prescribed shrinking-detuning sequence. It is not a statement about the cardinality of swappable sets or finite circuit optimization. |
| [N26](LITERATURE.md#n26) | Comparison of coarse-grained classical-bit and qubit erasure under finite control, energy, and interaction resources; the explicit model includes a work system and energy-conserving interactions. | The present theorem fixes a finite-dimensional memory and varies the spectral structure of one initially thermal bath under arbitrary joint driving. It makes no classical-versus-quantum implementation comparison. |

## Boundaries of the result

The matching necessity and sufficiency theorem is for the paired bath, fixed $`d,\beta,\Delta`$, individually vanishing detunings, and the stated nonresonance condition. The converse extends to more general product baths with bounded total squared detuning; a matching generic-disorder construction is not established. The results do not determine the exact optimal heat in the crossover, gate complexity, locality requirements, or the effect of catalysts, extra entropy sinks, and interactions.

This comparison records the specific primary results checked in the [source guide](LITERATURE.md), including recent versions available on 28 October 2026. It is not a claim that every conceivable neighboring formulation has been exhausted.
