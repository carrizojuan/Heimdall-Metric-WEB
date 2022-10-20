from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken


from .serializers import UsuarioSerializer, LoginSerializer, RegistroSerializer, ChangePasswordSerializer, SolicitarRestablecimientoSerializer
from .models import Usuario


# Login
class LoginAPI(generics.GenericAPIView):
    
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


# Obtener Datos Usuario
class DetalleUsuarioAPI(generics.RetrieveAPIView):
    """
    Obtiene información de un Usuario según su identificador único

    * Requiere autenticación
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]


# Listo todos los usuarios
class ListaUsuariosAPI(generics.ListAPIView):
    """
    Lista todos los usuarios registrados en la plataforma.

    * Requiere autenticación
    """
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = serializer_class.Meta.model

    # paginate_by = 10

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


# activa un usuario segun id
class ActivarUsuarioAPI(generics.GenericAPIView):
    """
        Activa un usuario registrado segun el id generado
        * Requiere autenticaciòn
        """
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id", None)
        instancia = Usuario.objects.get(id=id)
        if instancia:
            if instancia.is_active:
                #return HttpResponseRedirect(settings.LOGIN_URL)
                return Response({'message': 'El usuario ya esta activo'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                instancia.is_active = True
                instancia.save()
                #HttpResponseRedirect(settings.LOGIN_URL)
                return Response({'message': 'Usuario activado'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No se encuentra el usuario registrado.'}, status=status.HTTP_400_BAD_REQUEST)


# desactiva un usuario segun id
class DesactivarUsuarioAPI(generics.GenericAPIView):
    """
        Desactiva un usuario registrado segun el id generado
        * Requiere autenticaciòn
    """
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("id", None)
        instancia = Usuario.objects.get(id=id)
        if instancia:
            if not instancia.is_active:
                return Response({'detail': 'Usuario activado.'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                instancia.is_active = False
                instancia.save()
                return Response({'message': 'Usuario desactivado'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'No se encuentra el usuario registrado.'}, status=status.HTTP_400_BAD_REQUEST)



class CambiarContraseñaAPI(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = Usuario
        permission_classes = (permissions.IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'message': 'Password updated successfully'
                }

                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SolicitarRestablecimientoPassApi(generics.GenericAPIView):

    """
    Solicita restablecer contraseña de la cuenta

    """
    serializer_class = SolicitarRestablecimientoSerializer
    pagination_class = None

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = request.data.get("email", "")
            usuario = Usuario.objects.get(email=email)
            if usuario:
                # enviar mail de reseteo de contraseña
                try:
                    # resetear_pass(usuario)
                    return Response({
                        "usuario": UsuarioSerializer(usuario, context=self.get_serializer_context()).data,
                    }, status=status.HTTP_200_OK)
                except Exception as e:
                    print("ERROR -  Tratando de enviar mail - ", str(e))
                    return Response({'detail': 'No se pudo enviar mail'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'No se encontró el usuario.'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
