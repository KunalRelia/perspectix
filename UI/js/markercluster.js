var drop_source = '/views/some_drop.geojson';
var pick_source = '/views/some_pick.geojson';
mapboxgl.accessToken = 'pk.eyJ1IjoiYWJoaXBpbCIsImEiOiJjaW5kcXExcTIweGs5djBrdnpnejF2NnR5In0.m6YGJReBUVHwgE4hKCilQA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/dark-v8',
    center: [-73.986728, 40.751882],
    zoom: 11
});
var options = {
    styles: [
          {
            'id': 'gl-draw-active-line',
            'type': 'line',
            'filter': ['all',
              ['==', '$type', 'LineString'],
              ['==', 'active', 'true']
            ],
            'layout': {
              'line-cap': 'round',
              'line-join': 'round'
            },
            'paint': {
              'line-color': '#FF9800',
              'line-dasharray': [0.2, 2],
              'line-width': 4
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-active-polygon',
            'type': 'fill',
            'filter': ['all', ['==', 'active', 'true'], ['==', '$type', 'Polygon']],
            'paint': {
              'fill-color': '#FF9800',
              'fill-opacity': 0.25
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-active-polygon-stroke',
            'type': 'line',
            'filter': ['all', ['==', 'active', 'true'], ['==', '$type', 'Polygon']],
            'layout': {
              'line-cap': 'round',
              'line-join': 'round'
            },
            'paint': {
              'line-color': '#FF9800',
              'line-dasharray': [0.2, 2],
              'line-width': 4
            },
            'interactive': true
          },


          {
            'id': 'gl-draw-point-mid-outline',
            'type': 'circle',
            'filter': ['all',
              ['==', '$type', 'Point'],
              ['==', 'meta', 'midpoint']],
            'paint': {
              'circle-radius': 7,
              'circle-opacity': 0.65,
              'circle-color': '#fff'
            },
            'interactive': true
          },
            {
            'id': 'gl-draw-point-mid',
            'type': 'circle',
            'filter': ['all',
              ['==', '$type', 'Point'],
              ['==', 'meta', 'midpoint']],
            'paint': {
              'circle-radius': 6,
              'circle-opacity': 0.65,
              'circle-color': '#FF9800'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-polygon',
            'type': 'fill',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'Polygon']],
            'paint': {
              'fill-color': '#FF1924',
              'fill-outline-color': '#FF1924',
              'fill-opacity': 0.25
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-polygon-stroke',
            'type': 'line',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'Polygon']],
            'layout': {
              'line-cap': 'round',
              'line-join': 'round'
            },
            'paint': {
              'line-color': '#FF0100',
              'line-width': 3
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-line',
            'type': 'line',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'LineString']],
            'layout': {
              'line-cap': 'round',
              'line-join': 'round'
            },
            'paint': {
              'line-color': '#03A9F4',
              'line-width': 3
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-active-point',
            'type': 'circle',
            'filter': ['all',
              ['==', '$type', 'Point'],
              ['==', 'active', 'true'],
              ['!=', 'meta', 'midpoint']
            ],
            'paint': {
              'circle-radius': 9,
              'circle-color': '#fff'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-active-point-highlight',
            'type': 'circle',
            'filter': ['all',
              ['==', '$type', 'Point'],
              ['!=', 'meta', 'midpoint'],
              ['==', 'active', 'true']],
            'paint': {
              'circle-radius': 7,
              'circle-color': '#EF6C00'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-polygon-point-outline',
            'type': 'circle',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'Point'], ['==', 'meta', 'vertex']],
            'paint': {
              'circle-radius': 9,
              'circle-color': '#fff'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-polygon-point',
            'type': 'circle',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'Point'], ['==', 'meta', 'vertex']],
            'paint': {
              'circle-radius': 7,
              'circle-color': '#FF9800'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-point-point-outline',
            'type': 'circle',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'Point'], ['==', 'meta', 'feature']],
            'paint': {
              'circle-radius': 9,
              'circle-color': '#fff'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-point',
            'type': 'circle',
            'filter': ['all', ['==', 'active', 'false'], ['==', '$type', 'Point'], ['==', 'meta', 'feature']],
            'paint': {
              'circle-radius': 7,
              'circle-color': '#03A9F4'
            },
            'interactive': true
          },
          {
            'id': 'gl-draw-too-small',
            'type': 'circle',
            'filter': ['all', ['==', '$type', 'Point'], ['==', 'meta', 'too-small']],
            'paint': {
              'circle-radius': 5,
              'circle-color': '#037994'
            },
            'interactive': true
          }
    ]
};
var readyForQuery = false;
var Draw = mapboxgl.Draw(options);
map.addControl(Draw);
map.on('draw.modechange', function(e){
//    console.log(e);
    if(!e || !e.mode)
        return
    if (readyForQuery) {
        if(e.mode === "simple_select"){
            if (queriedPolygons.length === 2){
                readyForQuery = false;
                queryFromPolygons();
            }
        }
    }
    if(e.mode === "draw_line_string"){
        readyForQuery = true;
    } else {
        readyForQuery = false;
    }
});
map.on('load', function () {

    // Add a new source from our GeoJSON data and set the
    // 'cluster' option to true.
    map.addSource("earthquakes", {
        type: "geojson",
        // Point to GeoJSON data. This example visualizes all M1.0+ earthquakes
        // from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
        data: pick_source,
        cluster: true,
        clusterMaxZoom: 17, // Max zoom to cluster points on
        clusterRadius: 35 // Radius of each cluster when clustering points (defaults to 50)
    });

    // Use the earthquakes source to create five layers:
    // One for non-clustered markers, three for each cluster category,
    // and one for cluster labels.
    map.addLayer({
        "id": "non-cluster-markers",
        "type": "symbol",
        "source": "earthquakes",
        "layout": {
            "icon-image": "marker-15"
        }
    });

    // Display the earthquake data in three layers, each filtered to a range of
    // count values. Each range gets a different fill color.
    var layers = [
        [1000, '#fc2c41', 20],
        [500, '#f1a075', 16],
        [0, '#51bbd6', 13]
    ];

    layers.forEach(function (layer, i) {
        map.addLayer({
            "id": "cluster-" + i,
            "type": "circle",
            "source": "earthquakes",
            "paint": {
                "circle-color": layer[1],
                "circle-radius": layer[2]
            },
            "filter": i === 0 ?
                [">=", "point_count", layer[0]] :
                ["all",
                    [">=", "point_count", layer[0]],
                    ["<", "point_count", layers[i - 1][0]]]
        });
    });

    // Add a layer for the clusters' count labels
    map.addLayer({
        "id": "cluster-count",
        "type": "symbol",
        "source": "earthquakes",
        "layout": {
            "text-field": "{point_count}",
            "text-font": [
                    'DIN Offc Pro Medium',
                    'Arial Unicode MS Bold'
                ],
            "text-size": 12
        }
    });
});

