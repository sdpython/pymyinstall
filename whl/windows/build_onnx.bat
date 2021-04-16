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
git clone --recursive https://github.com/onnx/onnx %current%onnx
goto build:

:update:
git pull %current%onnx

:build:
pushd %current%onnx

set vcplatform=x64
set generator=Visual Studio 15 Win64
set language=cpp
set PATH="C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\amd64";%PATH%

rem set PROTOBUF_ROOT=<PROTOBUF>
rem set PROTOBUF_LIBRARIES=<PROTOBUF>\build_msvc\Release
rem set PROTOBUF_INCLUDE_DIRS=<PROTOBUF>\src
rem set ONNX_PROTOC_EXECUTABLE=<PROTOBUF>\build_msvc\Release\protoc.exe
rem set pybind11_DIR=<ONNX>\third_party\pybind11\tools
rem set CMAKE_ARGS=-Dpybind11_DIR=<GITHUBROOTWITH\\>\\onnx\\third_party\\pybind11\\tools -DPROTOBUF_INCLUDE_DIRS=<GITHUBROOTWITH\\>\\protobuf\\src -DPROTOBUF_LIBRARIES=<GITHUBROOTWITH\\>\\protobuf\\build_msvc\\Release -DONNX_PROTOC_EXECUTABLE=<GITHUBROOTWITH\\>\\protobuf\\build_msvc\\Release\\protoc.exe
set CMAKE_ARGS=-Dpybind11_DIR=<GITHUBROOTWITH\\>\\onnx\\third_party\\pybind11\\tools -DPROTOBUF_INCLUDE_DIRS=<GITHUBROOTWITH\\>\\protobuf\\src -DPROTOBUF_LIBRARIES=<GITHUBROOTWITH\\>\\protobuf\\build_msvc\\Release -DONNX_PROTOC_EXECUTABLE=<GITHUBROOTWITH\\>\\protobuf\\build_msvc\\Release\\protoc.exe
python setup.py bdist_wheel --universal

popd