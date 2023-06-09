"""
Django settings for spyFruit project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from decouple import config
import mimetypes
mimetypes.add_type("text/css", ".css", True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Importação para rodar os sites do allauth


    # Apps
    'dashboard.apps.DashboardConfig',  # Dashboard
    'users.apps.UsersConfig',  # Usuários

    # Imports
    'csp',
    'crispy_forms',
    'qr_code',
    'chartjs',

    # Allauth
    'allauth',
    'allauth.account',
    # SocialAccount é para caso deseje login via outros meios, tipo Facebook, Gmail
    'allauth.socialaccount',
]

SITE_ID = 1
# Máximo de tentativas de login errado
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
# Tempo que vai ficar sem poder acessar por erro
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 14400  # 4h

LOGIN_REDIRECT_URL = '/dashboard'
LOGOUT_REDIRECT_URL = '/login'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Proteção contra clickjacking
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Here
    # Quando ocorrer erros 404 ('Página não encontrada') o Django irá enviar emails com os erros (Obs: DEBUG = False)
    'django.middleware.common.BrokenLinkEmailsMiddleware',
]

SEND_BROKEN_LINK_EMAILS = True  # Enviar emails quando link estiver inativo

ROOT_URLCONF = 'spyFruit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates',)],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'spyFruit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASE POSTGRESQL
DATABASES = {
    # Default é o banco do projeto
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAMELOCAL'),
        'USER': config('DB_USERLOCAL'),
        'PASSWORD': config('DB_PASSWORDLOCAL'),
        'HOST': config('DB_HOSTLOCAL'),
        'PORT': config('DB_PORTLOCAL'),
    }

}


# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'mydatabase',  # This is where you put the name of the db file.
#        # If one doesn't exist, it will be created at migration time.
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Com isso ocorre verificação de email para confirmação de cadastro, o padrão é False
ACCOUNT_EMAIL_REQUIRED = False
# Confirmação de e-mail, o padrão é optional
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# Aqui vai impedir que o usuário registre ou adicione um endereço de e-mail adicional se esse já estiver
# sendo utilizado
ACCOUNT_EMAIL_UNIQUE = True

# Falso para retirar pergunta se deseja lembrar (True para sempre lembrar e None para fazer pergunta)
ACCOUNT_SESSION_REMEMBER = None

# gmail_send/settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# past the key or password app here
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'SpyFruit'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/assets/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Ajustes do STATICFILES_DIRS para rodar com DEBUG False
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'assets')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "assets"),
# ]
MEDIA_URL = '/media/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# User Model
AUTH_USER_MODEL = "users.User"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
