#!/usr/bin/python

import sys


def convert_to_date(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, values = line.split('\t', 1)

    keys = key.split(',')
    pickup_date = convert_to_date(keys[3])

    values = values.split(',')
    try:
        pickup = list(map(float, values[6:8]))
    except ValueError:
        continue

    try:
        passenger_count, trip_time, trip_dist = list(map(int, values[3:6]))
        total_amt, total_toll, tip_amt = (int(values[-1]), int(values[-2]), int(values[-3]))
    except ValueError:
        continue
    payment_type = values[-7].strip()
    print '%s,%0.3f,%0.3f\t%d,%d,%d,%d,%d,%d,%s' % (pickup_date, pickup[0], pickup[1],
                                                    passenger_count, trip_time, trip_dist, total_amt,
                                                    total_toll, tip_amt, payment_type)
