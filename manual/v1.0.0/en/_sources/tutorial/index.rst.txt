.. 2dmat documentation master file, created by
   sphinx-quickstart on Tue May 26 18:44:52 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tutorials
================================

``odatse-XAFS`` is a direct problem solver module for the ODAT-SE framework to use FEFF developed by J. J. Rehr of University of Washington.
FEFF evaluates theoretical prediction of X-ray spectroscopy data such as XAFS by the first-principle calculations using multiple scattering for given atomic positions and other parameters.
Consider this to be a direct problem from atomic positions to X-ray spectrum, it turns to an inverse problem to find the atomic position from a given spectrum.
ODAT-SE provides the following five algorithms to solve the inverse problem.

- ``minsearch``

   Nelder-Mead method.

- ``mapper_mpi``

   Searching the entire search grid for a given parameter.

- ``bayes``

   Bayesian optimization.

- ``exchange``

   Sampling by the replica exchange Monte Carlo method.

- ``pamc``

   Sampling by the population annealing Monte Carlo method.

In this tutorial, we will first introduce how to run the direct problem solver ``FEFF``.
Then we will instruct how to run ``mapper_mpi`` for solving inverse problems.
Hereinafter, we use ``odatse-XAFS`` program included in odatse-XAFS with input files in TOML format.

At the end of the tutorial, we will explain how to write your own main program for analyses.


.. toctree::
   :maxdepth: 1

   feff
   mapper
   user_program
