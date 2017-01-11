@echo off
rem The script requires one argument: Python PATH
rem https://github.com/libdynd/dynd-python/blob/master/BUILD_INSTALL.md

if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python35_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
@echo create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
if exist dynd goto update:
git clone --recursive https://github.com/libdynd/dynd-python %current%dync
pushd %current%dync\dynd-python
git clone --recursive https://github.com/libdynd/libdynd
popd
goto buid:

:update:
git pull %current%dynd
pushd %current%dync\dynd-python
git pull
popd

:build:
pushd %current%dynd
python -u setup.py develop
python -u setup.py bdist_wheel
popd

:copy:
copy %current%polylearn\dist\*.whl %current%..\..\dist