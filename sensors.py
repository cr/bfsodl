#!/usr/bin/env python

import urllib
import HTMLParser

class HTMLTables( HTMLParser.HTMLParser ):
    '''Extract tables from HTML'''
 
    def __init__( self, *args, **kwargs ):
        HTMLParser.HTMLParser.__init__( self )
        self.state = 'IDLE'
        self.tables = []
        self.table = []
	self.tr = []

    def handle_starttag( self, tag, attr ):
        if tag.lower() == 'table':
            self.state = 'TABLE'
            self.table = []
        if tag.lower() == 'tr':
            self.state = 'TR'
            self.tr = []
        if tag.lower() == 'td':
            self.state = 'TD'
 
    def handle_endtag( self, tag ):
        if tag.lower() == 'td':
	    self.state = 'TR'
        if tag.lower() == 'tr':
	    self.state = 'TABLE'
            self.table.append( self.tr )
        if tag.lower() == 'table':
	    self.state = 'IDLE'
            self.tables.append( self.table )

    def handle_data( self, data ):
	if self.state == 'TD':
            self.tr.append( data )

    def tables():
        self.tables

pages = (
  'http://odlinfo.bfs.de/01.php',
  'http://odlinfo.bfs.de/02.php',
  'http://odlinfo.bfs.de/03.php',
  'http://odlinfo.bfs.de/04.php',
  'http://odlinfo.bfs.de/05.php',
  'http://odlinfo.bfs.de/06.php',
  'http://odlinfo.bfs.de/07.php',
  'http://odlinfo.bfs.de/08.php',
  'http://odlinfo.bfs.de/09.php',
  'http://odlinfo.bfs.de/10.php',
  'http://odlinfo.bfs.de/11.php',
  'http://odlinfo.bfs.de/12.php',
  'http://odlinfo.bfs.de/13.php',
  'http://odlinfo.bfs.de/14.php',
  'http://odlinfo.bfs.de/15.php',
  'http://odlinfo.bfs.de/16.php'
)

data = []
for url in pages:
  p = HTMLTables()
  p.feed( urllib.urlopen( url ).read() )
  table = p.tables[4]
  p.close()

  for row in table:
    if row[-1] == 'betriebsbereit':
      try:
        value = float( row[-2] )
      except ValueError:
        pass
      else:
        data.append( ( row[1][1:-1], value ) )

for ( id, value ) in data:
  print id, value
