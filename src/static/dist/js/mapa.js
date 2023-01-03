var ws_path = '/ws/equipos/';
var socket = new WebSocket('ws://' + window.location.host + ws_path);

//Seteo de iconos personalizados
var redIcon = L.icon.pulse({iconSize:[10,10],color:'red'});
var greenIcon = L.icon.pulse({iconSize:[10,10],color:'#008000'});
var orangeIcon = L.icon.pulse({iconSize:[10,10],color:'#FF8C00'});
var grayIcon = L.icon.pulse({iconSize:[10,10],color:'#464646'});


// Crear un mapa de Leaflet
var map = L.map('map', {condensedAttributionControl: false, fullscreenControl: {pseudoFullscreen: false}}).setView([-26, -60], 7);  // Establezca las coordenadas y el nivel de zoom iniciales del mapa


//Instancias de Capas:Activas y desactivadas
/* var nodos_d = L.layerGroup(); // equipos desactivados
var nodos_a = L.layerGroup(); // equipos activos */


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
    }, 5000)
    
}

// Procesa el mensaje recibido del WebSocket
socket.onmessage = function(e) {
    // Deserializa la lista de equipos del mensaje recibido
    var equipos = JSON.parse(e.data).equipos;
    equipos.forEach(function(equipo) {
        if(equipo.activo){
            var icon = greenIcon
            var mens_estado = 'Activo'
        }else{
            var icon = redIcon
            var mens_estado = 'Desactivado'
        }
        var marker = L.marker([equipo.latitud, equipo.longitud], {
            icon: icon}).addTo(map)
        marker.bindPopup("<b>Estado: </b>" + mens_estado)
            
    });
}


