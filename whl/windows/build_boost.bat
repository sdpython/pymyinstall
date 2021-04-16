@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python363_x64

:start_script:
@echo [boost] %current%boost
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;%PATH%
if not exist boost mkdir boost
pushd boost

:download:
set version=1_66_0
set version2=1.66.0
if exist %current%boost\boost_%version%.7z goto unzip:
@echo [boost] Download boost
bitsadmin /transfer wcb /priority high https://dl.bintray.com/boostorg/release/%version2%/source/boost_%version%.7z %current%boost\boost_%version%.7z
@echo [boost] Done download.

:unzip:
if exist %current%boost\boost_%version%\boost\python\return_arg.hpp goto booststrap:
@echo [boost] Unzip xgboost
set PATH=%PATH%;C:\Program Files\7-Zip\
7z x %current%boost\boost_%version%.7z -o%current%boost
@echo [boost] Done unzip.

:booststrap:
if exist %current%boost\MYINST\share\boost-build\src\tools\gcc.py goto b2:
@echo [boost] bootstrap
pushd %current%boost\boost_%version%
cmd /c bootstrap msvc
popd
@echo [boost] Done Bootstrap


:b2:
if exist %current%boost\MYINST\share\boost-build\src\tools\gcc.py goto build:
@echo [boost] B2 install
pushd %current%boost\boost_%version%
cmd /c b2 --prefix=%current%boost\MYINST install toolset=msvc runtime-link=static address-model=64
popd
@echo [boost] Done b2 install


:build:
@echo [boost] b2 build
set PATH=%PATH%;%current%boost\MYINST\bin
pushd %current%boost\boost_%version%
b2 --build-dir=%current%boost\build --with-python runtime-link=static address-model=64 toolset=msvc --build-type=complete stage
popd
@echo [boost] Done b2 build

:end:
@echo [boost] Done.
popd