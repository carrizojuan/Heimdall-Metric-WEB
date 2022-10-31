from django.urls import path
from .views import lista_entidades, CrearEntidadView

app_name = 'entidad'

urlpatterns = [
    path('entidades', lista_entidades, name="lista_entidades"),
    path('nuevaEntidad', CrearEntidadView.as_view(), name='nueva_entidad'),
]

