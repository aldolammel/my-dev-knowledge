"""
    DJANGO > CALLING DEBUG ENVIRONMENT VAR:

    More info:
        /python/web-development/django/16-debug/1-implementing.md
"""


# This way, all Django app knows the settings address:
from django.conf import settings

# Good practice to store DEBUG (from Environment Variables) in settings.py:
if settings.DEBUG:
    print()