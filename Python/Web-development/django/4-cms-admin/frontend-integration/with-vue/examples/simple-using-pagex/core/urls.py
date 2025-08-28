# FILE: /my_django_project/core/urls.py
# ...
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from pages.views import PageViewSet, CategoryViewSet
from .settings import (
    # ...
    STATIC_URL,
    STATIC_ROOT,
)

urlpatterns = [
    # DJANGO:
    # ...

    # APIs:
    path("api/", include("apps.pagex.urls")),
    
    # THIRD-PARTY:
    # ...

    # SUB-APPS:
    # Pagex (apps.pagex.urls) needs to be before the Vue fallback!

    # FRONTEND:
    # Only under development:
    # reserved space...
    # Only in Production: this index folder is defined in settings > template > dir
    path("", TemplateView.as_view(template_name="index.html"), name="vue-app"),
    # Only under development:
    # reserved space...
    # Only in Production: this index folder is defined in settings > template > dir
    path("<path:path>", TemplateView.as_view(template_name="index.html"), name="vue-app-paths"),
]

if DEBUG:
    # ...
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)