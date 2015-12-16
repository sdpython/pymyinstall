"""
@file
@brief Custom versions of some modules
"""
import sys
import platform


class UnavailableCustomBuildError(Exception):
    """
    raise when a module does not have a custom build
    """
    pass
