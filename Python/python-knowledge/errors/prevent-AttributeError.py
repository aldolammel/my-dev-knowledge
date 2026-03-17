
"""
    ATTRIBUTE ERROR PREVENTION

    Let's say you have a custom feature in your application but you forgot to declare some settings in the settings.py file. If you try to access those settings, you'll get an AttributeError. To prevent this, you can use the getattr() function to provide a default value if the setting is not found.

    Those missing variables:
        PAGEX_BACK_URL
        PAGEX_FRONT_URL
        PAGEX_PROD_URL
"""

# Prevents AttributeError if the dev forgot to declare them:
back_url = getattr(stgs, "PAGEX_BACK_URL", None)
front_url = getattr(stgs, "PAGEX_FRONT_URL", None)
prod_url = getattr(stgs, "PAGEX_PROD_URL", None)

if not back_url or not front_url or not prod_url:
    e = "Some required Pagex variables are missing in your settings.py."
    print(e)
    raise ImproperlyConfigured(e)