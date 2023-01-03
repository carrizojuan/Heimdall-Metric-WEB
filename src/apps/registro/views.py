from django.views.generic import ListView, DetailView
from .measurement import MQTTConsumerMeasurement
from influxable.db import RawQuery
from influxable.db import Field
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
        res = MQTTConsumerMeasurement.get_query().select('*').evaluate()
        registros = []
        print(res)
        for r in res:
            registro = create_registro(r)
            # Añadimos el registro a la lista de registros
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
        # Ejecuta la consulta y devuelve los resultados
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


def create_registro(r):
    registro = {}
    registro["time"] = datetime.fromtimestamp(r["time"]/(1000000000))
    print(r["time"])
    # Accedemos a los campos de la medición y los almacenamos en el diccionario
    registro["Kwh"] = r["Kwh"]
    registro["topic"] = r["topic"]
    registro["host"] = r["host"]
    registro["nro_serie"] = r["nro_serie"]
    registro["id_lectura"] = r["id_lectura"]
    registro["tipo_lectura"] = r["tipo_lectura"]
    # Añadimos el registro a la lista de registros
    return registro

class ListarNRegistrosEquipoView(ListView):
    """
        Lista los últimos n registros de un equipo
    """

    template_name = 'registros/registros_equipo.html'
    context_object_name = 'readings'

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

    """ def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        equipo = Equipo.objects.get_or
        context["equipo"] = self.kwargs["nro_serie"]
        return context """

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

    def get_queryset(self):
        # Obtenemos los parámetros de la URL
        nro_serie = int(self.kwargs["nro_serie"])
        fecha = self.kwargs["fecha"]
        # Convertimos la fecha a un objeto datetime
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
       
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
