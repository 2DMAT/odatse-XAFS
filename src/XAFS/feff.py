# odatse-XAFS -- X-ray Absorption Fine Structure solver module for ODAT-SE
# Copyright (C) 2024- The University of Tokyo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see http://www.gnu.org/licenses/.
# 

import os
import sys
import subprocess
import time

from typing import List
from pathlib import Path

import numpy as np
from pydantic import ValidationError

import odatse
from .input import Input
from .output import Output
from .parameter import SolverInfo
from odatse.solver.util import Workdir, set_solver_path, run_by_subprocess


class Solver(odatse.solver.SolverBase):
    """
    Solver class for handling the execution of the FEFF solver for XAFS data analysis.
    """

    path_to_solver: Path

    def __init__(self, info: odatse.Info):
        """
        Initialize the Solver instance.

        Parameters
        ----------
        info : odatse.Info
            Information required to configure the solver.
        """
        super().__init__(info)
        self._name = "xafs"

        try:
            info_solver = SolverInfo(**info.solver)
        except ValidationError as e:
            print("ERROR: {}".format(e))
            sys.exit(1)
        self.info = info_solver

        self.path_to_solver = set_solver_path(info_solver.config.feff_exec_file, self.root_dir)

        self.input = Input(info.base, info_solver)
        self.output = Output(info_solver)
        self.result = None

    def evaluate(self, x: np.ndarray, args=(), nprocs: int = 1, nthreads: int = 1) -> float:
        """
        Evaluate the solver with the given parameters.

        Parameters
        ----------
        x : np.ndarray
            Input array for the solver.
        args : tuple, optional
            Additional arguments for the solver. Defaults to ().
        nprocs : int, optional
            Number of processes to use. Defaults to 1.
        nthreads : int, optional
            Number of threads to use. Defaults to 1.

        Returns
        -------
        float
            Result of the evaluation.
        """
        work_dir = "Log{:08d}_{:08d}".format(*args)
        with Workdir(work_dir, remove=self.info.config.remove_work_dir, use_tmpdir=self.info.config.use_tmpdir):

            subdirs = self.input.prepare(x, args)

            cwd = os.getcwd()
            for subdir in subdirs:
                os.chdir(subdir)
                self._run(nprocs, nthreads)
                # time.sleep(3)
                os.chdir(cwd)

            result = self.output.get_results(x, subdirs)
        return result

    def _run(self, nprocs: int = 1, nthreads: int = 1) -> None:
        """
        Run the solver.

        Parameters
        ----------
        nprocs : int, optional
            Number of processes to use. Defaults to 1.
        nthreads : int, optional
            Number of threads to use. Defaults to 1.
        """
        try:
            run_by_subprocess([str(self.path_to_solver)])
        except subprocess.CalledProcessError as e:
            print("WARNING: NO ATOMS CLOSE ENOUGH TO OVERLAP ATOM    1,  UNIQUE POT    0!!  Rmt set to Rnorman.  May be error in input file. {}".format(e))
