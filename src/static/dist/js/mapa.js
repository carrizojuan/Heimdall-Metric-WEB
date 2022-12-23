// Crear un mapa y agregar una capa base
const map = L.map("map").setView([-27.442777, -58.985833], 12);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
}).addTo(map);


// Crear una capa de marcadores y agregarla al mapa
const markersLayer = L.layerGroup().addTo(map);

// Obtener los datos del modelo y cargarlos en la capa de marcadores
fetch("Equipo/api/equipos/")
    .then(response => response.json())
    .then(equipos => {
        // Iterar sobre cada equipo y crear un marcador en el mapa
        for (const equipo of equipos) {
            // Obtener los datos de ubicación del equipo
            const latitud = equipo.latitud;
            const longitud = equipo.longitud;

            // Crear un marcador en el mapa
            const marker = L.marker([latitud, longitud]).addTo(markersLayer);
        }})