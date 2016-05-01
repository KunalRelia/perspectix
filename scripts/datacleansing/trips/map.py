#!/usr/bin/env python

import sys, os

for line in sys.stdin:
    if "trip" in line:
        continue
    print line.strip()
