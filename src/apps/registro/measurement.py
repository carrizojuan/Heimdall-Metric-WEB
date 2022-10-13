from influxable import attributes, serializers
from influxable.measurement import Measurement


class MQTTConsumerMeasurement(Measurement):
    parser_class = serializers.FormattedSerieSerializer
    measurement_name = 'mqtt_consumer'

    time = attributes.TimestampFieldAttribute()
    Kwh = attributes.FloatFieldAttribute() # se cambia por el de abajo
    # valor_lectura=attributes.FloatFieldAttribute()
    topic = attributes.StringFieldAttribute()
    host = attributes.StringFieldAttribute()
    #nro_serie= attributes.IntegerFieldAttribute()
    #id_lectura= attributes.IntegerFieldAttribute()
    #tipo_lectura== attributes.StringFieldAttribute()


