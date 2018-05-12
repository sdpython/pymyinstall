"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG

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
        for _, k in sorted(couples):
            fLOG("'{0}',".format(k))


if __name__ == "__main__":
    unittest.main()
