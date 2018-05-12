"""
@brief      test log(time=3s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder

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


from src.pymyinstall.setuphelper import create_empty_folder_setup


class TestOnlyMain (unittest.TestCase):

    def test_empty_setup(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_empty_setup")

        cr = create_empty_folder_setup(temp, "CVXcanon",
                                       description="module created with compiled files issues from the installation of CVXcanon")
        assert len(cr) >= 2
        for o in cr:
            if not os.path.exists(o):
                raise FileNotFoundError(o)


if __name__ == "__main__":
    unittest.main()
