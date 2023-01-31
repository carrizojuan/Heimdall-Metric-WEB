
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
from django.views.decorators.csrf import csrf_exempt

app_name = 'registros'

urlpatterns = [

    #LISTADO DE REGISTROS

    #LISTAR TODOS LOS REGISTROS
    path('', views.ListarRegistrosView.as_view(), name='mqtt_consumer_list'),

    #LISTAR TODOS LOS REGISTROS DE UN EQUIPO
    #en el mismo se puede filtrar por una fecha en especifico
    path('<str:nro_serie>', views.ListarRegistrosEquipoView.as_view(), name='listar_registros_equipo'),

    #LISTAR ULTIMOS "N" REGISTROS DE UN EQUIPO
    path('<str:nro_serie>/ultimos/<int:n>', views.ListarNRegistrosEquipoView.as_view(), name='listar_n_registros_equipo'),
    
    #OBTENER EL ULTIMO REGISTRO DE UN EQUIPO
    path('<str:nro_serie>/ultimo/', views.UltimoRegistroEquipoView.as_view(), name='ultimo_registro_equipo'),
    
    #LISTAR LOS REGISTROS DE UN EQUIPO EN UN MES Y AÑO EN ESPECIFICO. mes: "<n° mes>-<año>">
    path('<str:nro_serie>/mes/<str:mes>/', views.RegistrosMesEquipoView.as_view(), name='registros_equipo_mes'),
    
    #LISTAR LOS REGISTROS DE UN EQUIPO EN UNA FECHA. fecha: "<n° dia>-<n° mes>-<año>"
    path('<str:nro_serie>/fecha/<str:fecha>/', views.RegistrosFechaEquipoView.as_view(), name='registros_equipo_fecha'),
    
    #LISTAR LOS REGISTROS DE UN EQUIPO ENTRE DOS FECHAS
    # se hace con un filtro que esta en el template
    path('<str:nro_serie>/entre-fechas/', views.RegistrosIntervaloFechaEquipoView.as_view(), name='registros_equipo_intervalo'),
    
    #LISTAR LOS REGISTROS DE UN EQUIPO EN UN AÑO
    path('<str:nro_serie>/año/<str:año>', views.RegistrosAñoEquipoView.as_view(), name='registros_equipo_intervalo'),

    path('obtener-registros/', views.obtener_registros, name='obtener_registros')
]

""" path('<str:nro_serie>/consumo-diario/<str:fecha>', views.ConsumoMensualEquipoView.as_view(), name='registros_equipo_consumo_diario') """