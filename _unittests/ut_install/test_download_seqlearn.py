"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, get_temp_folder
from pymyinstall.installhelper import compare_version
from pymyinstall.packaged import find_module_install


class TestDownloadSeqlearn(unittest.TestCase):

    def test_install_seqlearn(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if sys.platform.startswith("win") and sys.version_info[0] >= 3:
            temp = get_temp_folder(__file__, "temp_download_seqlearn")
            source = "2" if is_travis_or_appveyor() else None
            m = find_module_install("seqlearn")
            m.source = source
            name = m.get_exewheel_url_link2(wheel=True, source=source)
            fLOG(m.existing_version)
            r = compare_version(m.existing_version, "0.2")
            self.assertTrue(r >= 0)
            self.assertTrue("unoptimized" not in name[0])
            whl = m.download(temp_folder=temp, source="2")
            fLOG(m.version)
            self.assertTrue(os.path.exists(whl))
            self.assertTrue("unoptimized" not in whl)


if __name__ == "__main__":
    unittest.main()
