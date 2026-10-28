# Spectral obstruction to reversible erasure

This page proves the converse in the [threshold theorem](theorem.md). It applies to every joint unitary allowed by the [model](model.md), including coherent transformations and protocols whose reset error tends to zero arbitrarily slowly. The argument uses the exact Landauer identity, a scalar spectral witness, and quantum Pinsker's inequality. It does not assume maximal cooling or solve the finite-bath optimization problem.

The finite converse is stated first for an arbitrary finite Gibbs bath. The paired bath is substituted only after that bound has been established.

## 1. The exact entropy balance

Let the initial memory state be $`I_d/d`$, let the bath be $`\tau_B=e^{-\beta H_B}/Z_B`$, and write

```math
\rho_0=\frac{I_d}{d}\otimes\tau_B,\qquad
\sigma_{SB}=U\rho_0U^\dagger,\qquad
\sigma_S=\mathrm{Tr}_B\sigma_{SB}.
```

The heat and target reset error for this input are

```math
Q=\mathrm{Tr}H_B(\sigma_B-\tau_B),\qquad
\epsilon=1-\langle0|\sigma_S|0\rangle.
```

All logarithms are natural. The bath has full rank because its dimension and inverse temperature are finite. Unitary invariance of entropy gives the exact identity

```math
\begin{aligned}
\Sigma
&:=\beta Q-\ln d+S(\sigma_S)\\
&=D\!\left(\sigma_{SB}\,\middle\|\,\sigma_S\otimes\tau_B\right)\\
&=I(S:B)_\sigma+D(\sigma_B\|\tau_B).
\end{aligned}
```

This is the standard equality form of Landauer's principle [[RW14]](../references/LITERATURE.md#rw14). To see it directly, expand the relative entropy using $`\ln\tau_B=-\beta H_B-\ln Z_B`$ and substitute $`S(\sigma_{SB})=\ln d+S(\tau_B)`$. The support of $`\sigma_{SB}`$ is contained in $`\mathrm{supp}(\sigma_S)\otimes\mathcal H_B`$, so the expression remains finite if the final memory is not full rank.

Define

```math
g_d(\epsilon)=h_2(\epsilon)+\epsilon\ln(d-1),\qquad
h_2(x)=-x\ln x-(1-x)\ln(1-x),
```

with $`0\ln0=0`$. Then $`S(\sigma_S)\le g_d(\epsilon)`$ for every $`0\le\epsilon\le1`$. Indeed, pinching between $`|0\rangle`$ and its orthogonal complement cannot decrease entropy; the entropy of the pinched state is at most $`h_2(\epsilon)+\epsilon\ln(d-1)`$.

Consequently any positive lower bound on $`\Sigma`$ becomes an explicit heat bound after subtracting $`g_d(\epsilon)`$.

## 2. A dimension-independent spectral witness

For real $`t`$, define

```math
F_t(\rho)=\mathrm{Tr}\rho^{\,1+it},\qquad
0^{\,1+it}:=0,\qquad
L_t=\sqrt{1+t^2}.
```

Functional calculus makes this definition unambiguous for positive semidefinite matrices. Four elementary properties will be used:

1. $`F_t`$ is invariant under unitary conjugation.
2. $`F_t(\rho\otimes\omega)=F_t(\rho)F_t(\omega)`$.
3. $`F_t(I_d/d)=d^{-it}`$ and $`F_t(P)=1`$ for every rank-one state $`P`$.
4. $`|F_t(\rho)|\le1`$ for every density matrix.

The required continuity estimate is

```math
\boxed{\;
|F_t(\rho)-F_t(\omega)|
\le L_t\|\rho-\omega\|_1 .
\;}
```

The constant is independent of the Hilbert-space dimension. Here is a precise justification. The scalar function $`f_t(x)=x^{1+it}`$, extended by $`f_t(0)=0`$, is continuous on $`[0,1]`$. On $`(0,1]`$,

```math
f_t'(x)=(1+it)x^{it},\qquad |f_t'(x)|=L_t.
```

Integration along a real interval gives $`|f_t(x)-f_t(y)|\le L_t|x-y|`$ for positive $`x,y`$; continuity gives the same inequality when one argument is zero.

Let $`\lambda_j^\downarrow(\rho)`$ and $`\lambda_j^\downarrow(\omega)`$ be eigenvalues in nonincreasing order, including zero eigenvalues in the common ambient space. The Hermitian eigenvalue perturbation inequality for the trace norm gives

```math
\sum_j
\left|\lambda_j^\downarrow(\rho)-\lambda_j^\downarrow(\omega)\right|
\le\|\rho-\omega\|_1 .
```

