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


from src.pymyinstall.packaged import find_module_install
from src.pymyinstall.installhelper import compare_version, get_wheel_version
from pyquickhelper.loghelper import fLOG


class TestDownloadAzure(unittest.TestCase):

    def test_install_azure(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_download_azure")
        if not os.path.exists(temp):
            os.mkdir(temp)
        for _ in os.listdir(temp):
            if os.path.isfile(os.path.join(temp, _)):
                os.remove(os.path.join(temp, _))

        r1 = compare_version("2.0.0rc5", "1.0.3")
        r2 = compare_version("1.0.3", "2.0.0rc5")
        assert r1 * r2 < 0
        assert r1 > 0
        if sys.platform.startswith("win") and sys.version_info[0] >= 3:
            m = find_module_install("azure")
            if m.pip_options is None:
                raise Exception("no pip_options, issue '{0}'".format(m))
            m.fLOG = fLOG
            name = m.download(temp_folder=temp)
            v = get_wheel_version(name)
            r = compare_version(v, "1.9.9")
            if r <= 0:
                raise Exception(
                    "unexception version for '{0}',\nshould be >= 1.9.9 not '{1}'".format(name, v))
            fLOG(m.version, v, name)
            assert os.path.exists(name)
            assert "azure" in name


if __name__ == "__main__":
    unittest.main()
