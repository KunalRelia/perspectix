# Instructions for Elasticsearch

###Queries used

curl -XPOST <domain>/_bulk' --data-binary @<filename>

curl -XDELETE ‘<domain>/<index>/’

curl -XGET '<ddomain>/<index>/_search?pretty=true&q=*:*'


###Creation of index prior to pushing off data

PUT taxifarejoin/

{

    "settings" : {

        "number_of_shards" : 1

    },

	"mappings" : {

		"taxifare" : {

			"properties" : {

				"medallion" : {"type" : "string"},

				"hack_license" : {"type" : "string"},

				"vendor_id" : {"type" : "string"},

				"pickup_datetime" : {"type" : "date","format":"yyyy-MM-dd HH:mm:ss","index": "not_analyzed"},

				"rate_code" : {"type" : "string"},

				"store_and_fwd_flag" : {"type" : "string"},

				"dropoff_datetime" : {"type" : "date","format":"yyyy-MM-dd HH:mm:ss","index": "not_analyzed"},

				"passenger_count" : {"type" : "integer"},

				"trip_time_in_secs" : {"type" : "integer"},

				"trip_distance" : {"type" : "float"},

				"pickup_location" : {"type" : "geo_point","index": "not_analyzed"},

				"dropoff_location" : {"type" : "geo_point","index": "not_analyzed"},

				"payment_type" : {"type" : "string"},

				"fare_amount" : {"type" : "float"},

				"surcharge" : {"type" : "float"},

				"mta_tax" : {"type" : "float"},

				"tip_amount" : {"type" : "float"},

				"tolls_amount" : {"type" : "float"},

				"total_amount" : {"type" : "float"}

			}

		}

	}

}


###Command to run the file to load join output into ES

python [path]/curlRequests.py [s3 path]
