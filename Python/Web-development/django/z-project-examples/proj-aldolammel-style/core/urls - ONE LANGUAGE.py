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

    # APIs:
    # Reserved space...

    # THIRD-PARTY:
    # Reserved space...

    # SUB-APPS:
    path("", include("apps." + NAMESPACE_1 + ".urls")),
    path(NAMESPACE_3 + "/", include("apps." + NAMESPACE_3 + ".urls")),
    path(NAMESPACE_2 + "/", include("apps." + NAMESPACE_2 + ".urls")),
    #path(NAMESPACE_2 + "/attacks/", include("apps." + NAMESPACE_4 + ".urls")),

    # FRONTEND:
    # Reserved space...
]