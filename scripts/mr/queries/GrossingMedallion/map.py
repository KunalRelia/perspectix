#!/usr/bin/python

import sys


def converttodate(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t', 1)
    keys = key.split(',')
    medallion = keys[0]
    pickupDay = converttodate(keys[3])
    columns = value.split(",")
    totalAmount = float(columns[-1])
    # we will consider only those trips where total amount > 0
    if totalAmount > 0:
        print '%s,%s\t%s' % (medallion, pickupDay, totalAmount)
