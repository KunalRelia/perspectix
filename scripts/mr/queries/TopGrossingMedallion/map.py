#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    
    key, value = line.split('\t',1)
    keys = key.split(',')
    medallion = keys[0]
    columns = value.split(",")
    totalAmount = float(columns[-1])

    # we will consider only if total amount > 0
    if totalAmount > 0:
        print '%s\t%s' % (medallion,totalAmount)

