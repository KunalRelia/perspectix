#!/usr/bin/python

import sys


def convert_to_date(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, columns = line.split('\t', 1)
    keys = key.split(',')
    values = columns.split(',')

    pick_up_date_time = keys[3]
    day = convert_to_date(pick_up_date_time)

    try:
        total_distance = int(values[5])
    except ValueError:
        total_distance = 0

    try:
        tips = int(values[-3])
    except ValueError:
        tips = 0

    try:
        toll = int(values[-2])
    except ValueError:
        toll = 0

    try:
        total_amount = int(values[-1])
    except ValueError:
        total_amount = 0

    print '%s\t%d,%d,%d,%d' % (day, total_distance, tips, toll, total_amount)
