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
if exist protobuf goto update:
git clone --recursive https://github.com/protocolbuffers/protobuf %current%protobuf
goto build:

:update:
git pull %current%protobuf

:build:
pushd %current%protobuf

@echo on
set vcplatform=x64
set platform=x64
set configuration=Release
set generator=Visual Studio 15 Win64
set language=cpp
set PATH="C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\amd64";%PATH%
appveyor
@echo off

popd
