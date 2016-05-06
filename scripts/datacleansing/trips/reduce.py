#!/usr/bin/env python


import StringIO
import csv
import json
import sys
import urllib2
from math import sin, cos, sqrt, atan2, radians

polygons = []


def calculatedistance(pickuplat, pickuplon, droplat, droplon):
    R = 3959

    lat1 = radians(pickuplat)
    lon1 = radians(pickuplon)
    lat2 = radians(droplat)
    lon2 = radians(droplon)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def is_left(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


def wn_PnPoly(P, V):
    wn = 0  # the winding number counter

    # repeat the first vertex at end
    V = tuple(V[:]) + (V[0],)

    # loop through all edges of the polygon
    for i in range(len(V) - 1):  # edge from V[i] to V[i+1]
        if V[i][1] <= P[1]:  # start y <= P[1]
            if V[i + 1][1] > P[1]:  # an upward crossing
                if is_left(V[i], V[i + 1], P) > 0:  # P left of edge
                    wn += 1  # have a valid up intersect
        else:  # start y > P[1] (no test needed)
            if V[i + 1][1] <= P[1]:  # a downward crossing
                if is_left(V[i], V[i + 1], P) < 0:  # P right of edge
                    wn -= 1  # have a valid down intersect
    return wn


def get_nyc_bounds():
    url = "http://catalog.civicdashboards.com/dataset/e5bbe399-aee4-45d4-a7d3-d6ece7f18bf4/resource/" \
          "a31b967f-3df2-47da-ac67-50fa420f9cb2/download/9a2703e0737d4aab855017ff2d636603nycboroughboundaries.geojson"
    req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
    con = urllib2.urlopen(req)
    data = json.loads(con.read(), )
    for feature in data["features"]:
        for polygon in feature["geometry"]["coordinates"]:
            if len(polygon) > 20:
                if "Manhattan" in feature["properties"]["borough"] or len(polygons) == 0:
                    polygons.append([feature["properties"]["borough"], polygon])
                elif polygons[-1][0] in feature["properties"]["borough"]:
                    if len(polygons[-1][1]) < len(polygon):
                        polygons[-1] = [feature["properties"]["borough"], polygon]
                else:
                    polygons.append([feature["properties"]["borough"], polygon])
    return data


def is_in_nyc(p, borough=None):
    i = 0
    for polygon in polygons:
        if borough is not None:
            if borough not in polygon[0]:
                continue
        if wn_PnPoly(p, polygon[1]) != 0:
            return [True, i]
        i += 1
    return False


def is_in_manhattan(p):
    return is_in_nyc(p, "Manhattan")


def is_in_queens(p):
    return is_in_nyc(p, "Queens")


def is_in_bkln(p):
    return is_in_nyc(p, "Brooklyn")


def is_in_bronx(p):
    return is_in_nyc(p, "Bronx")


def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False


def main():
    """
    Input file: trip data
    """
    get_nyc_bounds()
    for line in sys.stdin:
        csv_file = StringIO.StringIO(line.strip())
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:  # iterates the rows of the file in orders
            if "medallion" in row:
                continue
            try:
                pick = map(float, row[-4:-2])
                drop = map(float, row[-2:])
            except ValueError:
                continue
            # added the condition to remove outliers (straight line dist > 8 miles)
            # and also checked if trip_dist > straight line dist
            if isfloat(row[-5]):
                if float(row[-5]) > calculatedistance(pick[0], pick[1], drop[0], drop[1]) and calculatedistance(pick[0],
                                                                                                            pick[1],
                                                                                                            drop[0],
                                                                                                            drop[1]) <= 8 and is_in_nyc(pick) and is_in_nyc(drop):
                    print ",".join(row)


if __name__ == '__main__':
    main()
