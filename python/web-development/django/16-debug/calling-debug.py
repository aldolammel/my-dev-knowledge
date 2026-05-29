


# This way, all Django app knows the settings address:
from django.conf import settings as stgs

# Good practice to store DEBUG (from Environment Variables) in settings.py:
if stgs.DEBUG:
    print()