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
; update
Name: "{app}\UpdatePython"; IconFilename: "{app}\tools\icons\pymyinstall.ico"; Filename: "{app}\config\run_update_all_packages.bat"; IconIndex: 0; WorkingDir: "{app}\workspace"; Parameters: "{app}\config"

[Run]
Filename: "{app}\config\add_kernels.bat"; Parameters:"ENSAE"; Description: "Configure Kernels"; 
Filename: "{app}\config\replace_shebang.bat"; Description: "Fix distribution shebangs (not portable anymore)"; 
