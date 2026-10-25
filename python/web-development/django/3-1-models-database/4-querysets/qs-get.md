#### Python > Django > Models > Query sets
# get

---
## Before:
- What is QuerySet: [/python/web-development/django/3-1-models-database/4-querysets/\_what-is-queryset](/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md)

---
In these examples, consider each queryset is asking data to a model called `Recipe`:
### Showing the entry with pk/id = 4
```python
from . import models

r_specific = models.Recipe.objects.get(id=4)
```
### Showing all objects in a specific table (Recipe)
```python
from . import models

r_all = models.Recipe.objects
# Or:
r_all = models.Recipe.objects.all()
```

---
## Examples:
How to make the CMS doens't show unpublished things with the published ones: [/python/web-development/django/4-cms-admin/method-formfield_for_foreignkey](/python/web-development/django/4-cms-admin/method-formfield_for_foreignkey.md)


