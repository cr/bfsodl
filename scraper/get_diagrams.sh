#!/bin/bash

[ -d diagrams ] || mkdir diagrams
cd diagrams
while read nr
do
  if [ ! -e $nr.gif ]
  then
    wget http://odlinfo.bfs.de/messwerte/$nr.gif
    #sleep 2
  fi
done

