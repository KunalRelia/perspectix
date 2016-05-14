#!/usr/bin/python

import sys

def convertToDate(val):
	year = val[0:4]
	month = val[4:6]
	day = val[6:8]
    	return '%s-%s-%s'%(year,month,day)


for line in sys.stdin:
	
    	line = line.strip()
	values = line.split(",")
	if "WBAN" in values:
		continue
	elif len(values) == 50:
    		pickUpDateTime = values[1]
    		day = convertToDate(pickUpDateTime)
		max = int(values[2])
		print '%s\t%s'%(day,max)
	else:
		continue
