#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    
    key,value = line.split('\t',1)
    keys = key.split(',')
    medallion = keys[0]
    columns = value.split(",")
    totalAmount = float(columns[-1])
    print '%s\t%s' % (medallion,totalAmount)

