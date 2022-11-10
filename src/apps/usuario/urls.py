from django.urls import path
import apps.usuario.views as views

app_name = 'usuario'

urlpatterns = [
    path('', views.UsuarioListView.as_view(), name="usuarios"),
    path('activos', views.UsuarioActivosListView.as_view(), name="usuarios_activos"),
    path('inactivos', views.UsuarioInactivosListView.as_view(), name="usuarios_inactivos"),
    path('administradores', views.UsuarioAdministradorListView.as_view(), name="usuarios_administradores"),
    path('monitores', views.UsuarioMonitorListView.as_view(), name="usuarios_monitores"),
    path('inactivar/<str:id>', views.inactivar_usuario, name="inactivar_usuario"),
    path('activar/<str:id>', views.activar_usuario, name="activar_usuario")
]
