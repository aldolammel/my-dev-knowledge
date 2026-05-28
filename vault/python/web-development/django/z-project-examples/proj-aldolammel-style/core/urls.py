from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

# DJANGO BASIC:
urlpatterns = [
    # CMS:
    path("admin/", admin.site.urls),
    path("admin", RedirectView.as_view(url="/admin/")),
    path("wp-admin/", RedirectView.as_view(url="/admin/")),
    path("wp-admin", RedirectView.as_view(url="/admin/")),
    # SUB-APPs, APIs:
    # Reserved space...
]

# DJANGO > ONLY WHEN DEBUG TRUE:
# Reserved space...

# THIRD-PARTY:
# Reserved space...

# FRONTEND:
# Reserved space...
