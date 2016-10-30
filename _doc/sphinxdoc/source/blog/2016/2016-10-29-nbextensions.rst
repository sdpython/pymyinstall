

.. blogpost::
    :title: Jupyter Notebook Extensions
    :keywords: notebook, jupyter, extensions
    :date: 2016-10-29
    :categories: module

    The notebook extensions seemed to have achieved stability
    in `jupyter_contrib_nbextensions <https://github.com/ipython-contrib/jupyter_contrib_nbextensions>`_.
    To install it, just do:
    
    ::
    
        pip install jupyter_contrib_nbextensions
        jupyter contrib nbextension install --user
        
    The    
    `list of extensions <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions>`_
    is growing and the documentation is available at
    `jupyter-contrib-nbextensions.readthedocs.io <http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/>`_.    
    Here is a short list:
    
    * `code_prettify <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/code_prettify>`_:
      shorten long lines, use `yapf <https://github.com/google/yapf>`_
    * `execute_time <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/execute_time>`_:
      displays execution time below each cell
    * `exercise2 <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/exercise2>`_:
      hide / show solution to exercise 
    * `highlighter <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/highlighter>`_:
      highligh text which comes with magic cells
    * `move_selected_cells <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/move_selected_cells>`_:
      to move several cells in one move
    * `scratchpad <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/scratchpad>`_:
      Open a separate Windows where you can try some code without modifying the original notebook (type CTRL + B)
    * `toc2 <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/toc2>`_:
      add a table of contents as a side bar, could be difficult to make it work
    * `skip-traceback <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/skip-traceback>`_:
      skip the trace back, only show the last error
    * `tree-filter <https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/tree-filter>`_:
      if you have many notebook, helps filtering them out
    
    Some tricks with notebooks: ``Shift-J`` and ``Shift-K`` selects cells. To enable / disable an extension:
    
    ::
    
        jupyter nbextension enable <nbextension>
        
    Example:
    
    ::
    
        jupyter nbextension enable codefolding/main
        
    So for the proposed short list:
    
    ::
    
        jupyter nbextension enable code_prettify/code_prettify
        jupyter nbextension enable execute_time/ExecuteTime
        jupyter nbextension enable exercise2/main
        jupyter nbextension enable highlighter/highlighter
        jupyter nbextension enable move_selected_cells/main
        jupyter nbextension enable scratchpad/main
        jupyter nbextension enable toc2/toc2
        jupyter nbextension enable tree-filter/index
        
    ::
    
        jupyter nbextension enable skip-traceback/main
        jupyter nbextension enable codefolding/main
    
    