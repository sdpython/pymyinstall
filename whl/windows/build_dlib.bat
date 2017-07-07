@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python36_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
@echo create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
@echo CLONE
if exist param goto update:
git clone --recursive https://github.com/davisking/dlib %current%dlib
goto build:

:update:
@echo PULL
git pull %current%param

:build:
@echo BUILD

:appveyor:
pushd %current%dlib
@echo BUILD following APPVEYOR instructions
mkdir build_test
cd build_test
cmake -G "Visual Studio 14 2015 Win64" ../dlib/test
cmake --build . --config Release
popd
  
:python:
@echo BUILD python module
set version=1_64_0
set BOOST_ROOT=%~dp0boost\boost_%version%
set BOOST_LIBRARYDIR=%~dp0boost\build\boost\bin.v2\libs
if exist %BOOST_ROOT% goto good1:
@echo Unable to find(1) %BOOST_ROOT%
exit 1
:good1:
if exist %BOOST_LIBRARYDIR% goto good2:
@echo Unable to find(2) %BOOST_LIBRARYDIR%
exit 1

:good2:
rem boost
rem got boost/build/tools
rem run bootstrap.bat
rem run b2 toolset=msvc-14.0 --build-type=complete --abbreviate-paths architecture=x86 address-model=64 install -j4

:python:
set PATH=c:\Python36_x64;%PATH%
pushd %current%dlib
python -u %current%dlib\setup.py build_ext --inplace --yes USE_AVX_INSTRUCTIONS
python -u %current%dlib\setup.py bdist_wheel
popd

:copy:
@echo COPY
copy %current%param\dist\*.whl %current%..\..\dist
