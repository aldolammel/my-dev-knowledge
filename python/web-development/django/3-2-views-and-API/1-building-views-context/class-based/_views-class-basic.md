#### Python > Django > Views > Class-based
# Using basic inherit

---

With a basic view inherit, you are able to create your own view-class-based with all the potential offered by classes in `views.py`. But with this one, you'd write more code!

It handles the basic HTTP request methods (get, post, etc). Perfect when you need to implement custom logic for handling HTTP requests that don't fit the standard patterns provided by other CBVs.

---
## Who inherit this view class:
All other view-classes!

---
## Example
```python
from django.views import View

class MyOwnTestView(View):  # This 'View' in classname is a convention.
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, this is a GET request")
    def post(self, request, *args, **kwargs):
        return HttpResponse("Hello, this is a POST request")
```

---
## How to use (full implementation example):
[/python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/view-class-basic-usage](/python/web-development/django/3-2-views-and-API/1-building-views-context/class-based/view-class-basic-usage.md)
