from django.views.generic import ListView, DetailView, View
from .measurement import MQTTConsumerMeasurement
import calendar
from influxable.db.function import aggregations
from influxable.db import Field
from influxable.db import RawQuery
from datetime import datetime
from apps.equipo.models import Equipo


class ListarRegistrosView(ListView):
    """
        Lista todos los registros
        * Requiere autenticación
    """

    template_name = 'registros/registros_total.html'
    context_object_name = 'readings'

    def get_queryset(self):
        # Ejecuta la consulta y devuelve los resultados
        str_query = f'SELECT time, Kwh, topic, NumeroDeSerie FROM mqtt_consumer ORDER BY time DESC LIMIT 20'
        res = RawQuery(str_query).execute()
        registros = []
        if 'series' in res['results'][0]:
            valores = res['results'][0]['series'][0]['values']
            for v in valores:
                registro = {}
                registro["time"] = datetime.fromtimestamp(v[0]/(1000000000)).strftime('%d-%m-%Y')
                registro["Kwh"] = v[1]
                registro["topic"] = v[2]
                registro["nro_serie"] = v[3]
                registros.append(registro)
        
        return registros
    

class ListarRegistrosEquipoView(ListView):
    
    template_name = 'registros/registros_equipo.html'
    context_object_name = 'readings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_queryset(self):
        nro_serie = int(self.kwargs["nro_serie"])
        fecha = self.request.GET.get('fecha')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')
        if fecha:
            #Convertimos la fecha a un objeto datetime
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        
            # Obtenemos el valor de timestamp Unix a partir del objeto datetime
            timestamp_unix = int(fecha.timestamp())*1000000000
        
            str_query = f'SELECT time, Kwh, topic, NumeroDeSerie FROM mqtt_consumer WHERE NumeroDeSerie={nro_serie} AND time>{timestamp_unix} AND time<{timestamp_unix + 86400*1000000000} ORDER BY time DESC LIMIT 20'
            res = RawQuery(str_query).execute()
            registros = []
            if 'series' in res['results'][0]:
                valores = res['results'][0]['series'][0]['values']
                for v in valores:
                    registro = {}
                    registro["time"] = datetime.fromtimestamp(v[0]/(1000000000)).strftime('%d-%m-%Y')
                    registro["Kwh"] = v[1]
                    registro["topic"] = v[2]
                    registro["nro_serie"] = v[3]
                    registros.append(registro)
            return registros
        else:
            # Ejecuta la consulta y devuelve los resultados
            registros = []
            if fecha_inicio and fecha_fin:
                # Convertimos la fecha a un objeto datetime
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
                # Obtenemos el valor de timestamp Unix a partir del objeto datetime
                fecha_inicio = int(fecha_inicio.timestamp())*1000000000
                fecha_fin = int(fecha_fin.timestamp())*1000000000
            

                # Ejecutamos la consulta y filtramos los registros por la fecha
                
                str_query = f'SELECT time, Kwh, topic, NumeroDeSerie FROM mqtt_consumer WHERE NumeroDeSerie={nro_serie} AND time>{fecha_inicio} AND time<{fecha_fin} ORDER BY time DESC LIMIT 20'
                res = RawQuery(str_query).execute()
                
            elif fecha_inicio:
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
                fecha_inicio = int(fecha_inicio.timestamp())*1000000000

                str_query = f'SELECT time, Kwh, topic, NumeroDeSerie FROM mqtt_consumer WHERE NumeroDeSerie={nro_serie} AND time>{fecha_inicio} ORDER BY time DESC LIMIT 20'
                res = RawQuery(str_query).execute()

            elif fecha_fin:
            
                fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
                fecha_fin = int(fecha_fin.timestamp())*1000000000
                print(fecha_fin)

                str_query = f'SELECT time, Kwh, topic, NumeroDeSerie FROM mqtt_consumer WHERE NumeroDeSerie={nro_serie} AND time<{fecha_fin} ORDER BY time DESC LIMIT 20'
                res = RawQuery(str_query).execute()

            else:
                str_query = f'SELECT time, Kwh, topic, NumeroDeSerie FROM mqtt_consumer WHERE NumeroDeSerie={nro_serie} ORDER BY time DESC LIMIT 20'
                res = RawQuery(str_query).execute()
                
            if 'series' in res['results'][0]:
                    valores = res['results'][0]['series'][0]['values']
                    for v in valores:
                        registro = {}
                        registro["time"] = datetime.fromtimestamp(v[0]/(1000000000)).strftime('%d-%m-%Y')
                        registro["Kwh"] = v[1]
                        registro["topic"] = v[2]
                        registro["nro_serie"] = v[3]
                        registros.append(registro)

            return registros


