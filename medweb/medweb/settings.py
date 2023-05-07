"""
Django settings for medweb project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from os import getenv
from datetime import timedelta
import django_prometheus


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv('DEBUG') == '1'

ALLOWED_HOSTS = ["*"] + getenv('ALLOWED_HOSTS').split(';')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_prometheus',

    'django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',

    'medml',
    'inner_mail',
    'metrics',
    'segmentation'
]

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'medweb.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'medweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.postgresql',
        # 'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('POSTGRES_DB'),
        'USER': getenv('POSTGRES_USER'),
        'PASSWORD': getenv('POSTGRES_PASSWORD'),
        'HOST': getenv('SQL_HOST'),
        'PORT': getenv('SQL_PORT'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'medml.MedWorker'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""CUSTOM SETTINGS"""

MEDIA_URL = getenv('MEDIA_URL', 'media/')
MEDIA_ROOT = getenv('MEDIA_ROOT', './media')
MEDIA_ROOT_PATH = Path(MEDIA_ROOT)
STATIC_ROOT = "/usr/src/web/static_files"
IMAGE_NAME_MAX_CHARS = 10
BASE_MODEL_PATH = MEDIA_ROOT_PATH / 'nnModel'


# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5) if not DEBUG else timedelta(hours=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),

}

"""CELERY"""
# https://realpython.com/asynchronous-tasks-with-django-and-celery/
CELERY_BROKER_URL = "redis://redis_server:6379"
CELERY_RESULT_BACKEND = "redis://redis_server:6379"

"""NNModel"""
NN_SETTINGS = {
  'IMAGE_NAME_MAX_CHARS': 10,
  'MAX_IMAGE_BYTES': 1024,
  'classification': {
    'cross': BASE_MODEL_PATH / 'base/classUZI/cross/resnet.zip', 
    'long': BASE_MODEL_PATH / 'base/classUZI/long/resnet.zip'
  },
  'segmentation': {
    'cross': BASE_MODEL_PATH / 'base/segUZI/cross/deeplabv3plus.zip', 
    'long': BASE_MODEL_PATH / 'base/segUZI/long/deeplabv3plus.zip'
    },
}

if DEBUG:
    INSTALLED_APPS += [
        'drf_yasg',
        'debug_toolbar'
    ]
    CORS_ALLOW_ALL_ORIGINS = True
    CSRF_TRUSTED_ORIGINS = ['http://localhost:49118']
    REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    }

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware",]
    
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
else:

    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),

        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.BrowsableAPIRenderer',
            'rest_framework.renderers.JSONRenderer',
        ],

        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
            # 'rest_framework.permissions.AllowAny',
        ],

        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
        ),

        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 100,
    }

"""CHANGE"""