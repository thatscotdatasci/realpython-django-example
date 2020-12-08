import os
from .settings import *

CACHES['default'].update({'LOCATION': os.environ.get('REDIS_URL')})

# https://stackoverflow.com/questions/26898597/django-debug-toolbar-and-docker
DEBUG_TOOLBAR_CONFIG.update({'SHOW_TOOLBAR_CALLBACK': lambda x: True})

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOSTNAME"),
        'PORT': '5432',
    }
}
