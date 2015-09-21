import os

import dj_database_url
from django.core.urlresolvers import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get('SECRET_KEY', 'CHANGE IN PRODUCTION')
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = []


INSTALLED_APPS = (
    # Core app
    'core',

    # Apps in this project
    'users',

    # Third party apps
    'crispy_forms',
    'incuna_auth',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


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


_db_config = dj_database_url.config(default='postgres://localhost/qanda')
_db_config['ATOMIC_REQUESTS'] = True
_db_config['CONN_MAX_AGE'] = None
DATABASES = {'default': _db_config}


LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = False


STATIC_URL = '/static/'
