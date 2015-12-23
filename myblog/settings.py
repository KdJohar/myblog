"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django.conf.global_settings as DEFAULT_SETTINGS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# Application definition
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'pipeline.finders.PipelineFinder',
)

INSTALLED_APPS = (
    'wpadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'blogs',
    'tagging',
    'pipeline',
    'django.contrib.sitemaps',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
PIPELINE_CSSMIN_BINARY = 'cssmin'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.slimit.SlimItCompressor'
PIPELINE_ENABLED = True

PIPELINE_CSS = {
    'style': {
        'source_filenames': (
            'assets/css/normalize.css',
            'assets/font/font-awesome/css/font-awesome.min.css',
            'assets/libs/materialize/css/materialize.min.css',
            'assets/css/bootstrap.css',
            'assets/css/animate.min.css',
            'assets/libs/sweetalert/sweet-alert.css',
            'assets/libs/owl-carousel/owl.carousel.css',
            'assets/libs/owl-carousel/owl.transitions.css',
            'assets/libs/owl-carousel/owl.theme.css',
            'assets/css/main.css',
            'assets/css/responsive.css',
            'assets/css/colors/color1.css',
        ),
        'output_filename': 'global.css',
        'variant' : 'datauri',
    },
    'style2': {
        'source_filenames': (
            'assets/css/normalize.css',
            'assets/font/font-awesome/css/font-awesome.min.css',
            'assets/libs/materialize/css/materialize.min.css',
            'assets/css/bootstrap.css',
            'assets/css/animate.min.css',
            'assets/libs/sweetalert/sweet-alert.css',
            'assets/libs/owl-carousel/owl.carousel.css',
            'assets/libs/owl-carousel/owl.transitions.css',
            'assets/libs/owl-carousel/owl.theme.css',
            'assets/css/main.css',
            'assets/css/responsive.css',
            'assets/css/colors/color1.css',
            'assets/css/blog.css',
        ),
        'output_filename': 'global2.css',
        'variant' : 'datauri',
    }
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'assets/js/jquery.easing.1.3.js',
            'assets/js/detectmobilebrowser.js',
            'assets/js/isotope.pkgd.min.js',
            'assets/js/wow.min.js',
            'assets/js/waypoints.js',
            'assets/js/jquery.counterup.min.js',
            'assets/js/jquery.nicescroll.min.js',
            'assets/js/gmaps.js',
            'assets/libs/owl-carousel/owl.carousel.min.js',
            'assets/libs/materialize/js/materialize.min.js',
            'assets/libs/jwplayer/jwplayer.js',
            'assets/libs/sweetalert/sweet-alert.min.js',
            'assets/js/common.js',
            'assets/js/main.js',
            'assets/js/rrssb.js',

        ),
        'output_filename': 'scripts.js',
        'variant' : 'datauri',
    }
}


MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

CKEDITOR_UPLOAD_PATH = "editor_uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'cms',
        'height': 500,
        'width': 1050,
        'skin': 'moono',
        'extraPlugins': 'syntaxhighlight,youtube',

    },
}


WPADMIN = {
    'admin': {

        'title': 'KdJohar',
        'menu': {
            'top': 'wpadmin.menu.menus.BasicTopMenu',
            'left': 'wpadmin.menu.menus.BasicLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': True,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/midnight.css',
    }
}

STATIC_URL = '/static/'

MEDIA_URL = ''

STATICFILES_DIRS = os.path.join(
    os.path.dirname(__file__), '..', 'static').replace('\\', '/'),

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\', '/'),)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/tmp/memcached.sock',
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

try:
    from local_settings import *
except ImportError:
    pass
try:
    from production_settings import *
except ImportError:
    pass

