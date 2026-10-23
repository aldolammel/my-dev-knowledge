#### Python > Django > Models > QuerySets
# `attname` attribute/column benefits

---

When you declare a `ForeignKey` like this:
```python
class Component(...):
	id = ...
	plane = models.ForeignKey(Plane, ...)
	# ...
```
Django creates 2 things on the model that's using the *Foreign-Key* (FK):

- It creates a column/attribute called `plane` that returns the related object (`Plane`) - this is the "descriptor" that you already created to call the FK.
- And also it creates a column/attribute called `plane_id` stores only the integer (or `None`). 

When you need the FK `id` the current instance is using, you SHOULDN'T create a query for this. E.g. of a useless query:
```python
self.instance.plane.id  # BAD! It fetches the whole `Plane` row, only to read the PK (id) you already had in memory.
```

That is useless because you already have the FK `id` in your current instance through the `plane_id` attribute/column:
```python
self.instance.plane_id # Great performance because it's in memory!
```

---
## ERD uses the same logic for its *ForeignKey* names:
[When you create an ERD](/database/_tools/ERD/_about.md), all "Many" side of an *One-to-Many* relationship ([ForeignKey](/python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)) is connected not to the entity/object instance ID but to an attribute with the name of the entity/object where the "One" side is connected, adding an `_id` as suffix of this attribute, e.g., `plane_id`.

