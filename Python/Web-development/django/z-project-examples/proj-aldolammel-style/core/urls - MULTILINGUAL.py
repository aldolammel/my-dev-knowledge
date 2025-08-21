from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from .constants import (
    NAMESPACE_1,
    NAMESPACE_2,
    NAMESPACE_3,
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
    path("", include("apps." + NAMESPACE_1 + ".urls")),
    path(NAMESPACE_3 + "/", include("apps." + NAMESPACE_3 + ".urls")),
    path(NAMESPACE_2 + "/", include("apps." + NAMESPACE_2 + ".urls")),
    #path(NAMESPACE_2 + "/attacks/", include("apps." + NAMESPACE_4 + ".urls")),
    # Crucial to be "True" for the class 'UserLanguageMiddleware' in 'core/middlewares.py':
    prefix_default_language=True,
)
