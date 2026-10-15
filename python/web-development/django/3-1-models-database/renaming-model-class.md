#### Python > Django > Models
# Renaming a model class safely

---

To safely rename a Model Class you must check these things:

1. Rename the model class itself in `/apps/subapp_folder/models.py`;
2. Inside this class, rename each [related_name](/python/web-development/django/3-1-models-database/arg-related_name.md) argument once this name is based in the class name.
3. Check the class Meta if there's no any [constraints](/python/web-development/django/6-errors-and-validations/validation-1-for-database.md). If there's constraints, you probably has your old class name naming a constraint `name` argument.
4. Check the `admin.py` because the admin class of this model class follows the old name yet.
5. Search for all occurrences of that model class name and update all of them!
6. Careful because it's not done yet: Django has different patterns to call a model class in different situations. For example, your model class is called `PagexElementBase`. So, it can be used like these example below:
```python
# E.g.:
# admin.py
url = reverse("admin:pagex_pagexelementbase_add")
# "admin:<yourappname_yourmodelclassname_...>"
```
5. Update your database schema with the new data:
```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

