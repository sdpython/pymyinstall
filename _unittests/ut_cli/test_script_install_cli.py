"""
@brief      test log(time=20s)

skip this test for regular run
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


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


from src.pymyinstall.installhelper import run_cmd


class TestScriptInstallCli(unittest.TestCase):

    def test_script_help(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            # run_cmd no end on travis.
            return
        script = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "cli", "pymy_install.py")
        if not os.path.exists(script):
            raise Exception(script)
        scriptu = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "cli", "pymy_update.py")
        if not os.path.exists(script):
            raise Exception(script)

        exe = sys.executable

        cmd = exe + " " + script + " --help"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        if "usage: pymy_install.py" not in out:
            raise Exception(out)

        cmd = exe + " " + scriptu + " --help"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        if "usage: pymy_update.py" not in out:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))

    def test_script_schedule(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "travis":
            # run_cmd no end on travis.
            return
        script = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "cli", "pymy_install.py")
        self.assertTrue(os.path.exists(script))
        scriptu = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "..", "..", "src", "pymyinstall", "cli", "pymy_update.py")
        self.assertTrue(os.path.exists(script))

        exe = sys.executable

        cmd = exe + " " + script + " --schedule --set=minimal --source=2"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        fLOG(out)
        fLOG("---")
        fLOG(err)
        if "[install-check] ## flake8 ## [begin]" not in out and sys.version_info[0] > 2:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}\nFOUND STRING\n{3}".format(cmd,
                                                                               out, err, "[install-check] flake8" not in out))

        cmd = exe + " " + scriptu + " --schedule --set=minimal --source=2"
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
        if "[update-check] ## pycodestyle ## [begin]" not in out and sys.version_info[0] > 2:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))


if __name__ == "__main__":
    unittest.main()
