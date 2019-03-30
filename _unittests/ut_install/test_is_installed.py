"""
@brief      test log(time=1s)
"""
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor
from pymyinstall.packaged import find_module_install
from pymyinstall.win_installer import is_package_installed


class TestIsInstalled(unittest.TestCase):

    def test_is_installed_imbalanced_learn(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() or sys.version_info[0] == 2:
            return
        mod = find_module_install("imbalanced-learn")
        self.assertTrue(mod.is_installed_local())
        r = is_package_installed(sys.real_prefix if hasattr(  # pylint: disable=E1101
            sys, "real_prefix") else sys.prefix, "imbalanced-learn")
        self.assertTrue(r)


if __name__ == "__main__":
    unittest.main()
