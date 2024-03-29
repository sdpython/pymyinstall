"""
@brief      test log(time=1290s)

skip this test for regular run
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installcustom import install_python


class TestDownloadPythonMinimal(unittest.TestCase):

    def test_install_python_minimal(self):
        fLOG(__file__, self._testMethodName, OutputPrint=True)
        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(
            __file__, "temp_py%s_minimal" % vers, clean=True, persistent=True)
        down = get_temp_folder(
            __file__, "temp_py%s_minimal_download" % vers, clean=True, persistent=True)
        self.assertEqual(len(os.listdir(down)), 0)

        fLOG("BEGIN in", temp)
        clog = CustomLog(temp)
        install_python(install=True, temp_folder=temp,
                       fLOG=clog, modules="minimal", custom=True, latest=True,
                       download_folder=temp + "_download")
        fLOG("END")
        if sys.platform.startswith("win"):
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
                raise AssertionError(
                    "'os.path.exists(dest)' not found in '{0}'".format(post))
        else:
            # already checked
            pass


if __name__ == "__main__":
    unittest.main()
