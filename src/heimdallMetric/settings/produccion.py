from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'logs/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }
}