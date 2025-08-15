# FILE: /my_django_project/core/urls.py
# ...
from pages.views import PageViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter
from .settings import (
    # ...
    STATIC_URL,
    STATIC_ROOT,
)

# API routes
router = DefaultRouter()
router.register('pages', PageViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    # DJANGO:
    # ...
    # THIRD-PARTY:
    path("api/", include(router.urls)),  # All API endpoints under /api/
    # ...
    # APPLICATION SUB-APPS:
    # ...
]

if DEBUG:
    # ...
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)