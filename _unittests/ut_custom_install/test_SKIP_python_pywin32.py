"""
@brief      test log(time=1290s)

skip this test for regular run
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder


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


from src.pymyinstall.installcustom import install_python


class TestDownloadPythonPyWin32 (unittest.TestCase):

    def test_install_python_pywin32(self):
        fLOG(__file__, self._testMethodName, OutputPrint=True)
        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(
            __file__, "temp_py%s_pywin32" % vers, clean=True, persistent=True)
        down = get_temp_folder(
            __file__, "temp_py%s_pywin32_download" % vers, clean=True, persistent=True)
        self.assertEqual(len(os.listdir(down)), 0)

        clog = CustomLog(temp)
        install_python(install=True, temp_folder=temp,
                       fLOG=clog, modules="pywin32", custom=True, latest=True,
                       download_folder=temp + "_download")
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
