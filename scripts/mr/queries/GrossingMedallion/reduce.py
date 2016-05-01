#!/usr/bin/python

import sys

currentMedallion = None
currentTotalAmount=0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    key, totalAmount = line.strip().split("\t", 1)
    
    try:
        count = float(totalAmount)
    except ValueError:
   	continue

    if key == currentMedallion:
	currentTotalAmount += count
    else:
        if currentMedallion:
	     print "%s\t%0.2f" %(currentMedallion,currentTotalAmount)
        currentMedallion = key
	currentTotalAmount = count
print "%s\t%0.2f" %(currentMedallion,currentTotalAmount)
