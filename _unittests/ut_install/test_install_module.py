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
    import pyquickhelper
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
    import pyquickhelper


from src.pymyinstall.installhelper.module_install import ModuleInstall, get_module_version
from pyquickhelper import fLOG


class TestInstallModule (unittest.TestCase):

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

        mod = ModuleInstall("pandas", "wheel")
        fLOG(mod)
        vers = mod.get_pypi_version()
        assert vers >= "0.16.1"

        mod = ModuleInstall("openpyxl", "pip", version="1.8.6")
        fLOG(mod)
        vers = mod.get_pypi_version()
        assert vers >= "0.16.1"

        update = mod.has_update()
        if update:
            vers = mod.get_pypi_numeric_version()
            fLOG(vers)
        fLOG(update)
        
    def test_module_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        d = get_module_version(None)
        if len(d) < 10:
            for k,v in sorted(d.items()):
                fLOG(k,v)
            assert False
        
    def test_installed_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ModuleInstall("jinja2", "pip")
        res = mod.is_installed()
        if not res:
            fLOG(mod)
            fLOG(mod.get_installed_version())
            for k,v in get_module_version(None).items():
                if k[0] in ("j","J"):
                    fLOG("+++",k,v)
            assert False
        
        mod = ModuleInstall("pandas", "wheel")
        res = mod.is_installed()
        assert res
        fLOG("****",mod.get_installed_version(), mod.get_pypi_version())
        if mod.get_installed_version() != mod.get_pypi_version():
            assert mod.has_update()
        


if __name__ == "__main__":
    unittest.main()
