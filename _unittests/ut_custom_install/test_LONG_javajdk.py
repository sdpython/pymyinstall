"""
@brief      test log(time=45s)
"""
import sys
import os
import unittest
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


from src.pymyinstall.installcustom import install_javajdk, ManualDownloadException


class TestJavaJdk (unittest.TestCase):

    def test_install_javajdk(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_javajdk")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        try:
            r = install_javajdk(temp_folder=temp, fLOG=fLOG, install=False)
            fLOG(r)
        except ManualDownloadException:
            pass


if __name__ == "__main__":
    unittest.main()
