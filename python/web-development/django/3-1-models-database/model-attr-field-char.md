#### Python > Django > Models > Field Classes (Attribute types)
# CharField()

---

Requiring the max_length parameter to define the maximum number of characters, this field is for storing short-to-medium-length strings like a person's first or last name, a city name, country code, category name, an ISBN number, product code, or other short identifier.

Field look-like on front-end:
- Single line field.

**Examples:**

Basic:
```python
class Something(...):
	first_name = models.CharField(
		max_length=consts.VAL_GENERIC_MAX,
		blank=True,
		default="",  # or None, but avoid to use 'null=True' if blank=True!
		verbose_name="xxxxxx",
		help_text="",
	)
```
Advanced:
```python
class Something(...):
	first_name = models.CharField(
		max_length=consts.VAL_GENERIC_MAX,
		default="",  # or None, but avoid to use 'null=True' if blank=True!
		blank=True,
		verbose_name="xxxxxx",
		help_text="",
		validators=[
			MinLengthValidator(consts.VAL_GENERIC_MIN),
			MaxLengthValidator(consts.VAL_GENERIC_MAX),
			# validators.validate_chars_spaces_enabled,
		],
	)
```
Drop-down field:
```python
class Something(...):
	front_type = models.CharField(
		max_length=consts.VAL_GENERIC_MAX,  # Database level checking.
		choices=consts.CHOICES_SOMETHING,
		default=consts.VAL_SOMETHING_DEF,
		verbose_name="xxxxxx",
		help_text="",
	)
```

---
## Similar field classes:
- Text Field: [/python/web-development/django/3-1-models-database/model-attr-field-text](/python/web-development/django/3-1-models-database/model-attr-field-text.md)
- Email Field: [/python/web-development/django/3-1-models-database/model-attr-field-email](/python/web-development/django/3-1-models-database/model-attr-field-email.md)
- URL Field: [/python/web-development/django/3-1-models-database/model-attr-field-url](/python/web-development/django/3-1-models-database/model-attr-field-url.md)
- Slug Field: [/python/web-development/django/3-1-models-database/model-attr-field-slug](/python/web-development/django/3-1-models-database/model-attr-field-slug.md)
- Binary Field: [/python/web-development/django/3-1-models-database/model-attr-field-binary](/python/web-development/django/3-1-models-database/model-attr-field-binary.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

