#### Python > Django > Errors
# How to avoid circular import issue

---
## 1) Use string references for model relationships:

Model field classes like [ForeignKey](/python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md), [OneToOneField](/python/web-development/django/3-1-models-database/model-attr-field-one-to-one.md), or [ManyToManyField](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md) have the ability to call other model classes, but to avoid the circular issue, you should build their relationship with other models declaring other models between quotes (as string, not as object):
```python
# /apps/subapp_a/models.py file:
from apps.subapp_b.models import AnotherClass    # <---- importing a model as object as it is!

class Something(...):
    my_attribute = models.ForeignKey(
	    'AnotherClass',                          # <---- but calling that as string!
	    # ...
	)
```

Django resolves these lazily at app-loading time, so `app_a` and `app_b` never need to import each other's `models.py` directly.

---
## 2) Import inside functions/methods (local imports):

When you genuinely need the class itself (not just a relation), defer the import to where it's used:
```python
def some_function():
    from app_b.models import AnotherClass       # imported only when called
    ...
```

This is common in `save()` overrides, signal handlers, and management commands.

---
## 3) Use `apps.get_model()` for dynamic lookups:

Useful in migrations, signals, or utility functions where you don't want a hard import dependency at all:
```python
from django.apps import apps

def get_another_model():
    return apps.get_model('app_b', 'AnotherClass')
```

---
## 4) Move signals to a dedicated `signals.py` and connect them in `AppConfig.ready()`:

Signal handlers are a classic source of circularity because they often need to import models from other apps. Isolating them avoids polluting `models.py`:
```python
# app_a/apps.py
class AppAConfig(AppConfig):
    name = 'app_a'
    def ready(self):
        import app_a.signals  # noqa
```

More about *Signals*: [/python/web-development/django/7-middlewares-and-signals/signals/\_basic-signals](/python/web-development/django/7-middlewares-and-signals/signals/_basic-signals.md)

---
## 5) Restructure with a shared/common app:

If two apps depend on each other's models, that's often a sign a shared concept (e.g., a base model or [mixin](python/web-development/django/4-cms-admin/model-type-mixin.md)) should live in its own app that both import from, avoiding the cross-dependency altogether.

---
## 6) Use `TYPE_CHECKING` for type hints only:

If the only reason you're importing a model is for a type annotation, guard it so it doesn't execute at runtime:
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app_b.models import Customer

def process(customer: "Customer") -> None:
    ...
```

---
## 7) Be careful with `related_name` and reverse accessors:

Circular-looking errors sometimes come from clashing `related_name` values across apps rather than actual import cycles, worth ruling out before restructuring code.

More about related_name: [/python/web-development/django/3-1-models-database/arg-related_name](/python/web-development/django/3-1-models-database/arg-related_name.md)

---
