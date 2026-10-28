# Compression with a thermal bath of small-gap qubits

This page gives the finite construction used in the sufficiency proof of the [threshold theorem](theorem.md). A memory of fixed dimension $`d\ge2`$ is coupled to $`m`$ independent thermal qubits of gap $`h>0`$. A permutation unitary approximately resets every memory input, including inputs entangled with an untouched reference, while placing a uniform upper bound on bath heat.

The construction is a population rearrangement, a standard tool in finite-bath erasure [[AHJM11]](../references/LITERATURE.md#ahjm11), [[MMO16]](../references/LITERATURE.md#mmo16). The proof below supplies a finite cutoff criterion and an explicit completion of the permutation. The completion is needed to control heat on all input branches.

The physical bath in the main theorem has gaps close to $`\Delta`$, rather than close to zero. The [paired-bath construction](paired_bath.md) embeds the small-gap bath proved here into invariant subspaces of that physical bath without introducing an auxiliary system.

## 1. Setting and finite criterion

Put

```math
b=\beta h,\qquad
p_b=\frac{1}{1+e^b},\qquad
\tau_h=
\begin{pmatrix}
1-p_b&0\\
0&p_b
\end{pmatrix}.
```

The bath Hamiltonian is $`H_m=h\sum_{i=1}^m|1\rangle\langle1|_i`$, and its initial state is $`\tau_h^{\otimes m}`$. Define the cumulative number of bath basis states through excitation number $`k`$ by

```math
B_m(k)=\sum_{a=0}^k\binom ma,\qquad 0\le k\le m.
```

Choose integers $`k,r`$ satisfying

```math
0\le k\le m-1,\qquad
1\le r\le m-k,\qquad
\boxed{\;
\left(\frac{m-k-r+1}{k+r}\right)^r\ge d .
\;}
```

This is a sufficient condition that can be evaluated directly at finite size. It is not a claim that the construction minimizes heat.

More generally, the same construction works whenever the integer ranges above hold and

```math
B_m(\ell+r)\ge d\,B_m(\ell)
\qquad\text{for every integer }0\le\ell\le k.
```

The ratio condition implies these cumulative inequalities, as proved below. Either set of inequalities is a valid finite certificate.

Let $`K\sim\operatorname{Bin}(m,p_b)`$ and define the excluded thermal mass

```math
\eta_m=\Pr[K>k]
=\sum_{a=k+1}^m\binom ma p_b^a(1-p_b)^{m-a}.
```

**Finite compression lemma.** Whenever the stated integer criterion holds, there is a permutation unitary $`U_{m,k,r}`$ on the memory and these $`m`$ bath qubits whose induced channel $`\mathcal E_{m,k,r}`$ satisfies

```math
\frac12\left\|\mathcal E_{m,k,r}-\mathcal R\right\|_\diamond
\le\eta_m,\qquad
\mathcal R(X)=|0\rangle\langle0|\operatorname{Tr}X,
```

and whose heat for every memory density matrix $`\rho`$ satisfies

```math
Q_{m,k,r}(\rho)\le rh.
```

No memory measurement, postselection, extra thermal qubit, catalyst, or auxiliary entropy sink appears in this construction.

## 2. The cumulative-binomial inequality

For every integer $`0\le\ell\le k`$,

```math
B_m(\ell+r)
\ge
\left(\frac{m-\ell-r+1}{\ell+r}\right)^r B_m(\ell)
\ge d\,B_m(\ell).
```

To prove the first inequality, use the terms with excitation numbers $`r,r+1,\ldots,\ell+r`$ in the cumulative sum. For $`0\le a\le\ell`$,

```math
\frac{\binom m{a+r}}{\binom ma}
=
\prod_{q=1}^r\frac{m-a-q+1}{a+q}
\ge
\left(\frac{m-\ell-r+1}{\ell+r}\right)^r.
```

All numerators are positive because $`\ell+r\le m`$. Summing over $`a`$ proves the first inequality. The displayed ratio is nonincreasing in $`\ell`$, so the finite criterion at $`k`$ proves the second.

In particular, with $`R=B_m(k)`$ and bath dimension $`D_B=2^m`$,

```math
dR\le B_m(k+r)\le D_B.
```

Thus there is room to put the $`dR`$ good input basis states into the single target-memory sector.

## 3. An exact permutation on the full Hilbert space

Fix a bath energy eigenbasis and order its elements by nondecreasing excitation number, resolving degeneracies in any fixed way. Denote their ranks by $`j=1,\ldots,D_B`$. The memory basis is $`s=0,\ldots,d-1`$, with $`s=0`$ the reset target.

On every good input rank $`1\le j\le R`$, define

```math
\pi(s,j)=\bigl(0,d(j-1)+s+1\bigr).
```

This sends the entire memory subspace at bath rank $`j`$ into the target-memory sector. Its image is exactly $`\{(0,j):1\le j\le dR\}`$.

The input states with target memory and bath ranks $`R+1,\ldots,dR`$ have not yet been assigned outputs. For $`q=1,\ldots,(d-1)R`$, set

```math
\begin{aligned}
\pi(0,R+q)
&=\bigl(s(q),j(q)\bigr),\\
s(q)&=1+\left\lfloor\frac{q-1}{R}\right\rfloor,\\
j(q)&=1+\bigl((q-1)\bmod R\bigr).
\end{aligned}
```

These overflow inputs map bijectively to all non-target-memory states with bath ranks at most $`R`$. On every remaining basis state set $`\pi(s,j)=(s,j)`$.

The assigned domains are disjoint. Their union consists of all memory states at ranks at most $`R`$, together with the target-memory states at ranks $`R+1,\ldots,dR`$. The assigned outputs cover precisely the same union. The prescription is therefore a permutation of the complete joint basis and defines a unitary

```math
U_{m,k,r}|s,j\rangle=|\pi(s,j)\rangle.
```

The overflow rule is part of the protocol. An arbitrary extension of the good-input injection would not provide the heat bound below.

## 4. Channel guarantee, including a reference

For a fixed good bath rank $`j\le R`$, define the bath isometry

```math
V_j|s\rangle=|d(j-1)+s+1\rangle_B.
```

The permutation acts on this whole input subspace as

```math
U_{m,k,r}
\bigl(|\psi\rangle_S\otimes|j\rangle_B\bigr)
=
|0\rangle_S\otimes V_j|\psi\rangle_B.
```

Tracing out the bath therefore gives exactly $`\mathcal R`$ for every memory input. If the memory is entangled with a reference, the same calculation gives $`\mathcal R\otimes\operatorname{id}`$ on their joint state.

The thermal bath is diagonal in the chosen basis. Its ranks $`j\le R`$ have total weight $`1-\eta_m`$. Averaging the remaining conditional channels gives a completely positive trace-preserving channel $`\mathcal B`$ such that

```math
\mathcal E_{m,k,r}
=(1-\eta_m)\mathcal R+\eta_m\mathcal B.
```

The diamond distance between two channels is at most $`2`$, so

```math
\frac12\|\mathcal E_{m,k,r}-\mathcal R\|_\diamond
\le\eta_m.
```

The good set is a subset of the bath basis only. Its probability is therefore independent of the memory input and of any reference correlations.

## 5. A uniform heat bound

Let $`E(j)`$ denote the energy of bath rank $`j`$. Suppose a good input rank $`j\le R`$ lies in excitation shell $`\ell\le k`$. Then

```math
j\le B_m(\ell),\qquad
d(j-1)+s+1\le dj\le dB_m(\ell)\le B_m(\ell+r).
```

Its output bath energy is consequently at most $`(\ell+r)h`$, so its energy increase is at most $`rh`$.

Every overflow input has bath rank greater than $`R`$ and maps to a rank at most $`R`$. Its bath energy change is nonpositive. Every remaining basis state is fixed and has zero energy change.

Because $`U_{m,k,r}`$ is a basis permutation, the operator

```math
\Delta H
=
U_{m,k,r}^\dagger(I_S\otimes H_m)U_{m,k,r}
-I_S\otimes H_m
```

is diagonal in the input basis. The preceding pointwise statements imply the operator inequality

```math
\Delta H
\le rh\,(I_S\otimes P_R)
\le rh\,I_{SB},\qquad
P_R=\sum_{j=1}^R|j\rangle\langle j|.
```

Hence for every memory state, including one with coherence in the chosen basis,

```math
\begin{aligned}
Q_{m,k,r}(\rho)
&=\operatorname{Tr}\!\left[
(\rho\otimes\tau_h^{\otimes m})\Delta H
\right]\\
&\le rh(1-\eta_m)
\le rh.
\end{aligned}
```

No bound proportional to the bath's maximal energy is multiplied by a small exceptional probability. The overflow branches can only reduce the heat.

## 6. An explicit parameter choice

The finite lemma permits any certified pair $`k,r`$. The following conservative choice proves attainability throughout the required joint limit without invoking an unspecified asymptotic constant.

Write

```math
L=\ln d,\qquad z=mb^2,\qquad
\gamma=6\left[z^{-1/4}+\frac{2L+1}{z}\right].
```

Assume

```math
0<b\le1,\qquad \gamma\le\frac12,
```

and choose

```math
\boxed{\;
k=\left\lfloor mp_b+z^{1/4}\sqrt m\right\rfloor,\qquad
r=\left\lceil\frac{L}{b(1-\gamma)}\right\rceil .
\;}
```

Then all the finite-lemma conditions hold. Furthermore,

```math
\boxed{\;
\frac12\|\mathcal E_{m,k,r}-\mathcal R\|_\diamond
\le e^{-2\sqrt z},\qquad
\beta Q_{m,k,r}(\rho)
\le\frac{L}{1-\gamma}+b
\quad\text{for every }\rho.
\;}
```

These constants give a sufficient certificate; they are not intended as an optimized finite-size estimate.

### Verification of the integer criterion

First,

```math
\frac{k}{m}\le p_b+bz^{-1/4}.
```

Since $`\gamma\le1/2`$ and $`b\le1`$,

```math
r\le\frac{2L}{b}+1,\qquad
\frac rm\le b\,\frac{2L+1}{z}.
```

Consequently, for $`x=(k+r)/m`$,

```math
x\le p_b+b\left[z^{-1/4}+\frac{2L+1}{z}\right]
=p_b+\frac{b\gamma}{6}
\le p_b+\frac b{12}.
```

For $`0<b\le1`$,

```math
p_b>\frac14,\qquad
\frac12-p_b
=\frac{e^b-1}{2(1+e^b)}
\ge\frac b8.
```

The last inequality follows from $`e^b-1\ge b`$ and $`1+e^b\le1+e<4`$. Thus

```math
x\le\frac12-\frac b{24}<\frac12.
```

In particular $`k+r<m/2`$, so $`0\le k\le m-1`$ and $`1\le r\le m-k`$. Also $`x\ge p_b`$: indeed $`r\ge1`$ and $`\lfloor y\rfloor+1\ge y`$ applied to $`y=mp_b+z^{1/4}\sqrt m`$ suffice.

Let $`g(x)=\ln[(1-x)/x]`$. On $`[p_b,x]\subset[1/4,1/2]`$,

```math
|g'(x)|=\frac{1}{x(1-x)}\le\frac{16}{3}<6.
```

Using the exact identity $`g(p_b)=b`$ gives

```math
g(x)\ge b-6(x-p_b)\ge b(1-\gamma).
```

Finally,

```math
\begin{aligned}
r\ln\left(\frac{m-k-r+1}{k+r}\right)
&=r\ln\left(\frac{1-x+1/m}{x}\right)\\
&\ge r\,g(x)\\
&\ge rb(1-\gamma)\\
&\ge L.
\end{aligned}
```

This is exactly the finite compression criterion. In particular, the estimate does not replace $`b`$ by a small-$`b`$ expansion of the log odds, which could fail to control all joint limits of $`m`$ and $`b`$.

### Error and heat with this choice

For an integer-valued $`K`$,

```math
K>\left\lfloor mp_b+z^{1/4}\sqrt m\right\rfloor
\quad\Longleftrightarrow\quad
K>mp_b+z^{1/4}\sqrt m.
```

Hoeffding's inequality [[Hoeffding63]](../references/LITERATURE.md#hoeffding63) therefore gives

```math
\eta_m
\le
\exp\left[-\frac{2(z^{1/4}\sqrt m)^2}{m}\right]
=e^{-2\sqrt z}.
```

There is no additional loss from the floor in $`k`$. The ceiling in $`r`$ gives

```math
\beta Q_{m,k,r}(\rho)\le br
\le\frac{L}{1-\gamma}+b.
```

For example, the resulting excess over $`L`$ is at most $`2L\gamma+b`$ whenever $`\gamma\le1/2`$.

## 7. The joint small-gap limit

Let $`d`$ and $`\beta`$ be fixed and let a sequence of these baths obey

```math
b=\beta h\longrightarrow0,\qquad
z=m(\beta h)^2\longrightarrow\infty.
```

The explicit conditions in the preceding section eventually hold, $`\gamma\to0`$, the half-diamond error tends to zero, and

```math
\limsup\beta\sup_\rho Q_{m,k,r}(\rho)\le\ln d.
```

For the maximally mixed input, the ordinary finite-error Landauer inequality [[RW14]](../references/LITERATURE.md#rw14) gives

```math
\beta Q_{m,k,r}(I_d/d)
\ge\ln d-S\!\left(\mathcal E_{m,k,r}(I_d/d)\right).
```

The output entropy tends to zero because $`d`$ is fixed and the channel error tends to zero. Since the supremum over inputs is at least the value at $`I_d/d`$, the two bounds imply

```math
\boxed{\;
\beta Q_{m,k,r}(I_d/d)\longrightarrow\ln d,\qquad
\beta\sup_\rho Q_{m,k,r}(\rho)\longrightarrow\ln d.
\;}
```

The construction does not claim that the heat for every individual input tends to this value. It gives a universal reset channel and a matching asymptotic bound on the worst-input heat. Its unitary is permitted by the [global-control model](model.md); no efficient local circuit implementation is asserted.
