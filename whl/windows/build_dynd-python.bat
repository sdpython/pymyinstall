@echo off
rem The script requires one argument: Python PATH
rem https://github.com/libdynd/dynd-python/blob/master/BUILD_INSTALL.md

if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python363_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
@echo create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist
if not exist %current%dynd mkdir %current%dynd
rem if not exist %current%dynd\dynd-python mkdir %current%dynd\dynd-python
rem if not exist %current%dynd\libdynd mkdir %current%dynd\libdynd

:clone:
if exist %current%dynd\dynd-python\libdynd goto update:
pushd %current%dynd
git clone --recursive https://github.com/libdynd/dynd-python
pushd dynd-python
git clone --recursive https://github.com/libdynd/libdynd
popd
popd
goto build:

:update:
git pull %current%dynd\dynd-python
pushd %current%dynd\dynd-python
git pull
pushd libdynd
git pull
popd
popd

:build:
pushd %current%dynd\dynd-python
python -u setup.py develop
python -u setup.py bdist_wheel
popd

:copy:
copy %current%dynd\dynd-python\dist\*.whl %current%..\..\dist