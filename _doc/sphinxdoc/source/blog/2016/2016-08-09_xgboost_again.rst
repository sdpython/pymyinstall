
.. blogpost::
    :title: Build xgboost on Windows (again)
    :keywords: xgboost
    :date: 2016-08-09
    :categories: module, build

    Hopefully `xgboost <https://github.com/dmlc/xgboost>`_ won't change
    their building process any more. Here are the steps I followed
    to build *xgboost 0.6* on Windows for Python 3.5.
    (from `Building on Windows <http://xgboost.readthedocs.io/en/latest/build.html#building-on-windows>`_).
    Prerequisites:

    * Install `Visual Studio 2015 Comunity Edition <https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx>`_
      with C++ 11 enabled (updates >= 2)
    * Install `CMake <https://cmake.org/>`_
    * Get the sources from `xgboost <https://github.com/dmlc/xgboost>`_

    From the command line::

        mkdir build
        cd build
        "c:\Program Files\CMake\bin\cmake.exe" .. -G"Visual Studio 14 2015 Win64"

    Expected output::

        -- The C compiler identification is MSVC 19.0.23506.0
        -- The CXX compiler identification is MSVC 19.0.23506.0
        -- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe
        -- Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe -- works
        -- Detecting C compiler ABI info
        -- Detecting C compiler ABI info - done
        -- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe
        -- Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe -- works
        -- Detecting CXX compiler ABI info
        -- Detecting CXX compiler ABI info - done
        -- Detecting CXX compile features
        -- Detecting CXX compile features - done
        -- Try OpenMP C flag = [/openmp]
        -- Performing Test OpenMP_FLAG_DETECTED
        -- Performing Test OpenMP_FLAG_DETECTED - Success
        -- Try OpenMP CXX flag = [/openmp]
        -- Performing Test OpenMP_FLAG_DETECTED
        -- Performing Test OpenMP_FLAG_DETECTED - Success
        -- Found OpenMP: /openmp
        -- Performing Test COMPILER_SUPPORTS_CXX11
        -- Performing Test COMPILER_SUPPORTS_CXX11 - Failed
        -- Performing Test COMPILER_SUPPORTS_CXX0X
        -- Performing Test COMPILER_SUPPORTS_CXX0X - Failed
        -- The compiler C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/x86_amd64/cl.exe has no C++11 support. Please use a different C++ compiler.
        -- Could NOT find PythonInterp (missing:  PYTHON_EXECUTABLE) (Required is at least version "2")
        -- Found PythonInterp: C:/Python35_x64/python.exe (found suitable version "3.5.2", minimum required is "3")
        -- Configuring done
        -- Generating done
        -- Build files have been written to: C:/github/xgboost/build

    Open the file *xgboost.sln* and build.
    The compilation works despite the warning saying that Visual Studio does not C++ 11 support.
    Last steps::

    * copy *libxgboost.dll* in *python-package/xgboost*
    * type ``python setup.py bdist_wheel``

    Last remark, `xgboost <https://pypi.python.org/pypi/xgboost>`_ is back on pypi today
