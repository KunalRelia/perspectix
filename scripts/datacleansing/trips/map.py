#!/usr/bin/env python

import sys
from datetime import datetime


def validdate(date):
    d = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()

    return now > d


def comparedates(pickup, dropoff):
    p = datetime.strptime(pickup, "%Y-%m-%d %H:%M:%S")
    d = datetime.strptime(dropoff, "%Y-%m-%d %H:%M:%S")

    return p < d


for line in sys.stdin:
    if "trip" in line:
        continue
    values = line.split(',')
    pickupDate = values[5]
    dropoffDate = values[6]

    if validdate(dropoffDate) and validdate(pickupDate) and comparedates(pickupDate, dropoffDate):
        print line.strip()
