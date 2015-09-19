

.. blogpost::
    :title: Install Python 3.4 with packages for a Data Scientist on Linux
    :keywords: install, linux, ubuntu, azure
    :date: 2015-08-30
    :categories: install, modules, linux

    I tested the python installation on Linux from scratch
    (= without Anaconda). I used a distribution 
    `Ubuntu 14.0 <http://releases.ubuntu.com/14.04/>`_
    through `Azure <http://azure.microsoft.com/>`_.
    I did everything from the command line.
    I started by updating `apt-get <http://doc.ubuntu-fr.org/apt-get>`_
    (required for `kivy <http://kivy.org/docs/installation/installation-linux.html>`_)::
    
        sudo add-apt-repository ppa:kivy-team/kivy
        sudo apt-get update
        
    Python 3.4.0 is already installed so I did not need to do that
    but I needed the latest pip::
    
        sudo apt-get install python3-pip --fix-missing
        sudo python3 -m pip install -U pip
        
    Sometimes, pip reverts to its original version. If this happens,
    you can remove its folder and install it again::

        sudo rm -f -r /usr/lib/python3/dist-packages/pip
        sudo apt-get install python3-pip
        sudo pip3 install --upgrade pip    
        
    `GCC <https://en.wikipedia.org/wiki/GNU_Compiler_Collection>`_ was not installed.
    I followed the instructions described at
    `Getting error on Downloading updates <http://askubuntu.com/questions/146362/getting-error-on-downloading-updates>`_::
    
        sudo mv /var/lib/apt/lists{,bakjune4}
        sudo mv /var/cache/apt/archives/partial{,bakjune4}
        sudo apt-get update
        sudo apt-get upgrade
      
    And then gcc::
	
        sudo apt-get install gcc

    This is needed when a package includes C++ code which needs to be compiled.
    That's why some C++ libraries are required::

        sudo apt-get -y install libhdf5-dev libatlas-dev libatlas3gf-base llvm libgeos-dev freeglut3-dev libnetcdf-dev
        sudo apt-get -y install libgmp-dev libgmp3-dev libcpl-dev libmpc-dev
        sudo apt-get -y install binutils libproj-dev gdal-bin libgeoip1 libgdal-dev
        sudo apt-get -y install libmpfr-dev llvm-dev git libopencv-dev libsvm-dev libxml++ curl gmpc-dev libcurlpp-dev

    To get a minimal Gnome installation (takes some time), I don't know if
    it is mandatory::

        sudo apt-get install gdm gnome-core xfonts-base xserver-xorg
                
    Some modules are already available through `apt-get <http://doc.ubuntu-fr.org/apt-get>`_
    (check `Ubuntu packages <http://packages.ubuntu.com/search?suite=default&section=all&arch=any&keywords=python3-f&searchon=names>`_)::
    
        sudo apt-get -y install python3-dev python3-numpy python3-matplotlib python3-scipy python3-pandas python3-zmq python3-lxml python3-pyside 
        sudo apt-get -y install python3-gmpy2 python3-ecdsa python3-pillow python3-h5py python3-six python3-skimage
        sudo apt-get -y install python3-kivy
        sudo apt-get -y install python3-babel python3-bitarray python3-bs4
        sudo apt-get -y install python3-cffi python3-cherrypy3 python3-cloud-sptheme python3-colorama python3-coverage
        sudo apt-get -y install python3-dateutil python3-docutils python3-feedparser
        sudo apt-get -y install python3-flake8 python3-flask python3-gdal python3-geopy python3-gmpy2 python3-html5lib
        sudo apt-get -y install python3-itsdangerous python3-jedi python3-jinja2 python3-kdtree python3-keyring python3-logbook
        sudo apt-get -y install python3-mako python3-marisa python3-markdown python3-mccabe
        sudo apt-get -y install python3-numexpr python3-oauthlib
        sudo apt-get -y install python3-openssl python3-patsy python3-reportlab python3-requests python3-rply
        sudo apt-get -y install python3-shapely python3-simplejson
        sudo apt-get -y install python3-sphinx python3-sql python3-sqlparse python3-stemmer python3-tk python3-tornado python3-tz
        sudo apt-get -y install python3-urllib3 python3-xlib python3-yaml
        
    Not the latest packages are available so they might be installed and compiled again.  
    It should get some others C++ dependencies and save some time later.
    Then, I installed this module::
        
        sudo pip install pymyinstall

    Or, if it was already installed::
    
        sudo pip install pymyinstall --upgrade
        
    To complete the installation::

        sudo -H pymy_install3
        
    It is quite long. Finally, I tried to update packages to the latest::
    
        sudo -H pymy_update
        
    Some packages were removed (see below)::
    
        sudo -H pymy_install3 --skip=rpy2,dynd,pygame,python-igraph,basemap,autopy3,llvmpy,llvmlite,liblinear,mlpy,pygit2,xgboost,psycopg2,pymssql,mysqlclient,django-audiotracks,opencv_python,PyAudio,la,NLopt,pycuda,pymvpa2,pyodbc,pypmc,PyX,libsvm,JSAnimation,heatmap,cgal_bindings,skdata
        
    Finally, to update the installed modules::
    
        sudo -H pymy_update
        
    This command fails for a couple of libraries installed using ``apt-get python3-``. 
    Some dependencies are still missing from the list mentioned above.
    
    Issues during installation (skipped packages)::
        
        * rpy2: R needs to be installed first::
        
            sudo apt-get install r-base
          
          But the installation of *rpy2* still failed due to 
          a too old version of R (3.0.2) and python 3 version of these
          packages are not available through *apt-get*.
          
        * dynd: anaconda package, ``pip install dynd`` did not work
        * llvmpy: compilation error
        * llvmlite: compilation error
        * numba: depends on llvmlite
        * pygame: not available with pip install
        * kivy-garden: bug with pymy_install3, manual install: ``sudo pip3.4 install kivy-garden``
        * python-igraph: link error
        * autopy3: missing dependency (X11)
        * liblinear: compilation error
        * mlpy: compilation error
        * pygit2: compilation error
        * pyscopg2: compilation error
        * xgboost, la: setup.py does not compile on Python 3
        * pymssql, myslqclient: no SQL server installed
        * django-audiotracks
        * opencv_python: will investigate later
        * la:
        * PyAudio: ...
        * pypmc: ...
        * PyX: ...
        * libsvm: ...
        * NLopt: ...
        * pycuda: ...
        * pymvpa2: ...
        * pyodbc: ...
        * pypmc: ...
        * PyX: ...
        * JSAnimation: ...
        * heatmap: ...
        * cgal_bindings: ...
        * skdata: needs to download the source
        
    Finally, some tools (requires more than 1 Gb)::
    
        sudo apt-get install pandoc i7z i7z-gui scite java-common sqlitebrowser latex-cjk-all texlive-latex-base texlive-latex-recommended texlive-latex-extra mono-complete
        
    To get numpy and scipy depedencies, the following command is enough::
    
        sudo apt-get build-dep python3-numpy python3-scipy
    
        
