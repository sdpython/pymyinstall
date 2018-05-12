"""
@brief      test log(time=2s)
"""
import sys
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pandashelper import df2rst

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


from src.pymyinstall.packaged import all_set, classifiers2string


class TestDocumentation(unittest.TestCase):

    def test_documentation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mod = all_set()
        mod.sort()
        df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
        df = df[["usage", "rst_link", "kind", "version",
                 "license", "purpose", "classifier"]]
        df["classifier"] = df.apply(
            lambda row: classifiers2string(row["classifier"]), axis=1)
        df.columns = ["usage", "name", "kind", "version",
                      "license", "purpose", "classifier"]
        fLOG(df2rst(df))


if __name__ == "__main__":
    unittest.main()
