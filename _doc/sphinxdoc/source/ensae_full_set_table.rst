
.. index:: modules

.. _l-ensae_fullset-table:

All modules listed by pymyinstall
=================================

The following code exports the full list of modules
defined in pymyinstall as a table.

.. runpython::
    :showcode:
    :rst:

    from pymyinstall.packaged import all_set
    from pyquickhelper.pandashelper import df2rst
    import pandas
    mod = all_set()
    mod.sort()
    df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
    df = df[["rst_link", "usage", "kind", "version", "license", "purpose"]]
    df.columns=["usage", "name", "kind", "version", "license", "purpose"]
    df = df.sort_values("name")
    print(df2rst(df))
