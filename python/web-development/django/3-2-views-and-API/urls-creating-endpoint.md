#### Python > Django > API
# Creating API endpoint route (`urls.py`)

---
## Before:
- Assuming you have done the previous steps from this roadmap: [/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)
- Assuming you're using *Django Rest Framework*: [/python/web-development/django/component-libraries/django-rest-framework/0-restframewok](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md)

---
## 1) In `/apps/subapp/urls.py`, nothing need to be added or changed!

---
## 2) Include or make sure you already got API configured on the core:
### 2.1) `/core/urls.py`
This configure right below you need just once for your entire application, no matter how many sub-apps will used that.
```python
# CORE ENDPOINTS DECLARATION:
urlpatterns = [
    # ...
    # APPLICATION:
    # ...
    # OTHERS:
	# Remember to check the /urls_api.py!
    path("", include("core.urls_api")),
    # ...
]
```
### 2.2) `/core/urls_api.py`
Create this file or edit it, declaring the [existing endpoint logic](python/web-development/django/3-2-views-and-API/view-sending-data.md) (view class).
```python
from rest_framework.routers import DefaultRouter
from apps.subappname.views import SomethingViewSet

# CORE API ENDPOINTS DECLARATION:
# Each route can be tested using: http://localhost:8000/api/<somethingmodelnameinplural>/<view_lookup_field>/
router = DefaultRouter()
router.register("api/<somethingmodelnameinplural>", SomethingViewSet)
# ...

urlpatterns = router.urls
```

---
## 3) (If applicable) Test it:
**Before:**
- [Run Django's app](/python/web-development/django/_running-app.md)

http://localhost:8000/api/subappnamehere/

---
## Django serialization roadmap:
[/python/web-development/django/3-2-views-and-API/serializer](/python/web-development/django/3-2-views-and-API/serializer.md)