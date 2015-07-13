#
# script to run for the first time
#
# see https://github.com/IRkernel/IRkernel
#

#
# specify a location by default
#

cat(".Rprofile: Setting UK repositoryn")
r = getOption("repos")
r["CRAN"] = "http://cran.uk.r-project.org"
options(repos = r)
rm(r)

#
# installation for the notebook IKernel
#

install.packages(c('devtools'))
install.packages(c('rzmq','repr','IRkernel','IRdisplay'),
                 repos = c('http://irkernel.github.io/', getOption('repos')))
IRkernel::installspec(user=F)

#
# installation of others packages
#

install.packages(c('actuar',
                    'ADGofTest',
                    'AUC',
                    'clusterGeneration',
                    'caret',
                    'corrplot',
                    'dendroextras',
                    'DiagrammeR',
                    'dplyr',
                    'FactoMineR',
                    'Factoshiny',
                    'fastcluster',
                    'forecast',
                    'gdata',
                    'ggmaps',
                    'ggplot2',
                    'hflights',
                    'HistData',
                    'igraph',
                    'ineq',
                    'KernSmooth',
                    'magrittr',
                    'maps',
                    'maptools',
                    'mgcv',
                    'nnet',
                    'mnormt',
                    'normtest',
                    'quantreg',
                    'R.utils',
                    'Rcurl',
                    'rpart',
                    'RSQLite',
                    'rattle',
                    'rgdal',
                    'rvest',
                    'shiny',
                    'SparkR',
                    'spatstat',
                    'sna',
                    'sp',
                    'stringr',
                    'tidyr',
                    'tm',
                    'twitteR',
                    'xml2',
                    'xlsx',
                    'xts',
                    'wordcloud',
                    'YieldCurve',
                    'zoo'))

