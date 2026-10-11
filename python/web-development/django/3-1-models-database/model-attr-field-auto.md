#### Python > Django > Models > Field Classes (Attribute types)
# AutoField()

---

This is a subclass of IntegerField specifically designed for primary keys. It automatically increments each time a new object is created, just like the standard BigAutoField, but with the short range of an INTEGER.

**Typical Size:**
4 bytes (like IntegerField)

**Full Integer Range:**
-2,147,483,648 to 2,147,483,647

**Auto-incremental Range:**
1 to 2,147,483,647 (Effectively, as it's usually a primary key starting at 1)

**Field look-like on front-end:**
- Only the value.

**Common usage:**
Automatically incrementing primary keys. You don't define the value; Django automatically assigns the next available number upon object creation. BigAutoField is the default in modern Django to avoid the table size limit of AutoField.

Example:
```python
id = models.AutoField(
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


