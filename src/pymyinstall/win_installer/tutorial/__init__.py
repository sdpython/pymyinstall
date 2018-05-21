"""
@file
@brief Shortcuts to tutorial
"""
import os


def copy_tutorial(name, destination):
    """
    copy files and scripts for a specific tutorial

    @param      name            tutorial name or folder
    @param      destination     destination
    @return                     list of operations done by the function list of 3-uple: action, source_file, dest_file

    The function will create a sub folder in *destination*
    using *name* or the last folder name in *name*.

    This function requires modules
    `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/>`_.
    """
    from pyquickhelper.filehelper import synchronize_folder
    if os.path.exists(name):
        dest = os.path.join(destination, name)
    else:
        this = os.path.abspath(os.path.dirname(__file__))
        fold = os.path.join(this, name)
        if not os.path.exists(fold):
            raise FileNotFoundError(
                "unable to find tutorial {0}\n{1} not here".format(name, fold))
        spl = os.path.split(fold)
        dest = os.path.join(destination, spl[-1])

    if not os.path.exists(dest):
        os.mkdir(dest)

    return synchronize_folder(fold, dest)
