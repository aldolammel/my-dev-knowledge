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

# FRONTEND:
# Initializing router and its viewsets:
router = DefaultRouter()
router.register('pages', PageViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    # DJANGO:
    # ...
    
    # THIRD-PARTY:
    # ...

    # FRONTEND:
    # Serve Vue.js SPA for all other routes!
    path("api/", include(router.urls)),  # All API endpoints under /api/
    # Only under development:
    # reserved space...
    # Only in Production: this index folder is defined in settings > template > dir
    path("", TemplateView.as_view(template_name="index.html"), name="vue-app"),
    # Only under development:
    # reserved space...
    # Only in Production: this index folder is defined in settings > template > dir
    path("<path:path>", TemplateView.as_view(template_name="index.html"), name="vue-app-paths"),

    # APPLICATION SUB-APPS:
    # ...
]

if DEBUG:
    # ...
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)