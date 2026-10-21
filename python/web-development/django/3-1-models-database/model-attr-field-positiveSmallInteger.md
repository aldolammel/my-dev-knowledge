#### Python > Django > Models > Field Classes (Attribute types)
# PositiveSmallIntegerField()

---

The ideal choice for storing small, non-negative integers where saving space is a priority. Perfect for fields with a known, limited positive range like human age, quantity in stock, days until expiration, seats in a theater.

Typical Size:
2 bytes (16-bit)

Signed Range:
0 to 32,767 (It uses the same 2-byte storage as SmallIntegerField but restricts values to positive numbers and zero, enforced by Django).

E.g.
```python
pos_on_menu = models.PositiveSmallIntegerField(
	default=0,
	blank=True,
	verbose_name="xxxxxx",
	help_text="",
)
```
Using `choices` argument:
```python
class Something(...):
    # Recommended to set this in app's consts.py:
    STATUS_CHOICES = [
        (1, "Pending"),
        (2, "Active"),
        (3, "Completed"),
    ]
    # Using the choices argument in a class attribute:
    status = models.PositiveSmallIntegerField(
	    choices=STATUS_CHOICES,
	    # default=1,  # Uncomment it if you wanna force a default value (already selected).
	    null=True,
	    blank=False,
	    verbose_name="xxxxxxxxx",
		help_text="",
	)
```

---
## Similar field classes:
Small Integer: [/python/web-development/django/3-1-models-database/model-attr-field-smallInteger](/python/web-development/django/3-1-models-database/model-attr-field-smallInteger.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)
