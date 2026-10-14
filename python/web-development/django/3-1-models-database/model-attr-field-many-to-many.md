#### Python > Django > Models > Field Classes (Attribute types)
# ManyToManyField()

---

Defining a [Many-to-Many relationship](/python/web-development/django/3-1-models-database/relation-many-to-many.md) between two models. This requires Django to create a separate "junction" or "through" table in the database.

Field look-like on front-end:
- `<select multiple>`
- `<input type="checkbox">` (one per choice)

---

==ManyToManyField field create the bridge table on DB==
Read more about it but what I know today, if you simplify the fields, using it (instead of a [ForeignKey](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md) + [bridge table](/database/_tools/ERD/many-to-many.md)) Django will make it automatically!

---

E.g. in `models.py`:
```python
class Something(...):
	categories = models.ManyToManyField(  # m2m attr name's an exception: always PLURAL (unlike DB column uses, e.g., category_id).
		"Category",
		blank=True,
		related_name="%(app_label)s_categories",  # More about: /python/web-development/django/3-1-models-database/arg-related_name.md
		verbose_name="xxxxxx",
		help_text="",
	)
	tags = models.ManyToManyField(Tag)  # On an Article model (an article can have many tags, and a tag can be on many articles)!
	students = models.ManyToManyField(Student)  # On a Course model (a student can take many courses, and a course can have many students)!
```

==Don't follow the ERD convention:==
Meanwhile ERD brings *ManyToMany* relationships among column names of db tables using, e.g., `plane_seat_id`, it changes when it's used in classes attribute names. It means the right convention to be used for ManyToMany as class attribute is always in plural like, e.g., `plane_seats`.

---
# Using Self-Referential:
[python/web-development/django/3-1-models-database/relation-self-referential](python/web-development/django/3-1-models-database/relation-self-referential.md)

---
## Similar field classes:
- Foreign Key: [python/web-development/django/3-1-models-database/model-attr-field-foreignKey](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)
- One-To-One Field: [/python/web-development/django/3-1-models-database/model-attr-field-one-to-one](/python/web-development/django/3-1-models-database/model-attr-field-one-to-one.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)