def create_registro(r):
    registro = {}
    registro["time"] = datetime.fromtimestamp(r["time"]/(1000000000))
    # Accedemos a los campos de la medición y los almacenamos en el diccionario
    registro["Kwh"] = r["Kwh"]
    registro["topic"] = r["topic"]
    #registro["host"] = r["host"]
    registro["nro_serie"] = r["NumeroDeSerie"]
    #registro["id_lectura"] = r["id_lectura"]
    #registro["tipo_lectura"] = r["tipo_lectura"]
    # Añadimos el registro a la lista de registros
    return registro

class ListarNRegistrosEquipoView(ListView):
    """
        Lista los últimos n registros de un equipo
    """

    template_name = 'registros/registros_equipo.html'
    context_object_name = 'readings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_queryset(self):
        nro_serie = int(self.kwargs["nro_serie"])
        nro_registros = int(self.kwargs["n"])
        # Ejecuta la consulta y devuelve los resultados
        res = MQTTConsumerMeasurement.get_query().select('*') \
                .where(
                Field("nro_serie") == nro_serie)\
                .limit(nro_registros).evaluate()

        registros = []
        
        for r in res:
            registro = create_registro(r)
            # Añadimos el registro a la lista de registros
            registros.append(registro)
        return registros


#Se obtiene el ultimo registro de un equipo
class UltimoRegistroEquipoView(DetailView):
    template_name = 'registros/ultimo_registro_equipo.html'
    context_object_name = 'registro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_object(self, queryset=None):
        nro_serie = int(self.kwargs["nro_serie"])
        # Ejecuta la consulta y obtiene el último registro del equipo
        res = MQTTConsumerMeasurement.get_query().select('*') \
                .where(
                Field("nro_serie") == nro_serie
        ).limit(1).evaluate()

        print(res)
        # Si hay un resultado, devuelve un diccionario con la información del registro
        if res:
            return create_registro(res[0])
        # Si no hay resultados, devuelve None
        return None
    
#Lista los registros de un equipo dada una fecha
class RegistrosFechaEquipoView(ListView):
    template_name = 'registros/registros_equipo.html'
    context_object_name = 'readings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_queryset(self):
        # Obtenemos los parámetros de la URL
        nro_serie = int(self.kwargs["nro_serie"])
        fecha = self.kwargs["fecha"]
        # Convertimos la fecha a un objeto datetime
        fecha = datetime.strptime(fecha, '%d-%m-%Y')
       
        # Obtenemos el valor de timestamp Unix a partir del objeto datetime
        timestamp_unix = int(fecha.timestamp())*1000000000
       

        # Ejecutamos la consulta y filtramos los registros por la fecha
        res = MQTTConsumerMeasurement.get_query().select('*') \
                .where(
                    Field("nro_serie") == nro_serie,
                    Field("time") > timestamp_unix,
                    Field("time") < (timestamp_unix + 86400*1000000000)
                ).evaluate()
        
        registros = []

        for r in res:
            registro = create_registro(r)
            # Añadimos el registro a la lista de registros
            registros.append(registro)
        return registros


#Lista los registros de un equipo dada una fecha en un mes
class RegistrosMesEquipoView(ListView):
    template_name = 'registros/registros_equipo.html'
    context_object_name = 'readings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_queryset(self):
    
        nro_serie = int(self.kwargs["nro_serie"])
        mes_año = self.kwargs["mes"]
        
        año = int(mes_año.split("-")[1])
        mes = int(mes_año.split("-")[0])

        # Obtenemos el primer y último día del mes
        primer_dia = datetime(año, mes, 1)
        ult_dia = datetime(año, mes, calendar.monthrange(año, mes)[1], 23, 59, 59)

        primer_dia = int(primer_dia.timestamp())*1000000000
        ult_dia = int(ult_dia.timestamp())*1000000000

        res = MQTTConsumerMeasurement.get_query().select('*') \
                .where(
                    Field("nro_serie") == nro_serie,
                    Field("time") > primer_dia,
                    Field("time") < (ult_dia + 86400*1000000000)
                ).evaluate()
        
        registros = []

        for r in res:
            registro = create_registro(r)
            # Añadimos el registro a la lista de registros
            registros.append(registro)
        return registros


