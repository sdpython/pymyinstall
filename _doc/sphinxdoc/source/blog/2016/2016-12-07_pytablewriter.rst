
.. blogpost::
    :title: pytablewriter
    :keywords: pandas, dataframe, pytablewriter
    :date: 2016-12-07
    :categories: module

    `pytablewriter <http://pytablewriter.readthedocs.io/en/latest/index.html>`_
    which converts a dataframe into many formats.

    ::

        import pytablewriter
        writer = pytablewriter.JavaScriptTableWriter()
        writer.set_dataframe(df)
        writer.table_name = "a kind of title"
        writer.write_table()  # returns a string

    The excel example is interesting:
    `Write a table to Excel sheet <http://pytablewriter.readthedocs.io/en/latest/pages/examples/excel.html#write-tables-to-excel-sheets>`_.
