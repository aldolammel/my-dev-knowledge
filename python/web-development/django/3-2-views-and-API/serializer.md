#### Python > Django > Structure
# Serializers.py

---

**Before:**
1. What is it: [/dev-concepts/serialization](/dev-concepts/serialization.md)

---
## Creating the API

**Before:**
1. Django: assuming you have your Django project running with its database!
2. Toolkit: assuming you have already an Web API toolkit like Django REST Framework - [/python/web-development/django/component-libraries/django-rest-framework/0-restframewok](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md)

**1) Data conversion (my_app/serializers.py):**

Creating a Serializer-class (API) tied with the Model-class where the data belongs: [/python/web-development/django/3-2-views-and-API/\_serializer-class-model.py](/python/web-development/django/3-2-views-and-API/_serializer-class-model.py)

**2) API logic, sending data (my_app/views.py):**

Declaring which serialized data must be released externally: [/python/web-development/django/3-2-views-and-API/serializer-view-sending-data.py](/python/web-development/django/3-2-views-and-API/serializer-view-sending-data.py)

Or Sending/Receiving data:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

**3) URL routing (my_app/urls.py):**

Direct the incoming web requests, pointing them to the right Views.py class: [/python/web-development/django/3-2-views-and-API/serializer-urls.py](/python/web-development/django/3-2-views-and-API/serializer-urls.py)

**4) Visualization on CMS (my_app/admin.py):**

[/python/web-development/django/3-2-views-and-API/serializer-admin-json-preview.py](/python/web-development/django/3-2-views-and-API/serializer-admin-json-preview.py)

**5) Test it!**


