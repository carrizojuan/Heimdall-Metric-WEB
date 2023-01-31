# ------------------------ CONFIGURACION 1: FEDE ----------------------------------------------
from .base import *

CONFIG_SEL = 2  # VARIABLE PARA ELEGIR COMO INSTANCIAR INFLUXDB

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True

# Configuración credenciales
credentials_file = os.path.join(BASE_DIR, "settings", "credentials", "accessfede.conf")
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
    },
    'api': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parser.get('api', 'name'),
        'USER': parser.get('api', 'user'),
        'PASSWORD': parser.get('api', 'password'),
        'HOST': parser.get('api', 'host'),
        'PORT': parser.get('api', 'port'),
    }
}

INFLUXDB_URL = parser.get('influxdb', 'INFLUXDB_URL')
INFLUXDB_DATABASE_NAME = parser.get('influxdb', 'INFLUXDB_DATABASE_NAME')

# Optional
INFLUXDB_USER = parser.get('influxdb', 'INFLUXDB_USER')
INFLUXDB_PASSWORD = parser.get('influxdb', 'INFLUXDB_PASSWORD')

# OSS 2.0
INFLUXDB_AUTH_TOKEN = parser.get('influxdb', 'INFLUXDB_AUTH_TOKEN')

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
