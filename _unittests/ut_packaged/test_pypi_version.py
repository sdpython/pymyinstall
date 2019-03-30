"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.installhelper import get_pypi_version


class TestPypiVersion(unittest.TestCase):

    def test_package_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        ver = get_pypi_version("virtualenv")
        if len(ver) == 0:
            raise Exception(str(ver))


if __name__ == "__main__":
    unittest.main()
