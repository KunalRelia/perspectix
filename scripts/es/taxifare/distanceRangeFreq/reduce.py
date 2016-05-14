#!/usr/bin/python

import sys
import operator
import os

currentRange = None
currentRangeSum = 0
cnt = {}
result = {}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    range, val = line.strip().split("\t", 1)

    try:
        count = int(val)
    except ValueError:
        continue

    if range == currentRange:
        currentRangeSum += count
    else:
        if currentRange:
            key = "%s" % (currentRange)
            cnt[key] = currentRangeSum
            sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "distanceRangeFreq" } }\n')
            s = "{"
            s = s + '"distanceRange" : "%s" ' % (key)
            s = s + " , "
            s = s + '"count" : "%s" ' % (cnt[key])
            s = s + "}"
            sys.stdout.write('%s' % (s))
            print("\n")

        currentRange = range
        currentRangeSum = count

key = "%s" % (currentRange)
cnt[key] = currentRangeSum
sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "distanceRangeFreq" } }\n')
s = "{"
s = s + '"distanceRange" : "%s" ' % (key)
s = s + " , "
s = s + '"count" : "%s" ' % (cnt[key])
s = s + "}"
sys.stdout.write('%s' % (s))
print("\n")
