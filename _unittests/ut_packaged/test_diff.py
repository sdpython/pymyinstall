"""
@brief      test log(time=200s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.packaged import small_set


class TestDifference(unittest.TestCase):

    def test_diff(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        name = set(_.name for _ in small_set())
        keep = []
        for mod in small_set():
            if mod.name not in name:
                keep.append(mod)
        assert len(keep) > 0

        for mod in keep:
            if mod.mname is None:
                fLOG(
                    "ModuleInstall('{0}', '{1}'),".format(mod.name, mod.kind))
            else:
                fLOG("ModuleInstall('{0}', '{1}', mname='{2}'),".format(
                    mod.name, mod.kind, mod.mname))

    def test_diff2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        res = small_set()
        count = {}
        for mod in res:
            count[mod.name] = 1

        assert "pyquickhelper" in count
        assert "code_beatrix" in count


if __name__ == "__main__":
    unittest.main()
