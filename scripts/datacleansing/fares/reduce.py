#!/usr/bin/python

import sys

for line in sys.stdin:

    key, valueList = line.strip().split("\t", 1)

    print "%s" % key
