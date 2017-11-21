
pymyinstall documentation
=========================

.. image:: https://travis-ci.org/sdpython/pymyinstall.svg?branch=master
    :target: https://travis-ci.org/sdpython/pymyinstall
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

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

**Links:** `pypi <https://pypi.python.org/pypi/pymyinstall/>`_,
`github <https://github.com/sdpython/pymyinstall/>`_,
`documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall>`_,
`travis <https://travis-ci.org/sdpython/pymyinstalls>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`,
:ref:`l-issues-todolist`

What is it?
-----------

The module helps installing packages on Windows and Linux.
The module installs two batch files. The first one
``pymy_update`` updates existing modules. The second one
``pymy_install`` installes necessary modules to do machine learning.
To get help on both::

    pymy_update3 --help
    pymy_install3 --help

For example, to install packages for a datascientist::

    pip install pymyinstall
    pymy_install3

The module will download and install many modules (see :ref:`l-ensae_fullset-table`).
It includes *numpy*, *scikit-learn*, *jupyter*, *pandas* and many others.
If it fails for any reason - lost connexion -, run again the function with the same
parameter. If it fails again, you can skip the modules by filling the parameter ``skip``.
To update modules::

    pymy_update3

If some modules fail, they can be skipped by using option ``--skip=<modules comma separated>``.
Both scripts can be used to install a subset of modules::

    pymy_install3 --set=minimum

Modules sets are described at :ref:`l-name-set-table`. Corresponding
functions exist:

::

    from pymyinstall import download_module, install_module, update_module
    download_module("numpy")
    install_module("numpy")
    update_module("numpy")

Setup
-----

The module also includes a function
:func:`win_python_setup <pymyinstall.win_installer.win_setup_main.win_python_setup>`
which creates a setup with Python and R which modules and packages for a datascientist.
This function gives extra informations about module difficult to install
such as `theano <http://deeplearning.net/software/theano/>`_ which
will disappear in 2018.

Source of the packages
----------------------

* `PyPI <https://pypi.python.org/pypi>`_: pure python packages
* `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_: packages with C++
* `xavierdupre.fr <http://www.xavierdupre.fr/>`_: custom build (dlib, ...)

Installation
------------

``pip install pymyinstall``

Quick start
-----------

.. toctree::
    :maxdepth: 1

    i_ex
    all_notebooks
    i_faq
    name_set_table
    ensae_full_set_table
    completed_todoextlist
    issues_todoextlist

Galleries
---------

.. toctree::
    :maxdepth: 1

    gyexamples/index
    gynotebooks/index
    blog/blogindex

Indices and tables
------------------

+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-example2`  | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQ2`      | :ref:`l-notebooks`  |                    | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+

Navigation
----------

.. toctree::
    :maxdepth: 1

    indexmenu
