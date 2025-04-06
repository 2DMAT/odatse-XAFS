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

Copy ``feff85L`` to the current directory.

.. code-block::

     $ cp ../feff/feff85L .

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
    R-factor = 0.7762817472030608 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.26218705791753616  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.3520528886264926  Polarization [0.0, 0.0, 1.0] R-factor3 = 1.7146052950651536 
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 0.7762817472030608 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.26218705791753616  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.3520528886264926  Polarization [0.0, 0.0, 1.0] R-factor3 = 1.7146052950651536 
    value_01 = 1.37000000
    value_02 = 0.96000000
    value_03 = -1.57000000
    R-factor = 7.006992151846735 Polarization [0.0, 1.0, 0.0] R-factor1 = 2.097374935360426  Polarization [1.0, 0.0, 0.0] R-factor2 = 3.7994697622892972  Polarization [0.0, 0.0, 1.0] R-factor3 = 15.124131757890481 
    value_01 = 1.12000000
    value_02 = 1.21000000
    value_03 = -1.57000000
    R-factor = 5.73016510319226 Polarization [0.0, 1.0, 0.0] R-factor1 = 3.5024285153919115  Polarization [1.0, 0.0, 0.0] R-factor2 = 2.0041674778416843  Polarization [0.0, 0.0, 1.0] R-factor3 = 11.683899316343183 
    value_01 = 1.12000000
    value_02 = 0.96000000
    value_03 = -1.32000000
    R-factor = 56.31862514558586 Polarization [0.0, 1.0, 0.0] R-factor1 = 6.4008790163862015  Polarization [1.0, 0.0, 0.0] R-factor2 = 9.109651695414557  Polarization [0.0, 0.0, 1.0] R-factor3 = 153.44534472495684 
    value_01 = 1.28666667
    value_02 = 1.12666667
    value_03 = -1.82000000
    R-factor = 32.91890925644038 Polarization [0.0, 1.0, 0.0] R-factor1 = 2.2301127998431753  Polarization [1.0, 0.0, 0.0] R-factor2 = 5.050496886392638  Polarization [0.0, 0.0, 1.0] R-factor3 = 91.47611808308534 
    value_01 = 1.24500000
    value_02 = 1.08500000
    value_03 = -1.69500000
    R-factor = 14.218592101199897 Polarization [0.0, 1.0, 0.0] R-factor1 = 3.3863023885318193  Polarization [1.0, 0.0, 0.0] R-factor2 = 5.0060964449177945  Polarization [0.0, 0.0, 1.0] R-factor3 = 34.26337747015008 
    eval: x=[ 1.12  0.96 -1.57], fun=0.7762817472030608
    value_01 = 1.16166667
    value_02 = 1.00166667
    value_03 = -1.44500000
    R-factor = 7.048842595863635 Polarization [0.0, 1.0, 0.0] R-factor1 = 1.224939069135288  Polarization [1.0, 0.0, 0.0] R-factor2 = 1.8540984688270858  Polarization [0.0, 0.0, 1.0] R-factor3 = 18.06749024962853 
    value_01 = 1.18250000
    value_02 = 1.02250000
    value_03 = -1.50750000
    R-factor = 0.4469433592171206 Polarization [0.0, 1.0, 0.0] R-factor1 = 0.2535379790399123  Polarization [1.0, 0.0, 0.0] R-factor2 = 0.20069518356682897  Polarization [0.0, 0.0, 1.0] R-factor3 = 0.8865969150446205 
    eval: x=[ 1.1825  1.0225 -1.5075], fun=0.4469433592171206
    ...

``value_01``, ``value_02``, and ``value_03`` are the candidate parameters at each step, and ``R-factor`` is the function value at that point.
The results at each step are also written in the folder ``output/LogXXXX_YYYY`` (where XXXX and YYYY are the step counts).
The final estimated parameters will be written to ``output/res.dat``. 
In the current case, the following result will be obtained:

.. code-block::

    fx = 0.20606977805890725
    x_S = 1.125299780290939
    y_S = 0.9597181918334485
    z_S = -1.596967599355829

You can see that we will get the same values as the correct answer data in ``ref.txt``.

Note that ``do.sh`` is available as a script for batch calculation.

