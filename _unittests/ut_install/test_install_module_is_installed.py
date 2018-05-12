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
