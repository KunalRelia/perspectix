#!/usr/bin/python

import sys

currentLocation = None
currentTotalSum = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    geopoints, val = line.strip().split("\t", 1)

    try:
        count = int(val)
    except ValueError:
        continue

    if geopoints == currentLocation:
        currentTotalSum += count
    else:
        if currentLocation:
            print "%s\t%s" % (currentLocation, currentTotalSum)
        currentLocation = geopoints
        currentTotalSum = count

print "%s\t%s" % (currentLocation, currentTotalSum)
