# coding: latin-1
"""
@brief      test log(time=1s)
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
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper as skip_


from src.pymyinstall.installhelper.install_cmd_helper import run_cmd
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestPyMyInstallCliTool(unittest.TestCase):

    def test_install_tool(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_install_tool")
        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_install.py"))
        cmd = "{0} {1} {2} --force --folder={3}".format(
            sys.executable, script, "graphviz --task=tool --source=zip", temp)
        out, err = run_cmd(cmd, wait=True, do_not_log=True)
        fLOG("----", cmd)
        fLOG(out.replace("\r", "").replace("\n\n", "\n"))
        fLOG("-----")
        fLOG(err.replace("\r", "").replace("\n\n", "\n"))
        content = os.listdir(temp)
        assert content


if __name__ == "__main__":
    unittest.main()