#!/usr/bin/python

import sys
import operator
import os


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    	lat,long = line.strip().split(",")
    

	sys.stdout.write('{"index" : {"_index" : "maps" , "_type" : "dropoff" } }\n')
        s ='{ "type" : "Feature" , "geometry" : { "type" : "Point" , '
        s = s +'"coordinates" : [%s,%s] }, '%(long,lat)
        s = s+ ' "properties" : { "name" : "DropOff" } }  '
        sys.stdout.write('%s'%(s))
       	print("\n")
