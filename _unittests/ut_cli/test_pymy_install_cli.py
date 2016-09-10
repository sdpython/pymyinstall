"""
@brief      test log(time=1s)
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
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.pycode import is_travis_or_appveyor


class TestPyMyInstallCli(unittest.TestCase):

    def test_install_set_schedule(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_install.py"))
        cmd = "{0} {1} {2}".format(
            sys.executable, script, "--set=pyquickhelper --schedule")
        try:
            out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                               communicate=False, timeout=60)
        except subprocess.CalledProcessError as e:
            mes = "CMD\n{0}\nOUT\n{1}\nERR\n{2}".format(
                e.cmd, e.output, e.stderr.read() if e.stderr else "")
            raise Exception(mes) from e
        if len(out) == 0:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))

    def test_install_download(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_install_download")
        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_install.py"))
        cmd = "{0} {1} {2} --force --folder={3}".format(
            sys.executable, script, "colorama xlrd --download", temp)
        out, err = run_cmd(cmd, wait=True, fLOG=fLOG,
                           communicate=True, timeout=20)
        fLOG("----", cmd)
        fLOG(out.replace("\r", "").replace("\n\n", "\n"))
        fLOG("-----")
        fLOG(err.replace("\r", "").replace("\n\n", "\n"))
        if len(out) == 0 and is_travis_or_appveyor() == "appveyor":
            warnings.warn(
                "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            return
        if "downloaded modules" not in out:
            raise Exception(
                "CMD: {0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
        content = os.listdir(temp)
        if len(content) != 2:
            if is_travis_or_appveyor() == "appveyor":
                warnings.warn(
                    "CLI ISSUE cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))
            else:
                raise Exception(
                    "cmd:\n{0}\nOUT:\n{1}\nERR\n{2}".format(cmd, out, err))


if __name__ == "__main__":
    unittest.main()
