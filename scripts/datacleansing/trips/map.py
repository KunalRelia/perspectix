#!/usr/bin/env python

import sys, os
from datetime import datetime

def validDate(date):
	d = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
	now = datetime.now()

	return now > d

def compareDates(pickup,dropoff):
	p = datetime.strptime(pickup, "%Y-%m-%d %H:%M:%S")
	d = datetime.strptime(dropoff, "%Y-%m-%d %H:%M:%S")

       	return p <= d


for line in sys.stdin:
    if "trip" in line:
        continue
    values =line.split(',')
    pickupDate = values[5]
    dropoffDate = values[6]

    if validDate(dropoffDate) and validDate(pickupDate) and compareDates(pickupDate,dropoffDate):
    	print line.strip()
