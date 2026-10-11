#### Python > Django > Models > Field Classes (Attribute types)
# SlugField()

---

A specialized CharField for storing URL-friendly slugs. A slug typically contains only letters, numbers, underscores, or hyphens. It's primarily used for creating clean, readable URLs for objects. It enforces this format with a default validator and is often used with `prepopulate_from` in the admin to auto-generate from another field (like a title). 

Field look-like on front-end:
- Generating URLs for blog posts: `/blog/my-awesome-post-title/` where my-awesome-post-title is the slug.

Example:
```python
from django.utils.text import slugify

class Movie(models.Model):
	name = models.CharField(...)
	slug = models.SlugField(
		unique=True,  # Db-level constraint
		max_length=200, 
		default='', 
		editable=False,  # Auto-generated in save().
		blank=True,  # Once it's auto-generated in save(), it'll pass empty for clean().
		null=False, 
		db_index=True,  # Extremely recommeded for this field class!
		verbose_name="xxxxxx",
		help_text="",
	)

	def save(self, *args, **kwargs):
		"""Built-in Model method that's executed when the db entry saving runs."""
		# Runs full validation before saving:
		self.full_clean()
		# Defining the slug based on the name:
		if self.name:
			self.slug = slugify(self.name)
			super().save(*args, **kwargs)

```

---
## Custom: include an additional care for slug uniqueness:
My custom validator solution: [clean_checker_txt_uniqueness](/python/web-development/django/3-1-models-database/2-forms-and-validations/uniqueness-of-a-name.py)

---
## Slug with more flexibility by @aldolammel:
[/python/web-development/django/utils/aldo-slugifier.py](/python/web-development/django/utils/aldo-slugifier.py)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

