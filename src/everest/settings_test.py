# encoding: utf-8
# flake8: ignore=F403

from everest.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_everest',
        'USER': 'everest',
        'PASSWORD': 'everest',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}
