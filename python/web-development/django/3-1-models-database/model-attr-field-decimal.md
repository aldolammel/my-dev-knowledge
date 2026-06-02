#### Python > Django > Models > Attribute types
# DecimalField()

---

Financial data, monetary values, or any number where exact decimal representation is required. You must define max_digits (the total number of digits) and decimal_places (the digits after the decimal point). For storing numbers with decimal points, like *FloatField*, but with differences!!! Fixed-point numbers.

Typical Size:
Variable (configurable)

Signed Range:
Configurable, with exact precision.

E.g.
```
from decimal import Decimal
from django.core.validators import MinValueValidator

# Can store up to 999.999.
models.DecimalField(
	max_digits=6,      # 000.000
	decimal_places=3,  # .000
	validators=[
		MinValueValidator(Decimal('0.001'))
			# Using Decimal('0.001') instead of 0.001 (float) ensures proper decimal precision matching and allows 0.001 to pass validation correctly!!!
	]
)
```

---
## Other related options:
- FloatField: [python/web-development/django/3-1-models-database/model-attr-field-float](python/web-development/django/3-1-models-database/model-attr-field-float.md)
