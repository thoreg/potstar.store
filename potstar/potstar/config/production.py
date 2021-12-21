import os

from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('PSTAR_PSQL_DB'),
        'USER': os.getenv('PSTAR_PSQL_USER'),
        'PASSWORD': os.getenv('PSTAR_PSQL_PASSWORD'),
        'HOST': os.getenv('PSTAR_PSQL_HOST'),
        'PORT': int(os.getenv('PSTAR_PSQL_PORT')),
    }
}

DEBUG = False
SECRET_KEY = os.getenv('PSTAR_PRODUCTION_DJANGO_SECRET')

STATIC_ROOT = os.getenv('PSTAR_STATIC_ROOT')

PSTAR_LOG_DIR = os.getenv('PSTAR_LOG_DIR')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{PSTAR_LOG_DIR}/django/pstar/default.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{PSTAR_LOG_DIR}/django/pstar/requests.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {  # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
