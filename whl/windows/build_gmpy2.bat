@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python370_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
@echo create %current%..\..\dist
if not exist %current%..\..\dist mkdir %current%..\..\dist

:clone:
if exist gmpy goto update:
git clone --recursive https://github.com/aleaxit/gmpy %current%gmpy
goto build:

:update:
git pull %current%gmpy

:build:
pushd %current%gmpy
python -u setup.py bdist_wheel
popd

:copy:
copy %current%gmpy\dist\*.whl %current%..\..\dist