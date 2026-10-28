# Model, thermodynamic task and conventions

[Home](../README.md) · [Scientific route](README.md) · [Threshold theorem](theorem.md)

## 1. The physical question

A larger thermal reservoir can absorb a fixed amount of entropy with a smaller change in temperature. This familiar macroscopic argument does not by itself guarantee that a particular microscopic reservoir can erase information at the Landauer heat. The eigenvalues of the joint state are preserved by a unitary, and their arrangement can obstruct a reversible transformation even when the reservoir is large. The maximal-cooling heat law for identical thermal spins provides an established example [AHJM11].

Here the reservoir is made progressively closer to that identical-spin architecture as its size grows. We ask how much local variation must remain for reversible erasure to become possible. The result concerns a prescribed bath Hamiltonian and arbitrary global control of that bath together with a memory. It separates the availability of energy differences from their thermal occupation.

The literature and the distinction from existing fixed-gap and finite-machine results are discussed in [Related work](../references/RELATED_WORK.md). Citation identifiers refer to the [source register](../references/LITERATURE.md).

## 2. Memory and complete bath

Fix a memory dimension $`d\ge2`$, an inverse temperature $`0<\beta<\infty`$, and a baseline energy gap $`\Delta>0`$. These parameters do not vary with bath size. The memory Hamiltonian is zero at the beginning and end, and the reset target is a fixed unit vector $`|0\rangle_S`$.

For each positive integer $`N`$, the bath contains $`N`$ pairs of noninteracting qubits. Its Hamiltonian is

```math
H_{B,N}=\sum_{j=1}^{N}
\left[(\Delta+\delta_N)n_{j,+}
+(\Delta-\delta_N)n_{j,-}\right],
\qquad n=|1\rangle\langle1|,
```

where

```math
0<\delta_N<\Delta,\qquad \delta_N\longrightarrow0.
```

There are $`2N`$ physical bath qubits. The pair count $`N`$ is used throughout. The initial bath state is its Gibbs state,

```math
\tau_{B,N}=\frac{e^{-\beta H_{B,N}}}{Z_N}
=\bigotimes_{j=1}^{N}\tau_{\Delta+\delta_N}\otimes\tau_{\Delta-\delta_N},
\qquad
\tau_g=\operatorname{diag}(1-p_g,p_g),
\quad p_g=\frac1{1+e^{\beta g}}.
```

The bath is initially independent of the memory. In the mean-heat converse the memory starts in $`I_d/d`$. For the stronger channel statement it may be in any state, including a state entangled with an inaccessible reference; the bath remains independent of the memory and reference.

## 3. Allowed operation and resource boundary

One unitary $`U_N`$ acts on $`S B`$. Its induced memory channel is

```math
\mathcal N_N(\rho)
=\operatorname{Tr}_B\!\left[U_N(\rho\otimes\tau_{B,N})U_N^\dagger\right].
```

The unitary may depend on the known bath Hamiltonian, the temperature and the intended bath size. Predetermined external driving is allowed, so $`U_N`$ need not conserve the uncoupled energy. Interactions are off at the initial and final boundaries, and the bath Hamiltonian has the same value at both boundaries.

The complete finite apparatus in this model consists of the memory and the specified bath. There is no additional ancillary register, catalyst, refreshed reservoir, postselection or measurement record. A classical drive prescribes the unitary without carrying away entropy. A finite quantum model of that drive is a different resource specification.

The construction uses a global permutation of energy-basis states. Control time, circuit size, spatial locality and the cost of producing the drive are outside the heat objective. Thus the result is an attainability statement under global control, with no efficient implementation assertion.

## 4. Heat, error and full-channel accuracy

For a memory input $`\rho`$, heat is the mean increase in the energy of the entire bath:

```math
Q_N(\rho)=\operatorname{Tr}\!\left[
(I_S\otimes H_{B,N})U_N(\rho\otimes\tau_{B,N})U_N^\dagger
\right]-\operatorname{Tr}(H_{B,N}\tau_{B,N}).
```

Positive heat means that the bath gains energy. With the degenerate memory and boundary conditions above, the net mean supplied work equals this heat. This equality concerns the stated externally driven model; it does not price a separate controller.

For $`\rho=I_d/d`$, write $`Q_N=Q_N(I_d/d)`$ and define

```math
\epsilon_N=1-\langle0|\mathcal N_N(I_d/d)|0\rangle.
```

This is a population error for the specified initial memory. The stronger error convention is

```math
\eta_N=\frac12\|\mathcal N_N-\mathcal R\|_\diamond,
\qquad \mathcal R(X)=\operatorname{Tr}(X)|0\rangle\langle0|.
```

The factor $`1/2`$ is part of the convention. Diamond accuracy tests arbitrary memory inputs and their correlations with a reference. It implies $`\epsilon_N\le\eta_N`$. The construction establishes this stronger criterion directly; population accuracy of an arbitrary device is not used as a substitute for it.

Every finite Gibbs state here has full rank. Consequently a unitary on the finite memory and bath cannot reset a full-rank memory exactly. All perfect-reset statements refer to limits of finite protocols with vanishing error.

## 5. Entropy and the heat identity

All entropies and logarithms use natural units:

```math
S(\rho)=-\operatorname{Tr}\rho\ln\rho,\qquad
D(\rho\Vert\omega)=\operatorname{Tr}\rho(\ln\rho-\ln\omega).
```

Let $`\sigma_{SB}=U_N(I_d/d\otimes\tau_{B,N})U_N^\dagger`$ and $`\sigma_S=\operatorname{Tr}_B\sigma_{SB}`$. Unitary entropy preservation and the Gibbs form give the standard exact Landauer identity [RW14]:

```math
\Sigma_N:=\beta Q_N-\ln d+S(\sigma_S)
=D(\sigma_{SB}\Vert\sigma_S\otimes\tau_{B,N})\ge0.
```

The reference state on the right need not be the actual final product of marginals. It contains the original bath Gibbs state. The identity includes both final memory–bath correlation and bath disequilibrium.

Define the binary entropy in nats by

```math
h(x)=-x\ln x-(1-x)\ln(1-x),
\qquad 0\ln0:=0.
```

Dephasing in a basis containing the reset target and maximizing the remaining populations yields

```math
S(\sigma_S)\le h(\epsilon_N)+\epsilon_N\ln(d-1).
```

Hence every vanishing-error protocol has $`\liminf_N\beta Q_N\ge\ln d`$. The threshold theorem identifies when equality can be approached with this fixed bath architecture.

## 6. Collective scale and nonresonance

Use the dimensionless accumulated detuning

```math
c_N=N\left(\frac{\delta_N}{\Delta}\right)^2.
```

The threshold result assumes

```math
\frac{\ln d}{\beta\Delta}\notin\mathbb Z.
```

This is an explicit arithmetic condition on the fixed temperature, baseline gap and memory dimension. The known identical-spin resonance phenomenon [AHJM11] motivates retaining it. The necessity theorem makes no assertion at an excluded resonance. Sufficiency for $`c_N\to\infty`$ does not need nonresonance.

The [threshold theorem](theorem.md) quantifies over every sequence of allowed unitaries, and its achievable side supplies one sequence that works on the entire input space.
