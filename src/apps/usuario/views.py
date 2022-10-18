from django.conf import settings
from django.shortcuts import HttpResponseRedirect

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from knox.models import AuthToken

from .serializers import UsuarioSerializer, LoginSerializer, RegistroSerializer
from .models import Usuario


# Login
class LoginAPI(generics.GenericAPIView):
    """
    Permite manejar la autenUsuarioSerializerticación a la plataforma

    """
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.validate(request.data)
        _, token = AuthToken.objects.create(usuario)
        return Response({
            "message": "Inicio de Sesion exitoso",
            "usuario": UsuarioSerializer(usuario, context=self.get_serializer_context()).data,
            "token": token
        }, status=status.HTTP_200_OK)



# Register API
class RegistroAPI(generics.GenericAPIView):
    """
    Permite dar de alta un nuevo usuario a la plataforma

    """
    serializer_class = RegistroSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        return Response({
        "usuario": UsuarioSerializer(usuario, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(usuario)[1]
        }, status=status.HTTP_201_CREATED)
