"""
@brief      test log(time=2s)

skip this test for regular run
"""

import sys
import os
import unittest
import re
import pandas

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
    import pyquickhelper
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
    import pyquickhelper


from pyquickhelper import fLOG, df2rst
from src.pymyinstall.installhelper import run_cmd


class TestScriptInstall(unittest.TestCase):

    def test_script_help(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        script = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "scripts", "pymy_install.py")
        assert os.path.exists(script)
        scriptu = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "scripts", "pymy_update.py")
        assert os.path.exists(script)

        exe = sys.executable

        cmd = exe + " " + script + " --help"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        assert "usage: pymy_install.py" in out

        cmd = exe + " " + scriptu + " --help"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        assert "usage: pymy_update.py" in out

    def test_script_schedule(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        script = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "scripts", "pymy_install.py")
        assert os.path.exists(script)
        scriptu = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "scripts", "pymy_update.py")
        assert os.path.exists(script)

        exe = sys.executable

        cmd = exe + " " + script + " --schedule --set=minimal"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        fLOG(out)
        fLOG("---")
        fLOG(err)
        assert "check module:  flake8" in out

        cmd = exe + " " + scriptu + " --schedule --set=minimal"
        out, err = run_cmd(cmd, wait=True)
        assert "check module:  flake8" in out


if __name__ == "__main__":
    unittest.main()
