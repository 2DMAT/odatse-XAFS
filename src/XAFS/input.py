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

import os
import numpy as np
import shutil

from pathlib import Path
from typing import List, Dict, Optional, TYPE_CHECKING

#from odatse.solver.template import Template
from .template import Template

class Input(object):
    """
    Class for handling input preparation for the FEFF solver.
    """
    root_dir: Path
    output_dir: Path
    dimension: int
    string_list: List[str]
    polarization_list: List[str]
    feff_input_file: Path
    feff_template_file: Path

    def __init__(self, info_base, info_solver):
        """
        Initialize the Input class with the given base and solver information.

        Parameters
        ----------
        info_base : dict
            Object containing base information.
        info_solver : object
            Object containing solver information.
        """
        self.root_dir = info_base["root_dir"]
        self.output_dir = info_base["output_dir"]

        if info_solver.dimension:
            self.dimension = info_solver.dimension
        else:
            self.dimension = len(info_solver.param.string_list)

        # solver.param
        self.string_list = info_solver.param.string_list
        self.polarization_list = info_solver.param.polarization_list
        self.polarization = info_solver.param.polarization

        self.call_dir = ["call_{:02d}".format(k+1) for k in range(len(self.polarization))]

        # solver.config
        self.feff_input_file = Path(info_solver.config.feff_input_file)
        self.remove_work_dir = info_solver.config.remove_work_dir
        self.use_tmpdir = info_solver.config.use_tmpdir

        filename = Path(info_solver.config.feff_template_file).expanduser().resolve()
        self.feff_template_file = self.root_dir / filename
        if not self.feff_template_file.exists():
            raise RuntimeError(
                f"ERROR: feff_template_file ({self.feff_template_file}) does not exist"
            )

        format_list = {
            "*": "{:.8f}",
        }
        self.tmpl = Template(
            file=self.feff_template_file,
            keywords=[*self.string_list, *self.polarization_list],
            format=format_list,
        )

    def prepare(self, x: np.ndarray, args):
        """
        Prepare the input files and working directory.

        Parameters
        ----------
        x : np.ndarray
            Numpy array of input values.
        args : tuple
            Tuple containing step and iset values.

        Returns
        -------
        tuple
            Tuple containing fitted_x_list, workdir, and subdirs.
        """
        for idx, subdir in enumerate(self.call_dir):
            os.makedirs(subdir, exist_ok=True)
            self.tmpl.generate([*x, *self.polarization[idx]], output=os.path.join(subdir, self.feff_input_file))

        return self.call_dir
