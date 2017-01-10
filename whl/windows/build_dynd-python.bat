@echo off
rem The script requires one argument: Python PATH
rem https://github.com/libdynd/dynd-python/blob/master/BUILD_INSTALL.md

set PATH=%1;%1\Scripts;%PATH%
git clone --recursive https://github.com/libdynd/dynd-python
cd dynd-python
git clone --recursive https://github.com/libdynd/libdynd
python setup.py develop
python setup.py bdist_wheel