/**
 * getFeatureFromClick
 *
 * parameter - e : jQuery click event
 * return first valid polygon feature, else
 *        last feature in list if valid, else
 *        undefined if no valid feature list at click point
 */
var getFeatureFromClick = function (e) {
    if(!e.clientX || !e.clientY)
        return undefined;
    var featureID = Draw.getFeatureIdsAt(e.clientX,e.clientY);
//    console.log(featureID);
    var feature = undefined;
    if (!featureID || !featureID.length)
            return feature;
    for (var i = 0; i<featureID.length; i++) {
        if (feature = Draw.get(featureID[i]) ) {
            if (checkIfFeatureIs(feature[i],"Polygon")){
                return feature;
            }
        } 
    }
    return feature;
};
var checkIfFeatureIs = function (feature, type) {
    if (feature && feature.geometry && feature.geometry.type) {
        if(feature.geometry.type === type) {
            return true;
        }
    }
    return false;
}
$(document).on('click', function(e){
    var feature = getFeatureFromClick(e)
    if (checkIfFeatureIs(feature,"Polygon")) {
        Draw.options.styles[5].paint["line-color"]="#03A9F4";
    }
});

$(document).on('click', function(e){
    var feature = getFeatureFromClick(e)
//    console.log(readyForQuery);
    if(checkIfFeatureIs(feature, "Polygon") && readyForQuery) {
//        console.log("les do this");
        readyForQuery = true;
        addPolygon(feature);
//        console.log("currently"+queriedPolygons.length);
        return;
    }
//    console.log("not ready");
    queriedPolygons=[];
    readyForQuery = false;
});
document.getElementById('pickup').onclick = function () {
    var enable = this.className !== 'active';
    map.getSource("earthquakes").setData(pick_source)
    this.className = enable ? 'active' : '';
    document.getElementById('dropoff').className = !enable ? 'active' : '';
    return false;
};

document.getElementById('dropoff').onclick = function () {
    var enable = this.className !== 'active';
    map.getSource("earthquakes").setData(drop_source)
    this.className = enable ? 'active' : '';
    document.getElementById('pickup').className = !enable ? 'active' : '';
    return false;
};

/**
 * queriedPolygons - queried polygons stored here
 * legal value - geoJSON array
 * legal length - 0,1,2
 * length = 2 if both pickup and dropoff have been selected by the user using a simple line
 * length = 1 if only the pickup has been chosen and currently in draw line mode
 * length = 0 otherwise
 * must be reset each time an invalid state occurs, invalid state - 
 *      - not in draw line mode (using line to indicate query polygons)
 */
var queriedPolygons = [];
var addPolygon = function (feature) {
    if (!checkIfFeatureIs(feature, "Polygon")) {
        return 0;
    }
    if (queriedPolygons.push(feature) > 2) {
        queriedPolygons=[];
    }
    return queriedPolygons.length;
};
var queryFromPolygons = function () {
    console.log(queriedPolygons.length+" length, we good?");
    console.log(queriedPolygons);
    // TODO: curl polygons to elastic search and update sources to reflect the query result
    selectByPolygon(queriedPolygons)
    result = curl();
    if (result){
        map.getSource("earthquakes").setData(result);
    }
};


var selectByPolygon = function(polygon) {
    if(!checkIfFeatureIs(polygon, "Polygon"))
        return
    data = map.getSource("earthquakes");
    
    console.log(data);
    $.getJSON(data._data, function(json) {
        output = {
            "type": "FeatureCollection",
            "features": []
        };
        for (var i = 0; i<json["features"].length; i++) {
             if (json["features"][i]) {
                 if (turf.inside(json["features"][i], polygon[1]) && turf.inside(json["features"][i], polygon[0])) {
                    output["features"].push(i);
                 }
             }
        }
        console.log(output)
        map.getSource("earthquakes").setData(output);
    });
};
