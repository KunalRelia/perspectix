#!/usr/bin/python

import sys
import operator
import os

currentDay = None
currentDaySum = 0
cnt = {}
result={}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    day, val = line.strip().split("\t", 1)
    
    try:
        count = int(val)
    except ValueError:
   	continue

    if day == currentDay:
	currentDaySum += count
    else:
        if currentDay:
	     	key = "%s" %(currentDay)
	     	cnt[key] = currentDaySum
	     	sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "daytrips" } }\n')
        	s ="{"
                s = s +'"pickupday" : "%s" '%(key)
                s = s+ " , "
		s = s +'"count" : "%s" '%(cnt[key])
        	s = s+"}"
        	sys.stdout.write('%s'%(s))
       	 	print("\n")

	currentDay = day
	currentDaySum = count
key = "%s" %(currentDay)
cnt[key] = currentDaySum
sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "daytrips"  } }\n')
s ="{"
s = s +'"pickupday" : "%s" '%(key)
s = s+ " , "
s = s +'"count" : "%s" '%(cnt[key])
s = s+"}"
sys.stdout.write('%s'%(s))
print("\n")
