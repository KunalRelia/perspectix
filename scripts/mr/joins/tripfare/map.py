#!/usr/bin/env python

import sys
header=0
for line in sys.stdin:
	if(header==0):
		header=1
		continue
	line = line.strip()
	splits = line.split(",")
	if len(splits) == 11:
		print "%s,%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s" % (splits[0],splits[1],splits[2],splits[3],"0",splits[4],splits[5],splits[6],splits[7],splits[8],splits[9],splits[10])
	else :
		print "%s,%s,%s,%s\t%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (splits[0],splits[1],splits[2],splits[5],"1",splits[3],splits[4],splits[6],splits[7],splits[8],splits[9],splits[10],splits[11],splits[12],splits[13])