

.. _l-README:

README / Changes
================

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
         
.. image:: https://landscape.io/github/sdpython/pymyinstall/master/landscape.svg?style=flat
   :target: https://landscape.io/github/sdpython/pymyinstall/master
   :alt: Code Health  

.. image:: https://requires.io/github/sdpython/pymyinstall/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/pymyinstall/requirements/?branch=master
     :alt: Requirements Status   
    
.. image:: https://codecov.io/github/sdpython/pymyinstall/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pymyinstall?branch=master
    
   
**Links:**
    * `pypi/pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_
    * `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_
    * `documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall>`_
    * `Travis <https://travis-ci.org/sdpython/pymyinstall>`_
    * `Blog <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/main_0000.html#ap-main-0>`_


Description
-----------

The module helps installing modules in Windows and Linux.
It installs two scripts. The first one installs modules:

    pymy_install3
    
The second one updates installed modules::

    pymy_update3
    
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


Versions
--------

* **1.1 - 2016/??/??**
    * **fix:** module dynd is only available on Python 3, remove it for Python 2.7
    * **fix:** fix function *create_win_batches* (batch script ipython were missing, batch to update all installed packages)
    * **change:** the function *update_all* continues if an update fails (catches excptions)
    * **add:** add scripts *pymy_install* and *pymy_update* to folder *<python>/Scripts*
    * **change:** on Anaconda, the module tries to use *conda* first before trying another way (*pip*, *wheel*)
    * **fix:** fix function *update_all* when cannot check if there is a new version
    * **add:** retrieve license and classifier of installed modules
    * **add:** putty was added to the setup
    * **add:** TDM-GCC was added to the setup (for theano)
    * **add:** function *install_module_deps* installs a module with its dependencies
    * **add:** the setup works with Python 3.5
    * **change:** improve modules set definition ``pymy_install3 --set=<module_set>``
    * **fix:** fix issues while update numpy and networkx, add module *qgrid*
    * **add:** function *download_module*
    * **add:** another source for the wheels can be specified

* **1.0.418 - 2015/08/15**
    * **new:** function win_python_setup
      to create a setup similar to WinPython but with InnoSetup (avoid limit size)
    * **add:** function to check for update and update an existing module, see 
      class ModuleInstall


