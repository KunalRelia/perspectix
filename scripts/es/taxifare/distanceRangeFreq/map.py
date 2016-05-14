#!/usr/bin/python

import sys

def convertToDate(val):
    return val.strip().split(' ')[0]

for line in sys.stdin:
    line = line.strip()
    key,value = line.split("\t",1)

    values = value.split(',')
    try:
        dist_travelled = int(values[5])
    except ValueError:
        continue

    if dist_travelled <= 1609.34*5:
        print('%s\t%s' % ('0-5',1))
    elif dist_travelled <= 1609.34 * 10:
        print('%s\t%s' % ('6-10', 1))
    elif dist_travelled <= 1609.34 * 15:
        print('%s\t%s' % ('11-15', 1))
    elif dist_travelled <= 1609.34 * 20:
        print('%s\t%s' % ('16-20', 1))
    elif dist_travelled <= 1609.34 * 25:
        print('%s\t%s' % ('21-25', 1))
    elif dist_travelled <= 1609.34 * 30:
        print('%s\t%s' % ('26-30', 1))
    elif dist_travelled <= 1609.34 * 35:
        print('%s\t%s' % ('31-35', 1))
    elif dist_travelled <= 1609.34 * 40:
        print('%s\t%s' % ('36-40', 1))
    elif dist_travelled <= 1609.34 * 45:
        print('%s\t%s' % ('41-45', 1))
    elif dist_travelled <= 1609.34 * 50:
        print('%s\t%s' % ('46-50', 1))
    else: continue
