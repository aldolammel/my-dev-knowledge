#### Python > Django > Model matters
# Meta class: Abstract

---

**Before:**
1. What is Model meta: [/python/web-development/django/3-1-models-database/meta](/python/web-development/django/3-1-models-database/meta.md)

---

Marks a model as a base class for inheritance, not a database table.

**When to use:**
- To create reusable model components/[mixins](dev-concepts/class-type-mixin.md);
- For shared fields or methods across multiple models;
- To implement design patterns (like BaseModel with common fields);
- The abstract model itself doesn't get a database table.

E.g.
```python
class AuditBase(models.Model): # Abstract model!
	"""Stores who and when things were changed."""
	created_at = models.DateTimeField(
		auto_now_add=True,
		editable=False,
		verbose_name=lang.lbl_created_at,
	)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="%(app_label)s_%(class)s_created_by",
		editable=False,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name=lang.lbl_created_by,
	)
	updated_at = models.DateTimeField(
		auto_now=True,
		editable=False,
		verbose_name=lang.lbl_updated_at,
	)
	updated_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name="%(app_label)s_%(class)s_updated_by",
		editable=False,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name=lang.lbl_updated_by,
	)
	
	class Meta:
		abstract = True # Flags to the db that no tables should be created from this.
```

==Aware!==
- Abstract models shouldn't have a primary key!
- In this example above, those classes that inherited this class must send the user via `admin.py` [save_model()](/python/web-development/django/4-cms-admin/method-save_model.py) method!

---
## When you CANNOT use abstract:

You cannot use an abstract model directly in a ForeignKey or ManyToManyField, even with a '*through=*' model. Django's ORM simply doesn't allow it 'cause abstract models are not installed in the database, so there's no concrete table to point to.

**Possible solution > Concrete Model:** [/python/web-development/django/3-1-models-database/\_model-class-model.py](/python/web-development/django/3-1-models-database/_model-class-model.py)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

MODEL'S INHERITANCE IN DJANGO:

[/python/web-development/django/3-1-models-database/Inheriting-attributes](/python/web-development/django/3-1-models-database/Inheriting-attributes.md)

WHAT IS MODEL META:

[/python/web-development/django/3-1-models-database/meta](/python/web-development/django/3-1-models-database/meta.md)