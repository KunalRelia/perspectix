# perspectix

###Course project for Big Data - DS 1004 under Prof.Juliana Freire

by

####Kunal Relia

####Sanjitha Udipi

####Abhishek Pillai


#####Brief
Explore & Analyze the NYC Taxi data.

####Project Workflow - Our appraoch


#####Cleaning the data

*use - scripts/datacleansing files*

Once the entire dataset was downloaded from [here](https://publish.illinois.edu/dbwork/open-data/), it needed to be cleaned. 

The taxi had many anomalous data like a (0,0) coordinate or travel distance was less than the straight line distance. There were also many points that were outside the New York City and something of the taxi drop-offs were in middle of Pacific Ocean! So using the polygon of NYC provided by the civic dashboards [here](http://catalog.civicdashboards.com/dataset/e5bbe399-aee4-45d4-a7d3-d6ece7f18bf4/resource/a31b967f-3df2-47da-ac67-50fa420f9cb2/download/9a2703e0737d4aab855017ff2d636603nycboroughboundaries.geojson), we removed the points that were not within the city boundary limits. The data was cleaned using python mapper and reducer on AWS EMR.  For the weather data [availabe here](http://www.ncdc.noaa.gov/qclcd/QCLCD), we were fortunate enough to have got a cleaned data from the website itself. 

#####Joining the Taxi data with Fare data

*use - scripts/mr/joins files*
	
Once the the trips and fares were cleaned, the datasets were joined using “medallion, hack_license, vendor_id, pickup_datetime” as its key. The data needed to be joined so as to ensure the trip data without any fare is removed and any fare data without the corresponding trips is removed. Also, the analysis was heavily dependent on using the data from both the datasets.

#####Queries

*use - scripts/mr/queries files*
	
After joining the datasets, querying was done. The entire query processing was done in 2 parts: 
Queries that modularized certain parameters for a quicker execution in future
Queries whose output was loaded into the AWS Elasticsearch in JSON format

The first part of the queries ensured that whenever we run the map reduce jobs to create the JSON format, the time consumed was less.

Queries that modularized certain parameters for a quicker execution in future

* Query - trips per day
This query simply calculated the total number of trips per day.

* Query - trips per taxi per day
This query calculated the total number of trips done by each taxi per day.

* Query - popular drop off locations
This query clusters together the most popular drop off locations

* Query - popular pick up locations
This query clusters together the most popular pick up locations

#####Converting the Map Reduce output to JSON format for Elasticsearch

*use - scripts/es/ files*

All the data processing was to be done using the AWS Elasticsearch. Hence, the data needed to be converted into JSON format. Map Reduce jobs were run on the previous outputs and the result of the map reduce job was JSON files. 

The results obtained by queries from previous section along with the entire joined data served as input for this batch of queries. These queries gave output in form of JSON format so that it can directly be used as an input for elasticsearch.

* Elasticsearch Query - dayTrips
This query simply converted the output of a query from previous set into JSON format

* Elasticsearch Query - Weather
This query made the use of weather data and converted the already cleaned csv data into JSON format

* Elasticsearch Query - dayPaymentType
This query fetched the joined trip & fare data and found the ratio (percentage) of trips that were paid with cash and card.

* Elasticsearch Query - distRangeFreq
This query helps us to rank the most frequent distance range ,ie, the distance range having the most number of trips

#####Execution strategy (a suggestion so as to save AWS charges)

We used the “scale up on success” technique where a code could move up in hierarchy only if it passed the lower step. Incase of failure on any step, that code would have to start back from the previous success step.

The technique followed for this project was to first run the code locally on a small subset of data to check its executability. If successful, then the code was run on local hadoop to check its functionality in hadoop environment on taxi data for one day. Finally, the code was loaded and executed on AWS EMR on entire year’s data. 
 

#####Visualize the JSON output using curl command on AWS Elasticsearch

*refer to scripts/es/InstructionsForElasticSearch.md*

After the queried data was converted into JSON format, it was ready for visualization. Curl command was used to upload these JSON files into the AWS Elasticsearch. The results from the AWS Elasticsearch were fetched using the curl command.

Once the data was received, it was represented using appropriate graphs.

#####Analyze the final product

The final step in the project was to analyze the graphs and visual representations. Various interesting analysis was done on the output and newer inferences were tried to be made using the existing resources. 
