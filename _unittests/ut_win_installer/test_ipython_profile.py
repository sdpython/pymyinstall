"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.win_installer.win_ipython_helper import ipython_create_profile, ipython_update_profile
from pymyinstall.installhelper.run_cmd import RunCmdException


class TestIPythonProfile(unittest.TestCase):

    def test_ipython_profile(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        python_path = os.path.abspath(os.path.dirname(sys.executable))
        temp = get_temp_folder(__file__, "temp_ipython_profile")
        try:
            path = ipython_create_profile(
                temp, python_path, name="ZZZ", fLOG=fLOG)
        except (FileNotFoundError, RunCmdException) as e:
            if "_venv" in str(e) and (".exe" in str(e) or "/_venv/" in str(e)):
                # ipython.exe not present in virtual environment
                warnings.warn("needs to add custom command line")
                return
            else:
                raise Exception(
                    "Error message\n---\n{0}\n---".format(e)) from e

        fLOG(path)
        assert os.path.exists(path)

        if sys.platform.startswith("win"):
            ipython_update_profile(path)
            profile = os.path.join(path, "ipython_kernel_config.py")
            with open(profile, "r", encoding="utf8") as f:
                lines = f.readlines()

            exp = "c.ContentsManager.hide_globs = ['__pycache__',"
            nb = 0
            for line in lines:
                if line.startswith(exp):
                    nb += 1
            assert nb > 0
        else:
            profile = os.path.join(path, "ipython_config.py")
            assert os.path.exists(profile)


if __name__ == "__main__":
    unittest.main()
