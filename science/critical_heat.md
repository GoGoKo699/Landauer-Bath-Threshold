# Exact heat at the critical detuning scale

[Scientific account](README.md) · [Model](model.md) · [Threshold theorem](theorem.md) · [Reproduce the calculation](../verification/README.md)

The detuning threshold identifies when the Landauer heat is attainable. At the threshold scale, the gap between adjacent excitation shells and the thermal spread *within* each shell are both relevant. The exact heat is determined by how the ranks of bath states move when the reset must accommodate all memory labels in the reset sector.

## The exact heat curve

Use the paired bath and single joint unitary of the [model](model.md). The memory dimension $`d\ge2`$, baseline gap $`\Delta>0`$ and inverse temperature $`\beta>0`$ are fixed. Write

```math
a_N=\delta_N/\Delta,\qquad c_N=Na_N^2\longrightarrow c\in(0,\infty),
\qquad \alpha=\beta\Delta,\qquad
p=(1+e^\alpha)^{-1},\qquad \sigma^2=2p(1-p)c.
```

Let $`\Phi`$ be the standard normal cumulative distribution function and define

```math
A(u)=\sum_{m\in\mathbb Z}e^{\alpha m}\Phi((u-m)/\sigma),
\qquad T(u)=A^{-1}(d A(u)),\qquad
U\sim\mathcal N(-\alpha\sigma^2,\sigma^2).
```

**Critical heat theorem.** Every sequence of allowed unitaries with population reset error $`\epsilon_N\to0`$ on the maximally mixed memory obeys

```math
\liminf_{N\to\infty}\beta Q_N(I_d/d)
\;\ge\; \mathcal H_c(d,\alpha)
\;:=\;\alpha\,\mathbb E[T(U)-U].
```

A sequence of energy-basis permutations attains $`\mathcal H_c`$ with vanishing half-diamond reset error. Its heat converges to the same value uniformly over memory input states, so the minimum for worst-input heat at vanishing half-diamond error is also $`\mathcal H_c`$. Reset accuracy includes an inaccessible reference initially entangled with the memory. The theorem allows any vanishing error rate in the converse. It charges the entire bath and assumes the globally driven unitary of the model.

The series converges uniformly on compact sets, since negative shell indices have geometric weights and the positive tail of the normal cumulative probability decays faster than its exponential weight grows. The same bounds justify differentiation on compact sets. The function is positive and strictly increasing, with $`A(u+1)=e^\alpha A(u)`$. Thus it maps the real line onto the positive reals, and $`T(u)-u`$ is a bounded continuous function of period one.

For a two-level memory with $`\alpha=1`$ and $`c=0.05`$, the formula gives $`\mathcal H_c\simeq0.723139421`$. The Landauer value is $`\ln 2\simeq0.693147181`$. The corresponding finite permutations give about $`0.754099`$, $`0.728719`$ and $`0.724972`$ at 24, 96 and 256 bath pairs. The finite values are heat for the maximally mixed input. The uniform-input and reset guarantees are analytical.

## Counting thermally occupied shells

Measure bath energy in units of $`\Delta`$. Let $`K_+`$ and $`K_-`$ be the numbers of excited qubits with the larger and smaller gaps. A configuration has energy $`J+a_N D`$, where $`J=K_++K_-`$ and $`D=K_+-K_-`$. Write $`B_N(x)`$ for the number of bath basis states with dimensionless energy at most $`x`$.

For uniform counting at fixed total excitation $`J=k`$, the number of configurations is $`\binom{2N}{k}`$. The conditional variable $`K_+`$ counts marked sites when $`k`$ sites are drawn from $`2N`$ sites of which $`N`$ are marked. In particular,

```math
\Pr(D_k=z)=
\frac{\binom N{(k+z)/2}\binom N{(k-z)/2}}{\binom{2N}k},
\qquad
v_{N,k}:=\operatorname{Var}(D_k)=\frac{k(2N-k)}{2N-1}.
```

The probability is zero unless both binomial indices are integers in range. For $`k/(2N)\to p`$, this hypergeometric law is asymptotically normal on the scale $`\sqrt N`$. One way to see uniformity over such typical indices is to use Stirling's formula in the displayed probability. For admissible $`|z|\le C\sqrt N`$, expanding the two log-binomial terms about $`k/2`$ cancels the linear terms. The result, uniformly in that range, is

