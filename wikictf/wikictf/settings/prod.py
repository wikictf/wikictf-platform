from __future__ import absolute_import # optional, but I like it
from .common import *
from . import *
# Production overrides
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wikictf',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')