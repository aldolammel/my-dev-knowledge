
# ENVIRONMENT VARIABLES: DJANGO PROJECTS

'''
Those variables linked exclusively with the environment where the code is running. It's a safe option to save
keys, passwords, tokens and other information that must be unique for each environment.
'''

    # 1) Install this module in your project:
        # $ pip install django-environ

    # 2) Create a file called ".env" on the project root (same place of 'manage.py' file):
        # model: /31-Environment-Variables/.env

    # 3) In the Django settings.py file, add these lines:

        import os
        import environ
        from pathlib import Path

        # Build paths inside the project like this: BASE_DIR / 'subdir'.
        BASE_DIR = Path(__file__).resolve().parent.parent

        # Initialize environment variables
        env = environ.Env(
            # Set casting, default value
            DEBUG=(bool, False)
        )
        environ.Env.read_env(env_file=os.path.join(BASE_DIR, '.env'))

        # Quick-start development settings - unsuitable for production
        SECRET_KEY = env('SECRET_KEY')
        DEBUG = env('DEBUG')
        if DEBUG:
            print("SECRET_KEY:", env('SECRET_KEY', default='Not Set')) # type: ignore
            print("ALLOWED_HOSTS:", env('ALLOWED_HOSTS', default='Not Set')) # type: ignore
            print("DATABASE_URL:", env('DATABASE_URL', default='Not Set')) # type: ignore

        # Allowed hosts
        ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

        # Database
        DATABASES = {
            'default': env.db(),
        }


    # 4) Crucial: make sure if you want or not the .gitignore file ignoring the .env file;
