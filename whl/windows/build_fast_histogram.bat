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
if exist fast_histogram goto update:
git clone --recursive https://github.com/astrofrog/fast-histogram %current%fast_histogram
goto build:

:update:
git pull %current%fast_histogram

:build:
pushd %current%fast_histogram
python -u setup.py bdist_wheel
popd

:copy:
copy %current%fast_histogram\dist\*.whl %current%..\..\dist