"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.module_install import ModuleInstall
from pymyinstall.installhelper.install_cmd_helper import run_cmd


class TestInstall (unittest.TestCase):

    def test_run_cmd(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        out, err = run_cmd("find", wait=True, fLOG=fLOG)
        self.assertTrue(out is not None)
        self.assertTrue(err is not None)

    def test_install(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        m = ModuleInstall("pip", "pip")
        self.assertTrue(m.install())
        m = ModuleInstall("pip", "exe")
        self.assertTrue(m.install())


if __name__ == "__main__":
    unittest.main()
