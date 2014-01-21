.. project_name documentation documentation master file, created by
   sphinx-quickstart on Fri May 10 18:35:14 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pymyinstall documentation
====================================

.. contents::
   :depth: 3


Description
-----------

This module contains a function which installs a module from pipy, using pip or from a setup::

    from pymyinstall import complete_installation
    for _ in complete_installation() :
        _.install(temp_folder="install")
        
Or::

    from pymyinstall import ModuleInstall
    ModuleInstall("pyquickhelper", "github", "sdpython").install(temp_folder="temp")


The module is available on `pypi/pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_ and
on `GitHub/pymyinstall <https://github.com/sdpython/pymyinstall>`_.

About this documentation
------------------------

.. toctree::
    :maxdepth: 2

    generatedoc
    glossary

    
Indices and tables
==================

+------------------+---------------------+------------------+------------------+------------------------+---------------------+
| :ref:`l-modules` |  :ref:`l-functions` | :ref:`l-classes` | :ref:`l-methods` | :ref:`l-staticmethods` | :ref:`l-properties` |
+------------------+---------------------+------------------+------------------+------------------------+---------------------+
| :ref:`genindex`  |  :ref:`modindex`    | :ref:`search`    | :ref:`l-license` | :ref:`l-changes`       | :ref:`l-README`     |
+------------------+---------------------+------------------+------------------+------------------------+---------------------+
   

