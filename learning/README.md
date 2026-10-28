# Learning the collective Landauer threshold

[Home](../README.md) · [Source-to-project bridge](ANCHOR_BRIDGE.md) · [30 milestones](MILESTONES.md) · [Scientific account](../science/README.md)

Erasing a memory means returning it to one prescribed state whatever information it initially held. A unitary on the memory and its environment preserves the joint information, so the bath must receive what the memory loses. The familiar Landauer heat describes the reversible limit. This project asks whether a particular sequence of microscopic baths can reach that limit.

The bath consists of pairs of nearly identical thermal qubits. Their small differences in energy gap can become useful collectively. The learning route explains why the scale $`\sqrt N\,\delta_N`$ appears in both a universal obstruction and an explicit reset construction.

## One educational anchor

**Sai Vinjanampathy and Janet Anders, _Quantum Thermodynamics_.** *Contemporary Physics* **57**(4), 545–579 (2016). Use the [author version arXiv:1508.06099v2](https://arxiv.org/abs/1508.06099v2), dated 10 May 2016, for the section and page numbers in this route. The [publisher DOI](https://doi.org/10.1080/00107514.2016.1201896) identifies the journal article.

The focused source route uses §2.1 on heat, work, and entropy; §§2.3–2.4 on erasure and side information; and §4.1 on quantum maps and relative entropy. Read these alongside the bridge and the project's examples. The route does not require reading the entire review before approaching the result.

The review supplies the thermodynamic setting. The project supplies the precise bath architecture, spectral witness, complete compression permutation, and uniform joint-limit proof. The [source bridge](ANCHOR_BRIDGE.md) explains the notation and resource assumptions at that transition. Research papers and mathematical sources in [references/](../references/LITERATURE.md) retain their roles as attribution and proof dependencies.

## How the 30 milestones form one story

The [map](MILESTONES.md) defines the project's understanding targets and their dependencies for any reader. It has two phases:

| Phase | Milestones | Role in the story |
|---|---|---|
| [Background and preliminaries](MILESTONES.md#background-preliminaries) | M01–M14 | Connect states, Gibbs qubits, heat and control, entropy, channel accuracy, spectra, and concentration into the complete prescribed-bath task. |
| [Narrative and innovation](MILESTONES.md#narrative-innovation) | M15–M30 | Build the all-unitary obstruction and the complete compression separately, realize the compression in the physical pairs, and combine the results into the threshold and its meaning. |

The 14/16 allocation reflects the tools that must meet in this problem. The background ends by integrating its objects into one operational model. The narrative ends by integrating the two proof directions, prior-work attribution, and the limits of the result. Each milestone has a central question, an understanding target, dependencies, a conceptual connection, and source pointers.

## Reading routes

| Starting question | Route |
|---|---|
| How does ordinary erasure lead to this bath question? | [Source bridge](ANCHOR_BRIDGE.md), then [M01–M14](MILESTONES.md#background-preliminaries). |
| Why can a large bath retain a positive heat penalty? | [M15–M19](MILESTONES.md#m15), then the [spectral obstruction](../science/spectral_obstruction.md). |
| How can one unitary reset every memory input at bounded heat? | [M20–M24](MILESTONES.md#m20), then the [compression proof](../science/compression.md). |
| Where do the useful small-gap qubits come from? | [M25–M27](MILESTONES.md#m25), then the [paired-bath realization](../science/paired_bath.md). |
| What does the complete theorem establish? | [M28–M30](MILESTONES.md#m28), the [theorem](../science/theorem.md), and the [physical interpretation](../science/interpretation.md). |
| What do the figures and finite examples verify? | [Verification guide](../verification/README.md), [data contracts](../results/README.md), and [claim map](../verification/CLAIMS.md). |

## Conventions to carry through the route

$`N`$ counts pairs, so the bath has $`2N`$ physical qubits. The memory dimension $`d`$, inverse temperature $`\beta`$, and baseline gap $`\Delta`$ stay fixed. Heat is energy gained by the complete bath. Entropies use natural logarithms, and full-channel error is half the diamond distance to the pure replacement channel.

The necessity theorem excludes the stated resonances; the construction does not need that exclusion. Global driving is allowed, and no additional entropy-carrying ancilla is supplied. The specialist [model](../science/model.md) and [theorem](../science/theorem.md) remain the authoritative definitions and claims throughout the learning route.
