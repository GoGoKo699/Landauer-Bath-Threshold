# Why the collective detuning scale matters

[Home](../README.md) · [Model](model.md) · [Theorem](theorem.md)

## A macroscopic bath can retain a microscopic obstruction

The bath in this problem grows without changing its temperature or its baseline single-qubit gap. Its heat capacity is extensive: each almost-identical thermal qubit contributes a positive quantity approaching $`k_{\mathrm B}(\beta\Delta)^2p(1-p)`$, where $`p=(1+e^{\beta\Delta})^{-1}`$. Nevertheless, a large heat capacity is not sufficient for reversible erasure under a unitary on a fixed bath.

The reason is spectral. The initial memory contributes a factor $`1/d`$ to every eigenvalue of the joint state. A nearly reset memory at the Landauer heat would leave a joint state close to a pure memory tensored with the original bath Gibbs state. A unitary must reconcile these two eigenvalue patterns. For a bath with a rigid spectral lattice, the required rescaling can fail even when each individual bath spin changes very little. The identical-spin maximal-cooling heat law and its arithmetic exceptions were established in [AHJM11]; see the [source comparison](../references/RELATED_WORK.md).

The quantity $`\operatorname{Tr}\rho^{1+it}`$ is a convenient way to detect the residual pattern. Its absolute value is the modulus of the characteristic function of the random variable $`\ln\lambda`$, when eigenvalue $`\lambda`$ is sampled with probability $`\lambda`$. Thus it weights spectral locations by their actual population. It is also unchanged by every unitary, which makes it useful for a converse without specifying a control protocol.

## Small local detunings can accumulate

At the frequency $`t_0=2\pi/(\beta\Delta)`$, the phases contributed by a perfectly homogeneous bath align. A detuning changes those phases slightly. For independent thermal spins the characteristic functions multiply, and the accumulated attenuation is governed to leading order by the sum of squared detunings.

For the paired bath this gives

```math
\left|\operatorname{Tr}\tau_{B,N}^{1+it_0}\right|^2
\sim\exp\!\left[-8\pi^2p(1-p)
N(\delta_N/\Delta)^2\right]
```

when the accumulated detuning has a finite limit. The [spectral proof](spectral_obstruction.md) states the exact finite expression and its limit. If $`\sqrt N\,\delta_N/\Delta`$ stays bounded, the spectral witness retains a nonzero magnitude. Nonresonance then turns it into a positive excess heat.

This reasoning is a necessary condition. Its converse needs an operation that uses the relevant bath states, and that operation is supplied explicitly.

## The same scale creates a useful virtual bath

Each physical pair has a one-excitation sector spanned by $`|01\rangle`$ and $`|10\rangle`$. The two states differ in energy by $`2\delta_N`$. Conditional on occupying that sector, the pair is a thermal qubit with that small gap. A positive fraction of the pairs are active at fixed temperature.

The small-gap virtual bath combines two properties. Its energy resolution improves as $`\delta_N\to0`$, and its collective thermal polarization remains sufficient for erasure when $`N(\beta\delta_N)^2\to\infty`$. The compression proof shows how to use both properties together. The unitary moves almost all input weight into the target-memory subspace while raising the bath energy by at most a number of small steps whose total tends to $`\ln d/\beta`$.

The activity pattern is an internal orthogonal decomposition of the bath. It is not read out or stored in an external controller. The direct-sum unitary leaves the pattern labels unchanged, so all entropy and energy remain in the stated memory–bath system.

## Available gaps and populated gaps

For $`\delta_N=\Delta N^{-\alpha}`$, the result has a simple classification:

| Exponent | Collective scale | Vanishing-error heat |
|---|---|---|
| $`0<\alpha<1/2`$ | $`N(\delta_N/\Delta)^2\to\infty`$ | Landauer heat is attainable. |
| $`\alpha=1/2`$ | Finite nonzero collective scale | A positive excess remains at nonresonance. |
| $`\alpha>1/2`$ | Collective scale tends to zero | A positive excess remains at nonresonance. |

The interval $`1/2<\alpha<1`$ is especially informative. There are energy differences spaced by $`2\delta_N`$ over a range $`2N\delta_N`$, so the set of available differences becomes dense on every fixed bounded interval. This counts possible transitions. It does not require those transitions to carry enough Gibbs probability to implement reversible erasure. The all-unitary heat bound shows that they do not suffice in this regime.

This is compatible with the broader role of thermal spectral structure in [T23]. The quantitative distinction here is between the total virtual bandwidth, proportional to $`N\delta_N`$, and the thermally relevant fluctuation scale, proportional to $`\sqrt N\,\delta_N`$.

## What the threshold says about an erasure device

The achievable protocol erases the entire input channel. It does not rely on knowing which pure state was supplied, and its error remains small when the input is entangled with a reference. Its heat upper bound holds for every memory input, while the maximally mixed input fixes the limiting worst-case cost.

The theorem identifies which prescribed baths permit that task in principle. Implementing the permutation may require extensive control. A local or finite-time architecture would add a separate restriction; the present proof does not turn the information-theoretic construction into an efficient cooling circuit.

The resonance condition is also part of the result. At excluded values the particular spectral mismatch vanishes, and the necessity statement is not available. The finite bound remains true there but may give no excess beyond the ordinary Landauer inequality.

The [finite certificates](theorem.md) and [reproduction materials](../verification/README.md) quantify what is proved for finite instances. The explicit critical-window lower bound is useful for obstruction, but it is not an exact optimal crossover curve.
