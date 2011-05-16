#!/bin/bash
dir=$(dirname "$0")
[ -n "$dir" ] && cd "$dir"
[ -d data ] || mkdir data
[ -e bfsodl.log ] || echo time count average median minimum maximum variance >bfsodl.log
date=$(date +%s)
./sensors.py >data/$date.dat
stats=$(./stats.py <data/$date.dat)
echo $date $stats >>bfsodl.log
./plot.gp
