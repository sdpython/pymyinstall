.. _l-README:

README
======

   
   
**Links:**
    * `pypi/pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_
    * `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_
    * `documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall>`_


Description
-----------

This module contains functions which install a module from pipy, using pip or from a setup::

    from pymyinstall import datascientist
    datascientist("install", full = True)
        # full = False for a smaller set of modules to install
        # but needed to make IPython work.
        
Or::

    from pymyinstall import ModuleInstall
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")

Some modules fail on Windows due to Permission error, in that case, you should go to the
folder ``install`` and run the installer. Once it is done, you can run the function again 
to continue. It will skip the modules already installed.


Functionalities
---------------

    - help installing module from GitHub, pip and setup
    - install other common tools or editors
    - provides a list of modules to install to use Python to manipulate data (IPython, pandas, scikit-learn...)


Versions
--------

* **0.7 - 2014/10/22**
    * **new:** list of modules to manipulate and view data cubes (not included in the main function as their design might evolve in the future)
    * **new:** a few modules such as `paramiko <http://www.paramiko.org/>`_ to open a SSH connection
    * **add:** add a new source for Windows setups: ``exe_xd``
* **0.6 - 2014/08/26**
    * **fix:** fix an import issue
* **0.5 - 2014/08/24**
    * **new:** a couple of new modules in the full set of modules
    * **new:** a subset of modules to work with ipython
    * **add:** add parameter ``skip`` to function :func:`datascientist <pymyinstall.packaged.packaged_functions.datascientist>`


