
"""
ENDPOINTS POSIBLES:
LISTAR MEDICIONES ACORDE A UN RANGO DE FECHAS
LISTAR MEDICIONES SEGUN FECHA

LISTAR CONSUMOS EN EL MES POR DIA
LISTAR CONSUMOS ENTRE FECHAS POR DIA

OBTENER CONSUMO DEL DIA DE UN EQUIPO
OBTENER CONSUMO DEL MES DE UN EQUIPO
OBTENER CONSUMO ANUAL DE UN EQUIPO

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarRegistrosView.as_view(), name='mqtt_consumer_list'),
    path('<str:nro_serie>', views.ListarRegistrosEquipoView.as_view(), name='listar_registros_equipo'),
    path('<str:nro_serie>/ultimos/<int:n>', views.ListarNRegistrosEquipoView.as_view(), name='listar_n_registros_equipo'),
    path('<str:nro_serie>/ultimo/', views.UltimoRegistroEquipoView.as_view(), name='ultimo_registro_equipo'),
    path('<str:nro_serie>/mes/<str:mes>/', views.RegistrosMesEquipoView.as_view(), name='registros_equipo_mes'),
    path('<str:nro_serie>/fecha/<str:fecha>/', views.RegistrosFechaEquipoView.as_view(), name='registros_equipo_fecha'),
    path('<str:nro_serie>/entre-fechas/', views.RegistrosIntervaloFechaEquipoView.as_view(), name='registros_equipo_intervalo'),
    path('<str:nro_serie>/año/<str:año>', views.RegistrosAñoEquipoView.as_view(), name='registros_equipo_intervalo'),
    path('<str:nro_serie>/consumo-anual/<int:año>', views.ConsumoAnualEquipoView.as_view(), name='registros_equipo_consumo_anual')
]
