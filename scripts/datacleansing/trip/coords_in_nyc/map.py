#!/usr/bin/env python

import csv     # imports the csv module
import sys      # imports the sys module
import urllib2
import json
import StringIO

polygons = []

def is_left(P0, P1, P2):
    return (P1[0] - P0[0]) * (P2[1] - P0[1]) - (P2[0] - P0[0]) * (P1[1] - P0[1])

def wn_PnPoly(P, V):
    wn = 0   # the winding number counter

    # repeat the first vertex at end
    V = tuple(V[:]) + (V[0],)

    # loop through all edges of the polygon
    for i in range(len(V)-1):     # edge from V[i] to V[i+1]
        if V[i][1] <= P[1]:        # start y <= P[1]
            if V[i+1][1] > P[1]:     # an upward crossing
                if is_left(V[i], V[i+1], P) > 0: # P left of edge
                    wn += 1           # have a valid up intersect
        else:                      # start y > P[1] (no test needed)
            if V[i+1][1] <= P[1]:    # a downward crossing
                if is_left(V[i], V[i+1], P) < 0: # P right of edge
                    wn -= 1           # have a valid down intersect
    return wn

def get_nyc_bounds():
    url = "http://catalog.civicdashboards.com/dataset/e5bbe399-aee4-45d4-a7d3-d6ece7f18bf4/resource/a31b967f-3df2-47da-ac67-50fa420f9cb2/download/9a2703e0737d4aab855017ff2d636603nycboroughboundaries.geojson"
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen( req )
    data = json.loads(con.read())
    for feature in data["features"]:
        for polygon in feature["geometry"]["coordinates"]:
            if len(polygon)>20:
                polygons.append(polygon)

def is_in_nyc(P):
    for polygon in polygons:
        if(wn_PnPoly(P,polygon)!=0):
            return True
    return False

def main():
    '''
    Input file: trip data
    '''
    get_nyc_bounds()
    for line in sys.stdin:
        csv_file = StringIO.StringIO(line.strip())
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:   # iterates the rows of the file in orders
                if ("medallion" in row):
                    continue
                pick = map(float,row[-4:-2])
                drop = map(float,row[-2:])
                if(is_in_nyc(pick) and is_in_nyc(drop)):
                    print ",".join(row)

    
if __name__ == '__main__':
    main()
