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


from src.pymyinstall.installhelper.module_install_exceptions import MissingPackageOnPyPiException
from src.pymyinstall.installhelper.module_install_exceptions import MissingVersionOnPyPiException, AnnoyingPackageException
from src.pymyinstall.packaged import ensae_fullset
from pyquickhelper.loghelper import fLOG


class TestAllPyPiModule (unittest.TestCase):

    def test_pipy_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        subset = {"cubehelix", "dataspyre", "ete3", "heapdict", "libpython", "natgrid", "onedrive-sdk-python",
                  "orange3", "orange3-associate", "orange3-network", "orange3-text",
                  "py-earth", "pyexecjs", "pymc3", "pyreact", "pythonqwt", "qtpy"}

        mods = ensae_fullset()
        mods = [_ for _ in mods if _.name in subset]
        self._pipy_version(mods, nbmax=15)

    def test_all_pipy_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.version_info[0] == 2:
            return

        mods = ensae_fullset()
        self._pipy_version(mods)

    def _pipy_version(self, mods, nbmax=15):
        error = []
        annoying = []
        for mod in mods:
            try:
                v = mod.get_pypi_version()
                fLOG(mod.name, " --> ", v)
                if v is None:
                    error.append((mod.name, "None", None))
            except MissingPackageOnPyPiException as e:
                error.append((mod.name, "pipy", e))
            except MissingVersionOnPyPiException as ee:
                error.append((mod.name, "version", ee))
            except AnnoyingPackageException as eee:
                annoying.append((mod.name, "?", eee))

        if len(error) > nbmax:
            # we accept some errors
            # joblib seems to give errors from time to time
            # multipledispatch
            # ipython --> jupyter (transitionning)
            raise MissingPackageOnPyPiException("Two many errors\n" +
                                                "\n".join("{0}:{1}\n   {2}".format(a, b, c) for a, b, c in sorted(error)))

        if len(annoying) > 0:
            ans = "\n".join(str(_) for _ in annoying)
            fLOG("Annoying\n", ans)
            warnings.warn("ANNOYING PACKAGES\n{0}".format(ans))


if __name__ == "__main__":
    unittest.main()
