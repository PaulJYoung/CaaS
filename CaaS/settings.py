"""
Django settings for GoodandBad project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''
SECRET_KEY = '5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#DOMAIN_NAME = ''
ALLOWED_HOSTS = ['*']
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_DOMAIN = DOMAIN_NAME
#CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CloudasaService',
    'storages',
    'django_mysql',
]

MIDDLEWARE_CLASSES = [
#    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CaaS.urls'

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

WSGI_APPLICATION = 'CaaS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CaaS',
	'USER': '',
	'PASSWORD': '',
        'HOST': 'db',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/CaaS/static/'
#STATIC_ROOT = '/home/pyoung/WebDev/django/Sites/CaaS/static/'
#STATIC_ROOT = '/home/pyoung/WebDev/django/Sites/GoodandBad/static/'

# Login redirect

LOGIN_REDIRECT_URL = '/CaaS/'
LOGIN_URL = '/CaaS/login/'

# AWS Storage for static files
AWS_STORAGE_BUCKET_NAME = 'caas-static-prod'
AWS_DEFAULT_ACL = 'public-read'
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = 'd6idje9xyotdi.cloudfront.net'
REGION_HOST = 's3.eu-west-2.amazonaws.com'
if not DEBUG:

#   AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_STORAGE_BUCKET_NAME = 'caas-static-prod'
    STATIC_URL = "https://d6idje9xyotdi.cloudfront.net/"
#   STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

