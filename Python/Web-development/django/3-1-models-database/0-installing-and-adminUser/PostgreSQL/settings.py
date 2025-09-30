

# Most common aldolammel's settings template/model:
# /Python/Web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py


# Or below you see all the django needs for POSTGRESQL database settings:
# /core/settings.py:
from pathlib import Path
import environ
            
# Environment Variables, basic:
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")  # Take environment variables from .env file.
env = environ.Env(DEBUG=(bool, False))  # Initialize environment variables.
...
# Environment Variables, callers:
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

...

# ONLY FOR LOCAL DB SOLUTION!!
# Environments custom settings:
DB_CONN_TIMEOUT = 600  # 600 = 10min / 3600 = 1h
if DEBUG:
    DB_CONN_TIMEOUT = 0  # It always reuses the same connection.

# Application definition:
# ABCOO - Engineering Data document about this project:
# TODO: <Product Engineering Data Document link here (not public access)!>
INSTALLED_APPS = [
    # DJANGO DEFAULT SUB-APPS:
    ...
    # DJANGO ADDITIONAL SUB-APPS:
    "django.contrib.postgres",  # Expands the postgres options.
    # THIRD-PARTY SUB-APPS:
    ...
    # APP ORIGINAL SUB-APPS:
    ...
]

...

# Database IF LOCAL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
        "CONN_MAX_AGE": DB_CONN_TIMEOUT,
        "CONN_HEALTH_CHECKS": True,  # Ensure the connection's still alive before reusing it.
    }
}
# Database IF CLOUD:
DATABASES = {
    # The db() method is an alias for db_url().
    'default': env.db_url('DATABASE_URL'),
}