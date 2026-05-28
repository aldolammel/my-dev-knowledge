

JWT: VERIFYING HMAC SIGNED TOKENS


    You can also include a route for Simple JWT’s TokenVerifyView if you wish to allow API users to
    verify HMAC-signed tokens without having access to your signing key.
    The TokenVerifyView provides no information about a token’s fitness for a particular use, it
    only verifies if a token is valid or not, and return a 200 or 401 status code respectively:


        from rest_framework_simplejwt.views import TokenVerifyView

        urlpatterns = [
            //...
            path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
            //...
        ]


    >> FOR TRANSLATIONS:
        If you wish to use localizations/translations, simply add rest_framework_simplejwt
        to INSTALLED_APPS.