
# ENVIRONMENT VARIABLES: DJANGO PROJECTS

'''
Those variables linked exclusively with the environment where the code is running. It's a safe option to save
keys, passwords, tokens and other information that must be unique for each environment.
'''

    # 1) Install this module in your project:
        # $ pip install django-environ

    # 2) Create a file called ".env" on the project root (same place of 'manage.py' file):
        # model: /Environment-Variables/

    # 3) In the Django settings.py file, add these lines:

        
from pathlib import Path
import environ

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')

# Initialize environment variables
env = environ.Env(
    # Set casting, default value
    DEBUG=(bool, False)
)

# Quick-start development settings - unsuitable for production
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ADMIN_EMAIL = env('ADMIN_EMAIL')

# Allowed hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])  # type: ignore

if DEBUG:
    print("SECRET_KEY:", env('SECRET_KEY', default='Not Set'))  # type: ignore
    print("ALLOWED_HOSTS:", env('ALLOWED_HOSTS', default='Not Set'))  # type: ignore
    #print("DATABASE_URL:", env('DATABASE_URL', default='Not Set'))  # type: ignore


# Database
# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    # The db() method is an alias for db_url().
    'default': env.db(),
}

            

    # 4) Crucial: make sure if you want or not the .gitignore file ignoring the .env file;
