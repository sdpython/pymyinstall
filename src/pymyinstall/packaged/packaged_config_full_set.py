"""
@file
@brief Defines different set of modules to install.
"""
from .packaged_config import small_set, sphinx_theme_set, extended_set, azure_set, ensae_set, teachings_set


def ensae_fullset():
    """
    .. index:: ENSAE

    Installation of all possible modules for my teachings at the ENSAE.
    This list is described at :ref:`l-ensae_fullset-table`.
    """
    base = small_set() +  \
        sphinx_theme_set() + \
        extended_set() + \
        azure_set() + \
        ensae_set() + \
        teachings_set()

    return base
