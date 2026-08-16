"""
Django settings for Nyotaswerve CRM - a Bitrix24-like system with Tally Prime integration.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-nyotaswerve-dev-key-change-in-production')

DEBUG = os.environ.get('DEBUG', 'True').lower() in ('true', '1', 'yes')

ALLOWED_HOSTS = ['*']  # For preview - restrict in production

# CSRF & CORS trusted origins for preview domains
# Dynamically detect e2b.app sandbox preview URL
E2B_SANDBOX_ID = os.environ.get('E2B_SANDBOX_ID', '')
_trusted_origins = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost',
    'http://0.0.0.0:8000',
]

# Add e2b.app preview URLs if running in sandbox
if E2B_SANDBOX_ID:
    _trusted_origins.append(f'https://8000-{E2B_SANDBOX_ID}.e2b.app')

# Also allow env var override
_env_origins = os.environ.get('CSRF_TRUSTED_ORIGINS', '')
if _env_origins:
    _trusted_origins.extend(_env_origins.split(','))

CSRF_TRUSTED_ORIGINS = list(set(_trusted_origins))
CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    
    # Third-party
    'rest_framework',
    'corsheaders',
    'django_filters',
    'import_export',
    
    # Local apps
    'accounts',
    'contacts',
    'leads',
    'deals',
    'tasks',
    'products',
    'invoices',
    'tally',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'accounts.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard:home'
LOGOUT_REDIRECT_URL = 'accounts:login'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# CORS
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True

# Tally Prime Configuration
TALLY_CONFIG = {
    'HOST': os.environ.get('TALLY_HOST', 'localhost'),
    'PORT': int(os.environ.get('TALLY_PORT', '9000')),
    'TIMEOUT': int(os.environ.get('TALLY_TIMEOUT', '30')),
}

# Auto-sync to Tally Prime when invoices/contacts are created
TALLY_AUTO_SYNC = os.environ.get('TALLY_AUTO_SYNC', 'True').lower() in ('true', '1', 'yes')