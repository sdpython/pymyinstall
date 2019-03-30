"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.module_install import ModuleInstall


class TestInstallModuleIsInstalled (unittest.TestCase):

    def test_module_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ModuleInstall("autopep8", "pip", fLOG=fLOG)
        self.assertTrue(mod.is_installed_local())
        self.assertTrue(mod.is_installed_local_cmd())


if __name__ == "__main__":
    unittest.main()
