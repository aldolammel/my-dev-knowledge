#### Python
# `requirements-dev.txt` file

---

==Attention!==
Case you are in [Prod](/dev-concepts/environment-production-prod.md) (or [Staging one](/dev-concepts/environment-staging-uat.md)), you don't need to install dependencies listed in this file at all. 
Remember: those dependencies that should be installed every project environment are called "core dependencies" and they should be listed in [requirements.txt](/python/requirements-txt.md) file!

---

It's a variant of [requirements.txt](/python/requirements-txt.md) that is focused only in tools used during [local development](/dev-concepts/environment-development-dev.md) and [testing](/dev-concepts/environment-testing-qa.md).

E.g. of a dev-only dependency in a Python web project:
- pytest-django

---
## Creating a `requirements-dev.txt` file:
E.g.
```txt
-r requirements.txt
pytest-django==4.9.0
black==24.3.0
flake8==7.0.0
```
Important to notice the dependencies used as example, they got their versions pinned but you can use >= too. 

---
## Installing all core + dev dependencies in a row:

**Before:**
- Make sure in the project root folder you have the requirement file.

Installing all Core + Dev dependencies in a row:
```bash
pip install -r requirements-dev.txt
```

---

