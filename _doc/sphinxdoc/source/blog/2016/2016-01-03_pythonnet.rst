

.. blogpost::
    :title: pythonnet for Python 3.5
    :keywords: pythonnet, .net, C#, python, issue
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
    
    Pythonnet was compiled with for Python 3.5 with Visual Studio 2015 (Free Community Edition).
    However you might face the following error::
    
        Unhandled Exception: System.IO.FileLoadException: Could not load file or assembly 'file:///<apath>\Python.Runtime.dll' or one of its dependencies. 
        Operation is not supported. (Exception from HRESULT: 0x80131515) ---> System.NotSupportedException: An attempt was made to load an assembly 
        from a network location which would have caused the assembly to be sandboxed in previous versions of the .NET Framework. 
        This release of the .NET Framework does not enable CAS policy by default, so this load may be dangerous. 
        If this load is not intended to sandbox the assembly, please enable the loadFromRemoteSources switch. See http://go.microsoft.com/fwlink/?LinkId=155569 for more information.
           --- End of inner exception stack trace ---
           at System.Reflection.RuntimeAssembly._nLoad(AssemblyName fileName, String codeBase, Evidence assemblySecurity, RuntimeAssembly locationHint, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
           at System.Reflection.RuntimeAssembly.InternalLoadAssemblyName(AssemblyName assemblyRef, Evidence assemblySecurity, RuntimeAssembly reqAssembly, StackCrawlMark& stackMark, IntPtr pPrivHostBinder, Boolean throwOnFileNotFound, Boolean forIntrospection, Boolean suppressSecurityChecks)
           at System.Reflection.RuntimeAssembly.InternalLoadFrom(String assemblyFile, Evidence securityEvidence, Byte[] hashValue, AssemblyHashAlgorithm hashAlgorithm, Boolean forIntrospection, Boolean suppressSecurityChecks, StackCrawlMark& stackMark)
           at System.Reflection.Assembly.LoadFrom(String assemblyFile)
           at clrModule.PyInit_clr()
           
    In that case, I suggest to get the source and to compile them with Visual Studio 2015
    on your machine, it should import the missing DLL which I'm still trying to find out.
    The DLL was compiled on an Azure Virtual Machine. You might have to recompile
    it on your own machine.
    
    