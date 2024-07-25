// Initialiser la carte
var map = L.map('map').setView([43.237464, -0.25244], 17); // Vue centrée sur votre position

// Ajouter une couche de tuiles satellite de Google Maps
L.tileLayer('https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}', {
    attribution: '&copy; <a href="https://www.google.com/maps">Google Maps</a>',
    maxZoom: 20
}).addTo(map);

// Charger et parser le fichier CSV
Papa.parse("csv/points.csv", {
    download: true,
    header: true,
    delimiter: ";",  // Spécifier le délimiteur
    complete: function(results) {
        results.data.forEach(function(point) {
            var marker = L.marker([point.lat, point.lon]).addTo(map);
            marker.bindPopup("<b>" + point.nom_voie + "</b><br/>" + point.numero);
        });
    }
});
