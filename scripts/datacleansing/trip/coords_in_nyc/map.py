#!/usr/bin/env python

import sys, os

for line in sys.stdin:
    if "trip" not in os.environ['mapreduce_map_input_file']:
        continue
    print line.strip()
