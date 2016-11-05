#-*- coding: utf-8 -*-
"""
@brief      test log(time=33s)
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_


import pyquickhelper
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import execute_notebook_list
from pyquickhelper.pycode import compare_module_version, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import install_python_kernel_for_unittest
import IPython


class TestRunNotebooks(unittest.TestCase):

    def test_run_notebook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            # notebooks are not converted into python 2.7, so not tested
            return

        if "travis" in sys.executable:
            # requires too many dependencies
            return

        if compare_module_version(IPython.__version__, "4.0.0") < 0:
            # IPython is not recent enough
            return

        kernel_name = None if "travis" in sys.executable else install_python_kernel_for_unittest(
            "pymyinstall")

        temp = get_temp_folder(__file__, "temp_run_notebooks")

        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks"))
        keepnote = []
        pyq = os.path.join(os.path.dirname(pyquickhelper.__file__), '..')
        code_init = "import sys\nsys.path.append('{0}')\n".format(
            pyq.replace("\\", "\\\\"))
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb":
                if "install_module" in f:
                    continue
                else:
                    keepnote.append((os.path.join(fnb, f), code_init))
        assert len(keepnote) > 0

        def valid(cell):
            if "snakeviz" in cell:
                return False
            return True

        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src"))]

        if "travis" in sys.executable:
            keepnote = [_ for _ in keepnote if "javascript_extension" not in _ and
                        (not is_travis_or_appveyor() or "example_xgboost" not in _)]

        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths,
            kernel_name=kernel_name)
        assert len(res) > 0
        fails = [(os.path.split(k)[-1], v)
                 for k, v in sorted(res.items()) if not v[0]]
        for f in fails:
            fLOG(f)
        for k, v in sorted(res.items()):
            name = os.path.split(k)[-1]
            fLOG(name, v[0], v[1])
        if len(fails) > 0:
            raise fails[0][1][-1]


if __name__ == "__main__":
    unittest.main()
