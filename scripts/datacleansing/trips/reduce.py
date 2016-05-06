#!/usr/bin/env python


import StringIO
import csv
import json
import sys
import urllib2

polygons = []


def is_left(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


def wn_point_in_poly(point, polygon):
    wn = 0  # the winding number counter

    # repeat the first vertex at end
    polygon = tuple(polygon[:]) + (polygon[0],)

    # loop through all edges of the polygon
    for i in range(len(polygon) - 1):  # edge from V[i] to V[i+1]
        if polygon[i][1] <= point[1]:  # start y <= P[1]
            if polygon[i + 1][1] > point[1]:  # an upward crossing
                if is_left(polygon[i], polygon[i + 1], point) > 0:  # P left of edge
                    wn += 1  # have a valid up intersect
        else:  # start y > P[1] (no test needed)
            if polygon[i + 1][1] <= point[1]:  # a downward crossing
                if is_left(polygon[i], polygon[i + 1], point) < 0:  # P right of edge
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


def check_bounds_in(p, borough=None):
    i = 0
    for polygon in polygons:
        if borough is not None:
            if borough not in polygon[0]:
                continue
        if wn_point_in_poly(p, polygon[1]) != 0:
            return [True, i]
        i += 1
    return False


def is_in_manhattan(p):
    return check_bounds_in(p, "Manhattan")


def is_in_queens(p):
    return check_bounds_in(p, "Queens")


def is_in_bkln(p):
    return check_bounds_in(p, "Brooklyn")


def is_in_bronx(p):
    return check_bounds_in(p, "Bronx")


def in_nyc(p):
    if is_in_manhattan(p):
        return True
    elif is_in_queens(p):
        return True
    elif is_in_bkln(p):
        return is_in_bronx(p)


def main():
    """
    Input file: trip data
    """
    get_nyc_bounds()
    for line in sys.stdin:
        line = line.strip('\t', 2)[1]
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
            if in_nyc(pick) and in_nyc(drop):
                print ",".join(row)


if __name__ == '__main__':
    main()
