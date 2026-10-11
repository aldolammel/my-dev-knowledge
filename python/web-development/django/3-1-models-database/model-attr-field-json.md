#### Python > Django > Models > Field Classes (Attribute types)
# JSONField()

---

In Django, use `models.JSONField()` to store JSON data in your database. It supports dictionaries, lists, strings, numbers, booleans, and `None`.

**Common Usage:**
Storing structured data in JSON format. This is incredibly useful for flexible, schema-less data attached to a model. Supported by PostgreSQL, MySQL 8+, and SQLite. Good for storing user preferences or configuration settings as a key-value object; saving API responses or web-hook payloads for auditing; dynamic form data or product attributes that can vary greatly.

**Field look-like on front-end:**
xxxxxxx

Example:
        
```python
class Aircraft(models.Model):
    specs = models.JSONField(
	    default=dict,
	    blank=True,
		verbose_name="xxxxxx",
		help_text="",
	)
```

---
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

