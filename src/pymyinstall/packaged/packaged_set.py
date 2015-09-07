"""
@file
@brief Defines different sets of modules to install in addition to the existing ones in @see md packaged_config.
"""
from .packaged_config import small_set, sphinx_theme_set, extended_set, ensae_set, teachings_set, iot_set


def ensae_fullset():
    """
    .. index:: ENSAE

    Installation of all possible modules for my teachings at the ENSAE.
    This list is described at :ref:`l-ensae_fullset-table`.
    """
    base = small_set() +  \
        sphinx_theme_set() + \
        extended_set() + \
        ensae_set() + \
        teachings_set()

    return base


def all_fullset():
    """
    Installation of all possible modules register in this module.
    Some if the list is described at :ref:`l-ensae_fullset-table`.
    """
    base = small_set() +  \
        sphinx_theme_set() + \
        extended_set() + \
        ensae_set() + \
        teachings_set() + \
        iot_set()

    return base
