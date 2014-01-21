.. _l-README:

README
======

.. contents::
   :depth: 3


Introduction
------------

This module contains a function which installs a module from pipy, using pip or from a setup::

    from pymyinstall import complete_installation
    for _ in complete_installation() :
        _.install(temp_folder="install")
        
Or::

    from pymyinstall import ModuleInstall
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")
    
    
The documentation is available at 
`pymyinstall documentation <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_.
You can download the setup  `here <http://www.xavierdupre.fr/site2013/index_code.html>`_.
The module is available on `pypi/pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_ and
on `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_.


Design
------

This project contains various helper about logging functions, unit tests and help generation.
   * a source folder: ``src``
   * a unit test folder: ``_unittests``, go to this folder and run ``run_unittests.py``
   * a _doc folder: ``_doc``, it will contains the documentation
   * a file ``setup.py`` to build and to install the module
   * a file ``make_help.py`` to build the sphinx documentation
    
    
    
Dependencies
------------

To build the documentation, you need:
   * `Sphinx <http://sphinx-doc.org/>`_ and its dependencies.

