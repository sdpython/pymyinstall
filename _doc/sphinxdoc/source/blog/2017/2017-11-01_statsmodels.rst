
.. blogpost::
    :title: Issue with scipy 1.0 and statsmodels 0.8
    :keywords: scipy, statsmodels
    :date: 2017-11-01
    :categories: module

    It is difficult to fix a package when there is no
    error but silent warnings. :epkg:`statsmodels` fails
    with :epkg:`scipy` 1.0 because some deprecated functions
    were removed: `chisqprob <https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.stats.chisqprob.html>`_.
    I sometimes look into warnings but many packages do not fix them and
    this is quite difficult to notice yours in that long list.
    I created a function which fixes it. The documentation
    contains more information about it.

    .. runpython::
        :showcode:
        :rst:

        from textwrap import dedent
        from pymyinstall.fix import fix_scipy10_for_statsmodels08
        print(dedent(fix_scipy10_for_statsmodels08.__doc__))
