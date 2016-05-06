#!/usr/bin/python

import sys

def convertToDate(val):
    return val.strip().split(' ')[0]

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    
    key,columns = line.split('\t',1)
    keys = key.split(',')
    medallion = keys[0]
    pickUpDateTime = keys[3]
    day = convertToDate(pickUpDateTime)
               
	
    print '%s\t%s' % (day,1)