class RegistrosIntervaloFechaEquipoView(ListView):
    template_name = 'registros/registros_equipo_intervalo.html'
    context_object_name = 'readings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_queryset(self):
        # Obtenemos los parámetros de la URL
        nro_serie = int(self.kwargs["nro_serie"])
        fecha = ('fecha')
        fecha_inicio = self.request.GET.get("fecha_inicio")
        fecha_fin = self.request.GET.get("fecha_fin")

        if fecha_inicio and fecha_fin:
            # Convertimos la fecha a un objeto datetime
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
       
            # Obtenemos el valor de timestamp Unix a partir del objeto datetime
            fecha_inicio = int(fecha_inicio.timestamp())*1000000000
            fecha_fin = int(fecha_fin.timestamp())*1000000000
        

            # Ejecutamos la consulta y filtramos los registros por la fecha
            res = MQTTConsumerMeasurement.get_query().select('*') \
                    .where(
                        Field("nro_serie") == nro_serie,
                        Field("time") > fecha_inicio,
                        Field("time") < (fecha_fin + 86400*1000000000)
                    ).evaluate()
        
        elif fecha_inicio:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            fecha_inicio = int(fecha_inicio.timestamp())*1000000000

            res = MQTTConsumerMeasurement.get_query().select('*') \
                    .where(
                        Field("nro_serie") == nro_serie,
                        Field("time") > fecha_inicio
                    ).evaluate()
        elif fecha_fin:
        
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
            fecha_fin = int(fecha_fin.timestamp())*1000000000

            res = MQTTConsumerMeasurement.get_query().select('*') \
                    .where(
                        Field("nro_serie") == nro_serie,
                        Field("time") < (fecha_fin + 86400*1000000000)
                    ).evaluate()
        else:
            res = MQTTConsumerMeasurement.get_query().select('*') \
                    .where(
                    Field("nro_serie") == nro_serie
                ).evaluate()


        registros = []

        for r in res:
            registro = create_registro(r)
            # Añadimos el registro a la lista de registros
            registros.append(registro)
        return registros



class RegistrosAñoEquipoView(ListView):
    template_name = 'registros/registros_equipo.html'
    context_object_name = 'readings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        return context

    def get_queryset(self):
        nro_serie = int(self.kwargs["nro_serie"])
        año = int(self.kwargs["año"])
        ult_dia_año = datetime(año, 12, 31)
        ult_dia_año = int(ult_dia_año.timestamp())*1000000000 + 86400*1000000000
        primer_dia_año = datetime(año, 1, 1)
        primer_dia_año = int(primer_dia_año.timestamp())*1000000000

        res = MQTTConsumerMeasurement.get_query().select('*') \
                .where(
                    Field("nro_serie") == nro_serie,
                    Field("time") > primer_dia_año,
                    Field("time") < ult_dia_año
                ).evaluate()

        registros = []

        for r in res:
            registro = create_registro(r)
            # Añadimos el registro a la lista de registros
            registros.append(registro)
        return registros
    

class ConsumoAnualEquipoView(DetailView):
    template_name = 'registros/consumo_equipo.html'
    context_object_name = 'consumo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        context["año"] = self.kwargs["año"]
        return context



    def get_object(self, queryset=None):
        nro_serie = int(self.kwargs["nro_serie"])
        año = int(self.kwargs["año"])
        ult_dia_año = datetime(año, 12, 31)
        ult_dia_año = int(ult_dia_año.timestamp())*1000000000 + 86400*1000000000
        primer_dia_año = datetime(año, 1, 1)
        primer_dia_año = int(primer_dia_año.timestamp())*1000000000

        res = MQTTConsumerMeasurement.get_query().select(aggregations.Sum("Kwh")) \
                .where(
                    Field("nro_serie") == nro_serie,
                    Field("time") > primer_dia_año,
                    Field("time") < ult_dia_año
                ).evaluate()
        
        print(res)
        consumo_anual = res[0]['sum']

        return consumo_anual
    
