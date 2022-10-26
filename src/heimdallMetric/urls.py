"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


schema_view = get_schema_view(
   openapi.Info(
      title="Heindall Metric Web API",
      default_version='v1',
      description="API  de Plataforma de Telemedición",
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

api_urls = [
    # API
    #path('api/usuario/', include('apps.usuario.urls_usuario')),
    #path('api/auth/', include('apps.usuario.urls_auth'))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', views.DashboardAdmin.as_view(), name='dashboard_admin'),
    path('login', views.login ,name="login"),
    path('registrarme', views.registrar_usuario, name="registro_usuario"),
    path('perfil', views.detalle_usuario, name="detalle_usuario"),
    path('usuarios', views.lista_usuarios, name="lista_usuarios"),
    path('cambiar-contraseña', views.CambiarContraseñaView.as_view(), name='change_password'),
    path('restablecer-contraseña', views.ResetPasswordView.as_view(), name="restablecer_contraseña"),
]

