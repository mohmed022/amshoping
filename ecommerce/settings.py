import os
from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*-7nxx+dkrjm*oyaxt47l#jwog-i#z9bwcyr@g&g^fc*e)nx-_"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False
ALLOWED_HOSTS = ['amshoping.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ecommerce.apps.catalogue",
    "ecommerce.apps.account",
    "ecommerce.apps.checkout",
    "ecommerce.apps.basket",
    "ecommerce.apps.orders",
    "mptt",
]

MIDDLEWARE = [
    
    "django.middleware.security.SecurityMiddleware",
     # Added Following One Line Of Code
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]



ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "ecommerce.apps.catalogue.context_processors.categories",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }



# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "amshoping",
#         "USER": "postgres",
#         "PASSWORD": "aml",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }




DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "database-1.cluster-ccs9eitlywtm.ap-south-1.rds.amazonaws.com",
        "USER": "admin",
        "PASSWORD": "Aml782000",
        "HOST": "ec2-18-209-143-227.compute-1.amazonaws.com",
        "PORT": "3306",
    }
}
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
# STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfile")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Basket session ID
BASKET_SESSION_ID = "basket"

# Custom user model
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"

# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#      os.path.join(BASE_DIR, "static"),
#  )

#STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static")

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#STATIC_ROOT = "/home/cfedeploy/webapps/cfehome_static_root/"

# MEDIA_URL = "/media/"

# MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media/")