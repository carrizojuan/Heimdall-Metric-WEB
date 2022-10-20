from django.urls import path
from .views import LoginAPI, RegistroAPI, DetalleUsuarioAPI, ListaUsuariosAPI, ActivarUsuarioAPI, DesactivarUsuarioAPI, CambiarContraseñaAPI,SolicitarRestablecimientoPassApi
from knox.views import LogoutView
app_name = 'usuarios'


urlpatterns = [
    path('<int:pk>', DetalleUsuarioAPI.as_view(), name="detalle_usuario"),
    path('login', LoginAPI.as_view(), name='login_usuario'),
    path('logout', LogoutView.as_view(), name='logout_usuario'),
    path('registrar', RegistroAPI.as_view(), name='registro_usuario'),
    path('listar', ListaUsuariosAPI.as_view(), name='lista_usuarios'),
    path('<str:uuid>/activar', ActivarUsuarioAPI.as_view(), name='activar_usuario'),
    path('<str:uuid>/desactivar', DesactivarUsuarioAPI.as_view(), name='desactivar_usuario'),
    path('cambiar-contraseña', CambiarContraseñaAPI.as_view(), name='cambiar_contraseña'),
    path('restablecer/solicitud', SolicitarRestablecimientoPassApi.as_view(), name='restablecer_solicitud'),
]
