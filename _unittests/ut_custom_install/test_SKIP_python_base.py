"""
@brief      test log(time=12s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installcustom import install_python, folder_older_than


class TestDownloadPythonBase(unittest.TestCase):

    def test_install_python_base(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(__file__, "temp_py%s_base" %
                               vers, persistent=True, clean=folder_older_than)
        down = get_temp_folder(
            __file__, "temp_py%s_base_download" % vers, clean=True, persistent=True)
        self.assertEqual(len(os.listdir(down)), 0)

        clog = CustomLog(temp) if __name__ != "__main__" else fLOG
        install_python(install=True, temp_folder=temp, fLOG=clog,
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
