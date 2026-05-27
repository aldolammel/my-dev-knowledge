from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# You can now open the API in your browser at http://127.0.0.1:8000/, and view your new 'users' API.
# If you use the login control in the top right corner you'll also be able to add, create and
# delete users from the system.