# Thirty milestones for understanding the bath threshold

[Home](../README.md) · [Learning route](README.md) · [Anchor bridge](ANCHOR_BRIDGE.md) · [Scientific account](../science/README.md)

This map records the project's understanding targets and their scientific dependencies. The **single educational anchor** is Sai Vinjanampathy and Janet Anders, *Quantum Thermodynamics* (2016), [arXiv:1508.06099v2](https://arxiv.org/abs/1508.06099v2). The [bridge](ANCHOR_BRIDGE.md) translates its notation and connects its treatment to the present model.

The allocation is **14 background/preliminaries milestones and 16 narrative/innovation milestones**. The background must connect quantum states, thermal populations, heat, channel accuracy, spectral constraints, and probability before the apparatus and asymptotic question can be understood together. The narrative then develops two distinct proof branches—the obstruction and the construction—and joins them in the threshold theorem. Each phase progresses from individual objects and mechanisms to an integrated account. The map tracks global understanding; specialist calculations remain in the canonical proof pages.

## Source conventions

**VA16** below always means the selected version of the review. The relevant passages are:

| Review passage | Role in this project |
|---|---|
| [§2.1, pp. 3–5](https://arxiv.org/pdf/1508.06099v2#page=3) | Average energy, heat, work, and entropy. |
| [§2.3, p. 6](https://arxiv.org/pdf/1508.06099v2#page=6) | Reset and Landauer's principle, including finite-resource questions. |
| [§2.4, pp. 6–7](https://arxiv.org/pdf/1508.06099v2#page=6) | Erasure with accessible quantum side information. |
| [§4.1, pp. 17–20](https://arxiv.org/pdf/1508.06099v2#page=17) | Quantum channels, unitary dilation, relative entropy, and contractivity. |

An anchor pointer marked **context** supplies the physical or mathematical setting. The accompanying **project-supplied** pointer identifies an argument developed or explicitly imported in the repository's proofs. In particular, the review is not the source of the spectral witness, the compression certificate, or the collective-detuning threshold. Primary attributions remain in the [source guide](../references/LITERATURE.md).

<a id="background-preliminaries"></a>
## Background / preliminaries

M01–M14 assemble the objects, operational distinctions, and quantifiers needed to state the task precisely.

<a id="m01"></a>
### M01. Memory states and reset targets

**Central question:** What physical change counts as erasing a finite-dimensional memory?

- **Understanding target:** Distinguish a density matrix, a basis label, and a prescribed pure reset state; explain why the initially maximally mixed state $`I_d/d`$ represents the specified uncertain input.
- **Dependencies and story role:** No earlier milestone. Establishes the object that the rest of the apparatus acts on.
- **Conceptual connection:** Reset fixes the output state while transferring the input's information elsewhere in the joint system.
- **Source pointers:** VA16 §2.3; [memory and complete bath](../science/model.md#2-memory-and-complete-bath).

<a id="m02"></a>
### M02. Gibbs qubits and energy gaps

**Central question:** How do temperature and a qubit's gap determine its thermal populations?

- **Understanding target:** Relate a gap $`g`$ to $`p_g=(1+e^{\beta g})^{-1}`$, interpret $`\beta g`$ as dimensionless, and explain why finite temperature and finite gap give a full-rank state.
- **Dependencies and story role:** M01. Introduces the elementary bath component before combining components.
- **Conceptual connection:** The same gap determines both energy changes and the probabilities available to an erasure protocol.
- **Source pointers:** VA16 §§2.1 and 4.1, thermal-environment discussion after Eq. (34); [Gibbs bath definition](../science/model.md#2-memory-and-complete-bath).

<a id="m03"></a>
### M03. Composite states and correlations

**Central question:** What is specified by an initially independent memory and bath, and what can change under their interaction?

- **Understanding target:** Explain tensor-product preparation, reduced states obtained by partial trace, and the difference between a joint state and the product of its marginals. Track where memory–bath correlations can arise.
- **Dependencies and story role:** M01–M02. Builds the joint state space on which the allowed unitary acts.
- **Conceptual connection:** Local erasure is compatible with globally reversible dynamics because information can move into the bath and correlations.
- **Source pointers:** VA16 §§2.4 and 4.1, Eq. (34); [initial state and channel](../science/model.md#3-allowed-operation-and-resource-boundary).

<a id="m04"></a>
### M04. Heat, work, and global driving

**Central question:** Which energy change is counted, and what control is allowed to produce it?

- **Understanding target:** Identify heat as the complete bath's mean energy gain; explain why the degenerate memory and boundary conditions make net supplied work equal to that heat. Distinguish the allowed driven unitary from an energy-conserving operation on the uncoupled memory and bath.
- **Dependencies and story role:** M02–M03. Connects the joint dynamics to the physical objective.
- **Conceptual connection:** A heat bound depends on a specified apparatus and energy accounting, not just a state transformation.
- **Source pointers:** VA16 §2.1; [allowed operation](../science/model.md#3-allowed-operation-and-resource-boundary) and [heat convention](../science/model.md#4-heat-error-and-full-channel-accuracy).

<a id="m05"></a>
### M05. Entropy and the information to erase

**Central question:** Why does a maximally mixed $`d`$-level memory have an erasure scale of $`\ln d`$?

- **Understanding target:** Interpret von Neumann entropy as a function of state eigenvalues, compare the entropies of pure and maximally mixed states, and keep natural-log entropy distinct from entropy measured in bits.
- **Dependencies and story role:** M01 and M03. Introduces the information quantity whose reduction enters the heat balance.
- **Conceptual connection:** The dimension fixes the initial entropy, while the physical bath determines whether its removal can approach reversible cost.
- **Source pointers:** VA16 §2.1, Eq. (8), and §2.3; [entropy conventions](../science/model.md#5-entropy-and-the-heat-identity).

<a id="m06"></a>
### M06. Population error and finite-bath impossibility

**Central question:** Why is successful erasure expressed as a vanishing-error limit?

- **Understanding target:** Read $`\epsilon=1-\langle0|\sigma_S|0\rangle`$ as an error for a specified input. Explain the rank obstruction to exact reset with a finite full-rank bath and why fixed $`d`$ makes vanishing population error force vanishing output entropy.
- **Dependencies and story role:** M01–M02 and M04–M05. Makes the accuracy objective precise before strengthening it to a channel statement.
- **Conceptual connection:** Finite impossibility and asymptotic attainability are compatible statements about different quantifiers.
- **Source pointers:** VA16 §2.3; project-supplied [finite-rank limitation](../science/model.md#4-heat-error-and-full-channel-accuracy) and [population–entropy bound](../science/spectral_obstruction.md#1-the-exact-entropy-balance).

<a id="m07"></a>
### M07. Reset channels and untouched references

**Central question:** What does it mean for one device to reset every input, including an entangled input?

- **Understanding target:** Distinguish the population error on $`I_d/d`$ from the half-diamond distance to the replacement channel. Explain why an untouched reference tests channel accuracy without becoming an accessible erasure resource.
- **Dependencies and story role:** M03 and M06. Establishes the stronger objective achieved by the construction.
- **Conceptual connection:** Complete positivity concerns valid action on correlated inputs; reference-stable accuracy concerns closeness of that action to the desired reset.
- **Source pointers:** VA16 §4.1 and the contrasting accessible-side-information setting of §2.4; project-supplied [channel-accuracy definition](../science/model.md#4-heat-error-and-full-channel-accuracy).

<a id="m08"></a>
### M08. Relative entropy and irreversibility

**Central question:** How can a state comparison quantify the departure from reversible erasure?

- **Understanding target:** Distinguish $`S(\rho)`$ from $`D(\rho\Vert\omega)`$, recognize the reference state's role, and explain why correlation and bath disequilibrium are separate contributions to entropy production.
- **Dependencies and story role:** M03 and M05. Supplies the information quantities that connect local entropy change to joint-state constraints.
- **Conceptual connection:** The relevant comparison retains the original thermal bath state, even though the actual bath state changes.
- **Source pointers:** VA16 §4.1, Eqs. (37)–(40); [exact entropy balance](../science/spectral_obstruction.md#1-the-exact-entropy-balance).

<a id="m09"></a>
### M09. The exact Landauer balance

**Central question:** What must become small for a reset protocol to approach Landauer heat?

- **Understanding target:** Explain the identity $`\beta Q-\ln d+S(\sigma_S)=I(S:B)_\sigma+D(\sigma_B\Vert\tau_B)`$ and infer that vanishing error alone does not guarantee vanishing excess heat.
- **Dependencies and story role:** M04, M06, and M08. Integrates energy accounting with entropy and correlations.
- **Conceptual connection:** The Landauer inequality becomes an equality criterion whose failure can be detected by a spectral obstruction.
- **Source pointers:** VA16 §§2.1, 2.3, and 4.1 provide context; the exact identity and its primary attribution are in [spectral proof §1](../science/spectral_obstruction.md#1-the-exact-entropy-balance).

<a id="m10"></a>
### M10. Unitary spectra and population rearrangement

**Central question:** What freedom remains when a joint unitary preserves the state's eigenvalues?

- **Understanding target:** Separate eigenvalues from basis populations, explain how a permutation redistributes populations, and recognize the dimension constraint on placing several memory inputs into one target-memory sector.
- **Dependencies and story role:** M03–M05. Introduces the common spectral starting point of the converse and construction.
- **Conceptual connection:** A unitary can change local purity and bath energy while preserving the global spectrum; this is both a restriction and a constructive tool.
- **Source pointers:** VA16 §4.1 for unitary/channel context; project-supplied [spectral invariance](../science/spectral_obstruction.md#2-a-dimension-independent-spectral-witness) and [basis rearrangement](../science/compression.md#3-an-exact-permutation-on-the-full-hilbert-space).

<a id="m11"></a>
### M11. Trace distance and entropy bounds

**Central question:** How does a spectral mismatch become a quantitative entropy-production bound?

- **Understanding target:** Explain the roles of the trace norm, ordered-eigenvalue variation, and natural-log Pinsker inequality. Distinguish a scalar Lipschitz estimate for a traced spectral function from an operator-Lipschitz assertion.
- **Dependencies and story role:** M07–M08 and M10. Identifies the mathematical links needed to turn spectral information into heat.
- **Conceptual connection:** A dimension-independent estimate remains useful as the bath Hilbert space grows exponentially.
- **Source pointers:** VA16 §4.1 supplies relative-entropy context; the required norm inequalities and conventions are explicitly supplied in [spectral proof §§2–3](../science/spectral_obstruction.md#2-a-dimension-independent-spectral-witness).

<a id="m12"></a>
### M12. Thermal excitation counts and concentration

**Central question:** How are the number of bath states and their total thermal probability related?

- **Understanding target:** Distinguish the shell multiplicity $`\binom m\ell`$, cumulative dimension $`B_m(k)`$, and binomial thermal mass. Explain how a cutoff can include almost all probability while leaving enough higher-rank states for compression.
- **Dependencies and story role:** M02 and M10. Adds the counting and probability language required by the constructive branch.
- **Conceptual connection:** Dimension counts certify that an injection fits; concentration controls how often its good input sector occurs.
- **Source pointers:** VA16 §§2.3 and 4.1 provide context. The project supplies [shell counting](../science/compression.md#1-setting-and-finite-criterion) and [the concentration estimate](../science/compression.md#error-and-heat-with-this-choice).

<a id="m13"></a>
### M13. Joint limits and logical quantifiers

**Central question:** What must a proof establish when the bath grows while its local detunings shrink?

- **Understanding target:** Identify which parameters are fixed, distinguish a finite certificate from an asymptotic theorem, and explain why separate fixed-gap and fixed-size limits do not establish a result for every sequence $`\delta_N\to0`$.
- **Dependencies and story role:** M06, M09, and M12. Introduces the logical structure of necessity, sufficiency, and uniform control.
- **Conceptual connection:** A bounded subsequence can defeat claimed convergence, while a construction must eventually work along every permitted attainable sequence.
- **Source pointers:** VA16 §2.3 for finite-resource context; project-supplied [T1 and its quantifiers](../science/theorem.md#t1-exact-attainability-threshold).

<a id="m14"></a>
### M14. The complete prescribed-bath task

**Central question:** What single physical and mathematical question do the background ingredients define?

- **Understanding target:** Give a coherent account of the memory, $`N`$ physical pairs, product Gibbs input, allowed drive, complete-bath heat, two accuracy notions, fixed parameters, and nonresonance. Distinguish a prescribed bath spectrum from an independently engineered or refreshed reservoir.
- **Dependencies and story role:** M01–M13. Integrates the background into the exact task that the theorem answers.
- **Conceptual connection:** Reversible erasure requires compatibility between the apparatus, its thermally weighted spectrum, and the output-channel objective.
- **Source pointers:** VA16 §§2.1, 2.3–2.4, and 4.1; the complete [model](../science/model.md) and [threshold statement](../science/theorem.md#t1-exact-attainability-threshold).

<a id="narrative-innovation"></a>
## Narrative / innovation

M15–M19 build the obstruction. M20–M24 build a small-gap compression protocol. M25–M27 realize it inside the physical bath. M28–M30 combine the branches and interpret the result.

<a id="m15"></a>
### M15. A multiplicative spectral witness

**Central question:** Which spectral quantity can compare the preserved joint state with a reversibly erased state?

- **Understanding target:** Explain the unitary invariance and tensor multiplicativity of $`F_t(\rho)=\mathrm{Tr}\rho^{1+it}`$, including its values on a pure state and on $`I_d/d`$.
- **Dependencies and story role:** M10 and M14. Introduces the local mathematical mechanism of the converse.
- **Conceptual connection:** For a Gibbs bath, the witness's magnitude is an equilibrium energy characteristic function; choosing a frequency exposes residual spectral phase structure.
- **Source pointers:** VA16 §4.1 is the unitary-state context; the witness and its interpretation are project-supplied in [spectral proof §§2–3](../science/spectral_obstruction.md#2-a-dimension-independent-spectral-witness).

<a id="m16"></a>
### M16. Continuity and the memory mismatch

**Central question:** Why does a nearly reset memory retain a detectable mismatch with its initial maximally mixed spectrum?

- **Understanding target:** Follow the scalar derivative bound and ordered-eigenvalue inequality to a dimension-independent continuity estimate. Explain how population error bounds the memory witness and why the joint comparison carries the factor $`|F_t(\tau_B)|`$.
- **Dependencies and story role:** M06, M11, and M15. Turns an exact spectral invariant into a robust approximate-reset statement.
- **Conceptual connection:** Small reset error cannot remove a fixed spectral mismatch when the bath still has a nonvanishing phase signal.
- **Source pointers:** VA16 §§2.3 and 4.1 provide context; project-supplied [continuity and reset-error argument](../science/spectral_obstruction.md#2-a-dimension-independent-spectral-witness).

<a id="m17"></a>
### M17. The finite all-unitary heat bound

**Central question:** How does the mismatch constrain heat for every permitted unitary?

- **Understanding target:** Combine the witness, Pinsker, and the exact entropy balance to interpret the finite lower bound, its positive-part factor, and its output-entropy correction. Explain why no particular cooling optimizer or error-decay rate is assumed.
- **Dependencies and story role:** M09 and M16. Completes the general finite-bath converse before choosing a bath architecture.
- **Conceptual connection:** A spectral separation forces positive entropy production, which becomes excess heat when the output entropy vanishes.
- **Source pointers:** VA16 §§2.3 and 4.1 provide the thermodynamic context; project-supplied [finite-bath bound](../science/spectral_obstruction.md#3-finite-bath-heat-bound) and [S1](../science/theorem.md#s1-finite-spectral-heat-bound).

<a id="m18"></a>
### M18. Evaluating the paired-bath witness

**Central question:** How do near-equal physical gaps enter the general spectral bound?

- **Understanding target:** Explain the choice $`t_0=2\pi/(\beta\Delta)`$, the cancellation of the baseline phase, and the product of single-qubit factors. Recognize that $`A_N`$ is already a squared modulus and that nonresonance makes the memory mismatch nonzero.
- **Dependencies and story role:** M02, M14–M15, and M17. Specializes the general converse to the stated apparatus.
- **Conceptual connection:** Each small detuning weakly attenuates a bath phase signal; many independent factors accumulate.
- **Source pointers:** VA16 §4.1 for Gibbs-environment context; project-supplied [paired product evaluation](../science/spectral_obstruction.md#4-evaluation-for-the-paired-bath).

<a id="m19"></a>
### M19. Bounded detuning and the necessity direction

**Central question:** Why does bounded accumulated squared detuning rule out reversible erasure at nonresonance?

- **Understanding target:** Relate the logarithm of the bath product to $`c_N=N(\delta_N/\Delta)^2`$, explain the positive limiting heat floor when $`c_N`$ is bounded, and use a bounded subsequence to handle failure of divergence. Identify why the argument becomes inconclusive at resonance.
- **Dependencies and story role:** M13 and M17–M18. Completes the necessary half of the threshold.
- **Conceptual connection:** The relevant stability scale depends on thermally weighted phase accumulation, not merely on the number of distinct energy differences.
- **Source pointers:** VA16 §2.3 supplies finite-resource context; project-supplied [positive-floor argument](../science/spectral_obstruction.md#bounded-collective-detuning-leaves-a-positive-floor) and [resonance qualification](../science/spectral_obstruction.md#resonance-is-an-actual-exception).

<a id="m20"></a>
### M20. Capacity for small-gap compression

**Central question:** When can all memory inputs over a chosen bath sector fit into the reset sector?

- **Understanding target:** Interpret $`B_m(\ell+r)\ge dB_m(\ell)`$ as a capacity statement and explain how the binomial ratio certificate guarantees it simultaneously below the cutoff. Keep the auxiliary small-gap bath distinct from the physical near-$`\Delta`$ bath.
- **Dependencies and story role:** M10, M12, and M14. Opens the constructive branch with a finite, checkable condition.
- **Conceptual connection:** An entropy-removing transformation requires enough bath basis states at controlled additional energy.
- **Source pointers:** VA16 §2.3 for erasure context; project-supplied [finite criterion and counting proof](../science/compression.md#1-setting-and-finite-criterion). The [bridge](ANCHOR_BRIDGE.md) provides a complete finite example for M20–M23.

<a id="m21"></a>
### M21. Completing the permutation

**Central question:** How does an injection that resets good inputs become a unitary on the full apparatus?

- **Understanding target:** Track the good-input map, identify the displaced target-sector inputs, and explain how the overflow rule fills exactly the vacant output states. Account for all remaining basis states.
- **Dependencies and story role:** M20. Converts a dimension argument into a fully specified physical operation.
- **Conceptual connection:** A complete bijection preserves information globally; its completion also determines the energy cost on the exceptional inputs.
- **Source pointers:** VA16 §4.1 for unitary dynamics; project-supplied [complete basis permutation](../science/compression.md#3-an-exact-permutation-on-the-full-hilbert-space).

<a id="m22"></a>
### M22. A channel guarantee for the good sector

**Central question:** Why does the good-sector map erase coherent and reference-entangled inputs?

- **Understanding target:** Explain the bath isometry that stores the entire memory input while fixing its output to the target. Use the input-independent thermal weight of the good sector to obtain a channel mixture and the half-diamond error bound.
- **Dependencies and story role:** M07 and M21. Establishes the operational strength of the construction.
- **Conceptual connection:** Linearity on the whole memory subspace promotes successful basis-state reset to a reference-stable channel statement.
- **Source pointers:** VA16 §4.1, with §2.4 clarifying the different role of accessible side information; project-supplied [channel guarantee](../science/compression.md#4-channel-guarantee-including-a-reference).

<a id="m23"></a>
### M23. Uniform heat accounting

**Central question:** Why do rare bad inputs not produce an uncontrolled heat contribution?

- **Understanding target:** Explain the branchwise upper bound $`rh`$, the nonpositive heat of overflow branches, and the diagonal energy-change operator. Infer a heat upper bound for every memory input, including coherent inputs.
- **Dependencies and story role:** M04 and M20–M21. Completes the finite protocol's energy guarantee.
- **Conceptual connection:** Controlling the completion point by point avoids multiplying a small failure probability by an extensive worst-case bath energy.
- **Source pointers:** VA16 §2.1 for average heat; project-supplied [uniform heat proof](../science/compression.md#5-a-uniform-heat-bound).

<a id="m24"></a>
### M24. The uniform small-gap limit

**Central question:** How can one choose a valid cutoff and energy shift throughout the joint limit?

- **Understanding target:** Explain the role of $`z=m(\beta h)^2`$, the exact thermal log-odds identity, and the explicit slack parameter. Connect concentration to vanishing channel error and the shift to $`\beta rh\to\ln d`$; use the maximally mixed input to identify the limiting maximum-input heat.
- **Dependencies and story role:** M12–M13 and M20, M22–M23. Turns the finite lemma into the uniform small-gap sufficiency result.
- **Conceptual connection:** Typical fluctuations must fit inside a weak thermal bias while leaving enough space to encode the memory.
- **Source pointers:** VA16 §§2.1 and 2.3 provide context; project-supplied [explicit selector](../science/compression.md#6-an-explicit-parameter-choice) and [joint limit](../science/compression.md#7-the-joint-small-gap-limit).

<a id="m25"></a>
### M25. Virtual qubits inside physical pairs

**Central question:** Where does the required small gap exist when every physical qubit's gap stays near $`\Delta`$?

- **Understanding target:** Identify $`|01\rangle`$ and $`|10\rangle`$ as a two-level sector with gap $`2\delta_N`$, derive its conditional thermal population ratio, and separate its Gibbs state from its probability of occupation.
- **Dependencies and story role:** M02–M03 and M14. Locates the small-gap resource within the specified physical bath.
- **Conceptual connection:** Small energy differences between composite states can supply a thermal qubit without adding a new physical subsystem.
- **Source pointers:** VA16 §§2.1 and 4.1 supply composite/Gibbs-state context; the virtual-sector calculation and primary attribution are in [paired-bath proof §1](../science/paired_bath.md#1-one-physical-pair).

<a id="m26"></a>
### M26. Coherent activity-sector control

**Central question:** How can the protocol use occupied virtual sectors without measuring which sectors are present?

- **Understanding target:** Interpret activity strings as labels of orthogonal subspaces, explain the direct-sum unitary, and account for both sectors with enough active pairs and sectors on which the operation is identity.
- **Dependencies and story role:** M04, M21, and M25. Embeds the compression operation into the complete physical Hilbert space.
- **Conceptual connection:** A predetermined block-dependent unitary uses the bath's internal structure without creating a measurement record or granting fresh thermal resources.
- **Source pointers:** VA16 §4.1 for unitary dilation context; project-supplied [sector decomposition](../science/paired_bath.md#2-an-orthogonal-sector-decomposition-of-the-whole-bath) and [global unitary](../science/paired_bath.md#3-one-global-unitary).

<a id="m27"></a>
### M27. A finite paired-bath certificate

**Central question:** How do sector availability, compression error, and physical heat combine into one finite guarantee?

- **Understanding target:** Explain the two failure probabilities and why they bound channel error. Show why preserved sector offsets cancel from the complete-bath energy change and why a linear number of active virtual qubits is available with high probability.
- **Dependencies and story role:** M12, M22–M24, and M26. Produces a finite physical protocol with both accuracy and heat bounds.
- **Conceptual connection:** The virtual description becomes thermodynamically meaningful only after its occupation probability and all physical energy offsets are accounted for.
- **Source pointers:** VA16 §§2.1 and 4.1 supply context; project-supplied [channel and heat accounting](../science/paired_bath.md#4-exact-channel-decomposition-and-heat-accounting), [activity tail](../science/paired_bath.md#5-an-explicit-bound-on-inactive-sectors), and [P1](../science/theorem.md#p1-from-a-virtual-bath-to-the-physical-pairs).

<a id="m28"></a>
### M28. The three-way threshold equivalence

**Central question:** Why are the scalar erasure task, diverging collective detuning, and universal reset-channel task equivalent?

- **Understanding target:** Explain each implication in T1, including $`m(2\beta\delta_N)^2\to\infty`$ on the constructive side and the maximally mixed input's role in fixing maximum-input heat. Locate nonresonance precisely in the necessity argument.
- **Dependencies and story role:** M14, M19, M24, and M27. Joins the two proof branches into the main result.
- **Conceptual connection:** The same collective scale controls the survival of the obstruction and the availability of useful small-gap compression.
- **Source pointers:** VA16 §2.3 supplies the erasure question; the equivalence is project-supplied in [T1](../science/theorem.md#t1-exact-attainability-threshold) and the [paired joint limit](../science/paired_bath.md#7-sufficiency-in-the-joint-limit).

<a id="m29"></a>
### M29. Dense gaps, finite curves, and physical meaning

**Central question:** What does the threshold reveal that formal gap density or a finite numerical plot cannot decide?

- **Understanding target:** Compare the bandwidth $`N\delta_N`$ with the fluctuation scale $`\sqrt N\delta_N`$ using $`1/2<\alpha<1`$. Distinguish a witness intercept, a numerical population optimum, and a constructive channel bound when reading the finite evidence.
- **Dependencies and story role:** M18–M19 and M27–M28. Connects the theorem to its physical interpretation and finite manifestations.
- **Conceptual connection:** Available transitions and thermally useful weight answer different questions; finite computations illustrate analytical claims under their own accuracy conventions.
- **Source pointers:** VA16 §2.3 for finite-resource context; project-supplied [dense-gap consequence](../science/theorem.md#a-dense-gap-regime-that-still-has-excess-heat), [interpretation](../science/interpretation.md), and [verification contracts](../verification/README.md#reading-the-figures-correctly).

<a id="m30"></a>
### M30. Contribution, scope, and synthesis

**Central question:** What complete conclusion follows, which ingredients support it, and where do its assumptions matter?

- **Understanding target:** Explain the physical question, both proof mechanisms, and the threshold in one connected account. Separate inherited entropy identities, sorting, virtual qubits, and maximal-cooling resonance results from the shrinking-detuning theorem. State the limits concerning resonance, unpaired spectra, exact crossover heat, and implementation resources.
- **Dependencies and story role:** M14 and M28–M29, drawing together the intervening proof branches. Integrates the complete scientific story.
- **Conceptual connection:** The result concerns reversible erasure with a prescribed, thermally occupied spectrum under a specified control model; its significance follows from that full combination of assumptions and conclusions.
- **Source pointers:** VA16 §§2.1, 2.3–2.4, and 4.1 frame the task; [T1 and scope](../science/theorem.md), [model](../science/model.md), [related work](../references/RELATED_WORK.md), and [claim-to-evidence map](../verification/CLAIMS.md) give the canonical synthesis.
