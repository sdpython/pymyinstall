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

To use modules related to the manipulation of big datasets::

    from pymyinstall import ds_complete, ds_huge
    ds_complete()
    ds_huge()
    
It is better to use it outside the interpreter::

    python -c "from pymyinstall import complete_installation, process_installation;process_installation(complete_installation())"
    
Installation
------------

``pip install pymyinstall``


Functionalities
---------------

    - help installing module from GitHub, pip and setup
    - install other common tools or editors
    - provides a list of modules to install to use Python to manipulate data (IPython, pandas, scikit-learn...)
    


    
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

