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


from src.pymyinstall.packaged import ensae_fullset
from src.pymyinstall.win_installer.win_batch import create_win_batches


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
