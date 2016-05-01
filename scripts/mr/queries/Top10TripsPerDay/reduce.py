#!/usr/bin/python

import sys
import operator
import os

currentDay = None
currentDaySum = 0
cnt = {}
result={}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    day, val = line.strip().split("\t", 1)
    
    try:
        count = int(val)
    except ValueError:
   	continue

    if day == currentDay:
	currentDaySum += count
    else:
        if currentDay:
	     key = "%s" %(currentDay)
	     cnt[key] = currentDaySum
	currentDay = day
	currentDaySum = count
key = "%s" %(currentDay)
cnt[key] = currentDaySum

for i in range(0,10):
        if len(cnt) > 0 :
                tpword = max(cnt.iteritems(), key=operator.itemgetter(1))[0]
                print "%s\t%d" %(tpword,cnt[tpword])
                cnt.pop(tpword, None)
