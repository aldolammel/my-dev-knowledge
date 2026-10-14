#### Python > Django > Models > Field Classes (Attribute types)
# ForeignKey()

---

In a [One-to-Many](/python/web-development/django/3-1-models-database/relation-one-to-many.md) relationship, the *ForeignKey()* field class stays only in the many side. The attibute name is always singular.

**Common Usage:**
Defining a many-to-one relationship between two models. It creates a database foreign key from one table to another's primary key.

**Field look-like on front-end:**
`<select>`

E.g.:
```python
from django.conf import settings

class BlogPost(...):
	# ...
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		editable=False,
		related_name="blog_posts",
		on_delete=models.SET_NULL,
		null=True,
		blank=False,
		verbose_name="name",
		help_text="",
	)
```
A common use example:
```python
class Something(...):
	plane_seat_type = models.ForeignKey(
		PlaneSeatType,  # or "PlaneSeatType" (between quotes if model comes later).
		related_name="<WhatExactlyModelOwnedHere+s>",
		on_delete=models.SET_NULL,
		null=True,
		blank=False,
		verbose_name="name",
		help_text="",
	)
```
Read more about:
- Argument `related_name`: [/python/web-development/django/3-1-models-database/arg-related_name](/python/web-development/django/3-1-models-database/arg-related_name.md)
- Argument `on_delete`: [/python/web-development/django/3-1-models-database/arg-on_delete](/python/web-development/django/3-1-models-database/arg-on_delete.md)

---
## Similar field classes:
Many-To-Many Field: [/python/web-development/django/3-1-models-database/model-attr-field-many-to-many](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)



    