# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import os
import unittest
import pyquickhelper
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
import pymyinstall


class TestRunNotebooks4(unittest.TestCase):

    def a_test_run_notebook(self, name):
        temp = get_temp_folder(
            __file__, "temp_run_notebooks4_{0}".format(name))

        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks"))
        keepnote = []
        pyq = os.path.join(os.path.dirname(pyquickhelper.__file__), '..')
        code_init = "import sys\nsys.path.append('{0}')\n".format(
            pyq.replace("\\", "\\\\"))
        for f in os.listdir(fnb):
            if name not in f:
                continue
            if os.path.splitext(f)[-1] == ".ipynb":
                if "install_module" in f:
                    continue
                else:
                    keepnote.append((os.path.join(fnb, f), code_init))
        self.assertTrue(len(keepnote) > 0)

        def valid(cell):
            if "snakeviz" in cell:
                return False
            return True

        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "jyquickhelper", "src"))
        ]

        if len(keepnote) == 0:
            raise ValueError("No notebook for name='{0}'".format(name))

        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=pymyinstall)

    def test_notebook_example_xgboost(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_run_notebook("example_xgboost")


if __name__ == "__main__":
    unittest.main()
