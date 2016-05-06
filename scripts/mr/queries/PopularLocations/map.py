#!/usr/bin/python

import sys


def converttodate(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t', 1)

    keys = key.split(',')
    values = value.split(',')
    pickupDate = converttodate(keys[3])

    print '%0.3f,%0.3f,%0.3f,%0.3f,%s\t%s' % (
        float(values[6]), float(values[7]), float(values[8]), float(values[9]), pickupDate, 1)
