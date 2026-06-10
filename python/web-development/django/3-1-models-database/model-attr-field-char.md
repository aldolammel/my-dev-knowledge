#### Python > Django > Models > Attribute fields
# CharField()

---

Requiring the max_length parameter to define the maximum number of characters, this field is for storing short-to-medium-length strings like a person's first or last name, a city name, country code, category name, an ISBN number, product code, or other short identifier.

Field look-like on front-end:
- Single line field.

**Examples:**

Basic:
```
first_name = models.CharField(
	max_length=25,
	blank=True,
	default="",                   # or None, but avoid to use 'null=True' if blank=True!
)
```
Advanced:
```
first_name = models.CharField(
	max_length=25,
	blank=True,
	default="",                   # or None, but avoid to use 'null=True' if blank=True!
	validators=[
		MinLengthValidator(2),
		MaxLengthValidator(25),
		# validators.validate_chars_spaces_enabled,
	],
)
```
Drop-down field:
```
front_type = models.CharField(
	max_length=35,  # Database level checking.
	choices=consts.CHOICES_FRONTEND,
	default=consts.VAL_FRONT_TOOL_DEFAULT,
)
```

---
## Other related options:
- Text Field: [python/web-development/django/3-1-models-database/model-attr-field-text](python/web-development/django/3-1-models-database/model-attr-field-text.md)
- Email Field: [python/web-development/django/3-1-models-database/model-attr-field-email](python/web-development/django/3-1-models-database/model-attr-field-email.md)
- URL Field: [python/web-development/django/3-1-models-database/model-attr-field-url](python/web-development/django/3-1-models-database/model-attr-field-url.md)
- Slug Field: [python/web-development/django/3-1-models-database/model-attr-field-slug](python/web-development/django/3-1-models-database/model-attr-field-slug.md)
- Binary Field: [python/web-development/django/3-1-models-database/model-attr-field-binary](python/web-development/django/3-1-models-database/model-attr-field-binary.md)


