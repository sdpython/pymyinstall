
.. blogpost::
    :title: Standalone distribution of Python
    :keywords: standalone, distribution
    :date: 2017-09-23
    :categories: distribution

    It is usually impossible to manually copy a Python distribution
    somewhere else after it was installed. The scripts such as ``pip.exe``
    contains the absolute location of the interpreter. That's why, if you
    insist to do so on Windows (like I do), you need to replace
    every path by a relative one or a blank one. That's what the
    following script is doing.

    ::

        from pymyinstall.win_installer import win_patch_paths
        win_patch_paths(r"C:\temp\Python36-3.6.2-amd64\Scripts", fLOG=print)

    The function :func:`win_patch_paths <pymyinstall.win_installer.win_patch.win_patch_paths>`
    looks for all paths following a given pattern and replace them by an empty string
    or a custom one.
