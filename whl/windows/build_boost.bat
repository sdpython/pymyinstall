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
if not exist boost mkdir boost
pushd boost

:download:
set version=1_64_0
set version2=1.64.0
if exist %current%boost\boost_%version% goto booststrap:
@echo Download boost
bitsadmin /transfer wcb /priority high https://dl.bintray.com/boostorg/release/%version2%/source/boost_%version%.7z %current%boost\boost_%version%.7z
set PATH=%PATH%;C:\Program Files\7-Zip\
@echo Unzip xgboost
7z x %current%boost\boost_%version%.7z -o%current%boost\boost_%version%

:booststrap:
@echo BOOTSTRAP ---------------------
cd %current%boost\boost_%version%\boost_%version%\tools\build
rem cmd /c bootstrap

:b2:
@echo B2 ---------------------
rem cmd /c b2 install --prefix=%current%boost\MYINST

:python-config:
@echo [config]
rem @echo "using python : 3.6;" >> boost\MYINST\share\boost-build\example\user-config.jam

:build:
@echo [build]
set PATH=%PATH%;%current%boost\MYINST\bin
cd %current%boost\boost_%version%\boost_%version%
b2 --build-dir=%current%boost\build toolset=msvc --with-python --build-type=complete architecture=x86 address-model=64 runtime-link=static msvc stage
