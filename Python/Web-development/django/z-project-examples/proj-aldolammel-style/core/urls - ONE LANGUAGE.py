from django.contrib import admin
from django.urls import path, include
from .consts import (
    NAMEAPP_1,
    NAMEAPP_2,
    NAMEAPP_3,
)

urlpatterns = [
    # DJANGO:
    path("admin/", admin.site.urls),

    # APIs:
    # Reserved space...

    # THIRD-PARTY:
    # Reserved space...

    # SUB-APPS:
    path("", include("apps." + NAMEAPP_1 + ".urls")),
    path(NAMEAPP_3 + "/", include("apps." + NAMEAPP_3 + ".urls")),
    path(NAMEAPP_2 + "/", include("apps." + NAMEAPP_2 + ".urls")),
    #path(NAMEAPP_2 + "/attacks/", include("apps." + NAMEAPP_4 + ".urls")),

    # FRONTEND:
    # Reserved space...
]