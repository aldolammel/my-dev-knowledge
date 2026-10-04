TYPE CHECKER DJANGO STUBS: INSTALLATION AND INTEGRATION

    >> WHAT IS IT:
        ./_about.md


---
## INSTALLING:

### Before
1. Your Python Type-Checker is one of them:
	- Python MyPy: [/python/linter-formatter-typechecker/MyPy/installation](/python/linter-formatter-typechecker/MyPy/installation.md)
	- Or Python PyRight: [/python/linter-formatter-typechecker/PyRight/installation](/python/linter-formatter-typechecker/PyRight/installation.txt)

### 1) Install

**For MyPy compatibility:**

Using UV:
```bash
uv add --optional dev 'django-stubs[compatible-mypy]'
```
Or using PIP:
```
$ xxxxxxxxxxxx
# Include this in the pyproject.toml dev dependencies:
	xxxxxxxxxxx
```

**For PyRight compatibility:**

Using UV:
```bash
uv add --optional dev 'django-stubs[compatible-pyright]'
```
Or using PIP:
```
$ xxxxxxxxxxxx
# Include this in the pyproject.toml dev dependencies:
	xxxxxxxxxxx
```

---
## INTEGRATING:

### Before
1. Assuming you already got the `pyproject.toml` in your project: [/python/web-development/pyproject.toml](/python/web-development/pyproject.toml)
### 1) Include/edit these lines in your `pyproject.toml`
- For MyPy: [/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-mypy.toml](/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-mypy.toml)
- Or for PyRight: [/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-pyright.toml](/python/web-development/django/Linter-Formatter-Typechecker/django-stubs/pyproject-for-pyright.toml)

---

