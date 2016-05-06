#!/usr/bin/python

import sys

for line in sys.stdin:
    	line = line.strip()
	key = line.replace("\t",",")
	print '%s\t%s' % (key,1)
