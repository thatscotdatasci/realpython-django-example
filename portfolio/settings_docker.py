import os
from .settings import *

CACHES['default'].update({'LOCATION': os.environ.get("REDIS_URL")})

# https://stackoverflow.com/questions/26898597/django-debug-toolbar-and-docker
DEBUG_TOOLBAR_CONFIG.update({'SHOW_TOOLBAR_CALLBACK': lambda x: True})
