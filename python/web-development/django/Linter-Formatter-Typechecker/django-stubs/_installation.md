#### Python > Django > Linter, Formatter & Type checker
# Django Stubs

---

It's a package contains type stubs and a custom MyPy plugin to provide more precise static types and type inference for Django framework. Django uses some Python "magic" that makes having precise types for some code patterns problematic. This is why we need this project. The final goal is to be able to get precise types for most common patterns.

https://github.com/typeddjango/django-stubs

---
## 1) Installing:

- [ ] **Before:**
	1. Your Python Type-Checker is one of them:
		- Python MyPy: [python/linter-formatter-typechecker/MyPy/_installation](python/linter-formatter-typechecker/MyPy/_installation.md)
		- Or Python PyRight: [/python/linter-formatter-typechecker/PyRight/installation](/python/linter-formatter-typechecker/PyRight/installation.txt)

- [ ] **1.1) Installing:**

For MyPy compatibility:
Using UV:
```bash
uv add --group dev 'django-stubs[compatible-mypy]'
```
Or using PIP:
```bash
$ xxxxxxxxxxxx
# Include this in the pyproject.toml dev dependencies:
	xxxxxxxxxxx
```

For PyRight compatibility:
Using UV:
```bash
uv add --group dev 'django-stubs[compatible-pyright]'
```
Or using PIP:
```bash
$ xxxxxxxxxxxx
# Include this in the pyproject.toml dev dependencies:
	xxxxxxxxxxx
```

- [ ] **1.2) (If applicable) Extending type checker:**
	 - Are you using Django Rest Framework (DRF)? If so, considering to extend the type checker to serializers, viewsets, etc: [DRF Stubs](/python/web-development/django/Linter-Formatter-Typechecker/drf-stubs/installation.md)

---
## 2) Integration:

- [ ] **Before:**
	1. Assuming you already got the `pyproject.toml` in your project: [python/pyproject-toml](python/pyproject-toml.md)

- [ ] **2.1) Include/edit these lines in your `pyproject.toml`:**
	- For MyPy: [/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-mypy.toml](/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-mypy.toml)
	- Or for PyRight: [/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-pyright.toml](/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-pyright.toml)

---

