from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ishu.k@skysoft.net.in'
EMAIL_HOST_PASSWORD = 'ishu@kumar'

WSGI_APPLICATION = 'Energe.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "energe",
        'USER': "postgres",
        'PASSWORD': "skysoft",
        'HOST': "192.168.1.9",
        'PORT': "5432",
    }
}
