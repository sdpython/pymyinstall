"""
@file
@brief Exceptions raised during the installation of a module
"""


class MissingPackageOnPyPiException(RuntimeError):

    """
    raised when a package is not found on pipy
    """
    pass


class MissingInstalledPackageException(RuntimeError):

    """
    raised when a package is not installed
    """
    pass


class AnnoyingPackageException(RuntimeError):

    """
    raised when a package is not on pypi
    """
    pass


class MissingVersionOnPyPiException(RuntimeError):

    """
    raised when a version is missing on pipy
    """
    pass


class MissingVersionWheelException(RuntimeError):

    """
    raised when a version is missing as a wheel
    """
    pass


class MissingWheelException(RuntimeError):

    """
    raised when a wheel is missing
    """
    pass


class MissingReferenceException(RuntimeError):

    """
    raised when a module is not referenced by this package
    """
    pass


class InstallError(RuntimeError):
    """
    raised when a package cannot be installed
    """
    pass


class DownloadError(RuntimeError):
    """
    raised when a package cannot be downloaded
    """
    pass


class ConfigurationError(RuntimeError):
    """
    raised when something is wrong the current configuration
    """
    pass


class UpdatePipError(RuntimeError):
    """
    raised when pip cannot be update or reinstalled
    """
    pass


class RunCmdError(RuntimeError):
    """
    raised when a command line cannot be run
    """
    pass


class WrongVersionError(RuntimeError):
    """
    cannot interpret a version
    """
    pass


class WrongWheelException(RuntimeError):
    """
    raised when the downloaded wheel seems wrong
    """
    pass


class UnavailableCustomBuildError(RuntimeError):
    """
    raise when a module does not have a custom build
    """
    pass
