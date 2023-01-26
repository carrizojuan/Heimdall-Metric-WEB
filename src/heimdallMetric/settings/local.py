from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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
""" 
'api': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parser.get('api', 'name'),
        'USER': parser.get('api', 'user'),
        'PASSWORD': parser.get('api', 'password'),
        'HOST': parser.get('api', 'host'),
        'PORT': parser.get('api', 'port'),
} 
"""


INFLUXDB_URL = parser.get('influxdb', 'INFLUXDB_URL')
INFLUXDB_USER = parser.get('influxdb', 'INFLUXDB_USER')
INFLUXDB_PASSWORD = parser.get('influxdb', 'INFLUXDB_PASSWORD')
#INFLUXDB_ORG = parser.get('influxdb', 'INFLUXDB_ORG')
#INFLUXDB_BUCKET = parser.get('influxdb', 'INFLUXDB_BUCKET')
INFLUXDB_TOKEN = parser.get('influxdb', 'INFLUXDB_AUTH_TOKEN')
INFLUXDB_DATABASE_NAME = parser.get('influxdb', 'INFLUXDB_DATABASE_NAME')


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
