"""
@brief      test log(time=1290s)

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
from pyquickhelper.pycode import get_temp_folder


class TestDownloadPythonMinimal(unittest.TestCase):

    def test_install_python_minimal(self):
        fLOG(__file__, self._testMethodName, OutputPrint=True)
        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(
            __file__, "temp_py%s_minimal" % vers, clean=True, max_path=True)
        down = get_temp_folder(
            __file__, "temp_py%s_minimal_download" % vers, clean=True, max_path=True)
        self.assertEqual(len(os.listdir(down)), 0)

        if sys.platform.startswith("win"):
            fLOG("BEGIN in", temp)
            clog = CustomLog(temp)
            install_python(install=True, temp_folder=temp,
                           fLOG=clog, modules="minimal", custom=True, latest=True,
                           download_folder=temp + "_download")
            fLOG("END")
            pyt = os.path.join(temp, "python.exe")
            pip = os.path.join(temp, "Scripts", "pip.exe")
            if not os.path.exists(pyt):
                raise FileNotFoundError(pyt)
            if not os.path.exists(pip):
                raise FileNotFoundError(pip)
            post = os.path.join(temp, "Scripts", "pywin32_postinstall.py")
            with open(post, "r") as f:
                content = f.read()
            if "os.path.exists(dest)" not in content:
                raise Exception(
                    "'os.path.exists(dest)' not found in '{0}'".format(post))


if __name__ == "__main__":
    unittest.main()
