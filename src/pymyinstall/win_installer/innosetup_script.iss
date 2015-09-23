#define MyAppName "PythonENSAE"
#define MyAppVersion "0.1"
#define MyAppPublisher "Xavier Dupré"
#define MyAppURL "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html"
#define MyAbsPath "__DISTPATH__"
#define MyAppURLAct "http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html"
#define MyAppURLCB "http://lesenfantscodaient.fr/"
#define CMDApp "%windir%\system32\cmd.exe"

#define MyAppVSURL "https://www.visualstudio.com/fr-fr/products/visual-studio-community-vs.aspx"
#define MyAppMiktexURL "http://miktex.org/"
#define MyAppTXCURL "http://www.texniccenter.org/"
#define MyAppGitURL "https://git-scm.com/"
#define MyAppGitHubURL "https://desktop.github.com/"
#define MyAppTGitURL "https://tortoisegit.org/"
#define MyAppRStudioURL "https://www.rstudio.com/"
#define MyAppPyCharmURL "https://www.jetbrains.com/pycharm/"
#define MyAppVS2015 "https://www.microsoft.com/en-us/download/details.aspx?id=48145"
#define MyAppSDK1081 "https://dev.windows.com/en-US/downloads/windows-10-sdk"
#define MyCygwin "https://www.cygwin.com/"
#define MyRTools "https://cran.r-project.org/bin/windows/Rtools/"
#define MyInkScape "https://inkscape.org/fr/"
#define MyJenkins "https://jenkins-ci.org/"
#define MyW10Runtime "http://www.microsoft.com/en-us/download/details.aspx?id=48234"


