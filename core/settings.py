from pathlib import Path
import os
import tempfile

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Vercel define la variable VERCEL=1 en sus entornos
EN_VERCEL = os.environ.get('VERCEL') == '1'

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-solo-para-desarrollo-local')

DEBUG = os.environ.get('DEBUG', 'False' if EN_VERCEL else 'True') == 'True'

ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']
if os.environ.get('ALLOWED_HOSTS'):
    ALLOWED_HOSTS += os.environ['ALLOWED_HOSTS'].split(',')

CSRF_TRUSTED_ORIGINS = ['https://*.vercel.app']
if os.environ.get('CSRF_TRUSTED_ORIGINS'):
    CSRF_TRUSTED_ORIGINS += os.environ['CSRF_TRUSTED_ORIGINS'].split(',')

# Vercel sirve por HTTPS a través de un proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'farmacia',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# En producción se usa DATABASE_URL (PostgreSQL, p. ej. Neon desde el Marketplace de Vercel).
# Sin DATABASE_URL en Vercel se usa SQLite en /tmp: funciona, pero los datos se pierden
# cuando la función se reinicia (el sistema de archivos de Vercel es de solo lectura salvo /tmp).
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=0, ssl_require=True),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': Path(tempfile.gettempdir()) / 'db.sqlite3' if EN_VERCEL else BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise sirve los estáticos (admin) directamente desde las apps, sin collectstatic
WHITENOISE_USE_FINDERS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
