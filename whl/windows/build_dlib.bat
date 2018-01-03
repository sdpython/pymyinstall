@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python363_x64

:start_script:
@echo [dlib] build
set BOOST_VERSION_LIB=1_66
set BOOST_VERSION=1.66.0
set BOOST_VERSION_=1_66_0
@echo [dlib] boost version %BOOST_VERSION%
set current=%~dp0

set PATH=%pythonexe%;%pythonexe%\Scripts;%pythonexe%\libs;%PATH%
@echo [dlib] create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
@echo [dlib] CLONE https://github.com/davisking/dlib
if exist dlib goto update:
git clone --recursive https://github.com/davisking/dlib %current%dlib
goto build:

:update:
@echo [dlib] PULL %current%dlib
git pull %current%dlib

:build:
@echo [dlib] BUILD
pushd %current%dlib
@echo BUILD following APPVEYOR instructions
mkdir build_test
pushd build_test
cmake -G "Visual Studio 14 2015 Win64" -DPYTHON3=1 ..\..\tools\python
rem ../dlib/test 
cmake --build . --config Release
popd

:python:
@echo [dlib] build python module from %current%dlib
if exist %BOOST_LIBRARYDIR%\libboost_python3-vc140-s-%BOOST_VERSION_LIB%.lib goto good2:
@echo [dlib] ERROR: Unable to find(2) '%BOOST_LIBRARYDIR%\libboost_python3-vc140-s-%BOOST_VERSION_LIB%.lib'
@echo [dlib] call build_boost_python_static.bat from a visual studio command line in 64 bits
exit 1

:good2:
:appveyor:
pushd %current%dlib
if exist build_test goto python:
@echo [dlib] BUILD following APPVEYOR instructions
mkdir build_test
pushd build_test
cmake -G "Visual Studio 14 2015 Win64" ../dlib/test
cmake --build . --config Release
popd

:python:
popd
@echo [dlib] build_wheel
set PATH=%pythonexe%;%pythonexe%\include;%pythonexe%\libs;%BOOST_LIBRARYDIR%;%PATH%
@echo [dlib] copy Python lib into %BOOST_LIBRARYDIR%
copy %pythonexe%\libs\*.lib %BOOST_LIBRARYDIR%
copy %BOOST_LIBRARYDIR%\libboost_python3-vc140-mt-s-%BOOST_VERSION_LIB%.lib %BOOST_LIBRARYDIR%\libboost_python-vc140-mt-s-%BOOST_VERSION_LIB%.lib
copy %BOOST_LIBRARYDIR%\libboost_numpy3-vc140-mt-s-%BOOST_VERSION_LIB%.lib %BOOST_LIBRARYDIR%\libboost_numpy3-vc140-mt-s-%BOOST_VERSION_LIB%.lib
@echo [dlib] done copy
pushd %current%dlib
python -u %current%dlib\setup.py build_ext --inplace --yes USE_AVX_INSTRUCTIONS

@echo [dlib] create wheel
python -u %current%dlib\setup.py bdist_wheel
popd

:copy:
@echo COPY
copy %current%param\dist\*.whl %current%..\..\dist

:end:
@echo [dlib] Done.

