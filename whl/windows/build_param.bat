@echo off
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

:clone:
@echo CLONE
if exist param goto update:
git clone --recursive https://github.com/ioam/param %current%param
goto build:

:update:
@echo PULL
git pull %current%param

:build:
@echo BUILD
pushd %current%param
python -u setup.py build_ext --inplace
python -u setup.py bdist_wheel
popd

:copy:
@echo COPY
copy %current%param\dist\*.whl %current%..\..\dist