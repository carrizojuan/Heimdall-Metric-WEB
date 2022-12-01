from django.urls import path, re_path
from .views import CiudadanosView, DetalleCiudadanoView, ActualizarCiudadanoView

# CrearEntidadView, ActualizarEntidadView, EliminarEntidadView, \
#     DetalleEntidadInactivosView, DetalleEntidadActivosView

app_name = 'ciudadano'

urlpatterns = [
    path('ciudadanos', CiudadanosView.as_view(), name="listar_ciudadanos"),
    # path('nueva', CrearCiudadanoView.as_view(), name='nuev0_ciudadano'),
    path('detalle/<int:pk>/', DetalleCiudadanoView.as_view(), name='detalle_ciudadano'),
    path('editar/<int:pk>/', ActualizarCiudadanoView.as_view(), name='modificar_ciudadano'),
    # path('eliminar/<int:pk>', EliminarCiudadanoView.as_view(), name='eliminar_ciudadano'),

]
