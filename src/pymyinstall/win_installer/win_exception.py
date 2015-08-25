"""
@file
@brief Helpers, inspired from `utils.py <https://github.com/winpython/winpython/blob/master/winpython/utils.py>`_
"""


class WinInstallException(Exception):

    """
    exception raised by this package
    """
    pass


class WinInstallPackageException(Exception):

    """
    exception raised by this package when installing a Python package
    """
    pass


class WinInstallMissingDependency(Exception):
    """
    raised when a dependency is missing
    """
    pass
