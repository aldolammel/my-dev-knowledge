#### Python > Django > Models > Field Classes (Attribute types)
# BigIntegerField()

---

This is a subclass of BigIntegerField specifically designed for primary keys. It automatically increments each time a new object is created, just like the standard AutoField, but with the large range of a BIGINT.

**Typical Size:**
8 bytes (like BigIntegerField)

**Full Integer Range:**
-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807

**Auto-incremental Range:**
1 to 9,223,372,036,854,775,807

**Field look-like on front-end:**
- Only the value.

**Common usage:**
Automatically incrementing primary keys. You don't define the value; Django automatically assigns the next available number upon object creation. BigAutoField is the default in modern Django to avoid the table size limit of AutoField.

Example:
```python
id = models.BigIntegerField(
	primary_key=True,
	unique=True,
	editable=False,
)
```

---
## Other options for Primary Key:
[/python/web-development/django/3-1-models-database/creating-id](/python/web-development/django/3-1-models-database/creating-id.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)





