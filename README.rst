
.. image:: https://github.com/sdpython/pymyinstall/blob/master/_doc/sphinxdoc/source/phdoc_static/project_ico.png?raw=true
    :target: https://github.com/sdpython/pymyinstall/

.. _l-README:

pymyinstall: easier installation of packages
============================================

.. image:: https://travis-ci.com/sdpython/pymyinstall.svg?branch=master
    :target: https://app.travis-ci.com/github/sdpython/pymyinstall
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/ccsvoi29n3a71i6j?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pymyinstall
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/pymyinstall/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/pymyinstall/tree/master

.. image:: https://badge.fury.io/py/pymyinstall.svg
    :target: http://badge.fury.io/py/pymyinstall

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/pymyinstall/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pymyinstall?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/pymyinstall.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pymyinstall/issues

.. image:: http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://pepy.tech/badge/pymyinstall/month
    :target: https://pepy.tech/project/pymyinstall/month
    :alt: Downloads

.. image:: https://img.shields.io/github/forks/sdpython/pymyinstall.svg
    :target: https://github.com/sdpython/pymyinstall/
    :alt: Forks

.. image:: https://img.shields.io/github/stars/sdpython/pymyinstall.svg
    :target: https://github.com/sdpython/pymyinstall/
    :alt: Stars

Installing packages on Windows is not necessarily easy when
they contain C++ code. I usually use
`Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
for one package but it requires some tricks to start from
scratch and install all the needed packages.
That's what this package is doing.
The module helps installing modules in *Windows* and *Linux*.
It installs two scripts. The first one installs modules:

    pymy_install3

The second one updates installed modules::

    pymy_update3

For a specific module::

    pymy_update3 <module_name>

To install a preconfigured set of modules::

    pymy_install3 --set=pyquickhelper

``--help`` gives the usage.

It provides the following functionalities:

* help installing module from GitHub, pip and setup
* install other common tools or editors
* provides a list of modules to install to use Python to manipulate data (IPython, pandas, scikit-learn...)
* function to build a setup with Python, R and useful packages like `WinPython <https://winpython.github.io/>`_

Source of the packages:

* `PyPI <https://pypi.python.org/pypi>`_: pure python packages
* `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_: packages with C++
* `xavierdupre.fr <http://www.xavierdupre.fr/>`_: custom build (xgboost, ...)

**Links:**

* `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_
* `documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/main_0000.html#ap-main-0>`_
