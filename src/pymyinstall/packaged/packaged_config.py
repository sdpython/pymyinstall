#-*- coding: utf-8 -*-
"""
@file
@brief Defines different set of modules to install.


"""
from .packaged_config_0_minimal import minimal_set
from .packaged_config_0_pyquickhelper import pyquickhelper_set
from .packaged_config_1_small import small_set
from .packaged_config_2_sphinx import sphinx_theme_set
from .packaged_config_3_extended import extended_set
from .packaged_config_4_ml import ml_set, ensae_set
from .packaged_config_A_teachings import teachings_set
from .packaged_config_B_iot import iot_set
from .packaged_config_C_webscraping import scraping_set


def ensae_fullset():
    """
    Installation of all possible modules for my teachings at the ENSAE.
    """
    base = small_set() +  \
        sphinx_theme_set() + \
        extended_set() + \
        ensae_set() + \
        teachings_set()

    return base


def all_set():
    """
    Installation of all possible modules listed in this module.
    """
    base = small_set() +  \
        sphinx_theme_set() + \
        extended_set() + \
        ensae_set() + \
        teachings_set() + \
        iot_set() + \
        scraping_set()

    return base


def _function_set_name(f):
    """
    return the name of a function (not the module)

    @param      f       function
    @return             name

    .. versionadded:: 1.3
    """
    name = f.__name__
    return name.split(".")[-1]


def _build_set_correspondance(module_set):
    """
    builds a dictionary which returns a dictionary *{ name: function_set }*.

    @param      module_set      list of functions
    @return                     dictionary
    """
    res = {}
    for f in module_set:
        name = _function_set_name(f)
        res[name] = f
        name = name.replace("_set", "")
        res[name] = f
    return res


_modules_set = [minimal_set,
                small_set,
                sphinx_theme_set,
                extended_set,
                ml_set, ensae_set,
                teachings_set,
                iot_set,
                scraping_set,
                all_set,
                pyquickhelper_set,
                ]

_module_set_name = _build_set_correspondance(_modules_set)


def get_package_set(name):
    """
    return a list of modules included in one the functions imported in this module

    @param      name        set name
    @return                 list of modules

    See :ref:`l-name-set-table` to get the list of available sets.
    """
    if name not in _module_set_name:
        keys = [_.replace("_set", "") for _ in _module_set_name.keys()]
        keys = list(sorted(set(keys)))
        raise ValueError("unable to find set for {0}\navailable sets:\n{1}".format(
            name, "\n".join(keys)))
    return _module_set_name[name]


def name_sets_dataframe(module_set=None):
    """
    returns a RST tables which described all the available sets

    @param      module_set      list of module sets or None to get all the sets described in this module
    @return                     list of dictionaries ``[ { "name": name1, "description": description } ]``

    the functions requires
    """
    if module_set is None:
        module_set = _modules_set

    def process_doc(doc):
        lines = [_.strip() for _ in doc.split("\n")]
        res = []
        for line in lines:
            if "@return" in line:
                break
            if not line.startswith(".. index::"):
                res.append(line)
        return (" ".join(res)).strip()

    res = [{"name": _function_set_name(f).replace("_set", ""),
            "description": process_doc(f.__doc__)} for f in module_set]
    so = [(_["name"], _) for _ in res]
    so.sort()
    return [_[1] for _ in so]


def classifiers2string(l):
    """
    shorten the list of classifiers into a string

    @param      l       list
    @return             string

    Example::

        ['Development Status :: 4 - Beta', 'Programming Language :: Python',
         'Programming Language :: Python :: 2', 'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.3',
         'Programming Language :: Python :: 3.4', 'License :: OSI Approved :: Apache Software License']
    """
    if l is None:
        return ""
    res = []
    for cl in sorted(set(l)):
        if cl == "Programming Language :: Python":
            s = "Python"
        else:
            s = cl.replace("Programming Language :: Python :: ", "")
            s = s.replace("License :: ", "")
            s = s.replace("OSI Approved :: ", "OSI Approved ")
            s = s.replace("Development Status :: ", "")
            s = s.replace("Operating System :: Microsoft :: ", "")
            s = s.replace("Operating System :: ", "")
            s = s.replace("Implementation :: ", "")
            s = s.replace("Programming Language :: ", "")
            s = s.replace("Environment :: ", "")
            s = s.replace("POSIX :: ", "")
            s = s.replace("BSD :: ", "")
        if s == "3 :: Only":
            s = "py3"
        elif s == "2 :: Only":
            s = "py2"
        elif s == "MacOS :: MacOS X":
            s = "MacOS/X"
        elif s == "POSIX :: Linux":
            s = "Linux"
        elif s == "POSIX :: BSD :: FreeBSD":
            s = "FreeBSD"
        elif s == "X11 Applications :: Qt":
            s = "Qt"
        elif s.startswith("Windows"):
            s = "Windows"
        if "Framework" not in s and "Topic" not in s and "Intended Audience" not in s and "Natural Language" not in s:
            res.append(s)
    return ", ".join(res)
