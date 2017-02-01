"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to settings/local.py. It should not be checked into
your code repository.

"""
DEBUG = True

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev.db'),
    }
}

# ROOT_URLCONF = 'urls.local'
# WSGI_APPLICATION = 'wsgi.local.application'