#!/usr/bin/python

import sys


def convert_to_cents(val):
    val = float(val)
    if val > 0:
        val *= 100
    else:
        val = 0
    return int(val)

count = 0

for line in sys.stdin:
    line = line.strip()
    if 'medallion' in line:
        continue
    else:
        columns = line.split(',')
        try:
            l2 = list(convert_to_cents(x) for x in columns[5:-1])
            #remove all tuples with total amount > $500, possible outliers
            if (temp_total_amount=sum(l2))>50000:
                continue
            l2.append(temp_total_amount)

            print '%d\t%s,%s' % (count, ','.join(columns[:5]), ','.join(str(x) for x in l2))
            count += 1
        except ValueError:
            continue