```math
\Pr(D_k=z)
=\frac{2}{\sqrt{2\pi v_{N,k}}}
  e^{-z^2/(2v_{N,k})}(1+o(1)).
```

The factor two is the lattice spacing. The hypergeometric variance controls the discarded tails as $`C`$ increases. Summing the local approximation gives convergence of the cumulative probabilities to a continuous normal law. Consequently $`a_N D_k`$ converges in distribution to $`\mathcal N(0,\sigma^2)`$.

For $`j`$ with $`|j-2Np|\le 2N^{2/3}`$, decompose the count near shell $`j`$ as

```math
\frac{B_N(j+u)}{\binom{2N}j}
=\sum_{m\in\mathbb Z}
\frac{\binom{2N}{j+m}}{\binom{2N}j}
\Pr(a_N D_{j+m}\le u-m).
```

A summand is zero for a shell outside the bath. For fixed $`m`$, the ratio of multiplicities tends to $`e^{\alpha m}`$ uniformly over these $`j`$. For $`m<0`$ it is bounded by $`r^{|m|}`$ for a fixed $`r<1`$, by monotonicity of the adjacent binomial ratios and $`p<1/2`$. For $`m\ge0`$ it is bounded by $`R^m`$ for a fixed finite $`R`$. In the positive tail $`m>u`$, Hoeffding's without-replacement comparison [Hoeffding63] gives

```math
\Pr(a_ND_{j+m}\le u-m)
\le e^{-(m-u)^2/(4c_N)}.
```

Indeed $`D_k`$ is the sum of $`k`$ sampled labels in $`[-1,1]`$ with population mean zero, so the exponent before bounding $`k\le2N`$ is $`-(m-u)^2/(2k a_N^2)`$. The geometric and Gaussian bounds are summable uniformly on compact sets of $`u`$. Thus the normalized count tends to $`A(u)`$ uniformly in the displayed range of $`j`$ and compact sets of $`u`$. The count with strict inequality in energy has the same limit, by bracketing at $`u`$ and $`u-\eta`$ and using continuity as $`\eta\downarrow0`$. Exact degeneracies therefore allow any fixed tie ordering consistent with keeping the $`d`$ memory labels of each bath configuration together.

The distribution that weights heat is the bath **Gibbs distribution**, which differs from uniform shell counting. In the Gibbs state, $`K_+`$ and $`K_-`$ are independent binomial variables with success probabilities

```math
p_\pm=(1+e^{\alpha(1\pm a_N)})^{-1}
=p\mp\alpha p(1-p)a_N+O(a_N^2).
```

The mean of $`a_N D`$ tends to $`-\alpha\sigma^2`$, and its variance tends to $`\sigma^2`$. Since the independent centered terms after multiplying by $`a_N`$ have maximum absolute value tending to zero, the triangular-array central limit theorem gives $`a_N D\Rightarrow U`$. The mean of $`J`$ is $`2Np+O(1)`$, and concentration for independent bounded variables gives $`\Pr(|J-2Np|>N^{2/3})\le 2e^{-\Omega(N^{1/3})}`$. Also $`|a_N D|\le Na_N=O(\sqrt N)`$ deterministically. Both $`J`$ and the integer part of the physical dimensionless energy are therefore within the typical range used in the count, except on a set of exponentially small Gibbs weight.

## Matching reset and all-unitary converse

### The sorted permutation

Order the bath configurations by increasing energy, with position $`s`$ starting at one. Order the input pairs consisting of a bath configuration and a memory basis label $`\ell\in\{1,\ldots,d\}`$ by the contiguous ranks $`d(s-1)+\ell`$. Send as many of these input states as fit, in order, to the bath configurations in the reset sector $`|0\rangle_S`$, also in increasing energy order. Complete the basis permutation with the remaining inputs and output states. This is the finite maximal-reset rearrangement [MMO16]; the argument below evaluates its heat in the paired-bath limit.

With overwhelming Gibbs probability, the input energy is at most $`bN`$ for a fixed $`2p<b<1`$. Every configuration at such an energy has at most $`bN/(1-a_N)`$ excitations. Counting configurations below this excitation threshold, using the binomial tail under uniform counting, shows that its maximum bath rank is at most $`4^N e^{-\Omega(N)}`$. Hence for large $`N`$ the full set of $`d`$ logical basis labels fits into the reset sector for each such configuration. Conditional on a particular one of these bath configurations, the memory channel is exactly the reset channel, since distinct logical basis inputs map to orthogonal bath states in that sector. This remains true with a reference. The weight of the remaining bath configurations bounds the half-diamond error, which decays exponentially in $`N`$ at this fixed cutoff.

