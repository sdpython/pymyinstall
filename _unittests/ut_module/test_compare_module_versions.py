"""
@brief      test log(time=5s)
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


from pyquickhelper.loghelper import fLOG, CustomLog
from src.pymyinstall.packaged import all_set
from src.pymyinstall.installhelper import get_wheel_version, compare_version
from src.pymyinstall.installhelper.module_install_exceptions import MissingWheelException


class TestCompareVersion(unittest.TestCase):

    def test_compare_versions(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if not sys.platform.startswith("win"):
            # useful only on Windows
            return

        if sys.version_info[0] == 2:
            # not maintaining for Python 2.7
            return

        mods = [mod for mod in all_set() if mod.kind in ("wheel",)]
        fLOG(len(mods))
        assert len(mods) > 0
        clog = CustomLog(os.path.dirname(__file__),
                         "windows_modules_versions.txt")

        diff = []
        for i, mod in enumerate(mods[0:]):
            if mod.name in ["PySide", "cgal_bindings", "ad3"]:
                # skipping modules not available
                continue

            if i % 10 == 0:
                fLOG(i, mod)
            try:
                url1 = mod.get_exewheel_url_link(wheel=True)
            except MissingWheelException:
                url1 = None
            try:
                url2 = mod.get_exewheel_url_link2(wheel=True, source="2")
            except MissingWheelException:
                url2 = None
            if url1 is None and url2 is None:
                fLOG("missing package on both sides", mod)
                clog("missing package on both sides", mod)
                continue
            # fLOG(i, url1, url2)
            n1 = url1[-1] if url1 is not None else None
            n2 = url2[-1] if url2 is not None else None
            v1 = get_wheel_version(n1) if n1 is not None else None
            v2 = get_wheel_version(n2) if n2 is not None else None
            cmp = compare_version(
                v1, v2) if v1 is not None and v2 is not None else -2
            if cmp != 0:
                fLOG("---", i, v1, v2, mod.name)
                clog("---", i, v1, v2, mod.name)
                if v1 is not None and v2 is not None and not ("rc1" in v1 or "rc1" in v2):
                    diff.append(mod)

        assert len(diff) <= 10


if __name__ == "__main__":
    unittest.main()
