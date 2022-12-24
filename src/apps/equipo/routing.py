from django.urls import path
from django.urls import re_path
from .consumers import EquipoConsumer

websocket_urlpatterns = [
    re_path(r'ws/equipos/', EquipoConsumer.as_asgi())
]