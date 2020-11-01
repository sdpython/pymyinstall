"""
@brief      test log(time=63s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor
from pymyinstall.installhelper.install_cmd_helper import run_cmd


class TestPyMyUpdateCli(unittest.TestCase):

    def test_update_set_schedule(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            # run_cmd no end on travis.
            return
        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_update.py"))
        cmd = "{0} -u {1} {2}".format(
            sys.executable, script, "--set=pyquickhelper --schedule")
        out, err = run_cmd(cmd, wait=True)
        if len(out) == 0:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))


if __name__ == "__main__":
    unittest.main()
