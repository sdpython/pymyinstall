"""
@brief      test log(time=10s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase


class TestCodeStyle(ExtTestCase):

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'R1703', 'C0111', 'C0201', 'R1702',
                                  'W0703', 'W0622', 'C0412', 'R0912',
                                  'W0603', 'W0212', 'W0123', 'W0201',
                                  'C0200', 'W0122', 'C0302', 'W0102',
                                  'W0621', 'R1710', 'R0401', 'R1714',
                                  'R0915', 'W0107', 'C0415',
                                  'W0707', 'R1725', 'R1732', 'C0207',
                                  'W1514', 'C0209'),
                   skip=["__init__.py:1: R0401",
                         "win_installer",
                         "Redefining built-in ",
                         "is assigned to nothing",
                         "Disallow trailing comma tuple",
                         "The if statement can be replaced with",
                         "Unable to import 'src.pymyinstall.packaged.get_pip'",
                         "Redefining name 'is_installed' from outer",
                         "module_install_version.py:17: E0401",
                         "module_install_page_wheel.py:15: E0401",
                         "module_install_page_wheel.py:14: E0401",
                         "install_custom.py:13: E0401",
                         "install_custom.py:14: E0401",
                         "install_custom.py:15: E0401",
                         "install_custom_python.py:220",
                         "module_install_version.py:16: E0401",
                         "module_install_page_wheel.py:13: E0401",
                         "module_install_page_wheel.py:13: E0401",
                         "module_install.py:29: E0401",
                         "module_install.py:28: E0401",
                         "module_install.py:27: E0401",
                         "get_pip.py",
                         "pymy_status.py:53: W0612",
                         "module_install.py:26: E0401",
                         "ipython_helper.py:24: E1101",
                         "Unable to import 'selenium.webdriver'",
                         "Unable to import 'Queue'",
                         "Unable to import 'src.pymyinstall.installhelper.status_helper'",
                         "[W503] line break before binary operator",
                         "install_custom_python.py:164",
                         "ipython_helper.py:21: E1101",
                         ])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0703', 'W0622', 'W0621', 'C0412', 'C0411',
                                  'R0915', 'W0107', 'C0415', 'W0707', 'R1725',
                                  'R1732', 'C0207', 'W1514', 'C0209'),
                   skip=["test_is_installed.py:41: E1101",
                         "Unable to import 'selenium.webdriver'",
                         "Unable to import 'Queue'",
                         ])


if __name__ == "__main__":
    unittest.main()
