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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.installhelper.module_install_version import get_module_version
from pyquickhelper.loghelper import fLOG


class TestLONGInstallModule (unittest.TestCase):

    def test_pypi_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ModuleInstall("sphinx", "pip")
        vers = mod.get_pypi_version()
        assert vers >= "1.3.1"

        mod = ModuleInstall("scikit-learn", "wheel", mname="sklearn")
        fLOG(mod)
        vers = mod.get_pypi_version()
        assert vers >= "0.16.1"
        update = mod.has_update()
        fLOG("scikit-learn", update)

        if sys.version_info[0] == 2:
            # we don't test it for Python 2.7
            return

        mod = ModuleInstall("pandas", "wheel")
        fLOG(mod)
        vers = mod.get_pypi_version()
        if vers is None or vers < "0.16.1":
            raise Exception("{0}: {1}".format(mod.name, vers))

        mod = ModuleInstall("openpyxl", "pip", version="2.3.5")
        fLOG(mod)
        vers = mod.get_pypi_version()
        if vers is None or vers < "2.3.5":
            raise Exception("{0}: {1}".format(mod.name, vers))

        update = mod.has_update()
        if update:
            vers = mod.get_pypi_numeric_version()
            fLOG(vers)
        fLOG(update)

    def test_installed_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ModuleInstall("jinja2", "pip")
        res = mod.is_installed_version()
        if not res:
            fLOG(mod)
            fLOG(mod.get_installed_version())
            for k, v in get_module_version(None).items():
                if k[0] in ("j", "J"):
                    fLOG("+++", k, v)
            assert False

        mod = ModuleInstall("pandas", "wheel")
        res = mod.is_installed_version()
        assert res
        fLOG("****", mod.get_installed_version(), mod.get_pypi_version())
        if mod.get_installed_version() != mod.get_pypi_version():
            assert mod.has_update()

if __name__ == "__main__":
    unittest.main()
