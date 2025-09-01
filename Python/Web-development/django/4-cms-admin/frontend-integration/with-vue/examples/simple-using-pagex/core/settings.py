# FILE: /my_django_project/core/settings.py
# ...

import environ  # How to build env() function: /Python/Web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py
from .constants import (
    NAMEAPP_1,
    #...
)

# Environment Variables, basic:
#...
# Environment Variables, callers:
#...
PROD_BASE_URL = env("PROD_BASE_URL")  # Main client's product domain.
BACK_URL1 = env("BACK_URL1")  # Dev env for backend.
BACK_URL2 = env("BACK_URL2")  # Dev env for backend.
FRONT_URL1 = env("FRONT_URL1")  # Dev env for frontend.
FRONT_URL2 = env("FRONT_URL2")  # Dev env for frontend.

INSTALLED_APPS = [
    # DJANGO DEFAULT SUB-APPS:
    # ...
    # DJANGO ADDITIONAL SUB-APPS:
    # ...
    # THIRD-PARTY SUB-APPS:
    'corsheaders',
    'rest_framework',
    # ...
    # APP ORIGINAL SUB-APPS:
    'apps.' + NAMEAPP_1 , # 'apps.pagex'
]

MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",  # Right before CommonMiddleware!
    "django.middleware.common.CommonMiddleware",
    # ...
]

TEMPLATES = [
    {
        "...": "...",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "frontend",  # "frontend/dist"
        ],
        "...": "...",
    },
]

# CORS > CSRF Integration:
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    PROD_BASE_URL,
    BACK_URL1,
    BACK_URL2,
    FRONT_URL1,
    FRONT_URL2,
]
CSRF_TRUSTED_ORIGINS = [
    PROD_BASE_URL,
    BACK_URL1,
    BACK_URL2,
    FRONT_URL1,
    FRONT_URL2,
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    )
}