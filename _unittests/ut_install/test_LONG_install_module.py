"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.module_install import ModuleInstall
from pymyinstall.installhelper.module_install_version import get_module_version


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

        mod = ModuleInstall("pandas", "wheel")
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
        if res is not None:
            raise AssertionError(
                "Issue with module (res empty) %r." % mod)
        fLOG("****", mod.get_installed_version(), mod.get_pypi_version())
        if mod.get_installed_version() != mod.get_pypi_version():
            if not mod.has_update():
                raise AssertionError(
                    "Issue with module %r." % mod)


if __name__ == "__main__":
    unittest.main()
