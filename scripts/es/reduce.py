#!/usr/bin/python

import sys

import csv
import json

fieldnames = ["medallion","hack_license","vendor_id","pickup_datetime","rate_code","store_and_fwd_flag","dropoff_datetime","passenger_count","trip_time_in_secs","trip_distance","pickup_location","dropoff_location","payment_type","fare_amount","surcharge","mta_tax","tip_amount","tolls_amount","total_amount"]
currentMapId = None
count = 1
for line in sys.stdin:
	data = {}
	mapId,columns = line.strip().split('\t',1)
	if int(mapId) != currentMapId:
		if currentMapId:
			currentMapId = int(mapId)
			count = 1
		else:
			currentMapId = int(mapId)
	columns = columns.split(",")
	l = len(columns)
	n =0
	for field in fieldnames:
        #To store the location as a geo point in es...we have to modify in the join
		if field == 'pickup_location' or field == 'dropoff_location':
			data[field]=columns[n+1]+","+columns[n]
			n = n+2
		else:
			data[field] = columns[n]
			n = n+1
	sys.stdout.write('{"index" : {"_index" : "taxifarejoin" , "_type" : "taxifare" , "_id" : "%s%s"}}\n'%(currentMapId,count))
	s ="{"
	for field in fieldnames:
		s = s+'"%s" : "%s" '%(field,data[field])
		#print('%s %s'%(fieldnames[-1],field))
		if fieldnames[-1] != field:
			s = s+ " , "
	s = s+"}"
	sys.stdout.write('%s'%(s))
	print("\n")
	count = count+1