class ConsumoMensualEquipoView(DetailView):
    template_name = 'registros/consumo_equipo.html'
    context_object_name = 'consumo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        context["año"] = self.kwargs["mes"].split("-")[1]
        context["mes"] = self.kwargs["mes"].split("-")[0]
        return context

    def get_object(self, queryset=None):
        nro_serie = int(self.kwargs["nro_serie"])        
        año = int(self.kwargs["mes"].split("-")[1])
        mes = int(self.kwargs["mes"].split("-")[0])

        primer_dia_mes = datetime(año, mes, 1, 0, 0, 0)
        print(primer_dia_mes)
        primer_dia_mes = int(primer_dia_mes.timestamp())*1000000000
        ult_dia_mes = datetime(año, mes, calendar.monthrange(año, mes)[1], 23, 59, 59)
        print(ult_dia_mes)
        ult_dia_mes = int(ult_dia_mes.timestamp())*1000000000
        

        res = MQTTConsumerMeasurement.get_query().select(aggregations.Sum("Kwh")) \
                .where(
                    Field("nro_serie") == nro_serie,
                    Field("time") > primer_dia_mes,
                    Field("time") < ult_dia_mes
                ).evaluate()
        
        print(res)
        consumo_mensual = res[0]['sum']

        return consumo_mensual
    
class ConsumoMensualPorDiaEquipoView(ListView):
    template_name = 'registros/consumo_mensual_equipo.html'
    context_object_name = 'consumos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        fecha_actual = datetime.now()
        mes = fecha_actual.month
        año = fecha_actual.year
        meses = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre"
        }
        context["año"] = año
        context["mes"] = meses[(int(mes))]

        return context

    def get_queryset(self):
        nro_serie = int(self.kwargs["nro_serie"])

        # Obtener la fecha actual
        fecha_actual = datetime.now()
        # Darle el formato "dd-mm-aaaa"
        dia = fecha_actual.day
        mes = fecha_actual.month
        año = fecha_actual.year
        print(mes)
        print(año)
         # Obtenemos el primer y último día del mes
        primer_dia = int(datetime(año, mes, 1, 0, 0, 0).timestamp())*1000000000
        ult_dia = int(datetime(año, mes, calendar.monthrange(año, mes)[1], 23, 59, 59).timestamp())*1000000000
        
        str_query = f'SELECT sum(Kwh) FROM mqtt_consumer WHERE NumeroDeSerie={nro_serie} AND time > {primer_dia} AND time < {ult_dia} GROUP BY time(1d, 3h) fill(0)'
        res = RawQuery(str_query).execute()
        registros = []
        print(res)
        if 'series' in res['results'][0]:
            valores = res['results'][0]['series'][0]['values']
            for v in valores:
                registro = {}
                registro["time"] = datetime.fromtimestamp(v[0]/(1000000000)).strftime('%d-%m-%Y')
                registro["consumo"] = v[1]
                registros.append(registro)

        return registros
    


class ConsumoDiarioEquipoView(DetailView):
    template_name = 'registros/consumo_equipo.html'
    context_object_name = 'consumo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipo"] = self.kwargs["nro_serie"]
        context["año"] = self.kwargs["fecha"].split("-")[2]
        context["mes"] = self.kwargs["fecha"].split("-")[1]
        return context

    def get_object(self, queryset=None):
        nro_serie = int(self.kwargs["nro_serie"])
        # Convertimos la fecha a un objeto datetime
        fecha = datetime.strptime(self.kwargs["fecha"], '%d-%m-%Y') 
        primer_segundo = int(fecha.replace(hour=0, minute=0, second=0).timestamp())*1000000000
        ultimo_segundo = int(fecha.replace(hour=23, minute=59, second=59).timestamp())*1000000000   
    
        res = MQTTConsumerMeasurement.get_query().select(aggregations.Sum("Kwh")) \
                .where(
                    Field("nro_serie") == nro_serie,
                    Field("time") > primer_segundo,
                    Field("time") < ultimo_segundo
                ).evaluate()
        
        print(res)
        if len(res)>0:
            consumo_diario = res[0]['sum']
        else:
            consumo_diario = "0"
    
        return consumo_diario