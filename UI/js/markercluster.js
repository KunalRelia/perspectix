var drop_source = '/views/some_drop.geojson';
var pick_source = '/views/some_pick.geojson';

mapboxgl.accessToken = 'pk.eyJ1IjoiYWJoaXBpbCIsImEiOiJjaW5kcXExcTIweGs5djBrdnpnejF2NnR5In0.m6YGJReBUVHwgE4hKCilQA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/dark-v8',
    center: [-73.986728, 40.751882],
    zoom: 11
});

map.on('load', function () {

    // Add a new source from our GeoJSON data and set the
    // 'cluster' option to true.
    map.addSource("earthquakes", {
        type: "geojson",
        // Point to GeoJSON data. This example visualizes all M1.0+ earthquakes
        // from 12/22/15 to 1/21/16 as logged by USGS' Earthquake hazards program.
        data: "/views/some_pick.geojson",
        cluster: true,
        clusterMaxZoom: 17, // Max zoom to cluster points on
        clusterRadius: 50 // Radius of each cluster when clustering points (defaults to 50)
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
        [500, '#f28cb1'],
        [100, '#f1f075'],
        [0, '#51bbd6']
    ];

    layers.forEach(function (layer, i) {
        map.addLayer({
            "id": "cluster-" + i,
            "type": "circle",
            "source": "earthquakes",
            "paint": {
                "circle-color": layer[1],
                "circle-radius": 18
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