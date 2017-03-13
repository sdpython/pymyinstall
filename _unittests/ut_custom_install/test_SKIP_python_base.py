"""
@brief      test log(time=12s)

skip this test for regular run
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
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper as skip_


from src.pymyinstall.installcustom import install_python
from pyquickhelper.loghelper import fLOG, CustomLog


class TestDownloadPython (unittest.TestCase):

    def test_install_python(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        vers = "%d%d" % sys.version_info[:2]
        temp = os.path.join(fold, "temp_python%s" % vers)
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win"):
            clog = CustomLog(temp)
            install_python(install=True, temp_folder=temp, fLOG=clog,
                           download_folder=temp + "_download")
            pyt = os.path.join(temp, "python.exe")
            pip = os.path.join(temp, "Scripts", "pip.exe")
            if not os.path.exists(pyt):
                raise FileNotFoundError(pyt)
            if not os.path.exists(pip):
                raise FileNotFoundError(pip)


if __name__ == "__main__":
    unittest.main()
