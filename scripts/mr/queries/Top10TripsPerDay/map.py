#!/usr/bin/python

import sys


def converttodate(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, columns = line.split('\t', 1)
    keys = key.split(',')
    medallion = keys[0]
    pickUpDateTime = keys[3]
    day = converttodate(pickUpDateTime)

    print '%s\t%s' % (day, 1)
