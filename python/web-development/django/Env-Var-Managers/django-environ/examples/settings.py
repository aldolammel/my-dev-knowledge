# DONT USE THIS. THIS IS JUST AN EXAMPLE FILE.
# FILE: /core/settings.py

# Django Env Var Manager:
import environ

# Environment Variables, basic:
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")  # Take environment variables from .env file.
env = environ.Env(DEBUG=(bool, False))  # Initialize environment variables.
# Environment Variables, callers:
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Environments custom settings:
DB_CONN_TIMEOUT = 600  # 600 = 10min / 3600 = 1h
if DEBUG:
    DB_CONN_TIMEOUT = 0  # It always reuses the same connection.
...

# In case the db is running on a cloud service:
DATABASES = {
    # The db() method is an alias for db_url().
    'default': env.db_url('DATABASE_URL'),
}



# If you need a deeper look into this settings.py file, check my model:
# /python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py