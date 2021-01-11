
.. blogpost::
    :title: AttributeError: module 'nbconvert.exporters' has no attribute 'WebPDFExporter'
    :keywords: python, nbconvert, jupyter
    :date: 2021-01-11
    :categories: installation

    I faced the following issue when running a notebook
    server juste the installation.

    ::

        AttributeError: module 'nbconvert.exporters' has no attribute 'WebPDFExporter'

    That leaded to an empty screen showing `"500: internal error"`
    returned by the server. I could not find a solution
    despite many searches on the internet so I decided to modify
    the code of `notebook` in file `notebook/handler.py
    <https://github.com/jupyter/notebook/blob/master/
    notebook/notebook/handlers.py#L41>`_ and update with the
    following lines:

    ::

        try:
            exporter_class = get_exporter(name)
        except AttributeError:
            continue

    I hope this issue if fixed next time I install it.
    I remember facing the same one quite a while
    but I have no memory on how I got it fixed.
