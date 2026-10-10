#### Python
# `requirements.txt` file

---

The `requirements.txt` is a simple flat text file listing exact package names and pinned versions used by [PIP](/python/package-manager/pip/_install.md) to install dependencies for a specific environment. All dependencies listed in this file are the "core" ones, those that the project mandatorily depends them installed to be running.

E.g. of a core dependency in a Python web project:
- django.

==Critical==
Never include non-core dependencies in this file. Use its variants to be clear the goal of every dependency:
- For development only: [requirements-dev-txt](python/requirements-dev-txt.md)
- For production only: [requirements-prod-txt](/python/requirements-prod-txt.md)

---
## Creating a `requirements.txt` file:
E.g.
```txt
Django==5.2.18
psycopg2-binary==2.9.10
```
Important to notice the dependencies used as example, they got their versions pinned but you can use >= too. 

---
## Installing all core dependencies in a row:

**Before:**
- Make sure in the project root folder you have the requirement file.

Installing all Prod dependencies in a row:
```bash
pip install -r requirements.txt
```

---
## Creating this file for a project:
[/python/package-manager/pip/creating-requirements-of-project](/python/package-manager/pip/creating-requirements-of-project.md)
## Converting a requirements file to a `pyproject.toml`:
[/python/package-manager/uv/converting-non-uv-project-in-one](/python/package-manager/uv/converting-non-uv-project-in-one.md)
