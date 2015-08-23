
.. index:: modules

.. _l-ensae_fullset-table:

All modules listed by pymyinstall
=================================

The following code exports the full list of modules
defined in pymyinstall as a table.

.. runpython::
    :showcode:
    :rst:
    
    from pymyinstall.packaged import ensae_fullset
    from pyquickhelper import df2rst
    import pandas
    mod = ensae_fullset()
    mod.sort()
    df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
    df = df[["usage", "rst_link", "kind", "version", "purpose"]]
    df.columns=["usage", "name", "kind", "version", "purpose"]
    print(df2rst(df))




