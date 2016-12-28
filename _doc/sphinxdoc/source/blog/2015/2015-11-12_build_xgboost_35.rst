
.. blogpost::
    :title: Build xgboost for Python 3.5
    :keywords: install, xgboost, vcomp110.dll, OpenMP
    :date: 2015-11-12
    :categories: build, module, windows
    :lid: blog_xgboost_install35

    This is a process I followed to build `xgboost <https://github.com/dmlc/xgboost>`_ 0.4
    on Python 3.5
    This is also what you should follow to get missing dependency such as
    ``vcomp110.dll`` (which comes from `OpenMP in Visual C++ <https://msdn.microsoft.com/library/tt15eb9t.aspx>`_).
    The following process is only available for Python 3.4 64 bit:

    * Install `Visual Studio Community Edition (C++) <https://www.microsoft.com/france/visual-studio/>`_.
      The link points to an image *.iso*.
    * Install the `Java JDK <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>`_.
      Select the newest version.
    * Download the modified version of `xgboost <https://github.com/sdpython/xgboost>`_.
    * Check `OpenMD <https://msdn.microsoft.com/fr-fr/library/tt15eb9t.aspx>`_ files are present in
      ``C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC`` with files ``vcomp.lib``, ``vcombd.lib``, ``omp.h``.
    * Open the solution in Windows directory (in xgboost) and update the path to
      point to Java JDK and OpenMP, build the version release/x64,
      update paths to point to your version of Java SDK
    * Copy/Paste the built assemblies into the python folder
    * Go to the python folder and type ``python setup.py bdist_wheel`` to build the file *.whl*.

    This wheel can be installed on any Python 3.5 64 bits installation.
    You can compare with :ref:`instructions for Python 3.4 <blog_xgboost_install>`.

    *About*

    * `OpenMP <https://en.wikipedia.org/wiki/OpenMP>`_
      is an API that supports multi-platform shared
      memory multiprocessing programming in C, C++, and Fortran (Wikipedia).
    * `XGBoost: A Scalable Tree Boosting System <http://arxiv.org/pdf/1603.02754v1.pdf>`_, paper by
      Tianqi Chen, Carlos Guestrin
