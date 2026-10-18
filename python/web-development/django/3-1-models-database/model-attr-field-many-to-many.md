#### Python > Django > Models > Field Classes (Attribute types)
# ManyToManyField()

---

**Before:**
1. What is *Many-to-Many* in a database: [/database/\_tools/ERD/many-to-many](/database/_tools/ERD/many-to-many.md)

---

Used when you wanna select one or many options in a field and it means a relation between two models. This field class requires Django to automatically create a separate ["junction" (bridge class/table)](/database/_tools/ERD/many-to-many.md) in the database. This intermediary table is not directly visible in the `models.py`, but is present in the db schema.

==It automatically creates a bridge table==
Unlike a detailed [ERD](/database/document-templates/erd.md), for Django you don't need to create a [ForeignKey](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md) + [bridge table](/database/_tools/ERD/many-to-many.md) to resolve the Many-to-Many issue. In Django Models, you just use the ManyToManyField and Django will create and manage the bridge table automatically!

**Field look-like on Django CMS:**
![](/python/web-development/django/4-cms-admin/z_imgs/many-to-many-field-on-django-cms.png)
- Also, you can use this double-column solution: [/python/web-development/django/4-cms-admin/1-customizing/listview-model-option-filter_horizontal](/python/web-development/django/4-cms-admin/1-customizing/listview-model-option-filter_horizontal.md)
- Step-by-step to build this kind of multi-selection-menu: [/python/web-development/django/3-1-models-database/field-select-menu-multiple](/python/web-development/django/3-1-models-database/field-select-menu-multiple.md)

**Field look-like on front-end:**
- `<select multiple>`
- `<input type="checkbox">` (one per choice)

---

E.g. in `models.py`:
```python
class Something(...):
	categories = models.ManyToManyField(  # m2m attr name's an exception: always PLURAL (unlike DB column uses, e.g., category_id).
		"Category",
		# null=True,  # This field has NO effect over M2M field!
		blank=True,
		related_name="%(app_label)s_%(class)s_categories",  # More about: /python/web-development/django/3-1-models-database/arg-related_name.md
		verbose_name="xxxxxx",
		help_text="",
	)
	tags = models.ManyToManyField(Tag)  # On an Article model (an article can have many tags, and a tag can be on many articles)!
	students = models.ManyToManyField(Student)  # On a Course model (a student can take many courses, and a course can have many students)!
```
*ManyToManyField* doesn't need the `on_delete` argument because if some list option is deleted, Django will delete the reference directly in the bridge table (mapping) created automatically for this kind of field class.

Another common use example:
```python
class Publication(...):
    title = models.CharField(...)

class Article(...):
    headline = models.CharField(...)
    publications = models.ManyToManyField(
	    'Publication',  # You can set it between quotes to avoid circular import issues in the future.
	    related_name="articles",
	)
```

==Don't follow the ERD convention:==
Meanwhile ERD brings *ManyToMany* relationships among column names of db tables using, e.g., `plane_seat_id`, it changes when it's used in classes attribute names. It means the right convention to be used for ManyToMany as class attribute is always in plural like, e.g., `plane_seats`.

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
## Avoid `related_name` argument error using ManyToManyField in Mixin Model classes:
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
## Similar field classes:
- Foreign Key: [python/web-development/django/3-1-models-database/model-attr-field-foreignKey](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)
- One-To-One Field: [/python/web-development/django/3-1-models-database/model-attr-field-one-to-one](/python/web-development/django/3-1-models-database/model-attr-field-one-to-one.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)
