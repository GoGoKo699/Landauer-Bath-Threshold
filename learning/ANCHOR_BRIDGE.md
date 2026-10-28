# From quantum thermodynamics to the paired-bath threshold

[Learning guide](README.md) · [Milestones](MILESTONES.md) · [Model](../science/model.md) · [Threshold theorem](../science/theorem.md)

The educational anchor is **Sai Vinjanampathy and Janet Anders, “Quantum Thermodynamics”**, *Contemporary Physics* **57**(4), 545–579 (2016). This bridge uses **arXiv:1508.06099v2, revised 10 May 2016**: [version record](https://arxiv.org/abs/1508.06099v2), [official PDF](https://arxiv.org/pdf/1508.06099v2), and [published article](https://doi.org/10.1080/00107514.2016.1201896). All source page and equation numbers below refer to that 48-page author version. The bibliographic entry is [VA16](../references/LITERATURE.md#va16).

The project asks a precise attainability question. A memory must be reset using one prescribed finite thermal bath and a global unitary. As the bath grows, its individual qubit gaps become increasingly alike. Does the bath still permit reset at the Landauer heat, and how much variation must survive?

The review supplies the thermodynamic and channel language. The additional steps developed here connect that language to the spectral obstruction and the explicit bath construction. The detailed proofs have their authoritative homes in the [scientific account](../science/README.md).

<a id="reading-route"></a>
## 1. A focused route through the review

| Source location in VA16 | Use in this project | Next destination |
|---|---|---|
| Section 2.1, pp.3–5, Eqs.(1)–(8) | Translate energy, heat, work, temperature, and entropy into the bath-energy convention. | [M04](MILESTONES.md#m04), [M05](MILESTONES.md#m05) |
| Section 2.3, p.6, Eq.(10) | Identify the reset task and distinguish an entropy lower bound from attainability with a prescribed bath. | [M06](MILESTONES.md#m06), [M14](MILESTONES.md#m14) |
| Section 2.4, pp.6–7, Eq.(11) | Keep accessible side information separate from an untouched reference. | [M03](MILESTONES.md#m03), [M07](MILESTONES.md#m07) |
| Section 4.1, pp.17–20; especially Eq.(34) on p.18 and Eqs.(37)–(40) on pp.19–20 | Connect a reduced channel to its joint unitary implementation and introduce relative entropy. | [M07–M11](MILESTONES.md#m07) |

Within Section 4.1, the relevant sequence is the definition of a completely positive trace-preserving map, its unitary dilation, and the entropy inequalities. The general master-equation discussion provides broader context; the present argument works directly with one finite unitary and does not require a Markovian approximation.

The project-specific route then separates into the [spectral converse, M15–M19](MILESTONES.md#m15), the [compression construction, M20–M24](MILESTONES.md#m20), and the [physical paired-bath implementation, M25–M27](MILESTONES.md#m25).

<a id="conventions"></a>
## 2. Translate the conventions before calculating

### Heat, work, and entropy

The following translations keep the review's physical discussion compatible with the exact [project model](../science/model.md).

| Review notation or concept | Project convention |
|---|---|
| Internal energy $`U(\rho)=\mathrm{Tr}(\rho H)`$ | Use $`E_{\mathrm{int}}`$ when needed; $`U_N`$ denotes a unitary in the project. |
| Heat absorbed by the system, $`\langle Q\rangle`$ | $`Q_N`$ is the energy gained by the complete bath, positive for dissipation into it. |
| Work done on the system, $`\langle W\rangle`$ | Net mean work supplied to the complete memory–bath apparatus equals $`Q_N`$ under the stated boundary conditions. |
| $`\beta=1/(k_{\mathrm B}T)`$ | The same inverse temperature, fixed and strictly positive. |
| $`S(\rho)=-\mathrm{Tr}\rho\ln\rho`$ | The same dimensionless entropy in nats; $`S(I_d/d)=\ln d`$. |
| Relative entropy $`S[\rho\Vert\omega]`$ in Eq.(37) | $`D(\rho\Vert\omega)`$, also with natural logarithms. |
| Erased system $`S`$ and accessible memory $`M`$ in Section 2.4 | The erased memory is $`S`$; the bath is $`B`$. An optional reference $`R_{\mathrm{ref}}`$ is inaccessible to the operation. |

Thus the familiar qubit cost $`k_{\mathrm B}T\ln2`$ is $`\beta^{-1}\ln2`$, and $`\beta Q`$ is measured in the same entropy units as $`S`$.

The review's Eq.(2) splits a system's energy change into integrals involving changes of its state and Hamiltonian. The project instead defines heat operationally by the bath's endpoint energy increase:

```math
Q_N(\rho)
=
\mathrm{Tr}\!\left[
H_{B,N}\bigl(\sigma_{B,N}-\tau_{B,N}\bigr)
\right].
```

This has the sign of heat dissipated into the surroundings. Equating it with a particular integral for the memory alone would require compatible assumptions about the interaction and driving. The endpoint definition remains unambiguous here.

The memory Hamiltonian is zero at both endpoints, the bath Hamiltonian returns to its original value, and interactions are off at both endpoints. Therefore the change of the complete apparatus's energy is

```math
W_{\mathrm{on}}
=\Delta E_{SB}
=\Delta E_S+\Delta E_B
=Q_N.
```

The drive can act through the joint interaction during the protocol. A degenerate memory at the endpoints does not imply zero supplied work. The allowed unitary is globally driven and need not commute with the uncoupled Hamiltonian. No extra bath, catalyst, measurement record, or entropy-carrying controller is part of the apparatus. These assumptions define the resource model; a restriction to energy-conserving unitaries alone would define a different task.

### A channel description does not supply a free environment

The review's dilation formula, Eq.(34), has the form

```math
\Phi(\rho)
=
\mathrm{Tr}_E
\!\left[V(\rho\otimes\tau_E)V^\dagger\right].
```

For this project, $`E`$ must be the specified bath $`B`$, and $`\tau_E`$ must be its prescribed Gibbs state. The mathematical existence of a dilation of a channel does not imply its realizability with this particular bath.

This distinction already explains why exact reset is unavailable at any finite size. For a bath of dimension $`D_B`$, the initial state $`I_d/d\otimes\tau_B`$ has rank $`dD_B`$. A unitary preserves that rank. A joint state with a pure memory marginal has support inside $`|0\rangle_S\otimes\mathcal H_B`$, whose dimension is only $`D_B`$. Therefore exact reset of the maximally mixed memory is impossible when $`d\ge2`$. Vanishing error is a limit of finite protocols.

For channel calculations, the operator-sum convention is

```math
\Phi(\rho)=\sum_\mu K_\mu\rho K_\mu^\dagger,\qquad
\sum_\mu K_\mu^\dagger K_\mu=I.
```

The operator-sum form ensures complete positivity, and the normalization ensures trace preservation. A joint unitary with an initially independent bath gives both properties automatically.

### An untouched reference is not accessible side information

In the project, the operation on a possibly entangled input is $`U_{SB}\otimes I_{R_{\mathrm{ref}}}`$. Its ideal reduced action is

```math
(\mathcal R\otimes\mathrm{id})(\rho_{S R_{\mathrm{ref}}})
=
|0\rangle\langle0|_S\otimes\rho_{R_{\mathrm{ref}}},
\qquad
\mathcal R(X)=\mathrm{Tr}(X)|0\rangle\langle0|.
```

The reference checks that reset works even on correlated inputs. It is not available as a thermodynamic resource. This differs from the accessible side information in VA16 Section 2.4, where operations can exploit the correlations with the additional memory.

For example, resetting half of a Bell pair must produce a pure target on $`S`$ while leaving the other half's marginal equal to $`I/2`$. The initial correlations are transferred to the bath by the joint unitary. They are not consumed by manipulating the inaccessible reference.

<a id="exact-balance"></a>
## 3. From an entropy lower bound to an exact heat balance

The first additional step is an exact finite-bath identity. It is the link between the review's relative entropy and the project's heat objective.

Let $`\rho_S\otimes\tau_B`$ be the initial state and $`\sigma_{SB}=U(\rho_S\otimes\tau_B)U^\dagger`$ the final state. Since

```math
\ln\tau_B=-\beta H_B-\ln Z_B,
\qquad
S(\sigma_{SB})=S(\rho_S)+S(\tau_B),
```

expanding the relative entropy gives

```math
\begin{aligned}
D(\sigma_{SB}\Vert\sigma_S\otimes\tau_B)
&=-S(\sigma_{SB})+S(\sigma_S)
  +\beta\mathrm{Tr}(H_B\sigma_B)+\ln Z_B\\
&=\beta Q-\bigl[S(\rho_S)-S(\sigma_S)\bigr].
\end{aligned}
```

The reference bath in this expression is the **initial** Gibbs state. The final bath need not be thermal. For the maximally mixed memory,

```math
\boxed{\;
\Sigma
:=\beta Q-\ln d+S(\sigma_S)
=D(\sigma_{SB}\Vert\sigma_S\otimes\tau_B)
=I(S:B)_\sigma+D(\sigma_B\Vert\tau_B).
\;}
```

The equality and its attribution are given in [ELV10](../references/LITERATURE.md#elv10) and [RW14](../references/LITERATURE.md#rw14). The [canonical derivation](../science/spectral_obstruction.md#1-the-exact-entropy-balance) supplies the support details.

The two terms on the right account for final memory–bath correlations and bath disequilibrium. Dropping them gives the ordinary Landauer lower bound. Retaining them tells us what reversible erasure would require.

For target error $`\epsilon=1-\langle0|\sigma_S|0\rangle`$,

```math
S(\sigma_S)\le h_2(\epsilon)+\epsilon\ln(d-1),
```

so $`S(\sigma_S)\to0`$ when $`d`$ is fixed and $`\epsilon\to0`$. If simultaneously $`\beta Q\to\ln d`$, then $`\Sigma\to0`$. Quantum Pinsker's inequality in natural units gives

```math
\left\|\sigma_{SB}-\sigma_S\otimes\tau_B\right\|_1
\le\sqrt{2\Sigma}.
```

Thus Landauer saturation demands closeness of the **joint** final state to a product with the original bath, even while the bath dimension grows. The dimension-independent constant is essential. The relevant norm convention is recorded under [Pinsker](../references/LITERATURE.md#pinsker).

This is the transition from [M08–M09](MILESTONES.md#m08) to the spectral argument: a proposed reversible reset must respect both joint-state closeness and exact unitary preservation of eigenvalues.

<a id="spectral-witness"></a>
## 4. Detect the spectral mismatch

Unitary evolution preserves the spectrum of $`I_d/d\otimes\tau_B`$. Its nonzero eigenvalues are the bath eigenvalues divided by $`d`$, each repeated $`d`$ times. A pure target memory tensored with the original bath instead has the original bath eigenvalues and additional zeros.

In a growing bath these two patterns can sometimes become close. To detect when they cannot, use

```math
F_t(\rho)=\mathrm{Tr}\rho^{1+it}
=\sum_j\lambda_j e^{it\ln\lambda_j},
\qquad 0^{1+it}=0.
```

This is a probability-weighted phase sum: an eigenvalue $`\lambda_j`$ contributes phase $`t\ln\lambda_j`$ with weight $`\lambda_j`$. It is unchanged by a unitary and multiplies under tensor products. Consequently,

```math
F_t(I_d/d\otimes\tau_B)=d^{-it}F_t(\tau_B),
\qquad
F_t(|0\rangle\langle0|\otimes\tau_B)=F_t(\tau_B).
```

The mismatch is measurable only if a small trace-norm change cannot produce a large change in $`F_t`$. The required estimate is

```math
|F_t(\rho)-F_t(\omega)|
\le\sqrt{1+t^2}\,\|\rho-\omega\|_1.
```

Its proof combines the scalar derivative $`|(x^{1+it})'|=\sqrt{1+t^2}`$ with an ordered-eigenvalue perturbation inequality [Mirsky60](../references/LITERATURE.md#mirsky60). This is a trace-functional estimate; it does not assume an operator-Lipschitz theorem for matrix powers. The [spectral proof](../science/spectral_obstruction.md#2-a-dimension-independent-spectral-witness) handles zero eigenvalues and the reset-error term.

For a baseline gap $`\Delta`$, choose

```math
t_0=\frac{2\pi}{\beta\Delta},\qquad
\kappa=\frac{|1-d^{-it_0}|}{\sqrt{1+t_0^2}},\qquad
A_N=|F_{t_0}(\tau_{B,N})|^2.
```

Combining continuity with the heat identity yields

```math
\Sigma_N\ge\frac{A_N}{2}(\kappa-2\epsilon_N)_+^2.
```

Every joint unitary has the same initial spectral witness. This is why the conclusion applies to coherent protocols as well as population permutations.

For an exactly homogeneous Gibbs qubit, the phase difference at $`t_0`$ is $`2\pi`$, so the thermal phases align. A detuning $`\eta`$ changes its squared witness magnitude to

```math
|F_{t_0}(\tau_{\Delta+\eta})|^2
=
1-4p_\eta(1-p_\eta)
\sin^2\!\left(\frac{\pi\eta}{\Delta}\right).
```

Independent qubits contribute multiplicatively. For the paired bath and

```math
p=\frac1{1+e^{\beta\Delta}},\qquad
c_N=N(\delta_N/\Delta)^2\to c<\infty,
```

the product tends to

```math
A_N\longrightarrow e^{-8\pi^2p(1-p)c}>0.
```

The phase mismatch is nonzero exactly when $`\ln d/(\beta\Delta)\notin\mathbb Z`$. For example, $`d=2`$ and $`\beta\Delta=\ln4`$ give $`d^{-it_0}=-1`$. The witness then forbids Landauer saturation on every bounded-$`c_N`$ subsequence. It supplies a lower bound, not an exact optimum heat curve.

The complete argument is [M15–M19](MILESTONES.md#m15) and [spectral_obstruction.md](../science/spectral_obstruction.md). The construction must now show that divergence of $`c_N`$ is sufficient.

<a id="compression"></a>
## 5. Turn thermal state counts into a reset channel

Consider temporarily a bath of $`m`$ identical qubits with gap $`h`$. Put

```math
b=\beta h,\qquad
p_b=\frac1{1+e^b},\qquad
B_m(k)=\sum_{\ell=0}^k\binom m\ell.
```

Two quantities play different roles. $`B_m(k)`$ counts the number of available bath basis states below a cutoff; $`\Pr[\mathrm{Bin}(m,p_b)\le k]`$ gives their thermal probability. A large-dimensional subspace is useful only if it also contains sufficient probability.

If the good bath subspace has dimension $`R=B_m(k)`$, all memory inputs over it occupy $`dR`$ dimensions. Reset puts them in the one-dimensional memory target, so the bath must provide $`dR`$ distinguishable output states. To bound heat, require these output states to be close in energy as well. A sufficient finite certificate is

```math
\left(\frac{m-k-r+1}{k+r}\right)^r\ge d,
\qquad
k\ge0,\quad r\ge1,\quad k+r\le m.
```

It implies $`B_m(\ell+r)\ge dB_m(\ell)`$ for every $`\ell\le k`$. Thus every good input can be placed in the target-memory sector while increasing bath excitation by at most $`r`$. The construction includes a complete overflow permutation whose energy changes are nonpositive. Population rearrangement is a standard ingredient [AHJM11](../references/LITERATURE.md#ahjm11), [MMO16](../references/LITERATURE.md#mmo16); the exact finite certificate and completion are in [compression.md](../science/compression.md).

### Why the guarantee concerns a full channel

For each good bath basis state $`j`$, the permutation takes the entire memory subspace to

```math
|\psi\rangle_S\otimes|j\rangle_B
\longmapsto
|0\rangle_S\otimes V_j|\psi\rangle_B,
```

where $`V_j`$ is an isometry. All amplitudes, including correlations with an untouched reference, have a destination in the bath.

Let $`\eta_{\mathrm{cmp}}=\Pr[\mathrm{Bin}(m,p_b)>k]`$. Because the bath initially has a classical mixture of its energy eigenstates, the reduced channel has the exact form

```math
\mathcal C
=(1-\eta_{\mathrm{cmp}})\mathcal R
+\eta_{\mathrm{cmp}}\mathcal B
```

for some channel $`\mathcal B`$. The diamond distance between two channels is at most $`2`$, hence

```math
\frac12\|\mathcal C-\mathcal R\|_\diamond
\le\eta_{\mathrm{cmp}}.
```

This argument gives one input-independent error bound. Checking only the target population for $`I_d/d`$ would establish a weaker statement.

### Why the joint small-gap limit uses $`mb^2`$

The mean excitation number is $`mp_b`$, while the binomial counting distribution is centered at $`m/2`$. Their separation relative to a scale $`\sqrt m`$ is

```math
\frac{m(1/2-p_b)}{\sqrt m}
=\frac{\sqrt m}{2}\tanh\frac b2
\sim\frac{\sqrt{mb^2}}4
\qquad(b\to0).
```

This motivates the two requirements

```math
b\to0,\qquad z=mb^2\to\infty.
```

Small $`b`$ provides fine energy steps; large $`z`$ separates the thermally occupied region from the dimension-counting midpoint by many fluctuation widths. The rigorous joint-limit proof uses the exact thermal log odds and an explicit cutoff. It produces vanishing error and $`rb\to\ln d`$. Its constants and floor/ceiling estimates are given in [compression.md Section 6](../science/compression.md#6-an-explicit-parameter-choice), corresponding to [M24](MILESTONES.md#m24). The scale argument above explains the mechanism without replacing those uniform estimates.

<a id="worked-example"></a>
## 6. A complete finite virtual-bath example

This is a finite, imperfect reset on the virtual-qubit bath used by the compression step. Section 7 accounts separately for that bath's activity sectors inside the physical pairs.

Take a qubit memory and six bath qubits, with

```math
d=2,\qquad m=6,\qquad
\beta h=\ln4,\qquad p_b=\frac15,\qquad
k=1,\qquad r=1.
```

This uses the general finite certificate, which is valid for every positive $`b`$. The relevant counts are

```math
B_6(0)=1,\qquad B_6(1)=7,\qquad B_6(2)=22,
\qquad
\frac{6-1-1+1}{1+1}=\frac52\ge2.
```

The bath has $`64`$ basis states; the good subspace has rank $`R=7`$; its $`14`$ joint memory–bath input states fit within the target-memory sector.

### The whole permutation

Order bath ranks by excitation number. Rank $`1`$ has energy $`0`$, ranks $`2,\ldots,7`$ have energy $`h`$, and ranks $`8,\ldots,22`$ have energy $`2h`$.

For $`s\in\{0,1\}`$ and $`j=1,\ldots,7`$, set

```math
(s,j)\longmapsto(0,2j-1+s).
```

Complete the permutation with

```math
(0,7+q)\longmapsto(1,q),
\qquad q=1,\ldots,7,
```

and fix every remaining basis state. The good inputs occupy target ranks $`1,\ldots,14`$. The seven overflow inputs fill the seven non-target vacancies at bath ranks $`1,\ldots,7`$. This specifies all $`128`$ joint basis states.

A good input raises bath energy by at most $`h`$. Each overflow input starts at energy $`2h`$ and ends at energy $`0`$ or $`h`$. For a superposition on the memory at a good bath rank,

```math
(\alpha|0\rangle+\zeta|1\rangle)_S|j\rangle_B
\longmapsto
|0\rangle_S
\bigl(\alpha|2j-1\rangle+\zeta|2j\rangle\bigr)_B.
```

The reset transfers the amplitudes to orthogonal bath states.

### Error: distinguish a channel bound from a population value

Let $`w_\ell`$ be the probability of **one bath basis state** with $`\ell`$ excitations. In particular,

```math
w_0=\frac{4096}{15625},\qquad
w_1=\frac{1024}{15625},\qquad
w_2=\frac{256}{15625}.
```

There are six states in the one-excitation shell. Therefore the excluded probability is

```math
\eta_{\mathrm{cmp}}
=1-w_0-6w_1
=\frac{5385}{15625}
=0.34464.
```

The full channel obeys $`\tfrac12\|\mathcal C-\mathcal R\|_\diamond\le0.34464`$.

For a maximally mixed memory, the actual target-population error can also be counted. Non-target inputs on bad bath ranks contribute $`\eta_{\mathrm{cmp}}/2`$. The seven overflow inputs, each of bath probability $`w_2`$ and memory probability $`1/2`$, contribute another $`7w_2/2`$. Thus

```math
\epsilon
=\frac{\eta_{\mathrm{cmp}}}{2}+\frac{7w_2}{2}
=\frac{7177}{31250}
=0.229664.
```

The population error and the channel upper bound are different quantities.

### Heat: count every branch, including overflow

For memory input $`|0\rangle`$, three good one-excitation inputs gain $`h`$. The overflow inputs collectively lose $`8h`$, each weighted by $`w_2`$. For input $`|1\rangle`$, the zero-excitation input and four one-excitation inputs gain $`h`$. Hence

```math
\begin{aligned}
\frac{Q_0}{h}
&=3w_1-8w_2=\frac{1024}{15625},\\
\frac{Q_1}{h}
&=w_0+4w_1=\frac{8192}{15625},\\
\frac{Q(I_2/2)}{h}
&=\frac{Q_0+Q_1}{2h}
=\frac{4608}{15625}.
\end{aligned}
```

The energy-change operator is diagonal, so coherences in the input memory do not alter the heat. Therefore

```math
\begin{aligned}
\beta Q(I_2/2)
&=\frac{4608\ln4}{15625}
\approx0.408834843,\\
\sup_\rho\beta Q(\rho)
&=\frac{8192\ln4}{15625}
\approx0.726817498.
\end{aligned}
```

Both satisfy the uniform certificate $`\beta Q(\rho)\le rh\beta=\ln4`$. The stronger good-weight bound is $`\beta Q(\rho)\le(1-\eta_{\mathrm{cmp}})\ln4`$.

The mean cost for $`I_2/2`$ is below $`\ln2`$ because this is an imperfect reset. The appropriate finite-error lower bound is

```math
\beta Q(I_2/2)
\ge\ln2-h_2(0.229664)
\approx0.154277150.
```

Landauer saturation concerns the separate limit in which the error vanishes.

The numbers above can be reproduced with $`m=6`$, $`b=\ln4`$, $`k=1`$, and $`d=2`$ using `cutoff_certificate`, `cutoff_permutation`, `rank_bath`, and `permutation_statistics` in [compression.py](../src/landauer_bath/compression.py). They illustrate the capacity, completion, channel, and heat steps in [M20–M23](MILESTONES.md#m20).

<a id="paired-implementation"></a>
## 7. Obtain the virtual bath from the actual physical pairs

The physical bath supplies pairs with gaps $`\Delta+\delta_N`$ and $`\Delta-\delta_N`$. Its singly occupied subspace is spanned by $`|01\rangle`$ and $`|10\rangle`$, with energies

```math
\Delta-\delta_N,\qquad \Delta+\delta_N.
```

Inside this subspace the Hamiltonian is

```math
H_{\mathrm{pair}}\big|_{\mathrm{active}}
=(\Delta-\delta_N)I+2\delta_N n_{\mathrm v}.
```

The energy difference is $`h_N=2\delta_N`$. Dividing the two Gibbs probabilities gives $`e^{-2\beta\delta_N}`$, so the conditional state is exactly a thermal qubit at the original temperature. Virtual-qubit methods are an established ingredient [BLPS12](../references/LITERATURE.md#blps12).

A pair is active with probability

```math
a_N=p_+(1-p_-)+(1-p_+)p_-,
\qquad
p_\pm=\frac1{1+e^{\beta(\Delta\pm\delta_N)}}.
```

Consequently the number of active pairs obeys $`M\sim\mathrm{Bin}(N,a_N)`$. Choose $`m=\lfloor Na_N/2\rfloor`$. The inactive-sector error satisfies

```math
\Pr[M\lt m]\le e^{-Na_N^2/2}.
```

This is a concentration bound [Hoeffding63](../references/LITERATURE.md#hoeffding63), with all floor conditions given in [paired_bath.md](../science/paired_bath.md).

The word “conditional” describes the bath's decomposition into orthogonal sectors. The protocol itself is one direct-sum unitary. In each sector with enough active pairs, it applies compression to the first $`m`$ active pairs; in each remaining sector, it is the identity. The labels remain in the bath and are never measured or stored elsewhere.

The common sector energy offset remains unchanged, and unselected virtual qubits remain unchanged. Thus the complete physical heat is bounded by the virtual compression cost:

```math
\sup_\rho Q_N(\rho)\le2r\delta_N.
```

Both sources of error are retained:

```math
\eta_N
\le
\Pr[M\lt m]
+\Pr[\mathrm{Bin}(m,p_{h_N})>k].
```

This accounts for bad sectors through their probability instead of discarding them. The direct-sum construction, its exact channel decomposition, and its complete heat accounting are the content of [M25–M27](MILESTONES.md#m25).

<a id="threshold"></a>
## 8. Assemble the threshold and retain its scope

As $`\delta_N\to0`$,

```math
a_N\to2p(1-p)>0,\qquad
\frac mN\to p(1-p),\qquad
p=\frac1{1+e^{\beta\Delta}}.
```

The virtual gap and collective parameter therefore satisfy

```math
b_N=2\beta\delta_N\to0,\qquad
m b_N^2
\sim4(\beta\Delta)^2p(1-p)c_N.
```

If $`c_N\to\infty`$, the small-gap compression theorem applies and the inactive-sector probability vanishes. It constructs a universal reset channel with worst-input heat tending to $`\beta^{-1}\ln d`$. Evaluating the ordinary Landauer lower bound on $`I_d/d`$ supplies the matching lower limit.

Conversely, at nonresonance, any bounded subsequence of $`c_N`$ retains a positive spectral witness and hence a positive heat excess for every vanishing-error protocol. These two arguments prove the [three-way equivalence](../science/theorem.md#t1-exact-attainability-threshold) of ordinary Landauer attainability, $`c_N\to\infty`$, and universal-channel attainability with the same limiting worst-input heat.

The bath architecture, fixed $`d`$, $`\beta`$, and $`\Delta`$, global driving, and absence of additional entropy sinks are part of that statement. The necessary direction excludes the arithmetic resonances. The constructive direction uses the paired spectrum. Exact critical-window optimal heat and efficient local control are separate questions.

The distinction developed from the review's erasure discussion is between an entropy lower bound and an attainable operation with specified resources. The bath can have increasingly dense energy differences while retaining the spectral obstruction: the available virtual bandwidth scales as $`N\delta_N`$, while the occupied fluctuation scale is $`\sqrt N\,\delta_N`$. The [physical interpretation](../science/interpretation.md), [finite verification guide](../verification/README.md), and [M28–M30](MILESTONES.md#m28) connect this distinction to the theorem and its plotted certificates.
