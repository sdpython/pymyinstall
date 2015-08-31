#-*- coding: utf-8 -*-
"""
@file
@brief Helpers about configurations
"""
import sys


def is_64bit():
    """
    tells if the python is 64 bit or not

    @return     boolean
    """
    return sys.maxsize > 2 ** 32
