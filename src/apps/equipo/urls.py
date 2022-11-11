from django.urls import path
import apps.equipo.views as views


app_name = 'equipo'

urlpatterns = [
    path('equipos', views.ListEquiposView.as_view(), name="listar_equipos"),
    path('crear', views.CrearEquipoView.as_view(), name="crear_equipo"),
    path('eliminar/<str:nro_serie>', views.eliminar_equipo, name="eliminar_equipo"),
    path('equipos/inactivos', views.EquipoInactivosListView.as_view(), name="equipos_inactivos"),
    path('equipos/activos', views.EquipoActivosListView.as_view(), name="equipos_activos"),
]






