import os
import sys

SOURCE_PATH = os.path.join(os.path.dirname(__file__), '../../src')
sys.path.append(SOURCE_PATH)

class switch_dir:
    def __init__(self, d):
        self.d = d
    def __enter__(self):
        self.owd = os.getcwd()
        os.chdir(self.d)
        return self
    def __exit__(self, ex_type, ex_value, tb):
        os.chdir(self.owd)
        return ex_type is None

def test_parameters():
    import tomli
    from XAFS.parameter import SolverInfo
    import numpy as np

    input_data = """
    [solver]
    name = "feff"
    dimension = 3

    [solver.config]
    #feff_exec_file  = "../bin/feff85L"
    remove_work_dir = false
    use_tmpdir = false

    [solver.param]
    string_list = ["value_01", "value_02","value_03"]
    polarization_list = ["polarization_01", "polarization_02", "polarization_03"]
    polarization = [ [0,1,0], [1,0,0], [0,0,1] ]
    k_range = [3.6, 10]

    [solver.reference]
    path_epsilon = "mock_data.txt"
    """

    params = tomli.loads(input_data)
    info = SolverInfo(**params["solver"])

    assert info.config.feff_exec_file == "feff85L"
    assert info.config.feff_input_file == "feff.inp"
    assert info.config.feff_output_file == "chi.dat"
    assert np.isclose(info.param.calculated_first_k, 3.6)
    assert np.isclose(info.param.calculated_last_k, 10.0)

def test_input_file():
    import odatse
    from XAFS.input import Input
    from XAFS.parameter import SolverInfo
    import shutil
    from tempfile import TemporaryDirectory
    import tomli

    xval = [1.12, 0.96, -1.57]
    arg = (13, 7)

    test_dir = os.path.dirname(__file__)

    with open(os.path.join(test_dir, "input.toml"), "rb") as f:
        params = tomli.load(f)

    with TemporaryDirectory() as work_dir:
        with switch_dir(work_dir):
            shutil.copy(os.path.join(test_dir, "template.txt"), "template.txt")

            info = odatse.Info(params)
            info_s = SolverInfo(**info.solver)
            input = Input(info.base, info_s)

            input.prepare(xval, arg)

            data_dir = "Log{:08d}_{:08d}".format(*arg)

            npol = len(info_s.param.polarization)
            for idx in range(1, 1+npol):
                with open(os.path.join(data_dir, "call_{:02d}".format(idx), "feff.inp"), "r") as f:
                    inp = f.readlines()
                with open(os.path.join(test_dir, "feff.in_{:d}_ref".format(idx)), "r") as f:
                    inp_ref = f.readlines()

                for i, (a, b) in enumerate(zip(inp_ref, inp)):
                    assert a == b, "call_{:02d}/feff.in: line {} differs".format(idx, i)

def test_get_results():
    import odatse
    from XAFS.output import Output
    from XAFS.parameter import SolverInfo
    import shutil
    from tempfile import TemporaryDirectory
    import tomli
    import numpy as np

    xval = [1.12, 0.96, -1.57]
    arg = (13, 7)
    fval = 0.22284188252224896

    test_dir = os.path.dirname(__file__)

    with open(os.path.join(test_dir, "input.toml"), "rb") as f:
        params = tomli.load(f)

        
    with TemporaryDirectory() as work_dir:
        with switch_dir(work_dir):
            info = odatse.Info(params)
            info_s = SolverInfo(**info.solver)

            npol = len(info_s.param.polarization)
            subdirs = ["call_{:02d}".format(i+1) for i in range(npol)]
            for idx, d in enumerate(subdirs, 1):
                os.makedirs(d)
                shutil.copy(os.path.join(test_dir, "chi_{}.dat".format(idx)), os.path.join(d, "chi.dat"))

            shutil.copy(os.path.join(test_dir, "mock_data.txt"), "mock_data.txt")

            output = Output(info.base, info_s)

            v = output.get_results(xval, subdirs)
            assert np.isclose(v, fval)
