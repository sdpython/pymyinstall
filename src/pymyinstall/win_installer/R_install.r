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
                    'clusterGeneration',
                    'caret',
                    'corrplot',
                    'DiagrammeR',
                    'dplyr',
                    'FactoMineR',
                    'Factoshiny',
                    'fastcluster',
                    'forecast',
                    'ggplot2',
                    'hflights',
                    'igraph',
                    'magrittr',
                    'mnormt',
                    'R.utils',
                    'Rcurl',
                    'rpart',
                    'RSQLite',
                    'rvest',
                    'shiny',
                    'SparkR',
                    'sna',
                    'stringr',
                    'tidyr',
                    'tm',
                    'twitteR',
                    'xml2',
                    'wordcloud',
                    'zoo'))

