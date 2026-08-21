#### Python > Django > Signals > Seeding
# Creating a singleton instance automatically after a migration command

---

## Before:

1. What is singleton: [/dev-concepts/singleton](/dev-concepts/singleton.md)
2. You already created your model class singleton: [/python/web-development/django/3-1-models-database/singleton.py](/python/web-development/django/3-1-models-database/singleton.py)
3. You already create your admin model class for this singleton: [/python/web-development/django/4-cms-admin/singleton.py](/python/web-development/django/4-cms-admin/singleton.py)

---
## 3) In `your_subapp/signals.py`:
```
def create_pagex_singleton(sender, **kwargs):
	"""Function to auto-seed to ensure the PagexSettings singleton exists right after migrate."""
	singleton = sender.get_model("PagexSettings")
	singleton.get_settings()
```

---
## 4) In `your_subapp/apps.py`:
```
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class YourSubappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.your_subapp"

    def ready(self):
        from . import signals
        
        # Auto-seeding for Pagex singleton:
		post_migrate.connect(signals.create_pagex_singleton, sender=self)
```

---
## 5) Done!

Now, every time the `migrate` command is run, Django will execute that function, making sure those instances exist!

---
## Auto seeding for model instances that should be available since the beginning?
[/python/web-development/django/7-middlewares-and-signals/signals/seeding-multi-instances](/python/web-development/django/7-middlewares-and-signals/signals/seeding-multi-instances.md)
