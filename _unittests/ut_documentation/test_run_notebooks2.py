# -*- coding: utf-8 -*-
"""
@brief      test log(time=26s)
"""

import sys
import os
import unittest
import pyquickhelper
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import (
    execute_notebook_list, execute_notebook_list_finalize_ut)
from pyquickhelper.pycode import is_travis_or_appveyor, skipif_appveyor
import pymyinstall


class TestRunNotebooks2(unittest.TestCase):

    def a_test_run_notebook(self, name):
        temp = get_temp_folder(
            __file__, "temp_run_notebooks2_{0}".format(name))

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

        if is_travis_or_appveyor() == "travis":
            keepnote = [_ for _ in keepnote if "javascript_extension" not in _ and
                        (not is_travis_or_appveyor() or "example_xgboost" not in _)]

        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=pymyinstall)

    @skipif_appveyor("Proactor event loop does not implement add_reader")
    def test_notebook_pivottablejs(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_run_notebook("pivottablejs")


if __name__ == "__main__":
    unittest.main()
