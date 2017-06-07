
.. blogpost::
    :title: Package update and new bugs
    :keywords: matplotlib, numpy
    :date: 2017-06-07
    :categories: bug

    The latest version of numpy 1.13.rc2 makes matplotlib fail
    in one particular place:

    ::

           lib\site-packages\matplotlib\lines.py in set_markerfacecolor(self, fc)
           1204         if fc is None:
           1205             fc = 'auto'
        -> 1206         if self._markerfacecolor != fc:
           1207             self.stale = True
           1208         self._markerfacecolor = fc

    With the following error:

    ::

        ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
