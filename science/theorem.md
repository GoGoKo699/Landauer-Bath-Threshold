# Threshold theorem and finite certificates

[Home](../README.md) · [Model](model.md) · [Scientific route](README.md)

The statements below use the fixed parameters and complete resource boundary in the [model](model.md). The bath has $`N`$ pairs, so $`2N`$ physical qubits. All logarithms are natural.

## T1. Exact attainability threshold

Fix $`d\ge2`$, $`0<\beta<\infty`$ and $`\Delta>0`$, and let $`0<\delta_N<\Delta`$ tend to zero. Assume

```math
\frac{\ln d}{\beta\Delta}\notin\mathbb Z.
```

The following three statements are equivalent:

1. There exist allowed unitaries $`U_N`$ with $`\epsilon_N\to0`$ and $`\beta Q_N(I_d/d)\to\ln d`$.
2. The accumulated detuning diverges: $`c_N=N(\delta_N/\Delta)^2\longrightarrow\infty`$.
3. There exist allowed unitaries whose memory channels obey $`\eta_N\to0`$ and whose maximum input heat obeys $`\sup_{\rho_S}\beta Q_N(\rho_S)\longrightarrow\ln d`$.

The same construction proves $`2\Rightarrow3`$ without the nonresonance condition. The implication $`1\Rightarrow2`$ is the part that requires it.

### Proof and dependencies

The [spectral obstruction](spectral_obstruction.md) gives a strictly positive lower bound on the excess heat along every subsequence on which $`c_N`$ is bounded. If $`c_N`$ does not tend to infinity, it has such a subsequence. Therefore statement 1 implies statement 2.

For statement 2, the [paired-bath construction](paired_bath.md) finds a linear number of thermally occupied virtual qubits with gaps $`2\delta_N`$. The [small-gap compression theorem](compression.md) provides an input-independent permutation with vanishing channel error and a uniform heat upper bound tending to $`\ln d/\beta`$. The ordinary Landauer bound evaluated on $`I_d/d`$ gives the matching lower bound for the maximum over inputs. Thus statement 2 implies statement 3.

Finally, statement 3 implies statement 1: half-diamond convergence implies population convergence for $`I_d/d`$; its heat is at most the maximum input heat and is bounded below asymptotically by the Landauer identity.

The proofs establish the full joint limit $`N\to\infty`$, $`\delta_N\to0`$. They do not exchange two fixed-parameter asymptotic limits.

## S1. Finite spectral heat bound

Let

```math
t_0=\frac{2\pi}{\beta\Delta},\qquad
\kappa=\frac{|1-d^{-it_0}|}{\sqrt{1+t_0^2}},
\qquad p_\pm=\frac1{1+e^{\beta(\Delta\pm\delta_N)}}.
```

Define

```math
A_N=\left[
\left(1-4p_+(1-p_+)\sin^2\frac{\pi\delta_N}{\Delta}\right)
\left(1-4p_-(1-p_-)\sin^2\frac{\pi\delta_N}{\Delta}\right)
\right]^N.
```

For every allowed unitary,

```math
\boxed{
\beta Q_N\ge\ln d-h(\epsilon_N)-\epsilon_N\ln(d-1)
+\frac{A_N}{2}(\kappa-2\epsilon_N)_+^2,
}
\qquad (x)_+:=\max\{x,0\}.
```

This is a lower bound, not a formula for the optimal finite-bath heat. It applies to arbitrary coherent unitaries and does not assume the fastest or strongest possible cooling.

For $`p=(1+e^{\beta\Delta})^{-1}`$, if $`c_N\to c<\infty`$ and $`\epsilon_N\to0`$, then

```math
\boxed{
\liminf_N(\beta Q_N-\ln d)
\ge\frac{\kappa^2}{2}\exp[-8\pi^2p(1-p)c]>0.
}
```

The strict inequality uses nonresonance. In particular, the scale $`\delta_N\asymp\Delta/\sqrt N`$ still has a positive obstruction for any fixed finite asymptotic coefficient. The bound can be small, and no claim of tightness is made.

