

.. blogpost::
    :title: Build xgboost 0.4a30 for Python 3.4 and 3.5
    :keywords: install, xgboost, vcomp110.dll, OpenMP
    :date: 2016-04-04
    :categories: install, modules, windows
    :lid: blog_xgboost_install3504a30
    
    `xgboost <https://github.com/dmlc/xgboost>`_ does not support the Windows
    compilation anymore so I had to look for a way to compile *xgboost* for Windows.
    I tried to start from the source but it seemed quite complex plus the owners
    mention they don't support it anymore. Instead, I chose to use
    the source included the release package on 
    `PyPi <https://pypi.python.org/pypi/xgboost>`_.
    I copy paste some of the instructions I used from the previous 
    blog post I wrote on that topic since I did not start from a fresh and empty
    environment. The steps I did not do again are marked with a ``*``.
    This is the process I followed:
    
    * Install `Visual Studio Community Edition (C++) <https://www.microsoft.com/france/visual-studio/>`_.
      The link points to an image *.iso*. ``*``
    * Install the `Java JDK <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_.
      Select the newest version. ``*``
    * Download the modified version of `xgboost <https://pypi.python.org/pypi/xgboost>`_ from PyPI.
    * Check `OpenMD <https://msdn.microsoft.com/fr-fr/library/tt15eb9t.aspx>`_ files are present in 
      ``C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC`` with files ``vcomp.lib``, ``vcombd.lib``, ``omp.h``.
      This is also what you should follow to get missing dependency such as 
      ``vcomp110.dll`` (which comes from `OpenMP in Visual C++ <https://msdn.microsoft.com/library/tt15eb9t.aspx>`_). 
      ``*``
    * Open the solution in Windows directory (in xgboost) and update the path to 
      point to Java JDK and OpenMP, build the version release/x64,
      update paths to point to your version of Java SDK ``*``
    * Copy/Paste the built assemblies ``xgboost_wrapper.dll`` into the python folder
    * Go to the python folder and type ``python setup.py bdist_wheel`` to build the file *.whl*.
    
    This wheel can be installed on any Python 3.4 and 3.5 64 bits installation.
    It is available at `xgboost-0.4a30-py3-none-any.whl <https://github.com/sdpython/xgboost/releases/tag/0.4a30>`_.
    The source I used to compile are located on 
    `github <https://github.com/sdpython/xgboost/tree/master/xgboost-0.4a30>`_

    *About* 
    
    * `OpenMP <https://en.wikipedia.org/wiki/OpenMP>`_
      is an API that supports multi-platform shared 
      memory multiprocessing programming in C, C++, and Fortran (Wikipedia).
    * `XGBoost: A Scalable Tree Boosting System <http://arxiv.org/pdf/1603.02754v1.pdf>`_, paper by
      Tianqi Chen, Carlos Guestrin
