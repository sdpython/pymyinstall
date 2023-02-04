"""
@brief      test log(time=999s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder
from pymyinstall.installhelper.install_cmd_helper import run_cmd


class TestPyMyStatusCli(unittest.TestCase):

    def test_status(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            # run_cmd no end on travis.
            return
        temp = get_temp_folder(__file__, "temp_status")
        outfile = os.path.join(temp, "modules.xlsx")
        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_status.py"))
        cmd = "{0} -u {1} {2}".format(
            sys.executable, script, "numpy --out={0}".format(outfile))
        fLOG(cmd)
        out, err = run_cmd(cmd, wait=True)
        if len(out) == 0:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
                return
            raise AssertionError(
                "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
        if len(err) > 0:
            raise AssertionError(
                "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
        if not os.path.exists(outfile):
            raise AssertionError(outfile)
        fLOG(out)


if __name__ == "__main__":
    unittest.main()
