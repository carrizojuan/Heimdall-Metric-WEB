from django.urls import path
import apps.equipo.views as views


app_name = 'equipo'

urlpatterns = [
    path('equipos', views.ListEquiposView.as_view(), name="listar_equipos"),
    path('crear', views.CrearEquipoView.as_view(), name="crear_equipo"),
    path('eliminar/<str:nro_serie>', views.eliminar_equipo, name="eliminar_equipo"),
    path('equipos/inactivos', views.EquipoInactivosView.as_view(), name="equipos_inactivos"),
    path('equipos/activos', views.EquipoActivosView.as_view(), name="equipos_activos"),
    path('equipos/<str:pk>', views.EquipoDetalleView.as_view(), name="equipo_detalle"),
    path('editar/<str:pk>', views.ActualizarEquipoView.as_view(), name="editar_equipo"),
]






