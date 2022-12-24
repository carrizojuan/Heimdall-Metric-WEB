var ws_path = '/ws/equipos/';
var socket = new WebSocket('ws://' + window.location.host + ws_path);

// Crear un mapa de Leaflet
var map = L.map('map').setView([-27.454567, -58.986893], 13);  // Establezca las coordenadas y el nivel de zoom iniciales del mapa

// Añadir una capa de mapa (por ejemplo, OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
    maxZoom: 18
}).addTo(map);

// Espera a que la conexión se establezca correctamente
socket.onopen = function(){
    // Hace una solicitud HTTP para obtener la lista de equipos
    setInterval(function(){
            fetch("Equipo/api/equipos/")
        .then(response => response.json())
        .then(equipos => {
        // Envía la lista de equipos a través del WebSocket
        socket.send(JSON.stringify({
            'equipos': equipos
        }));
        });
    }, 10000)
    
}

// Procesa el mensaje recibido del WebSocket
socket.onmessage = function(e) {
    // Deserializa la lista de equipos del mensaje recibido
    var equipos = JSON.parse(e.data).equipos;
    equipos.forEach(function(equipo) {
        L.marker([equipo.latitud, equipo.longitud]).addTo(map)
            .bindPopup(equipo.nombre)
            .openPopup();
    });
}


