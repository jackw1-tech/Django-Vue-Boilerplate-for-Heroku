"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url
from dotenv import load_dotenv

ALLOWED_HOSTS = ['*', '0.0.0.0', 'localhost', '192.168.x.x','your-app-name.herokuapp.com']


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-qlag58uqtk*)j#y!=w!lyo-@x*859tcjxk8_k6e8g+6now8d5u'


DEBUG = True
#DEBUG = False


load_dotenv() 


DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main',
    'rest_framework'
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

ROOT_URLCONF = 'back.urls'

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

WSGI_APPLICATION = 'back.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#Db connection to supabase

#DATABASES = {
    #'default': {  
     #   'ENGINE': 'django.db.backends.postgresql',
      #  'NAME': 'postgres',
       # 'USER': '',
       # 'PASSWORD': '',
       # 'HOST': '',
       # 'PORT': '',  
       # 'OPTIONS': {
        #    'gssencmode': 'disable',
         #   'sslmode': 'require',  # Usa SSL per la connessione
           # 'options': '-c statement_timeout=30000 -c krbsrvname=postgres',  # Disabilita GSSAPI
       # },
   # }
#}

# Vite - Django connection
VITE_BUILD_DIRNAME = "build"
VITE_STATIC_BUNDLE = BASE_DIR / f"static/{VITE_BUILD_DIRNAME}"


print(f"DJANGO_ENV: {DJANGO_ENV}")

if DJANGO_ENV == 'production':
    VITE_LIVE_SERVER = False 
else:
    VITE_LIVE_SERVER = True 



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())