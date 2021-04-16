@echo off
if "%1"=="" goto default_value_python:
if "%1"=="default" goto default_value_python:
set pythonexe=%1
goto start_script:

:default_value_python:
set pythonexe=c:\Python363_x64

:start_script:
@echo [boost] start building boost
set current=%~dp0
set PATH=%pythonexe%;%pythonexe%\Scripts;%PATH%

:vcpkg:
if exist vcpkg\scripts\bootstrap.ps1 goto bcpkgbuild:
@echo [boost] clone vcpkg
git clone https://github.com/Microsoft/vcpkg

:bcpkgbuild:
pushd vcpkg
if exist vcpkg.exe goto boost:
@echo [boost] build vcpkg
powershell -exec bypass scripts\bootstrap.ps1

:boost:
if exist packages\boost_x64-windows goto end:
@echo [boost] build boost
vcpkg install boost:x64-windows --with-python address-model=64 runtime-link=static

:end:
popd
@echo [boost] Done.