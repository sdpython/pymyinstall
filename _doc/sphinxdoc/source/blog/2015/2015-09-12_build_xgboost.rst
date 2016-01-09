
.. _blog_xgboost_install:

.. blogpost::
    :title: Build xgboost for Python 3.4
    :keywords: install, xgboost, vcomp110.dll, OpenMP
    :date: 2015-09-12
    :categories: install, modules, windows

    This is a process I followed to build `xgboost <https://github.com/dmlc/xgboost>`_ 0.4 (which I also described
    at `Building xgboost on Windows for Python <http://www.xavierdupre.fr/blog/2015-08-23_nojs.html>`_).
    This is also what you should follow to get missing dependency such as 
    ``vcomp110.dll`` (which comes from `OpenMP in Visual C++ <https://msdn.microsoft.com/library/tt15eb9t.aspx>`_). 
    The following process is only available for Python 3.4 64 bit:

    * Install `Microsoft Windows SDK for Windows 7 and .NET Framework 4 <http://www.microsoft.com/en-us/download/details.aspx?id=8279>`_.
      It has to be done to make Visual Studio Express 2010 build for x64. It must be done first if you have
      a more recent version of Visual Studio installed on the same machine.
    * Install `Visual Studio Express (C++) <http://download.microsoft.com/download/1/E/5/1E5F1C0A-0D5B-426A-A603-1798B951DDAE/VS2010Express1.iso>`_.
      The link points to an image *.iso*.
    * Install the `Java JDK <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_.
      Select the newest version.
    * Download `xgboost <https://github.com/dmlc/xgboost>`_.
    * Check `OpenMD <https://msdn.microsoft.com/fr-fr/library/tt15eb9t.aspx>`_ files are present in 
      ``C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC`` with files ``vcomp.lib``, ``vcombd.lib``, ``omp.h``.
    * Open the solution in Windows directory (in xgboost) and update the path to 
      point to Java JDK and OpenMP, build the version release/x64
      (see this `comment <https://github.com/sdpython/xgboost/commit/91cc9b2fadeb87560c24006b49a36fccc8bf3270>`_.
    * Go to the python folder and type ``python setup.py bdist_wheel`` to build the file *.whl*.
    
    This wheel can be installed on any Python 3.4 64 bits installation.
    The first two steps might have to be done a second time to get ``vcomp110.dll``.
    This library must be available in one the path in environment variable ``PATH``
    or be in the same folder as ``python.exe``.
    
    *About* 
    
    `OpenMP <https://en.wikipedia.org/wiki/OpenMP>`_
    is an API that supports multi-platform shared 
    memory multiprocessing programming in C, C++, and Fortran (Wikipedia).