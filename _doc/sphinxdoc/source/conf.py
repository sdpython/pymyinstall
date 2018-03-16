#-*- coding: utf-8 -*-
import sys
import os
import datetime
import re
import sphinx_readable_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables

set_sphinx_variables(__file__, "pymyinstall", "Xavier Dupré", 2018,
                     "readable", sphinx_readable_theme.get_html_theme_path(),
                     locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pymyinstall/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/"


epkg_dictionary['boost'] = "http://www.boost.org/"
epkg_dictionary['boost_python'] = "http://www.boost.org/doc/libs/release/libs/python/"
epkg_dictionary['cvxopt'] = "http://cvxopt.org/"
epkg_dictionary['cvxpy'] = "http://www.cvxpy.org/en/latest/index.html"
epkg_dictionary['dlib'] = "http://dlib.net/"
epkg_dictionary['SQLiteSpy'] = "https://www.yunqa.de/delphi/products/sqlitespy/index"
epkg_dictionary['statsmodels'] = "http://www.statsmodels.org/stable/index.html"
