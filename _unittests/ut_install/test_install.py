"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG

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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.installhelper.install_cmd_helper import run_cmd


class TestInstall (unittest.TestCase):

    def test_run_cmd(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        out, err = run_cmd("find", wait=True, fLOG=fLOG)
        self.assertTrue(out is not None)
        self.assertTrue(err is not None)

    def test_install(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2 or "conda" in sys.version:
            # disabled on python 2.7 and anaconda
            return
        m = ModuleInstall("pip", "pip")
        self.assertTrue(m.install())
        m = ModuleInstall("pip", "exe")
        self.assertTrue(m.install())


if __name__ == "__main__":
    unittest.main()
