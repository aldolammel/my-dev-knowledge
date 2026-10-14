#### Python > Django > Model Class > Field Classes (Attribute types)
# BooleanField()

---

**Common Usage:**
Representing a True/False or On/Off state.

**Field look-like on front-end:**
- Checkbox field.

E.g.
```python
class Something(...):
	is_published = models.BooleanField(
		default=True,
		verbose_name="xxxxxx",
		help_text="",
	)
```

---
## Similar field classes:
Null Boolean Field ==(Deprecated)==: [/python/web-development/django/3-1-models-database/model-attr-field-nullBoolean](/python/web-development/django/3-1-models-database/model-attr-field-nullBoolean.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)
