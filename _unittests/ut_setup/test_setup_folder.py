# -*- coding: utf-8 -*-
"""
@brief      test log(time=25s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from pymyinstall.setuphelper import create_folder_setup


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
