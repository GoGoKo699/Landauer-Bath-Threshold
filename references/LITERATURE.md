# Source guide

[Home](../README.md) · [Related work](RELATED_WORK.md) · [BibTeX](references.bib)

This guide identifies the exact sources and versions behind the imported proof ingredients and the related-work comparison. Section and equation locators refer to the listed version. The project uses natural logarithms, bath heat positive for energy deposited in the bath, and the trace norm without a factor of one half.

## Entropy balance and mathematical ingredients

<a id="rw14"></a>
### [RW14] Equality form of Landauer's principle

**David Reeb and Michael M. Wolf.** “An improved Landauer principle with finite-size corrections.” *New Journal of Physics* **16**, 103011 (2014).

- [Publisher / DOI](https://doi.org/10.1088/1367-2630/16/10/103011)
- [arXiv:1306.4352v3](https://arxiv.org/abs/1306.4352v3), 11 October 2014; published-version manuscript.
- **Exact dependency:** Theorem 3, Eqs. (21)–(23), for an initially uncorrelated system and Gibbs reservoir followed by a joint unitary. Its equality gives entropy reduction plus final mutual information and bath relative entropy. The identity is used directly; its finite-dimension correction is not the new spectral bound.

<a id="elv10"></a>
### [ELV10] Earlier relative-entropy formulation

**Massimiliano Esposito, Katja Lindenberg, and Christian Van den Broeck.** “Entropy production as correlation between system and reservoir.” *New Journal of Physics* **12**, 013013 (2010).

- [Publisher / DOI](https://doi.org/10.1088/1367-2630/12/1/013013)
- [arXiv:0908.1125v1](https://arxiv.org/abs/0908.1125v1), 7 August 2009.
- **Attribution:** Eqs. (5)–(9) express entropy production as relative entropy from the final system state tensored with the initial thermal reservoirs. RW14 explicitly acknowledges this antecedent after its Theorem 3. The project does not attribute that identity's first appearance to RW14.

<a id="mirsky60"></a>
### [Mirsky60] Spectral variation in a unitarily invariant norm

**Leon Mirsky.** “Symmetric gauge functions and unitarily invariant norms.” *The Quarterly Journal of Mathematics* **11**(1), 50–59 (1960).

- [Publisher record / DOI](https://doi.org/10.1093/qmath/11.1.50)
- **Specialization used:** for positive matrices, with eigenvalues in the same decreasing order,

  ```math
  \sum_j|\lambda_j(\rho)-\lambda_j(\omega)|\le\|\rho-\omega\|_1.
  ```

The original bibliographic record is verified at the publisher. An accessible explicit statement of precisely this specialization is [Shirokov22](#shirokov22), Sec. 2.1, Eq. (3) in the arXiv version; it is Eq. (2.1) in the published version. This source distinction avoids assigning an unchecked equation number to the original paper.

<a id="shirokov22"></a>
### [Shirokov22] Accessible statement of the trace-norm specialization

**M. E. Shirokov.** “Convergence criterion for quantum relative entropy and its use.” *Sbornik: Mathematics* **213**(12), 1740–1772 (2022).

- [Published English version / DOI](https://doi.org/10.4213/sm9794e)
- [arXiv:2205.10341v3](https://arxiv.org/abs/2205.10341v3), 5 December 2022. The arXiv metadata uses the longer title “Quantum relative entropy: general convergence criterion and preservation of convergence under completely positive linear maps.”
- **Exact dependency:** only the spectral inequality in Sec. 2.1, Eq. (3), and its identification with Mirsky's inequality. None of this paper's convergence theorems is needed.

<a id="pinsker"></a>
### [Pinsker] Quantum Pinsker inequality and its logarithm convention

**John Watrous.** *The Theory of Quantum Information*. Cambridge University Press (2018).

- [Publisher / DOI](https://doi.org/10.1017/9781316848142)
- [Author's official book page and manuscript](https://cs.uwaterloo.ca/~watrous/TQI/)
- **Exact dependency:** Theorem 5.38, Eq. (5.190), pp. 282–283. The book's base-two relative entropy gives the coefficient $`1/(2\ln2)`$. Multiplying relative entropy by $`\ln2`$ gives the convention used here:

  ```math
  D(\rho\Vert\omega)\ge\frac12\|\rho-\omega\|_1^2.
  ```

The proof proceeds through optimal binary discrimination and relative-entropy data processing. The book's bibliographic remarks identify earlier quantum formulations; the label [Pinsker] here names the inequality, not a claim of authorship by Watrous.

<a id="schurhorn"></a>
### [SchurHorn] Exact population-vector description of a unitary orbit

**John Watrous.** *The Theory of Quantum Information* (2018), the same [official source](https://cs.uwaterloo.ca/~watrous/TQI/) as [Pinsker].

**Exact dependency:** Theorem 4.33, pp. 243–244, characterizes possible diagonals of a Hermitian operator by majorization of its spectrum. Theorem 4.30, p. 237, gives the equivalent doubly stochastic and unistochastic-vector formulations. Consequently, optimizing linear heat and target population over vectors $`v=D\lambda`$, with $`D`$ doubly stochastic, is exact for a joint unitary orbit. The particular transport matrix returned by a linear program need not itself be unistochastic; existence of some unitary producing the same population vector is sufficient.

<a id="hoeffding63"></a>
### [Hoeffding63] Binomial concentration

**Wassily Hoeffding.** “Probability Inequalities for Sums of Bounded Random Variables.” *Journal of the American Statistical Association* **58**(301), 13–30 (1963).

- [Publisher / DOI](https://doi.org/10.1080/01621459.1963.10500830)
- [University-hosted scan](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf)
- **Exact dependency:** Theorem 1, Eq. (2.3), p. 15. For $`K\sim\operatorname{Bin}(m,p)`$ and $`u\ge0`$, it gives $`\Pr[K-mp\ge u]\le e^{-2u^2/m}`$; the lower-tail version follows by replacing each Bernoulli variable by its complement. Both the virtual-qubit count and compression tail use this bound.

<a id="blps12"></a>
### [BLPS12] Virtual qubits

**Nicolas Brunner, Noah Linden, Sandu Popescu, and Paul Skrzypczyk.** “Virtual qubits, virtual temperatures, and the foundations of thermodynamics.” *Physical Review E* **85**, 051117 (2012).

- [Publisher / DOI](https://doi.org/10.1103/PhysRevE.85.051117)
- [arXiv:1106.2138v2](https://arxiv.org/abs/1106.2138v2), 13 August 2012; published version.
- **Imported idea:** Sec. II, Eqs. (1)–(6), treats two-level subspaces of composite thermal systems as virtual qubits. The present same-temperature specialization, its exact occupation probability, and its use inside a coherent direct-sum unitary are derived in [the paired-bath proof](../science/paired_bath.md).

## Closest bath and cooling results

<a id="ahjm11"></a>
### [AHJM11] Identical-spin reservoir and fixed-gap resonance

**Armen E. Allahverdyan, Karen V. Hovhannisyan, Dominik Janzing, and Guenter Mahler.** “Thermodynamic limits of dynamic cooling.” *Physical Review E* **84**, 041109 (2011).

- [Publisher / DOI](https://doi.org/10.1103/PhysRevE.84.041109)
- [arXiv:1107.1044v1](https://arxiv.org/abs/1107.1044v1), 6 July 2011.
- **Checked location:** Sec. VI.B, especially Eqs. (90), (93), and (94), pp. 11–13. The degenerate target is explicitly considered. The homogeneous-bath limiting work and its resonance behavior are inherited, as explained in [Related work](RELATED_WORK.md).

<a id="mmo16"></a>
### [MMO16] Finite error–heat optimization

**M. Hamed Mohammady, Masoud Mohseni, and Yasser Omar.** “Minimising the heat dissipation of quantum information erasure.” *New Journal of Physics* **18**, 015011 (2016).

- [Publisher / DOI](https://doi.org/10.1088/1367-2630/18/1/015011)
- [arXiv:1510.02062v2](https://arxiv.org/abs/1510.02062v2), 25 January 2016.
- [Institutional copy of the published article](https://hdl.handle.net/1721.1/101693)
- **Checked locations:** Secs. 2.4–2.5, Eq. (2.13), partial swaps in Eq. (2.15), and Appendix C, Theorems C.1–C.2. These cover the finite error–heat tradeoff, not only the maximal-cooling endpoint. The current construction is a uniform asymptotic certificate, not a replacement finite optimizer.

<a id="t23"></a>
### [T23] Control complexity and spectral conditions

**Philip Taranto and coauthors.** “Landauer Versus Nernst: What is the True Cost of Cooling a Quantum System?” *PRX Quantum* **4**, 010332 (2023). Full authors are in [references.bib](references.bib).

- [Publisher / DOI](https://doi.org/10.1103/PRXQuantum.4.010332)
- [arXiv:2106.05151v3](https://arxiv.org/abs/2106.05151v3), 28 March 2023; close to the published version.
- **Checked locations:** main-text Theorem 4; Appendix D4, Theorem 12 and Eqs. (D23)–(D24); D4's final discussion of other near-perfect protocols; D5. The occupation qualification and maximal-cooling scope of the explicit eigenvalue condition are retained in [Related work](RELATED_WORK.md).

<a id="t25"></a>
### [T25] Thermodynamic length for collision schedules

**Philip Taranto, Patryk Lipka-Bartosik, Nayeli A. Rodríguez-Briones, Martí Perarnau-Llobet, Nicolai Friis, Marcus Huber, and Pharnam Bakhshinezhad.** “Efficiently Cooling Quantum Systems with Finite Resources: Insights from Thermodynamic Geometry.” *Physical Review Letters* **134**, 070401 (2025).

- [Publisher / DOI](https://doi.org/10.1103/PhysRevLett.134.070401)
- [arXiv:2404.06649v2](https://arxiv.org/abs/2404.06649v2), 20 February 2025; close to the published version.
- **Checked locations:** Theorem 1, the following optimality discussion, Appendix B1, and Appendix C. Fresh-machine Markovian steps and controllable machine Hamiltonians are assumptions of the relevant optimization. The GOE example uses sorted and rescaled schedules.

<a id="lp25"></a>
### [LP25] Interaction-assisted convergence rates

**Patryk Lipka-Bartosik and Martí Perarnau-Llobet.** “Minimizing Dissipation via Interacting Environments: Quadratic Convergence to Landauer Bound.” *Physical Review Letters* **135**, 170404 (2025).

- [Publisher / DOI](https://doi.org/10.1103/5w1r-1nzs)
- [arXiv:2411.00944v1](https://arxiv.org/abs/2411.00944v1), 1 November 2024.
- **Checked locations:** Sec. III.A, Eq. (10), and Sec. III.B's engineered interacting bath. These compare best convergence rates as bath size grows. Their inverse-size lower bound for noninteracting reservoirs does not imply that every fixed family of such reservoirs approaches zero entropy production.

<a id="x25"></a>
### [X25] Cooling with nonidentical thermal qubits

**Jake Xuereb, Benjamin Stratton, Alberto Rolandi, Jinming He, Marcus Huber, and Pharnam Bakhshinezhad.** “Cooling a Qubit Using $`n`$ Others.” *PRX Quantum* **6**, 040368 (2025).

- [Publisher / DOI](https://doi.org/10.1103/hrph-dbv7)
- [arXiv:2506.10059v2](https://arxiv.org/abs/2506.10059v2), 20 December 2025.
- **Checked locations:** finite-machine setup and cooling criteria; perfect-matching formulation; Appendix H, including Eq. (H14); Appendix I2 on swappable sets and median degeneracies. These are the appropriate comparators for energetic structure and small gap noise; they do not state the joint-limit threshold studied here.

<a id="n26"></a>
### [N26] Classical and quantum encodings under resource constraints

**Jan Neuser, Jake Xuereb, Pharnam Bakhshinezhad, and Marcus Huber.** “Quantum vs Classical Erasure: Equal Bounds but Unequal Costs.” arXiv preprint (2026).

- [arXiv:2607.27341v1](https://arxiv.org/abs/2607.27341v1), 29 July 2026.
- **Checked locations:** the definitions of classical and quantum bits, the explicit work-system model, Eqs. (2)–(5), and the finite-interaction comparison. Its macroscopic bath/work assumptions and restricted control frequencies differ from the prescribed finite-bath model here. No journal publication is assumed for this version.

## Reading the attribution correctly

The cited mathematical inequalities and finite-bath optimization methods are imported results. The [spectral certificate](../science/spectral_obstruction.md), the [uniform compression argument](../science/compression.md), and their [combination for paired gaps](../science/paired_bath.md) are proved within this repository. Source checks were current on **28 October 2026**. Later revisions may change theorem numbering or enlarge a paper's scope; the version links above make this comparison reproducible.
