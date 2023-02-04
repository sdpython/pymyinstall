"""
@brief      test log(time=20s)
"""
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor
from pymyinstall.installhelper import get_installed_modules


class TestStatusHelper(unittest.TestCase):

    def test_status_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        res = get_installed_modules(
            fLOG=fLOG, stop=10, pypi=True, short_list=["autopep8"])
        for f in res:
            fLOG(f)
        if is_travis_or_appveyor():
            self.assertEqual(len(res), 1)
        else:
            warnings.warn(
                "This test does not work well on a virtual environment [TestStatusHelper].")

        res = get_installed_modules(
            fLOG=fLOG, stop=5, pypi=True, short_list=["dataspyre"])
        fLOG(res)

        res = get_installed_modules(fLOG=fLOG, stop=5, pypi=True)
        for f in res:
            fLOG(f)
        if len(res) != 5:
            raise AssertionError("\n".join(
                "\n---------\n{0}/{1} {2}".format(i + 1, len(res), _) for i, _ in enumerate(res)))


if __name__ == "__main__":
    unittest.main()
