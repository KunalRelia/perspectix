#!/usr/bin/python

import sys


def converttocents(val):
    val = float(val)
    if val > 0:
        val *= 100
    else:
        val = 0
    return val


def calTotalAmount(fare, sur, tax, tip, toll):
    return fare + sur + tax + tip + toll


for line in sys.stdin:
    line = line.strip()
    if 'medallion' in line:
        continue
    else:
        columns = line.split(',')
        try:
            fareAmount = converttocents(columns[5])
            surcharge = converttocents(columns[6])
            mtaTax = converttocents(columns[7])
            tipAmount = converttocents(columns[8])
            tollsAmount = converttocents(columns[9])

            totalAmount = calTotalAmount(fareAmount, surcharge, mtaTax, tipAmount, tollsAmount)

            keyList = [columns[0], columns[1], columns[2], columns[3], columns[4]]
            l2 = [fareAmount, surcharge, mtaTax, tipAmount, tollsAmount, totalAmount]
            print '%s,%s\t%s' % (','.join(keyList), ','.join(format(x, ".2f") for x in l2), 1)
        except ValueError:
            raise
