#### Python > Django > Models > Field Classes (Attribute types)
# OneToOneField()

---

Defining a one-to-one relationship between two models. This is often used for model inheritance or extending a model with additional information.

Field look-like on front-end:
xxxxxxx

Example:

```python
home_page = models.OneToOneField(
	"PagexPage",
	on_delete=models.SET_NULL,
	null=True,
	blank=True,
	related_name="is_home_for",
	verbose_name="xxxxxx",
	help_text="",
)
```

---

## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)