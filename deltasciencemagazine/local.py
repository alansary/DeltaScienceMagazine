import os

# DIRECTORIES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '73t)2w3*2@15qy&%4_fy-p%2x6%$fi_ep4rgrro$=w@l5p@9mv'

# ALLOWED_HOSTS

ALLOWED_HOSTS = [u'127.0.0.1', u'0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'crispy_forms',
    'contact',
    'carousel',
    'latestnews',
    'developer',
    'userprofile',
    'notification',
    'volume',
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

ROOT_URLCONF = 'deltasciencemagazine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            'article/templates',
            'contact/templates',
            'latestnews/templates',
            'developer/templates',
            'userprofile/templates',
            'notification/templates',
            'volume/templates',
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

WSGI_APPLICATION = 'deltasciencemagazine.wsgi.application'

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# EMAIL SETTINGS

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

# PROFILE_AUTH

AUTH_PROFILE_MODEL = 'userprofile.UserProfile'

# MESSAGES

DELETE_MESSAGE = 50
MESSAGE_TAGS = {
    DELETE_MESSAGE: 'deleted',
}

# LOGGING

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# STATICFILES_FINDERS

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

# DATABASES

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# heroku local web

ROOT_HOSTCONF = "deltasciencemagazine.hosts"
DEFAULT_HOST = "www"
DEFALUT_REDIRECT_URL = "http://0.0.0.0:5000"
PARENT_HOST = "0.0.0.0:5000"

# # python manage.py runserver
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'assets'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')

UPLOAD_FILE_PATTERN_PREFIX = ''