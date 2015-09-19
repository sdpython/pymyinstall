
.. index:: modules

.. _l-ensae_fullset-table:

All modules listed by pymyinstall
=================================

The following code exports the full list of modules
defined in pymyinstall as a table.

.. runpython::
    :showcode:
    :rst:
    
    from pymyinstall.packaged import all_set, classifiers2string
    from pyquickhelper import df2rst
    import pandas
    mod = all_set()
    mod.sort()
    df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
    df = df[["usage", "rst_link", "kind", "version", "license", "purpose", "classifier"]]
    df["classifier"] = df.apply(lambda row: classifiers2string(row["classifier"]), axis=1)
    df.columns=["usage", "name", "kind", "version", "license", "purpose", "classifier"]
    print(df2rst(df))




