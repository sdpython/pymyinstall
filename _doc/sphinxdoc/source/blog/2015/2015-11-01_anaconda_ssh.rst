

.. blogpost::
    :title: Install Anaconda through SSH connection
    :keywords: Anaconda, SSH, Miniconda
    :date: 2015-11-01
    :categories: install, Anaconda, SSH
    
    The following page 
    `Install/Uninstall Anaconda Server <http://docs.continuum.io/anaconda-server/easy-gui/index>`_
    describes how to install Anaconda through a SSH connection and only a command line.
    It starts from `Miniconda <http://conda.pydata.org/miniconda.html>`_
    which is Anaconda without this exhaustive list of modules.
    By default, the page gives the instruction for Python 2.7.
    I just changed them to get Python 3.4.
    
    As I do not want to install a server, I directly go to the
    second step ::
                
        curl 'http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh' > Miniconda3.sh
        bash Miniconda3.sh
        
    I avoid adding the new Python to be added to the current ``PATH``. I followed the instructions,
    I left the current command line window to open a new one. Miniconda3 is installed in ``/home/binstar/miniconda3``.
    We go then to::
    
        cd /home/azureuser/miniconda3/bin
        
    To be sure I'm using this version and batch file in this folder, 
    I need to add ``./`` before typing any command. We update *conda*::
    
        ./conda update conda
        
    After that, we can install the necessary packages::
    
        ./conda install numpy pandas matplotlib jupyter
        
    To install all the necessary modules for 
    `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_::
    
        ./pip install pymyinstall --upgrade
        ./pymy_install3 --set=pyensae
        ./pip install pyensae
        
    And finally run jupyter::
    
        ./jupyter-console
        
    On OS X, please check the list of available builds
    at `Miniconda installer archive <https://repo.continuum.io/miniconda/>`_. 
    It should be::
    
        curl 'http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh' > Miniconda3.sh
        bash Miniconda3.sh