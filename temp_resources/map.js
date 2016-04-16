var map;
var bermudaTriangle;
var flag=true;
function setbounds(arg){
	triangleCoords=arg;
	bermudaTriangle = new google.maps.Polygon({
			path: triangleCoords,
		    strokeColor: '#FF0000',
		    strokeOpacity: 0.8,
		    strokeWeight: 3,
		    fillColor: '#2F0000',
		    fillOpacity: 0.35,
		    clickable: false
	});
	bermudaTriangle.setMap(map);
}

function initMap() {
	var defaultBounds = new google.maps.LatLngBounds(
	  new google.maps.LatLng(40.700621, -74.027377),
	  new google.maps.LatLng(40.763450, -73.952361)
	 );
	 
	 var options = {
	 	  bounds: defaultBounds,
	  types: ['geocode'],
	  componentRestrictions: {country: "us"}
	 };
     autocomplete = new google.maps.places.Autocomplete(
      (document.getElementById('address')),
      options);

    var myLatLng = {lat: 40.73772, lng: -73.9844164};
    map = new google.maps.Map(document.getElementById('map'), {
    center: myLatLng,
    zoom: 13,
    mapTypeControl: false,
    streetViewControl: false,
    zoomControl: true,
    zoomControlOptions: {
        position: google.maps.ControlPosition.LEFT_BOTTOM
    },
    mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    var geocoder = new google.maps.Geocoder();  
    document.getElementById('address').addEventListener('keydown', function(e) {
    	if(e.keyCode === 13){
        	geocodeAddress(geocoder, map);
        }
    });
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
    });
	    
    google.maps.event.addListener(map, 'click', function(event) {
        myLatLng = {lat: event.latLng.lat(), lng: event.latLng.lng()};
        geocoder.geocode({'location': myLatLng}, function(results, status) {
            if (status === google.maps.GeocoderStatus.OK) { 
            	if(bermudaTriangle){
            		bermudaTriangle.setMap(null);
            	}   
                marker.setPosition(results[0].geometry.location);
                document.getElementById('address').value= results[0].formatted_address;
        		document.getElementById('formaddress').value= results[0].formatted_address;
        		document.getElementById('lat').value=myLatLng.lat;
        		document.getElementById('lng').value=myLatLng.lng;
        		checkclicked(myLatLng.lat,myLatLng.lng);
        		flag=false;
            } else {
              alert('Geocode was not successful for the following reason: ' + status);
            }
        });
        marker.setPosition(myLatLng);
        marker.setMap(map);
    });
    function geocodeAddress(geocoder,resultsMap) {
        var address = document.getElementById('address').value;
        geocoder.geocode({'address': address}, function(results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
            	if(bermudaTriangle){
            		bermudaTriangle.setMap(null);
            	} 
                resultsMap.setCenter(results[0].geometry.location);
                marker.setPosition(results[0].geometry.location);
				document.getElementById('formaddress').value= results[0].formatted_address;
        		document.getElementById('lat').value=results[0].geometry.location.lat();
        		document.getElementById('lng').value=results[0].geometry.location.lng();
				checkclicked(results[0].geometry.location.lat(),results[0].geometry.location.lng());
            } else {
              alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
}