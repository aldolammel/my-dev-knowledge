#### Python > Django > Models
# Renaming a model class safely

---

To safely rename a Model Class you must check these things below.

E.g. your model class to rename is `ProcTypeGroup`. That said, do it:

1. In `models.py`, rename the model class itself.
2. In `models.py`, rename all model class' attribute field names that's calling the target model class as *ForeignKey*: e.g. `proc_type_group = models.ForeignKey(...)`.
3. In `models.py`, don't forget to check the `verbose_name` argument if declared.
4. In `models.py`, check the name of all target model class attribute names and their verbose_name too. Some of them can be variations or use part of the old name. 
5. In `models.py`, inside the class, rename each [related_name](/python/web-development/django/3-1-models-database/arg-related_name.md) argument once this name is based in the class name.
6. In `models.py`, check the class Meta if there's no any [constraints](/python/web-development/django/6-errors-and-validations/validation-1-for-database.md). If there's constraints, you probably has your old class name naming a constraint `name` argument.
7. In `admin.py`, check it because admin class of this model class probably follows the old name.
8. Search for the model class full name but with spaces: e.g., "`procedure type group`" with case-insensitive.
9. Search for the model class name variants, with underscores: e.g., "`proc_type_group`" with its variants.
10. Search for URL/View patterns: e.g., "`proctypegroup`".
11. Ask you if you should update project's documents like [Architecture Design](/python/web-development/django/document-templates/django-architecture-design.md), [TDD](/python/web-development/django/document-templates/tdd.md) and [ERD](/database/document-templates/erd.md).

Update your database schema with the new data:
```bash
uv run manage.py makemigrations
uv run manage.py migrate
```

Done.

---
## Renaming a sub-app:
[/python/web-development/django/3-1-models-database/renaming-subapp](/python/web-development/django/3-1-models-database/renaming-subapp.md)


