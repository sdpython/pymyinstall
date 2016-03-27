
.. index:: modules, set

.. _l-name-set-table:

List of available sets of modules
=================================

I defined sets of modules which can be installed by using::

    pymy_install3 --set=<set_name>
    
Or updated if they were installed with::

    pymy_update3 --set=<set_name>
    
The following table described the available sets.
    

.. runpython::
    :showcode:
    :rst:

    from pymyinstall.packaged.packaged_config import name_sets_dataframe
    from pyquickhelper.pandashelper import df2rst
    import pandas
    r = name_sets_dataframe()
    df = pandas.DataFrame(r)
    df = df[["name", "description"]]
    print(df2rst(df))


