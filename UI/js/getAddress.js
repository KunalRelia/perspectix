function fetchAddress(latitude,longitude,marker) {
	
    var geocoder = new google.maps.Geocoder();  
    
    myLatLng = {lat: latitude, lng: longitude};
    geocoder.geocode({'location': myLatLng}, function(results, status) {
        if (status === google.maps.GeocoderStatus.OK) { 
            marker.bindPopup("Address : "+results[0].formatted_address);
        } else {
            console.log('Geocode was not successful for the following reason: ' + status);
            marker.bindPopup("Location Unavailable");
        }
    });  
    
}