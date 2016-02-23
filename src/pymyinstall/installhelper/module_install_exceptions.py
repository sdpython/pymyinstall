"""
@file
@brief Exceptions raised during the installation of a module
"""


class MissingPackageOnPyPiException(Exception):

    """
    raised when a package is not found on pipy
    """
    pass


class MissingInstalledPackageException(Exception):

    """
    raised when a package is not installed
    """
    pass


class AnnoyingPackageException(Exception):

    """
    raised when a package is not on pypi
    """
    pass


class MissingVersionOnPyPiException(Exception):

    """
    raised when a version is missing on pipy
    """
    pass


class MissingVersionWheelException(Exception):

    """
    raised when a version is missing as a wheel
    """
    pass


class MissingWheelException(Exception):

    """
    raised when a wheel is missing
    """
    pass


class MissingReferenceException(Exception):

    """
    raised when a module is not referenced by this package
    """
    pass


class InstallError(Exception):
    """
    raised when a package cannot be installed
    """
    pass


class DownloadError(Exception):
    """
    raised when a package cannot be downloaded
    """
    pass


class ConfigurationError(Exception):
    """
    raised when something is wrong the current configuration
    """
    pass


class UpdatePipError(Exception):
    """
    raised when pip cannot be update or reinstalled
    """
    pass


class RunCmdError(Exception):
    """
    raised when a command line cannot be run
    """
    pass


class WrongVersionError(Exception):
    """
    cannot interpret a version
    """
    pass


class WrongWheelException(Exception):
    """
    raised when the downloaded wheel seems wrong
    """
    pass


class UnavailableCustomBuildError(Exception):
    """
    raise when a module does not have a custom build
    """
    pass
