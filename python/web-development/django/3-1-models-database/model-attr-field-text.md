#### Python > Django > Models > Field Classes (Attribute types)
# TextField()

---

Storing large, arbitrary amounts of text where the length is unpredictable or can be very long. No required max_length in the database (though you can set one for form validation). It's perfect for body content of a blog post or article, user comments, product descriptions, or reviews, JSON data stored as a string (before JSONField existed), any free-form, long-text input from a user.

**Field look-like on front-end:**
- Textarea field with multilines.

Basic: `TextField()` field class the default value is an empty string (`''`) and `null=True` should be avoided.
```python
class Something(...):
	book_chapter_content = models.TextField(
		default="",
		blank=False,
		verbose_name="xxxxxx",
		help_text="",
		validators=[
			MinLengthValidator(140),
		],
	)
```
Limiting size for core-business and db-size-protection:
```python
class Something(...):
	seo_desc = models.TextField(
		max_length=consts.INT_GENERIC_DESC_MAX,
		default="",
		blank=True,
		verbose_name="xxxxxx",
		help_text="",
		validators=[
			MinLengthValidator(consts.INT_GENERIC_DESC_MIN),
			MaxLengthValidator(consts.INT_GENERIC_DESC_MAX),
		],
	)
```

---
## Similar field classes:
- CharField: [/python/web-development/django/3-1-models-database/model-attr-field-char](/python/web-development/django/3-1-models-database/model-attr-field-char.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)