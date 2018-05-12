"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor

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

from src.pymyinstall.installhelper import get_installed_modules


class TestStatusHelper(unittest.TestCase):

    def test_status_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = get_installed_modules(
            fLOG=fLOG, stop=10, pypi=True, short_list=["autopep8"])
        for f in res:
            fLOG(f)
        if sys.version_info[0] > 2:
            if is_travis_or_appveyor():
                self.assertEqual(len(res), 1)
            else:
                warnings.warn(
                    "This test does not work well on a virtual environment [TestStatusHelper].")

        res = get_installed_modules(
            fLOG=fLOG, stop=5, pypi=True, short_list=["dataspyre"])
        fLOG(res)

        res = get_installed_modules(fLOG=fLOG, stop=5, pypi=True)
        for f in res:
            fLOG(f)
        if sys.version_info[0] == 2:
            # we disable the test for Python 2.7
            warnings.warn(
                "TestStatusHelper.test_status_helper disabled on Python 2.7")
            return
        if len(res) != 5:
            raise Exception("\n".join(
                "\n---------\n{0}/{1} {2}".format(i + 1, len(res), _) for i, _ in enumerate(res)))


if __name__ == "__main__":
    unittest.main()
