"""
@brief      test log(time=32s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder

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


from src.pymyinstall.installhelper.install_cmd_helper import run_cmd


class TestPyMyInstallCliTool(unittest.TestCase):

    def test_install_tool(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if not sys.platform.startswith("win"):
            # No installation on linux.
            return
        temp = get_temp_folder(__file__, "temp_install_tool")
        this = os.path.abspath(os.path.dirname(__file__))
        script = os.path.normpath(os.path.join(
            this, "..", "..", "src", "pymyinstall", "cli", "pymy_install.py"))
        cmd = "{0} -u {1} {2} --force --folder={3}".format(
            sys.executable, script, "graphviz --task=tool --source=zip", temp)
        out, err = run_cmd(cmd, wait=True)
        fLOG("----", cmd)
        fLOG(out.replace("\r", "").replace("\n\n", "\n"))
        fLOG("-----")
        fLOG(err.replace("\r", "").replace("\n\n", "\n"))
        content = os.listdir(temp)
        if not content:
            comp = "OUT:\n{0}\nERR:\n{1}".format(out, err)
            if sys.platform.startswith("win"):
                raise Exception("content is empty for: " + temp + "\n" + comp)


if __name__ == "__main__":
    unittest.main()
