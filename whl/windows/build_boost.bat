@echo off
@echo [boost] begin
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python36_x64

:start_script:
set current=%~dp0

@echo [boost] vcvarsall.bat
pushd "C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC"
call vcvarsall.bat x64
popd
@echo [boost] vcvarsall.bat Done

@echo [boost] mkdir
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%
if not exist boost mkdir boost
pushd boost

:download:
set version=1_64_0
set version2=1.64.0
if exist %current%boost\boost_%version% goto booststrap:
@echo [boost] Download
bitsadmin /transfer wcb /priority high https://dl.bintray.com/boostorg/release/%version2%/source/boost_%version%.7z %current%boost\boost_%version%.7z
set PATH=%PATH%;C:\Program Files\7-Zip\
@echo Unzip xgboost
7z x %current%boost\boost_%version%.7z -o%current%boost\boost_%version%

:booststrap:
@echo [boost] BOOTSTRAP ---------------------
cd %current%boost\boost_%version%\boost_%version%\tools\build
cmd /c bootstrap

:b2:
@echo [boost] B2 ---------------------
cmd /c b2 install --prefix=%current%boost\MYINST

:python-config:
@echo [boost] config in %current%boost\MYINST\share\boost-build\example\user-config.jam
if not exist %current%boost\MYINST\share\boost-build\example\user-config.jam goto erroruser:
@echo "using python : 3.6: c:/Python36_x64/python.exe : c:/Python36_x64/include : c:/Python36_x64/libs ;" >> %current%boost\MYINST\share\boost-build\example\user-config.jam
goto build:

:erroruser:
@echo Cannot find %current%boost\MYINST\share\boost-build\example\user-config.jam.
exit 1


:build:
@echo [boost] build
set PATH=%PATH%;%current%boost\MYINST\bin
cd %current%boost\boost_%version%\boost_%version%
b2 --build-dir=%current%boost\build toolset=msvc --stagedir=stage/x64 --without-python --build-type=complete architecture=x86 address-model=64 runtime-link=static msvc stage
@echo [boost] done