#!/usr/bin/python

import sys

currentDay = None
currentDaySum = 0
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
	     print "%s\t%s" %(currentDay,currentDaySum)
	currentDay = day
	currentDaySum = count
print "%s\t%s" %(currentDay,currentDaySum)
