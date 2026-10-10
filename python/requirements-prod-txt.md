#### Python
# `requirements-prod.txt` file

---

==Attention!==
Case you are in [Dev environment](/dev-concepts/environment-development-dev.md) (or [Testing one](/dev-concepts/environment-testing-qa.md)), you don't need to install dependencies listed in this file at all. 
Remember: those dependencies that should be installed every project environment are called "core dependencies" and they should be listed in [requirements.txt](/python/requirements-txt.md) file!

---

It's a variant of [requirements.txt](/python/requirements-txt.md) that is focused only in dependencies that must be installed in [Production environment](/dev-concepts/environment-production-prod.md).

E.g. of a prod-only dependency in a Python web project:
- gunicorn

---
## Creating a `requirements-prod.txt` file:
E.g.
```txt
-r requirements.txt
gunicorn==23.0.0
django-storages==1.14.4
sentry-sdk==2.14.0
```
Important to notice the dependencies used as example, they got their versions pinned but you can use >= too. 

---
## Installing all core + prod dependencies in a row:
**Before:**
- Make sure in the project root folder you have the requirement file.

Installing all Core + Prod dependencies in a row:
```bash
pip install -r requirements-prod.txt
```

---
