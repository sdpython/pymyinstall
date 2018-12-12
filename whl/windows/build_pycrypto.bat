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
if exist pycrypto goto update:
git clone --recursive https://github.com/sdpython/pycrypto %current%pycrypto
goto build:

:update:
git pull %current%pycrypto

:build:
rem see https://github.com/aleaxit/gmpy
pushd %current%pycrypto
python -u setup.py -q build
popd

:copy:
copy %current%polylearn\dist\*.whl %current%..\..\dist