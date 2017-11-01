"""
@file
@brief Some fixes for deprecated functions and not updated packages.
"""


def fix_scipy10_for_statsmodels08():
    """
    :epkg:`scipy` deprecated some functions
    still used by :epkg:`statsmodels` 0.8.
    See `deprecated features <https://scipy.github.io/devdocs/release.1.0.0.html#deprecated-features>`_
    and pull request `3942 <https://github.com/statsmodels/statsmodels/pull/3942/files>`_
    in :epkg:`statsmodels`.
    """
    import scipy.stats
    if not hasattr(scipy.stats, "chisqprob"):
        import scipy.stats.distributions
        setattr(scipy.stats, "chisqprob", scipy.stats.distributions.chi2.sf)


if __name__ == "__main__":
    fix_scipy10_for_statsmodels08()
