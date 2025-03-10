# core/middlewares.py

from django.utils import translation
from django.conf import settings


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.language:
            # Set language from user profile
            language = request.user.language.code
        else:
            # Fallback to cookie or accept header
            language = (
                request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, None) or request.LANGUAGE_CODE
            )

        translation.activate(language)
        request.LANGUAGE_CODE = language

        response = self.get_response(request)

        # If anonymous, store the language in a cookie
        if not request.user.is_authenticated:
            response.set_cookie(
                settings.LANGUAGE_COOKIE_NAME, language, max_age=settings.LANGUAGE_COOKIE_AGE
            )

        return response

        """
            DONT FORGET TO REGISTER THE MIDDLEWARE IN THE SETTINGS.PY:
            
            MIDDLEWARE = [
                ...
                'django.middleware.locale.LocaleMiddleware',
                'core.middlewares.UserLanguageMiddleware',  # Advanced geolocation feature. 
                ...
            ]
        
        """
