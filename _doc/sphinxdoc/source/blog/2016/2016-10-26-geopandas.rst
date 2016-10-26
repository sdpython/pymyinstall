

.. blogpost::
    :title: geopandas
    :keywords: geopandas
    :date: 2016-10-26
    :categories: module

    I was looking for modules able to merge or intersect shapefiles.
    `shapely <https://pypi.python.org/pypi/Shapely>`_ is probably a good place
    to start but I was surprised to discover others modules
    extending shapely in their own way.
    
    * `shapely <https://github.com/Toblerity/Shapely>`_ leverages 
      `GEOS <https://trac.osgeo.org/geos/>`_
    * `pyproj <http://jswhit.github.io/pyproj/>`_ leverages 
      `PROJ.4 <https://github.com/OSGeo/proj.4/wiki>`_ to convert geocoordinates
      into many projections systems (`list <https://trac.osgeo.org/proj/wiki/ProjList>`_)
    * `descartes <https://bitbucket.org/sgillies/descartes/>`_ explicitely extends 
      `shapely <https://github.com/Toblerity/Shapely>`_ 
    * `fiona <https://github.com/Toblerity/Fiona>`_ leverages 
      `GDAL <http://www.gdal.org/>`_
    * `geopandas <http://geopandas.org/index.html#>`_ tries to unify
      all of them