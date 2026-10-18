DJANGO MODEL CLASS > Field Classes (Attribute types): NULL BOOLEAN FIELD (DEPRECATED!)

==Deprecated:==
As of Django 3.1, `NullBooleanField()` is deprecated. Its usage should be replaced with BooleanField with the appropriate `null=True` setting. It remains in the documentation for backward compatibility but will be removed in a future release.

**Common Usage:**
It was used to represent a boolean field that needed a "unknown" or "not set" state in addition to True/False. This required three states: True, False, and NULL (in the database) / None (in Python).

**Field look-like on front-end:**
xxxxxxx

Example:
```python
legacy_field = models.NullBooleanField()  # It should be replaced by BooleanField(null=True, blank=True)
```

---
## Similar field classes:
Boolean Field: [/python/web-development/django/3-1-models-database/model-attr-field-boolean](/python/web-development/django/3-1-models-database/model-attr-field-boolean.md)

