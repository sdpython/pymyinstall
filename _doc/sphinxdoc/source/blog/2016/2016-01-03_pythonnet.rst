

.. blogpost::
    :title: pythonnet for Python 3.5
    :keywords: pythonnet, .net, C#, python
    :date: 2016-01-03
    :categories: install, modules, pythonnet
    
    People usually install modules from
    `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pythonnet>`_
    on Windows. This also goes for 
    `pythonnet <https://github.com/fkarb/pythonnet>`_ which was compiled 
    this github repository. This release works somehow for Python 3.5 but fails if 
    some functionalities are required. You can try::
    
        import clr
        clr.__dict__
    
    The module does not seem to be maintained an a regular basis.
    So I tried to make some changes to make it work for Python 3.5:
    `pythonnet-2.1.1-cp35-none-win_amd64.whl <https://github.com/sdpython/pythonnet/releases>`_.
    The source are available at: 
    `sdpython/pythonnet <https://github.com/sdpython/pythonnet>`_.
    Some changes were needed to replicate the changes in Python API
    introduced by Python 3.5. The Python API and its duplication in C#
    on Pythonnet side must match otherwise some unexpected error will happen.
    A classical C++ error as Python or Pythonnet is going to 
    overwrite some memory it should not access.
    
    Debugging is still uneasy. Maybe I missed something. I downloaded the source
    from `Python website <https://www.python.org/downloads/source/>`_ and I inserted
    many prints to understand where the module was stuck::
    
        cd C:\github\pythonnet\pybin\x64\Release35
        D:\python_source\Python-3.5.1\PCbuild\amd64\python -c "import clr;print(clr.__dict__);print(type(clr))"
        
    However, with this new version, the following instruction fails::
    
        array = numpy.ones((2,2))
    
        File "test_pythonnet.py", line 97, in test_pythonnet_array
            ar = IntPtr.__overloads__[int](array.__array_interface__['data'][0])
        TypeError: no constructor matches given arguments

    It is now replaced by::
    
        array = numpy.ones((2,2))
        from clr import IntPtr_long
        ar = IntPtr_long(array.__array_interface__['data'][0])
    
    Pythonnet was compiled with for Python 3.5 with Visual Studio 2015.
    If it fails, you might need to install it.