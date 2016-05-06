#!/usr/bin/env python


import StringIO
import csv
import json
import sys
import urllib2

polygons = []
manhattan = [
    [-73.9325, 40.88029],
    [- 74.0178, 40.7561],
    [- 74.0324, 40.69548],
    [- 73.97335, 40.70693],
    [- 73.9545, 40.75186],
    [- 73.91706, 40.78858],
    [- 73.92117, 40.84862],
    [- 73.89819, 40.87378]
]
queens = [
    [-73.96683, 40.73321],
    [- 73.87207, 40.63428],
    [- 73.88649, 40.61082],
    [- 73.87207, 40.58736],
    [- 73.96889, 40.54511],
    [- 73.70865, 40.52946],
    [- 73.70865, 40.66215],
    [- 73.6785, 40.73045],
    [- 73.7715, 40.81249],
    [- 73.83816, 40.80241],
    [- 73.8999, 40.79927],
    [- 73.93858, 40.78163]
]
brooklyn = [
    [-73.96133, 40.7457],
    [- 73.88134, 40.72514],
    [- 73.81989, 40.64574],
    [- 73.88403, 40.61841],
    [- 73.87207, 40.57772],
    [- 74.02644, 40.55348],
    [- 74.04295, 40.66957]
]


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
    for polygon in polygons:
        if borough is not None:
            if borough not in polygon[0]:
                continue
        if wn_point_in_poly(p, polygon[1]) != 0:
            return True
    return False


def is_in_manhattan(p):
    if wn_point_in_poly(p, manhattan) != 0:
        return check_bounds_in(p, "Manhattan")
    return False


def is_in_queens(p):
    if wn_point_in_poly(p, queens) != 0:
        return check_bounds_in(p, "Queens")
    return False


def is_in_bkln(p):
    if wn_point_in_poly(p, brooklyn) != 0:
        return check_bounds_in(p, "Brooklyn")
    return False


def is_in_bronx(p):
    return check_bounds_in(p, "Bronx")


def in_nyc(p):
    if is_in_manhattan(p):
        return True
    if is_in_queens(p):
        return True
    if is_in_bkln(p):
        return True
    return is_in_bronx(p)


def main():
    """
    Input file: trip data
    """
    get_nyc_bounds()
    for line in sys.stdin:
        key, line = line.split('\t', 2)
        if key.strip() == '0':
            print line.strip()
            continue
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
