#!/usr/bin/python

import sys
import operator
import os

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    	day, val = line.strip().split("\t", 1)
    
    	try:
        	max = int(val)
    	except ValueError:
   		continue

	sys.stdout.write('{"index" : {"_index" : "weather" , "_type" : "dayMax" } }\n')
        s ="{"
        s = s +'"day" : "%s" '%(day)
        s = s+ " , "
	s = s +'"max" : "%d" '%(max)
        s = s+"}"
        sys.stdout.write('%s'%(s))
	print("\n")
