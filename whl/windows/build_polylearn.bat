@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python35_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
if exist polylearn goto update:
git clone --recursive https://github.com/scikit-learn-contrib/polylearn %current%polylearn
goto buid:

:update:
git pull %current%polylearn

:build:
pushd %current%polylearn
python -u setup.py bdist_wheel
popd

:copy:
copy %current%polylearn\dist\*.whl %current%..\..\dist