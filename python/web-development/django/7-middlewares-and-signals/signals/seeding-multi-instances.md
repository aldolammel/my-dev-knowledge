[seeding-singleton](python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton.md)
#### Python > Django > Signals > Seeding
# Creating multiple instances automatically after a migration command

---
## Before:

1. You must have your model classes done: [/python/web-development/django/3-1-models-database/\_model-class-model.py](/python/web-development/django/3-1-models-database/_model-class-model.py)

---
## 1) Create the function where you are creating those instances you need:

In `subapp_name/signals.py` (if it doesn't exist yet, create it):
```
INSTANCES_TO_AUTO_ADD = {
    "MyModelNameOne": {"name": "Link Int Page", "slug": "link_int_page", "css_class": ""},
    "MyModelNameTwo": {"name": "Link Int Cat",  "slug": "link_int_cat",  "css_class": ""},
    "MyModelNameThree": {"name": "Link Int Tag",  "slug": "link_int_tag",  "css_class": ""},
}


def your_fuction_name_to_create_instances(sender, **kwargs):
	"""Function to auto-seed MY_SUB_APP with xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
    for model_name, defaults in INSTANCES_TO_AUTO_ADD.items():
        model = sender.get_model(model_name)
        model.objects.get_or_create(slug=defaults["slug"], defaults=defaults)
```

---
## 2) Connect a receiver to `post_migrate`:

In `subapp_name/apps.py`:
```
from django.apps import AppConfig
from django.db.models.signals import post_migrate


class YourSubappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.your_subapp"

    def ready(self):
        from . import signals
        post_migrate.connect(signals.your_fuction_name_to_create_instances, sender=self)
```

---
## 3) (Optional) Blocking the deletion of seed instances:
[/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-delete](/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-delete.py)

---
## 4) (Optional) Blocking the addition of new instances:
[/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-add](/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-add.py)

---
## 5) Done!

Now, every time the `migrate` command is run, Django will execute that function, making sure those instances exist!

---
## Auto seeding for a Singleton too?
[/python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton](/python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton.md)
