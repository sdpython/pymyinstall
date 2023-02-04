"""
@file
@brief Helpers, inspired from `utils.py <https://github.com/winpython/winpython/blob/master/winpython/utils.py>`_
"""


class WinInstallException(RuntimeError):

    """
    exception raised by this package
    """
    pass


class WinInstallPackageException(RuntimeError):

    """
    exception raised by this package when installing a Python package
    """
    pass


class WinInstallMissingDependency(RuntimeError):
    """
    raised when a dependency is missing
    """
    pass


class WinInstallDistributionError(RuntimeError):
    """
    raised when an issue is detected in the distribution
    """
    pass
