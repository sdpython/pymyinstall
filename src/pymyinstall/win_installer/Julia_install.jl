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