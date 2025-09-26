# FILE: /my_django_project/apps/pagex/urls.py

from rest_framework.routers import DefaultRouter
from .views import (
    PagexPageViewSet,
    PagexMenuViewSet,
)


# NAMESPACE
app_name = 'pagex'

# FRONTEND:
# Initializing router and its viewsets:
router = DefaultRouter()
router.register('pages', PagexPageViewSet)
router.register('menus', PagexMenuViewSet)

urlpatterns = []
