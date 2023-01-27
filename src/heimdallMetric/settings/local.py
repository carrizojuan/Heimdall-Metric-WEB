# ------------------------ CONFIGURACION 1: JUAN ----------------------------------------------
from .base import *

CONFIG_SEL = 1  # VARIABLE PARA ELEGIR COMO INSTANCIAR INFLUXDB

DEBUG = True

ALLOWED_HOSTS = []

# Configuración credenciales
credentials_file = os.path.join(BASE_DIR, "settings", "credentials", "access.conf")
parser = configparser.ConfigParser()
parser.read(credentials_file)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parser.get('default', 'name'),
        'USER': parser.get('default', 'user'),
        'PASSWORD': parser.get('default', 'password'),
        'HOST': parser.get('default', 'host'),
        'PORT': parser.get('default', 'port'),
    }
}
INFLUXDB_URL = parser.get('influxdb', 'INFLUXDB_URL')
INFLUXDB_ORG = parser.get('influxdb', 'INFLUXDB_ORG')
INFLUXDB_BUCKET = parser.get('influxdb', 'INFLUXDB_BUCKET')
INFLUXDB_AUTH_TOKEN = parser.get('influxdb', 'INFLUXDB_AUTH_TOKEN')
INFLUXDB_DATABASE_NAME = parser.get('influxdb', 'INFLUXDB_DATABASE_NAME')

INFLUXDB_DATABASES = {
    'default': {
        'NAME': INFLUXDB_DATABASE_NAME,
        'TOKEN': INFLUXDB_AUTH_TOKEN,
        'URL': INFLUXDB_URL,
        'PORT': 8086,
    }
}

# CONFIG LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'logs/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
