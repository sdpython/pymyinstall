
.. blogpost::
    :title: pyecharts + echarts
    :keywords: pyecharts
    :date: 2018-07-05
    :categories: module

    `pyecharts <https://github.com/pyecharts/pyecharts>`_ is a wrapper
    around `echarts <https://ecomfe.github.io/>`_,
    a library developped by
    `Baidu <https://www.baidu.com/>`_.
    Most of the documentation is in Chinese so it handles
    every language.
    Check the `gallery <https://ecomfe.github.io/echarts-examples/public/index.html#chart-type-graph>`_,
    it is quite impressive. One example about is graph shows relationships
    in `Les Miserables <https://ecomfe.github.io/echarts-examples/public/editor.html?c=graph>`_.
    The Python wrapper used som technics such as modules
    to automatically converts python code
    into javascript: `javascripthon <https://github.com/metapensiero/metapensiero.pj>`_.
    I recommend reading the associated paper
    `ECharts: A declarative framework for rapid construction of web-based visualizatio <https://www.sciencedirect.com/science/article/pii/S2468502X18300068>`_
    which mentions many existing libraries and explain their technical choice
    like not using SVG to increase performance
    (so no depndency on `d3.js <https://d3js.org/>`_).
