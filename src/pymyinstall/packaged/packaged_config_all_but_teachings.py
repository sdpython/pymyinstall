# -*- coding: utf-8 -*-
"""
@file
@brief Defines a set of module for teaching purpose.
"""


def all_but_teachings_set():
    """
    all availables modules except the one used to teach
    """
    #
    from .packaged_config import all_set, ensae_teaching_cs_set
    mod = all_set()
    names = set(m.name for m in ensae_teaching_cs_set())
    mod = [m for m in mod if m.name not in names]
    return mod
