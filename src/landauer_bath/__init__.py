"""Numerical checks for the paired-gap Landauer threshold.

These routines distinguish explicit protocols, universal lower bounds, and
optimization of diagonal observables. They are not proof assistants.
"""

from .spectral import paired_gaps, spectral_witness, thermal_bath
from .compression import cutoff_certificate, cutoff_permutation

__all__ = ["paired_gaps", "spectral_witness", "thermal_bath",
           "cutoff_certificate", "cutoff_permutation"]
