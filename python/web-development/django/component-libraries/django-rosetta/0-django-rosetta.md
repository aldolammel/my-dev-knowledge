#### Python > Django > Components & Libraries
# Django-Rosetta

---

Django-Rosetta is a Django third-party package that provides a web-based interface for managing Django translation files (`.po` files).

---
## Before:

1. Assuming you have it installed on the server: [/web-development/components-libraries-server-level/gettext/0-gettext](/web-development/components-libraries-server-level/gettext/0-gettext.md)

---
## 1) Installation:

Using UV:
```bash
uv add django-rosetta
```

Or using PIP:
```bash
xxxxxxxxxxxxxxxxxxxxx
```

---
## 2) Integration:

In `/core/settings.py`:
```python
INSTALLED_APPS = [
	# DJANGO DEFAULT SUB-APPS:
	# ...
	# DJANGO ADDITIONAL SUB-APPS:
	# ...
	“rosetta”,
```

---
## Django web project translation roadmap:
[/python/web-development/django/8-translate-and-internationalization/1-starting-translation](/python/web-development/django/8-translate-and-internationalization/1-starting-translation.md)
