#!/usr/bin/python

import sys


def convert_to_cents(val):
    val = float(val)
    if val > 0:
        val *= 100
    else:
        val = 0
    return int(val)


def calc_total_amount(fare, sur, tax, tip, toll):
    return fare + sur + tax + tip + toll

count = 0

for line in sys.stdin:
    line = line.strip()
    if 'medallion' in line:
        continue
    else:
        columns = line.split(',')
        try:
            l2 = list(convert_to_cents(x) for x in columns[5:-1])
            l2.append(sum(l2))

            print '%d\t%s,%s' % (count, ','.join(columns[:5]), ','.join(str(x) for x in l2))
            count += 1
        except ValueError:
            continue
