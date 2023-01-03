from influxable import attributes, serializers
from influxable.measurement import Measurement


class MQTTConsumerMeasurement(Measurement):
    parser_class = serializers.FlatFormattedSerieSerializer 
    measurement_name = 'mqtt_consumer'

    time = attributes.TimestampFieldAttribute(auto_now=True)
    Kwh = attributes.FloatFieldAttribute() # se cambia por el de abajo
    # valor_lectura=attributes.FloatFieldAttribute()
    topic = attributes.TagFieldAttribute()
    host = attributes.TagFieldAttribute()
    nro_serie= attributes.IntegerFieldAttribute()
    id_lectura= attributes.IntegerFieldAttribute()
    tipo_lectura= attributes.TagFieldAttribute()


