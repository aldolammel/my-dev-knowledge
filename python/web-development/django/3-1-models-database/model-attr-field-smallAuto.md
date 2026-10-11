#### Python > Django > Models > Field Classes (Attribute types)
# SmallAutoField()

---

It's the small integer version of an auto-incrementing primary key. Automatically incrementing primary keys for small tables with a hard, known upper size limit. This is a very specific optimization tool.

**Typical Size:**
2 bytes (16-bit)

**Full Integer Range:**
-32,768 to 32,767

**Auto-incremental Range:**
1 to 32,767 (It's effectively unsigned and starts at 1, like other auto fields).

**Field look-like on front-end:**
- Only the value.

E.g.
```python
id = models.SmallAutoField(
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



    