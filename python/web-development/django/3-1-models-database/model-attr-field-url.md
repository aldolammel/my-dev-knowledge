#### Python > Django > Models > Attribute types
# URLField()

---

A specialized *CharField* for storing URLs. It includes URL format validation in *Django forms*.

**Field look-like on front-end:**
- Single field with simple URL validation.

E.g.

Basic:
```
url = models.URLField(
	max_length=255,
	blank=True,  # Even if you set validators, blank=True will ignore any validator set for this attribute! Be aware!
	# validators=[URLValidator()],  # Not need for URLField!
)
```
Basic > Case blank false:
```
url = models.URLField(
	...
	blank=False,
	default="",  # or None. It's demanded if blank=False or null=False!
)
```
Basic > Forcing the field do not its built-in validator's validation:
```
url = models.URLField(
	...
	blank=False,
	default="",
	validators=[URLValidator()],  # This will overriden original validators for this field and nothing will be validated here!
)
```

---

## Other related options:
- CharField: [python/web-development/django/3-1-models-database/model-attr-field-char](python/web-development/django/3-1-models-database/model-attr-field-char.md)

