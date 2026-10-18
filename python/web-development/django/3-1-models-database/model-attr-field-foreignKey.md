#### Python > Django > Models > Field Classes (Attribute types)
# ForeignKey()

---

In a [One-to-Many](/database/_tools/ERD/one-to-many.md) relationship, the *ForeignKey()* stays only in the many side. The attibute name is always singular.

**Common Usage:**
It creates a database foreign key from one table to another's primary key.

**Field look-like on Django CMS:**
![](/python/web-development/django/4-cms-admin/z_imgs/foreignkey-on-django-cms.png)

**Field look-like on front-end:**
`<select>` (single-selection only)

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
		related_name="<WhatExactlyModelOwnedHere+s>",  # "somethings"
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
## Creating a circular relationship:

In this example, we have multiple relationships between the same two models. Hence we might need to define them in both models. By using the model name as a string instead of a direct reference, Django is able to resolve such dependencies. Two models that have a circular relationship:
```python
class Product(models.Model):
	last_buyer = models.ForeignKey('User')

class User(models.Model):
	created_products = models.ManyToManyField('Product')
```
In case you need a self-referential relationship instead: [/python/web-development/django/3-1-models-database/relation-self-referential](/python/web-development/django/3-1-models-database/relation-self-referential.md)

---
## Getting data from other model classes through ForeignKey:
Let's say we have a `House` object that we should fill its `full_address` by our own but, in case we leave it empty, the Python must fill that with the `Street` name. Once the street is a Foreign Key, all we need to do is to use the benefit the data already exists. And how both classes has a directly relationship (because the FK), we definitely  DONT need QuerySet in here.
```python
# models.py

class Street(models.Model):
    name = models.CharField(max_length=100)


class House(models.Model):
    street = models.ForeignKey(
	    Street,
	    on_delete=models.CASCADE
	)
	full_address = models.CharField(
		...
	)
	
	def save(...):
		# Follow the relationship from House to Garage:
		if not self.garage and self.garage and self.garage.name:
			self.garage_name = self.garage.name
```

---
## Avoid `related_name` argument error using ForeignKey in Mixin Model classes:
```python
related_name="%(class)s_<your_current_related_name_here>",
# This "%(class)s_" will be automatically replaceb by the model class that's inheriting the Mixin model class.
```

---
## Importing model from another sub-app:
[/python/web-development/django/3-1-models-database/importing-model-from-other-subapp](/python/web-development/django/3-1-models-database/importing-model-from-other-subapp.md)

---
# Using Self-Referential:
[python/web-development/django/3-1-models-database/relation-self-referential](python/web-development/django/3-1-models-database/relation-self-referential.md)

---

## CMS customizing: Removing permissions to show ForeignKey field buttons:
[/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-add-for-foreignKey](/python/web-development/django/4-cms-admin/1-customizing/removing-cms-permission-to-add-for-foreignKey.md)

---
## Similar field classes:
Many-To-Many Field: [/python/web-development/django/3-1-models-database/model-attr-field-many-to-many](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

