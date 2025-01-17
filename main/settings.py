"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import socket

from django.contrib.messages import constants as message_constants
from prettyconf import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    'SECRET_KEY', default='Don\'t forget to set this in a .env file.'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=config.boolean, default=True)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=config.list,
    default='localhost, 127.0.0.1',
)

if DEBUG:
    # tricks to have debug toolbar when developing with docker
    local_ip = socket.gethostbyname(socket.gethostname())
    docker_gateway = local_ip[:-1] + '1'
    INTERNAL_IPS = [
        docker_gateway,
        'localhost',
        '127.0.0.1',
        '0.0.0.0',
    ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_rq',
    'colorfield',
    'leaflet',
    'import_export',
    'apps.commons',
    'apps.homepage',
    'apps.jobs',
    'apps.events',
    'apps.locations',
    'apps.organizations',
    'apps.schedule',
    'apps.speakers',
    'apps.tickets',
    'apps.invoices',
    'apps.api',
    'apps.certificates',
    'apps.quotes',
    'apps.members',
    'apps.notices',
    'apps.about',
    'apps.legal',
    'apps.dev',
    'apps.learn',
]

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'debug_toolbar',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.insert(5, 'debug_toolbar.middleware.DebugToolbarMiddleware')

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.commons.context_processors.glob',
                'apps.commons.context_processors.main_organization_data',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config(
            'DATABASE_ENGINE', default='django.db.backends.postgresql'
        ),
        'NAME': config('DATABASE_NAME', default='pythoncanarias'),
        'USER': config('DATABASE_USER', default='pythoncanarias'),
        'PASSWORD': config('DATABASE_PASSWORD', default='pythoncanarias'),
        'HOST': config('DATABASE_HOST', default='127.0.0.1'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.UserAttributeSimilarityValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation' '.MinimumLengthValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.CommonPasswordValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation'
            '.NumericPasswordValidator'
        )
    },
]

LOGIN_URL = '/members/login/'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, '.static'))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, '.media'))


SITE_ID = 1

# Do not remove this!
# The value in `ORGANIZATION_NAME` must match with an entry on:
# organization.models.Organization
# See code: organization.models.Organization.load_main_organization()

ORGANIZATION_NAME = config('ORGANIZATION_NAME', default='Python Canarias')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Leaflet settings

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (28.4818, -16.3206),
    'DEFAULT_ZOOM': 16,
    'MIN_ZOOM': 5,
    'MAX_ZOOM': 19,
    'RESET_VIEW': False,
}

# Stripe settings

STRIPE_PUBLIC_KEY = config(
    'STRIPE_PUBLIC_KEY',
    default='Set your Stripe api public key in .env file',
)

STRIPE_SECRET_KEY = config(
    'STRIPE_SECRET_KEY',
    default='Set your Stripe api secret key in .env file',
)

SENDGRID_API_KEY = config('SENDGRID_API_KEY', default='<sengrid api key>')

LOGFILE_NAME = os.path.join(BASE_DIR, 'web.log')
LOGFILE_SIZE = 1 * 1024 * 1024
LOGFILE_COUNT = 3

LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (
                '%(levelname)s %(asctime)s %(module)s '
                '%(process)d %(thread)d %(message)s'
            ),
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        # Log to console
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE_NAME,
            'maxBytes': LOGFILE_SIZE,
            'backupCount': LOGFILE_COUNT,
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'tickets': {
            'handlers': ['logfile', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'invoices': {
            'handlers': ['logfile', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'events': {
            'handlers': ['logfile', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'members': {
            'handlers': ['logfile', 'console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
    },
}

if DEBUG:
    LOGGING['loggers']['werkzeug'] = {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    }

LC_TIME_SPANISH_LOCALE = config('LC_TIME_SPANISH_LOCALE', default='es_ES.utf8')

REDIS_HOST = config('REDIS_HOST', default='localhost')
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
REDIS_DB = config('REDIS_DB', default=0, cast=int)
REDIS_PREFIX = config('REDIS_PREFIX', default='pycan-web')

RQ_QUEUES = {
    'default': {
        'HOST': REDIS_HOST,
        'PORT': REDIS_PORT,
        'DB': REDIS_DB,
        'DEFAULT_TIMEOUT': 360,
    },
    'low': {
        'HOST': REDIS_HOST,
        'PORT': REDIS_PORT,
        'DB': REDIS_DB,
    },
}

CURRENT_API_VERSION = 1

# Twitter API
TWITTER_API_KEY = config(
    'TWITTER_API_KEY',
    default='<Your Twitter API KEY here>',
)
TWITTER_API_SECRET_KEY = config(
    'TWITTER_API_SECRET_KEY',
    default='<Your Twitter API SECRET here>',
)
TWITTER_ACCESS_TOKEN = config(
    'TWITTER_ACCESS_TOKEN',
    default='<Your Twitter ACCESS TOKEN here>',
)
TWITTER_ACCESS_TOKEN_SECRET = config(
    'TWITTER_ACCESS_TOKEN_SECRET',
    default='<Your Twitter ACCESS SECRET here>',
)

# Random quote interval (seconds)
RANDOM_QUOTE_INTERVAL = config(
    'RANDOM_QUOTE_INTERVAL', default=10, cast=lambda i: 1000 * int(i)
)

if DEBUG:
    MESSAGE_LEVEL = message_constants.DEBUG

if DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
else:
    url_redis = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": url_redis,
            "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
            "KEY_PREFIX": REDIS_PREFIX,
        }
    }

DOMAIN = config('DOMAIN', default='localhost')
