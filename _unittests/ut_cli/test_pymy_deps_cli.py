"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import warnings
import subprocess


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


class TestPyMyDepsCli(unittest.TestCase):

    def test_install_deps(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_deps.py"))
        cmd = "{0} -u {1} {2}".format(
            sys.executable, script, "pandas")
        try:
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                               communicate=True, timeout=120)
        except subprocess.CalledProcessError as e:
            mes = "CMD\n{0}\nOUT\n{1}\nERR\n{2}".format(
                e.cmd, e.output, e.stderr.read() if e.stderr else "")
            raise Exception(mes) from e
        out = out.strip()
        if len(out) == 0:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
        else:
            fLOG(out)
            if sys.version_info[0] == 2:
                # failing on Python 2.7
                return
            if "pandas" not in out:
                raise Exception(
                    "(1)CMD:\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))
            if "['pandas']" not in out:
                raise Exception(
                    "(2)CMD:\n{0}\nOUT\n{1}\nERR\n{2}".format(cmd, out, err))


if __name__ == "__main__":
    unittest.main()
