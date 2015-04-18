if "%1"=="" goto default_value:
set anaconda=%1
if exists %anaconda%.exe set anaconda=%1\..
goto next:

:default_value:
set anaconda=c:\Anaconda2

:next:
cd %anaconda%\Scripts
conda update --all
