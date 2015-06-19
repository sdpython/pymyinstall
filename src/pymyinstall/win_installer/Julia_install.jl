#
# script to run for the first time
#
# see https://github.com/JuliaLang/IJulia.jl
#

#
# installation for the notebook IKernel
#

Pkg.init()
Pkg.add("IJulia")
Pkg.add("PyCall")
Pkg.add("PyPlot")
Pkg.add("DataFrames")
Pkg.add("BayesNets")
Pkg.add("JuMP")
Pkg.add("Morsel")
Pkg.add("Optim")
Pkg.add("Convex")
Pkg.add("Mocha")
Pkg.add("Gadfly")
Pkg.add("Distributions")
Pkg.add("Docile")
Pkg.add("Clustering")
Pkg.add("Graphs")
Pkg.add("Winston")
