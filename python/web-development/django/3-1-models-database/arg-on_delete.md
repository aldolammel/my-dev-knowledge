#### Python > Django > Models > Arguments
# `on_delete`

---

The 'on_delete' is an argument to be use with one-to-one and one-to-many (ForeignKey) models where you define what happen with the entire instance if the foreign key is deleted:

E.g.

```python
class Director(models.Model):
	# ...
	
class Movie(models.Model):
	# ...
	director = models.ForeignKey(
		Director,
		on_delete=ONE-OPTION-HERE,
			# Options:
			models.CASCADE  # If the director is deleted, movies linked with them will be deleted.
			models.PROTECT  # If the director is deleted, Django will block the go to preserve the relation.
			models.SET_NULL  # If the director is deleted, movies linked with them will get their director field as 'null'.
		null=True,
	)
```

---
## Field class > ForeignKey():
[python/web-development/django/3-1-models-database/model-attr-field-foreignKey](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)

