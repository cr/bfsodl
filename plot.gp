#!/usr/bin/gnuplot

set title "Gamma background radiation in Germany\n(source http://odlinfo.bfs.de/)" font "/usr/share/fonts/truetype/ttf-liberation/LiberationSans-Regular.ttf,16"

# x-Achse ist Zeit in Epoch
set xdata time
set timefmt "%s"
set format x "%Y-%m-%d"

#set xlabel 'Date'
set ylabel 'Dose equivalent / µSv/h'

set xtics nomirror rotate by -45

set auto x
#set xrange ["2008-04-01":"2008-04-30"]

set ytics 0.01
set xtics 604800
set grid ytics

set output "plot.png"
set term png 10 size 1000,600

#time count average median minimum maximum variance

set key out vert right
set style data linespoints
plot for [i=3:6] "bfsodl.log" using 1:i title columnheader(i)

