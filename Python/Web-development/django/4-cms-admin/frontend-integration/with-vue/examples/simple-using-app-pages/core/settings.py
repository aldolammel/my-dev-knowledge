# FILE: /my_django_project/core/settings.py
# ...

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
    # ...
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
            BASE_DIR / "frontend/dist",
        ],
        "...": "...",
    },
]

# CORS > CSRF Integration:
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://MAIN-DOMAIN-CLIENT.com",
    "http://localhost:8000",  # Dev env for Django;
    "http://127.0.0.1:8000",  # Dev env for Django;
    "http://localhost:5173",  # Dev env for Vue;
    "http://127.0.0.1:5173",  # Dev env for Vue;
]
CSRF_TRUSTED_ORIGINS = [
    "https://MAIN-DOMAIN-CLIENT.com",
    "http://localhost:8000",  # Dev env for Django;
    "http://127.0.0.1:8000",  # Dev env for Django;
    "http://localhost:5173",  # Dev env for Vue;
    "http://127.0.0.1:5173",  # Dev env for Vue;
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.IsAuthenticated',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    )
}