#### Python > Django > Models > Arguments
# `related_name`

---

The `related_name` is a powerful feature for optimizing database access by managing how related objects are retrieved. It's an argument to specify the reverse relation name from the related model back to the model defining the `ForeignKey`.

The name you choose becomes the attribute name on the related model instance! Be specific!

---
## WITHOUT `related_name`

E.g.
```python
class Book(models.Model):
	author = models.ForeignKey(
		Author,
		on_delete=models.CASCADE
	)
```
Calling reverse relation:
```python
<foreignKeyAttribute>.<current_model>_set.all()
# E.g.: author.book_set.all()
```

---
## WITH `related_name`

E.g.
```python
class Book(models.Model):
	author = models.ForeignKey(
		Author,
		on_delete=models.CASCADE,
		related_name='books'       # Always plural(convention)!    # Usage: author.books
	)
```
                
Calling reverse relation:
```python
author.books.all()
```

---
## SPECIAL: Avoiding related_name conflicts

E.g.
```python
class AuditMixin(models.Model):  # Abstract model!
	...
	created_by = models.ForeignKey(
		stgs.AUTH_USER_MODEL,
		related_name="%(app_label)s_%(class)s_created_by",                     # <----
			# Output: "appName_modelName_modelInhiretedAuditmixin_created_by"   # <----
		...,
	)
```

---
## More special use:

- related_name='+' (Disables the reverse relation entirely!)
- Can be used in prefetch_related() for optimization: [/python/web-development/django/3-1-models-database/method-prefetch_related.py](/python/web-development/django/3-1-models-database/method-prefetch_related.py)

---
## Field class > ForeignKey():
[python/web-development/django/3-1-models-database/model-attr-field-foreignKey](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)
