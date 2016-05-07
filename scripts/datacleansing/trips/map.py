#!/usr/bin/env python

import sys
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians

import math


def calculate_distance(pick_point, drop_point):
    earth_radius_miles = 3959

    lat1 = radians(pick_point[1])
    lon1 = radians(pick_point[0])
    lat2 = radians(drop_point[1])
    lon2 = radians(drop_point[0])

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1

    a = ((sin(d_lat / 2)) ** 2) + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius_miles * c


def valid_trip_time(pickup, dropoff):
    p = datetime.strptime(pickup, "%Y-%m-%d %H:%M:%S")
    d = datetime.strptime(dropoff, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    if now < p or now < d:
        return False
    return p < d

count = 0

for line in sys.stdin:
    if "trip" in line:
        continue
    row = line.split(',')
    pickupDate = row[5]
    dropoffDate = row[6]
    try:
        pick = map(float, row[-4:-2])
        drop = map(float, row[-2:])
        distance = float(row[-5])
    except ValueError:
        continue
    # added the condition to remove outliers (straight line dist > 8 miles)
    # and also checked if trip_dist > straight line dist
    if not valid_trip_time(pickupDate, dropoffDate):
        continue
    straight_line_dist = calculate_distance(pick, drop)
    if straight_line_dist <= 0:
        continue
    # distance > 50 conditional was not checked for cleaned output,
    # handling during querying
    if distance < math.floor(straight_line_dist) or distance > 50:
        continue
    distance = int(straight_line_dist * 1609.34) if distance == 0 else int(distance * 1609.34)
    # If distance in meters is zero i.e. less than 1 m skip this trip
    if distance == 0:
        continue
    row[-5] = str(distance)
    print "%d\t%s" % (count, ",".join(row))
    count += 1
