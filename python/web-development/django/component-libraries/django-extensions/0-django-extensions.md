#### Python > Django > Components & Libraries
# Django-Extensions

---

Django-extensions is a popular Python library for Django that provides a collection of custom extensions to enhance your development workflow. Think of it as a toolbox filled with a wide variety of useful utilities (mostly new management commands) that help you perform common tasks faster and more efficiently than with plain Django.

---
## 1) Installation:

**Before:**
1. Assuming you already are in the project environment!

**1.1) Installing:**

Using UV:
```bash
uv add --group dev django-extensions
```

Or use pip:
```bash
python3 -m pip install django-extensions
```
And then add manually this to the dev sub-group in pyproject.toml file!            

---
## 2) Integration:
And include the app to INSTALLED_APPS on Django settings!
```python
INSTALLED_APPS = [
	# DJANGO DEFAULT SUB-APPS:
	# ...
	# DJANGO ADDITIONAL SUB-APPS:
	"django_extensions"  # to use the show_url command in shell!
	# ...
]
```

---

