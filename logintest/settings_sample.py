from .settings import *

DEBUG=True
PREPEND_WWW=False

ALLOWED_HOSTS = ['*']

ENV='local'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'YOUR_DB_HERE',
        'PASSWORD': 'YOUR_DB_SECRET',
        'PORT': '',
        'USER': 'YOUR_DB_USER'
    }
}