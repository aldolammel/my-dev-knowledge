DJANGO MODEL CLASS > Field Classes (Attribute types): IMAGE FIELD

Common Usage:
Handling file uploads. ImageField inherits from FileField and adds image-specific validation (e.g., checking if the upload is a valid image) and properties (like height and width).

Field look-like on front-end:
- Single upload field.

    Example:

```python
img_highlight = models.ImageField(
	upload_to=consts.PATH_IMG,
	blank=True,
	verbose_name="xxxxxx",
	help_text="",
)
```

---
## Similar field classes:
File Field:
        /python/web-development/django/3-1-models-database/model-attr-field-file.txt
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)