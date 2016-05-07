#!/usr/bin/python

import sys


def converttodate(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, values = line.split('\t', 1)
    keys = key.split(',')
    medallion = keys[0]
    pickupDay = converttodate(keys[3])

    values = values.split(',')
    try:
        passenger_count, trip_time, trip_dist = list(map(int, values[3:6]))
        total_amt, total_toll, tip_amt = (int(values[-1]), int(values[-2]), int(values[-3]))
    except ValueError:
        continue
    payment_type = values[-7].strip()
    # we will consider only those trips where total amount > 0
    if total_amt > 0:
        print '%s,%s\t%d,%d,%d,%d,%d,%d,%s' % (pickupDay, medallion,
                                               passenger_count, trip_time, trip_dist, total_amt,
                                               total_toll, tip_amt, payment_type)
