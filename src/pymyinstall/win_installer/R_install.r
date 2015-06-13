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
                    'DiagrammeR',
                    'dplyr',
                    'FactoMineR',
                    'Factoshiny',
                    'fastcluster',
                    'forecast',
                    'ggplot2',
                    'hflights',
                    'magrittr',
                    'R.utils',
                    'Rcurl',
                    'RSQLite',
                    'rvest',
                    'shiny',
                    'SparkR',
                    'stringr',
                    'tidyr',
                    'xml2',
                    'zoo')

