"""
@brief      test log(time=2s)

skip this test for regular run
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


from pyquickhelper.loghelper import fLOG
from src.pymyinstall.packaged import all_set


class TestPackageListPrint(unittest.TestCase):

    def test_package_list_print(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        every = {}
        duplicated = []
        for _ in all_set():
            name = _.name
            if name in every:
                duplicated.append(name)
            every[name] = 1

        if len(duplicated) > 0:
            raise Exception("Duplicated modules\n{0}".format(
                "\n".join(duplicated)))

        fLOG(len(every))
        couples = [(k.lower(), k) for k in every]
        for kn, k in sorted(couples):
            fLOG("'{0}',".format(k))


if __name__ == "__main__":
    unittest.main()
