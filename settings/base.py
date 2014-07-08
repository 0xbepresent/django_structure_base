"""
Django Base settings for {{project_name}} project.

Shared by all environments
"""
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{secret_key}}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#==============================================================================
# URLS and media settings
#==============================================================================

ROOT_URLCONF = 'apps.urls'

# WSGI_APPLICATION = 'wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = '%s/static/' % BASE_DIR


#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
