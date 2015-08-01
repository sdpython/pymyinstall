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

This module contains functions which install a module from pipy, using pip or from a wheel package::

    from pymyinstall.packaged import ensae_fullset
    for mod in ensae_fullset():
        mod.install()
        
Or::

    from pymyinstall import ModuleInstall
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")
    
If it fails for any reason - lost connexion -, run again the function with the same
parameter. If it fails again, you can skip the modules by filling the parameter ``skip``.
Some modules might fail on Windows due to Permission error, in that case, you should go to the
folder ``install`` and run the installer. Once it is done, you can run the function again 
to continue. 

It is better to use it outside the interpreter::

    python -c "from pymyinstall.packaged import ensae_fullset;list(mod.install() for mod in ensae_fullset())"


Installation
------------

``pip install pymyinstall``



Functionalities
---------------

- help installing module from GitHub, pip and setup
- install other common tools or editors
- provides a list of modules to install to use Python to manipulate data (IPython, pandas, scikit-learn...)
- function to build a setup with Python, R and useful packages like `WinPython <https://winpython.github.io/>`_,
  see :func:`win_python_setup <pymyinstall.win_installer.win_setup_main.win_python_setup>`
    

Quick start
-----------

.. toctree::
    :maxdepth: 1
    
    all_example
    all_notebooks
        
    
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

