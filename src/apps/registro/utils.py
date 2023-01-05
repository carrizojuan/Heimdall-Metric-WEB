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
    token = "GZqGCkZJS1eFdgbrFtm2Uoty0rPkv5p27Qw0Rxt4RPKV_F0xSaYBtuhH4DF7Lh7onbi5PEq1qSDTWdEvGlqikg=="
    database = "monitor_equipos"
    url = "https://us-east-1-1.aws.cloud2.influxdata.com"
    client = Influxable(
        base_url=url,
        token = token,
        database_name = database
    )
    print(f"Conectado: {client.ping()}")
      
    res = MQTTConsumerMeasurement.get_query().select('*').evaluate()
    print(res)
    """ for r in res:
        print(r["Kwh"]) """

    
    print("*"*100)
    date = int(datetime(2023, 2, 1, 22).timestamp())
    #end_date = int(datetime(2023, 3, 5).timestamp())*1000000000
    # Generamos los datos aleatorios
    points = []
    
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

    #print(points)
    point=[MQTTConsumerMeasurement(time = date, Kwh = 10.5, nro_serie = 20)]

    MQTTConsumerMeasurement.bulk_save(point)
    

    

    return client









