#!/bin/bash
NAME="heimdallMetricAPI"
DJANGODIR="/opt/heimdall-metric-api/src"
NUM_WORKERS=1
IP_RUN="127.0.0.1:8036"
echo "Arrancando heimdall metric_api"
cd $DJANGODIR
source "/opt/Entornos/ve_heimdall-metric-api/bin/activate"
exec gunicorn -w $NUM_WORKERS $NAME.wsgi:application --bind $IP_RUN
