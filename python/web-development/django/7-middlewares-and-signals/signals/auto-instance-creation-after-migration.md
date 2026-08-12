#### Python > Django > Signals
# How to create instances automatically after a migration command

---

If you want to automatically populate ([seeding](/dev-concepts/seeding.md)) your database with an initial data, in Django you'll need to use signals. For example, instead of you manually add each data every time you install your app, it already brings a piece of data to use the app as fast as possible.

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
## 3) Done!

Now, every time the `migrate` command is run, Django will execute that function, making sure those instances exist!