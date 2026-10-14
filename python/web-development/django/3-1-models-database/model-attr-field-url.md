#### Python > Django > Models > Field Classes (Attribute types)
# URLField()

---

A specialized *CharField* for storing URLs. It includes URL format validation in *Django forms*.

**Field look-like on front-end:**
- Single field with simple URL validation.

Basic:
```python
url = models.URLField(
	max_length=255,
	blank=True,  # Even if you set validators, blank=True will ignore any validator set for this attribute! Be aware!
	# validators=[URLValidator()],  # Not need for URLField!
)
```
Case blank false:
```python
url = models.URLField(
	# ...
	blank=False,
	default="",  # or None. It's demanded if blank=False or null=False!
)
```
Forcing the field do not use its built-in validator (NOT TESTED YET):
```python
url = models.URLField(
	# ...
	blank=False,
	default="",
	validators=[],  # Once you declare the usage of valitadors like this, and set it empty, it will overriden original validators for none!
)
```

---
## If you wanna customize the URLField validation:

```python
url = models.CharField(
	# Why not URLField: I didn't find a solid way to create exceptions in URLField original behavior so I changed to CharField. The custom validator used here (validate_exceptions_url) takes care of it, calling all built-in URLField benefits through itself!
	# ...
	blank=False,
	default="https://#",
	validators=[
		validators.validate_exceptions_url,
	],
)
```
E.g. in `validators.py`:
```python
from django.core.validators import URLValidator

def validate_exceptions_url(value):
	"""App-level URLValidator that additionally accepts specific exceptions as a valid value."""
	exceptions = ["https://#", "http://#"]
	if value in exceptions:
		return
	URLValidator()(value)
```

---
## Similar field classes:
- CharField: [/python/web-development/django/3-1-models-database/model-attr-field-char](/python/web-development/django/3-1-models-database/model-attr-field-char.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