This standard matrix inequality follows from the majorization form of the Hermitian eigenvalue perturbation theorem; its precise convention and sources are recorded under [[Mirsky60]](../references/LITERATURE.md#mirsky60). Therefore

```math
\begin{aligned}
|F_t(\rho)-F_t(\omega)|
&\le\sum_j
\left|f_t(\lambda_j^\downarrow(\rho))
      -f_t(\lambda_j^\downarrow(\omega))\right|\\
&\le L_t\sum_j
\left|\lambda_j^\downarrow(\rho)-\lambda_j^\downarrow(\omega)\right|\\
&\le L_t\|\rho-\omega\|_1.
\end{aligned}
```

The estimate concerns the trace of a matrix function. No operator-Lipschitz estimate for $`\rho^{1+it}-\omega^{1+it}`$ is assumed.

### Reset error controls the memory witness

Since $`\lambda_{\max}(\sigma_S)\ge\langle0|\sigma_S|0\rangle=1-\epsilon`$, a projector $`P`$ onto a largest-eigenvalue eigenvector obeys

```math
\|\sigma_S-P\|_1
=2[1-\lambda_{\max}(\sigma_S)]\le2\epsilon.
```

The continuity estimate therefore yields

```math
|F_t(\sigma_S)-1|\le2L_t\epsilon.
```

Unitary invariance and multiplicativity now give

```math
\begin{aligned}
F_t(\sigma_{SB})
&=d^{-it}F_t(\tau_B),\\
F_t(\sigma_S\otimes\tau_B)
&=F_t(\sigma_S)F_t(\tau_B).
\end{aligned}
```

Applying the continuity estimate to these two joint states and then the reverse triangle inequality shows

```math
\left\|\sigma_{SB}-\sigma_S\otimes\tau_B\right\|_1
\ge
|F_t(\tau_B)|
\left(
\frac{|1-d^{-it}|}{\sqrt{1+t^2}}-2\epsilon
\right)_+,
```

where $`x_+=\max\{x,0\}`$.

## 3. Finite-bath heat bound

Quantum Pinsker's inequality with natural logarithms is

```math
D(\rho\|\omega)\ge\frac12\|\rho-\omega\|_1^2.
```

This convention is detailed in [[Pinsker]](../references/LITERATURE.md#pinsker). Combining it with the preceding estimates proves, for every real $`t`$ and every allowed joint unitary,

```math
\boxed{\;
\Sigma\ge
\frac12|F_t(\tau_B)|^2
\left(
\frac{|1-d^{-it}|}{\sqrt{1+t^2}}-2\epsilon
\right)_+^2 .
\;}
```

In particular,

```math
\boxed{\;
\beta Q\ge
\ln d-g_d(\epsilon)
+\frac12|F_t(\tau_B)|^2
\left(
\frac{|1-d^{-it}|}{\sqrt{1+t^2}}-2\epsilon
\right)_+^2 .
\;}
```

Both expressions are finite-size inequalities. There is no restriction on the rate at which $`\epsilon`$ may approach zero.

For a Gibbs bath the magnitude of the witness has a useful interpretation:

```math
F_t(\tau_B)
=Z_B^{-it}\mathrm{Tr}\!\left(\tau_B e^{-it\beta H_B}\right).
```

Thus $`|F_t(\tau_B)|`$ is the magnitude of the equilibrium characteristic function of the bath energy at frequency $`t\beta`$. The obstruction survives when the bath retains a nonzero spectral phase signal at a frequency that distinguishes a maximally mixed memory from a pure memory.

## 4. Evaluation for the paired bath

Adopt the notation of the [model](model.md). There are $`N`$ pairs with gaps $`\Delta+\delta_N`$ and $`\Delta-\delta_N`$, where $`\Delta>0`$ and $`\beta>0`$ are fixed, $`0<\delta_N<\Delta`$, and $`\delta_N\to0`$.

Set

```math
t_0=\frac{2\pi}{\beta\Delta},\qquad
\kappa=\frac{|1-d^{-it_0}|}{\sqrt{1+t_0^2}},\qquad
p_\pm=\frac{1}{1+e^{\beta(\Delta\pm\delta_N)}}.
```

For one Gibbs qubit whose gap is $`\Delta+\eta`$, write $`p_\eta=(1+e^{\beta(\Delta+\eta)})^{-1}`$. Direct calculation gives

```math
\begin{aligned}
|F_{t_0}(\tau_{\Delta+\eta})|^2
&=\left|(1-p_\eta)^{1+it_0}+p_\eta^{1+it_0}\right|^2\\
&=1-4p_\eta(1-p_\eta)\sin^2\!\left(\frac{\pi\eta}{\Delta}\right).
\end{aligned}
```

Here the relative phase is $`e^{-it_0\beta(\Delta+\eta)}`$; the baseline contribution $`e^{-it_0\beta\Delta}=1`$ drops out.

Define the nonnegative product

```math
\begin{aligned}
A_N
&:=|F_{t_0}(\tau_{B,N})|^2\\
&=\left[
\left(1-4p_+(1-p_+)\sin^2\frac{\pi\delta_N}{\Delta}\right)
\left(1-4p_-(1-p_-)\sin^2\frac{\pi\delta_N}{\Delta}\right)
\right]^N.
\end{aligned}
```

The finite converse becomes

```math
\boxed{\;
\beta Q_N(I_d/d)\ge
\ln d-g_d(\epsilon_N)
+\frac{A_N}{2}(\kappa-2\epsilon_N)_+^2 .
\;}
```

In this notation $`A_N`$ is already the squared modulus. No further square is applied to the product.

### Bounded collective detuning leaves a positive floor

Let

```math
p=\frac{1}{1+e^{\beta\Delta}},\qquad
v=p(1-p),\qquad
c_N=N\left(\frac{\delta_N}{\Delta}\right)^2.
```

If $`c_N\to c<\infty`$, then

```math
A_N\longrightarrow e^{-8\pi^2vc}.
```

For completeness, put $`x=\delta_N/\Delta`$ and $`v_\pm=p_\pm(1-p_\pm)`$. Smoothness in the detuning and symmetry imply $`v_++v_-=2v+O(x^2)`$. Since $`\sin^2(\pi x)=\pi^2x^2+O(x^4)`$ and $`\ln(1-y)=-y+O(y^2)`$,

```math
\ln A_N=-8\pi^2v\,Nx^2+O(Nx^4).
```

The remainder tends to zero because $`Nx^2`$ is bounded and $`x\to0`$. The implicit constants here depend only on the fixed $`\beta\Delta`$; the finite product above requires no expansion.

For every sequence of unitaries with $`\epsilon_N\to0`$,

```math
\boxed{\;
\liminf_{N\to\infty}
\left[\beta Q_N(I_d/d)-\ln d\right]
\ge
\frac{\kappa^2}{2}e^{-8\pi^2vc}.
\;}
```

The factor $`\kappa`$ is nonzero exactly when

```math
\frac{\ln d}{\beta\Delta}\notin\mathbb Z.
```

This is the nonresonance condition in the main theorem. If only $`C=\limsup c_N<\infty`$ is known, the same lower bound holds with $`c`$ replaced by $`C`$. If $`c_N`$ fails to diverge, it has a bounded subsequence and then a subsequence converging to some finite $`c`$. The positive floor on that subsequence rules out convergence of the heat to $`\beta^{-1}\ln d`$.

The worst-input heat is at least the heat for $`I_d/d`$. Moreover, the half-diamond distance from the pure replacement channel bounds the target error for this particular input. Thus the same necessity applies to the universal-reset formulation of the [threshold theorem](theorem.md).

### Resonance is an actual exception

When $`\ln d/(\beta\Delta)\in\mathbb Z`$, this witness has $`\kappa=0`$ and supplies no positive floor. For qubit erasure, the fixed-gap resonance mechanism and the exact homogeneous-bath heat law are already present in the identical-spin analysis of [[AHJM11]](../references/LITERATURE.md#ahjm11). The threshold theorem therefore excludes resonance from its necessity claim. It does not reinterpret a zero witness as a proof of reversibility for every perturbed sequence.

## 5. A finite extension to unpaired detunings

The obstruction itself does not require pairing. Consider any product of Gibbs qubits with gaps $`\Delta+\eta_j`$ and assume

```math
|\eta_j|\le\frac{\Delta}{4}.
```

At the same frequency $`t_0`$,

```math
|F_{t_0}(\tau_B)|^2
=\prod_j
\left[
1-4p_j(1-p_j)\sin^2\!\left(\frac{\pi\eta_j}{\Delta}\right)
\right].
```

Each subtracted quantity lies in $`[0,1/2]`$. Using $`\ln(1-x)\ge-2x`$ on this interval, $`4p_j(1-p_j)\le1`$, and $`|\sin x|\le|x|`$ gives the explicit estimate

```math
\boxed{\;
|F_{t_0}(\tau_B)|^2
\ge
\exp\!\left[
-2\pi^2\sum_j\left(\frac{\eta_j}{\Delta}\right)^2
\right].
\;}
```

A bounded total squared detuning therefore preserves a positive nonresonant asymptotic heat excess for every vanishing-error protocol. In particular, for the paired bath and $`\delta_N\le\Delta/4`$ this elementary finite estimate reads

```math
A_N\ge e^{-4\pi^2c_N}.
```

The sharper paired limit above retains the equilibrium variance $`v`$. This extension is a converse only. The constructive sufficiency argument in [paired_bath.md](paired_bath.md) uses the paired spectrum and does not establish a threshold for arbitrary disorder.

## Relation to earlier finite-bath results

The equality form of Landauer's principle and its finite-size refinements are standard [[RW14]](../references/LITERATURE.md#rw14). Homogeneous spin-bath heat penalties and their resonance exceptions are known [[AHJM11]](../references/LITERATURE.md#ahjm11), and finite-bath heat optimization by population rearrangement has been studied in detail [[MMO16]](../references/LITERATURE.md#mmo16). Spectral conditions for approaching the Landauer cost are also central to [[T23]](../references/LITERATURE.md#t23).

The result proved here is the explicit all-unitary spectral bound and its quantitative stability consequence under shrinking local detunings. The complementary construction is proved in [compression.md](compression.md) and [paired_bath.md](paired_bath.md). The [source comparison](../references/RELATED_WORK.md) separates this claim from the results already established in those works.
