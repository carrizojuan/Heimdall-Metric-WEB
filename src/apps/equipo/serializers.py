from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Equipo


# EquipoMedicion Serializer
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('nro_serie', 'label', 'name', 'latitud', 'longitud', 'fecha_asignacion', 'activo', 'app_eui', 'app_key', 'dev_eui')
        read_only_fields = ['nro_serie']









