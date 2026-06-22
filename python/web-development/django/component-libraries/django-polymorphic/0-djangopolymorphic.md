#### Python > Django > Components & Libraries
# Django-Polymorphic

---

**Before:**
1. What is Polymorphism: [dev-concepts/polymorphism](dev-concepts/polymorphism.md)

The *Django-Polymorphic* builds on top of the standard Django model inheritance. It makes using inherited models easier. When a query is made at the base model, the inherited model classes are returned.

https://django-polymorphic.readthedocs.io/en/latest/

E.g.
- Basic: [/python/web-development/django/component-libraries/django-polymorphic/example/basic.py](/python/web-development/django/component-libraries/django-polymorphic/example/basic.py)
- Real case: [/python/web-development/django/component-libraries/django-polymorphic/example/real-case.py](/python/web-development/django/component-libraries/django-polymorphic/example/real-case.py)

---

## 1) INSTALLING:

**Before:**
1. Assuming you already are in the project environment!

**Install as a project dependency:**

LINUX:
PIP:
```
pip install django-polymorphic
```
Or UV:
```
uv add django-polymorphic
```

WINDOWS:
```
soon...
```


---

## 2) INTEGRATING:

In your Django core settings:

```
INSTALLED_APPS = [
	# DJANGO DEFAULT SUB-APPS:
	'django.contrib.contenttypes',
	# THIRD-PARTY SUB-APPS:
	'polymorphic',
]
```

---
## EXAMPLES:
./example/basic.py
./example/real-case.py




