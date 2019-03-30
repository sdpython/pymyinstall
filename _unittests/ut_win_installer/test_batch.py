"""
@brief      test log(time=3s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pymyinstall.packaged import ensae_fullset
from pymyinstall.win_installer.win_batch import create_win_batches


class TestBatch(unittest.TestCase):

    def test_batch(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_batch")
        list_modules = ensae_fullset()
        folders = dict(tools=temp, config=temp)
        op = create_win_batches(
            folders, selection={"r", "julia"}, fLOG=fLOG, module_list=list_modules)
        for _ in op:
            fLOG(_)
        assert len(op) > 0
        for _, b in op:
            assert os.path.exists(b)


if __name__ == "__main__":
    unittest.main()
