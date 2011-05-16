#!/usr/bin/env python

import sys
from numpy import *

lines=[]
for line in sys.stdin:
  ( id, value ) = line.split( ' ' )
  lines.append( float( value ) )

data = array( lines )
#time count average median minimum maximum variance
print len( data ), data.mean(), median( data ), data.min(), data.max(), data.var()

