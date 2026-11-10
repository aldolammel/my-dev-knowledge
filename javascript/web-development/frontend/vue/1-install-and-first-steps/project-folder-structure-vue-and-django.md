#### JavaScript > Vue
# Project folder structure: Vue with Django as back-end

---

==CRITICAL==:
Don't install Vue in Django's templates folder! It would create process rendering conflicts.

---
## Before:
- Define which type of Vue project you wanna create - SPA or MPA: [/javascript/web-development/frontend/vue/vue-knowledge/SPA-vs-MPA](/javascript/web-development/frontend/vue/vue-knowledge/SPA-vs-MPA.md)
- Assuming your Django folder is already structured: [/python/web-development/django/django-project-folder-structure](/python/web-development/django/django-project-folder-structure.md)

---
## 1) Before to install Vue, check the options for your project folder's structure:

- 1A) For Multi-Page-App (MPA) projects.
- 1B) For Single-Page-App (SPA) projects.

......................................

### 1A) Recommendation for MPA project
```python
my_project/         # If needed, check the Django folder structure!
└── frontend/
```
Vue project folder (e.g. `/frontend/`) must be created in the root of Django project folder (e.g. `/my_project/frontend/`).

......................................

### 1B) Recommendation for SPA project
```python
my_project/         # If needed, check the Django folder structure!
└── frontend/
```
Vue project folder (e.g. `/frontend/`) must be created in the root of Django project folder (e.g. `/my_project/frontend/`).

---
## 2) Vue `/frontend/` folder structure:
[/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure](/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure.md)

---
## 3) Once you have decided with structure to follow, return to the main guide for Vue installation you are following!

---


