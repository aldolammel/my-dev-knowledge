#### Python > Django > Project types
# Discovery in Django

---

Group of action to figure out a Django project settings and features:

---
## Before:

1. Assuming you already complete the Python discovery: [/python/0-new-project/discovery-python](/python/0-new-project/discovery-python.md)
2. Assuming you already know which database this product uses: [/database/00-new-project/discovery-database](/database/00-new-project/discovery-database.md)

---
## 1) Project installed dependencies:

**Using UV:**
```bash
uv pip list
# And take a note!
```
Checking how outdated they are:
```bash
uv tree --outdated --depth 1 --all-groups
# This shows each direct dependency, including dev groups, next to its latest available version.
```

.....

**Using Python/PIP:**
```
xxxxxxxxx
```

---
## 2) Test current Django:
[/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---
## 3) (If applicable) To update/upgrade:

==CRITICAL==
Any update/upgrade is NOT recommended until the discovery of the whole project layers (back-end + front-end) to be finished.

[/python/web-development/django/0-new-project/update-django-version](/python/web-development/django/0-new-project/update-django-version.md)

---
## 4) Discovery of project's front-end framework:

- If it runs **Django Template**: 
- If it runs **Vue**: [/javascript/web-development/frontend/vue/0-new-project/discovery-vue](/javascript/web-development/frontend/vue/0-new-project/discovery-vue.md)
- If it runs **React**: xxxxxx
- If it runs **Angular**: xxxxx
