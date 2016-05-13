#!/usr/bin/python

import sys

def convertToDate(val):
    return val.strip().split(' ')[0]

for line in sys.stdin:
    	line = line.strip()
	key,values = line.split("\t",1)

    	keys = key.split(',')
	value = values.split(',')
    	pickUpDateTime = keys[3]
    	day = convertToDate(pickUpDateTime)
	type = value[10]
	print '%s\t%s,%s'%(day,type,1)
