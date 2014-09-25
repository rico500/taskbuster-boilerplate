# -*- coding: utf-8 -*-
"""
Django settings for taskbuster project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
# Base Dir points to the taskbuster folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Get SECRET_KEY from the virtual environment
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')


# Production settings
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'django.contrib.sitemaps',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'taskbuster.urls'

WSGI_APPLICATION = 'taskbuster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
from django.utils.translation import ugettext_lazy as _
LANGUAGE_CODE = 'en-us'
USE_I18N = True
LANGUAGES = (
    ('en', _('English')),
    ('ca', _('Catalan')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Localization
USE_L10N = True

# Time Zone support
USE_TZ = True
TIME_ZONE = 'Europe/Madrid'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Templates files
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

# Sites Framework
# SITE_ID = 1

