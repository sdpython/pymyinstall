"""
@brief      test log(time=20s)
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
    import pyquickhelper
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
    import pyquickhelper


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.installhelper import compare_version
from pyquickhelper import fLOG


class TestDownloadNumpy (unittest.TestCase):

    def test_install_numpy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_numpy")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        if sys.platform.startswith("win") and sys.version_info[0] >= 3:
            m = ModuleInstall(
                "numpy",
                "wheel",
                fLOG=fLOG)
            name = m.get_exewheel_url_link(wheel=True)
            fLOG(m.existing_version)
            r = compare_version(m.existing_version, "1.10.1")
            assert r >= 0
            assert "unoptimized" not in name[0]
            whl = m.download(temp_folder=temp, source="2")
            fLOG(m.version)
            assert os.path.exists(whl)
            assert "unoptimized" not in whl


if __name__ == "__main__":
    unittest.main()
