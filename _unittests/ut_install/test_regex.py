"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper


from src.pymyinstall.installhelper.module_install import ModuleInstall
from pyquickhelper import fLOG


class TestRegex (unittest.TestCase):

    def test_1(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = 'onclick=.javascript:dl[(]([,\[\]0-9]+) *, *.([0-9&;@?=:A-Zgtl]+).[)].' + \
                  ' title(.+)?.>(.+?-((cp34)|(py3)|(py2[.]py3)|(py33[.]py34))-none-((win_amd64)|(any)).whl)</a>'
        raw = """<li><a id='networkx'></a><strong><a href='http://networkx.lanl.gov/'>NetworkX</a></strong>, a package for complex networks.
                <ul>
                <li><a href='javascript:;' onclick='javascript:dl([97,46,45,116,111,57,50,114,101,112,120,49,53,104,51,107,121,106,119,110,55,108,47], "7D34&lt;?&gt;AFC83B47?:2;151;29@619@&gt;2C4C820C@1B=E")' title='[1.2&#160;MB] [Dec 24, 2014]'>networkx&#8209;1.9.1&#8209;py2.py3&#8209;none&#8209;any.whl</a></li>
                </ul>""".replace("&#8209;", "-")
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False

    def test_2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = '''onclick=.javascript:dl[(]([,\[\]0-9]+) *, *.([0-9&;@?=:A-Zgtl#]+).[)]. title(.+)?.>''' + \
                  '''(.+?-((cp34)|(py3)|(py2[.]py3)|(py34))-none-((win_amd64)|(any)).whl)</a>'''
        raw = """<li><a href='javascript:;' onclick='javascript:dl([45,111,46,119,109,108,112,104,105,50,51,120,110,118,48,47,52,99,53,102,121,101],""" + \
              """ "A7CD=&lt;@&lt;?5;450:2B2&#62;0A6:@0&lt;1&lt;E038&lt;:92375")' """ + \
              """title='[1.4&#160;MB] [Nov 30, 2015]'>lxml-3.5.0-cp34-none-win_amd64.whl</a></li>"""
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False

    def test_3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        pattern = '''onclick=.javascript:dl[(]([,\[\]0-9]+) *, *.([0-9&;@?=:A-Zgtl#]+).[)]. title(.+)?.>''' + \
                  '''(.+?-((cp34)|(py3)|(py2[.]py3)|(py34))(-none)?-((win_amd64)|(any))(.whl)?)</a>'''
        raw = """<li><a href='javascript:;' onclick='javascript:dl([120,53,99,109,95,100,122,51,46,97,119,117,110,57,54,104,47,106,52,48,105,101,108,111,116,45,112], "6;H;BA1=@F03FI7818CI2J7BI&lt;G&lt;EI:D&lt;4935&#62;B8:?F")' """ + \
              """title='[1.6&#160;MB] [Nov 30, 2015]'>lxml-3.5.0-cp34-win_amd64</a></li>"""
        reg = re.compile(pattern)
        r = reg.search(raw)
        if r:
            fLOG(r.groups())
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
