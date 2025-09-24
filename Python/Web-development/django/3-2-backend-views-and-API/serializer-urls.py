"""
    DJANGO SERIALIZERS: CREATING API ENDPOINTS

    The URLs.py files create endpoints. 
    The core urls.py serves as the main URL configuration for the entire application. It acts as the central router, directing incoming web requests to the internal, specific and reusable urls.py files.

    >> Whole Django serialization roadmap:
        /Python/Web-development/django/3-2-backend-views-and-API/serializer.txt

"""

# FILE: /apps/my_app/urls.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Using Django Rest Framework:
# /Python/Web-development/django/component-libraries/django-rest-framework/
from rest_framework.routers import DefaultRouter

from .views import ExampleModelViewSet

...

# Initializing router and its viewsets:
router = DefaultRouter()
router.register("example", ExampleModelViewSet)
urlpatterns = router.urls



# FILE: /core/urls.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from django.urls import include

urlpatterns = [
    # DJANGO:
    ...
    # APIs:
    path("api/", include("apps.my_app.urls")),
    # THIRD-PARTY:
    ...
    # SUB-APPS:
    ...
]