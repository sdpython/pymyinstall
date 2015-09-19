
.. index:: modules

.. _l-name-set-table:

List of available sets of modules
=================================


.. runpython::
    :showcode:
    :rst:

    from pymyinstall.packaged.packaged_config import name_sets_dataframe
    from pyquickhelper import df2rst
    import pandas
    r = name_sets_dataframe()
    df = pandas.DataFrame(r)
    df = df[["name", "description"]]
    print(df2rst(df))


