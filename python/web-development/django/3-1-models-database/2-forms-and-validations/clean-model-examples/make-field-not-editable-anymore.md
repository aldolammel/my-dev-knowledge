#### Python > Django > Models > Validations > `clean()` examples
# Making a field not editable anymore

---

Basic: if you wanna make a model field easily not editable:
```python
# models.py:
class Something(...):
	my_attr = models.SomeFieldTypeHere(
		editable = False,  # App and DB level!
	)

```

But if you wanna make a field totally editable by the user for the very first time, but later make it not editable, do it:
```python
# models.py:
class Something(...):
	# ...
	def clean(self):
		"""..."""
		# Protecting the code field to be edited after the creation:
		if self.pk:
			original = Something.objects.filter(pk=self.pk).values("my_attr").first()
			if original and self.my_attr != original["my_attr"]:
				raise ValidationError(
					{"my_attr": "CRITICAL: The my_attr cannot be changed after creation."}
				)
```

==Important==
Don't do this `clean()` validation if the attribute field has `editable = False` argument. It wouldn't make sense.

---
## What is Model clean() method:
[/python/web-development/django/3-1-models-database/method-clean](/python/web-development/django/3-1-models-database/method-clean.md)

