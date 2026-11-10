#### Python > Django > API
# Creating API endpoint logic (`views.py`)

---
## Before:
- Assuming you have done the previous steps from this roadmap: [/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)
- Assuming you're using *Django Rest Framework*: [/python/web-development/django/component-libraries/django-rest-framework/0-restframewok](/python/web-development/django/component-libraries/django-rest-framework/0-restframewok.md)
- What are Views: [/python/web-development/django/3-2-views-and-API/\_about](/python/web-development/django/3-2-views-and-API/_about.md)

---

Views are the place where all Django model data is declared to be sent externally, using or not a [api](python/web-development/django/3-2-views-and-API/api.md).

In `/apps/subapp/views.py`:
```python
from rest_framework import viewsets
from . import models
from . import serializers as serial

class ExampleModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoint exposing xxxxxxxxSerializerNamexxxxxxx to Vue Router."""
    
    queryset = models.ExampleModel.objects.prefetch_related("one_related_field_from_foreignkey")
    serializer_class = serial.ExampleModelSerializer
    lookup_field = "slug"
    lookup_value_regex = "[^/]+" # Handles slugs with hyphens or underscores correctly.

    # def get_queryset(self):
    #     """Built-in method to customize even more the qs."""
    #     pass
```
More about `get_queryset()` method: [/python/web-development/django/3-2-views-and-API/method-get_queryset.py](/python/web-development/django/3-2-views-and-API/method-get_queryset.py)

---
## Django API creating roadmap:
[/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)
