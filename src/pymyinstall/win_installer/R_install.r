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
                    'biglm',
                    'clusterGeneration',
                    'caret',
                    'corrplot',
                    'dendroextras',
                    'DiagrammeR',
                    'data.table',
                    'distr',
                    'distrEx',
                    'dplyr',
                    'e1071',
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
                    'LaF',
                    'magrittr',
                    'maps',
                    'maptools',
                    'microbenchmark',
                    'mgcv',
                    'mnormt',
                    'memoise',
                    'neuralnet',
                    'nnet',
                    'normtest',
                    'parallel',
                    'pROC',
                    'pryr',
                    'quantreg',
                    'R.utils',
                    'Rcpp',
                    'Rcurl',
                    'rgl',
                    'rpart',
                    'rPython',
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
                    'tcltk',
                    'tm',
                    'twitteR',                    
                    'VGAM',
                    'XML',
                    'xml2',
                    'xlsx',
                    'xts',
                    'wordcloud',
                    'YieldCurve',
                    'zoo'))

