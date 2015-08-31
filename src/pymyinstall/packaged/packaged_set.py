"""
@file
@brief Defines different sets of modules to install in addition to the existing ones in @see md packaged_config.
"""
from .packaged_config import small_set, sphinx_theme_set, extended_set, ensae_set, teachings_set


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
