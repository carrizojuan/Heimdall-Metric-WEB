from django.urls import path
from . import views

app_name = 'consumos'

urlpatterns=[
    #OBTENER EL CONSUMO ANUAL DE UN EQUIPO 
    path('<str:nro_serie>/consumo-anual/<int:año>', views.ConsumoAnualEquipoView.as_view(), name='registros_equipo_consumo_anual'),
    
    #OBTENER CONSUMO DEL MES DE UN EQUIPO
    path('<str:nro_serie>/consumo-mensual/<str:mes>', views.ConsumoMensualEquipoView.as_view(), name='registros_equipo_consumo_mensual'),
    
    #OBTENER EL CONSUMO DIARIO DE UN EQUIPO 
    path('<str:nro_serie>/consumo-diario/<str:fecha>', views.ConsumoDiarioEquipoView.as_view(), name='registros_equipo_consumo_diario'),

    #LISTAR CONSUMOS EN EL MES POR DIA DE UN EQUIPO 
    # fecha: "<n° mes>-<año>"
    path('<str:nro_serie>/consumo-mensual-dia/<str:fecha>', views.ConsumoMensualPorDiaEquipoView.as_view(), name='equipo_consumo_mensual_dia'),
    
    #LISTAR CONSUMOS ENTRE DOS FECHAS POR DIA
]