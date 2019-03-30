"""
@brief      test log(time=2290s)

skip this test for regular run
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installcustom import install_python, folder_older_than


class TestDownloadPythonPyEnsae(unittest.TestCase):

    def test_install_python_pyensae(self):
        fLOG(__file__, self._testMethodName, OutputPrint=True)
        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(
            __file__, "temp_py%s_pyensae" % vers, clean=folder_older_than, persistent=True)
        down = get_temp_folder(
            __file__, "temp_py%s_pyensae_download" % vers, clean=True, persistent=True)
        self.assertEqual(len(os.listdir(down)), 0)

        clog = CustomLog(temp)
        install_python(install=True, temp_folder=temp,
                       fLOG=clog, modules="pyensae", custom=True, latest=True,
                       download_folder=temp + "_download")
        if sys.platform.startswith("win"):
            pyt = os.path.join(temp, "python.exe")
            pip = os.path.join(temp, "Scripts", "pip.exe")
            if not os.path.exists(pyt):
                raise FileNotFoundError(pyt)
            if not os.path.exists(pip):
                raise FileNotFoundError(pip)
        else:
            # already checked
            pass


if __name__ == "__main__":
    unittest.main()
