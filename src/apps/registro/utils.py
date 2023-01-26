from django.conf import settings
import time
from influxable import Influxable
from influxable.db import Field
from .measurement import MQTTConsumerMeasurement
from influxable.db import RawQuery
from datetime import datetime
from influxdb_client import InfluxDBClient
import random

def instanciar():
    """
    Instancia de InfluxDB
    """
    """ token = settings.INFLUXDB_TOKEN
    database = settings.INFLUXDB_DATABASE_NAME
    url = settings.INFLUXDB_URL
    client = Influxable(
        base_url=url,
        token = token,
        database_name = database
    ) """
    client = Influxable(base_url=settings.INFLUXDB_URL,
                        user=settings.INFLUXDB_USER,
                        database_name=settings.INFLUXDB_DATABASE_NAME,
                        password=settings.INFLUXDB_PASSWORD)
    
    print(f"Conectado: {client.ping()}")
      
    """ res = MQTTConsumerMeasurement.get_query().select('*').limit(100).evaluate()
    print("*"*100)
    print(res)
 """    
    # Ahora podemos imprimir los datos generados para comprobar que están correctos


    return client









