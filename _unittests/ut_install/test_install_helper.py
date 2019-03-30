"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper.module_install_version import get_wheel_version


class TestInstallHelper(unittest.TestCase):

    def test_version_name(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        v = get_wheel_version("rpy2-2.6.0-cp34-none-win_amd64.whl")
        if v != "2.6.0":
            raise Exception(v)

        v = get_wheel_version("tornado-4.2-cp34-none-win_amd64.whl")
        if v != "4.2":
            raise Exception(v)


if __name__ == "__main__":
    unittest.main()
