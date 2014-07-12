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
    datascientist ("install")
        
Or::

    from pymyinstall import ModuleInstall
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")


Functionalities
---------------

    - help installing module from GitHub


Design
------

This project contains various helper about logging functions, unit tests and help generation.
   * a source folder: ``src``
   * a unit test folder: ``_unittests``, go to this folder and run ``run_unittests.py``
   * a _doc folder: ``_doc``, it will contains the documentation
   * a file ``setup.py`` to build and to install the module
   * a file ``make_help.py`` to build the sphinx documentation

Versions
--------

* **v0.4 - 2014/??/??**
    * **new:** add a function to install SciTE, see :func:`install_scite <installhelper.install_custom.install_scite>`
    * **new:** add a function to setup ipython, see :func:`setup_ipython <setuphelper.setup_ipython>`
    * **new:** add a function to setup an environment for a `Data Scientist <http://en.wikipedia.org/wiki/Data_science>`_
    * **new:** add shortcuts on Windows desktop
    * **new:** class ``ModuleInstall`` can now install an application such as ``Spyder`` (not an extension which can be imported)
    * **new:** add a function to add a shortcut on the desktop for Spyder
* **v0.3 - 2014/06/03**
    * **changes:** add a version parameter
    * **fix:** fix the method install when platform is ``amd64``
    * **add:** list of website for popular tools

