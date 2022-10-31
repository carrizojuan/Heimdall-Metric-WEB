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
from django.urls import path
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
    
    #RESETEO DE CONTRASEÑA

    path('reset_password', views.password_reset_request, name="password_reset"),
    path('reset_password_sent', views.PasswordResetDoneView.as_view(template_name = "usuario/reset_pass/password_reset_sent.html"), name="password_reset_sent"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name = "usuario/reset_pass/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', views.PasswordResetCompleteView.as_view(template_name = "usuario/reset_pass/password_reset_done.html"), name="password_reset_complete"),

    #USUARIOS 
    path('perfil', views.detalle_usuario, name="detalle_usuario"),
    path('usuarios', views.UsuarioListView.as_view(), name="usuarios"),
    path('usuarios/activos', views.UsuarioActivosListView.as_view(), name="usuarios_activos"),
    path('usuarios/inactivos', views.UsuarioInactivosListView.as_view(), name="usuarios_inactivos"),
    path('usuarios/administradores', views.UsuarioAdministradorListView.as_view(), name="usuarios_administradores"),
    path('usuarios/monitores', views.UsuarioMonitorListView.as_view(), name="usuarios_monitores"),

]



