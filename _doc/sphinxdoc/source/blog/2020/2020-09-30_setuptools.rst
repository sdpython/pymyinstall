
.. blogpost::
    :title: Issue with setuptools and pip
    :keywords: pip, setuptools
    :date: 2020-09-30
    :categories: automation

    I got the following error which I resolved by
    updating `setuptools <https://setuptools.readthedocs.io/en/latest/>`_.
    But quite a difficult error message to interpret.

    ::

        File "python3.7/site-packages/pip/_vendor/pep517/wrappers.py", line 265, in _call_hook
            raise BackendUnavailable(data.get('traceback', ''))
        pip._vendor.pep517.wrappers.BackendUnavailable: Traceback (most recent call last):
          File "python3.7/site-packages/pip/_vendor/pep517/_in_process.py", line 86, in _build_backend
            obj = import_module(mod_path)
          File "python3.7/importlib/__init__.py", line 127, in import_module
            return _bootstrap._gcd_import(name[level:], package, level)
          File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
          File "<frozen importlib._bootstrap>", line 983, in _find_and_load
          File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
          File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
          File "<frozen importlib._bootstrap>", line 983, in _find_and_load
          File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
          File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
          File "<frozen importlib._bootstrap_external>", line 728, in exec_module
          File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
          File "python3.7/site-packages/setuptools/__init__.py", line 5, in <module>
            import distutils.core
          File "python3.7/site-packages/_distutils_hack/__init__.py", line 83, in create_module
            return importlib.import_module('setuptools._distutils')
          File "python3.7/importlib/__init__.py", line 127, in import_module
            return _bootstrap._gcd_import(name[level:], package, level)
        ModuleNotFoundError: No module named 'setuptools._distutils'
