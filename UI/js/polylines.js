L.mapbox.accessToken = 'pk.eyJ1Ijoic2Fuaml0aGEiLCJhIjoiY2luM25yMXZxMGJ3dXdrbHVpZWlmbDEzdiJ9.qS7O8lKdfDESfEtJW5b6bA';
var map = L.mapbox.map('map', 'mapbox://styles/mapbox/dark-v8')
    .setView([-73.986728, 40.751882], 11);

var featureGroup = L.featureGroup().addTo(map);

var drawControl = new L.Control.Draw({
  edit: {
    featureGroup: featureGroup
  },
  draw: {
    polygon: true,
    polyline: true,
    rectangle: false,
    circle: false,
    marker: false
  }
}).addTo(map);

map.on('draw:created', showPolygonArea);
map.on('draw:edited', showPolygonAreaEdited);

function showPolygonAreaEdited(e) {
  e.layers.eachLayer(function(layer) {
    showPolygonArea({ layer: layer });
  });
}
function showPolygonArea(e) {
  //featureGroup.clearLayers();
  featureGroup.addLayer(e.layer);
  e.layer.bindPopup(' 100 points');
  e.layer.openPopup();
}