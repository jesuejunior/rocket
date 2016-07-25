from rocket.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_everest',
        'USER': 'everest',
        'PASSWORD': 'everest',
        'HOST': DATABASE_HOST,
        'PORT': '5432',
    }
}