#### Python > Django > Components & Libraries
# Django-Rest-Framework (DRF)

---

Django REST framework is a powerful and flexible toolkit for building Web APIs. Some reasons you might want to use REST framework:

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.

    https://www.django-rest-framework.org/

**More about API:**
- API:          /api/_about.md
- Serializers:  /api/serializers.txt

Data-flow of a real Django REST Framework usage: [/python/web-development/django/useful-sub-apps/pagex/docs/django-with-vue-integration.excalidraw](/python/web-development/django/useful-sub-apps/pagex/docs/django-with-vue-integration.excalidraw)

---
## 1) Install:

**Before:**
1. Assuming you already are in the project environment!

**Installing:**

Using UV:
```bash
uv add djangorestframework
```
Or using PIP:
```bash
python3 -m pip install djangorestframework
```

---
## 2) Integration:

2.1) Open the core `settings.py` in your Django project, and add this lines:

```python
INSTALLED_APPS = [
	# ...
	# DJANGO ADDITIONAL SUB-APPS:
	# ...
	'rest_framework',
]
```

2.2) Still in `settings.py`, add these lines too:

In case you are using JWT, it comes first:
```python
SIMPLE_JWT = {
	# ...
}
```
After that, the Django Rest Framework things:
```python
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		#... or nothing in.
	),
	'DEFAULT_PERMISSION_CLASSES': (
		# Use Django's standard `django.contrib.auth` permissions, or allow read-only
		# access for unauthenticated users!

		#'rest_framework.permissions.IsAuthenticated',
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
	),
}
```

2.3) If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your core `urls.py` file:

```python
from django.urls import include

urlpatterns = [
	# DJANGO:
	#...

	# APIs:
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

	# THIRD-PARTY:
	#...
]
```

==INFO:==
Note that the URL path can be whatever you want!

Example:
- [.../django-rest-framework/example/core/serializers.py](/python/web-development/django/component-libraries/django-rest-framework/example/core/serializers.py)
- [.../django-rest-framework/example/core/urls.py](/python/web-development/django/component-libraries/django-rest-framework/example/core/urls.py)
- [.../django-rest-framework/example/core/views.py](/python/web-development/django/component-libraries/django-rest-framework/example/core/views.py)

---

## DRF POWER-UPS: CREATING APIs
[1-serializers](/python/web-development/django/component-libraries/django-rest-framework/1-serializers.md)

## EXPANDING DJANGO REST FRAMEWORK: JSON WEB TOKEN (JWT) PLUGIN
[0-jwt](/python/web-development/django/component-libraries/json-web-token-SimpleJWT/0-jwt.md)

