"""
@file
@brief Functions to get a status on the distribution

.. versionadded:: 1.1
"""
import os

import time
from .module_install_version import get_pypi_version
from ..packaged import all_set
from ..packaged.packaged_config import classifiers2string


def get_installed_modules(pypi=False, skip_betas=False, fLOG=None, stop=-1, short_list=None):
    """
    Returns all modules recored in this modules.
    Adds installed modules.

    @param      pypi            add pypi version
    @param      skip_betas      skip the intermediate functions
    @param      stop            stop after *stop* (or -1 for all)
    @param      short_list      short list of modules or None for all
    @param      fLOG            logging function
    @return                     list of dictionaries
    """
    mod = all_set()
    mod.sort()
    rows = [_.as_dict(rst_link=True) for _ in mod]
    for row in rows:
        row["classifier"] = classifiers2string(row["classifier"])
    keys = {mod["name"].lower(): mod for mod in rows}
    keys.update({mod["mname"].lower(): mod for mod in rows if mod["mname"]})

    from pip._internal.utils.misc import get_installed_distributions
    all_installed = []
    dists = get_installed_distributions()
    if short_list:
        dists = [_ for _ in dists if _.project_name in short_list]
    pack = map(lambda d: (d.project_name.lower(), d), dists)
    for i, (_, dist) in enumerate(sorted(pack)):
        if i >= stop >= 0:
            break
        res = {}
        key = dist.project_name.lower()
        if key in keys:
            res.update(keys[key])

        names = [dist.key, dist.project_name, dist.key.replace("-", "_"),
                 res.get("mname", None), res.get("name", None)]
        date = ""
        location = None
        for name in names:
            if name is None:
                continue
            ini = os.path.join(dist.location, name, "__init__.py")
            if os.path.exists(ini):
                date = time.ctime(os.path.getctime(ini))
                location = os.path.dirname(ini)
                break
            ini = os.path.join(dist.location, name + ".py")
            if os.path.exists(ini):
                date = time.ctime(os.path.getctime(ini))
                location = ini
                break
        res["installed"] = dist.project_name
        if ini is not None:
            res["location"] = location
            res["installed_date"] = date
        res["installed_version"] = dist.version

        # update?
        if pypi:
            available = get_pypi_version(
                dist.project_name, skip_betas=skip_betas, full_list=True)

            if not available:
                msg = '-'
            elif available[0] != dist.version:
                msg = '!='
            else:
                msg = "=="
            res["available"] = available
            res["pypi"] = available[0]
        else:
            msg = ''
            available = None

        res["diff_pypi"] = msg

        if fLOG:
            pkg_info = '{dist.project_name:30} {dist.version:20}'.format(
                dist=dist)
            key = key if dist.key != dist.project_name else ""
            mes = '{pkg_info} {msg:3} - {date:20} --- {available} - {location}'
            mes = mes.format(pkg_info=pkg_info, msg=msg, date=date, dist=dist,
                             available=available, location=res.get('location', ''))
            fLOG("[pymy] {0}/{1} - {2}".format(i, len(dists), mes))

        all_installed.append(res)
    return all_installed
