var Elasticsearch = require('c:/users/Sanju/AppData/Roaming/npm/node_modules/aws-es');

elasticsearch = new Elasticsearch({
		accessKeyId: <id>',
		secretAccessKey: <key>,
		service: 'es',
		region: <region>,
		host: <host>
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
