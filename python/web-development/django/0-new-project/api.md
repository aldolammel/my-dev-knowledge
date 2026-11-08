#### Python > Django > Project types
# API with Django

---

==Ultra simple solution!==
If you're creating a project just to build up an API, be sure you will use *Django* as solution just 'cause the system where the API will run already use *Django* or this API demands authentication, admin interface, or ORM. Otherwise, consider a micro-framework like *Flask*: [/python/web-development/flask/0-new-project/api](/python/web-development/flask/0-new-project/api.md)

---
## Before:
1. [ ] What is an API: [/api/\_about](/api/_about.md)
2. [ ] What is a serializer: [/dev-concepts/serialization](/dev-concepts/serialization.md)
3. [ ] The data-flow when Django's using serializers:
![](python/web-development/django/django-dataflow-simplified-by-aldolammel.png)
4. [ ] Django: assuming you have your Django project running with its database!
5. [ ] Toolkit: assuming you have already an Web API toolkit like *Django REST Framework*: [/python/web-development/django/component-libraries/django-rest-framework/0-restframewok](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md)

---
## Creating the API
If you need ideas, check this out: [/api/\_how-to-plan-an-api](/api/_how-to-plan-an-api.md)
### 1) Converting the model data to JSON (`/apps/subapp/serializers.py`)
- [ ] Creating a Serializer-class tied with the Model-class where the data belongs: [/python/web-development/django/3-2-views-and-API/\_serializer-class-model](/python/web-development/django/3-2-views-and-API/_serializer-class-model.md)
### 2) Creating the endpoint logic (`/apps/subapp/views.py`)
- [ ] Developing which serialized data must be sent/released externally: [python/web-development/django/3-2-views-and-API/view-sending-data](python/web-development/django/3-2-views-and-API/view-sending-data.md)
### 3) Declaring the endpoints (`/apps/subapp/urls.py`):
- [ ] Pointing incoming web requests to the right `views.py` class: [python/web-development/django/3-2-views-and-API/urls-creating-endpoint](python/web-development/django/3-2-views-and-API/urls-creating-endpoint.md)
### 4) Adding a friendly JSON link preview on the CMS (`/apps/subapp/admin.py`):
- [ ] Creating a JSON link for visual inspection on CMS: [python/web-development/django/3-2-views-and-API/admin-json-preview](python/web-development/django/3-2-views-and-API/admin-json-preview.md)
### 5) Test it!
[/python/web-development/django/\_running-app](/python/web-development/django/_running-app.md)

---




