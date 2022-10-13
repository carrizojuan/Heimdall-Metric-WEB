from django.conf import settings
from influxable import Influxable


def instanciar():
    """
    Instancia de InfluxDB
    """
    client = Influxable(base_url=settings.INFLUXDB_URL,
                        database_name=settings.INFLUXDB_DATABASE_NAME,
                        user=settings.INFLUXDB_USER,
                        password=settings.INFLUXDB_PASSWORD)

    print(f"Conectado: {client.ping()}")
    return client

