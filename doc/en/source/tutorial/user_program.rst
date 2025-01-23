Analyses by user programs
================================================================

In this tutorial, we will write a user program using odatse-XAFS module and perform analyses. As an example, we adopt Nelder-Mead method for the inverse problem algorithm.


Location of the sample files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample files are located in ``sample/user_program``.
The following files are stored in the folder.

- ``simple.py``

  Source file of the main program. This program reads ``input.toml`` for the parameters.

- ``input.toml``

  Input file of the main program.

- ``mock_data.txt``, ``template.txt``

  Reference file to proceed with calculations in the main program.

- ``ref.txt``

  A file containing the answers you want to seek in this tutorial.

- ``prepare.sh`` , ``do.sh``

  Script prepared for doing all calculation of this tutorial

The following sections describe these files and then show the actual calculation results.


Description of main program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``simple.py`` is a simple program for the analyses using odatse-XAFS module.
The entire source file is shown as follows:

.. code-block:: python

    import numpy as np

    import odatse
    import odatse.algorithm.min_search
    from odatse.extra.XAFS import Solver

    info = odatse.Info.from_file("input.toml")

    solver = Solver(info)
    runner = odatse.Runner(solver, info)
    alg = odatse.algorithm.min_search.Algorithm(info, runner)
    alg.main()


At the beginning of the program, the required modules are imported as listed below.

- ``odatse`` for the main module of ODAT-SE.

- ``odatse.algorithm.min_search`` for the module of the inverse problem algorithm used in this tutorial.

- ``odatse.extra.XAFS`` for the direct problem solver module.

Next, the instances of the classes are created.

- ``odatse.Info`` class

  This class is for storing the parameters. It is created by calling a class method ``from_file`` with a path to TOML file as an argument.

- ``odatse.extra.XAFS.Solver`` class

  This class is for the direct problem solver of the odatse-XAFS module. It is created by passing an instance of Info class.

- ``odatse.Runner`` class

  This class is for connecting the direct problem solver and the inverse problem algorithm. It is created by passing an instance of Solver class and an instance of Info class.

- ``odatse.algorithm.min_search.Algorithm`` class

  This class is for the inverse problem algorithm. In this tutorial, we use ``min_search`` module that implements the optimization by Nelder-Mead method. It is created by passing an instance of Runner class.

After creating the instances of Solver, Runner, and Algorithm in this order, we invoke ``main()`` method of the Algorithm class to start analyses.


Input files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The input file ``input.toml`` for the main program is almost the same as that used in the previous tutorial for grid search.
In the ``algorithm.param`` section, the search region ``min_list`` and ``max_list``, and the initial value ``initial_list`` are specified.
``algorithm.name`` parameter for specifying the algorithm type is ignored.

The template file and the reference experimental data are the same as those in the previous tutorials.


Calculation execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, move to the folder where the sample files are located. (We assume that you are directly under the directory where you downloaded this software.)

.. code-block::

     $ cd sample/user_program

Copy ``feff85L``.

.. code-block::

     $ cp ../../feff8.5light/build/feff85L .

Then, run the main program. The computation time will take only a few minutes on a normal PC.

.. code-block::

     $ python3 simple.py | tee log.txt

The standard output will look as follows.

.. code-block::

    name            : minsearch
    label_list      : ['x_S', 'y_S', 'z_S']
    param.min_list  : [-2.0, -2.0, -2.0]
    param.max_list  : [2.0, 2.0, 2.0]
    param.initial_list: [1.12, 0.96, -1.57]
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 0.600274737286056 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.351331393471473  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.7068794828810981  Polarization [0.0, 0.0, 1.0] R-factor3 = 0.7426133355055966 
    remove directory: Log00000000_00000000
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 0.600274737286056 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.351331393471473  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.7068794828810981  Polarization [0.0, 0.0, 1.0] R-factor3 = 0.7426133355055966 
    remove directory: Log00000001_00000000
    value_01 = 1.37000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 4.784551806438849 Polarization [0.0, 1.0, 0.0] R-factor1 = 1.3408785150447546  Polarization [1.0, 0.0, 0.0] R-factor2 = 2.312170159259668  Polarization [0.0, 0.0, 1.0] R-factor3 = 10.700606745012124 
    remove directory: Log00000002_00000000
    value_01 = 1.12000000
    value_02 = 1.21000000
    value_03 = -1.57000000
    R-factor = 4.117191586678408 Polarization [0.0, 1.0, 0.0] R-factor1 = 1.8602662077424392  Polarization [1.0, 0.0, 0.0] R-factor2 = 1.3907386197304963  Polarization [0.0, 0.0, 1.0] R-factor3 = 9.100569932562289 
    remove directory: Log00000003_00000000
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.32000000
    R-factor = 9.423169910838718 Polarization [0.0, 1.0, 0.0] R-factor1 = 3.3998266834700908  Polarization [1.0, 0.0, 0.0] R-factor2 = 7.455741765410984  Polarization [0.0, 0.0, 1.0] R-factor3 = 17.41394128363508 
    remove directory: Log00000004_00000000
    ...

``value_01``, ``value_02``, and ``value_03`` are the candidate parameters at each step, and ``R-factor`` is the function value at that point.
The results at each step are also written in the folder ``output/LogXXXX_YYYY`` (where XXXX and YYYY are the step counts).
The final estimated parameters will be written to ``output/res.dat``. 
In the current case, the following result will be obtained:

.. code-block::

    fx = 0.5882857603777499
    x_S = 1.152284911047407
    y_S = 0.931495559770223
    z_S = -1.5710799186906792

You can see that we will get the same values as the correct answer data in ``ref.txt``.

Note that ``do.sh`` is available as a script for batch calculation.

