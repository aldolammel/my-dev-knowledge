#### Python > Django > Models > Field Classes (Attribute types)
# PositiveIntegerField()

---

Any integer value that should never be negative. Examples: stock quantities, a count of items, or any other number where a negative value would be invalid or nonsensical.

Typical Size:
4 bytes (32-bit)

Signed Range:
0 to 2,147,483,647 (It's "unsigned" in practice, enforced by Django, not the database)

Example:
```python
class Something(...):
	stock = models.PositiveIntegerField(
		default=0,
		blank=True,
		verbose_name="xxxxxx",
		help_text="",
	)
```

Using `choices` argument:
- Probably you won't use choices with this field class! Try something like [PositiveSmallIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveSmallInteger.md).

---
## Similar field classes:

    >> Positive Big Integer Field
        /python/web-development/django/3-1-models-database/model-attr-field-positiveBigInteger.txt

    >> Positive Small Integer Field
        /python/web-development/django/3-1-models-database/model-attr-field-positiveSmallInteger.txt
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)