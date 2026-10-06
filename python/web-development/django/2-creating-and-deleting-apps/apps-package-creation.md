#### Python > Django > Sub-apps
# Creating the `apps` package folder

---

This folder will store all your sub-apps, respecting the best-practice for [Django project folder structure](/python/web-development/django/django-project-folder-structure.md).

---
## Before:

1. Make sure you are using the terminal in the project root.

---
## 1) Create the sub-app package folder:

In this new folder, all project's sub-apps will be installed in here:
```bash
mkdir -p apps
```

---
## 2) Create the dunder init:

Without this dunder file, Django wouldn't know `apps` folder is a package of sub-apps:
```bash
cd apps
# Creating the file:
touch __init__.py
# And keep this new file empty once the file existance if enough for Django flag it as a package.
```

Done.

---
## How to create a sub-app:
[/python/web-development/django/2-creating-and-deleting-apps/creating](/python/web-development/django/2-creating-and-deleting-apps/creating.md)
