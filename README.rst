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

This module contains a function which installs a module from pipy, using pip or from a setup::

    from pymyinstall import complete_installation
    for _ in complete_installation() :
        _.install(temp_folder="install")
        
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

* **v0.3 - 2014/06/03**
    * **changes:** add a version parameter
    * **fix:** fix the method install when platform is ``amd64``
    * **add:** list of website for popular tools

