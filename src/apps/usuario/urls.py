from django.urls import path
from .views import LoginAPI, RegistroAPI
app_name = 'usuarios'


urlpatterns = [
    path('login', LoginAPI.as_view(), name='login_usuario'),
    path('registrar/', RegistroAPI.as_view(), name='registro_usuario'),
]
