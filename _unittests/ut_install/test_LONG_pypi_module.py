"""
@brief      test log(time=1s)
"""

import sys
import os
import unittest
import warnings
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
from src.pymyinstall.installhelper.module_install_exceptions import MissingVersionOnPyPiException


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
