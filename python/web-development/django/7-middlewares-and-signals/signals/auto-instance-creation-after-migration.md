#### Python > Django > Signals
# Seeding: how to create an instance automatically after a migration command

---

If you want to automatically populate ([seeding](/dev-concepts/seeding.md)) your database with an initial data, in Django you'll need to use signals. For example, instead of you manually add each data every time you install your app, it already brings a piece of data to use the app as fast as possible.

---
## Approaches:

- Auto seeding (create) a singleton: [/python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton](/python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton.md)
- Auto seeding (create) multiple instances: [/python/web-development/django/7-middlewares-and-signals/signals/seeding-multi-instances](/python/web-development/django/7-middlewares-and-signals/signals/seeding-multi-instances.md)
