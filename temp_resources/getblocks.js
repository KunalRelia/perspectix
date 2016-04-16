function checkclicked(lat,lng){
	var triangleCoords=[];
	//document.getElementById("blockid").value='lat='+lat.toPrecision(9)+'&lng='+lng.toPrecision(9);
	$.ajax({
		url: 'http://127.0.0.1/hoods/index.php?c=register&a=getblocks&lat='+lat.toPrecision(9)+'&lng='+lng.toPrecision(9), 
    	success: function(data) {
    		var obj = JSON.parse(data);			
			var arrayLength = obj.length;
			for (var i = 0; i < arrayLength; i++) {
				document.getElementById("blockid").value=obj[i].bid;
			    var boundCount = obj[i].bounds.length;
			    document.getElementById("print").value=boundCount;
			    for (var j = 0; j < boundCount; j++) {
			    	triangleCoords.push({lat: parseFloat(obj[i].bounds[j][0]), lng: parseFloat(obj[i].bounds[j][1])});
			    }
			}
  			setbounds(triangleCoords);
    	},
    	data: {
      		format: 'json'
    	},
    	error: function(data) {
      		console.log(JSON.stringify(data));
	    },
    	type: 'GET'
    });
  }