# A small-gap virtual bath inside the physical pairs

This page proves the achievable part of the [threshold theorem](theorem.md). It uses only the memory and the paired Gibbs bath specified in the [model](model.md). Each pair supplies a two-dimensional one-excitation sector with gap $`2\delta_N`$. A single block-diagonal unitary applies the [compression construction](compression.md) on sectors with enough active pairs.

Virtual two-level systems and their temperatures are established thermodynamic tools [[BLPS12]](../references/LITERATURE.md#blps12), [[T23]](../references/LITERATURE.md#t23). Here the decomposition gives an exact finite implementation on the prescribed bath, including the probability that too few such sectors are occupied.

Throughout the finite construction, fix $`N`$ and write $`\delta=\delta_N`$. The plus-gap qubit is the first entry in each pair's computational basis.

## 1. One physical pair

The pair Hamiltonian is

```math
H_{\mathrm{pair}}
=(\Delta+\delta)n_+
+(\Delta-\delta)n_-.
```

Its energy eigenstates separate into three orthogonal subspaces:

| Label | Physical states | Energy |
|---|---|---|
| $`0`$ | $`\lvert00\rangle`$ | $`0`$ |
| $`A`$ | $`\lvert01\rangle,\ \lvert10\rangle`$ | $`\Delta-\delta,\ \Delta+\delta`$ |
| $`2`$ | $`\lvert11\rangle`$ | $`2\Delta`$ |

Call a pair active when it lies in subspace $`A`$. Inside that subspace, identify

```math
|0\rangle_{\mathrm v}=|01\rangle,\qquad
|1\rangle_{\mathrm v}=|10\rangle,\qquad
h=2\delta.
```

Then

```math
H_{\mathrm{pair}}\big|_A
=(\Delta-\delta)I_A+h|1\rangle_{\mathrm v}\langle1|.
```

The common offset has no effect on conditional Gibbs probabilities. If

```math
p_\pm=\frac{1}{1+e^{\beta(\Delta\pm\delta)}},
```

the probability of the active sector is

```math
a_N=(1-p_+)p_-+p_+(1-p_-).
```

Conditional on that sector, the state is exactly a Gibbs qubit at the same inverse temperature:

```math
\tau_{\mathrm v}=\tau_h
=\mathrm{diag}(1-p_h,p_h),\qquad
p_h=\frac{1}{1+e^{\beta h}}.
```

Indeed, the ratio of the probabilities of $`|10\rangle`$ and $`|01\rangle`$ is $`e^{-2\beta\delta}=e^{-\beta h}`$.

For later reference, with $`q=e^{-\beta\Delta}`$,

```math
\begin{aligned}
Z_{\mathrm{pair}}
&=1+2q\cosh(\beta\delta)+q^2,\\
w_0&=Z_{\mathrm{pair}}^{-1},\\
a_N&=\frac{2q\cosh(\beta\delta)}{Z_{\mathrm{pair}}},\\
w_2&=\frac{q^2}{Z_{\mathrm{pair}}}.
\end{aligned}
```

These three probabilities sum to one.

## 2. An orthogonal sector decomposition of the whole bath

A label string $`\lambda\in\{0,A,2\}^N`$ specifies the subspace of every pair. Let $`M(\lambda)`$ be the number of active pairs and $`n_2(\lambda)`$ the number in state $`|11\rangle`$. There is a fixed tensor-product identification of the corresponding bath sector with $`M(\lambda)`$ virtual qubits, ordered by their physical pair indices.

Under this identification,

```math
\begin{aligned}
\mathcal H_B
&=\bigoplus_{\lambda\in\{0,A,2\}^N}\mathcal H_\lambda,\\
H_B\big|_{\mathcal H_\lambda}
&=E_\lambda I_\lambda
+h\sum_{i=1}^{M(\lambda)}n_i,\\
E_\lambda
&=M(\lambda)(\Delta-\delta)+2\Delta n_2(\lambda).
\end{aligned}
```

The bath Gibbs state has the direct-sum form

```math
\tau_{B,N}
=
\bigoplus_{\lambda\in\{0,A,2\}^N}
w_\lambda\,\tau_h^{\otimes M(\lambda)},\qquad
w_\lambda=\prod_{j=1}^N w_{\lambda_j},
```

where $`w_A=a_N`$ and a tensor product with zero active factors is one-dimensional. The label probabilities are normalized, $`\sum_\lambda w_\lambda=1`$.

The pairs are independent, so their activity indicators are independent Bernoulli variables. Consequently

```math
M\sim\mathrm{Bin}(N,a_N).
```

The strings $`\lambda`$ are labels of subspaces already present in the bath Hilbert space. No additional register is introduced to hold them.

## 3. One global unitary

Choose an integer $`1\le m\le N`$ and integers $`k,r`$ satisfying the [finite compression criterion](compression.md#1-setting-and-finite-criterion) for $`m`$ qubits with gap $`h=2\delta`$:

```math
0\le k\le m-1,\qquad
1\le r\le m-k,\qquad
\left(\frac{m-k-r+1}{k+r}\right)^r\ge d.
```

Let $`U_{m,k,r}`$ denote the complete compression permutation from that proof.

For each sector with $`M(\lambda)\ge m`$, select the first $`m`$ active pairs in physical index order. On this sector, apply $`U_{m,k,r}`$ to the memory and those $`m`$ virtual qubits, and act as identity on the other virtual qubits. On sectors with $`M(\lambda)<m`$, act as identity on the memory and the entire sector. Formally,

```math
U_N=\bigoplus_\lambda U_\lambda,\qquad
U_\lambda=
\begin{cases}
U_{m,k,r}\otimes I_{M(\lambda)-m},&M(\lambda)\ge m,\\
I_{S\otimes\mathcal H_\lambda},&M(\lambda)<m,
\end{cases}
```

with the first line written in the sector's fixed virtual-qubit coordinates.

Every block is unitary, and the blocks cover the whole memory–bath Hilbert space. Thus $`U_N`$ is one allowed global unitary. It preserves every sector label. The sector-dependent definition requires no measurement or external classical record: a direct sum specifies the action of a linear operator on orthogonal subspaces.

The construction may require elaborate global control. Its admissibility is the global-unitary assumption of the [model](model.md), not a statement about the efficiency of a local implementation.

## 4. Exact channel decomposition and heat accounting

Let

```math
\eta_{\mathrm{act}}=\Pr[M<m],\qquad
\eta_{\mathrm{cmp}}=\Pr[K>k],\qquad
K\sim\mathrm{Bin}(m,p_h).
```

In every sector with enough active pairs, the selected $`m`$ virtual qubits begin in exactly $`\tau_h^{\otimes m}`$ and are independent of the untouched virtual qubits. The induced memory channel is therefore the same compression channel $`\mathcal C`$ in every such sector. On every remaining sector it is the identity channel. Hence the physical memory channel obeys the exact equality

```math
\mathcal N_N
=(1-\eta_{\mathrm{act}})\mathcal C
+\eta_{\mathrm{act}}\mathrm{id}_S.
```

The compression proof gives $`\mathcal C=(1-\eta_{\mathrm{cmp}})\mathcal R+\eta_{\mathrm{cmp}}\mathcal B`$ for a channel $`\mathcal B`$. The weight of the replacement channel in the full protocol is consequently

```math
(1-\eta_{\mathrm{act}})(1-\eta_{\mathrm{cmp}}).
```

It follows that

```math
\boxed{\;
\begin{aligned}
\eta_N
:=\frac12\|\mathcal N_N-\mathcal R\|_\diamond
&\le1-(1-\eta_{\mathrm{act}})(1-\eta_{\mathrm{cmp}})\\
&\le\eta_{\mathrm{act}}+\eta_{\mathrm{cmp}}.
\end{aligned}
\;}
```

This is a channel statement and therefore includes arbitrary reference-entangled inputs.

For heat, the offset $`E_\lambda`$ is unchanged in every block because the unitary preserves $`\lambda`$. Untouched virtual qubits are also unchanged. The only energy change in a good sector is the energy change of its selected $`m`$ virtual qubits. Bad sectors have zero energy change. For every memory input $`\rho`$,

```math
Q_N(\rho)
=(1-\eta_{\mathrm{act}})Q_{m,k,r}(\rho)
\le rh=2r\delta.
```

In particular,

```math
\boxed{\;
\sup_\rho Q_N(\rho)\le2r\delta.
\;}
```

The equality before the bound concerns the complete physical bath energy, including the physical gaps close to $`\Delta`$. No energy has been omitted by calling the selected degrees of freedom virtual.

## 5. An explicit bound on inactive sectors

Choose

```math
m=\left\lfloor\frac{Na_N}{2}\right\rfloor
```

and assume $`m\ge1`$. Since $`\mathbb E M=Na_N`$, the event $`M<m`$ implies $`M<Na_N/2`$. Hoeffding's inequality [[Hoeffding63]](../references/LITERATURE.md#hoeffding63) gives

```math
\boxed{\;
\eta_{\mathrm{act}}
\le
\exp\!\left[-\frac{2(Na_N/2)^2}{N}\right]
=e^{-Na_N^2/2}.
\;}
```

The exact binomial tail may be used instead of this sufficient upper bound in finite calculations.

Define the baseline occupation and variance

```math
p=\frac{1}{1+e^{\beta\Delta}},\qquad v=p(1-p).
```

At fixed finite temperature and fixed baseline gap,

```math
a_N\longrightarrow 2v>0,\qquad
\frac mN\longrightarrow v>0
```

as $`\delta_N\to0`$. Thus the number of usable virtual qubits is linear in the number of physical pairs, while the probability of too few active pairs tends to zero exponentially in $`N`$.

## 6. A fully explicit finite upper certificate

For the choice of $`m`$ in the preceding section, set

```math
b=2\beta\delta_N,\qquad
z=mb^2,\qquad
L=\ln d,\qquad
\gamma=6\left[z^{-1/4}+\frac{2L+1}{z}\right].
```

Whenever

```math
m\ge1,\qquad 0<b\le1,\qquad \gamma\le\frac12,
```

the [explicit compression selector](compression.md#6-an-explicit-parameter-choice)

```math
k=\left\lfloor mp_h+z^{1/4}\sqrt m\right\rfloor,\qquad
r=\left\lceil\frac{L}{b(1-\gamma)}\right\rceil
```

satisfies the finite integer criterion. The resulting physical unitary therefore has

```math
\boxed{\;
\eta_N\le e^{-Na_N^2/2}+e^{-2\sqrt z},\qquad
\sup_\rho\beta Q_N(\rho)
\le\frac{\ln d}{1-\gamma}+b.
\;}
```

For finite instances, another pair $`k,r`$ satisfying the same finite criterion may give tighter error and heat bounds. The explicit selector is useful because its conditions eventually hold along every sequence in the attainable regime.

## 7. Sufficiency in the joint limit

Assume

```math
\delta_N\to0,\qquad
c_N=N\left(\frac{\delta_N}{\Delta}\right)^2\to\infty.
```

With $`m=\lfloor Na_N/2\rfloor`$,

```math
b=2\beta\delta_N\to0,\qquad
z=m(2\beta\delta_N)^2
\sim4(\beta\Delta)^2v\,c_N\to\infty.
```

The finite conditions in the preceding section hold for all sufficiently large $`N`$. Use the constructed unitary for those sizes and any allowed unitary, for example the identity, at the finitely many earlier sizes. Then $`\gamma\to0`$, both error terms tend to zero, and

```math
\eta_N\to0,\qquad
\limsup_N\sup_\rho\beta Q_N(\rho)\le\ln d.
```

For the maximally mixed input, channel convergence implies that the final memory entropy tends to zero. The exact Landauer identity [[RW14]](../references/LITERATURE.md#rw14) gives

```math
\liminf_N\beta Q_N(I_d/d)\ge\ln d.
```

Since the maximum input heat is at least the value for this input, the bounds combine to prove

```math
\boxed{\;
\eta_N\longrightarrow0,\qquad
\beta Q_N(I_d/d)\longrightarrow\ln d,\qquad
\sup_\rho\beta Q_N(\rho)\longrightarrow\ln d.
\;}
```

No nonresonance condition was used in this construction. Nonresonance is required for the [converse](spectral_obstruction.md), which excludes Landauer attainability when the accumulated squared detuning fails to diverge.

The theorem established here concerns the prescribed paired architecture. An arbitrary collection of slightly detuned qubits need not contain this exact positive-weight virtual bath, so the construction does not supply a sufficiency theorem for general disorder.
