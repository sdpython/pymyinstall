# -*- coding: utf-8 -*-
"""
@brief      test log(time=25s)
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


from src.pymyinstall.setuphelper import create_folder_setup
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase


class TestSetupFolder(ExtTestCase):

    def test_setup_folder(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_setup_folder", clean=False)

        import cairocffi
        self.assertTrue(cairocffi is not None)
        st = create_folder_setup('cairocffi', fLOG=fLOG, output_path=temp)
        self.assertEqual(len(st), 1)
        self.assertExists(st[0])
        exp = os.path.join(temp, 'dist')
        found = os.listdir(exp)
        self.assertEqual(len(found), 1)
        self.assertIn(".whl", found[0])


if __name__ == "__main__":
    unittest.main()
