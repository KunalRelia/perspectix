#!/usr/bin/python

import sys

header = 0
for line in sys.stdin:
    	line = line.strip()
    	if header == 0:
		header = 1
		continue
    	else:
           	columns = line.split(',')
	   	try:
	     		fareAmount = float(columns[5])
			surcharge = float(columns[6])
			mtaTax = float(columns[7])
			tipAmount = float(columns[8])
			tollsAmount = float(columns[9])
			totalAmount = float(columns[10])
			if fareAmount > 0:
				fareAmount = fareAmount*100
			else:
				fareAmount = 0
			if surcharge > 0:
				surcharge = surcharge*100
			else:
				surcharge = 0
			if mtaTax > 0:
				mtaTax = mtaTax*100
			else:
				mtaTax = 0
			if tipAmount > 0:
				tipAmount = tipAmount*100
			else:
				tipAmount = 0
			if tollsAmount > 0:
				tollsAmount = tollsAmount*100
			else:
				tollsAmount = 0
			if totalAmount > 0:
				totalAmount = totalAmount*100
			else:
				totalAmount = 0

			keyList = [columns[0],columns[1],columns[2],columns[3],columns[4]]
			l2 = [fareAmount,surcharge,mtaTax,tipAmount,tollsAmount,totalAmount]
			print '%s,%s\t%s' % (','.join(keyList),','.join(format(x,".2f")for x in l2),1)
	   	except ValueError:
	     		raise
