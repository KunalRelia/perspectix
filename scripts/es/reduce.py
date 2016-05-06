#!/usr/bin/python

import sys

import csv
import json

fieldnames = ['Medallion','Hack license','Vendor id','Pickup datetime','Rate code','Store and fwd flag','Dropoff datetime','Passenger count','Trip time in secs','Trip distance','Pickup longitude','Pickup latitude','Dropoff longitude','Dropoff latitude','Payment type','Fare Amount','Surcharge','Mta tax','Tip amount','Tolls amount','Total amount']

count = 1
for line in sys.stdin:
	data = {}
	columns,value = line.strip().split("\t",1)
	columns = columns.split(",")
	l = len(columns)
	n =0
	for field in fieldnames:
		data[field] = columns[n]
		n = n+1
	sys.stdout.write('{"index" : {"_index" : "TaxiFareJoin" , "_type" : "taxifare" , "_id" : "%s"}}\n'%(count))
	sys.stdout.write("%s"%(data))
	print("\n")
	count = count+1

