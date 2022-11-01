from django.urls import path
from .views import lista_entidades, DetalleEntidadView, CrearEntidadView, ActualizarEntidadView

app_name = 'entidad'

urlpatterns = [
    path('entidades', lista_entidades, name="lista_entidades"),
    path('nueva', CrearEntidadView.as_view(), name='nueva_entidad'),
    path('detalle/<int:pk>/',DetalleEntidadView.as_view(), name='detalle_entidad'),
    path('editar/<int:pk>/', ActualizarEntidadView.as_view(), name='modificar_entidad'),
]

