# coding: latin-1
"""
@brief      test log(time=1s)
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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.installhelper.module_install_exceptions import MissingVersionOnPyPiException
from pyquickhelper.loghelper import fLOG


class TestPyPiModule (unittest.TestCase):

    def test_pipy_bug_flask(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ModuleInstall(
            'flask-sqlalchemy', 'pip', mname='flask.ext.sqlalchemy')
        vers = mod.get_pypi_version()
        assert vers is not None

    def test_pipy_bug_ipython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = ModuleInstall(
            'ipython', 'wheel', mname='IPython')
        try:
            vers = mod.get_pypi_version()
        except MissingVersionOnPyPiException:
            vers = "no release version"
            warnings.warn("IPython is is unstable, transitionning to jupyter")
        assert vers is not None


if __name__ == "__main__":
    unittest.main()
