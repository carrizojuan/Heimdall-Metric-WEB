from django.urls import path
import apps.equipo.views as views


app_name = 'equipo'

urlpatterns = [
    path('equipos', views.ListEquiposView.as_view(), name="listar_equipos"),
    path('crear', views.CrearEquipoView.as_view(), name="crear_equipo")
]






