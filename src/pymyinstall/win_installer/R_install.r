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
                    'bigglm',
                    'clusterGeneration',
                    'caret',
                    'corrplot',
                    'dendroextras',
                    'DiagrammeR',
                    'data.table',
                    'distr',
                    'distrEx',
                    'doSNOW',
                    'doParallel',
                    'dplyr',
                    'e1071',
                    'FactoMineR',
                    'Factoshiny',
                    'fastcluster',
                    'ff',
                    'ffbase',
                    'foreach',
                    'forecast',
                    'ggmaps',
                    'ggplot2',
                    'graph',
                    'hflights',
                    'HistData',
                    'igraph',
                    'ineq',
                    'KernSmooth',
                    'LaF',
                    'lubridate',
                    'magrittr',
                    'maps',
                    'maptools',
                    'MASS',
                    'microbenchmark',
                    'mgcv',
                    'mnormt',
                    'memoise',
                    'multicore',
                    'network',
                    'neuralnet',
                    'nnet',
                    'normtest',
                    'nws',
                    'parallel',
                    'plyr',
                    'pmml',
                    'pROC',
                    'pryr',
                    'qcc',
                    'quantreg',
                    'R.utils',
                    'randomForest',
                    'rattle',
                    'Rcmdr',
                    'Rcpp',
                    'Rcurl',
                    'rgl',
                    'rmarkdown',
                    'RMongo',
                    'RMySQL',
                    'rpart',
                    'RODBC',
                    'RPostgreSQL',
                    'rPython',
                    'RSQLite',
                    'reshape2',
                    'rgdal',
                    'rmpi',
                    'rvest',
                    'shiny',
                    'sna',
                    'snow',
                    'SOAR',
                    'som',
                    'sp',
                    'spatstat',
                    'speedglm',
                    'sqldf',
                    'stringr',
                    'tidyr',
                    'tcltk',
                    'tm',
                    'VGAM',
                    'xgboost',
                    'XML',
                    'xml2',
                    'xlsx',
                    'xts',
                    'wordcloud',
                    'YieldCurve',
                    'zoo'))

#
# big memory
# http://www.thecoatlessprofessor.com/programming/installing-the-bigmemory-package-and-biglm-on-windows-os-x-or-linux/
# https://r-forge.r-project.org/R/?group_id=556
#
# Install Bigmemory packages from r-forge page
#
# This part is commented out because rpy2 requires 3.2.x and bigmemory binaries are only available
# for R 3.1.3 (2015/09/18).
 

# install.packages("bigmemory", repos="http://R-Forge.R-project.org")

# install.packages("bigmemory.sri", repos="http://R-Forge.R-project.org")
# install.packages("biganalytics", repos="http://R-Forge.R-project.org")
# install.packages("bigalgebra", repos="http://R-Forge.R-project.org")
# install.packages("bigkmeans", repos="http://R-Forge.R-project.org")
# install.packages("bigrf", repos="http://R-Forge.R-project.org")
# install.packages("bigtabulate", repos="http://R-Forge.R-project.org")

# Install Boost Header and biglm package from CRAN

# install.packages(c("BH","biglm"))
