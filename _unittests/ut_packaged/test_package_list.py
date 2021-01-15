"""
@brief      test log(time=2s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pymyinstall.packaged import small_set


class TestPackageList(unittest.TestCase):

    def test_package_list(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        filename = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "data", "status_installation_2016-05.txt")

        def clean(s):
            if "\\" in s or "/" in s:
                s = s.replace("\\", "/")[-1]
            return s.strip().lower().replace("_", "-")

        every = set(clean(_.name) for _ in small_set())

        collected = set()
        success = set()
        with open(filename, "r") as f:
            for line in f:
                line = line.strip("\n\r ")
                if "collected" in line:
                    pack = line.split(":")[-1].split(",")
                    for p in pack:
                        collected.add(clean(p))
                else:
                    end = line.split("installed")[-1]
                    spl = end.split()
                    for p in spl:
                        v = p.split('-')[0].strip()
                        if v:
                            success.add(clean(v))

        fLOG(len(collected), list(sorted(collected))[:4])
        fLOG(len(success), list(sorted(success))[:4])
        concat = collected.union(success)

        # not in the list
        fLOG('---------')
        not_list = concat - every
        for p in sorted(not_list):
            fLOG("not in", p)

        # not installed
        fLOG('---------')
        not_installed = every - concat
        for p in sorted(not_installed):
            fLOG("not installed", p)


if __name__ == "__main__":
    unittest.main()
