#!/usr/bin/python

import sys
import operator
import os

currentDay = None
currDict = {}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    day, values = line.strip().split("\t", 1)
    
    try:
	key,val = values.split(',')
        val = int(val)
    except ValueError:
   	continue

    if day == currentDay:
	if key == "CSH" or key == "CRD":
		if key in currentDict:
			currentDict[key] += val
		else:
			currentDict[key] = val
	else:
		if "Others" in currentDict:
                        currentDict["Others"] += val
                else:
                        currentDict["Others"] = val
    else:
        if currentDay:
		sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "dayPaymentType" } }\n')
		sum = 0
		for key,value in currentDict.iteritems():
                        sum += int(value)
		s ='{ "day" : "%s" '%(currentDay)
		for key,value in currentDict.iteritems():
			percent = value*100/float(sum)
			s = s+ ","
                	s = s +'"%s" : "%.2f" '%(key,percent)
        	s = s+"}"
        	sys.stdout.write('%s'%(s))
       	 	print("\n")

	currentDay = day
	currentDict = {}
	if key == "CSH" or key == "CRD":
		currentDict[key] = val
	else:
		currentDict["Others"] = val

sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "dayPaymentType" } }\n')

sum = 0
for key,value in currentDict.iteritems():
	sum += int(value)

s ='{ "day" : "%s" '%(currentDay)
for key,value in currentDict.iteritems():
	percent = float((value/sum)*100)
        s = s+ ","
        s = s +'"%s" : "%.2f" '%(key,percent)
s = s+"}"
sys.stdout.write('%s'%(s))
print("\n")

