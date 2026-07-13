#### Python > Django > Models
# Attribute type: IntegerField

---

**Typical Size:**

4 bytes (32-bit)

**Signed Range:**

-2,147,483,648 to 2,147,483,647

**Common usage:**

General-purpose integers where the value is unlikely to exceed 2 billion. Examples: counts (e.g., page_views, likes), ages, small system IDs, choices from a limited set, and ForeignKey fields (on databases that use integer-based keys).

E.g. in *models.py*:
```
class Product(...):
	...
    quantity = models.IntegerField(default=0)
    ...
```

**Common *IntegerField* options:**

- default=0 ....................................... Default value.
- null=True	........................................ Allows NULL in the database.
- blank=True ..................................... Allows the field to be left empty in forms.
- validators=[...] ................................ Restricts allowed values.
- choices= .......................................... Limits the field to predefined integer values.
- db_index=True ............................... Creates a database index for faster lookups.

---
## More examples:

With validation:
```
# models.py:

from django.core.validators import MinValueValidator, MaxValueValidator

class Student(...):
    ...
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(120),
        ]
    )
    ...
```
Example using *choices*:
```
# models.py

class Order(...):
    STATUS_PENDING = 1
    STATUS_PROCESSING = 2
    STATUS_COMPLETED = 3

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_COMPLETED, "Completed"),
    ]

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
```

---
## Other related options:

- Big Integer Field: [/python/web-development/django/3-1-models-database/model-attr-field-bigInteger](/python/web-development/django/3-1-models-database/model-attr-field-bigInteger.md)


