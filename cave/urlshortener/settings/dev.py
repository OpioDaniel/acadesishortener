from .base import *

DEBUG = True
# DEBUG = False
#
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['acade.com', 'www.acade.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'urlshortener',
        'USER': 'urlshortener',
        'PASSWORD': 'urlshortener',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