More generally, the same [spectral proof](spectral_obstruction.md) yields an obstruction for product baths with individually vanishing detunings and bounded total squared detuning. A matching construction is established here for the paired architecture only.

## C1. A finite compression certificate

Consider $`m`$ identical thermal qubits of gap $`h>0`$, with $`p_h=(1+e^{\beta h})^{-1}`$. Let

```math
B_m(k)=\sum_{\ell=0}^{k}\binom m\ell.
```

Suppose integers $`k_*\ge0`$ and $`r\ge1`$ satisfy $`k_*+r\le m`$ and

```math
\left(\frac{m-k_*-r+1}{k_*+r}\right)^r\ge d.
```

The [explicit permutation](compression.md) then resets the memory for every initial bath basis state of excitation number at most $`k_*`$, and obeys

```math
\frac12\|\mathcal C-\mathcal R\|_\diamond
\le\Pr[\mathrm{Bin}(m,p_h)>k_*],
\qquad
\sup_{\rho_S}Q(\rho_S)\le rh.
```

The ratio condition is a convenient sufficient certificate. The more general exact condition $`B_m(k+r)\ge d B_m(k)`$ for all $`0\le k\le k_*`$ is also sufficient. Neither condition claims to optimize a finite protocol.

The permutation includes its overflow completion. The completion moves displaced states to lower bath energy; it therefore avoids an extensive-energy penalty on a small bad tail.

## P1. From a virtual bath to the physical pairs

The probability that one pair has exactly one excitation is

```math
a_N=p_+(1-p_-)+(1-p_+)p_-.
```

Its conditional two-level state is Gibbs at the same inverse temperature with gap $`h_N=2\delta_N`$. Choose an integer $`m\le N`$ and a compression certificate for $`m`$ such virtual qubits. Conditional on an activity pattern with at least $`m`$ active pairs, use the first $`m`$ of them. Act as identity on the other activity patterns. This is a direct-sum unitary on the original bath; the pattern is not measured.

Writing $`M\sim\mathrm{Bin}(N,a_N)`$ and $`K\sim\mathrm{Bin}(m,(1+e^{2\beta\delta_N})^{-1})`$, the resulting physical channel has

```math
\eta_N\le\Pr[M\lt m]+\Pr[K>k_*],
\qquad
\sup_{\rho_S}Q_N(\rho_S)\le2r\delta_N.
```

For example, $`m=\lfloor Na_N/2\rfloor\ge1`$ gives

```math
\Pr[M\lt m]\le e^{-Na_N^2/2}.
```

Since $`a_N\to2p(1-p)>0`$, this choice is linear in $`N`$. The [uniform small-gap argument](compression.md) supplies suitable $`k_*`$ and $`r`$ whenever $`m(2\beta\delta_N)^2\to\infty`$, with $`2\beta r\delta_N\to\ln d`$. This proves the attainable half of T1.

## A dense-gap regime that still has excess heat

Choose $`\delta_N=\Delta N^{-\alpha}`$ for sufficiently large $`N`$. For $`1/2<\alpha<1`$, the excitation configurations inside the all-active sector have energy differences on the grid

```math
0,\;2\delta_N,\;4\delta_N,\;\ldots,\;2N\delta_N.
```

Its spacing tends to zero and its bandwidth tends to infinity, so available positive energy differences approximate every fixed bounded interval. Yet $`c_N=N^{1-2\alpha}\to0`$, and S1 gives a strictly positive excess for every vanishing-error protocol. This statement concerns energy differences, not a finite density of thermally occupied states in every such interval. The [physical interpretation](interpretation.md) explains the distinction.

## Attribution and scope

The Landauer identity, finite-bath cooling by spectral rearrangement, virtual-qubit methods and fixed-gap obstructions are established ingredients. The [comparison](../references/RELATED_WORK.md) identifies their sources. The additional theorem here is the collective shrinking-inhomogeneity threshold, with a uniform all-unitary converse and a construction in the stated resource model.

The threshold determines attainability in the limit. Exact optimal heat in the critical window, arbitrary unpaired-bath sufficiency, interactions and efficient control synthesis are separate questions. The finite bounds above support the stated theorem without resolving those questions.
