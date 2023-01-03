from django.conf import settings
import time
from influxable import Influxable
from influxable.db import Field
from .measurement import MQTTConsumerMeasurement
from influxable.db import RawQuery
from datetime import datetime
from influxdb_client import InfluxDBClient

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
      


    str_query = 'select * FROM mqtt_consumer'
    res = RawQuery(str_query).execute()
    print(res)
    

    """ res = MQTTConsumerMeasurement.get_query().select('*').evaluate()
    print(res) """
    return client









