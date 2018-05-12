"""
@brief      test log(time=1s)
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

from src.pymyinstall.installhelper import missing_dependencies


class TestMissingModules (unittest.TestCase):

    def test_missing_module(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        deps = missing_dependencies()
        self.assertTrue(isinstance(deps, dict))
        for k, v in sorted(deps.items()):
            fLOG(k, "--->", ", ".join(v))


if __name__ == "__main__":
    unittest.main()
