var Elasticsearch = require('c:/users/Sanju/AppData/Roaming/npm/node_modules/aws-es');

elasticsearch = new Elasticsearch({
		accessKeyId: 'AKIAJKITYVEXMYVRRJ2A',
		secretAccessKey: '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',
		service: 'es',
		region: 'us-west-2',
		host: 'search-perspectix-3p663ekdctlax3ve6gqmrel6kq.us-west-2.es.amazonaws.com'
});

elasticsearch.mget({
			index: 'cars',
			type: 'car',
			body: {
				ids: ['1', '2','3','4','5']
			}
		}, function(err, data) {
			console.log('json reply received');
			console.log(data)
			cars = data.docs
			cars.forEach(function(car){
			  console.log(car["_source"]);
			});
			
        });
