from django.urls import path
from .views import TiposGatewayView, CrearTipoGatewayView
# DetalleTipoGatewayView, CrearTipoGatewayView, ActualizarTipoGatewayView, EliminarTipoGatewayView

app_name = 'tipo_gateway'

urlpatterns = [
    path('gateways', TiposGatewayView.as_view(), name="lista_tipogateway"),
    path('nuevo', CrearTipoGatewayView.as_view(), name='nuevo_tipo_gateway'),
    # path('detalle/<int:pk>/',DetalleTipoGatewayView.as_view(), name='detalle_tipo_gateway'),
    # path('editar/<int:pk>/', ActualizarTipoGatewayView.as_view(), name='modificar_tipo_gateway'),
    # path('eliminar/<int:pk>', EliminarTipoGatewayView.as_view(), name='eliminar_tipo_gateway'),

]
