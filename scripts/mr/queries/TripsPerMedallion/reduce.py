#!/usr/bin/python

import sys

currentMedallion = None
currentTotalSum=0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    medallion, val = line.strip().split("\t", 1)
    
    try:
        count = int(val)
    except ValueError:
   	continue

    if medallion == currentMedallion:
	currentTotalSum += count
    else:
        if currentMedallion:
	     print "%s\t%s" %(currentMedallion,currentTotalSum)
        currentMedallion = medallion
	currentTotalSum = count
print "%s\t%s" %(currentMedallion,currentTotalSum)
