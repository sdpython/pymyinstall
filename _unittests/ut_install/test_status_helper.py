"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import warnings

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


from src.pymyinstall.installhelper import get_installed_modules
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor


class TestStatusHelper(unittest.TestCase):

    def test_status_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = get_installed_modules(
            fLOG=fLOG, stop=10, pypi=True, short_list=["pep8"])
        for f in res:
            fLOG(f)
        if sys.version_info[0] > 2:
            if is_travis_or_appveyor():
                self.assertEqual(len(res), 1)
            else:
                warnings.warn(
                    "This test does not work well on a virtual environment [TestStatusHelper].")

        res = get_installed_modules(
            fLOG=fLOG, stop=10, pypi=True, short_list=["dataspyre"])
        fLOG(res)

        res = get_installed_modules(fLOG=fLOG, stop=10, pypi=True)
        for f in res:
            fLOG(f)
        if sys.version_info[0] == 2:
            # we disable the test for Python 2.7
            warnings.warn(
                "TestStatusHelper.test_status_helper disabled on Python 2.7")
            return
        if len(res) != 10:
            raise Exception("\n".join(str(_) for _ in res))


if __name__ == "__main__":
    unittest.main()
