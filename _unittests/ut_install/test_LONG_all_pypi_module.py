"""
@brief      test log(time=80s)
"""

import sys
import os
import unittest
import warnings

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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.installhelper.module_install_exceptions import MissingPackageOnPyPiException, MissingVersionOnPyPiException, AnnoyingPackageException
from src.pymyinstall.packaged import ensae_fullset
from pyquickhelper import fLOG, get_temp_folder


class TestAllPyPiModule (unittest.TestCase):

    def test_all_pipy_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mods = ensae_fullset()
        error = []
        annoying = []
        for mod in mods:
            try:
                v = mod.get_pypi_version()
                fLOG(mod.name, " --> ", v)
                if v is None:
                    error.append((mod.name, "None"))
            except MissingPackageOnPyPiException:
                error.append((mod.name, "pipy"))
            except MissingVersionOnPyPiException:
                error.append((mod.name, "version"))
            except AnnoyingPackageException:
                annoying.append(mod.name)

        if len(error) > 15:
            # we accept some errors
            # joblib seems to give errors from time to time
            # multipledispatch
            # ipython --> jupyter (transitionning)
            raise MissingPackageOnPyPiException("Two many errors\n" +
                                                "\n".join("{0}:{1}".format(a, b) for a, b in sorted(error)))

        if len(annoying) > 0:
            fLOG("Annoying\n", "\n".join(annoying))
            warnings.warn("ANNOYING PACKAGES\n" + "\n".join(annoying))

if __name__ == "__main__":
    unittest.main()
