"""
Django settings for myvalentine project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ly(pcj+0ml_(-0to*m5ght2jyyzz3)l72$%rk12ey51@%zt^xg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.coffeehangout.com',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'valentine',
    'social.apps.django_app.default',
    'gunicorn',
)


TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)


AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
   'social.backends.email.EmailAuth',
   
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'myvalentine.urls'

WSGI_APPLICATION = 'myvalentine.wsgi.application'

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
MANDRILL_API_KEY = "ckC02FTiZK8773eKiPPHbg"


# EMAIL_HOST = 'smtp.mandrillapp.com'                                                                                                          E

EMAIL_PORT = 587
EMAIL_USE_TLS = True

# EMAIL_HOST_USER = 'cupid@coffeehangout.com'
# EMAIL_HOST_PASSWORD = 'ckC02FTiZK8773eKiPPHbg'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': 'coffeeVIGNAN',
        'HOST': '127.0.0.1',
        'PORT': '3306',

    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '884636264890343'
SOCIAL_AUTH_FACEBOOK_SECRET = '76ea9acba9eec25eb8d78ddc57dc1cf3'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'publish_actions'
]
#FACEBOOK_EXTRA_DATA = ['gender']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

MEDIA_ROOT = '/var/www/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/www/static/'
STATIC_URL = '/static/'
