from django.urls import path
from .views import EntidadesView, DetalleEntidadView, CrearEntidadView, ActualizarEntidadView, EliminarEntidadView, \
    DetalleEntidadInactivosView, DetalleEntidadActivosView, send_email_to_members

app_name = 'entidad'

urlpatterns = [
    path('entidades', EntidadesView.as_view(), name="lista_entidades"),
    path('nueva', CrearEntidadView.as_view(), name='nueva_entidad'),
    path('detalle/<int:pk>/',DetalleEntidadView.as_view(), name='detalle_entidad'),
    path('detalle/<int:pk>/miembros/activos', DetalleEntidadActivosView.as_view(), name='detalle_entidad_activos'),
    path('detalle/<int:pk>/miembros/inactivos', DetalleEntidadInactivosView.as_view(), name='detalle_entidad_inactivos'),
    path('editar/<int:pk>/', ActualizarEntidadView.as_view(), name='modificar_entidad'),
    path('eliminar/<int:pk>', EliminarEntidadView.as_view(), name='eliminar_entidad'),

    path('send-email/', send_email_to_members, name='send_email_to_members')

]

