from .ENV import BASE_DIR, ENV_VAR

# SECURITY WARNING: don't run with debug turned on in production!
# False if not in os.environ
DEBUG = ENV_VAR('DEBUG', default=True)

# SECURITY WARNING: keep the secret key used in production secret!
# If not found in os.environ will raise ImproperlyConfigured error
SECRET_KEY = ENV_VAR('SECRET_KEY', default='omt87r-ugl9ryuufz_-cb!4a5g(cg1%jvbw#!%w3)l9!fz&n=sum')

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_extensions',
    # DRF apps
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'django_filters',
    # Local Apps
    'apps.mobiles'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR('templates'),
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': ENV_VAR.db(default='psql://postgres:secret@127.0.0.1:5432/mobileapidb')
}
DATABASES['default']['CONN_MAX_AGE'] = 500

# Password validators
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR('static'),
]
STATIC_ROOT = BASE_DIR('staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# '' if not in os.environ
EMAIL_HOST = ENV_VAR('EMAIL_HOST', default='')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# '' if not in os.environ
EMAIL_HOST_USER = ENV_VAR('EMAIL_HOST_USER', default='')
# '' if not in os.environ
EMAIL_HOST_PASSWORD = ENV_VAR('EMAIL_HOST_PASSWORD', default='')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
