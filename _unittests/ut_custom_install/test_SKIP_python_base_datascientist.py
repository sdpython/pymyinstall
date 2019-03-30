"""
@brief      test log(time=12s)
"""
import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.installcustom import install_python, folder_older_than
from pymyinstall.packaged.packaged_config import datascientistbase_set


class TestDownloadPythonDataScienstist(unittest.TestCase):

    def test_install_python_data_scientist(self):
        """
        This test is using pymyinstall from pypi not the latest version
        of the sources.
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = datascientistbase_set()
        self.assertTrue(res is not None)
        if not any(filter(lambda m: m.name == "toolz", res)):
            raise ImportError("toolz not found.")

        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(
            __file__, "temp_py%s_ds" % vers, clean=folder_older_than, persistent=True)

        if __name__ == "__main__":
            clog = fLOG
            do_clean = False
        else:
            clog = CustomLog(temp)
            do_clean = True

        down = get_temp_folder(
            __file__, "temp_py%s_ds_download" % vers, clean=do_clean, persistent=True)
        if __name__ != "__main__":
            self.assertEqual(len(os.listdir(down)), 0)

        install_python(install=True, temp_folder=temp,
                       fLOG=clog, modules="datascientistbase", custom=True, latest=True,
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
