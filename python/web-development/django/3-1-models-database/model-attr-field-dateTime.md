DJANGO MODEL CLASS > Field Classes (Attribute types): DATE TIME FIELD

Common Usage:
Storing dates with time like the exact timestamp a record was created, a record was last modified, start time of a meeting or appointment, the publication date and time of a news article, etc.

Field look-like on front-end:
- A date and time field (simple calendar with hour together)

Example:

```python
created_at = models.DateTimeField(
	auto_now_add=True,
	verbose_name="xxxxxx",
	help_text="",
)

updated_at = models.DateTimeField(
	auto_now=True,
	verbose_name="xxxxxx",
	help_text="",
)
```

---
## Other related options:

    >> Date Field:
        /python/web-development/django/3-1-models-database/model-attr-field-date.txt

    >> Duration Field:
        /python/web-development/django/3-1-models-database/model-attr-field-duration.txt
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

