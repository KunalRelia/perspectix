#!/usr/bin/python

import sys

def convertToDate(val):
    return val.strip().split(' ')[0]

for line in sys.stdin:
    	line = line.strip()
	key,columns = line.split("\t",1)

	keys = key.split(',')
	pickUpDateTime = keys[3]
    	columns = columns.split(',')
    	pickupLong = columns[6]
	pickupLat = columns[7]
    	day = convertToDate(pickUpDateTime)
	highest = "2013-02-23"
	if day == highest:
		print '%s,%s'%(pickupLong,pickupLat)
