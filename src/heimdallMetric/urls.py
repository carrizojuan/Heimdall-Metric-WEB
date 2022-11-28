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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.DashboardAdmin.as_view(), name='dashboard_admin'),

    #AUTENTICACION USUARIO

    path('logout/', auth_views.logout_then_login, name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registrarme', views.registrar_usuario, name="registro_usuario"),

    #CAMBIO CONTRASEÑA

    path('cambiar-contraseña', views.CambiarContraseñaView.as_view(), name='change_password'),
    path('restablecer-contraseña', views.ResetPasswordView.as_view(), name="restablecer_contraseña"),

    path('Entidad/', include('apps.entidad.urls')),
    path('Miembro/', include('apps.entidad.url_miembros')),
    path('TipoGateways/', include('apps.tipo_gateway.urls')),
    path('Consola/', include('apps.tipo_gateway.url_consolas')),
    path('Ciudadano/', include('apps.ciudadano.urls')),
    #RESETEO DE CONTRASEÑA

    path('reset_password', views.password_reset_request, name="password_reset"),
    path('reset_password_sent', views.PasswordResetDoneView.as_view(template_name = "usuario/reset_pass/password_reset_sent.html"), name="password_reset_sent"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name = "usuario/reset_pass/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name = "usuario/reset_pass/password_reset_done.html"), name="password_reset_complete"),

    #USUARIOS 
    path('Usuario/', include('apps.usuario.urls')),

    #EQUIPOS
    path('Equipo/', include('apps.equipo.urls')),

    #MEDIDOR
    path('Medidor/', include('apps.medidor.urls')),

    path('perfil', views.detalle_usuario, name="detalle_usuario"),
    
]



