"""
@file
@brief Caching functions
"""


def install_memoize(f):
    """
    cache a downloaded page
    """
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def install_memoize2(f):
    """
    cache a downloaded page
    """
    memo = {}

    def helper(x, is406=False):
        if x not in memo:
            memo[x] = f(x, is406)
        return memo[x]
    return helper
