from django.contrib import admin
from django.urls import path, include
from .constants import (
    NAMESPACE_1,
    NAMESPACE_2,
    NAMESPACE_3,
)

urlpatterns = [
    # DJANGO:
    path("admin/", admin.site.urls),
    # THIRD-PARTY:
    # Reserved space...
    # APPLICATION SUB-APPS:
    path("", include(NAMESPACE_1 + ".urls")),
    path(NAMESPACE_3 + "/", include(NAMESPACE_3 + ".urls")),
    path(NAMESPACE_2 + "/", include(NAMESPACE_2 + ".urls")),
    #path(NAMESPACE_2 + "/attacks/", include(NAMESPACE_4 + ".urls")),
]