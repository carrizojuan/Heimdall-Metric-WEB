from channels.generic.websocket import WebsocketConsumer
from .models import Equipo
import json


class EquipoConsumer(WebsocketConsumer):
    def connect(self):

        # Se conecta al canal
        self.accept()
        #self.channel_layer.group_add('equipos', self.channel_name)

    def disconnect(self, close_code):
        # Se desconecta del canal
        pass
        #self.channel_layer.group_discard('equipos', self.channel_name)

    def receive(self, text_data):
        # Procesa el mensaje recibido
        text_data_json = json.loads(text_data)
        equipos = text_data_json['equipos']
        self.send(text_data=json.dumps({
            'equipos': equipos
        }))