#### JavaScript > Front-end > Vue > Project types > Initial roadmap
# Project folder structure: Vue with Django as back-end

---

This roadmap is just for information, you don't need to do anything.

==CRITICAL==:
Never install Vue in Django's `/templates/` folder! It would create process rendering conflicts.

---
## Before:
- Keep in mind which Vue app architecture you wanna build up: [/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture](/javascript/web-development/frontend/vue/vue-knowledge/vue-application-architecture.md)
- Assuming your Django folder is at least basically structured: [/python/web-development/django/django-project-folder-structure](/python/web-development/django/django-project-folder-structure.md)

---
## 1) Get to know specifics folder structure based on the app architecture:
==Currently, there is no folder difference between app architectures!==

- 1A) For MPA architecture.
- 1B) For SPA architecture.

......................................

### 1A) For MPA architecture
```python
my_project/         # Django root / back-end root / project root
├── ...
└── frontend/       # Vue root / front-end root
```

......................................

### 1B) For SPA architecture
```python
my_project/         # Django root / back-end root / project root
├── ...
└── frontend/       # Vue root / front-end root
```

---
## 2) Vue `/frontend/` full folder structure:
Just take a look, but ==DON'T== create anything once it'll be created later: [/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure](/javascript/web-development/frontend/vue/vue-knowledge/1-vue-structure.md)

---
## 3) Return to the previous Vue roadmap:
Once you have decided with structure to follow, return to the main guide for Vue installation you are following!

---


