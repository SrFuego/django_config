from .common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

ENVIRONMENT_NAME = "Testing server"
ENVIRONMENT_COLOR = "#1DC022"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


# MIGRATION_MODULES = {
#     'auth': None,
#     'contenttypes': None,
#     'default': None,
#     'sessions': None,
#
#     'core': None,
#     'profiles': None,
#     'snippets': None,
#     'scaffold_templates': None,
# }
