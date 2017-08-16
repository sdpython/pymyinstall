
.. _l-README:

README
======

.. image:: https://travis-ci.org/sdpython/pymyinstall.svg?branch=master
    :target: https://travis-ci.org/sdpython/pymyinstall
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/ccsvoi29n3a71i6j?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pymyinstall
    :alt: Build Status Windows

.. image:: https://badge.fury.io/py/pymyinstall.svg
    :target: http://badge.fury.io/py/pymyinstall

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://landscape.io/github/sdpython/pymyinstall/master/landscape.svg?style=flat
   :target: https://landscape.io/github/sdpython/pymyinstall/master
   :alt: Code Health

.. image:: https://requires.io/github/sdpython/pymyinstall/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/pymyinstall/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/pymyinstall/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pymyinstall?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/pymyinstall.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pymyinstall/issues

.. image:: https://badge.waffle.io/sdpython/pymyinstall.png?label=ready&title=Ready
    :alt: Waffle
    :target: https://waffle.io/sdpython/pymyinstall

.. image:: https://www.codacy.com/app/sdpython/pymyinstall?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sdpython/pymyinstall&amp;utm_campaign=Badge_Grade
    :alt: Codacy Badge
    :target: https://www.codacy.com/app/sdpython/pymyinstall?

.. image:: http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage    


**Links:**

* `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_
* `documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/main_0000.html#ap-main-0>`_

Description
-----------

The module helps installing modules in Windows and Linux.
It installs two scripts. The first one installs modules:

    pymy_install3

The second one updates installed modules::

    pymy_update3

For a specific module::

    pymy_update3 <module_name>

To install a preconfigured set of modules::

    pymy_install3 --set=pyquickhelper

``--help`` gives the usage.

Functionalities
---------------

* help installing module from GitHub, pip and setup
* install other common tools or editors
* provides a list of modules to install to use Python to manipulate data (IPython, pandas, scikit-learn...)
* function to build a setup with Python, R and useful packages like `WinPython <https://winpython.github.io/>`_

Source of the packages:

* `PyPI <https://pypi.python.org/pypi>`_: pure python packages
* `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_: packages with C++
* `xavierdupre.fr <http://www.xavierdupre.fr/>`_: custom build (xgboost, ...)