For an input configuration in shell $`j`$ and detuning $`u=a_ND`$, the normalized rank of each of its $`d`$ copies tends to $`d A(u)`$. The source and destination are counted against the same $`\binom{2N}j`$. The output energy minus $`j`$ tends to $`T(u)`$, by the uniform count convergence and the strictly increasing limiting count. Quantile convergence is uniform on bounded $`u`$ and typical $`j`$. This follows by testing the destination count at $`T(u)\pm\eta`$ for each fixed $`\eta>0`$ and using a compact positive lower bound on $`A'`$ in the resulting range.

A bound on the energy displacement also holds for typical configurations whose detuning $`u`$ is outside a compact set. Recenter the count at the integer part of their initial dimensionless energy, leaving an offset in $`[0,1)`$. Choose a fixed positive integer $`L`$ with $`e^{\alpha L}>d`$. By the same uniform count convergence and $`A(u+L)=e^{\alpha L}A(u)`$, the count up to the initial energy plus $`L`$ exceeds $`d`$ times the count at the initial energy for all such inputs, for sufficiently large $`N`$. Their output energies thus increase by at most $`L`$, and cannot decrease because the new bath position is at least $`s`$. The remaining displacements have magnitude $`O(N)`$ and exponentially small Gibbs weight. These bounds justify taking the expectation of the convergent rank displacement under the Gibbs law.

Each input basis label has limiting heat $`\Delta\mathbb E[T(U)-U]`$. Conjugating the bath energy by a basis permutation gives a diagonal observable, so the heat for any input state is an average over its basis-label probabilities. Since $`d`$ is fixed, convergence is uniform over inputs.

### An energy penalty for reset failure

Fix a positive integer $`L`$ and use the dimensionless output observable

```math
\mathcal K_{N,L}=I_S\otimes H_{B,N}/\Delta
   +L(I_S-|0\rangle\langle0|)\otimes I_B.
```

For the maximally mixed memory, the eigenvalues of the initial joint state are descending Gibbs weights in the same contiguous rank order used above. The trace rearrangement inequality minimizes the expectation of $`\mathcal K_{N,L}`$ over all allowed unitaries by putting those eigenvalues in increasing order of $`\mathcal K_{N,L}`$'s eigenvalues. This follows as well by writing the final diagonal as a doubly stochastic matrix acting on the input eigenvalues and applying the finite rearrangement inequality. It covers coherent unitaries.

The destination count is $`B_N(x)+(d-1)B_N(x-L)`$. Since $`L`$ is an integer, its limiting normalized count at $`x=j+v`$ is

```math
A(v)+(d-1)A(v-L)=[1+(d-1)e^{-\alpha L}]A(v).
```

Thus the destination quantile converges to

```math
T_L(u)=A^{-1}\!\left(\frac{d A(u)}{1+(d-1)e^{-\alpha L}}\right).
```

For every $`N`$, adding the penalty moves each ordered eigenvalue up by between zero and $`L`$. This follows because the unpenalized list has $`d`$ copies of each bath energy, and every entry is shifted by between zero and $`L`$ before sorting. It gives bounded displacements for the rearrangement at fixed $`L`$. The count limit and Gibbs law can therefore be averaged to yield

```math
\liminf_{N\to\infty}
\left[\beta Q_N(I_d/d)+\alpha L\epsilon_N\right]
\ge\alpha\,\mathbb E[T_L(U)-U].
```

Take $`N\to\infty`$ at each fixed $`L`$. The error penalty vanishes whenever $`\epsilon_N\to0`$, regardless of its rate of convergence. Now take the integer $`L`$ to infinity. The functions $`T_L(u)-u`$ increase to $`T(u)-u`$, which is bounded and periodic. The resulting lower bound matches the permutation. Half-diamond reset implies vanishing population error, and the maximum heat over inputs is at least the heat on the maximally mixed input, proving the worst-input claim.

## Resonance and limiting cases

