@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python36_x64

:start_script:
@echo [dlib] build
set BOOST_VERSION=1.64.0
set BOOST_VERSION_=1_64_0
@echo [dlib] boost version %BOOST_VERSION%
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
@echo [dlib] create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
@echo [dlib] CLONE https://github.com/davisking/dlib
if exist dlib goto update:
@echo [dlib] clone
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
@echo BUILD python module
set PATH=%~dp0vcpkg\packages\boost_x64-windows\bin;%PATH%
set BOOST_ROOT=%~dp0boost\boost_%BOOST_VERSION_%
set BOOST_LIBRARYDIR=%~dp0boost\boost_%BOOST_VERSION_%\stage\lib
@echo [dlib] BOOST_ROOT=%~dp0boost\boost_%BOOST_VERSION_%
@echo [dlib] BOOST_LIBRARYDIR=%~dp0boost\boost_%BOOST_VERSION_%\stage\lib
if exist %BOOST_ROOT% goto good1:
@echo Unable to find(1) %BOOST_ROOT%
exit 1
:good1:
if exist %BOOST_LIBRARYDIR% goto python:
@echo Unable to find(2) %BOOST_LIBRARYDIR%
exit 1

:python:
@echo [dlib] build python module from %current%dlib
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
