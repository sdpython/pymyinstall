

.. blogpost::
    :title: Cannot import DLL
    :keywords: numpy, scipy, scikit-learn, DLL
    :date: 2015-10-01
    :categories: import, modules, issue
    
    I just tried::
    
        import scipy
        import scipy.stats
        
    But it failed with an error::
    
        DLL load failed
        
    The error happened again when using *scikit-learn*.
    As both modules are using *numpy*, I suspected than 
    this one was not properly installed. It usually happens
    on Windows when you upgrade a module which takes a dependency on it::
    
        pip install <module> --upgrade
        
    *pip* notices that *numpy* has to be updated.
    Unfortunately, many modules only accepts the MKL compilation
    available here: 
    `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy>`_::
    
        pip uninstall numpy
        pymy_install3 numpy