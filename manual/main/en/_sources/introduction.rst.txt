Introduction
================================

What is ODAT-SE ?
--------------------------------

ODAT-SE is a framework for applying a search algorithm to a direct problem solver to find the optimal solution.
As the standard direct problem solver, the experimental data analysis software for two-dimensional material structure analysis is prepared.
The direct problem solver gives the deviation between the experimental data and the calculated data obtained under the given parameters such as atomic positions as a loss function used in the inverse problem.
The optimal parameters are estimated by minimizing the loss function using a search algorithm. For further use, the original direct problem solver or the search algorithm can be defined by users.
In the current version, for solving a direct problem, ODAT-SE offers the wrapper of the solver for the total-reflection high-energy positron diffraction (TRHEPD), the surface X-ray diffraction (SXRD), and the low-energy electron diffraction (LEED).
As algorithms, it offers the Nelder-Mead method, the grid search method, the Bayesian optimization method, the replica exchange Monte Carlo method, and the population annealing Monte Carlo method.


What is odatse-XAFS ?
--------------------------------

Polarization-dependent Total Reflection Fluorescence X-ray Absorption Fine Structure (PTRF-XAFS) is a method to analyze material structures by the X-ray absorption spectra that reveal symmetries or electronic states of atoms. Especially, by using the total reflection, it is efficient for the analysis of surface structure.

For the analysis of X-ray spectra, a first-principle calculation software, FEFF [1,2], has been developed that provides theoretical prediction of X-ray spectroscopy from the information of atomic positions. It is implemented by Fortran and runs on standard Linux platforms.
odatse-XAFS is an adaptor library to use FEFF as a direct problem solver of ODAT-SE.
It was originally developed as a component of 2DMAT v2.x, and has been restructured as a separate module to be used with ODAT-SE and FEFF.

[1] Ab initio theory and calculation of X-ray spectra, J. J. Rehr, J. J. Kas, M. P. Prange, A. P. Sorini, Y. Takimoto, F. D. Vila, `Comptes Rendus Physique 10 (6) 548-559 (2009) <https://doi.org/10.1016/j.crhy.2008.08.004>`_.

[2] Theoretical Approaches to X-ray Absorption Fine Structure, J. J. Rehr and R. C. Albers, `Rev. Mod. Phys. 72, 621 (2000) <https://doi.org/10.1103/RevModPhys.72.621>`_.


License
--------------------------------
|  This package is distributed under GNU General Public License version 3 (GPL v3).

Copyright (c) <2025-> The University of Tokyo. All rights reserved.

This software was developed with the support of "Project for advancement of software usability in materials science" of The Institute for Solid State Physics, The University of Tokyo.
We hope that you cite the following reference when you publish the results using 2DMAT / ODAT-SE:

"Data-analysis software framework 2DMAT and its application to experimental measurements for two-dimensional material structures", Y. Motoyama, K. Yoshimi, I. Mochizuki, H. Iwamoto, H. Ichinose, and T. Hoshi, `Computer Physics Communications 280, 108465 (2022). <https://doi.org/10.1016/j.cpc.2022.108465>`_

Bibtex::

  @article{MOTOYAMA2022108465,
    title = {Data-analysis software framework 2DMAT and its application to experimental measurements for two-dimensional material structures},
    journal = {Computer Physics Communications},
    volume = {280},
    pages = {108465},
    year = {2022},
    issn = {0010-4655},
    doi = {https://doi.org/10.1016/j.cpc.2022.108465},
    url = {https://www.sciencedirect.com/science/article/pii/S0010465522001849},
    author = {Yuichi Motoyama and Kazuyoshi Yoshimi and Izumi Mochizuki and Harumichi Iwamoto and Hayato Ichinose and Takeo Hoshi}
  }


Version Information
--------------------------------

odatse-XAFS

- v1.0.0: 2025-04-11


Main developers
--------------------------------

odatse-XAFS, and FEFF solver module for 2DMAT have been developed by following members.

- odat-XAFS v1.0.0 -

  - Y. Motoyama (The Institute for Solid State Physics, The University of Tokyo)
  - K. Yoshimi (The Institute for Solid State Physics, The University of Tokyo)
  - T. Aoyama (The Institute for Solid State Physics, The University of Tokyo)
  - A. Nakano (National Institute for Fusion Science)
  - T. Hoshi (National Institute for Fusion Science)
