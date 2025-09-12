# DONT USE THIS. THIS IS JUST AN EXAMPLE FILE.

# settings.py
import environ

# Initialize the library
env = environ.Env(
    # Set casting and default values
    DEBUG=(bool, False),
)

# Read the .env file
environ.Env.read_env()

# False if DEBUG not found in .env or not 'on'
DEBUG = env('DEBUG')

# Raises an error if SECRET_KEY not found
SECRET_KEY = env('SECRET_KEY')

# Parse a complex URL into a Django config dictionary
DATABASES = {
    # The 'default' key is parsed from the DATABASE_URL environment variable.
    # If the URL doesn't exist, it raises an error.
    'default': env.db(),
}

# Parse a cache URL (e.g., for Redis)
CACHES = {
    'default': env.cache_url(),
}