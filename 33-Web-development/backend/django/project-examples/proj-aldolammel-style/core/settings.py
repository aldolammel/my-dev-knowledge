"""
    ALDO!!!!!
    
    Be aware, DON'T replace/update this example-code below WITHOUT consider lines below have "commented" option's to follow the "New Project Installation" logic where "accounts" and multi-language options are commented, for example.

"""

from pathlib import Path
import environ
from .constants import (
    NAMESPACE_1,
    NAMESPACE_2,
    NAMESPACE_3,
    NAMESPACE_4,
    PATTERN_1_1,
    PATTERN_2_1,
    PATTERN_3_3,
)

# App Essential Settings:
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")  # Take environment variables from .env file.
env = environ.Env(DEBUG=(bool, False))  # Initialize environment variables.
# TODO: uncomment after to create the 'accounts' sub-app:
#AUTH_USER_MODEL = NAMESPACE_3 + ".User"  # Extending Django User features.
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

"""if DEBUG:
    print("SECRET_KEY:", env('SECRET_KEY', default='Not Set'))
    print("ALLOWED_HOSTS:", env('ALLOWED_HOSTS', default='Not Set'))
    print("DATABASE_URL:", env('DATABASE_URL', default='Not Set'))"""

# Application definition
# About each Installed Apps here:
# https://docs.google.com/document/d/1Xx9pGqPyUBmRg9ybJ8AZ1sh4UgtIH0DRzF62pQJukiI/edit#heading=h.ea7glk45xbxu
INSTALLED_APPS = [
    # DJANGO DEFAULT SUB-APPS:
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # DJANGO ADDITIONAL SUB-APPS:
    # "django.contrib.postgres",  # TODO: uncomment if POSTGRES DB!
    #'django_extensions',  # to use the show_url command in shell!
    # THIRD-PARTY SUB-APPS:
    #"rosetta",  # TODO: uncomment if multilingual!
    #"parler",  # TODO: uncomment if multilingual!
    # APP ORIGINAL SUB-APPS:
    #NAMESPACE_1,  # TODO: uncomment after to create the sub-app!
    #NAMESPACE_2,  # TODO: uncomment after to create the sub-app!
    #NAMESPACE_3,  # TODO: uncomment after to create the sub-app!
    #NAMESPACE_4,  # TODO: uncomment after to create the sub-app!
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # TODO: uncomment if multilingual:
    #"django.middleware.locale.LocaleMiddleware",  # Django additional built-in language features (need to be after Session).
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # TODO: uncomment if multilingual:
    #"core.middlewares.UserLanguageMiddleware",  # Advanced language features (need to be after the Locale and Authentication)!
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # DJANGO DEFAULT GLOBAL CONTEXTS:
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # DJANGO ADDITIONAL GLOBAL CONTEXTS:
                # Reserved space...
                # THIRD-PARTY GLOBAL CONTEXTS:
                # Reserved space...
                # APP CUSTOM GLOBAL CONTEXTS:
                "core.context_processors.app_info",
                "core.context_processors.constants_to_template",
                # TODO: uncomment if multilingual:
                #"core.context_processors.languages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# On cloud:
"""DATABASES = {
    # The db() method is an alias for db_url().
    'default': env.db_url('DATABASE_URL'),
}"""
# On local:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
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

# TODO: uncomment (and make USE_IE8N 'True') if multilingual:
# Internationalization
USE_I18N = False  # 'True' for multi-language support!
"""
# Available languages:
# LANG_CODE_PT = "pt"
LANG_CODE_PTBR = "pt-br"
LANG_CODE_ES = "es"
# LANG_CODE_ESMX = "es-mx"
# LANG_CODE_EN = "en"
LANG_CODE_ENUS = "en-us"
LANGUAGES = [
    # (LANG_CODE_PT, "Português (PT)"),
    (LANG_CODE_PTBR, "Português (BR)"),
    (LANG_CODE_ES, "Español (ES)"),
    # (LANG_CODE_ESMX, "Español (MX)"),
    # (LANG_CODE_EN, "English (UK)"),
    (LANG_CODE_ENUS, "English (US)"),
]
# Cefalog default language:
LANGUAGE_CODE = LANG_CODE_PTBR
LOCALE_PATHS = [BASE_DIR / "locale"]
# PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE  # Not needed because 'fallbacks' is set manually.
PARLER_LANGUAGES = {
    None: (
        {"code": LANG_CODE_PTBR},
        {"code": LANG_CODE_ENUS},
        {"code": LANG_CODE_ES},
    ),
    "default": {
        "fallbacks": [
            LANG_CODE_ENUS,
            LANG_CODE_PTBR,
            LANG_CODE_ES,
        ],  # Cascade fallbacks
        "hide_untranslated": False,
    },
}
LANGUAGE_COOKIE_NAME = "user_language"
LANGUAGE_COOKIE_AGE = 2592000  # 30 days.
"""

# Timezone-aware
# TODO: make USE_TZ 'True' for multilingual support:
USE_TZ = False  # 'True' for multi-language support compatibility!
TIME_ZONE = "America/Sao_Paulo"  # 'UTC'

# FORMATS
# Date:
DATE_FORMAT = "Y-m-d"  # ISO format for dates ('2006-10-25')
SHORT_DATE_FORMAT = "d-m-Y"  # '25-10-2006'
# Time:
TIME_FORMAT = "H:i"  # 24-hour format (H): '14:30'
# Datetime:
DATETIME_FORMAT = f"{DATE_FORMAT} {TIME_FORMAT}"  # '2006-10-25 14:30'
DATETIME_INPUT_FORMATS = [
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%Y/%m/%d %H:%M",  # '2006/10/25 14:30'
]
# Input formats:
DATE_INPUT_FORMATS = [
    "%Y-%m-%d",  # ISO 'yyyy-mm-dd'
    "%d/%m/%Y",  # '25/10/2006'
    "%d-%m-%Y",  # '25-10-2006'
]
TIME_INPUT_FORMATS = [
    "%H:%M",  # '14:30'
    "%H%M",  # '1430'
]
# Others:
FIRST_DAY_OF_WEEK = 1  # 0 = Sunday

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Authentification
SESSION_COOKIE_AGE = 2419200  # a month
LOGIN_URL = NAMESPACE_3 + ":" + PATTERN_3_3
LOGIN_REDIRECT_URL = NAMESPACE_2 + ":" + PATTERN_2_1
LOGOUT_REDIRECT_URL = NAMESPACE_1 + ":" + PATTERN_1_1

# Email settings
EMAIL_BACKEND = env(
    "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")
