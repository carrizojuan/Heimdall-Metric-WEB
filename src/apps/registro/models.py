from influxable import attributes, serializers
from influxable.measurement import Measurement

class TemperatureMeasurement(Measurement):
    parser_class = serializers.MeasurementPointSerializer # Default
    measurement_name = 'temperature'

    time = attributes.TimestampFieldAttribute()
    phase = attributes.TagFieldAttribute()
    value = attributes.FloatFieldAttribute()
