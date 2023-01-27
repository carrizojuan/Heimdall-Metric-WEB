from django.conf import settings
import time
from influxable import Influxable
from .measurement import MQTTConsumerMeasurement
from datetime import datetime


# from influxdb_client import InfluxDBClient
# import random

def instanciar1():
    """
    Instancia de InfluxDB juan contenedor
    """
    client = Influxable(
        base_url=settings.INFLUXDB_URL,
        token=settings.INFLUXDB_AUTH_TOKEN,
        database_name=settings.INFLUXDB_DATABASE_NAME
    )
    print(f"Conectado: {client.ping()}")

    res = MQTTConsumerMeasurement.get_query().select('*').evaluate()
    print(res)
    

    """ for i in range(5):
        current_date = random.randint(start_date, end_date)
        #print(current_date)
        print(datetime.fromtimestamp(current_date/(1000000000)))
        # Generamos una lectura aleatoria de consumo (en Kwh)
        kwh = round(random.uniform(0, 500), 1)
        print(kwh)
        # Generamos el registro con la fecha actual y el consumo aleatorio
        points.append(MQTTConsumerMeasurement(time= current_date, Kwh = kwh, nro_serie=20, topic="medicion", id_lectura=2, host="120.9.20", tipo_lectura="electricidad")) """
    # Ahora podemos imprimir los datos generados para comprobar que están correctos

    return client


# ORIGINAL


def instanciar2():
    """
    Instancia de InfluxDB test
    """
    client = Influxable(base_url=settings.INFLUXDB_URL,
                        database_name=settings.INFLUXDB_DATABASE_NAME,
                        user=settings.INFLUXDB_USER,
                        password=settings.INFLUXDB_PASSWORD)

    print(f"Conectado: {client.ping()}")
    return client
