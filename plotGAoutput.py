# This function can be used to display the results of a GA run saved in
# GAoutput.txt. It requires Gnuplot and the Python Gnuplot library, available
# from www.gnuplot.info and gnuplot-py.sourceforge.net, respectively.

import Gnuplot

g = None

def plotGAoutput(filename="GAoutput.txt"):
    global g
    f = open(filename)
    g = Gnuplot.Gnuplot()
    g("set style data lines")
    g("set xlabel 'generation'")
    g("set ylabel 'fitness'")
    command = "plot [0:][-100:500] "
    command += "'%s' using 1:2 title 'average fitness'" % filename
    command += ", '%s' using 1:3 title 'best fitness'" % filename
    g(command)

