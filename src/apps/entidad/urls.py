from django.urls import path
from .views import lista_entidades

app_name = 'entidad'

urlpatterns = [
    path('entidades', lista_entidades, name="lista_entidades"),
]

