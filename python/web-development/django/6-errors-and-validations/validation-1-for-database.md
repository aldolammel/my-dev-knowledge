#### Python > Django > Validations
# Validations for database-level (db constraints)

---
## Before:
- What is db constraints: [/database/_basic-concepts/constraint-for-db](/database/_basic-concepts/constraint-for-db.md)

---

When a form field needs a basic validation as well as *maximum length* or *it cannot be empty*, you need database level validation, also called *database constraints*. As we are talking about validations direct for database (via Django), we are restrict a not complex options, and NONE of them will force Django to propagate that rules for other levels/layers of your app.

---
## In `models.py`:
So, you must have it in mind that's just the first, basic and deepest validation level you will dive in your project. DB constraints are set via `/apps/your_subapp/models.py` file:
### Very basic constraints
These ones you define as argument through attributes of a class:
```python
class ExampleModel(models.Model):
	attribute_example_1 = models.CharField(
		# ...
		max_length=100,            # db level validation.
		blank=False,               # db level validation.
		unique=True,               # db level validation.
		null=False,                # db level validation.

		validators=[...]           # More options, but only for APP level.
	)
	attribute_example_2 = models.DecimalField(
		# ...
		max_digits=5,  # 999.99    # db level validation.
		decimal_places=2,  # .99   # db level validation.
		# ...
		validators=[...]           # More options, but only for APP level.
	)
```
### Meta constraints
E.g. Using a `CheckConstraint()` db constraints to be more specific (e.g., supported by PostgreSQL, MySQL):
```python
from django.db.models.functions import Length
models.CharField.register_lookup(Length)

class Product(models.Model):
	name = models.CharField(...)
	# ...

	class Meta:
		# ...
		constraints = [
			models.CheckConstraint(
				condition=models.Q(
					name__length__range=(
						consts.INT_GENERIC_MIN,
						consts.INT_GENERIC_MAX
					)
				),
				name="product_name_length",  # If this constraint looks only to the minimum length, the name could be more specific like "product_name_min_length".
			),
		]
```
Other example:
```python
from django.db.models.functions import Lower

class Something(...):
	email = ...
	
	class Meta:
		# ...
		constraints = [
			models.UniqueConstraint(
				Lower("email"),
				name="user_unique_email_lowered",
			),
		]
```
==Critical!==
For all validations above to run correctly, your model `save()` method must manually invoke the `self.full_clean`: [/python/web-development/django/3-1-models-database/method-save](/python/web-development/django/3-1-models-database/method-save.md)

---
## Exploring db constraint possibilities:
Make sure your DB supports:
- [/python/web-development/django/6-errors-and-validations/validation-constraint-text-length](/python/web-development/django/6-errors-and-validations/validation-constraint-text-length.md)
- [/python/web-development/django/6-errors-and-validations/validation-constraint-numerical-logics](/python/web-development/django/6-errors-and-validations/validation-constraint-numerical-logics.md)
- [/python/web-development/django/6-errors-and-validations/validation-constraint-date-logics](/python/web-development/django/6-errors-and-validations/validation-constraint-date-logics.md)
- [/python/web-development/django/6-errors-and-validations/validation-constraint-conditionals](/python/web-development/django/6-errors-and-validations/validation-constraint-conditionals.md)
- [/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness](/python/web-development/django/6-errors-and-validations/validation-constraint-uniqueness.md)

---
## About Model `clean()` method:
If you are thinking to use Model `clean()` method to validate database, remember: `clean()` method is used just to custom validates in app-level, never in db-level: [/python/web-development/django/3-1-models-database/method-clean](/python/web-development/django/3-1-models-database/method-clean.md)

---
## Other validation levels:
[/python/web-development/django/6-errors-and-validations/1-validation-basic](/python/web-development/django/6-errors-and-validations/1-validation-basic.md)

