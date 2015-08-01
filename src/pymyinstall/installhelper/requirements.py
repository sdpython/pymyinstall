"""
@file
@brief helpers around requirements
"""


def build_requirements(module_list):
    """
    builds a requirements list based on a list of @see cl ModuleInstall

    @param      module_list     list of @see cl ModuleInstall
    @return                     string
    """
    res = []
    for mod in module_list:
        if mod.version is not None:
            res.append("{0}=={1}".format(mod.name, mod.version))
        else:
            res.append(mod.name)
    return "\n".join(res)
