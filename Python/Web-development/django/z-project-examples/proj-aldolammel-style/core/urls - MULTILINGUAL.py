from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from .consts import (
    NAMEAPP_1,
    NAMEAPP_2,
    NAMEAPP_3,
)

urlpatterns = i18n_patterns(
    # DJANGO:
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    # THIRD-PARTY:
    path("rosetta/", include("apps.rosetta.urls")),

    # FRONTEND:
    # Reserved space...
    
    # APPLICATION SUB-APPS:
    path("", include("apps." + NAMEAPP_1 + ".urls")),
    path(NAMEAPP_3 + "/", include("apps." + NAMEAPP_3 + ".urls")),
    path(NAMEAPP_2 + "/", include("apps." + NAMEAPP_2 + ".urls")),
    #path(NAMEAPP_2 + "/attacks/", include("apps." + NAMEAPP_4 + ".urls")),
    # Crucial to be "True" for the class 'UserLanguageMiddleware' in 'core/middlewares.py':
    prefix_default_language=True,
)
