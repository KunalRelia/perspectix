#!/usr/bin/python

import sys

def convertToDate(val):
    return val.strip().split(' ')[0]

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    
    key,value = line.split('\t',1)
    keys = key.split(',')
    medallion = keys[0]
    pickupDay = convertToDate(keys[3])
    columns = value.split(",")
    totalAmount = float(columns[-1])
    print '%s,%s\t%s' % (medallion,pickupDay,totalAmount)

