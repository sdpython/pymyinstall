"""
@brief      test log(time=1s)
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

from src.pymyinstall.installhelper.module_install import ModuleInstall, get_pypi_version
from src.pymyinstall.installhelper.module_install_exceptions import MissingInstalledPackageException


class TestUpdateModule (unittest.TestCase):

    def test_update_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_update_module")

        if sys.version_info[0] >= 3:
            vers = get_pypi_version("pymyinstall", True)
            fLOG(vers)
            assert len(vers) > 0

            try:
                mod = ModuleInstall("joblib", "pip", fLOG=fLOG)
                mod.update(temp_folder=temp, source="2")
            except MissingInstalledPackageException:
                # not installed
                pass

            mod = ModuleInstall("pandas", "wheel", fLOG=fLOG)
            mod.update(temp_folder=temp, source="2")

            mod = ModuleInstall("xlrd", "pip", fLOG=fLOG)
            mod.update(temp_folder=temp, source="2")


if __name__ == "__main__":
    unittest.main()
