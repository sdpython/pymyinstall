"""
@brief      test log(time=200s)

skip this test for regular run
"""

import sys
import os
import unittest
import re

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


from src.pymyinstall.packaged import all_set
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestDownloadAll (unittest.TestCase):

    def test_reg(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        reg = re.compile("(.+?-((cp34)|(py2[.]py3))-none-((win32)|(any)).whl)")
        pp = ["virtualenv-12.0.5-py2.py3-none-any.whl",
              "numpy-1.9.1+mkl-cp34-none-win32.whl"]
        for p in pp:
            r = reg.search(p)
            assert r is not None

    def _download_all(self, pack, temp):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        assert len(pack) > 0

        if sys.version_info[0] == 2:
            # we skip that test on python 2
            return

        for m in pack:
            if m.kind != "pip":
                fLOG(m.name)
                m.fLOG = fLOG
                r = m.download(temp_folder=temp, source="2")
                fLOG(r)

    def test_download_all(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_all")
        pack = all_set()
        self._download_all(pack[1:], temp)

    def test_download_ad3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_download_ad3")
        pack = all_set()
        pack = [_ for _ in pack if _.name == "ad3"]
        self._download_all(pack, temp)


if __name__ == "__main__":
    unittest.main()
