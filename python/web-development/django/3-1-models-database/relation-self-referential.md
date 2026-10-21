#### Python > Django > Models
# Self-Referential

---
## Before:
- Assuming you know what is Self-Referential: [/database/\_tools/ERD/self-referential](/database/_tools/ERD/self-referential.md)

---

Relation with the same model:

Example 1:
```python
class User(models.Model):
	# ...
	friends = models.ManyToManyField(
		'self',
		# ...
	) 
```

Example 2:
```python
class User(AbstractUser):
	# ...
	updated_by = models.ForeignKey(
		'self',  # Itself relationship!
		editable=False,
		related_name='updated_users',
		on_delete=models.SET_NULL,  # if the user-updater is deleted, the updated_by field is null.
		null=True,
		verbose_name='name',
		help_text='',
	)
```

The special self keyword (used as a string value) tells Django that it should form a relationship with (other) instances of the same model.

---
## Using `ForeignKey()` field class:
[/python/web-development/django/3-1-models-database/model-attr-field-foreignKey](/python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)
## Using `ManyToManyField()` field class:
[/python/web-development/django/3-1-models-database/model-attr-field-many-to-many](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md)
## Excluding the self-referential instance from drop-down menus:
[/python/web-development/django/9-forms/form-queryset-filtering-dropdown](/python/web-development/django/9-forms/form-queryset-filtering-dropdown.md)

