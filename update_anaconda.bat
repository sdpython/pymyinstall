if "%1"=="" goto default_value:
set anaconda=%1
if exist %anaconda%.exe set anaconda=%1\..
goto next:

:default_value:
set anaconda=c:\Anaconda3

:next:
cd %anaconda%\Scripts
conda update -y --all
