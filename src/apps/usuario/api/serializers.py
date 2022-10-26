from rest_framework import serializers
from django.contrib.auth import authenticate
from ..models import Usuario
from django.utils.translation import gettext_lazy as _
from knox.models import AuthToken

# Usuario Serializer
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre_usuario', 'email', 'nombres', 'apellidos', 'is_staff',  'is_superuser', 'is_active')
        read_only_fields = ('email', 'id')

# Login Serializer
class LoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        usuario = authenticate(email = data['email'], password = data['password'])
        if usuario and usuario.is_active:
            # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
            self.context['usuario'] = usuario
            return usuario
        raise serializers.ValidationError({"message": "Credenciales Incorrectas"})


# Register Serializer
class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre_usuario', 'email', 'nombres', 'apellidos', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(email=validated_data['email'], password=validated_data['password'],
                                              nombre_usuario=validated_data['nombre_usuario'],
                                              nombres=validated_data['nombres'],
                                              apellidos=validated_data['apellidos']
                                              )
        return usuario

class ChangePasswordSerializer(serializers.Serializer):
    model = Usuario

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


# restablecer contraseña
class SolicitarRestablecimientoSerializer(serializers.Serializer):
    email = serializers.CharField(required=True, help_text=_("correo electrónico"))