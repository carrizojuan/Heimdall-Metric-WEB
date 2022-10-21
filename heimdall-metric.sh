#!/bin/bash
NAME="heimdallMetric"
DJANGODIR="/opt/heimdall-metric-web/src"
NUM_WORKERS=1
IP_RUN="127.0.0.1:8041"
echo "Arrancando heimdall metric"
cd $DJANGODIR
source "/opt/Entornos/ve_heimdall-metric-web/bin/activate"
exec gunicorn -w $NUM_WORKERS $NAME.wsgi:application --bind $IP_RUN
