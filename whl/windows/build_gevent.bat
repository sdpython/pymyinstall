@echo off
set libname=gevent
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python370_x64

:start_script:
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
set dest=%current%..\..\dist
if exist %dest% goto clone:
@echo Create '%dest%'.
mkdir "%dest%"

:clone:
if exist %current%%libname% goto update:
git clone --recursive https://github.com/%libname%/%libname% %current%%libname%
goto build:

:update:
@echo Update '%libname%'.
cmd /C git pull origin master

:build:
pushd %current%%libname%
rem set PATH=%PATH%;"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64"
rem call VCVARS64.bat
python -u setup.py bdist_wheel

:test:
set PYTHONPATH=%current%%libname%\python
@echo Test '%libname%'.
python -c "import gevent"
python -c "import gevent;print('Version', gevent.__version__)"

:end:
@echo Done.