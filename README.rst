

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
         
   
**Links:**
    * `pypi/pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_
    * `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_
    * `documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall>`_
    * `Travis <https://travis-ci.org/sdpython/pymyinstall>`_
    * `Blog <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/blog/main_0000.html#ap-main-0>`_


Description
-----------

This module contains functions which install a module from pipy, using pip or from a wheel package::

    from pymyinstall import datascientist
    datascientist("install", full = True)
        # full = False for a smaller set of modules to install
        # but needed to make IPython work.
        
Or::

    from pymyinstall import ModuleInstall
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")
    
This module also contains functions to extend distributions 
`Anaconda <http://continuum.io/downloads#py34>`_, `WinPython <https://winpython.github.io/>`_
for the notebooks proposed at `ENSAE - Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_ (French)::

    from pymyinstall import extend_anaconda, process_installation
    process_installation(extend_anaconda())
    
Or::

    from pymyinstall import extend_winpython, process_installation
    process_installation(extend_winpython())
    
If it fails for any reason - lost connexion -, run again the function with the same
parameter. If it fails again, you can skip the modules by filling the parameter ``skip``.
Some modules might fail on Windows due to Permission error, in that case, you should go to the
folder ``install`` and run the installer. Once it is done, you can run the function again 
to continue. 



Functionalities
---------------

* help installing module from GitHub, pip and setup
* install other common tools or editors
* provides a list of modules to install to use Python to manipulate data (IPython, pandas, scikit-learn...)
* function to build a setup with Python, R and useful packages like `WinPython <https://winpython.github.io/>`_,


Versions
--------

* **1.0.415 - 2015/08/15**
    * **new:** function win_python_setup
      to create a setup similar to WinPython but with InnoSetup (avoid limit size)
    * **add:** function to check for update and update an existing module, see 
      class ModuleInstall
* **0.9 - 2015/06/10**
    * **add:** install wheel packages
    * **add:** add new packages to the list of a datascientist
* **0.8 - 2014/11/09**
    * **add:** Python version is now checked, ImportError is raised if it used on Python 2
    * **add:** module `ansiconv <http://pythonhosted.org/ansiconv/>`_, `ansi2html <https://pypi.python.org/pypi/ansi2html/>`_
    * **add:** function `installation_azure <pymyinstall.packaged.packaged_config.installation_azure>`_
    * **fix:** the setup does not need the file ``README.rst`` anymore
* **0.7 - 2014/10/22**
    * **new:** list of modules to manipulate and view data cubes (not included in the main function as their design might evolve in the future)
    * **new:** a few modules such as `paramiko <http://www.paramiko.org/>`_ to open a SSH connection
    * **add:** add a new source for Windows setups: ``exe_xd``

