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


from src.pymyinstall.installhelper.module_install import ModuleInstall
from src.pymyinstall.installhelper import compare_version
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder


class TestDownloadNumpy (unittest.TestCase):

    def test_install_numpy(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win") and sys.version_info[0] >= 3:
            temp = get_temp_folder(__file__, "temp_download_numpy")
            source = "2" if is_travis_or_appveyor() else None
            m = ModuleInstall(
                "numpy",
                "wheel",
                fLOG=fLOG,
                source=source)
            name = m.get_exewheel_url_link(wheel=True)
            fLOG(m.existing_version)
            r = compare_version(m.existing_version, "1.10.1")
            self.assertTrue(r >= 0)
            self.assertTrue("unoptimized" not in name[0])
            whl = m.download(temp_folder=temp, source="2")
            fLOG(m.version)
            self.assertTrue(os.path.exists(whl))
            self.assertTrue("unoptimized" not in whl)


if __name__ == "__main__":
    unittest.main()
