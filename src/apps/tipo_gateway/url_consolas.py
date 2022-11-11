from django.urls import path
from .views import EliminarConsolaView
# CrearConsolaView,ActualizarConsolaView, DetalleConsolaView

app_name = 'consola'

urlpatterns = [
    # path('nuevo/<int:pk>/', CrearMiembroView.as_view(), name='nuevo_miembro'),
    # path('detalle/<int:pk>/', DetalleMiembroView.as_view(), name='detalle_miembro'),
    # path('editar/<int:pk>/', ActualizarMiembroView.as_view(), name='modificar_miembro'),
    path('eliminar/<int:pk>/', EliminarConsolaView.as_view(), name='eliminar_consola'),

]