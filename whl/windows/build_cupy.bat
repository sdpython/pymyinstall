@echo off
set project_name=cupy
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
if exist %project_name% goto update:
git clone --recursive https://github.com/%project_name%/%project_name% %current%%project_name%
goto build:


:update:
git pull %current%%project_name%

:build:
pushd %current%%project_name%
python -u setup.py bdist_wheel
popd

:copy:
copy %current%%project_name%\dist\*.whl %current%..\..\dist