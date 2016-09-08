"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import warnings


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
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper as skip_


from src.pymyinstall.installhelper.install_cmd_helper import run_cmd
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


class TestPyMyUpdateCli(unittest.TestCase):

    def test_update_set_schedule(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            warnings.warn("run_cmd no end on travis")
            return
        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_update.py"))
        cmd = "{0} {1} {2}".format(
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