Let $`r`$ be the density of $`U`$ modulo one, and let $`q=T_*r`$ be its pushforward under the map induced by $`T`$ on the circle. Completing the square in $`e^{-\alpha u}A'(u)`$ gives

```math
r(u)=e^{-\alpha u-\alpha^2\sigma^2/2} A'(u),
\qquad 0\le u<1.
```

The density is positive, and differentiating $`A(T(u))=d A(u)`$ gives $`A'(T(u))T'(u)=d A'(u)`$. The change of variables on the circle gives $`q(T(u))/r(T(u))=e^{\alpha(T(u)-u)}/d`$. Averaging its logarithm yields the exact excess,

```math
\mathcal H_c(d,\alpha)-\ln d=D(q\Vert r).
```

At resonance, $`\ln d/\alpha\in\mathbb Z`$, the map is the corresponding integer shift in energy and the excess is zero. Conversely, equality of the densities would imply $`T(u)=u+\ln d/\alpha`$ for every $`u`$. This would make $`\ln d/\alpha`$ a period of $`e^{-\alpha u}A(u)`$. Its Fourier coefficient at frequency one is nonzero. In the convention $`\widehat f(k)=\int_0^1f(u)e^{-2\pi iku}du`$, the coefficients are

```math
\widehat{e^{-\alpha u}A(u)}(k)=
\int_{\mathbb R} e^{-(\alpha+2\pi ik)x}\Phi(x/\sigma)\,dx
=\frac{e^{(\alpha+2\pi ik)^2\sigma^2/2}}{\alpha+2\pi ik}.
```

The first equality follows by unfolding the period and the second by integration by parts with the normal density. The nonzero first coefficient forces an integer period, so every finite positive $`c`$ has strictly positive excess off resonance.

### Increasing the detuning spread

Off resonance the curve strictly decreases with $`c`$. To see this, put $`t=\sigma^2`$ and normalize the periodic count as $`b(t,u)=\alpha e^{-\alpha u-\alpha^2t/2}A(u)`$. A shift by $`-\alpha t`$ in its argument removes the Fourier phase. In the rest of this argument let $`b`$ denote the shifted function, which satisfies $`\partial_t b=\partial_u^2 b/2`$. The shifted Gibbs density is $`b+\partial_u b/\alpha`$, which is positive. The increasing coordinate $`y=u+\ln b(t,u)/\alpha`$ converts this density to $`f(t,y)=b(t,u)`$ and converts the rank map to translation by $`a=\ln d/\alpha`$. Write $`g(t,y)=f(t,y-a)`$. The excess heat is $`D(g\Vert f)`$ in this coordinate.

Let $`s_f=\partial_y\ln f`$ and $`h(s)=s/(1-s/\alpha)`$ for $`s<\alpha`$. The coordinate derivative $`\partial_u y=1+(\partial_u b)/(\alpha b)>0`$ gives $`s_f<\alpha`$, $`fh(s_f)=\partial_u b`$, and $`\partial_t f=\partial_t b/\partial_u y`$ at fixed $`y`$. Consequently

```math
\partial_t f=\tfrac12\partial_y\!\left(fh(s_f)\right),\qquad
\frac{d}{dt}D(g\Vert f)
=-\tfrac12\int_0^1 g(s_g-s_f)\bigl(h(s_g)-h(s_f)\bigr)\,dy.
```

The second equality follows by applying the first equation to both densities and integrating by parts on the circle. Since $`h`$ is strictly increasing, the derivative is negative unless $`s_g=s_f`$ throughout. Equality of the scores would give equality of the normalized densities, which holds exactly at resonance.

As $`c`$ grows, the nonzero Fourier coefficients of the periodic count, relative to its constant coefficient, vanish as $`e^{-2\pi^2 k^2\sigma^2}`$. The displacement $`T(u)-u`$ tends uniformly to $`\ln d/\alpha`$, and the heat curve tends to $`\ln d`$. This is a limit of the critical-window curve. The [threshold theorem](theorem.md) supplies the operational claim for bath sequences with $`c_N\to\infty`$. The regime $`c_N\to0`$ can have jumps in its limiting shell counts and requires a separate treatment of tied ranks. The [identical-bath benchmark](../references/RELATED_WORK.md#ahjm11) illustrates that regime.

[Reference locations for spectral rearrangement and concentration](../references/LITERATURE.md)
