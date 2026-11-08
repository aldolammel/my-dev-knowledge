from rest_framework.routers import DefaultRouter

# from apps.subappname.views import SomethingViewSet

# CORE API ENDPOINTS DECLARATION:
# Each route can be tested using: http://localhost:8000/api/<somethingmodelnameinplural>/<view_lookup_field>/
router = DefaultRouter()
# router.register("api/<somethingmodelnameinplural>", SomethingViewSet)
# ...

urlpatterns = router.urls
