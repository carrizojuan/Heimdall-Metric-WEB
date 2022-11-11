from django.urls import path
from .views import EliminarConsolaView, DetalleConsolaView, ActualizarConsolaView
# CrearConsolaView,ActualizarConsolaView, DetalleConsolaView

app_name = 'consola'

urlpatterns = [
    # path('nuevo/<int:pk>/', CrearMiembroView.as_view(), name='nuevo_consola'),
    path('detalle/<int:pk>/', DetalleConsolaView.as_view(), name='detalle_consola'),
    path('editar/<int:pk>/', ActualizarConsolaView.as_view(), name='modificar_consola'),
    path('eliminar/<int:pk>/', EliminarConsolaView.as_view(), name='eliminar_consola'),

]