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
...

# In case the db is running on a cloud service:
DATABASES = {
    # The db() method is an alias for db_url().
    'default': env.db_url('DATABASE_URL'),
}