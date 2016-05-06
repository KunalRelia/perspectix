#!/usr/bin/env python

import sys
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians


def calculate_distance(pick_lat, pick_lon, drop_lat, drop_lon):
    earth_radius_miles = 3959

    lat1 = radians(pick_lat)
    lon1 = radians(pick_lon)
    lat2 = radians(drop_lat)
    lon2 = radians(drop_lon)

    d_lon = lon2 - lon1
    d_lat = lat2 - lat1

    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius_miles * c


def get_trip_time(pickup, dropoff):
    p = datetime.strptime(pickup, "%Y-%m-%d %H:%M:%S")
    d = datetime.strptime(dropoff, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    if now > p or now > d:
        return -1
    return p - d


for line in sys.stdin:
    if "trip" in line:
        continue
    row = list(value.strip() for value in line.split(','))
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
    if get_trip_time(pickupDate, dropoffDate) > 0:
        straight_line_dist = calculate_distance(pick[0], pick[1], drop[0], drop[1])
        if distance >= straight_line_dist and straight_line_dist <= 8.0:
            print "1\t", line.strip()
