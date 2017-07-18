@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python36_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%pythonexe%\libs;%PATH%
@echo create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
@echo [dlib] CLONE
if exist param goto update:
git clone --recursive https://github.com/davisking/dlib %current%dlib
goto build:

:update:
@echo [dlib] PULL
git pull %current%param

:build:
@echo [dlib] BUILD

:boost:
@echo [dlib] set up boost
set version=1_64_0
set BOOST_ROOT=%~dp0boost\boost_%version%\boost_%version%
set BOOST_LIBRARYDIR=%~dp0boost\boost_%version%\boost_%version%\stage\x64\lib
if exist %BOOST_ROOT%\bootstrap.bat goto good1:
@echo [dlib] ERROR: Unable to find(1) %BOOST_ROOT%
exit 1

:good1:
if exist %BOOST_LIBRARYDIR%\libboost_python3-vc140-s-1_64.lib goto good2:
@echo [dlib] ERROR: Unable to find(2) '%BOOST_LIBRARYDIR%\libboost_python3-vc140-s-1_64.lib'
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
copy %BOOST_LIBRARYDIR%\libboost_python3-vc140-mt-s-1_64.lib %BOOST_LIBRARYDIR%\libboost_python-vc140-mt-s-1_64.lib
copy %BOOST_LIBRARYDIR%\libboost_numpy3-vc140-mt-s-1_64.lib %BOOST_LIBRARYDIR%\libboost_numpy3-vc140-mt-s-1_64.lib
@echo [dlib] done copy
pushd %current%dlib
python -u %current%dlib\setup.py build_ext --inplace --yes USE_AVX_INSTRUCTIONS
python -u %current%dlib\setup.py bdist_wheel
popd

