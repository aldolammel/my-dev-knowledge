#### Python > Django > Models > Field Classes (Attribute types)
# SmallIntegerField()

---

Typical Size:
2 bytes (16-bit)

Signed Range:
-32,768 to 32,767

Common usage:
Storing small integers to save database space. Ideal for fields with a known, limited range. Examples: a person's age, a small rating scale (e.g., 1-5), number of items in a small set, or game levels.

Example:
```python
class Something(...):
    temperature = models.SmallIntegerField(
	    default=0,
	    blank=False,
	    verbose_name="xxxxxx",
		help_text="",
    )
```

---
## Similar field classes:
Positive Small Integer:
[/python/web-development/django/3-1-models-database/model-attr-field-positiveSmallInteger](/python/web-development/django/3-1-models-database/model-attr-field-positiveSmallInteger.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

