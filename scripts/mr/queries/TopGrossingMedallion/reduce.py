#!/usr/bin/python

import sys

import operator

currentMedallion = None
currentTotalAmount=0
cnt = {}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    medallion, totalAmount = line.strip().split("\t", 1)
    
    try:
        count = float(totalAmount)
    except ValueError:
   	continue

    if medallion == currentMedallion:
	currentTotalAmount += count
    else:
        if currentMedallion:
	     	key = "%s" %(currentMedallion)
             	cnt[key] = currentTotalAmount
        currentMedallion = medallion
	currentTotalAmount = count
key = "%s" %(currentMedallion)
cnt[key] = currentTotalAmount
for i in range(0,20):
        if len(cnt) > 0 :
                tpword = max(cnt.iteritems(), key=operator.itemgetter(1))[0]
                print "%s\t%d" %(tpword,cnt[tpword])
                cnt.pop(tpword, None)

