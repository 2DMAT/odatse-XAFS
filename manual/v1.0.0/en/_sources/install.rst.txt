Installation of odatse-XAFS
================================================================

Prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Python3 (>=3.9)

  - The following Python packages are required.

    - numpy >= 1.14
    - pydantic >= 2.0

  - ODAT-SE version 3.0 and later

  - FEFF 8.5light, or version 9 and later


How to download and install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install ODAT-SE

   - From source files:

     Download source files of ODAT-SE from the repository as follows:

     .. code-block:: bash

	$ git clone https://github.com/issp-center-dev/ODAT-SE.git

     Install ODAT-SE using ``pip`` command:

     .. code-block:: bash

	$ cd ODAT-SE
	$ python3 -m pip install .

     You may add ``--user`` option to install ODAT-SE locally (in ``$HOME/.local``).

     If you run the following command instead, optional packages will also be installed at the same time.

     .. code-block:: bash

	$ python3 -m pip install .[all]

2. Install FEFF

   - Download the source package from the distribution site, and compile the source files.

     - Obtain the source package and create a build directory:

       .. code-block:: bash

          $ git clone https://github.com/eucall-software/feff8.5light.git
          $ cd feff8.5light
          $ mkdir build && cd build

     - For GCC (gfortran), compiler options are required as follows:

       .. code-block:: bash

          $ cmake -DCMAKE_Fortran_FLAGS="-fallow-argument-mismatch -std=legacy" ..
          $ make

     - For intel compiler (ifort), compiler executable is specified as follows:

       .. code-block:: bash

          $ cmake -DCMAKE_Fortran_COMPILER=ifort ..
          $ make

     If the compiliation is successful, an executable file ``feff85L`` will be generated.
     Put ``feff85L`` in a directory listed in the PATH environment variable, or specify the paths to these commands at run time.
     
3. Install odatse-XAFS

   - From source files:

     The source files of odatse-XAFS are available from the GitHub repository. After obtaining the source files, install odatse-XAFS using ``pip`` command as follows:

     .. code-block:: bash

	$ git clone https://github.com/2DMAT/odatse-XAFS.git
	$ cd odatse-XAFS
	$ python3 -m pip install .

     You may add ``--user`` option to install the package locally (in ``$HOME/.local``).

     Then, the library of odatse-XAFS and the command ``odatse-XAFS`` wil be installed.


How to run
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In ODAT-SE, the analysis is done by using a predefined optimization algorithm and a direct problem solver.
There are two ways to do analyses of XAFS:

1. Use odatse-XAFS program included in this package to perform analyses.
   The users prepare an input parameter file in TOML format, and run command with it.
   The type of the inverse problem algorithms can be chosen by the parameter.

2. Write a program for the analysis with odatse-XAFS library and ODAT-SE framework.
   The type of the inverse problem algorithms can be chosen by importing the appropriate module.
   A flexible use would be possible, for example, to include data generation within the program.
   
The types of parameters and the instruction to use the library will be given in the subsequent sections.


How to uninstall
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In order to uninstall odatse-XAFS and ODAT-SE modules, type the following commands:

.. code-block:: bash

   $ python3 -m pip uninstall odatse-XAFS ODAT-SE