[Setup]
AppId={{4A9659CF-2654-493E-A751-58AE22D9D390}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=.
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile={#MyAbsPath}\LICENSE.txt
OutputDir={#MyAbsPath}\dist\setup
OutputBaseFilename=PythonENSAE
SetupIconFile={#MyAbsPath}\tools\icons\PythonENSAE.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "{#MyAbsPath}\python\*"; DestDir: "{app}\python"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAbsPath}\tools\*"; DestDir: "{app}\tools"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAbsPath}\workspace\*"; DestDir: "{app}\workspace"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#MyAbsPath}\config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{app}\actuariat_python sur Internet"; IconFilename: "{app}\tools\icons\actuariat_python.ico"; Filename: "{#MyAppURLAct}"
Name: "{app}\lesenfantscodaient.fr"; IconFilename: "{app}\tools\icons\code_beatrix.ico"; Filename: "{#MyAppURLCB}"
Name: "{app}\UninstallProgram"; Filename: "{uninstallexe}"
Name: "{app}\ENSAE Python sur Internet"; IconFilename: "{app}\tools\icons\teachings.ico"; Filename: "{#MyAppURL}"
; install
Name: "{app}\Installer\Visual Studio Community"; IconFilename: "{app}\tools\icons\vs.ico"; Filename: "{#MyAppVSURL}"
Name: "{app}\Installer\Miktex"; IconFilename: "{app}\tools\icons\miktex.ico"; Filename: "{#MyAppMiktexURL}"
Name: "{app}\Installer\TeXnicCenter"; IconFilename: "{app}\tools\icons\txc.ico"; Filename: "{#MyAppTXCURL}"
Name: "{app}\Installer\Git"; IconFilename: "{app}\tools\icons\git.ico"; Filename: "{#MyAppGitURL}"
Name: "{app}\Installer\GitHub Desktop"; IconFilename: "{app}\tools\icons\github.ico"; Filename: "{#MyAppGitHubURL}"
Name: "{app}\Installer\Tortoise Git"; IconFilename: "{app}\tools\icons\tortoisegit.ico"; Filename: "{#MyAppTGitURL}"
Name: "{app}\Installer\RSudio"; IconFilename: "{app}\tools\icons\rstudio.ico"; Filename: "{#MyAppRStudioURL}"
Name: "{app}\Installer\PyCharm"; IconFilename: "{app}\tools\icons\pycharm.ico"; Filename: "{#MyAppPyCharmURL}"
Name: "{app}\Installer\Visual C++ Redistributable for Visual Studio 2015"; IconFilename: "{app}\tools\icons\vs2015.ico"; Filename: "{#MyAppVS2015}"
Name: "{app}\Installer\SDK for Windows 8.1-10"; IconFilename: "{app}\tools\icons\vs2015.ico"; Filename: "{#MyAppSDK1081}"
Name: "{app}\Installer\Cygwin"; IconFilename: "{app}\tools\icons\cygwin.ico"; Filename: "{#MyCygwin}"
Name: "{app}\Installer\RTools"; IconFilename: "{app}\tools\icons\r.ico"; Filename: "{#MyRTools}"
Name: "{app}\Installer\InkScape (for Sphinx)"; IconFilename: "{app}\tools\icons\inkscape.ico"; Filename: "{#MyInkScape}"
Name: "{app}\Installer\Jenkins"; IconFilename: "{app}\tools\icons\jenkins.ico"; Filename: "{#MyJenkins}"
Name: "{app}\Installer\Windows 10 Universal C Runtime (for llvmlite, blaze, numba)"; IconFilename: "{app}\tools\icons\vs2015.ico"; Filename: "{#MyW10Runtime}"
; editors
Name: "{app}\Scite"; IconFilename: "{app}\tools\icons\Scite.ico"; Filename: "{app}\config\scite.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
Name: "{app}\SQLiteSpy"; IconFilename: "{app}\tools\icons\sqlitespy.ico"; Filename: "{app}\config\sqlitespy.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
; tools
Name: "{app}\R Console"; IconFilename: "{app}\tools\icons\r.ico"; Filename: "{app}\config\r_console.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
Name: "{app}\R Gui"; IconFilename: "{app}\tools\icons\r.ico"; Filename: "{app}\config\r_gui.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
;Name: "{app}\Julia Console"; IconFilename: "{app}\tools\icons\julia.ico"; Filename: "{app}\tools\Julia\bin\x64\julia.exe"; IconIndex: 0; WorkingDir: "{app}\workspace"
; Jupyter
Name: "{app}\Jupyter Console"; IconFilename: "{app}\tools\icons\ipython.ico"; Filename: "{app}\config\jupyter_console.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
Name: "{app}\Jupyter Qt Console"; IconFilename: "{app}\tools\icons\ipython.ico"; Filename: "{app}\config\jupyter_qtconsole.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"; Parameters: "--pylab=inline"
Name: "{app}\Jupyter Notebook"; IconFilename: "{app}\tools\icons\jupyter.ico"; Filename: "{app}\config\jupyter_notebook.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"; Parameters: "--notebook-dir={app}\workspace --pylab=inline"
; python
Name: "{app}\Python Console"; IconFilename: "{app}\tools\icons\python.ico"; Filename: "{app}\config\python_console.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
Name: "{app}\Rodeo"; IconFilename: "{app}\tools\icons\yhat.ico"; Filename: "{app}\config\rodeo.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"; Parameters: "{app}\workspace"
Name: "{app}\Spyder"; IconFilename: "{app}\tools\icons\spyder.ico"; Filename: "{app}\config\spyder.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"; Parameters: "{app}\workspace"
; rss
Name: "{app}\RSS"; IconFilename: "{app}\tools\icons\pyrsslocal.ico"; Filename: "{app}\config\run_fetch_rss.bat"; IconIndex: 0; WorkingDir: "{app}\config"; Parameters: "{app}\config"
; putty
Name: "{app}\Putty"; IconFilename: "{app}\tools\icons\putty.ico"; Filename: "{app}\config\putty.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"
; update
Name: "{app}\UpdatePython"; IconFilename: "{app}\tools\icons\pymyinstall.ico"; Filename: "{app}\config\run_update_all_packages.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"; Parameters: "{app}\config"

[Run]
Filename: "{app}\config\add_kernels.bat"; Parameters:"ENSAE"; Description: "Configure Kernels"; 
Filename: "{app}\config\replace_shebang.bat"; Description: "Fix distribution shebangs"; 
