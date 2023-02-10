from django.urls import path
import apps.equipo.views as views


app_name = 'equipo'

urlpatterns = [
    path('equipos', views.ListEquiposView.as_view(), name="listar_equipos"),
    path('crear', views.CrearEquipoView.as_view(), name="crear_equipo"),
    path('eliminar/<str:nro_serie>', views.eliminar_equipo, name="eliminar_equipo"),
    path('inactivos', views.EquipoInactivosView.as_view(), name="equipos_inactivos"),
    path('activos', views.EquipoActivosView.as_view(), name="equipos_activos"),
    path('detalle/<str:pk>', views.EquipoDetalleView.as_view(), name="equipo_detalle"),
    path('editar/<str:pk>', views.ActualizarEquipoView.as_view(), name="editar_equipo"),
    path('api/equipos/', views.api_equipos, name='api_equipos'),
    path('consumo/<str:pk>', views.EquipoConsumoView.as_view(), name="consumo_equipo")
]






