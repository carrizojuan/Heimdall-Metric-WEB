from channels.generic.websocket import WebsocketConsumer
from .models import Equipo
import json


class EquipoConsumer(WebsocketConsumer):
    def connect(self):

        # Se conecta al canal
        self.accept()
        

    def disconnect(self, close_code):
        # Se desconecta del canal
        pass

    def receive(self, text_data):
        # Procesa el mensaje recibido
        text_data_json = json.loads(text_data)
        equipos = text_data_json['equipos']
        self.send(text_data=json.dumps({
            'equipos': equipos
        }))

    