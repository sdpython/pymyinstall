"""
@file
@brief Helpers for pip.

.. versionadded:: 1.5
"""
try:
    from pip._internal.utils.compat import stdlib_pkgs
except ImportError:
    stdlib_pkgs = None


class Distribution:
    """
    Common interface for old and recent pip packages.

    .. versionadded:: 1.5
    """

    def __init__(self, dist):
        self.dist = dist

    def __getattr__(self, attr):
        if attr == 'key':
            if hasattr(self.__dict__['dist'], 'key'):
                return self.__dict__['dist'].key
            return self.__dict__['dist'].canonical_name
        if attr == 'dist':
            return self.__dict__['dist']
        if attr in {'_get_metadata', 'requires', 'PKG_INFO', 'project_name'}:
            if hasattr(self.__dict__['dist'], attr):
                return getattr(self.__dict__['dist'], attr)
            return getattr(self.__dict__['dist']._dist, attr)
        return getattr(self.__dict__['dist'], attr)


def get_installed_distributions(local_only=True, skip=stdlib_pkgs,
                                include_editables=True, editables_only=False,
                                user_only=False, use_cmd=False):
    """
    Directs call to function *get_installed_distributions* from :epkg:`pip`.

    Return a list of installed Distribution objects.

    :param local_only: if True (default), only return installations
        local to the current virtualenv, if in a virtualenv.
    :param skip: argument is an iterable of lower-case project names to
        ignore; defaults to ``pip.compat.stdlib_pkgs`` (if *skip* is None)
    :param editables: if False, don't report editables.
    :param editables_only: if True , only report editables.
    :param user_only: if True , only report installations in the user
        site directory.
    :param use_cmd: if True, use a different process (updated package list)
    :return: list of installed Distribution objects.

    .. versionadded:: 1.5
    """
    if use_cmd:
        raise NotImplementedError("use_cmd should be False")
    try:
        from pip._internal.metadata import get_default_environment
        return list(map(Distribution,
                        get_default_environment().iter_installed_distributions(
                            local_only=local_only, skip=skip,
                            include_editables=include_editables,
                            editables_only=editables_only,
                            user_only=user_only)))

    except ImportError:
        from pip._internal.utils.misc import get_installed_distributions as getd
        return list(map(Distribution, getd(
            local_only=local_only, skip=skip,
            include_editables=include_editables,
            editables_only=editables_only,
            user_only=user_only, use_cmd=use_cmd)))
