#!/usr/bin/python

import sys


def convert_to_date(val):
    return val.strip().split(' ')[0]


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    key, columns = line.split('\t', 1)
    keys = key.split(',')
    values=columns.split(',')

    pick_up_date_time = keys[3]
    day = convert_to_date(pick_up_date_time)

    total_distance = int(columns[5])
    tips = int(columns[-3])
    toll = int(columns[-2])
    total_amount = int(columns[-1])

    print '%s\t%d,%d,%d,%d' % (day, total_distance, tips, toll, total_amount)
