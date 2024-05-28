from .base import *

WSGI_APPLICATION = 'Energe.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite7'),
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': "incomet",
        # 'USER': "postgres",
        # 'PASSWORD': "123456",
        # 'HOST': "localhost",
        # 'PORT': "5433",
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ABCD',
        'USER': 'root',
        'PASSWORD': '987654321',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
