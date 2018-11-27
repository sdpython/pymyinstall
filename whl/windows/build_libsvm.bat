@echo off
set libname=libsvm
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
git clone --recursive https://github.com/cjlin1/%libname% %current%%libname%
goto build:

:update:
@echo Update '%libname%'.
cmd /C git pull origin master

:build:
pushd %current%%libname%
set PATH=%PATH%;"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64"
call VCVARS64.bat
@echo Build '%libname%'.
nmake -f Makefile.win lib
popd

:copy:
rem copy %current%%libname%\dist\*.whl %current%..\..\dist
copy %current%%libname%\windows\*.dll %current%%libname%\python

:test:
set PYTHONPATH=%current%%libname%\python
@echo Test '%libname%'.
python -c "import svmutil"
python -c "import svm;print('Version', svm.PRINT_STRING_FUN)"

:end:
@echo Done.