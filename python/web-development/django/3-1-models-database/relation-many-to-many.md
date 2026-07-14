#### Python > Django > Models > Attribute types
# ManyToManyField

---

This attribute type is used to create a many-to-many relationship where Django automatically creates an intermediary table (bridge) to manage the many-to-many relationship. This table contains two foreign keys: one pointing to each of the related models. This intermediary table is not directly visible in the models but is present in the database schema.

If you need an attribute contains one or maybe many id's in, you must use a *ManyToMany* relationship.

E.g.
```
# models.py

class Publication(...):
    title = models.CharField(...)

class Article(...):
    headline = models.CharField(...)
    publications = models.ManyToManyField(
	    'Publication',  # Set it between quotes to avoid circular import issues in the future.
	    related_name="articles",
	)
```

More: [/python/web-development/django/3-1-models-database/field-select-menu-multiple](/python/web-development/django/3-1-models-database/field-select-menu-multiple.md)

ManyToMany doesn't need the on_delete argument because if some list option is deleted, Django will delete the reference directly in the bridge table (mapping) created automatically in ManyToManyField relationship.

---
## How to avoid Circular Import issue:
[/python/web-development/django/6-errors-and-validations/importing-no-circular](/python/web-development/django/6-errors-and-validations/importing-no-circular.md)
