#### Python > Django > Structure
# `serializers.py` roadmap

---

**Before:**
1. What is an API: [/api/\_about](/api/_about.md)
2. What is a serializer: [/dev-concepts/serialization](/dev-concepts/serialization.md)
3. The data-flow when Django's using serializers:
![](python/web-development/django/django-dataflow-simplified-by-aldolammel.png)

---
## Creating the API

### Before
1. [ ] Django: assuming you have your Django project running with its database!
2. [ ] Toolkit: assuming you have already an Web API toolkit like Django REST Framework - [/python/web-development/django/component-libraries/django-rest-framework/0-restframewok](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md)
3. [ ] How to plan your API: [/api/\_how-to-plan-an-api](/api/_how-to-plan-an-api.md)

### 1) Data conversion (`/apps/subapp/serializers.py`)
- [ ] Creating a Serializer-class (API) tied with the Model-class where the data belongs: [/python/web-development/django/3-2-views-and-API/\_serializer-class-model](/python/web-development/django/3-2-views-and-API/_serializer-class-model.md)

### 2) API logic, sending data (`/apps/subapp/views.py`)
- [ ] Declaring which serialized data must be released externally: [/python/web-development/django/3-2-views-and-API/serializer-view-sending-data.py](/python/web-development/django/3-2-views-and-API/serializer-view-sending-data.py)

Or Sending/Receiving data:

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### 3) URL routing (`/apps/subapp/urls.py`):
- [ ] Direct the incoming web requests, pointing them to the right Views.py class: [/python/web-development/django/3-2-views-and-API/serializer-urls.py](/python/web-development/django/3-2-views-and-API/serializer-urls.py)

### 4) Visualization on CMS (`/apps/subapp/admin.py`):
[/python/web-development/django/3-2-views-and-API/serializer-admin-json-preview.py](/python/web-development/django/3-2-views-and-API/serializer-admin-json-preview.py)

### 5) Test it!


