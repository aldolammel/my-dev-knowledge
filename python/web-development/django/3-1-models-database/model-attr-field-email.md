DJANGO MODEL CLASS > Field Classes (Attribute types): EMAIL FIELD

Common Usage:
A specialized CharField that includes email format validation using Django's built-in validator. It's not enforced at the database level but in Django forms.

Field look-like on front-end:
- Single field with simple e-mail validation.

    Examples:
```python
# Basic:
email = models.EmailField(
	max_length=255,
	unique=True,
	blank=True,
	verbose_name="xxxxxx",
	help_text="",
)
# Advanced:
email = models.EmailField(
	max_length=255,
	unique=True,
	blank=False,
	default="",  # or None. It's demanded if blank=False or null=False!
	verbose_name="xxxxxx",
	help_text="",
)
```

---

> > Other related options:

    >> Char Field:
        /python/web-development/django/3-1-models-database/model-attr-field-char.txt
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)