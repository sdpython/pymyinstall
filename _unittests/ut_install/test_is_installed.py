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
    import pyquickhelper as skip_


from src.pymyinstall.packaged import find_module_install
from src.pymyinstall.win_installer import is_package_installed
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


class TestIsInstalled(unittest.TestCase):

    def test_is_installed(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() or sys.version_info[0] == 2:
            return
        mod = find_module_install("imbalanced-learn")
        assert mod.is_installed_local()
        r = is_package_installed(sys.real_prefix if hasattr(sys, "real_prefix") else sys.prefix, "imbalanced-learn")
        assert r


if __name__ == "__main__":
    unittest.main()
