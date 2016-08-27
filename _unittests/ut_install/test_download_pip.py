"""
@brief      test log(time=75s)
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
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestDownloadPip (unittest.TestCase):

    def test_install_pip(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        fold = get_temp_folder(__file__, "temp_download_pip")
        # This test can fail if the latest version of pyquickhelper is not
        # available for Python 2.7
        m = ModuleInstall("pyquickhelper", "pip", fLOG=fLOG)
        out = m.download(temp_folder=fold)
        assert os.path.exists(out)
        assert "pyquickhelper" in out
        out = m.download(temp_folder=fold)
        assert os.path.exists(out)
        assert "pyquickhelper" in out

    def test_install_pip_deps(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if sys.version_info[0] == 2:
            # disabled on python 2.7
            return
        fold = get_temp_folder(__file__, "temp_download_pip_deps")
        # This test can fail if the latest version of pyquickhelper is not
        # available for Python 2.7
        m = ModuleInstall("pyquickhelper", "pip", fLOG=fLOG)
        out = m.download(temp_folder=fold, deps=True)
        assert os.path.exists(out)
        assert "pyquickhelper" in out
        out = m.download(temp_folder=fold, source="2")
        assert os.path.exists(out)
        assert "pyquickhelper" in out


if __name__ == "__main__":
    unittest.main()
