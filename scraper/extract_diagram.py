#!/usr/bin/env python

import sys
import Image
import time

def find_xtics( i, startdate ):

  ticdate_t = time.strptime( startdate + " 20:00:00", "%Y-%m-%d %H:%M:%S" )
  ticdate = time.mktime( ticdate_t )

  xtics = []
  y = 440
  for x in range( 70, 750 ):
    pixel = i.getpixel( ( x, y ) )
    if pixel == ( 90, 90, 90, 255 ):
      xtics.append( ( int( ticdate ), x) )
      ticdate += 60*60*24
  return xtics

def find_graph( i, x ):

  #find all blue pixels
  blue = []
  for y in range( 440, 44, -1 ):
    pixel = i.getpixel( ( x, y ) )
    if pixel == ( 0, 0, 255, 255 ):
      blue.append( y )

  #throw away first and last to eliminate outlier
  blue.pop()
  blue.pop(0)

  #return average
  return sum( blue ) / len( blue )

def value( x ):
  A = (84, 0.270)
  B = (396, 0.030)
  m = ( B[1] - A[1] ) / ( B[0] - A[0] )
  y0 = A[1] - m * A[0]
  return ( m*x+y0 )


if len( sys.argv ) >= 3:
  startdate = sys.argv[2]
else:
  startdate = "2011-02-15"

img = Image.open( sys.argv[1] ).convert( 'RGBA' )

xtics = find_xtics( img, startdate )

graph = []
for (time, x) in xtics:
  graph.append( ( time, value( find_graph( img, x ) ) ) )

for ( time, value ) in graph:
  print time, value

