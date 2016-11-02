"""
Django settings for recomovie project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from os.path import dirname, abspath, join

DEBUG = True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1o&p08juv8z#^xm&*g%4v%x_g_$e=(vz%teo3cm2eeu^c@yov#'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'djangobower',
    'recomovie.api',
    'recomovie.desktop',
    'recomovie.movies',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'recomovie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'recomovie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'recomovie/static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap',
    'font-awesome',
)

###### URLS API ######

# THE MOVIE DB ########
THE_MOVIE_DB_CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'

# URL IMAGES, POSTER AND PHOTOS
IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{movie_id}/images?api_key={key}'
IMG_PATTERN_ES = 'http://api.themoviedb.org/3/movie/{movie_id}/images?api_key={key}&language=es-ES'

# URL MOVIE
MOVIE_PATTERN = 'http://api.themoviedb.org/3/movie/{movie_id}?api_key={key}'

# URL DISCOVER MOVIE
DISCOVER_URL = 'http://api.themoviedb.org/3/movie/top_rated?language=es-ES&api_key={key}&page={page}'

# URL CAST
PERSON_URL = 'http://api.themoviedb.org/3/person/{movie_id}/images?api_key={key}'
CREDITS_URL = 'http://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={key}'

# URL VIDEO YOUTUBE
VIDEO_URL = 'http://api.themoviedb.org/3/movie/{movie_id}/videos?language=es-ES&api_key={key}'

# URL GENRES
GENRE_LIST_URL = 'http://api.themoviedb.org/3/genre/movie/list?api_key={key}&language=es-ES'
GENRE_URL = 'http://api.themoviedb.org/3/discover/movie?language=es-ES&with_genres={genre}&api_key={key}'

NETFLIX_URL = 'https://www.netflix.com/watch/{show_id}'

# Heroku configuration
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
enviroment = os.environ.get('ENVIRONMENT', '')
if enviroment:
    THE_MOVIE_DB_KEY = os.environ.get('THE_MOVIE_DB_KEY', '')
    if enviroment == 'travis':
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    if enviroment == 'heroku':
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)

        # Honor the 'X-Forwarded-Proto' header for request.is_secure()
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

        # Allow all host headers
        ALLOWED_HOSTS = ['*']

        # Static files (CSS, JavaScript, Images)

        STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
        STATIC_URL = '/static/'

        # Extra places for collectstatic to find static files.
        STATICFILES_DIRS = [
            os.path.join(PROJECT_ROOT, 'static'),
        ]

        # Simplified static file serving.
        # https://warehouse.python.org/project/whitenoise/
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    from settings_local import *
except ImportError:
    pass
