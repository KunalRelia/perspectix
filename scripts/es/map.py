#!/usr/bin/python

import sys
mapid = 1
for line in sys.stdin:
    	line = line.strip()
	key = line.replace("\t",",")
	print '%s\t%s' % (mapid,key)
	mapid = mapid+1
