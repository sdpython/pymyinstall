.. project_name documentation documentation master file, created by
   sphinx-quickstart on Fri May 10 18:35:14 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pymyinstall documentation
=========================

.. image:: https://travis-ci.org/sdpython/pymyinstall.svg?branch=master
    :target: https://travis-ci.org/sdpython/pymyinstall
    :alt: Build status

.. image:: https://badge.fury.io/py/pymyinstall.svg
    :target: http://badge.fury.io/py/pymyinstall    
   
.. image:: http://img.shields.io/pypi/dm/pymyinstall.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/pymyinstall

.. image:: http://img.shields.io/github/issues/sdpython/pymyinstall.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pymyinstall/issues
    
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT                   
   
**Links:** `pypi <https://pypi.python.org/pypi/pymyinstall/>`_,
`github <https://github.com/sdpython/pymyinstall/>`_,
`documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall>`_,
`travis <https://travis-ci.org/sdpython/pymyinstalls>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`



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


Setup
-----

The module also includes a function 
:func:`win_python_setup <pymyinstall.win_installer.win_setup_main.win_python_setup>`
which creates a setup with Python and R which modules and packages for a datascientist.
This function gives extra informations about module difficult to install
such as `theano <http://deeplearning.net/software/theano/>`_.

Source of the packages
----------------------

* `PyPI <https://pypi.python.org/pypi>`_: pure python packages
* `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_: packages with C++
* `xavierdupre.fr <http://www.xavierdupre.fr/>`_: custom build (xgboost, ...)


Installation
------------

``pip install pymyinstall``




Quick start
-----------

.. toctree::
    :maxdepth: 1
    
    all_example
    all_notebooks
    name_set_table
    ensae_full_set_table    
    
Indices and tables
------------------

+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-example`   | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQ`       | :ref:`l-notebooks`  |                    | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+


Navigation
----------

.. toctree::
    :maxdepth: 1
    
    indexmenu

