"""
@brief      test log(time=3s)
"""
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall import is_travis_or_appveyor
from pymyinstall.win_installer.win_setup_main_checkings import distribution_checkings


class TestCheckings(unittest.TestCase):

    def test_checkings(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "Anaconda custom" in sys.version:
            try:
                distribution_checkings(None, None, fLOG=fLOG, skip_import=True)
            except Exception as e:
                # We skip errors involving spyder and rodeo as unit test are run from a virtual
                # environment and they might be present.
                lines = str(e).split()
                for line in lines:
                    if "pymyinstall" in line:
                        # if "rodeo" not in line and "spyder" not in line:
                        # rodeo is not checked anymore, the installation
                        # changed
                        if "spyder" not in line:
                            raise AssertionError(
                                "spyder not found in line\n{0}".format(line)) from e
        elif not is_travis_or_appveyor():
            try:
                distribution_checkings(None, None, fLOG=fLOG, skip_import=True)
            except Exception as e:
                if '_venv' not in str(e) or ('Scripts' not in str(e) and '.exe' not in str(e)):
                    raise AssertionError("version: " + sys.version) from e


if __name__ == "__main__":
    unittest.main()
