import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = '/Users/kd/projects/django/media/'

STATIC_ROOT = '/Users/kd/projects/django/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = '#8c84609&ilve82t@kz#h%d-2zs)0x4d%%kq5hbvc*_7963pt4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
