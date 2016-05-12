
import StringIO
import csv
import json
import sys
import urllib2
import requests
import os

def pushData(dir):

	for subdir, dirs, documents in os.walk(dir):
    		for document in documents:
        		f = os.path.join(subdir, document)
			r = requests.post('http://search-perspectix-3p663ekdctlax3ve6gqmrel6kq.us-west-2.es.amazonaws.com/_bulk',data=file(f,'rb').read())
    			print("%s,%s"%(r.status_code,r.text))


def main():
 	dir = sys.argv[1]
    	pushData(dir)

if __name__ == '__main__':
    main()
